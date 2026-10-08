"""Generate docs/reference/cli-settings.md from the Rotorflight firmware source.

Reads src/main/cli/settings.c, settings.h and fc/parameter_names.h straight
from a git ref of a rotorflight-firmware checkout, so the list always matches
the firmware it was generated from.

Usage:
    python tools/gen_cli_settings.py <rotorflight-firmware checkout> [git ref]

The ref defaults to upstream/master. Re-run after each firmware release and
commit the result.
"""
import os
import re
import subprocess
import sys

repo = sys.argv[1]
ref = sys.argv[2] if len(sys.argv) > 2 else "upstream/master"
out = os.path.join(os.path.dirname(__file__), "..", "docs", "reference", "cli-settings.md")


def show(path):
    return subprocess.run(["git", "-C", repo, "show", f"{ref}:{path}"],
                          capture_output=True, text=True, encoding="utf-8", check=True).stdout


settings_c = show("src/main/cli/settings.c")
settings_h = show("src/main/cli/settings.h")
param_names = dict(re.findall(r'#define\s+(PARAM_NAME_[A-Z0-9_]+)\s+"([a-z0-9_]+)"',
                              show("src/main/fc/parameter_names.h")))
version = subprocess.run(["git", "-C", repo, "describe", "--tags", "--always", ref],
                         capture_output=True, text=True).stdout.strip()

# Lookup tables: the TABLE_* enum and lookupTables[] are in the same order.
enum_body = re.search(r"typedef enum \{\s*TABLE_OFF_ON = 0,(.*?)LOOKUP_TABLE_COUNT", settings_h, re.S).group(1)
table_ids = ["TABLE_OFF_ON"] + re.findall(r"\b(TABLE_[A-Z0-9_]+)\s*,", enum_body)
table_arrays = re.findall(r"^\s*LOOKUP_TABLE_ENTRY\((\w+)\)", settings_c, re.M)


def find_array(arr):
    """The string array's initialiser -- in settings.c, or elsewhere in src/main."""
    m = re.search(rf"{arr}\[[^\]]*\]\s*=\s*\{{(.*?)\}};", settings_c, re.S)
    if m:
        return m
    hits = subprocess.run(["git", "-C", repo, "grep", "-l", "-F", f"{arr}[", ref, "--", "src/main"],
                          capture_output=True, text=True).stdout.split()
    for hit in hits:
        m = re.search(rf"{arr}\[[^\]]*\]\s*=\s*\{{(.*?)\}};", show(hit.split(":", 1)[1]), re.S)
        if m:
            return m
    return None


table_values = {}
for tid, arr in zip(table_ids, table_arrays):
    m = find_array(arr)
    if m:
        body = re.sub(r"//.*", "", m.group(1))
        body = re.sub(r"^\s*#.*$", "", body, flags=re.M)
        # Most tables are string literals; debug modes use DEBUG_NAME(X).
        table_values[tid] = re.findall(r'"([^"]*)"', body) or re.findall(r"DEBUG_NAME\((\w+)\)", body)

SECTION = {"MASTER_VALUE": "Global", "HARDWARE_VALUE": "Hardware",
           "PROFILE_VALUE": "PID profile", "PROFILE_RATE_VALUE": "Rate profile"}
TYPES = {"VAR_UINT8": "uint8", "VAR_INT8": "int8", "VAR_UINT16": "uint16",
         "VAR_INT16": "int16", "VAR_UINT32": "uint32", "VAR_INT32": "int32"}

ACRONYMS = {w.title(): w for w in [
    "ADC", "PID", "GPS", "RX", "ESC", "OSD", "VTX", "LED", "MSP", "SPI", "USB", "RC",
    "CRSF", "FBUS", "SBUS", "RPM", "MCO", "I2C", "SDIO", "PWM", "CMS", "RTC", "VCD", "MAX7456",
]}
ACRONYMS.update({"Sdcard": "SD card", "Ledstrip": "LED strip", "Pinio": "PINIO", "Pinioboxes": "PINIO boxes"})

entries = []
for line in settings_c.splitlines():
    m = re.match(r'\s*\{\s*(?:"([a-z0-9_]+)"|(PARAM_NAME_[A-Z0-9_]+))\s*,\s*(VAR_[A-Z0-9]+)\s*\|\s*([A-Z_]+)'
                 r'(?:\s*\|\s*(MODE_[A-Z]+))?\s*,\s*(.*)\},?\s*(?://.*)?$', line)
    if not m:
        continue
    name = m.group(1) or param_names.get(m.group(2))
    if not name:
        continue
    vtype, section, mode, rest = m.group(3), m.group(4), m.group(5) or "MODE_DIRECT", m.group(6)
    pg = re.search(r"\b(PG_[A-Z0-9_]+)", rest)
    pg = pg.group(1) if pg else ""
    if mode == "MODE_LOOKUP":
        t = re.search(r"lookup\s*=\s*\{\s*(TABLE_[A-Z0-9_]+)", rest)
        vals = table_values.get(t.group(1)) if t else None
        values = " ".join(f"`{v}`" for v in vals) if vals else (t.group(1) if t else "")
    elif mode == "MODE_ARRAY":
        n = re.search(r"array\.length\s*=\s*([\w ]+)", rest)
        values = f"array of {n.group(1).strip()} values" if n else "array"
    elif mode == "MODE_BITSET":
        values = "`OFF` `ON`"
    elif mode == "MODE_STRING":
        s = re.search(r"string\s*=\s*\{\s*([^,]+),\s*([^,}]+)", rest)
        values = f"text, {s.group(1).strip()}-{s.group(2).strip()} characters" if s else "text"
    else:
        r = re.search(r"minmax(?:Unsigned)?\s*=\s*\{\s*([^,]+?)\s*,\s*([^}]+?)\s*\}", rest) \
            or re.search(r"u32Max\s*=\s*([^,}]+)", rest)
        if r and r.lastindex == 2:
            values = f"{r.group(1)} .. {r.group(2)}"
        elif r:
            values = f"0 .. {r.group(1).strip()}"
        else:
            values = ""
    group = pg.replace("PG_", "").replace("_CONFIG", "").replace("_PROFILE", "").replace("_", " ").title()
    group = " ".join(ACRONYMS.get(w, w) for w in group.split())
    entries.append((SECTION.get(section, section), group, name, TYPES.get(vtype, vtype), values))

lines = [
    "# CLI Settings",
    "",
    "Every setting the firmware accepts with `set`, generated from the firmware",
    f"source (`{version}`). For what the important ones do, see the",
    "[CLI Reference](cli-reference.md) and the [Configurator](../configurator/index.md) pages.",
    "",
    "- **Global** and **Hardware** settings apply to the whole flight controller.",
    "- **PID profile** settings belong to the current PID profile; switch with `profile <n>` first.",
    "- **Rate profile** settings belong to the current rate profile; switch with `rateprofile <n>` first.",
    "",
    "Ranges are the raw values stored by the firmware -- many are scaled for display in the",
    "Configurator (for example tenths of a second, or percent × 10). Some settings only exist",
    "in firmware built with the matching feature.",
    "",
    "<!-- Generated by tools/gen_cli_settings.py. Do not edit by hand. -->",
    "",
]
for section in ["Global", "PID profile", "Rate profile", "Hardware"]:
    rows = [e for e in entries if e[0] == section]
    if not rows:
        continue
    lines += [f"## {section}", ""]
    for group in sorted({e[1] for e in rows}):
        lines += [f"### {group}", "", "| Setting | Type | Values |", "| --- | --- | --- |"]
        for _, _, name, vtype, values in sorted((e for e in rows if e[1] == group), key=lambda e: e[2]):
            lines.append(f"| `{name}` | {vtype} | {values} |")
        lines.append("")

with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines))
print(f"wrote {len(entries)} settings to {os.path.normpath(out)}")

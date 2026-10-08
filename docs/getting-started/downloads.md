# Downloads

Every Rotorflight component is released together under one version number.
The firmware, Configurator and Lua scripts must be from the same release:
the Configurator and the radio scripts talk to the firmware over MSP, and a
mismatched pair can refuse to connect or show the wrong settings.

!!! warning "Keep everything on the same version"
    When you update the firmware, update the Configurator and the Lua suite
    on your radio as well.

## Configurator

The Configurator flashes the firmware and configures the flight controller.

=== "Web (no install)"

    Open **[cfg.rotorflight.org](https://cfg.rotorflight.org)** in a
    Chromium-based browser (Chrome, Edge, Brave or Opera). It talks to the
    flight controller over USB using the browser's Web Serial and WebUSB
    support, so there is nothing to install. Firefox and Safari do not
    support Web Serial and cannot connect.

    The landing page lists every available build: the current release,
    older releases, and the `master` development build.

=== "Desktop"

    Desktop builds are on the
    [Configurator releases page](https://github.com/rotorflight/rotorflight-configurator/releases/latest):

    | Platform | File |
    | --- | --- |
    | Windows | `rotorflight-configurator-installer_<version>_x86_64.exe` (or the `.zip` for a portable install) |
    | macOS (Apple silicon) | `rotorflight-configurator_<version>_macos_arm64.dmg` |
    | macOS (Intel) | `rotorflight-configurator_<version>_macos_x86_64.dmg` |
    | Linux | `.deb`, `.rpm` or `.tar.xz` |
    | Android | `rotorflight-configurator_<version>_android.apk` |

    On Windows you may also need the USB drivers described in
    [Flashing the Firmware](flashing-the-firmware.md#usb-drivers).

## Blackbox Explorer

The Blackbox Explorer opens flight logs recorded by the flight controller.
Use it in the browser at
**[blackbox.rotorflight.org](https://blackbox.rotorflight.org)**, or install
it from the
[Blackbox releases page](https://github.com/rotorflight/rotorflight-blackbox/releases/latest).

## Radio Lua suites

The Lua suites run on your radio. They configure and tune the flight
controller over the telemetry link, and add dashboards and voice callouts.

| Radio | Suite | Download |
| --- | --- | --- |
| FrSky Ethos | Rotorflight Lua Ethos Suite | [Releases](https://github.com/rotorflight/rotorflight-lua-ethos-suite/releases/latest), or the [Ethos Suite Updater](https://github.com/rotorflight/rotorflight-lua-ethos-suite-updater/releases) |
| EdgeTX 2.11+ (colour screen, CRSF/ELRS) | RFSuite for EdgeTX | [Releases](https://github.com/rotorflight/rotorflight-lua-edgetx-suite/releases), or the [EdgeTX Suite Updater](https://github.com/rotorflight/rotorflight-lua-edgetx-suite-updater/releases) |
| EdgeTX / OpenTX (older or black-and-white radios) | Classic Lua scripts | [Releases](https://github.com/rotorflight/rotorflight-lua-scripts/releases/latest) |

The updaters are desktop apps that detect the radio over USB, download the
release in your language and install it while keeping your settings. See
[Radio & Lua](../radio/index.md) for setup.

## Firmware

You don't normally download firmware by hand: the Configurator's
[Firmware Flasher](flashing-the-firmware.md) fetches the right build for
your board. The raw files are on the
[firmware releases page](https://github.com/rotorflight/rotorflight-firmware/releases/latest)
if you need them.

## Releases and snapshots

| Type | Tag | Use it for |
| --- | --- | --- |
| **Release** | `release/2.3.0` | Normal flying. Release candidates (`-RC1`, `-RC2` ...) come first, for wider testing. |
| **Snapshot** | `snapshot/...` | Development builds for testers. They can contain bugs and break configurations -- only fly them if you are helping to test. |

Release notes for each version are on the GitHub releases pages. The
[Upgrade Notes](upgrade-notes.md) list what you have to redo when moving
between major versions.

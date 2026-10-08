# Ethos Troubleshooting

## The tool can't connect

- Is the helicopter powered and the receiver bound? The radio must show
  telemetry (signal bars, and live sensors under **Model → Telemetry**).
- With an FrSky receiver on SBUS only, there's no telemetry -- use F.Bus or
  F.Port, or add S.Port.
- On the flight controller, telemetry must be enabled on the
  [Receiver](../../configurator/tabs/receiver.md#telemetry) tab.
- With ExpressLRS, the packet rate and telemetry ratio must match on the
  module and the flight controller.
- The suite and the firmware must be from the same release.

## Background task not running

The dashboard shows this when the **Rotorflight [Background]** Lua task
isn't running. Press **MDL**, open the **Lua** page, and enable it.

## Missing sensors

RFSuite needs particular telemetry sensors from the flight controller. If
some are missing it says so.

1. Open the tool: **SYS → Rotorflight → Setup → Telemetry**.
2. Press the **Default** button at the top to select the suite's sensors,
   then **Save**. The suite writes them to the flight controller, which
   restarts.
3. On the radio, **Model → Telemetry**: delete all sensors, then discover
   them again.
4. Restart the radio to clear cached values.

**Tools → Diagnostics → Status** shows the connection and sensor state.

You can also choose the sensors on the Configurator's
[Receiver](../../configurator/tabs/receiver.md#telemetry-sensors) tab, or
apply the *Set telemetry sensors for RFsuite on Ethos* preset from the
[Presets](../../configurator/tabs/presets.md) tab.

## Settings didn't stick

Changes are only written when you press **Save** on the page. Pages are
read-only while armed.

## Reporting a problem

Ask on the [Rotorflight Discord](https://discord.gg/FyfMF4RwSA), or open
an issue on the
[RFSuite repository](https://github.com/rotorflight/rotorflight-lua-ethos-suite/issues),
with your Ethos version, radio, receiver and suite version.

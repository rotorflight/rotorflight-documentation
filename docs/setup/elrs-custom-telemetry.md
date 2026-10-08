# ELRS Custom Telemetry

ExpressLRS uses the Crossfire (CRSF) protocol, whose standard telemetry has
room for only a few values, mostly aimed at multirotors -- no headspeed, no
governor state, no ESC temperature. Rotorflight's **custom telemetry** sends
its own sensors over the same link instead: more than 100 to choose from,
up to 40 at once, updated up to 20 times a second.

The radio needs a script to decode the custom frames. The current Lua
suites do this themselves:

| Radio | Decoder |
| --- | --- |
| FrSky Ethos | The [Rotorflight Lua suite](../radio/ethos/lua-suite.md)'s background task. |
| EdgeTX (colour, 2.11+) | [RFSuite](../radio/edgetx/lua-suite.md) -- its widgets, or its background decoder. |
| Older EdgeTX / OpenTX | The `rf2tlm.lua` script from the [classic Lua scripts](https://github.com/rotorflight/rotorflight-lua-scripts/releases), run as a custom script. |

!!! danger "Use ExpressLRS 3.5.5 or later"
    ELRS before 3.5.5 has a bug that can cause loss of control when
    telemetry is busy. Update your transmitter module and receiver.

## 1. Flight controller

On the [Receiver](../configurator/tabs/receiver.md#telemetry) tab:

1. **Telemetry: Enable** -- on.
2. **Custom Telemetry** -- on.
3. **Telemetry Packet Rate** -- the same as the ELRS *Packet Rate* on your
   transmitter module (e.g. 500 Hz).
4. **Telemetry Packet Ratio** -- the same as the ELRS *Telem Ratio* (e.g.
   1:4 → 4). Start at 4; if the radio reports *telemetry lost*, go higher
   (up to 16).
5. Choose the sensors under **Telemetry Sensors**, then **Save**.

!!! tip "Let the suite choose"
    Saving the Telemetry page in the Ethos or EdgeTX suite picks sensors for
    its dashboards and switches the flight controller to Custom mode for
    you. There are also presets on the [Presets](../configurator/tabs/presets.md)
    tab.

## 2. Radio

1. Set the ELRS module's **Packet Rate** and **Telem Ratio** to match step 1.
2. Install and enable the decoder for your radio (table above). On Ethos,
   enable the Rotorflight background task; on EdgeTX with RFSuite, either a
   dashboard widget or the background decoder must be running.
3. **Discover sensors**: delete the existing telemetry sensors on the radio,
   start **Discover new**, and only then power up the helicopter. Powering
   up first can leave the sensors in the wrong order.

## Troubleshooting

| Problem | Try |
| --- | --- |
| *Telemetry lost* warnings | Raise the telemetry ratio (on both module and flight controller). |
| A sensor never appears, and others stop updating | The suite doesn't know a sensor the firmware sends -- update the suite, or untick that sensor. An unknown sensor stops the decoder reading the rest of its frame. |
| Sensors in the wrong order, or duplicated | Delete all sensors and discover again, with the helicopter powered up *after* discovery starts. |

See [Telemetry Sensors](../reference/telemetry.md) for the full sensor list.

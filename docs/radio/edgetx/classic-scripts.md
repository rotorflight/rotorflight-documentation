# Classic Lua Scripts

The classic Rotorflight Lua scripts run on OpenTX and EdgeTX radios that
can't run RFSuite -- black-and-white radios, older firmware, or links other
than CRSF.

## Requirements

- **OpenTX 2.3.12** or **EdgeTX 2.5.0** or newer.
- A receiver with telemetry: FrSky S.Port or F.Port, Crossfire (CRSF 2.11+),
  or ExpressLRS (3.5.5+ recommended).

For example a TX16S with ExpressLRS, or a QX7 with an FrSky R-XSR.

## Installing

1. Download the release matching your firmware from
   [rotorflight-lua-scripts](https://github.com/rotorflight/rotorflight-lua-scripts/releases/latest).
2. Copy the contents of its `SCRIPTS` folder to the radio's SD card.
3. `rf2.lua` should now be in `/SCRIPTS/TOOLS`, and **Rotorflight 2**
   in the radio's **Tools** menu.

## Using them

1. Enable telemetry on the flight controller's
   [Receiver](../../configurator/tabs/receiver.md#telemetry) tab, and
   discover the sensors on the radio.
2. Open **Rotorflight 2** from **Tools**. The first start compiles the
   scripts and returns to the Tools menu; open it again.
3. Power up the helicopter. Once the scripts have read the firmware version,
   the main menu appears.

Browse freely: nothing is changed until you **Save** -- the Save button on
colour radios, or a long press of the wheel then *Save* on black-and-white
radios.

Useful pages:

- **Status** -- the arming disable flags.
- **Battery** -- up to six battery profiles, and which pack you're flying.
- **Model** -- timers and other settings stored on the flight controller,
  so one radio model can fly several helicopters.
- **Settings** -- which pages appear in the menu.

## Background script

The optional background script `rf2bg.lua` adds:

- **Clock sync** -- sends the radio's time to the flight controller, so
  Blackbox logs get real timestamps (it beeps when done);
- **ELRS custom telemetry** decoding -- see
  [ELRS Custom Telemetry](../../setup/elrs-custom-telemetry.md);
- the **Adjustment Teller** -- announces each in-flight adjustment.

Run it either through the **RF Tool** widget (EdgeTX colour radios), or as
a special or global function in the radio.

## Widgets

The **RF Tool** widget exposes an API for other widgets to read flight
controller data -- see the
[RF Tool API](https://github.com/rotorflight/rotorflight-lua-scripts) in the
scripts repository. Bob00's
[ETX widgets](https://github.com/bob01/etx-widgets) are a popular
third-party telemetry display.

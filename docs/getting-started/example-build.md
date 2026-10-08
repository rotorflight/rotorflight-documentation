# Example Build

A complete setup of a small electric helicopter, from a fresh flight
controller to the first hover. It links to the detailed pages as it goes;
follow the same order for your own helicopter.

| | This example |
| --- | --- |
| Helicopter | OMPHobby M4, servo tail |
| Flight controller | Radiomaster Nexus |
| Receiver | ExpressLRS |
| ESC | OMPHobby 65A |
| RPM | ESC RPM wire to the Nexus RPM port |
| Radio | Any Ethos or EdgeTX radio with the Rotorflight Lua suite |

!!! danger "Blades off"
    Leave the main and tail blades off until step 12.

## 1. Firmware

[Flash](flashing-the-firmware.md) the latest release, choosing the Nexus
board, with **Full chip erase**. [Connect](first-connection.md).

## 2. Receiver

The Nexus has a dedicated ELRS port (Port A).

!!! warning
    Check the receiver lead's pin order against both ends before powering
    up. Some ELRS receivers use a different pin layout, and a wrong lead
    can damage the receiver.

1. [Configuration](../configurator/tabs/configuration.md#serial-ports) tab:
   set **Port A** to **Serial Rx**. Save and reboot.
2. [Receiver](../configurator/tabs/receiver.md) tab: **TBS CRSF** protocol,
   **ELRS** channel preset. Save and reboot.
3. Move every stick and switch and check the bars follow -- right way round.
4. Turn on **Telemetry** and **Custom Telemetry** -- see
   [ELRS Custom Telemetry](../setup/elrs-custom-telemetry.md).

To update the receiver's firmware later, use the ExpressLRS Configurator's
*Betaflight passthrough* with the Rotorflight Configurator closed.

## 3. Arm switch

Put the arm switch on channel 5 (AUX 1) and add the **ARM** mode on the
[Modes](../configurator/tabs/modes.md) tab. See [Arming & Safety](arming.md).

## 4. Orientation and accelerometer

1. Tilt and turn the helicopter: the 3D model on the Status tab must move the
   same way. If not, set the board orientation on the
   [Configuration](../configurator/tabs/configuration.md#board-and-sensor-alignment)
   tab.
2. Stand the helicopter level and
   [calibrate the accelerometer](../configurator/tabs/setup.md#calibrate-accelerometer).

## 5. Servos

The M4 uses **CCPM 120°**. Plug the servos in as the diagram on the
[Servos](../configurator/tabs/servos.md) tab shows, and follow
[Servo Setup](../setup/servos.md): rate and centre first, then directions,
then centring.

## 6. Mixer

Follow [Mixer & Swashplate Setup](../setup/mixer.md): directions, level
swashplate, zero pitch, collective and cyclic calibration, limits, tail.

## 7. Motor and ESC

On the [Motors](../configurator/tabs/motors.md) tab:

| Setting | Value |
| --- | --- |
| Throttle Protocol | PWM |
| Telemetry Protocol | OMPHOBBY (ESC telemetry wire to a UART set to *ESC Telemetry*) |
| RPM Sensor | On -- the ESC's RPM wire is on the Nexus RPM port |
| Main Rotor Gear Ratio | From the M4's specifications |
| Tail Rotor Gear Ratio | From the M4's specifications |
| Main Motor Pole Count | From the motor's specifications |

See [RPM Measurement](../setup/rpm-measurement.md) and
[ESC Telemetry](../setup/esc-telemetry.md). Calibrate the ESC's throttle
range if its manual asks for it.

## 8. Test the motor and telemetry

**Blades off.** Enable **Throttle Override** and raise it slowly. The motor
spins, and the Motors tab shows RPM, voltage, current and temperature from
the ESC. Check the rotor speed is plausible.

## 9. Power

With ESC telemetry working, set the **Battery Voltage Source** and
**Battery Current Source** to **ESC** on the
[Power](../configurator/tabs/power.md) tab, fill in the battery profile, and
turn on [SmartFuel](../setup/smartfuel.md).

## 10. Governor and RPM filter

1. [Governor Setup](../setup/governor-setup.md): ELECTRIC mode, full
   headspeed in the profile.
2. [RPM Filters](../setup/rpm-filters.md): enable on the Gyro tab, Medium
   strength.

## 11. Rates, radio and backup

1. Set the [Rates](../configurator/tabs/rates.md) to taste.
2. Install the [Lua suite](../radio/index.md) on your radio.
3. Check the [failsafe](../configurator/tabs/failsafe.md): blades off, armed
   and spinning, switch the radio off -- the motor must stop.
4. Take a [backup](backup-and-restore.md).

## 12. Pre-flight checks

With the blades on, before the first flight:

- Stick right → swashplate tilts right. Stick forward → tilts forward.
  Collective up → pitch increases. Rudder right → nose yaws right.
- **Gyro direction:** tilt the helicopter nose down by hand while armed (at
  idle, blades held) -- the swashplate must tilt *back* to resist. Repeat for
  roll and yaw.
- Throttle hold works, and the arm switch is where you expect it.

Then spool up, lift into a hover, and see [Tuning](../tuning/index.md).

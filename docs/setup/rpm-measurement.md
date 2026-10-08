# RPM Measurement

The flight controller needs to know how fast the motor is turning for two of
Rotorflight's most important features:

- the **[governor](governor.md)**, which holds the headspeed constant, and
- the **[RPM filter](rpm-filters.md)**, which removes rotor and motor
  vibration from the gyro.

Both need a fast, live RPM signal. There are two ways to get one.

| Method | Use it with |
| --- | --- |
| **RPM sensor input** | Traditional helicopter ESCs with an RPM output wire, or a separate RPM sensor. Also nitro engines with a magnetic sensor. |
| **Bidirectional DShot** | Multirotor-style ESCs running AM32, Bluejay or BLHeli_32 (32.7+). |

!!! warning "Serial ESC telemetry isn't fast enough"
    Most ESCs also report RPM in their [serial telemetry](esc-telemetry.md),
    but it only updates a few times a second -- too slow for the governor or
    the filters. Use it for display only.

=== "RPM sensor input"

    Many helicopter ESCs have an RPM output -- Hobbywing's yellow wire, for
    example. Otherwise, an RPM sensor (such as Hobbywing's) clips onto two
    of the motor wires and produces the signal.

    1. Connect the RPM signal to the flight controller's frequency input,
       usually labelled **RPM**. Betaflight boards need one
       [remapped](remapping.md).
    2. On the [Motors](../configurator/tabs/motors.md#rpm) tab, turn on
       **RPM Sensor**.
    3. Enter the **gear ratios** and the **Main Motor Pole Count**.

    !!! warning "Power an RPM sensor from 3.3 V"
        A sensor's output swings up to its supply voltage. Every flight
        controller input tolerates 3.3 V; only some tolerate 5 V, and none
        an 8 V BEC. Power external RPM sensors from 3.3 V where you can.

    Up to two frequency inputs are supported -- the second for a motorised
    tail. If both an RPM input and telemetry RPM are present, the RPM input
    wins.

=== "Bidirectional DShot"

    The ESC sends the RPM back on the throttle wire.

    1. Make sure the ESC firmware supports it: AM32, Bluejay, or BLHeli_32
       32.7 or later. BLHeli_S doesn't -- [flash it to Bluejay](blheli-s-to-bluejay.md).
    2. On the [Motors](../configurator/tabs/motors.md) tab, set **Throttle
       Protocol** to **DSHOT300** and turn on **Dshot RPM Telemetry**.
    3. Enter the **gear ratios** and the **Main Motor Pole Count**.

    The Motors tab shows a **DShot RPM Error Rate**; it should stay close to
    zero.

## Gear ratios and pole count

The flight controller measures *motor* RPM. To know the rotor speeds it
needs:

- **Main Motor Pole Count** -- the number of magnets in the motor's bell
  (not the stator teeth). It's in the motor's specifications, or count them.
  Since 2.3 this defaults to 0, which turns RPM measurement off until you
  set it.
- **Main Rotor Gear Ratio** -- pinion teeth : main gear teeth, e.g.
  `12 : 120`. For a two-stage gearbox see [Gear Ratios](gear-ratios.md).
- **Tail Rotor Gear Ratio** -- tail rotor turns per main rotor turn, as
  tail : main. For a torque tube, the tail gear : autorotation gear teeth;
  for a belt, the tail pulley : front pulley.

## Checking it

With the blades off, spin up gently with the
[Throttle Override](../configurator/tabs/motors.md#throttle-override) and
compare the **Rotor Speed** shown on the Motors tab with an optical
tachometer, or with the headspeed your ESC or radio reports. If it's out by
a constant factor, the pole count or a gear ratio is wrong.

!!! note "Autorotations and overspeed"
    The RPM measured is the *motor's*. With a one-way bearing, the rotor can
    turn faster than the motor -- in an autorotation, or in a steep descent
    with the governor easing off. The RPM filter then tracks the wrong
    frequencies for a moment. A tune pushed right to the edge can show some
    oscillation there; leave a little margin.

# Governor Setup

A walk-through for an electric helicopter. For nitro, see
[Nitro Helicopters](nitro.md). Read [Governor](governor.md) first if the
terms are new.

!!! danger "Blades off"
    Do all of this with the main and tail blades removed until the final
    test.

## Before you start

- [RPM measurement](rpm-measurement.md) works, with the right gear ratios
  and pole count: the Motors tab shows a sensible rotor speed.
- The ESC is in **fixed-wing / external governor** mode -- its own
  governor *off* -- so it follows the throttle signal directly. (Some ESCs
  call this *linear throttle* or, on FlyRotor, *RF Gyro Governor*.)
- The ESC's throttle range is calibrated to the flight controller's **Low
  Throttle** and **High Throttle** on the [Motors](../configurator/tabs/motors.md#throttle-range)
  tab, so 0% is just below motor start and 100% is full power.

## 1. Global settings -- Governor tab

On the [Governor](../configurator/tabs/governor.md) tab:

1. **Governor Mode**: ELECTRIC.
2. **Throttle Type**: NORMAL for throttle on a switch, SWITCH for several
   headspeeds on one switch, FUNCTION for ExpressLRS switch channels.
3. **Handover Throttle**: the default 20% is fine for most ESCs. The motor
   must start below it.
4. **Spoolup Time**: about 10 s for a gentle spoolup on a large helicopter;
   shorter for small ones.
5. **Throttle Hold Timeout** and **Autorotation Timeout** if you want those
   features.

**Save and Reboot.**

## 2. Headspeed -- Profiles tab

On the [Profiles](../configurator/tabs/profiles.md#governor-settings) tab,
set **Full Headspeed** to the headspeed at 100% throttle input. Leave the
gains at their defaults for now.

!!! tip "What headspeed?"
    Use the helicopter manufacturer's recommendation. The governor needs
    about 15-25% of throttle in reserve to hold the headspeed under load: if
    the throttle sits near 100% in a hover, the headspeed is too high for
    the motor, battery and pinion.

## 3. Throttle on the radio

Rotorflight needs a separate **throttle** channel (not mixed with
collective) and a **throttle hold**.

=== "Several headspeeds from the throttle"

    One profile, **Full Headspeed** set to your highest headspeed. The radio
    sends a different throttle value for each flight mode:

    | Switch position | Throttle | Headspeed (Full = 2500) |
    | --- | :-: | --- |
    | Throttle hold | stop (below 0%) | motor off |
    | Idle up 1 | 70% | 1750 rpm |
    | Idle up 2 | 90% | 2250 rpm |
    | Idle up 3 | 100% | 2500 rpm |

    Simple: one tune covers all headspeeds.

=== "One headspeed per profile"

    The throttle is either stop (hold) or 100%. A 3-position switch selects
    a **profile** through an [adjustment](../configurator/tabs/adjustments.md),
    and each profile has its own **Full Headspeed** -- and its own tune. See
    [Profile Switching](profile-switching.md).

## 4. Test

1. Blades off. Arm, release throttle hold.
2. The motor should spool up gently and settle at the target headspeed --
   watch the Motors tab or the headspeed on your radio.
3. Flick throttle hold on and off quickly: it should recover fast.
4. Fit the blades and do the same in a hover. The headspeed should stay
   steady through collective pumps.

If the headspeed surges or hunts, or drops under load, see
[Governor Tuning](../tuning/governor.md).

## ESC notes

### FlyRotor

- In the FlyRotor ESC Configurator, set **ESC Mode** to *RF Gyro Governor*,
  and set **Motor ERPM Max** (use its speed calculator; aim for 75-85%
  throttle at your headspeed).
- FlyRotor's default throttle range is **1100-1940 µs**. Set Low and High
  Throttle on the [Motors](../configurator/tabs/motors.md#throttle-range) tab
  to match, or teach the ESC new endpoints: override to 100%, connect the
  battery, wait for the beeps, then override to 0% and wait for the beeps.
- A lower **Handover Throttle** (10%) works well.
- Set the ESC telemetry protocol to **FLYROTOR**, and its telemetry wire
  for [forward programming](esc-programming.md). On 155A and 280A models,
  the motor temperature sensor appears as **ESC Temp 2** -- enable that
  telemetry sensor to see it on the radio.
- If the tail kicks on spool-up, lower **Starting Torque** in the ESC.

### Hobbywing, Scorpion, YGE, Kontronik and others

Set the ESC to its *external governor* / *fixed-wing* / *linear* mode and
calibrate its throttle range. Most can be programmed through the flight
controller -- see [ESC Forward Programming](esc-programming.md).

### Using the ESC's own governor

If you'd rather let the ESC govern, use **DIRECT** mode: the flight
controller still gives you slow spoolup, fast recovery and autorotation
bailout, and passes your throttle (the ESC's headspeed setting) through.

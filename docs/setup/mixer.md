# Mixer & Swashplate Setup

The mixer calibration makes the blade pitch the flight controller *asks*
for match the blade pitch you *get*. Rotorflight's rates, limits and default
PIDs are all in real degrees, so this step matters: with an uncalibrated
mixer, every number is wrong by the same unknown factor.

You need the [servos set up](servos.md) first, and a **blade pitch gauge**.
All settings are on the [Mixer](../configurator/tabs/mixer.md) tab.

## 1. Swashplate type and directions

1. Choose the **Swashplate Type** -- CCPM 120° for most helicopters -- and
   check the servo layout diagram matches your helicopter.
2. Set the **Main Rotor Direction** (looking from above; usually clockwise).
3. Turn on **Enable Mixer Override** and check the directions with the
   roll, pitch and collective sliders:

    | Command | Swashplate must |
    | --- | --- |
    | Positive roll | Tilt right |
    | Positive pitch | Tilt forward |
    | Positive collective | Rise -- blade pitch increases |

    If an axis moves the wrong way, change its **Control Direction** to
    *Reverse*. (If the whole swashplate moves oddly -- one servo fighting the
    others -- go back and check the [servo directions](servos.md#2-plug-in-the-servos-and-set-directions).)

!!! tip "Use your radio sticks"
    **Enable Mixer Passthrough** drives the override from your radio sticks,
    which is handy for the direction checks.

## 2. Level the swashplate and zero the pitch

With all overrides at **0°** (servo arms level):

1. Adjust the servo-to-swashplate links until the swashplate is **level**,
   both side to side and front to back.
2. Adjust the swashplate-to-grip links until the main blades read **0°**
   on the pitch gauge.

If the links aren't adjustable, use the **Roll**, **Pitch** and
**Collective trim** under *Swashplate Trims* instead.

## 3. Calibrate collective

1. Set the collective override to **+10°**.
2. Measure the blade pitch.
3. Adjust **Collective calibration** until the gauge reads 10°.
4. Set collective to **-10°** and check. If it isn't also 10°, adjust
   **Collective Geometry Correction** until +10° and -10° read the same.
5. Set collective back to 0°.

## 4. Calibrate cyclic

1. Fit the pitch gauge and turn the rotor head until moving the roll
   override changes the blade pitch the most -- that's where cyclic is
   measured.
2. Set the roll override to **+8°** and measure the blade pitch.
3. Adjust **Cyclic calibration** until it reads 8°.

## 5. Set the limits

These protect against mechanical binding. Use the override to find where
the head runs out of travel:

| Limit | Set it to |
| --- | --- |
| **Collective blade pitch limit** | The most collective the head can do without binding -- usually 14-16°. The collective you actually fly is set on the [Rates](../configurator/tabs/rates.md) tab, below this. |
| **Cyclic blade pitch limit** | The most cyclic the head can do around zero collective -- usually 12-16°. This isn't your cyclic rate; it's the physical limit. |
| **Total blade pitch limit** | The most cyclic + collective together. At full collective, add cyclic until something binds or a servo reaches its end -- the swashplate centre ball will stop following. Repeat at full negative collective. |

Check there's **no binding anywhere** across the full range of collective
and cyclic combined.

## 6. Collective tilt correction (optional)

At the extremes of collective, some heads tilt the swashplate when cyclic
is added. At full positive collective, add cyclic and watch the swashplate
centre ball: adjust **Positive Collective Tilt Correction** until it stays
put. Repeat at full negative with **Negative Collective Tilt Correction**.

## 7. Tail rotor

=== "Variable pitch tail (servo)"

    1. Set **Tail rotor type** to *Variable pitch*.
    2. Set the yaw override to **0°**. Adjust the tail pushrod so the tail
       bellcrank is at 90°; if that doesn't give 0° tail blade pitch,
       fine-tune with **Yaw center trim**.
    3. Check the direction: positive yaw must push the nose right (tail
       left). Reverse **Yaw Control Direction** if not.
    4. Set the yaw override to **+22°**, measure the tail blade pitch, and
       adjust **Yaw calibration** until it's about 22°. Check -22° too.
    5. Override to about ±60° and set the **CW / CCW Yaw Blade Angle
       Limits** to the most that doesn't bind.

    Tail geometry is never perfectly symmetric, so the calibration and
    limits won't match the gauge exactly at every angle. That's fine; the
    point is to get the numbers close, so the default tail gains work.

=== "Motorised tail"

    1. Set **Tail rotor type** to *Motorised*. The tail ESC goes on motor
       output 2.
    2. Leave **Yaw calibration** at 100%.
    3. Set **Motor idle throttle** just high enough that the tail motor
       keeps turning.
    4. See [Motorised Tail & TTA](../tuning/motorised-tail.md) for the rest.

Turn the mixer override off when you're finished -- it blocks arming.

Next: [RPM Measurement](rpm-measurement.md) and the
[Governor](governor.md).

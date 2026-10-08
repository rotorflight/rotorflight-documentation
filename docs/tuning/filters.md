# Filter Tuning

Filters keep vibration out of the control loop. Too little filtering lets
vibration through to the servos -- buzzing, heat, and a tune you can't push.
Too much adds delay -- a soft helicopter that can't take high gains. The aim
is filtering *just strong enough* to remove the peaks.

Start with the [RPM filter](../setup/rpm-filters.md) at Medium, one lowpass
filter around 100 Hz and the dynamic filter with a few notches -- the
defaults. Then check with a log.

## 1. A test flight

Take off at the highest headspeed you'll use and hover for a minute or two,
then fly a little forward flight. If you see or hear fast vibration on the
first hover, land at once and investigate before going on.

Log at a high rate (1 kHz or more), with **Raw Gyro** and **Gyro** ticked
on the [Blackbox](../configurator/tabs/blackbox.md) tab.

## 2. Read the spectrum

In the [Blackbox Explorer](https://blackbox.rotorflight.org):

1. Find a steady stretch at constant headspeed. Mark its start with **I**
   and its end with **O**.
2. Show the **filtered gyro** for roll, pitch and yaw, and open the
   **spectrum** (frequency analyser).

A well-filtered helicopter shows large values at the far left (the
helicopter's real movement), low values everywhere else, and **no sharp
peaks** -- maybe some small bumps between 40 and 80 Hz.

## 3. Identify the peaks

Divide each peak's frequency by the main rotor and tail rotor frequencies:

> main rotor frequency = headspeed ÷ 60   (2400 rpm → 40 Hz)
>
> tail rotor frequency = main rotor frequency × tail gear ratio

| Peak at | Is | Do |
| --- | --- | --- |
| A whole multiple of the main rotor frequency | A main rotor harmonic | Raise the RPM filter strength, or add that harmonic with custom notches. |
| A multiple of the tail rotor frequency | A tail rotor harmonic | As above, for the tail. |
| The motor frequency | Motor vibration | Make sure the motor notch is on (Medium and High have it). |
| A fixed frequency that doesn't move with headspeed | A frame resonance -- skids, fin, boom, belt | Check the helicopter mechanically first. If it can't be fixed, add a **notch filter** centred on it. |

A broad **bump** at the 1× or 2× main rotor frequency usually means
**blade tracking or balance** is off. Check the blades before adding filters.

## 4. Adjust

- Widen a notch by lowering its **Q** -- but not below 2.0, which adds a lot
  of delay.
- The **lowpass** filter shouldn't go below about 60 Hz; below 80 Hz only if
  you really need it. Lower it only if there's a broad "grass" of noise at
  60-80 Hz, especially during manoeuvres.
- With RPM filtering working well, the **dynamic filter** needs only 2-4
  notches.

## 3D flying

3D raises vibration, especially at the main rotor's 2× harmonic. Check a
log of 3D flight too. Peaks that only appear there may need a wider notch
(lower Q) on the 2× harmonic. A tall "grass" floor is usually fine.

## Overspeed and autorotation

The RPM filter follows the **motor** RPM. When a one-way bearing lets the
rotor turn faster than the motor -- in an autorotation, or the governor easing
off in a dive -- the notches are briefly in the wrong place. The dynamic
filter covers that gap; keep a couple of its notches on.

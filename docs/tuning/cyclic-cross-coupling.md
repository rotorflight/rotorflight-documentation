# Cyclic Cross-Coupling

## What it is

Give a hard pitch input and the helicopter also rolls a little. The frame,
heavy around the pitch axis, lags behind the rotor disc; the difference
loads the rotor, and through gyroscopic precession that load comes out as a
roll. You can see it:

- at the **stops of tic-tocs**, as the centre of the rotor rotating a little;
- in a hover, by **shaking the elevator stick** back and forth -- the
  helicopter tilts in roll and drifts in yaw.

**Cyclic cross-coupling compensation** feeds a little of the pitch command
(how fast it's changing) into roll, so the two effects cancel.

## Settings

On the [Profiles](../configurator/tabs/profiles.md#main-rotor-settings) tab:

| Setting | Default | |
| --- | :-: | --- |
| **Cyclic Cross-Coupling** | on | Enables it. |
| **Cross-Coupling Gain** | 50 | Strength of the pitch-to-roll compensation. |
| **Cross-Coupling Ratio** [%] | 0 | Adds the opposite (roll-to-pitch) compensation, as a percentage of the pitch-to-roll. |
| **Cross-Coupling Cutoff** [Hz] | 2.5 | How fast the compensation acts. |

## Tuning

Tune this early, while the gains are still soft and the coupling is easy to
see.

1. Hover and shake the elevator stick, or fly tic-tocs.
2. If the helicopter rolls, raise the **gain** in small steps until the roll
   is gone, or until raising it stops making a difference.
3. Check with piro-flips: cross-coupling compensation changes how the
   helicopter responds at different points of the piro-flip, so increase it
   gradually to get used to the feel.

Stiffer main rotor dampers usually need *less* gain.

## Constant cross-coupling

Very hard dampers, a very low headspeed or some head designs can leave the
blades' flapping hinge off-centre. Then the coupling is constant rather than
only during pitch changes. The **ratio** setting can help with that.

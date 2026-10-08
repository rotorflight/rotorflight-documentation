# High Speed Integral

**In short:** HSI keeps the helicopter's attitude steady in fast flight and
on big collective changes. The default works for most helicopters; raise it
if the helicopter balloons, dives or bobbles in fast passes; lower it if it
bobbles at the stops of tic-tocs.

## What it does

A rotor disc moving fast through the air produces more lift on the
advancing side and the front than at rest. In fast forward flight with
positive collective the helicopter tends to pitch up; with negative
collective, the opposite. The effect depends on both airspeed and
collective -- and it reverses when the collective does.

The **HSI offset** (the *O* term) is an integral that works in proportion to
the collective. It builds up the correction needed for the current flight
condition, and because it scales with collective, the correction reverses
automatically when you reverse the collective. On other flybarless systems
you may have seen this as the swashplate "arching" when you move the
collective with the helicopter tilted.

## Settings

On the [Profiles](../configurator/tabs/profiles.md#pid-controller-settings)
tab, for roll and pitch:

| Setting | Default | |
| --- | :-: | --- |
| **HSI Offset Gain** (O) | 50 | How strongly the offset builds. |
| **HSI Offset Limit** | 90° | The most offset allowed. |

## Tuning

| You see | Try |
| --- | --- |
| Pitches up or dives in fast forward flight | Raise HSI gain |
| Attitude jumps on big collective changes at speed | Raise HSI gain |
| Bobbles or restless at high collective | Lower HSI gain |
| Bobbles at the stops of tic-tocs | Lower HSI gain |

A good test: tilt into fast forward flight at high collective and jab the
elevator. Raise the gain until it starts to bobble, then back off.

## Why tic-tocs are tricky

HSI works best when the correction needed reverses together with the
collective. In tic-tocs, a small error also reverses at every stop -- so a
high HSI gain can start to treat it as a correction, and bobble. Rotorflight
transfers HSI into the normal I-term when large cyclic inputs are given,
which limits this; if it still happens, lower the gain.

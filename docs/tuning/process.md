# Tuning Process

A step-by-step order for tuning a helicopter, starting from the defaults.
Read [Tuning](index.md) first -- especially *Before you tune*.

All the settings are on the [Profiles](../configurator/tabs/profiles.md)
tab, and in the Lua suites under *Flight Tuning*.

## 1. Compensations first

Tune these while the gains are still at their soft defaults -- the effects
are easiest to see then.

### Collective to pitch compensation

On a sudden collective change, the long tail boom lags behind: the nose
pitches **up** on a hard climb-out and down on a hard push-over. This
mixes some elevator in with collective to cancel it.

1. Turn on **Collective to Pitch Compensation**.
2. From a hover, punch full collective. Watch the tail.
3. Tail drops (nose pitches up): raise the gain. Nose pitches down: lower it.

Not needed for gentle flying -- leave it off if you don't do hard
collective.

### Cyclic cross-coupling

When you pitch the helicopter, the rotor's gyroscopic precession makes it
roll a little too -- most visible at the stops of tic-tocs, or as a roll
wobble when you shake the elevator stick in a hover. See
[Cyclic Cross-Coupling](cyclic-cross-coupling.md).

## 2. Cyclic P

P is how hard the helicopter pushes back when it's off where you asked --
how locked-in it feels.

1. Raise roll and pitch **P** in steps of about 10%.
2. Test with hard forward-to-back and side-to-side transitions, then
   tic-tocs if you fly them. Watch the boom and skids for a fast shudder.
3. When it shudders, back off until it's gone.

Pitch is the hardest axis to tune and the most sensitive; roll tolerates a
wide range. Start with pitch.

## 3. Cyclic D

D damps any sudden rotation, from your stick or a gust, and stops P from
overshooting. The P:D balance sets the stick feel: more D feels more
"robotic".

!!! warning
    D amplifies vibration more than any other term. Make sure the
    [filters](filters.md) are working first, and check servo temperatures
    after flights while raising D.

1. Raise **D** until the stops feel well-damped, or until a fast buzz or
   shudder appears -- then back off.
2. If raising D lets you raise P further without a shudder, do so.

## 4. Cyclic I

I holds the helicopter where you put it. Too much I gives a slow wallow,
too little lets it drift off line.

1. Raise **I** until a slow oscillation appears, then back off by about a
   third.
2. The best test is **pirouetting pitch pumps** (piro-pogos): if the
   helicopter doesn't stop cleanly and shakes slowly at the end, I is too
   high or P too low.

Roll and pitch can usually share the same I.

## 5. Cyclic F (feedforward)

F moves the swashplate the moment you move the stick -- so the helicopter
follows the stick without waiting for P and I to build up.

1. Do continuous flips and rolls, and stop crisply.
2. Keeps rotating a little after the stop: **raise F** on that axis.
3. Stops, then bounces back: **lower F**.

In a Blackbox log, a well-set F leaves the I-term near zero through
full-stick flips and rolls.

!!! note "F is not for changing how fast it reacts"
    F should match the helicopter's natural response, nothing more. If you
    want a sharper feel, use **B** (next).

## 6. Cyclic B (boost)

Boost adds a kick while the stick is *moving*: sharper starts and stops.
Raise it in small steps until the feel is as sharp as you like. Usually only
pitch needs much. Too much shows as an oscillation right at the stops.

## 7. Tail

!!! warning "Wag that won't tune out"
    A tail that wags whatever the gains is almost always mechanical: slop in
    the linkage, a sticky pitch slider, or a slow servo. Fix that first.

1. **P**, **D** and **I** on yaw, in the same way as cyclic: test with
   pirouettes and hard stops, and fast forward flight.
2. **CW / CCW Yaw Stop Gain**: pirouette in each direction and stop hard.
   If the stop bounces back in one direction, lower that stop gain; if it
   overshoots, raise it.
3. **Collective Feedforward Gain**: hover, then punch collective. If the
   nose kicks round against the main rotor torque, raise it; if it kicks
   the other way, lower it. **Cyclic Feedforward Gain** works the same for
   hard cyclic.
4. Motorised tail: see [Motorised Tail & TTA](motorised-tail.md).

## 8. High speed integral

For fast forward flight and big collective changes: see
[High Speed Integral](high-speed-integral.md). The default suits most
helicopters.

## 9. Fine-tuning

- **I-Term Relax** cutoff (lower = less bounce-back after fast moves,
  higher = more precision in long continuous rotations).
- **Error Decay** time: longer holds a hover more firmly; shorter feels
  freer for 3D.
- **Rates** and **Response Time** for the stick feel you like.

See the [Profiles](../configurator/tabs/profiles.md#quick-troubleshooting)
page's symptom table for a quick reference.

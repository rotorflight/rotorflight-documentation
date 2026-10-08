# Governor Tuning

The goal: a steady headspeed through any manoeuvre, without surging or
hunting. Ideally the **precompensation** (feedforward) does most of the
work -- adding throttle *before* the headspeed sags -- with **P** making quick
corrections and **I** holding the headspeed over time.

You need the governor set up and working first -- see
[Governor Setup](../setup/governor-setup.md). The gains are per profile, on
the [Profiles](../configurator/tabs/profiles.md#governor-settings) tab.

!!! note "A governor can be too good"
    A well-tuned governor delivers a lot of torque, and the tail has to
    counter all of it. If the tail can't hold during hard collective, the
    answer may be a softer governor, less collective, or more tail authority
    (bigger tail blades, a higher tail ratio) -- not more tail gain.

## Preparation

- Motorised tail: set **TTA gain** to 0 while tuning the governor.
- On the [Blackbox](../configurator/tabs/blackbox.md) tab, log at 1 kHz with
  the **Governor** field on, and **Debug mode** `GOVERNOR` for extra detail.
- Change one gain at a time. With the Lua suite you can change gains at the
  field between flights; an efficient routine is to fly three or four values
  around the default for one gain, logging each, then compare.

The test manoeuvre: hard **pitch pumps** -- full positive, full negative,
repeated -- and fast climb-outs. Look at the headspeed trace in the log.

## 1. Collective precompensation and F

**Collective** precomp (default 50) adds throttle as collective rises; the
**Feedforward Gain** (default 10) scales all the precompensation together.

- Headspeed **drops** on each pump: raise collective precomp (or F).
- Headspeed **rises** above target on each pump: lower it.

Try steps of about 10. Then tune **Cyclic** and **Yaw** precomp the same
way, with hard cyclic and pirouettes.

## 2. I-gain

Raise **I** (default 50) until a slow oscillation in headspeed appears --
during or after the pumps -- then reduce it by about a third. Steps of about
25.

## 3. P-gain

Raise **P** (default 40) until fast oscillations appear, then reduce it by
about a third. Steps of about 10.

If the headspeed surges or hunts overall, **Master Gain** (default 40)
scales P, I and D together.

## 4. D-gain

Usually not needed. Larger helicopters, with heavy rotors, may benefit from
a little.

## Symptoms

| You see | Try |
| --- | --- |
| Headspeed sags on collective, recovers slowly | Raise collective precomp / F, then I |
| Headspeed overshoots after a pump | Lower precomp, or lower P |
| Slow headspeed wander, ~1 Hz | Lower I |
| Fast headspeed oscillation, audible surging | Lower P or Master Gain |
| Throttle near 100% in a hover | Headspeed too high for the power system -- lower it or change gearing |
| Motor bogs, then overspeeds in descents | Turn on **Dynamic Minimum Throttle** |
| Pack sag makes headspeed fall late in the flight | Turn on **Voltage Compensation** (needs Battery ADC) |

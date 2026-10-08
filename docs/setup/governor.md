# Governor

The governor holds the headspeed constant -- whatever the collective, the
manoeuvre or the battery voltage. It also spools the rotor up gently,
recovers quickly if you flick throttle hold by mistake, bails out of
autorotations, and copes safely with a lost RPM signal.

The Rotorflight governor works with electric motors and with nitro and
petrol engines. This page explains how it works; [Governor Setup](governor-setup.md)
walks through setting it up.

Settings are split between the [Governor](../configurator/tabs/governor.md)
tab (global) and the [Profiles](../configurator/tabs/profiles.md#governor-settings)
tab (per profile -- headspeed and gains).

## Governor modes

| Mode | What it does | Needs RPM |
| --- | --- | :-: |
| **OFF** | No governor: the throttle channel goes straight to the ESC. | No |
| **LIMIT** | No governor, but the idle, minimum and maximum throttle limits are applied. | No |
| **DIRECT** | Throttle follows your input, but with slow spoolup, fast recovery and autorotation bailout. For an ESC with its own governor, or a throttle curve in the radio. | No |
| **ELECTRIC** | The full governor, tuned for electric motors. | Yes |
| **NITRO** | The full governor, tuned for nitro and petrol engines. | Yes |

**ELECTRIC** and **NITRO** need a fast RPM signal -- see
[RPM Measurement](rpm-measurement.md). Without one, the flight controller
won't arm (`GOVERNOR` flag).

## The throttle channel

The throttle channel's range is shown as **0-100%**. Below 0% is the *stop*
range: the motor is off, and that's where the throttle must be to arm (your
throttle hold value).

```
 ┌ stop ┐┌──────────────────────── active ────────────────────────────┐
         0%                                                        100%
 ├┄┄┄┄┄┄┄┾━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┽┄┄┄┄┄┄┄┤
```

### Handover

The **handover throttle** divides the range in two. Below it is *idle*: the
throttle goes straight to the motor. Above it, the governor takes over.

```
        ┌───── idle ─────┬────────── governor enabled ───────────────────┐
        0%              25%                                          100%
 ├┄┄┄┄┄┄┾━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┽┄┄┄┄┄┄┄┤
```

The motor must be able to start below the handover point. On a nitro
helicopter, the clutch must engage below it.

### Target headspeed

Above handover, the target headspeed is the profile's **Full Headspeed** ×
the throttle input. With a full headspeed of 2500 rpm, 90% throttle aims for
2250 rpm and 100% for 2500.

## Throttle types

How you use the throttle channel depends on the **Throttle Type**:

=== "NORMAL"

    The throttle channel drives the motor directly until the target
    headspeed is reached; then the governor takes over until the throttle
    goes back below handover. Works with throttle on a switch or a throttle
    curve on the stick (set the flat part of the curve to your headspeed
    percentage).

    The ramp-up follows your input, limited by the spoolup time.

=== "SWITCH"

    Below handover the channel drives the motor directly (idle). Above
    handover it *selects the headspeed*. Use a switch that jumps between
    positions -- for example 10% idle, then 80% and 90% for two headspeeds:

    ```
                  10%                                   HS 80%  HS 90%
            0%     ▼        25%                             ▼       ▼    100%
     ├┄┄┄┄┄┄┾━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┽┄┄┄┄┄┄┄┤
    ```

    Not for throttle-on-stick. ELECTRIC and NITRO only.

=== "FUNCTION"

    The throttle position picks a governor *function*:

    ```
     ┌ OFF ┐ ┌─────── IDLE ───────┬─────── AUTO ───────┬─────── RUN ────────┐
             0%                  33%                  66%                 100%
     ├┄┄┄┄┄┄┄┾━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━┽┄┄┄┄┄┄┄┤
    ```

    | Function | Throttle output |
    | --- | --- |
    | OFF | Motor stopped. |
    | IDLE | The **Idle Throttle** setting. |
    | AUTO | The **Auto Throttle** setting -- autorotation practice. |
    | RUN | Governed, at full headspeed. |

    Ideal for ExpressLRS, whose low-resolution switch channels can't carry
    a precise throttle value. A typical setup: a throttle-cut switch for
    OFF, and a 3-position switch for IDLE / AUTO / RUN.

!!! warning "ELRS wide channels"
    NORMAL and SWITCH need a full-resolution throttle channel. ExpressLRS's
    *wide* switch channels aren't precise enough -- use FUNCTION, or put
    throttle on a full-resolution channel.

## States

The governor moves between states on its own, depending on the throttle
input and what the motor is doing. The current state is sent to your radio
as a telemetry sensor.

| State | When | What happens |
| --- | --- | --- |
| **OFF** | Throttle below 0% | Motor stopped. |
| **IDLE** | Throttle below handover | Throttle passed to the motor, limited by the startup ramp. Expected on the ground. |
| **SPOOLUP** | Throttle raised above handover | Ramps up to the target headspeed at the **spoolup** rate. |
| **ACTIVE** | Target headspeed reached | The governor holds the headspeed, with precompensation for collective, cyclic and yaw. Target changes follow the **tracking** rate. |
| **THROTTLE HOLD** | Throttle cut while ACTIVE | Spooling down. If throttle returns within the **Throttle Hold Timeout**, it recovers quickly instead of a slow spoolup. |
| **RECOVERY** | Coming back from hold or fallback | Fast ramp to the target, at the **recovery** rate -- the helicopter is probably in the air. |
| **AUTOROTATION** | Throttle dropped into the auto range while ACTIVE | Motor at idle or auto throttle; raising the throttle triggers a bailout. |
| **BAILOUT** | Throttle raised during autorotation | Fast spoolup at the recovery rate. |
| **FALLBACK** | RPM signal lost or unreliable | Throttle held at an estimated value, reduced by the **Fallback Drop** so you notice -- land. |
| **BYPASS** | GOVERNOR BYPASS mode switch on | All governor functions off; throttle from the bypass curve. |

## Autorotation bailout

To practise autorotations with a fast bailout:

1. Set an **Autorotation Timeout** on the Governor tab (0 disables
   bailout).
2. Set **Auto Throttle** below the handover throttle.

Autorotation is detected when, while governed, the throttle drops into the
range between **Auto Throttle** and handover. Raise it above handover to
bail out. Dropping below Auto Throttle -- e.g. into idle after landing --
cancels the autorotation, and the next spoolup is a normal, slow one.

```
        ┌ idle ─┬─ auto ─┬────────── governor enabled ───────────────────┐
        0%     12%      25%                                          100%
 ├┄┄┄┄┄┄┾━━━━━━━┷━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┽┄┄┄┄┄┄┄┤
```

## Idle throttle in the flight controller

If one radio model flies several helicopters, the idle level can live in the
flight controller instead: **Idle Throttle** sets a minimum motor output
whenever the motor is running below handover. The radio can still send a
higher idle.

## Mode switches

| Mode | |
| --- | --- |
| **GOVERNOR BYPASS** | Turns the governor off entirely and uses the collective-based bypass throttle curve. No ramps, no safeguards. A get-out for a failed RPM signal. |
| **GOVERNOR FALLBACK** | Simulates a lost RPM signal, to test what fallback feels like. |
| **GOVERNOR SUSPEND** | Suspends the governor's PID, leaving only precompensation. For testing. |

## Output throttle range

The governor's 0-100% output maps onto the [Motors](../configurator/tabs/motors.md#throttle-range)
tab's throttle range:

- **Low Throttle** is 0%. On electric, the motor shouldn't run there, but
  should start just above it.
- **High Throttle** is 100% -- full throttle.
- **Motor Off** is below Low Throttle, where the motor is *guaranteed* to
  stop. It's also what lets the ESC arm.

Every change within the range must change the motor's power -- no
deadbands. The motor must start below 5% and reach full power at 100%.
Calibrate the ESC's throttle range to match.

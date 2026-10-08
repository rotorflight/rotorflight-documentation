# Motorised Tail & TTA

Small helicopters often drive the tail rotor with its own motor instead of
a variable-pitch tail. A motorised tail has plenty of authority in one
direction -- spin the tail motor faster -- but little in the other: the
slowest it can go is idle, and a fixed-pitch rotor can't push the other way.

## Setup

On the [Mixer](../configurator/tabs/mixer.md#tail-rotor-settings) tab, set
**Tail rotor type** to *Motorised*. The tail ESC goes on motor output 2.

- **Yaw calibration**: leave at 100%.
- **Motor idle throttle**: just high enough that the tail motor keeps
  turning reliably.
- **Yaw center offset**: the tail throttle for a zero-yaw hover, so the
  controller starts from the right place.

Set the tail ESC's protocol on the [Motors](../configurator/tabs/motors.md)
tab, and give it an RPM signal (a second frequency input or bidirectional
DShot) so it shows up in logs and can be used for TTA. Turn off the tail
ESC's braking -- see [BLHeli_S to Bluejay](../setup/blheli-s-to-bluejay.md).

## Tail Torque Assist (TTA)

When the tail motor is already at idle and the helicopter needs more yaw in
that direction, **TTA** briefly *raises the main rotor headspeed*. More
headspeed means more main rotor torque, which turns the helicopter the way
the tail can't. It needs the [governor](../setup/governor.md).

Settings, on the [Profiles](../configurator/tabs/profiles.md#tail-rotor-settings)
tab:

| Setting | Default | |
| --- | :-: | --- |
| **TTA gain** | 0 (off) | How strongly TTA raises the headspeed. Typically 50-150. |
| **TTA limit** [%] | 20 | The most headspeed increase allowed. Typically 20-50%. |

### Tuning TTA

Push the helicopter into a situation where it runs out of tail authority:

- fly **backwards fast**, tail into the wind;
- **tail slides** and **backward loops**.

If the helicopter suddenly swings round -- sometimes up to 180° -- raise the
TTA gain. Repeat until the swing is mostly gone.

You may never remove it completely. On some helicopters the main motor
simply doesn't have the spare power to provide the torque needed.

Tune the [governor](governor.md) with TTA off first, then bring TTA in.

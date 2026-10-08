# Ethos Radio Setup

Setting up an Ethos model for a Rotorflight helicopter. Start from a new
model (any type), or from the template below.

!!! tip "Template model"
    [rotorflight-generic.bin](files/rotorflight-generic.bin) is a ready-made
    Ethos model with the channels and switches described here, for an
    SBUS / F.Port / F.Bus receiver. Copy it to the radio's `models` folder
    and adapt it.

## Receiver and binding

1. Bind the receiver to the model, following FrSky's instructions.
2. For an FrSky receiver, open **Model → RF System → (receiver) →
   Options** and set the **telemetry port** to **F.Bus** -- the preferred
   connection: one wire carrying both control and telemetry. Connect it to
   the flight controller's receiver port and set the protocol to
   **FrSky FBUS** on the [Receiver](../../configurator/tabs/receiver.md)
   tab.
3. For ExpressLRS, set the external module to ELRS, and set the packet rate
   and telemetry ratio to match the flight controller -- see
   [ELRS Custom Telemetry](../../setup/elrs-custom-telemetry.md).

Once bound, the receiver's telemetry sensors appear under **Model →
Telemetry**.

## Channels

For F.Bus, F.Port and SBUS, use the FrSky order:

| Channel | Function | Example control |
| :-: | --- | --- |
| 1 | Aileron (roll) | Right stick |
| 2 | Elevator (pitch) | Right stick |
| 3 | Throttle | Throttle hold switch + flight mode switch |
| 4 | Rudder (yaw) | Left stick |
| 5 | Collective | Left stick, through a pitch curve |
| 6 | AUX 1 -- Arm | SB, up = armed |
| 7 | AUX 2 -- Profile switch | SE, 3 positions |
| 8 | AUX 3 -- Rescue | SH, momentary |
| 9 | AUX 4 -- Blackbox | SA |
| 10 | AUX 5 -- spare | SC |

For ExpressLRS, use the ELRS order instead: 1 roll, 2 pitch, 3 collective,
4 yaw, **5 arm**, 6 throttle. Pick the matching preset on the
[Receiver](../../configurator/tabs/receiver.md#channel-assignment) tab.

Leave the throttle at 100% in the flight modes you fly with the governor,
and send a value below 0% on throttle hold.

## Telemetry sensors

RFSuite needs certain telemetry sensors from the flight controller. The
easiest way to select them is from the suite itself: **Setup → Telemetry**,
press **Save** -- see [Troubleshooting](troubleshooting.md#missing-sensors).

After changing sensors, **delete all** telemetry sensors on the radio and
**discover** them again.

## Flight controller side

Then on the flight controller:

- [Modes](../../configurator/tabs/modes.md): ARM on AUX 1, plus any rescue,
  Blackbox or other modes.
- [Adjustments](../../configurator/tabs/adjustments.md): profile switching
  on AUX 2 -- see [Profile Switching](../../setup/profile-switching.md).

# Buzzer

The flight controller's buzzer tells you what it's doing without a screen:
calibration done, arming, battery warnings, lost link. Choose which events
sound on the [Beepers](../configurator/tabs/beepers.md) tab, or with the
`beeper` command.

## What the beeps mean

| Sound | Event | Meaning |
| --- | --- | --- |
| 3 short beeps after power-up | `GYRO_CALIBRATED` | Gyro calibration finished. Keep the helicopter still until you hear it -- moving it restarts the calibration. |
| One long beep then a short one | `ARMING` | Armed. |
| Two medium beeps | `DISARMING` | Disarmed. |
| Short beep every 2.5 s | `ARMED` | Reminder that the flight controller is armed. |
| Repeating beep, 0.5 s on / 0.5 s off | `RX_LOST` | No signal from the receiver. |
| SOS in Morse | `RX_LOST_LANDING` | Failsafe active. |
| Repeating beep, 0.25 s on / 0.5 s off | `BAT_LOW` | Battery at the warning level. |
| Almost continuous tone | `BAT_CRIT_LOW` | Battery critically low. |
| Short beep, on demand | `RX_SET` | The BEEPER mode switch -- for finding a crashed helicopter. |
| Two short beeps | `ACC_CALIBRATION` / `BLACKBOX_ERASE` | Accelerometer calibration or Blackbox erase finished. |
| Two longer beeps | `ACC_CALIBRATION_FAIL` | Accelerometer calibration failed. |
| Melody | `READY_BEEP` | Ready (with GPS: fix acquired). |
| Counted beeps | `GPS_STATUS` / `MULTI_BEEPS` | Satellite count, or a confirmation -- e.g. one beep per in-flight adjustment, and the profile number when switching PID profile. |
| -- | `ON_USB` | Allows beeping while powered from USB only. Usually off. |

## The `beeper` command

```
beeper                  # list which events are on
beeper -<EVENT>         # turn an event off, e.g. beeper -ON_USB
beeper <EVENT>          # turn it on again
```

`play_sound [n]` plays the sounds in turn (or sound *n*) -- handy to hear
them on the bench.

## DShot beacon

With DShot ESCs, the motor can beep too (`beacon` command, and the *ESC
Beacon* section of the Beepers tab) -- for finding a helicopter in long
grass after a crash. `beeper_dshot_beacon_tone` sets the tone. It can't
sound while the motor runs, and arming waits two seconds after the last
beacon tone.

## Buzzer hardware

The buzzer output switches a pin on and off, so it needs an **active**
buzzer -- one that makes its own tone when powered. Passive buzzers that
need a PWM signal only click. Rotorflight flight controllers have one
built in, or a buzzer header.

On the bench, a buzzer powered from the servo rail only works if that rail
is powered.

# Blackbox

The Blackbox records flight data many times a second: stick inputs,
setpoints, gyro, PID terms, mixer and servo outputs, motors, RPM, battery,
governor and more. Logs are the most useful tool there is for tuning and for
finding out what went wrong.

The [Blackbox](../configurator/tabs/blackbox.md) tab page covers the
settings in the Configurator. This page is the background.

## Where logs go

| `blackbox_device` | |
| --- | --- |
| `SPIFLASH` | The flight controller's flash chip -- 16 MB to 256 MB on Rotorflight boards. |
| `SDCARD` | An SD card on the flight controller. |
| `SERIAL` | An external logger on a UART -- see [OpenLager](../setup/openlager.md). |
| `NONE` | No logging. |

## Getting logs off

- **Mass storage mode** (the Blackbox or Setup tab, or `msc` in the CLI)
  makes the flight controller a USB drive; copy the logs off as files. The
  fastest and most reliable way.
- **Save to file** in the Configurator downloads over MSP -- slow, and can
  corrupt large logs.
- With an external logger, take out its SD card.

Open the logs in the [Blackbox Explorer](https://blackbox.rotorflight.org)
(or the desktop version).

## Logging rate and space

`blackbox_rate_denom` divides the PID loop rate: at a 2 kHz PID loop, 1 logs
at 2 kHz, 2 at 1 kHz, 4 at 500 Hz.

| For | Use |
| --- | --- |
| Filter tuning, vibration | The highest rate the device can manage -- 1-2 kHz. |
| PID and governor tuning | 500 Hz - 1 kHz. |
| General flying, long logs | 250 Hz or less. |

Higher rates and more fields fill the flash faster. Every field you don't
need (`blackbox_log_*` = `OFF`) leaves room for more flights.

## Logged data

| Setting | Logs |
| --- | --- |
| `blackbox_log_command` | Stick commands |
| `blackbox_log_setpoint` | Rate setpoints |
| `blackbox_log_mixer` | Mixer inputs |
| `blackbox_log_pid` | P, I, D, F, B and O terms |
| `blackbox_log_attitude` | Attitude estimate |
| `blackbox_log_gyro_raw` | Unfiltered gyro (for filter tuning) |
| `blackbox_log_gyro` | Filtered gyro |
| `blackbox_log_acc` | Accelerometer |
| `blackbox_log_mag` | Compass |
| `blackbox_log_alt` | Altitude |
| `blackbox_log_gps` | GPS |
| `blackbox_log_battery` | Battery voltage and current |
| `blackbox_log_rssi` | RSSI |
| `blackbox_log_motors` | Motor outputs |
| `blackbox_log_servos` | Servo outputs |
| `blackbox_log_rpm` | Motor and rotor RPM |
| `blackbox_log_vbec` / `blackbox_log_vbus` | BEC and bus voltages |
| `blackbox_log_temp` | Temperatures |
| `blackbox_log_esc` | ESC telemetry |
| `blackbox_log_bec` | BEC telemetry |
| `blackbox_log_governor` | Governor state, target and throttle |

## When it logs

| `blackbox_mode` | |
| --- | --- |
| `ARMED` | Whenever armed (default since 2.3). |
| `SWITCH` | While the BLACKBOX [mode](../configurator/tabs/modes.md) switch is on. |
| `NORMAL` | While armed **and** the switch is on. |
| `OFF` | Never. |

`blackbox_grace_period` keeps logging for a few seconds after disarming.
`blackbox_rolling_erase` (default on) overwrites the oldest logs when the
flash is full; `blackbox_initial_erase_kb` erases enough space before a log
starts.

## Debug data

`debug_mode` adds eight extra values to the log for investigating one
subsystem -- for example `GOVERNOR`, `RPM_FILTER`, `RPM_SOURCE`, `TTA`,
`AIRBORNE`, `DYN_NOTCH`, `ESC_SENSOR`, `CRSF_LINK_STATISTICS_UPLINK`.
`debug_axis` picks the axis for modes that work per axis. The full list is
under `debug_mode` in [CLI Settings](cli-settings.md).

The log format is described in the
[Technical Reference](../contributing/tech/blackbox-format.md).

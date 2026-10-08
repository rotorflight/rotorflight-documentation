# CRSF Sensors

!!! info "New in 2.4"

Live diagnostics for CRSF-protocol sensor accessories wired to the flight
controller -- a GPS, battery sensor, barometer, cell-voltage sensor or RPM
sensor that speaks CRSF. The flight controller can use their readings for
telemetry, Blackbox and the battery meter.

The tab appears once a UART is set to **CRSF Sensors** on the
[Configuration](configuration.md) tab.

## Link

Shows whether data is arriving: the port state, bytes received, sync bytes,
CRC-good and CRC-failed frames, and the last frame type. Rising *CRC fail*
counts mean a wiring or baud problem.

## Decoded readings

Panels appear for each kind of data received:

| Panel | Shows |
| --- | --- |
| **GPS** | Latitude, longitude, ground speed, heading, altitude, satellites. |
| **Battery** | Voltage, current, capacity used, remaining. |
| **Barometer** | Altitude and vertical speed. |
| **Cell Voltages** | Cell count, total voltage and each cell. |
| **RPM** | Each RPM source. |

To use a CRSF sensor as the battery source, choose **CRSF** for the
battery voltage or current on the [Power](power.md) tab.

!!! warning "CRSF RPM is telemetry-rate"
    CRSF RPM can be fed to the flight controller with the CLI setting
    `crsf_sensors_use_rpm = ON`. It updates at telemetry rate, not motor
    rate, so it's not suitable for the RPM filter or the governor -- use an
    RPM sensor input or bidirectional DShot for those.

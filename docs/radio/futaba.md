# Futaba

Futaba radios connect over **S.BUS2**, which carries both control and
telemetry on one wire.

## Wiring

Connect the flight controller's receiver port (often labelled *SBUS*) to the
receiver's **S.BUS2** port with a servo lead.

## Flight controller

1. [Configuration](../configurator/tabs/configuration.md#serial-ports) tab:
   set the port to **Serial Rx**. Save and reboot.
2. [Receiver](../configurator/tabs/receiver.md) tab: protocol **Futaba
   S.BUS2** (with *Inverted* and *Half-Duplex* on), channel preset
   **Futaba / Hitec**, and telemetry **enabled**. Save and reboot.

## Radio

1. **Linkage Menu → System Type**: a protocol with telemetry, such as
   T-FHSS or FASSTest 18CH, with telemetry on.
2. **Linkage Menu → Sensor**: register the sensors in these slots. The slot
   numbers and sensor types must match exactly, or the readings come out
   wrong.

| Slot | Sensor type | Carries |
| :-: | --- | --- |
| 1 | Voltage | Battery voltage and average cell voltage |
| 3 | Current (SBS-01C) | Current, mAh used, voltage |
| 6 | RPM | Headspeed |
| 7 | Temperature (SBS-01T) | Flight controller temperature |
| 8 | Kontronik ESC | ESC telemetry: voltage, current, mAh, RPM, temperatures, BEC current, throttle |

Then add the values you want to your telemetry screen.

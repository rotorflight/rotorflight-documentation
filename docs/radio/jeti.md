# Jeti

Jeti receivers connect over **EX Bus**, which carries control and telemetry
on one wire. Rotorflight's telemetry sensors then appear on the radio
automatically.

## Wiring

Connect the flight controller's receiver port (often labelled *SBUS*) to an
EX Bus capable receiver output -- for example **E1** -- with a servo lead.

## Receiver

In the radio's **Device Explorer**, open the receiver and:

1. Select the receiver.
2. Enable the alternative pin configuration if needed, so the chosen output
   can be set to EX Bus.
3. Set that output (e.g. E1) to **EX Bus**.

## Flight controller

1. [Configuration](../configurator/tabs/configuration.md#serial-ports) tab:
   set the port to **Serial Rx**. Save and reboot.
2. [Receiver](../configurator/tabs/receiver.md) tab: protocol **Jeti
   EXBUS**, and enable telemetry. Save and reboot.

The control link and telemetry should now work, with the selected
[telemetry sensors](../configurator/tabs/receiver.md#telemetry-sensors)
listed on the radio.

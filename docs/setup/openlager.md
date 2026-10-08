# OpenLager Logging

[OpenLager](https://github.com/d-ronin/openlager/wiki) is a small external
Blackbox logger with a micro SD card. It's useful on flight controllers
without a flash chip, or when you want to log long flights at a high rate.

- Practically unlimited storage.
- Fast to download -- take out the card and read it on your computer.
- Logging over a UART costs the flight controller very little CPU.

!!! note "OpenLager, not OpenLog"
    The cheaper *OpenLog* looks similar but can't keep up with Blackbox
    data rates. You need an OpenLager.

## Wiring

Three wires: **5 V**, **ground**, and a free UART's **TX** pad to the
OpenLager's **RX**. When it's powered, it starts a new log file and writes
whatever it receives.

## Setup

1. On the [Configuration](../configurator/tabs/configuration.md#serial-ports)
   tab, set that UART to **Blackbox Logging** at **2000000** baud. Save and
   reboot.
2. On the [Blackbox](../configurator/tabs/blackbox.md) tab, set **Logging
   device** to **Serial Port**, and choose the logging mode, rate and data.

Use a fast card (UHS-I), formatted with the
[SD Association's formatter](https://www.sdcard.org/downloads/formatter/).

!!! tip "Card latch"
    Some OpenLagers have a hinged card holder rather than a push-to-eject
    slot, which pops open in heat-shrink. Carefully flatten the retaining
    pin a little so the card slides in and out.

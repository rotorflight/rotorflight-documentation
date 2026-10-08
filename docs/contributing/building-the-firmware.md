# Building the Firmware

Rotorflight builds with GNU Make and the ARM GCC toolchain, on Linux, macOS
or Windows (with WSL).

## Unified targets

There's one firmware build per MCU family, not per board:

| Target | MCU |
| --- | --- |
| `STM32F405` | F405 |
| `STM32F411` | F411 |
| `STM32F7X2` | F722 / F7x2 |
| `STM32F745` | F745 |
| `STM32G47X` | G474 |
| `STM32H743` | H743 |

The pins, timers and defaults for each board are a **board configuration**
in [rotorflight-targets](https://github.com/rotorflight/rotorflight-targets),
applied on top of the unified firmware by the Configurator when it flashes.
See [Custom Board Configuration](tech/custom-boards.md).

## Building

```
git clone https://github.com/rotorflight/rotorflight-firmware.git
cd rotorflight-firmware
make arm_sdk_install          # once: downloads the toolchain into tools/
make TARGET=STM32F7X2         # one target
make unified                  # all targets
```

The `.hex` files land in `obj/`. `make help` lists the options. Extra
defines go in `OPTIONS`, for example `make TARGET=STM32F7X2
OPTIONS="USE_SOMETHING"` -- see [Customizing the Build](tech/customizing-the-build.md).

The repository also has a `Dockerfile` and `docker-compose.yml` for
building in a container.

## Flashing your build

In the Configurator's [Firmware Flasher](../getting-started/flashing-the-firmware.md),
choose your board, then **Load Local** and pick your `.hex`. The board
configuration is still combined with it at flash time.

## Tests

```
make test
```

runs the unit tests (PID, setpoint, maths and others). The governor, mixer,
servos, rescue and levelling have few or no tests, so changes there need
extra care -- and, where possible, a new test. See
[Test Coverage](tech/test-coverage.md).

## Debugging

See [Hardware Debugging](tech/hardware-debugging.md) and
[Debugging with VS Code and J-Link](tech/hardware-debugging-vscode-jlink.md).

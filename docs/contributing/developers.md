# Developers

Developers are welcome on every part of the project: C for the firmware;
Svelte and JavaScript for the Configurator and Blackbox Explorer; Lua for
the radio suites.

## Before you start

Talk to the team on the [Rotorflight Discord](https://discord.gg/FyfMF4RwSA)
before starting anything big. It saves work on both sides:

- What's the change, and why?
- Are there alternatives, or a better place in the code for it?
- What testing has been done, and do you need testers?

## Process

1. Fork the repository and create a branch from `master`.
2. Make your change. Keep each pull request to one topic.
3. Rebase on the latest `master` before opening the pull request.
4. Open the pull request with a clear description, and say how you tested
   it -- on hardware, in the Virtual FC, with Blackbox logs.

Each repository has an `AGENTS.md` (and sometimes `CONTRIBUTING.md`) with
its own rules -- for example, the Configurator's Virtual FC must be kept in
step with any MSP change, and version numbers are only changed by the
maintainers.

## Where to go next

- [Building the Firmware](building-the-firmware.md)
- [Coding Style](coding-style.md) for the firmware
- The [Technical Reference](tech/index.md): parameter groups, configuration
  and Blackbox formats, build customisation, hardware debugging
- [MSP Overview](../reference/msp-overview.md) for tools that talk to the
  flight controller
- Firmware changes that affect the API or flight behaviour are recorded in
  [Changes.md](https://github.com/rotorflight/rotorflight-firmware/blob/master/Changes.md)

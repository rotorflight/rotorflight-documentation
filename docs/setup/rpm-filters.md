# RPM Filters

Every turning part of a helicopter -- main rotor, tail rotor, motor, gears --
shakes the flight controller at a frequency set by how fast it's turning.
The gyro picks this vibration up along with the helicopter's real movement.
The RPM filter uses the measured RPM and the gear ratios to know exactly
where those vibrations are, and removes just them with narrow notch filters.

Because the notches follow the RPM precisely, they can be narrow, and add
much less delay than general-purpose filtering. Less filtering delay means
the PID controller can work harder -- a tighter, more locked-in helicopter.

You need a working [RPM measurement](rpm-measurement.md) first.

## Turning it on

On the [Gyro](../configurator/tabs/gyro.md#rpm-filter) tab:

1. **Enable** the RPM Filter.
2. Choose a **Strength**:

    | Strength | Notches placed on | Use it for |
    | --- | --- | --- |
    | **Low** | Main rotor 1×, 2× and 4×; tail rotor 1× | Smooth helicopters, small helicopters |
    | **Medium** | Main rotor 1×-4×; tail rotor 1×-2×; main motor | Most helicopters (default) |
    | **High** | Main rotor 1×-6×, with a wider triple notch at 2×; tail rotor 1×-2×; main motor | Helicopters with a lot of vibration |

    "1×" is the rotor's speed itself (the fundamental), "2×" twice that,
    and so on. A main rotor at 2400 rpm turns 40 times a second, so its 1×
    vibration is at 40 Hz and its 2× at 80 Hz.

3. Set **Minimum Frequency** a little below the main rotor frequency at the
   lowest headspeed you fly -- headspeed ÷ 60. At 1500 rpm that's 25 Hz, so
   set about 20 Hz.

Start with Medium. Higher strength removes more vibration but adds delay.

## Other filters alongside

With the RPM filter on, keep:

- **one lowpass filter** around 100 Hz, and
- the **dynamic filter** with 2-4 notches, to catch what the RPM filter
  doesn't (frame resonances, the moment of overspeed when the one-way
  bearing lets the rotor outrun the motor).

See [Gyro](../configurator/tabs/gyro.md).

## Checking it with Blackbox

Make a [Blackbox](../configurator/tabs/blackbox.md) log of a short hover at
a steady headspeed, at a high logging rate. In the
[Blackbox Explorer](https://blackbox.rotorflight.org):

1. Find the steady part of the hover. Mark its start with **I** and its end
   with **O**.
2. Open the **Analyser** and look at the gyro spectrum.

Clear peaks left at a multiple of the rotor frequency mean a harmonic isn't
being filtered. For example, at 4200 rpm the main rotor turns at 70 Hz;
a peak near 140 Hz is its 2× harmonic. Try the next strength up, or use a
**Custom** set of notches (see below).

See [Filter Tuning](../tuning/filters.md) for more.

## Custom notches

For full control, the notches can be set one by one: which rotor harmonic
or motor each one follows, its width (Q), and single, double or triple
notches. Choosing a strength, then editing in the CLI, switches the tab to
**Custom**; **Reset Custom Notches** goes back to a preset.

Custom notches are for experienced tuners working from Blackbox logs --
the presets suit most helicopters.

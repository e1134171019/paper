# Prior-Art Boundary

Last updated: 2026-08-16

This file records what has already been found in the literature so that future sessions do not repeatedly "rediscover" the same ideas as possible novelty.

## Already-established concepts

The following concepts have direct prior art and must not be claimed as new by themselves.

### 1. Input-parallel / output-series and primary-parallel / secondary-series

Known magnetic implementations already exist at kW scale. Representative work includes fully integrated planar magnetics for primary-parallel isolated boost converters and IPOS high-step-up converter families.

Implication: "split current on the low-voltage side and stack voltage on the high-voltage side" is not new.

### 2. Optimal intermediate voltage

Cascaded converter research already optimizes intermediate bus voltage as a function of total loss / duty ratio / capacitor RMS current.

Implication: "find the best intermediate voltage" is not new by itself.

### 3. Loss maps / design-space optimization

Power-loss maps, Pareto optimization, efficiency-density co-optimization, and device-loss design-time optimization are established.

Implication: "make a loss map" is a method, not a novelty claim.

### 4. Active power decoupling / 100-120 Hz ripple buffering

Well established in single-phase AC/DC and DC/AC systems.

Known approaches include:

- dc-side active buffer,
- ac-side buffer,
- buck / boost / buck-boost decoupling,
- series-stacked buffer,
- partial-power buffer,
- ripple-port modules,
- transformer-integrated power decoupling,
- DAB active energy buffer,
- matrix-converter power decoupling,
- switched-capacitor energy buffer.

Implication: "use a bidirectional buffer to keep 120 Hz ripple away from the battery" is not new.

### 5. Multilevel Energy Buffer / Voltage Modulator (MEB)

Prior work already shows that an energy-buffer stage can also modify the effective input voltage of a high-frequency DC/AC stage, reduce transformer-primary current, and reduce conduction / magnetic losses sufficiently to offset some added buffer loss.

Implication: "add a buffer that also helps voltage transformation / converter operating range" is already known conceptually.

### 6. Integrated ripple steering in DC/AC DAB structures

Prior work integrates ripple-steering elements with existing primary-side full-bridge switches, reducing double-line-frequency source current ripple without simply adding a complete independent converter.

Implication: "reuse existing bridge switches to locally route ripple energy" is not new.

### 7. Center-tapped transformer + local LC buffer + matrix converter

Prior work has used the transformer common-mode degree of freedom and a small LC buffer to perform power decoupling without additional active switches; later versions also support bidirectional power conversion and ZVS.

Implication: "transformer simultaneously transfers main power and helps buffer ripple power" is already known.

### 8. DAB + active energy buffer in the high-frequency link / primary side

Prior work explicitly places active energy-buffer functionality before or around the high-frequency power-transfer stage so that the transformer / battery do not carry the full single-phase power pulsation.

Implication: "put the buffer before the HFT so ripple does not cross the transformer" is already known in AC/DC directions and related isolated converter structures.

### 9. Partial-power processing

Series voltage injection and related architectures already process only a fraction of the pulsating power with the active converter while a passive capacitor handles most energy storage.

Implication: "only process the correction power instead of the full power" is established.

### 10. Bidirectional low-voltage battery <-> high-voltage bus <-> AC

DAB + VSI and related battery-energy-storage architectures are mature.

Implication: bidirectional BUS / UPS operation is a benchmark and application context, not novelty.

## Closest prior-art families to the current candidate problem

The most dangerous prior-art directions for our current research are:

1. MEB / voltage-modulating energy buffers for low-voltage micro-inverters.
2. Integrated ripple-steering DC/AC DAB converters.
3. Center-tapped-transformer matrix converters with power decoupling.
4. DAB single-phase AC/DC converters with active energy buffers located before / inside the high-frequency link.
5. Series-stacked / partial-power energy buffers at kW scale.
6. Primary-parallel / secondary-series magnetic conversion at kW scale.

## What is still not closed

Current searches have not yet demonstrated an exact prior-art match for the following complete combination:

- 12 V-class source,
- 1-2 kW,
- roughly 100-200 A low-voltage source current,
- DC -> single-phase AC as the primary system direction,
- explicit accounting of battery / fuse / connector / busbar / PCB / MOS / transformer-primary current-path resistance,
- first major impedance-transformation placement treated as a design variable,
- local bidirectional energy-buffer placement treated jointly with that transformation point,
- objective explicitly minimizing low-side RMS / conduction loss and total system loss,
- fixed hardware topology rather than runtime selection among unrelated complete converters.

This is a candidate research boundary, not a novelty declaration.

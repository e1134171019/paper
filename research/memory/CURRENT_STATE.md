# Current Research State

Last updated: 2026-08-16

## 1. System boundary

Primary problem:

`12 V low-voltage DC -> single-phase 110 Vac`, target power roughly `1-2 kW`.

At 2 kW, ideal 12 V source current is about `166.7 A`.

The research is not "invent a topology for novelty". The objective is to minimize total system loss, especially losses caused by the low-voltage / high-current region.

Core physical questions:

- Why must the ~166 A current pass through particular devices and conductors?
- How far and how long must that high current exist before impedance transformation?
- Where should the first major voltage increase / impedance transformation occur?
- How much voltage increase is worthwhile?
- Does an extra conversion stage save more `I^2 R` loss than the converter loss it introduces?
- Which current components are necessary real-power current, and which are ripple / circulating / reactive / commutation currents that might be locally buffered or recycled?

## 2. Fundamental loss framing

Useful equations:

- `P = V I`
- `I = P / V`
- `P_path = I_rms^2 R`
- `R = rho L / A`

At 2 kW:

- 12 V -> 166.7 A
- 48 V -> 41.7 A
- 96 V -> 20.8 A
- 192 V -> 10.4 A

For the same `1 mOhm` path resistance:

- 12 V region -> ~27.8 W
- 48 V region -> ~1.74 W
- 96 V region -> ~0.434 W
- 192 V region -> ~0.109 W

Therefore, "where the milliohm lives" is a system-level design variable.

## 3. Known DC-to-AC architecture families already considered

These are not novelty claims; they are the known architecture map used for comparison.

1. Low-frequency transformer inverter.
2. High-frequency transformer two-stage inverter: LV HF switching -> HFT -> rectifier -> HV DC bus -> H-bridge/SPWM.
3. Non-isolated high-gain DC/DC + VSI: Boost / coupled-inductor / switched-inductor / switched-capacitor / voltage multiplier / quadratic families.
4. Single-stage boost / buck-boost inverter.
5. Z-source / quasi-Z-source inverter families.
6. Switched-capacitor / multilevel inverter families.
7. High-frequency-link direct AC / matrix-converter type structures.
8. Modular / IPOS / matrix-transformer / capacitive-power-transfer related structures.

A bidirectional DC bus / UPS / BESS architecture is not treated as a ninth converter topology. It is a system-level reference proving that low-voltage DC <-> AC bidirectional energy flow and buffering are already established concepts.

## 4. Current correction regarding internal bidirectional energy flow

The idea of adding an internal bidirectional energy buffer to a nominally DC-to-AC system is already well studied.

Known functions include:

- twice-line-frequency (100/120 Hz) active power decoupling,
- series-stacked energy buffers,
- partial-power buffers,
- multilevel energy buffer / voltage modulator structures,
- integrated ripple steering,
- center-tapped-transformer power decoupling,
- DAB converters with active energy buffers,
- matrix converters with power decoupling and bidirectional operation.

Therefore the following are NOT novelty by themselves:

- "add a bidirectional buffer",
- "keep 120 Hz energy away from the battery",
- "use a capacitor to absorb and return ripple energy",
- "reuse converter switches for active power decoupling",
- "combine power decoupling with a transformer or DAB",
- "partial-power buffer processing only a fraction of power".

## 5. Important distinction: irreversible loss vs recyclable / oscillatory energy

### Irreversible dissipation

Examples:

- MOSFET `RDS(on)` conduction heat,
- copper / PCB / busbar / connector `I^2 R`,
- capacitor ESR heat,
- magnetic core loss,
- dielectric loss.

These cannot be recovered after they become heat. Topology can only prevent or reduce them.

### Potentially recoverable / avoidable transition energy

Examples:

- leakage inductance energy otherwise burned in a snubber,
- MOSFET Coss energy under hard switching,
- clamp / commutation energy,
- some reactive energy.

These can sometimes be redirected through resonance, active clamp, ZVS/ZCS, or local energy recycling.

### Oscillatory energy that is not itself a loss

Examples:

- twice-line-frequency single-phase power pulsation,
- resonant tank energy,
- reactive load energy,
- DC-link energy fluctuation.

The loss comes from the RMS current and device stress created while moving this energy.

## 6. Current strongest open question

The broad concept of internal energy buffering is already known. The remaining candidate research question is narrower:

> In a very-low-voltage, kW-scale, 100-200 A DC-to-single-phase-AC system, where should the first impedance-transformation point and the local bidirectional energy-buffer point be placed relative to each other so that total system loss is minimized?

Candidate configurations:

- Buffer before first impedance transformation: may influence low-voltage loss, but buffer itself must carry very high current.
- Buffer after an intermediate voltage lift: less buffer current, but requires an extra conversion step.
- Buffer on the HV side: easy to buffer at low current, but it cannot undo low-voltage conduction loss that already occurred.
- Integrated structure: same hardware performs part of the first impedance transformation and the energy-buffer function.

This is still only a candidate gap. Current wording must remain:

"Current searches have not yet identified a paper that exactly overlaps the full 12 V-class, kW, 100-200 A, first-impedance-transformation placement + energy-buffer placement + low-side RMS/conduction-loss co-design problem."

## 7. Immediate research direction

Next prior-art search must be tightly scoped to:

- 12 V / 24 V input,
- kW-scale,
- isolated DC-to-single-phase-AC,
- current-fed / push-pull / full-bridge / matrix transformer,
- integrated active power decoupling,
- ripple steering on the low-voltage primary side,
- low-side RMS-current reduction,
- transformer-primary conduction-loss reduction,
- energy-buffer placement in HF link,
- combined voltage-lift + power-decoupling structures.

The next topology should NOT be drawn until this closure search is complete.

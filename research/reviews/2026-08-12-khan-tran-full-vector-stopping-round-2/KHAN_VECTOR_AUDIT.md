# Khan 2023 Full-Vector Audit

Date: 2026-08-12
DOI: `10.3390/pr11041087`
Title: *A Novel High-Voltage Gain Step-Up DC-DC Converter with Maximum Power Point Tracker for Solar Photovoltaic Systems*
Comparison mode: `BOUNDED_TRADEOFF`
Count basis: `SCHEMATIC_DISCRETE_POWER_STAGE_V1`

## Source boundary

- Canonical publisher: MDPI / *Processes* 11(4), 1087 (2023).
- A legal/readable published-version full text is available under CC BY through the publisher and White Rose Research Online.
- The publisher PDF binary is not committed to this repository.

## Prototype boundary

The paper reports a 150 W hardware program with regulated output around 380 V and input points from 20 V to 40 V at 50 kHz.

Experimental operating points reported in Table 4:

| Vin | Vout | Duty | reported efficiency |
|---:|---:|---:|---:|
| 20 V | 380 V | 0.54 | 90% |
| 25 V | 380 V | 0.48 | 91% |
| 30 V | 380 V | 0.44 | 93% |
| 35 V | 380 V | 0.39 | 94% |
| 40 V | 380 V | 0.35 | 96% |

These efficiency values are retained as condition-specific reported results and are not used as a leaderboard.

## Structural vector

Section 3 / Fig. 5 explicitly identifies:

- controlled switches: 1;
- discrete diodes: 7 (`D1`–`D7`);
- capacitors: 5 (`C1`–`C4`, `Co`);
- inductors: 3 (`L1`–`L3`);
- coupled-inductor/transformer core: none explicitly identified for the proposed circuit;
- schematic-discrete magnetic-element count: 3;
- schematic-discrete winding count: 3.

The VMC uses `L2`, `L3`, `C2`, `D2`, and `D3`; the switched-capacitor network uses `C3`, `C4`, `D4`, and `D5`.

## Semiconductor voltage-stress boundary

### Controlled switch

The paper states in its comparison/conclusion that the proposed switch stress is `Vo/2`, i.e. about `0.50 Vout` as a theoretical/design statement.

No experimental `VDS` waveform or topology-wide measured switch-voltage scalar was located in Figs. 16–20; those figures show `VGS`, input/PV voltage, and output voltage.

Therefore:

- maximum measured controlled-switch stress: `UNRESOLVED`;
- theory/design switch stress: `Vo/2 ≈ 0.50 Vout`;
- evidence type must remain `THEORY/AUTHOR_DESIGN_STATEMENT`, not measured.

### Diodes

The accessible full text does not lock an exact topology-wide maximum measured diode reverse-voltage scalar. It also does not provide a sufficiently explicit common-schema maximum diode scalar that can be safely substituted for measurement in this audit.

Therefore:

- maximum measured diode stress: `UNRESOLVED`;
- maximum theory-at-prototype diode scalar: `UNRESOLVED` for common-schema comparison.

## Current / grounding / switching-mode fields

- input-current continuity: theoretical operating assumption says the inductor current is uninterrupted; the paper also claims low input ripple;
- measured input-current ripple scalar: `UNRESOLVED`;
- explicit proposed-topology input/output common-ground claim: `UNRESOLVED` in the text used for this audit; do not infer it from schematic appearance alone;
- switch ZVS/ZCS: `NOT_LOCATED`;
- diode ZVS/ZCS: `NOT_LOCATED`;
- diode reverse-recovery burden: author claims the inductor arrangement reduces reverse-recovery loss; this is not promoted to a measured ZCS label.

## Hardware / instrumentation locator

Table 3 and Fig. 15 identify the prototype/test setup including:

- MCU: TI F28004x C2000;
- gate driver: TLP250H;
- solar PV simulator: Chroma 62100H-600S;
- electronic load: Chroma 63204A-600-280;
- experimental waveforms obtained using a digital oscilloscope.

## Internal numerical inconsistency

The simulation section states that 150 W output power is used to determine load resistance, while Table 1 lists `Rload = 100 ohm` and the same simulation discussion regulates `Vo = 380 V`.

`380^2 / 100 = 1444 W`, which is incompatible with 150 W if the 100-ohm load and 380 V are simultaneous steady-state conditions.

This is preserved as `INTERNAL_PARAMETER_INCONSISTENCY`; the audit does not silently repair or average it. The hardware section uses an electronic load in constant-current mode, so the simulation-table conflict is not automatically transferred to the hardware load boundary.

## Evidence decision

`L4_DIRECT_VECTOR_PARTIAL_WITH_STRESS_GAP`

Rationale:

- legal/readable full text resolved;
- hardware prototype and operating locators resolved;
- multiple numeric claims and structural fields verified;
- required topology-wide measured semiconductor stress vectors remain incomplete;
- an internal simulation-parameter inconsistency is preserved.

Khan is **not authorized for L5 promotion** in this node.

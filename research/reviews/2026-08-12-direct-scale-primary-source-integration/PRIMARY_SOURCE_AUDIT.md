# Direct-Scale Primary-Source Audit

Date: 2026-08-12
Scope: six newly supplied IEEE primary PDFs, plus the three previously supplied Hasanpour-lineage IEEE primary PDFs required to close the direct-scale integration node.
Comparison mode: `BOUNDED_TRADEOFF`
Count basis: `SCHEMATIC_DISCRETE_POWER_STAGE_V1`

## Rules applied

- PDF binaries are not stored in the repository.
- Exact/approximate/theoretical/unresolved values are not flattened into one scalar type.
- Multi-switch stress is compared by the maximum controlled-switch stress, not a preferred main switch.
- MOSFET body diodes are not counted as separate discrete diodes.
- Resonant/snubber capacitors visible in the power stage are counted as capacitors.
- Efficiency is descriptive only; it is not used for ranking.
- A direct-scale record targets approximately 20–50 V input, 380–400 V output, and 150–300 W hardware. Neighbor-scale and high-voltage/high-power records remain context evidence.

## DPSI-ABBASI-2024

- DOI: `10.1109/OJPEL.2024.3432628`
- Title: Two-Switch Ultrahigh Step-Up DC–DC Converterer With Low Input Current Ripple and Low Switch Voltage Stress
- Prototype: 20 V → 400 V, 240 W, 50 kHz, D=0.458, coupled-inductor turns ratio n=1.
- Locator: experimental section, Fig. 7–9; component design and stress calculations immediately before the experimental section.
- Measured controlled-switch stress: S1=39.5 V, S2=102 V; normalized maximum = 102/400 = 0.255.
- Measured diode stress: D1=36 V, D2=38 V, D3=174 V, D4=399 V, Do=269 V; normalized maximum = 399/400 = 0.9975.
- Input-current ripple: a little higher than 30% at the reported nominal test point.
- Common ground: explicitly claimed.
- Soft switching: no ZVS/ZCS claim for the proposed hardware was located; switch turn-on/turn-off loss and diode reverse-recovery loss are explicitly modeled. Preserve as `NOT_CLAIMED/HARD_SWITCHING_CONTEXT`, not inferred soft switching.
- Efficiency: 94.4% at nominal 240 W / 20 V; reported range 92–95.7% over 100–300 W for 20/30 V tests.
- Count: 2 controlled switches, 5 discrete diodes, 5 capacitors, 2 magnetic cores (one input inductor + one three-winding CI), 4 total windings.
- Evidence decision: direct-scale, stress-complete experimental record.

## DPSI-YAO-2023

- DOI: `10.1109/TPEL.2023.3298683`
- Title: A Family of High Step-Up DC–DC Converters Based on Enhanced Boost Cells With Coupled Inductor
- Prototype: 40 V → ~400 V, 200 W, nominal 500 kHz, duty approximately 0.5; dynamic regulation changes frequency from 500 to 570 kHz for 40→48 V input and up to ~650 kHz under the reported load step.
- Locator: Table II / Fig. 16 and experimental section; Fig. 18–24 for waveforms, dynamic response and efficiency.
- Coupled-inductor winding choice: 1:2:2, planar three-winding CI.
- Input current: continuous; reported RMS about 5.23 A.
- Switch: experimental waveform confirms ZVS turn-on.
- Diodes: experimental waveforms confirm ZCS turn-off.
- Exact measured maximum switch/diode voltage-stress scalars are not text-locked. Under the prototype operating point, theory gives Vsw=Vin/(1-D)≈80 V => 0.20 Vout; theoretical diode stresses are approximately 112 V and 288 V => theoretical maximum ≈0.72 Vout. These remain `theory_at_prototype`, not measured scalars.
- Efficiency: 95.55% at 200 W.
- Count: 1 controlled switch, 2 discrete diodes, 4 capacitors (C1, C2, Co and explicit resonant/switch capacitor), 2 magnetic cores (input inductor + one three-winding CI), 4 total windings.
- Common-ground status: ground-switch construction is stated; an explicit input-output common-ground claim was not located. Preserve `unresolved`.
- Evidence decision: direct-scale bounded record with measured-stress-scalar gap.

## DPSI-LIAO-2024

- DOI: `10.1109/JESTIE.2024.3386555`
- Title: A High Voltage-Gain DC–DC Converter With Low Switch Voltage Stress
- Prototype: 180 W, Vo≈300 V, Vin=14/22/32 V, fs=100 kHz, resonant frequency≈130 kHz, duty range about 0.61→0.39.
- Locator: Table II / Fig. 8; Figs. 9–16.
- Measured controlled-switch stress: Q1,Q2≈40 V; Q3,Q4≈80 V; normalized maximum≈80/300=0.267.
- Measured diode stress: D1,D2≈200 V; normalized maximum≈0.667.
- Soft switching: Q2/Q4 ZVS is experimentally shown; D1/D2 ZCS turn-on/turn-off is experimentally shown. Q1/Q3 are not promoted to soft-switched status without an explicit source claim.
- Efficiency: 96.09% at Vin=32 V, Vo=300 V.
- Count for one resonant step-up unit: 4 controlled switches, 2 discrete diodes, 4 capacitors (Cb,C1,C2,Cr), 2 coupled-inductor cores, 4 total windings.
- Common ground and numeric input-ripple scalar: unresolved.
- Evidence decision: L4 context because output voltage is outside the direct 380–400 V contract.

## DPSI-DING-2025

- DOI: `10.1109/TPEL.2025.3534272`
- Title: A Single-Switch ZVS High Step-Up DC–DC Converter With Stacked Voltage Multiplier Cell
- Rated prototype: 36–48 V → 380 V, 500 W, 50 kHz.
- Direct-boundary experimental point: 36 V → ~380 V at 300 W, D=0.55.
- Locator: Table I p.8298; Figs. 15–21.
- Turns: N1=8, N2=4, N3=16 (n1=0.5,n2=2).
- At 300 W with Lm=80 µH: measured switch and D1 stress are both about 77 V; switch normalized stress≈0.203. D1≈0.203 Vout.
- D2/D3 measured scalar is not text-locked. Theory at n1=0.5,n2=2 gives maximum diode stress≈0.80 Vout. Preserve measured maximum diode stress as unresolved.
- Input-current ripple: about 30% at 300 W; about 27% at the reported 500 W condition.
- Soft switching: switch ZVS at the 300 W / Lm=80 µH test; all diodes ZCS turn-off. With other Lm/load combinations the switch can operate in ZCS/TW-ZCM; Lm=50 µH is shown to extend ZVS to 500 W.
- Efficiency: peak 95.44% at 300 W; rated 94.16% at 500 W.
- Count: 1 controlled switch, 3 discrete diodes, 4 capacitors, 2 magnetic cores (L1 + three-winding BIT), 4 total windings.
- Input current ripple: Table IV classifies low. Common ground: Table IV explicitly `Yes`.
- Evidence decision: L4 neighbor-scale; the rated hardware is 500 W even though a 300 W direct-boundary operating point is experimentally reported.

## DPSI-BHASKAR-2026

- DOI: `10.1109/TIA.2026.3680371`
- Title: A Cubic Boost DC-DC Converter with Reduced Switch Voltage Stress for DC Microgrid Application
- Publication boundary: accepted author version; not fully edited, content may change before final publication.
- Prototype: 36 V → 650 V, 500 W, 50 kHz, D≈0.62.
- Locator: Table I; Fig. 11–13.
- Efficiency: experimental 94.4% at 500 W.
- Maximum switch stress: S2=406 V is text-locked and shown in Fig. 12(d); normalized maximum≈406/650=0.625.
- Diode D2 analytical waveform is clamped to Vo; Fig. 12(d) shows D2 voltage, but an exact measured scalar is not text-locked. Preserve measured maximum diode stress as unresolved and theory maximum≈1.0 Vout.
- Count: 3 controlled switches, 3 diodes, 3 capacitors, 3 independent inductors/cores, 3 windings.
- Continuous source current and common ground between input/output ports are explicit claims.
- Soft switching: not claimed for the proposed CBRV power stage.
- Evidence decision: L4 context because the prototype is 650 V / 500 W and because the source is an accepted author version.

## DPSI-OMRAN-2025

- DOI: `10.1109/JESTPE.2025.3598046`
- Title: A High Step-Up Soft-Switched Converter Based on Coupled Inductor and Current-Fed Voltage Multiplier
- Prototype: 40–50 V → 1 kV, 500 W, 200 kHz, N=4 VM stages.
- Locator: Table II; Figs. 10–17.
- Measured switch stress: both S1/S2≈150 V => normalized maximum≈0.15.
- First-stage VM diodes D1/D2: measured≈250 V and experimentally ZCS. Because only first-stage measured diode waveforms are text-locked, the measured maximum across all eight VM diodes remains unresolved.
- Soft switching: both switches ZVS; VM diodes operate under ZCS.
- Common ground between source and load is explicitly claimed.
- Efficiency: peak 95.18% at 250 W / Vin=50 V; rated 92.8% at 500 W / Vin=50 V.
- Count for N=4: 2 controlled switches, 8 discrete diodes (=2N), 9 capacitors (=2N+1; 6 resonant + 3 output), 1 coupled-inductor core, 2 windings.
- Measurement instruments were not explicitly identified in the searchable experimental text; preserve `unresolved`.
- Evidence decision: L4 high-voltage context because Vout=1 kV and rated power=500 W.

## Previously supplied direct-scale Hasanpour-lineage IEEE sources integrated in this node

### DPSI-HASANPOUR-2023
- DOI: `10.1109/OJPEL.2023.3275651`
- 25 V → 400 V, 200 W, 50 kHz.
- 2 switches, 2 diodes, 4 capacitors, 2 cores, 4 total windings.
- Measured maximum controlled-switch stress≈50 V => 0.125 Vout.
- Diode theory≈350 V => 0.875 Vout; exact measured maximum diode scalar unresolved.
- Both switches ZVS; diodes low-reverse-recovery; peak efficiency≈95.8% at 120 W.

### DPSI-HASANPOUR-2025
- DOI: `10.1109/TPEL.2025.3552015`
- 25 V → 400 V, 200 W, 50 kHz, D≈0.51.
- 2 switches, 4 diodes, 6 capacitors, 2 cores, 3 total windings.
- Measured maximum controlled-switch stress≈50 V => 0.125 Vout.
- Diode theory≈173.7 V => 0.434 Vout; exact measured maximum diode scalar unresolved.
- Source conclusion also states maximum component stresses below 40% of output voltage; retain this as a theory/measurement-boundary difference rather than force-reconciling it.
- Both switches ZVS; all diodes low-reverse-recovery; efficiency≈96.3% at full load and peak≈96.6% at 100 W.

### FTRIAGE-IEEE-11159317 / DPSI-HASANPOUR-2026
- DOI: `10.1109/TPEL.2025.3608899`
- 25 V → 400 V, 200 W, 50 kHz.
- 1 switch, 5 diodes, 6 capacitors, 2 cores, 4 total windings.
- Measured switch≈50 V => 0.125 Vout.
- Measured maximum diode≈180 V => 0.45 Vout.
- Switch ZCS turn-on; diodes low reverse recovery; full-load efficiency≈96.6%.

## Audit conclusion

The six newly supplied PDFs do not produce six new direct-scale members. Two are direct-scale (`ABBASI-2024`, `YAO-2023`), two are neighbor-scale (`LIAO-2024`, `DING-2025`), and two are high-voltage/high-power context (`BHASKAR-2026`, `OMRAN-2025`).

The strongest newly measured direct-scale stress observation is Abbasi 2024: maximum controlled-switch stress≈0.255 Vout while one diode reaches≈0.9975 Vout. This materially strengthens the burden-redistribution hypothesis without creating a formal all-objective Pareto claim.

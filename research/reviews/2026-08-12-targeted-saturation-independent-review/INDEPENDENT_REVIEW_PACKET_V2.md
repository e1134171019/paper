# Independent Review Packet v2

Date: 2026-08-12
Role: neutral evidence packet for a future independent reviewer.

This packet intentionally omits L5 decisions, independent-family labels, dominance conclusions, formal Pareto labels, and Research Gap conclusions.

## Direct-scale evidence rows

### 10.1049/iet-pel.2015.0923
- 25 V -> 400 V; 200 W; 88 kHz.
- 1 controlled switch; 4 discrete diodes; 5 capacitors; 2 magnetic cores; 3 windings.
- measured switch stress: `<100 V` (upper bound).
- maximum measured diode stress: unresolved.
- switch ZCS turn-on.
- measured full-load efficiency: 96.4%.

### 10.1038/s41598-024-78739-y
- 24 V -> 400 V; 200 W; 50 kHz; D=0.60.
- 1 switch; 8 diodes; 8 capacitors; 1 core; 2 windings.
- measured switch stress ~62 V.
- measured maximum diode stress ~110 V.
- paper comparison classifies soft switching as No.
- measured full-load efficiency 94.53%.
- common ground: No.

### 10.1038/s41598-025-17301-w
- 25 V -> 400 V; 250 W; 50 kHz; D=0.55.
- 1 switch; 4 diodes; 5 capacitors; 2 cores; 4 windings.
- measured switch stress ~55 V.
- measured maximum diode stress ~240 V.
- switch ZCS turn-on; diodes low reverse recovery.
- measured full-load efficiency 96.4%.

### 10.1049/iet-pel.2015.0870
- 40 V -> 400 V; 200 W; 100 kHz.
- 2 controlled switches; 4 diodes; 5 capacitors; 1 core; 2 windings.
- measured switch-stress vector reported as `<90 V` for both switches (upper bound).
- measured maximum diode stress ~200 V.
- main and clamp switches ZVS.
- measured full-load efficiency 95.4%.

### 10.1038/s41598-025-90093-1
- 25 V -> 400 V; 200 W; 50 kHz.
- 2 controlled switches; 5 diodes; 5 capacitors; 2 cores; 3 windings.
- measured switches ~56 V and ~110 V.
- measured maximum diode stress ~235 V.
- S2 ZCS turn-on; multiple diodes ZCS.
- full-load efficiency 95.9%; separate peak 96.2% at 160 W.
- common ground: Yes.

### 10.1038/s41598-026-47061-0
- 25 V -> 400 V; 200 W; 50 kHz; D=0.30.
- 1 switch; 4 diodes; 5 capacitors; 2 cores; 4 windings.
- measured switch stress ~50 V.
- measured diode vector ~50 / 180 / 300 / 300 V.
- switch ZCS turn-on.
- full-load efficiency 94.9%.
- common ground: Yes.

### 10.1109/TPEL.2025.3608899
- 25 V -> 400 V; 200 W; 50 kHz.
- 1 controlled switch; 5 diodes; 6 capacitors; 2 cores; 4 windings.
- measured switch stress ~50 V.
- measured maximum diode stress ~180 V.
- switch ZCS turn-on.
- measured full-load efficiency ~96.6%.

### 10.1109/OJPEL.2023.3275651
- 25 V -> 400 V; 200 W; 50 kHz.
- 2 controlled switches; 2 diodes; 4 capacitors; 2 cores; 4 windings.
- measured switches ~50 V.
- theoretical maximum diode stress at prototype parameters ~350 V; exact measured maximum diode scalar unresolved.
- both switches ZVS.
- measured peak efficiency ~95.8% at 120 W; exact full-load scalar unresolved.

### 10.1109/TPEL.2025.3552015
- 25 V -> 400 V; 200 W; 50 kHz; experimental D~0.51.
- 2 controlled switches; 4 diodes; 6 capacitors; 2 cores; 3 windings.
- measured switch maximum ~50 V.
- theoretical maximum diode stress at prototype parameters ~173.7 V; exact measured scalar unresolved.
- conclusion separately states maximum component stresses below 40% of Vout; do not reconcile this statement with the theoretical diode value without further source evidence.
- both switches ZVS.
- measured full-load efficiency ~96.3%.

### 10.1109/OJPEL.2024.3432628
- 20 V -> 400 V; 240 W; 50 kHz; D=0.458.
- 2 switches; 5 diodes; 5 capacitors; 2 cores; 4 windings.
- measured S1=39.5 V; S2=102 V.
- measured D1=36 V; D2=38 V; D3=174 V; D4=399 V; Do=269 V.
- input-inductor ripple slightly above 30%.
- common ground: Yes.
- measured nominal efficiency 94.4%.

### 10.1109/TPEL.2023.3298683
- 40 V -> approximately 400 V; 200 W; 500 kHz.
- 1 switch; 2 diodes; 4 capacitors; 2 cores; 4 windings.
- experimental switch ZVS and diode ZCS.
- exact measured maximum voltage-stress scalars unresolved.
- equation-at-prototype values imply switch ~80 V and maximum diode ~288 V; preserve as theoretical.
- measured efficiency 95.55% at 200 W.

### 10.1109/TPEL.2023.3344719
- 20 V -> 400 V; 200 W; 50 kHz.
- 2 controlled switches; 3 diodes; 5 capacitors; one input inductor plus one three-winding coupled inductor.
- prototype coupled-inductor ratios n21=0.5 and n31=2.
- measured S1 voltage stress almost 45 V.
- clamp switch Sc is experimentally shown with very low stress, but an exact measured scalar is unresolved in the recovered prose.
- both S1 and Sc turn on under ZVS.
- diode reverse-recovery loss is minimized; exact maximum measured diode voltage is unresolved.
- analytical equations state both switches share the clamp-capacitor voltage and provide diode stress formulas; retain these as theory.
- rated-power measured efficiency approximately 94%.
- input-current ripple is qualitatively low.

## Newly canonicalized target not yet fully extracted

### 10.1109/ACCESS.2025.3573936
- 40 V -> 400 V; 200 W; 100 kHz experimental prototype.
- measured main-switch maximum voltage approximately 120 V.
- main switch reported ZVS across the tested power range.
- auxiliary switch soft-switching reported.
- diodes turn off under ZCS.
- continuous input current and shared ground reported.
- measured full-load efficiency approximately 96.5%.
- complete controlled-switch stress vector, maximum measured diode stress, and common component-count basis are unresolved in this packet.

## Questions for independent reviewer

1. For every row, classify each stress value as measured, upper bound, theoretical/recalculated, conflict, or unresolved.
2. Identify source-internal contradictions and comparison-boundary mismatches without reconciling them by assumption.
3. For approximately matched 20-40 V -> 400 V / 200-250 W hardware, which engineering burden redistributions are directly supported?
4. For measured-to-measured stress pairs only, identify any strict dominance relationship and state the exact dimensions used.
5. Which additional measurements are required before an all-objective Pareto analysis is defensible?
6. State whether the evidence is sufficiently stable to support a Research Gap. If not, name the blocking evidence gaps.

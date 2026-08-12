# GPT Adjudication — Direct-Scale Primary-Source Integration

Date: 2026-08-12

## Decision

- Research direction: `APPROVE_CONTINUE`
- Bounded L5 records: **11**
- Independent L5 evidence families: **6**
- IEEE 11159317: `AUTHORIZED_L5_BOUNDED`
- Hasanpour 2023 OJPEL: `AUTHORIZED_L5_BOUNDED_WITH_MEASURED_DIODE_GAP`
- Hasanpour/Nouri 2025 TPEL: `AUTHORIZED_L5_BOUNDED_WITH_THEORY_MEASUREMENT_BOUNDARY_DIFFERENCE`
- Abbasi 2024 OJPEL: `AUTHORIZED_L5_BOUNDED`
- Yao 2023 TPEL: `AUTHORIZED_L5_BOUNDED_WITH_MEASURED_STRESS_SCALAR_GAP`
- Liao 2024: `L4_CONTEXT_NEIGHBOR_OUTPUT_SCALE`
- Ding 2025: `L4_CONTEXT_NEIGHBOR_HIGH_POWER`
- Bhaskar 2026: `L4_CONTEXT_HIGH_VOLTAGE_HIGH_POWER_VERSION_BOUNDARY`
- Omran 2025: `L4_CONTEXT_HIGH_VOLTAGE_HIGH_POWER`
- Exploratory stress-pair screen: `AUTHORIZED_INTERNAL_ONLY`
- Formal all-objective Pareto: `NOT_AUTHORIZED_YET`
- Research Gap Candidate: `NOT_AUTHORIZED`
- Independent review: `NOT_COMPLETE / independence_missing=true`

## 1. The direct-scale evidence set materially expanded

The prior bounded set contained six records and four independent-family credits. The primary-source integration adds five direct-scale bounded records:

1. Hasanpour 2023 OJPEL — 25→400 V, 200 W, 50 kHz;
2. Hasanpour/Nouri 2025 TPEL — 25→400 V, 200 W, 50 kHz;
3. IEEE 11159317 / Hasanpour-Nouri 2026 — 25→400 V, 200 W, 50 kHz;
4. Abbasi et al. 2024 OJPEL — 20→400 V, 240 W, 50 kHz;
5. Yao et al. 2023 TPEL — 40→400 V, 200 W, 500 kHz.

This produces eleven bounded L5 records. The three Hasanpour-lineage additions improve topology coverage but do not add independent-family credit. Abbasi and Yao add two new independent programs, so the independent L5 family count rises from four to six.

## 2. Abbasi 2024 is a decisive burden-redistribution observation

The Abbasi primary PDF supplies a complete measured direct-scale stress vector at 20→400 V / 240 W:

- S1=39.5 V;
- S2=102 V;
- D1=36 V;
- D2=38 V;
- D3=174 V;
- D4=399 V;
- Do=269 V.

Therefore:

- maximum controlled-switch stress≈0.255 Vout;
- maximum diode stress≈0.9975 Vout.

The topology also provides common ground and continuous input current, while the reported input-current ripple is slightly above 30% at the nominal point. This record directly demonstrates that improving gain/current-integration properties and keeping switch stress moderate does not imply low diode stress. It strengthens the burden-redistribution hypothesis without proving a universal law.

## 3. Yao 2023 adds a distinct independent design axis

The Yao/Guan enhanced-boost-cell family supplies a 40→400 V / 200 W / 500 kHz direct-scale prototype with a planar three-winding coupled inductor, switch ZVS and diode ZCS. Its high switching frequency and planar-magnetic implementation are materially different from the existing direct-scale families.

However, exact measured maximum switch/diode voltage-stress scalars are not text-locked. The prototype equations imply approximately 0.20 Vout maximum switch stress and approximately 0.72 Vout maximum diode stress. These values remain theory-at-prototype evidence and must not be relabeled as measured.

## 4. Hasanpour-lineage evolution now has a primary-source sequence

The direct primary PDFs now show a useful intra-family sequence:

- 2023 active-clamp trans-inverse: 2 switches / 2 diodes / 4 capacitors; measured max switch≈0.125 Vout; theoretical max diode≈0.875 Vout; ZVS.
- 2025 active-clamp quasi-resonant BIT: 2 switches / 4 diodes / 6 capacitors; measured max switch≈0.125 Vout; theoretical max diode≈0.434 Vout; ZVS.
- 2026 single-switch TWBIT/Cockcroft-Walton: 1 switch / 5 diodes / 6 capacitors; measured max switch≈0.125 Vout; measured max diode≈0.45 Vout; ZCS turn-on.

This is not three independent confirmations. It is stronger evidence for topology-dependent burden allocation within one research program.

## 5. Exploratory stress-pair screen changed materially

Using only maximum controlled-switch stress and maximum diode stress, with evidence boundaries preserved:

- PC-CAND-0027 (~0.155, ~0.275 measured) remains a robust tradeoff candidate.
- IEEE11159317 (~0.125, ~0.45 measured) becomes a second robust tradeoff candidate.
- PC-CAND-0028, PC-CAND-0029, FEXP-CAND-0001 and Abbasi 2024 are strictly dominated by IEEE11159317 on the **two measured stress axes only**.
- PC-CAND-0030 remains indeterminate because its switch stress is an upper bound `<0.225`.
- Hasanpour 2025 has a slightly lower theoretical diode-stress ratio (~0.434) than IEEE11159317's measured ~0.45, but theory and measurement boundaries differ, so no strict cross-boundary certificate is issued.
- Yao 2023 and Hasanpour 2023 retain theory/measured-boundary limitations.

This screen is not an all-objective Pareto frontier. Component counts, magnetics, common ground, input ripple, soft switching, power density, thermal burden and control complexity can change the ordering.

## 6. The research hypothesis is stronger, but the formal Gap is still blocked

The evidence increasingly supports the following hypothesis:

> At direct-scale high step-up conditions, reducing controlled-switch stress is already achievable by several architectures; the unresolved engineering problem is how voltage/current stress, semiconductor count, passive burden, magnetic complexity, input-current conditioning, common-ground behavior and soft-switching requirements are redistributed across the topology.

This hypothesis is stronger after the new primary-source batch because the batch added two independent direct-scale families and produced additional counterexamples to any simple one-axis claim such as “low switch stress is the missing capability.”

The formal Research Gap remains unauthorized because:

1. independent review has not succeeded;
2. PC-CAND-0024 and 10.1155/etep/9317966 still lack text-locked maximum measured diode stress;
3. several newly integrated records retain measured-vs-theory stress gaps;
4. the latest six-PDF batch still produced two new independent direct-scale families, so formal marginal yield is positive;
5. efficiency boundaries remain unmatched and efficiency is excluded from ranking;
6. the all-objective comparison contract is not yet complete enough for a field-wide Pareto certificate.

## Search decision

`STOP_BROAD_KEYWORD_SEARCH / CONTINUE_TARGETED_SATURATION_ONLY`

Broad search is no longer efficient because author/topology lineages are recurring. Future acquisition should target only:

- missing measured stress objectives for already important records;
- a genuinely different direct-scale family that can alter the current burden tradeoff;
- independent-review source needs.

## Authorized next node

`TARGETED SATURATION CLOSURE + INDEPENDENT PACKET REVIEW`

Priority:

1. obtain independent interpretation of the expanded neutral packet;
2. close maximum measured diode stress for PC-CAND-0024 and 10.1155/etep/9317966 if a legal/readable source permits it;
3. resolve remaining direct candidate conflicts only where they can change the frontier;
4. perform one targeted different-family saturation pass rather than broad keyword hunting;
5. rerun stopping rule and all-objective frontier gate.

## Guardrails

- no efficiency leaderboard;
- no claim that eleven L5 records equal eleven independent validations;
- no cross-scale ranking of 300/380, 650 V or 1 kV context records against 400 V direct records;
- no measured label for theory-derived stress values;
- no formal Pareto-optimal labels before independent review and stopping gates close;
- no Research Gap declaration yet.

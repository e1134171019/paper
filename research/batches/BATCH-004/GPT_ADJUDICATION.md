# GPT Adjudication — BATCH-004 Falsification + Coverage Closure

Date: 2026-08-12

## Decision

- Research direction: `APPROVE_CONTINUE`
- Comparison mode: `BOUNDED_TRADEOFF`
- Existing L5 core status: retained; PC-CAND-0030 structural context materially improved
- Broad active-device complexity hypothesis: `FALSIFIED`
- Narrow burden-redistribution hypothesis: `RECURRING_BOUNDARY_CANDIDATE_RETAINED`
- Controlled multi-objective frontier objective: `AUTHORIZED`
- Research Gap Candidate: `NOT_AUTHORIZED`
- Established Research Gap: `NOT_AUTHORIZED`
- Overall stopping rule: `NOT_MET`

## 1. Material closure achieved

The most important blocker closed in this pass is PC-CAND-0030 structural completeness.

Publisher full text now supports:

- 40 V → 400 V, 200 W, 100 kHz.
- duty ratio approximately 0.5.
- one main switch plus one active-clamp switch.
- four diodes.
- five capacitors.
- one coupled-inductor magnetic core.
- turns ratio `Ns/Np = 2`.
- measured main-switch stress `<90 V`, therefore normalized stress `<0.225`.
- diode voltage stress approximately `Vout/2`, therefore maximum normalized diode-stress context approximately `0.5`.
- ZVS turn-on for main and clamp switches.

Common-ground state, quantitative input-current ripple and measurement-instrument details remain unresolved. These values are not inferred from the schematic.

## 2. Effect on the recurring-boundary hypothesis

The completed 0030 structure strengthens the observation that reducing main-switch voltage stress does not imply that every other design burden decreases.

Current examples include:

- PC-CAND-0027: main switch stress ~0.155 Vout, max diode stress ~0.275 Vout, one switch, but eight diodes and eight capacitors; no soft switching in the paper's comparison classification.
- PC-CAND-0028: main switch stress ~0.1375 Vout, max diode stress ~0.60 Vout, one switch, four diodes, five capacitors, and two magnetic cores (input inductor + TWCI).
- PC-CAND-0030: main switch stress <0.225 Vout, diode stress ~0.5 Vout, and an auxiliary active-clamp switch.
- PC-CAND-0024: main switch stress only bounded at <0.25 Vout, one switch, four diodes, five capacitors, and two magnetic cores.

This does **not** establish a monotonic law. Instead it supports a narrower multi-objective interpretation: design burden can migrate among semiconductor stress, active-device count, passive count, magnetic implementation, source-current behavior and integration constraints.

## 3. Counterexample remains valid

DOI `10.1109/OJPEL.2025.3554381` remains a material falsification record against the broad proposition that soft switching necessarily requires an additional active switch or additional magnetic core.

The lawful institutional/final-version record describes:

- a single main switch;
- soft switching using a lossless snubber cell;
- the snubber consists of two diodes and requires no additional active switch or magnetic core;
- continuous input current;
- common ground.

Its stress point is not promoted into the current very-low-stress L5 set in this pass. Therefore it falsifies the broad complexity claim without resolving the narrower frontier question.

## 4. Search saturation is decisively not reached

Two new highly relevant 2025–2026 primary hardware records emerged from substantially different search paths:

### DOI 10.1049/pel2.70039

- 200 W, 400 V output, 100 kHz.
- reports main-switch stress below one quarter of output voltage.
- continuous low-ripple input current and active-clamp soft switching.
- source text contains an internal Vin discrepancy: experimental section indicates 40 V while the conclusion states 30 V.
- the conflict is preserved as an unresolved evidence contradiction and blocks L4/L5 promotion.

### DOI 10.1155/etep/9317966

- 48 V → 400 V, 200 W, 100 kHz.
- single active switch.
- common ground and continuous input current.
- analytical/nominal main-switch stress is approximately the 0.25 Vout boundary.
- the measured waveform scalar has not yet been locked in this pass.

Because new records with direct boundary relevance continue to appear, a saturation or 'literature exhausted' statement would be methodologically invalid.

## 5. The old candidate question must be narrowed again

The v0.2 targeted question:

> Is `common ground + continuous input current + very low normalized switch stress (<0.25)` an unresolved three-way design constraint?

is no longer a safe basis for a prospective gap claim.

Recent records approach or enter this intersection. The correct action is not to defend the candidate gap; it is to enlarge the controlled comparison set and determine the actual Pareto frontier.

## 6. Authorized research objective

The next comparison objective is:

> For approximately 380–400 V output and 150–300 W experimentally validated non-isolated high-step-up converters, characterize the Pareto frontier among main-switch stress, maximum diode stress, active-switch count, diode/capacitor count, magnetic-core/winding burden, source-current ripple, common-ground capability, soft-switching coverage, switching frequency and measurement boundary.

This objective is authorized because it is directly supported by observed heterogeneity in the verified hardware records. It is **not** a Research Gap declaration.

## 7. Independent-review gate remains open

A second extraction of PC-CAND-0024, 0027, 0028 and 0030 was performed as a consistency re-read. It found no material contradiction in 0024/0027/0028 and resolved the structural unknowns in 0030.

However, it was performed by the same GPT execution context. It must therefore be labelled `GPT_REEXTRACTION_NOT_INDEPENDENT` and cannot satisfy the independent-review requirement of the Research Evidence Pipeline.

## 8. Citation-snowball gate remains open

Backward and forward citation work advanced but is not exhaustive.

- Backward: topology-relevant references from all four core seeds and the counterexample were inspected, and recent hardware families were identified.
- Forward: exact-DOI citation-string searches were attempted, but they do not constitute a complete citer graph.

Therefore both snowball gates remain `PARTIAL`.

## 9. Research Gap gate

A Research Gap Candidate remains prohibited because all of the following are not yet simultaneously true:

1. exhaustive or stopping-rule-compliant backward citation screening;
2. exhaustive or stopping-rule-compliant forward citation screening;
3. genuinely independent duplicate extraction/review;
4. marginal-yield saturation across predefined query families;
5. stable direct-scale comparator set with conflicts resolved;
6. compatible measurement/loss boundaries for any efficiency-based inference.

## 10. Next controlled node

`DIRECT-SCALE PARETO FRONTIER CLOSURE`

Priority actions:

1. Resolve the 30 V vs 40 V prototype-boundary contradiction in `10.1049/pel2.70039` using exact table/figure/experimental locators.
2. Lock measured switch/diode stress and complete component counts for the three BATCH-004 candidates.
3. Obtain a genuine independent extraction/reviewer for the core and new direct-scale records.
4. Complete citation-graph traversal and canonical DOI dedup.
5. Build a frontier matrix using typed values (`exact`, `approx`, `upper_bound`, `unresolved`) instead of scalar coercion.
6. Continue marginal-yield tracking until the frozen stopping criterion passes.

## Guardrails

- No efficiency leaderboard.
- No overall-best topology claim.
- No causal attribution from cross-paper ZVS/ZCS vs efficiency.
- No conversion of bounds or approximations into exact scalars.
- No schematic-only inference for common-ground state.
- No silent reconciliation of conflicting source values.
- No Research Gap Candidate while the stopping rule is not met.

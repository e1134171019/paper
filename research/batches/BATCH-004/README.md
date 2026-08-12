# BATCH-004 — Falsification + Coverage Closure

Date: 2026-08-12
Status: `IN_PROGRESS_REVIEWABLE`
Parent audit: `research/reviews/2026-08-12-repeated-tradeoff-v0.2/`

## Objective

Close the blockers identified by Repeated Trade-off Pattern Audit v0.2 before any Research Gap Candidate can be authorized.

This batch is deliberately designed as a falsification and coverage-closure pass. It does **not** authorize a Research Gap claim.

## Work packages

1. Resolve the structural full-text fields of PC-CAND-0030.
2. Formally register the 2025 single-switch soft-switching counterexample (`10.1109/OJPEL.2025.3554381`).
3. Search for recent direct-scale hardware that can falsify or narrow the burden-redistribution hypothesis.
4. Run a first backward/forward citation-snowball pass around the core L5 families and new seeds.
5. Re-extract the four core L5 records as a consistency check.
6. Track disagreements explicitly.
7. Measure marginal yield and decide whether the search is approaching saturation.

## Current adjudication

- Direction: `APPROVE_CONTINUE`
- Comparison mode: `BOUNDED_TRADEOFF`
- `RECURRING_BOUNDARY_CANDIDATE`: retained, but narrowed to a multi-objective burden-redistribution question.
- `RESEARCH_GAP_CANDIDATE`: `NOT_AUTHORIZED`
- Overall stopping rule: `NOT_MET`

## Material change from v0.2

PC-CAND-0030 is no longer structurally unknown. Publisher full text supports a two-switch active-clamp structure with four diodes, five capacitors, one coupled-inductor core, turns ratio `Ns/Np = 2`, and duty ratio around `0.5`. Its measured main-switch stress remains `<90 V` (`<0.225 Vout`), while the four diode voltage stresses are approximately `Vout/2` (`~0.5 Vout`). Common-ground state and measurement-instrument details remain unresolved and are not inferred from the schematic.

The search also produced new 2025–2026 direct-scale hardware, including a 200 W IET design in the `<0.25 Vout` switch-stress region and a 200 W single-switch/common-ground 2026 design around the `0.25 Vout` boundary. The appearance of new directly relevant hardware means saturation has **not** been reached.

## Methodological boundary

The `second_extraction.csv` file is a same-model re-read and consistency check. It is explicitly **not** an independent reviewer. Therefore it cannot satisfy the independent-review gate required for a formal Research Gap conclusion.

## Current research question

The evidence increasingly supports a controlled Pareto/frontier question rather than a scalar leaderboard:

> At a fixed high-gain hardware boundary (approximately 380–400 V output and 150–300 W), how are main-switch stress, diode stress, active-device count, passive-component count, magnetic complexity, source-current ripple, common-ground capability, and soft-switching coverage traded against each other?

This is an authorized comparison objective, not an established research gap.

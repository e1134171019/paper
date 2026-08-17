# Research State Reorganization Design

Date: 2026-08-17
Status: approved for implementation
Repository: `e1134171019/paper`
Branch: `research/state-2026-08-17`

## Purpose

Reorganize the low-voltage high-current DC→AC research memory so the repository records the current research position rather than accumulating one increasingly large narrative file.

The reorganization must preserve the existing evidence pipeline, `research/batches/`, `research/contracts/`, SQLite SSOT policy, and the rule that search absence is not itself a research gap.

## Scope

Only the research-memory/documentation layer is changed.

Out of scope:

- collector source code;
- SQLite schema;
- batch evidence files;
- comparison contracts;
- CI behavior;
- downloaded PDFs;
- any final novelty claim.

## Research-state structure

`research/RESEARCH_STATE.md` becomes the short current-state entry point. Detailed reasoning is split into focused documents:

```text
research/
├── RESEARCH_STATE.md
├── 01_SCOPE.md
├── 02_TOPOLOGY_TAXONOMY.md
├── 03_LOSS_PHYSICS.md
├── 04_PRIOR_ART_CLOSURE.md
├── 05_RESEARCH_HYPOTHESIS.md
├── 06_VALIDATION_PLAN.md
├── 07_BENCHMARKS.md
├── 08_DECISION_LOG.md
├── batches/
└── contracts/
```

## Current research boundary to record

General envelope:

- input: 12–24 Vdc;
- power: 1–3 kW;
- output: 220 Vac;
- phase: single phase;
- primary stress anchor: 12 V / 2 kW.

The research question is not simply high voltage gain or removal of a transformer. It is how average power, twice-line-frequency pulsating energy, reactive energy, resonant/circulating energy, and commutation energy should traverse or avoid the extreme-low-voltage high-current domain so that low-side RMS current exposure and total system loss are minimized.

## Taxonomy policy

Topology families are classified by dominant power path, not by every implementation feature.

The current working map uses nine main power-path families. Orthogonal features such as IPOS, modularization, matrix connection, CPT/capacitive isolation, current sharing, and active buffering are recorded as design dimensions rather than automatically becoming additional numbered families.

The Xi'an high-frequency-link work is treated as an important modern implementation of the direct high-frequency-link DC–AC family, not as the historical invention of that family.

## Novelty policy

Use explicit states:

- `CLOSED`: established prior art exists for the broad claim;
- `PARTIALLY_CLOSED`: adjacent/partial intersection exists;
- `OPEN_INTERSECTION`: current targeted search has not found a complete match;
- `NOVELTY_NOT_ESTABLISHED`: mandatory until closest-prior-art closure is complete.

The current candidate intersection is:

`12–24 V + 1–3 kW + 220 Vac + single phase + electric-field/capacitive main conversion + intentional bidirectional 2ω energy routing + low-voltage RMS/total-loss objective`.

This is not to be written as a first-ever claim.

## Validation policy

Validation proceeds in gates:

1. analytical scaling;
2. PLECS system-level energy-routing/RMS/loss validation;
3. LTspice switching-cell validation;
4. Ansys Maxwell/Q3D field and parasitic extraction;
5. parameter back-annotation into PLECS;
6. hardware prototype and fair benchmark.

The first simulation is intentionally mechanism-first: compare buffer OFF vs ON around an idealized impedance-transformation boundary before committing to a specific electric-field topology.

## Preservation policy

The prior `RESEARCH_STATE.md` remains available in Git history. The new split documents become the active working state. Formal literature claims remain subject to the repository's evidence and comparison-contract gates.

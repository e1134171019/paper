# GPT Adjudication — Direct-Scale Pareto Frontier Closure

Date: 2026-08-12

## Decision

- Research direction: `APPROVE_CONTINUE`
- Direct-scale multi-objective Pareto frontier: `AUTHORIZED`
- Existing COMP-HG-001 L5 core: retained as bounded members
- B004-CAND-0003 / DOI `10.1155/etep/9317966`: `L3_CONTEXT → L4_NUMERICALLY_VERIFIED` for source-locked direct-scale fields
- B004-CAND-0002 / DOI `10.1049/pel2.70039`: remains `L3_CONTEXT`
- Research Gap Candidate: `NOT_AUTHORIZED`
- Established Research Gap: `NOT_AUTHORIZED`
- Stopping rule: `NOT_MET`

## 1. Material correction: pel2.70039 efficiency role

The prior BATCH-004 note retained a 97.8% full-load efficiency descriptor as context. This pass resolves the evidence role more precisely:

- Table 2 labels **Experimental Efficiency = 96.5%**.
- The Figure 17 discussion attributes **97.8% at 200 W to PSpice simulation**.
- The conclusion repeats 97.8% wording, but it does not override the body/table role distinction.

Therefore:

- `96.5%` is the current experimental efficiency descriptor.
- `97.8%` is retained only as a simulation descriptor.
- any historical wording that could be read as measured 97.8% is `SUPERSEDED` by this review.

No historical file is overwritten; the correction is append-only and traceable.

## 2. pel2.70039 operating-point conflict remains open

The same source contains an unresolved prototype Vin conflict:

- Table 2: 30 V input;
- experimental narrative: 40 V input;
- conclusion: 30 V input.

The paper otherwise supports 400 V output, 200 W, 100 kHz, measured main-switch stress around 100 V, and maximum measured diode-stress context around 200 V.

Because the input operating point is conflict-typed, this record cannot be promoted to L4/L5 for direct frontier membership in this pass.

## 3. New L4 direct-scale record

DOI `10.1155/etep/9317966` now has sufficient source-locked hardware evidence for L4 on the promoted fields:

- 48 V → 400 V;
- 200 W;
- 100 kHz;
- duty 0.52;
- one active switch;
- author comparison table reports seven diodes, five capacitors, one magnetic core / four windings;
- continuous input current;
- common ground;
- measured main-switch stress approximately 100 V, i.e. approximately 0.25 Vout;
- main switch ZCS turn-on and ZVS turn-off; diodes ZCS turn-off;
- measured efficiency 95.6% at 200 W;
- calculated/loss-model efficiency 95.9% retained as a separate role.

It is **not** promoted to L5 because measured maximum diode-stress scalar is not locked, component-count basis requires normalization, and independent duplicate review remains missing.

## 4. Pareto interpretation

The current direct-scale set supports a multi-objective frontier study, not a scalar ranking.

Observed configurations include:

- very low main-switch stress with comparatively high diode stress;
- low main-switch stress achieved through larger passive/diode networks;
- active-clamp designs that trade an auxiliary switch for soft switching and stress control;
- single-switch designs with different common-ground and source-current properties.

These observations support retaining the narrow `RECURRING_BOUNDARY_CANDIDATE`: design burden can migrate across semiconductor stress, passive count, magnetic burden, source-current conditioning and integration constraints.

They do not establish a universal monotonic law or a research gap.

## 5. Component-count correction

Raw component integers are no longer eligible for cross-paper Pareto dominance unless count basis is aligned.

Example: DOI `10.1155/etep/9317966` reports `C=5` in its author comparison table, while the circuit description includes a snubber capacitor. This is treated as a counting-basis difference, not a source contradiction.

The frontier must therefore retain author-reported and schematic-recounted counts separately.

## 6. Independent-review gate failed, not passed

An independent Firecrawl agent was launched without the GPT frontier conclusion and was instructed to duplicate-extract three source papers. It failed because it could not access the publisher content in its own environment.

Therefore:

- the attempt is traceable;
- it is not counted as an independent review;
- same-GPT source cross-checking cannot replace it;
- `independence_missing` remains active.

## 7. Stopping rule

The stopping rule remains `NOT_MET` because:

1. B004-CAND-0002 has an unresolved prototype-input contradiction;
2. B004-CAND-0003 lacks a locked measured maximum diode-stress scalar for full frontier use;
3. component-count bases are not yet normalized across all direct-scale records;
4. genuine independent duplicate extraction is still missing;
5. backward/forward citation coverage remains partial;
6. marginal-yield saturation is not reached;
7. auxiliary/thermal/measurement boundaries remain unmatched for efficiency dominance.

## 8. Authorized next node

`DIRECT-SCALE FRONTIER NUMERIC CLOSURE + INDEPENDENT REVIEW`

Priority:

1. resolve or permanently conflict-type the pel2.70039 Vin boundary using the highest-specificity experimental locator/editorial record;
2. lock maximum measured diode stress for `10.1155/etep/9317966`;
3. recount component classes for all direct-scale records under one frozen count basis;
4. obtain genuinely independent duplicate extraction;
5. advance backward/forward citation graph coverage and marginal-yield tracking;
6. only then run a formal non-dominance/Pareto calculation.

## Guardrails

- no efficiency leaderboard;
- no overall-best topology claim;
- no causal claim that ZVS/ZCS causes the observed cross-paper efficiency difference;
- no conversion of upper bounds/approximations to exact scalars;
- no silent resolution of source conflicts;
- no count comparison across incompatible count bases;
- no Research Gap Candidate while the stopping rule is not met.

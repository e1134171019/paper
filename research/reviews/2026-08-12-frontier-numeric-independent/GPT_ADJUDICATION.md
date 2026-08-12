# GPT Adjudication — Direct-Scale Frontier Numeric Closure + Independent Review

Date: 2026-08-12

## Decision

- Research direction: `APPROVE_CONTINUE`
- Unified component recount basis: `CLOSED`
- DOI `10.1049/pel2.70039` Vin issue: `PERMANENT_SOURCE_CONFLICT_TYPED`
- DOI `10.1155/etep/9317966` measured maximum diode-stress scalar: `UNRESOLVED`
- Independent duplicate extraction: `PARTIAL_PASS_TWO_RECORDS`
- Full-frontier independent-review gate: `NOT_COMPLETE`
- Conservative dominance screen: `COMPLETED`
- Formal all-objective Pareto non-dominance calculation: `NOT_AUTHORIZED_YET`
- Research Gap Candidate: `NOT_AUTHORIZED`
- Stopping rule: `NOT_MET`

## 1. pel2.70039 is closed as a contradiction, not reconciled

The input-voltage issue cannot be lawfully forced to a single scalar:

- the significant-parameters table reports 30 V;
- the conclusion reports a 30 V design point;
- the experiment-specific narrative describes the implemented laboratory prototype at 40 V;
- 400 V output, 200 W and 100 kHz are otherwise consistent.

The highest-specificity experimental narrative is important evidence for 40 V, but it does not erase the conflicting table/conclusion record. The canonical field is therefore retained as `30|40`, type `conflict`.

This satisfies the closure action `resolve or permanently conflict-type`; it does **not** satisfy the condition for L4/L5 frontier membership.

The efficiency roles remain separated:

- 96.5% = experimental efficiency descriptor;
- 97.8% at 200 W = PSpice simulation descriptor.

## 2. 10.1155/etep/9317966 remains L4, not L5

Source-locked direct-scale fields remain strong:

- 48 V → 400 V;
- 200 W;
- 100 kHz;
- duty ratio 0.52;
- one controlled switch;
- common ground;
- continuous input current;
- measured main-switch maximum voltage approximately 100 V;
- switch ZCS turn-on + ZVS turn-off;
- diode ZCS turn-off;
- measured efficiency 95.6% at 200 W;
- calculated loss-model efficiency 95.9%, stored separately.

However, the publisher text supplied for Figure 11(b-h) does not state an exact maximum **measured** diode-voltage scalar. The waveforms' existence and ZCS behavior do not authorize substituting an analytical stress, device rating or visually guessed number.

Therefore max measured diode stress remains `unresolved`, and the record remains L4.

## 3. Component count is now normalized

The frontier now uses `SCHEMATIC_DISCRETE_POWER_STAGE_V1`.

Normalized structural counts:

| record | switches | diodes | capacitors | cores | windings |
|---|---:|---:|---:|---:|---:|
| PC-CAND-0024 | 1 | 4 | 5 | 2 | 3 |
| PC-CAND-0027 | 1 | 8 | 8 | 1 | 2 |
| PC-CAND-0028 | 1 | 4 | 5 | 2 | 4 |
| PC-CAND-0030 | 2 | 4 | 5 | 1 | 2 |
| B004-CAND-0002 | 2 | 3 | 5 | 2 | 3 |
| B004-CAND-0003 | 1 | 7 | 6 | 1 | 4 |

For B004-CAND-0003, the source comparison table's `C=5` remains preserved, while the unified schematic basis counts the separately named snubber capacitor Cs and therefore records 6. This is a counting-policy difference, not a contradiction.

## 4. Independent review materially advanced but is not complete

A separate Firecrawl model (`spark-1-pro`) was given a neutral source packet for the two disputed/new records without GPT's frontier conclusion.

Its extraction independently reproduced the material findings:

- `pel2.70039`: Vin conflict; 96.5% experiment vs 97.8% simulation; ~100 V switch stress; ~200 V diode context; topology counts.
- `9317966`: 48→400 V / 200 W / 100 kHz; main stress ~100 V; 95.6% measured; diode max scalar unresolved; author C=5 vs schematic C=6 basis difference.

The agent job itself ended with `status: failed` because of its environment, but the failure payload contained the completed extraction and used zero credits. This is preserved exactly as `PARTIAL_INDEPENDENT_AGREEMENT_JOB_FAILED_AFTER_OUTPUT`.

Classification:

- independent model/context extraction for two records: pass;
- source acquisition independent of GPT: no;
- all-six-record reviewer coverage: no.

The project-level independent-review gate therefore remains open.

## 5. Dominance screen result

A conservative screen was performed on typed stress and structural metrics. No strict dominance certificate was found among the current usable direct-scale records.

Examples:

- PC-CAND-0028 has very low main-switch stress and low diode/capacitor count, but higher maximum diode stress and higher magnetic burden than PC-CAND-0027.
- PC-CAND-0030 has low magnetic burden and four diodes/five capacitors, but requires an auxiliary controlled switch and its main-switch stress is only upper-bounded.
- PC-CAND-0027 has lower maximum diode stress than PC-CAND-0028/0030 but a substantially larger diode/capacitor network.

This supports the `burden redistribution` interpretation.

It does **not** prove that every record is Pareto-optimal. Missing values, bounds and non-scalar integration criteria prevent that inference.

Efficiency is excluded from dominance because auxiliary, thermal and measurement boundaries remain unmatched.

## 6. Search saturation moved further away, not closer

The frozen 2025+ direct-scale query family produced additional material yield.

Most importantly, DOI `10.1038/s41598-026-64796-y`, published 2026-08-02, reports a new 25 V → 400 V, 200 W soft-switched trans-inverse hardware prototype with minimal-component positioning. It overlaps an existing author/evidence family and therefore cannot automatically increase independent evidence count, but it is a new frontier-relevant topology record and requires audit.

Another unincorporated direct-scale record, DOI `10.1038/s41598-025-90093-1`, reports 25 V → 400 V, 200 W, 50 kHz hardware with measured semiconductor stresses.

Therefore `marginal_yield > 0` and search saturation is false.

## 7. Why formal Pareto computation is still withheld

A formal non-dominance calculation across the frozen objective set is not authorized because:

1. PC-CAND-0024 lacks measured maximum diode stress;
2. B004-CAND-0003 lacks measured maximum diode stress;
3. pel2.70039 remains operating-point conflicted and excluded;
4. several main-stress values are upper bounds rather than exact points;
5. common-ground/input-ripple fields remain unresolved for multiple core records;
6. newly discovered direct-scale hardware has not yet been audited;
7. independent reviewer coverage is incomplete;
8. efficiency measurement boundaries are unmatched.

A `NO_STRICT_DOMINANCE_CERTIFICATE` screen is valid; an all-record `Pareto-optimal` declaration is not.

## 8. Authorized next node

`DIRECT-SCALE FRONTIER EXPANSION + MISSING-STRESS CLOSURE`

Priority:

1. audit DOI `10.1038/s41598-026-64796-y` under the frozen typed frontier contract and family-dedup rule;
2. audit DOI `10.1038/s41598-025-90093-1` under the same contract;
3. attempt image/figure-level locking of measured maximum diode stress for `10.1155/etep/9317966` through a lawful visual/fulltext route;
4. attempt the same missing diode-stress field for PC-CAND-0024 if the source provides it;
5. independently duplicate-extract the four current L5 core records;
6. rerun dominance only after the frontier set and required fields stabilize.

## Guardrails

- no efficiency leaderboard;
- no global best-topology claim;
- no coercion of upper bounds into exact values;
- no silent reconciliation of source contradictions;
- no cross-paper count comparison outside the frozen count basis;
- no claim that absence of dominance certificates proves Pareto optimality;
- no Research Gap Candidate while stopping and independent-review gates remain open.
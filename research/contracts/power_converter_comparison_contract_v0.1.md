# Power Converter Comparison Contract v0.1

Date: 2026-08-12
Status: active research contract
Applies to: Power-converter evidence staged under `research/batches/`
Upstream method: Research Evidence Pipeline v0.1
Upstream schema: Energy Conversion Evidence Schema v0.1

## 1. Purpose

This contract defines when independently published power-converter evidence may be compared across papers.

It exists to prevent invalid scalar rankings caused by mixing different metric definitions, electrical/system boundaries, operating points, prototype scales, or measurement methods.

A paper being `L4_NUMERICALLY_VERIFIED` is necessary but not sufficient for cross-paper comparison.

## 2. L5 promotion rule

A record may become `L5_COMPARISON_READY` only when all of the following are true:

1. The record is already `L4_NUMERICALLY_VERIFIED`.
2. It is assigned to a named comparison set with an explicit research question.
3. The set contains evidence from at least two independent papers.
4. The target metric definition is semantically matched.
5. The electrical/system boundary is matched or a documented normalization makes it equivalent.
6. Operating conditions required by the set are present and within the set's declared admissible range.
7. Direction, topology role, isolation role, and processed-power boundary are explicit.
8. Peak/full-load/average/curve-point semantics are not mixed.
9. Included/excluded auxiliary losses are known or the set explicitly excludes efficiency ranking.
10. Measurement basis and evidence locators are sufficient to reproduce the comparison decision.

Failure of any hard gate keeps the record below L5 for that comparison set.

## 3. Comparison modes

### 3.1 DIRECT_QUANTITATIVE

Used for scalar or curve comparison of the same physical metric.

Required:
- same metric definition;
- same numerator/denominator meaning;
- compatible system boundary;
- compatible direction;
- compatible operating-point basis;
- declared normalization for units and scale;
- no unresolved measurement-boundary conflict.

A leaderboard is permitted only inside a `DIRECT_QUANTITATIVE` set.

### 3.2 BOUNDED_TRADEOFF

Used to compare mechanisms where one or more design variables intentionally differ, for example:

`switching_frequency ↔ soft_switching ↔ efficiency ↔ power_density`

or

`processed_power_fraction ↔ system_efficiency ↔ voltage_range`.

This mode may compare structured dimensions but must not collapse them into a single best/worst ranking unless the direct-quantitative gates are separately satisfied.

### 3.3 CONTEXT_ONLY

Used when papers are useful references but their numerical claims are not contract-compatible. Context-only evidence never causes L5 promotion.

## 4. Mandatory comparison-set fields

Each comparison set must declare:

- `comparison_set_id`
- `research_question`
- `comparison_mode`
- `target_metric`
- `metric_definition`
- `boundary_scope`
- `power_flow_direction`
- `isolation_scope`
- `topology_scope`
- `input_voltage_scope`
- `output_voltage_scope`
- `power_scope`
- `switching_frequency_scope`
- `load_point_basis`
- `semiconductor_scope`
- `auxiliary_loss_policy`
- `measurement_basis`
- `normalization_rule`
- `admissible_mismatch`
- `prohibited_inference`
- `minimum_independent_papers`

If a field is not relevant, it must be explicitly marked `not_applicable`; it must not be silently omitted.

## 5. Power-converter normalization rules

### Efficiency

Keep distinct:
- converter efficiency;
- complete multi-stage converter efficiency;
- partial-power system/global efficiency;
- direction-specific charging efficiency;
- direction-specific discharging efficiency;
- calorimetric efficiency;
- wall-plug/end-to-end efficiency where applicable.

`modeling_accuracy` is never an efficiency metric.

### Partial-power processing

A partial-power comparison must preserve:
- processed power fraction / partial power ratio;
- bypass/direct-path boundary;
- converter-internal efficiency versus total-system efficiency;
- input/output voltage relationship that determines processed fraction;
- power-flow direction.

A high system efficiency obtained because most power bypasses the converter must not be ranked directly against a full-power converter efficiency.

### Power density

Unit conversion is insufficient by itself. The compared records must also have compatible volume definitions, for example whether cooling, magnetics, enclosure, control, and auxiliary supplies are included.

### Soft switching

ZVS/ZCS claims must retain:
- which switches/diodes achieve it;
- load/voltage range;
- switching frequency;
- dead-time or modulation conditions when material.

A statement such as `full-range ZVS` is not equivalent to an isolated waveform at one operating point.

### Voltage gain and stress

Keep design target and measured value separate. Normalized voltage stress may be compared only when the normalization denominator is the same physical voltage boundary.

## 6. Hard prohibitions

The following comparisons are invalid unless a later contract version supplies an explicit normalization:

- model accuracy versus conversion efficiency;
- partial-power system efficiency versus full-power converter efficiency;
- peak efficiency versus full-load efficiency as if they were identical;
- charging and discharging efficiencies collapsed into one value;
- design-target voltage versus measured voltage without labeling;
- power density values with incompatible volume boundaries;
- efficiency values with materially different auxiliary-loss inclusion presented as a flat ranking;
- abstract-only numerical claims promoted as verified full-text evidence;
- search-result absence interpreted as a Research Gap.

## 7. BATCH-001 application policy

BATCH-001 is used as the first contract test.

The contract is intentionally conservative: if the existing evidence cannot form a valid set, the output is `blocked` or `context_only`, not an artificially populated comparison matrix.

`comparison_sets.csv` records the instantiated sets and their gate results.

No BATCH-001 paper is promoted to L5 solely by adoption of this contract. Promotion requires an instantiated set that passes all relevant gates.

## 8. Research-gap boundary

A comparison-set failure is an evidence-acquisition requirement, not itself a Research Gap.

Examples:
- missing processed-power ratio → evidence extraction/search target;
- unmatched power range → targeted literature acquisition need;
- unresolved full text → source-resolution need;
- no second comparable paper → comparison-set insufficiency.

Only after a sufficiently populated comparison-ready set exists may repeated trade-offs, contradictions, scale limits, or condition limits be evaluated as Research Gap candidates.

## 9. SSOT boundary

This contract and batch CSV files are versioned research/audit artifacts. They do not replace the canonical SQLite store. Any future schema migration for comparison sets must reuse or extend the existing SSOT rather than create an independent authoritative database.
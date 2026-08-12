# Comparison Contract Application — Li / He / Luo 2023

Date: 2026-08-12
Target: `10.1007/s43236-022-00564-1`
Comparison set: `COMP-HG-001`
Mode: `BOUNDED_TRADEOFF`

## Research question

For non-isolated high-gain DC–DC converters in the active direct-scale acquisition region, what trade-off exists among gain, semiconductor stress, soft-switching coverage, structural burden and measured efficiency descriptors?

This application does not authorize a flat efficiency leaderboard.

## Gate application

### L4 prerequisite — PASS

The target has a readable complete article, hardware prototype and claim-critical numerical locators.

Locked prototype boundary:

- 20 V input;
- 400 V output;
- 200 W rated output;
- 50 kHz;
- forward step-up;
- non-isolated.

### Metric semantics — PASS FOR BOUNDED TRADE-OFF

- voltage/output boundary is explicit;
- controlled-switch measured voltage stress is explicit: 117 V;
- normalized controlled-switch stress is 0.2925 Vout;
- exact measured diode maximum is unresolved and remains typed as unresolved;
- theoretical diode stress is separately typed, not presented as measured;
- soft-switching coverage is `NOT_REPORTED`, not inferred;
- measured peak efficiency and full-load efficiency are kept as distinct covariates.

### Structural boundary — PASS

- one controlled switch;
- six discrete diodes;
- five capacitors;
- two magnetic cores under the project recount basis;
- three windings under the declared basis;
- continuous input current;
- common ground.

### Operating-condition boundary — PASS WITH EXCLUDED CONFLICT

A local article inconsistency exists: Section 5 states `Io = 0.2 A` alongside 400 V, whereas Table 2 declares 200 W rated power. This sentence would imply 80 W and is therefore not used as a comparison-defining full-load value.

The full-load comparison descriptor instead uses independently source-locked fields:

- Table 2 rated output power: 200 W;
- Section 5.2 tested load sweep: 20–200 W;
- Section 5.2 full-load efficiency: 93.7% at 200 W.

The conflict is retained in the record and not numerically repaired.

### Measurement gate — PASS FOR CURRENT SET

The frozen direct-scale protocol requires at least one measured semiconductor-stress or soft-switching locator. Li provides a measured switch-stress locator at rated conditions.

The missing exact measured diode maximum reduces completeness but does not invalidate the current bounded-tradeoff admission because:

- it remains explicitly unresolved;
- it is not used to claim measured-diode dominance;
- existing bounded L5 members preserve the same distinction between measured, theory-at-prototype and unresolved diode fields.

### Efficiency ranking gate — NOT AUTHORIZED

The paper's efficiency curve is valid descriptive evidence, but auxiliary/control/cooling/thermal boundaries across the frontier remain insufficiently harmonized. Peak 95.2% and full-load 93.7% are retained as descriptors only.

## Result

`COMP-HG-001 target status = L5_COMPARISON_READY / BOUNDED_MEMBER`

Allowed uses:

- gain/stress/structural burden bounded comparison;
- measured switch-stress normalization;
- descriptive efficiency/load information;
- evidence-family diversity analysis.

Prohibited uses:

- claim that theoretical diode stress is measured;
- claim a topology-wide measured diode maximum;
- infer hard switching from absence of a target soft-switch claim;
- rank efficiency against other papers without matching measurement/auxiliary boundaries;
- repair the `Io = 0.2 A` inconsistency silently;
- infer Pareto closure or a Research Gap from this promotion.

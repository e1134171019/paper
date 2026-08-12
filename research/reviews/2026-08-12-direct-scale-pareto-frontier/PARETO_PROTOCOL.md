# Direct-Scale Pareto Frontier Closure — Protocol

Date: 2026-08-12
Status: frozen for this review pass
Parent: BATCH-004 Falsification + Coverage Closure

## Research objective

For experimentally validated non-isolated high-step-up DC-DC converters near 380–400 V output and 150–300 W output power, characterize a bounded multi-objective frontier rather than rank a single best topology.

## Inclusion window

- primary journal hardware evidence;
- non-isolated high-step-up DC-DC;
- output voltage approximately 380–400 V for direct frontier membership;
- output power approximately 150–300 W;
- prototype switching frequency recorded;
- at least one measured semiconductor-stress or soft-switching locator;
- lawful/readable source path known for claim-critical promotion.

Records outside one field may remain `CONTEXT_ONLY`; they are not silently coerced into direct frontier membership.

## Frontier dimensions

1. input/output voltage and voltage gain;
2. output power and switching frequency;
3. main-switch voltage stress normalized to measured/declared output voltage;
4. maximum diode voltage stress when measured and text/figure locked;
5. active-switch count;
6. diode count;
7. capacitor count with an explicit counting basis;
8. magnetic-core and winding burden;
9. input-current behavior;
10. common-ground capability;
11. per-device soft-switching coverage;
12. measured efficiency descriptor with measurement/simulation role separated;
13. auxiliary, cooling, thermal and measurement boundary when available.

## Typed-value rule

Every frontier value must carry one of:

- `exact`
- `approx`
- `upper_bound`
- `range`
- `conflict`
- `unresolved`

Bounds and approximations must never be converted into exact scalars for dominance tests.

## Component-count rule

No cross-paper component-count comparison is allowed without `count_basis`. At minimum distinguish:

- `author_reported_count`
- `main_power_path_count`
- `schematic_discrete_count`
- `snubber_or_auxiliary_excluded`

If two papers use different conventions, the count is `NON_COMPARABLE_UNTIL_RECOUNTED`, not a numerical contradiction.

## Efficiency rule

Measured, calculated/loss-model and simulation efficiency are separate evidence roles. Peak, full-load and nominal points are separate operating conditions. Efficiency is a descriptive frontier covariate in this pass; no efficiency leaderboard is authorized because auxiliary/thermal/measurement boundaries remain unmatched.

## Promotion gates

`L4_NUMERICALLY_VERIFIED` requires claim-critical prototype conditions and the promoted numerical field(s) to be source-located and role-correct.

`L5_COMPARISON_READY` additionally requires the active comparison contract to pass, including typed stress fields and no unresolved operating-condition conflict on the comparison-defining point.

## Research-gap gate

This pass cannot authorize a Research Gap Candidate unless all of the following pass simultaneously:

- stopping-rule-compliant search coverage;
- backward and forward citation screening sufficiently closed;
- genuine independent duplicate review;
- stable direct-scale comparator set;
- contradiction handling complete;
- comparison boundaries compatible for the proposed claim.

A newly found paper or a search miss cannot by itself establish a gap.

# Energy Conversion Efficiency Research Reframe

Date: 2026-08-14
Status: active research reframe; no Research Gap authorization
Parent research state: `research/li-he-luo-2023-full-vector-stopping-round-3`
Upstream method: Research Evidence Pipeline v0.1
Upstream schema: Energy Conversion Evidence Schema v0.1
Comparison contract: `research/contracts/power_converter_comparison_contract_v0.1.md`

## 1. Mother topic

The research mother topic is no longer a topology label such as `High-Gain DC-DC` or `inverter`.

The active mother topic is:

`electrical energy-conversion efficiency / total conversion-loss minimization`

The primary research object is the complete power-processing path and the way architecture redistributes loss, current stress, semiconductor stress, magnetic burden, energy buffering and control burden.

## 2. Current research hierarchy

```text
Mother topic
Electrical energy-conversion efficiency / total loss minimization
        |
        v
Research direction
Power-processing path and loss distribution
        |
        +--> How many conversion stages process the power?
        +--> What fraction of total power is processed in each stage?
        +--> Where are semiconductor, magnetic, capacitor and auxiliary losses created?
        +--> Can loss be reduced by topology, modulation, soft switching, partial processing or stage integration?
        |
        v
Experimental / application boundary
Low-voltage DC source -> isolated step-up conversion -> high-voltage DC link -> single-phase DC-AC
```

The industrial reference architecture that motivated this boundary is intentionally generalized. Product names, proprietary schematics and company-specific implementation details are not stored in this public repository.

## 3. Relationship to the existing High-Gain evidence program

The existing `COMP-HG-001` work remains valid bounded evidence. It is not deleted or reinterpreted as direct inverter evidence.

Its new role is:

- evidence about low-voltage-to-high-voltage conversion burden;
- evidence about semiconductor stress reduction versus passive/magnetic/diode burden;
- evidence about hard/soft-switching trade-offs;
- evidence about why peak efficiency alone is insufficient for architecture selection.

The existing High-Gain frontier is therefore a supporting evidence branch under the wider energy-conversion question, not the final research title.

## 4. New active evidence line

The next targeted line is low-voltage, high-current, high-frequency isolated front-end conversion, with first priority on current-fed push-pull and closely related current-fed isolated families.

Primary questions:

1. How does current-fed push-pull reduce or redistribute low-voltage high-current conduction burden?
2. How do leakage-inductance spikes, clamp/commutation methods and circulating current affect total loss?
3. Under wide input and load ranges, where is ZVS/ZCS retained or lost?
4. How do RMS current, transformer utilization, flux balance, magnetic volume and switching stress change with modulation and phase count?
5. Does a locally improved front end reduce complete-system loss after the DC link and inverter stage are included?

This line is staged as `BATCH-005`.

## 5. Two comparison scopes

### COMP-CFPP-001

Scope: current-fed push-pull / push-pull DAB / closely related current-fed isolated DC-DC converters.

Purpose: compare loss mechanisms and operating-range burden without forcing a single efficiency ranking.

### COMP-ISO-DCAC-001

Scope: isolated low-voltage DC to single-phase AC systems.

Purpose: compare conventional two-stage conversion against integrated/single-stage/high-frequency-link approaches at a matched system boundary.

This set must keep stage efficiency and end-to-end system efficiency separate.

## 6. Evidence-state rule

The 2026-08-14 IEEE result list is discovery evidence only unless a paper already has a separately locked full-text audit.

New records enter as `candidate_metadata` or `evidence_linked_pending_repo_normalization`.

They must not be promoted directly to L4/L5 from title, abstract, citation count or search-result text.

Required progression remains:

```text
candidate metadata
-> source / DOI resolution
-> legal readable full text
-> exact evidence locators
-> numerical verification
-> comparison-contract check
-> L5 comparison-ready only when all gates pass
```

## 7. Prohibited inferences

- fewer stages = automatically higher efficiency;
- single-stage = automatically better than two-stage;
- soft switching = automatically the cause of higher measured efficiency;
- lower switch voltage stress = lower total converter loss;
- peak efficiency from one boundary = direct rank against another boundary;
- search miss = Research Gap;
- product architecture = academic novelty.

## 8. Current Research Gap status

`Research Gap Candidate = NOT_AUTHORIZED`.

Reason:

- the new current-fed isolated line is still in candidate acquisition;
- the prior High-Gain stopping rule was not met;
- independent review of the prior frontier remained incomplete;
- the new system-level comparison sets are not yet populated with contract-compatible full-text evidence.

## 9. Authorized next work

1. Resolve primary metadata and legal full-text access for BATCH-005 priority papers.
2. Extract Vin, Vout, Pout, switching frequency, topology, phase count and transformer structure.
3. Extract efficiency curves with exact load points and measurement boundary.
4. Extract switch/diode stress, RMS/circulating current and ZVS/ZCS range.
5. Separate direct low-voltage comparators from higher-voltage or higher-power mechanism context.
6. Import already audited conversation evidence only after source/locator provenance is restored inside the repository workflow.
7. Run counter-search after the first comparable current-fed isolated set exists.
8. Keep formal Pareto and Research Gap locked until comparison, stopping and independence gates are satisfied.

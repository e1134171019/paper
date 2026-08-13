# GPT Adjudication — Habibi + Jazi Vector Closure / Targeted Stopping Test

Date: 2026-08-13

## Decision snapshot

- research direction: `APPROVE_CONTINUE_TARGETED_ONLY`;
- bounded L5 records: `11`;
- independent L5 evidence families: `6`;
- Habibi: `L4_DIRECT_VECTOR_THEORY_CLOSED_MEASURED_VECTOR_INCOMPLETE`;
- Habibi independent-family credit: `NOT_YET_ELIGIBLE`;
- Jazi: `L4_DIRECT_FULL_STRUCTURE_AUDITED_SWITCH_VECTOR_INCOMPLETE`;
- Jazi independent-family credit: `NO_ADDITIONAL_CREDIT_RELATED_ADIB_PROGRAM`;
- Salehi/Varjani 2026: `L3_TARGETED_POWER_BOUNDARY_UNRESOLVED`;
- broad keyword search: `STOPPED`;
- targeted search saturation: `NOT_MET`;
- independent interpretation: `NOT_COMPLETE`;
- `independence_missing=true`;
- formal all-objective Pareto: `NOT_AUTHORIZED_YET`;
- Research Gap Candidate: `NOT_AUTHORIZED`.

## Habibi decision

The analytical semiconductor vector is now numerically closed at the prototype point without changing evidence type. Using the paper's gain equation and prototype turns ratios gives recalculated D ~= 0.52. The theoretical maximum controlled-switch stress is about 0.1042 Vout for both S1 and Sc, and the theoretical maximum diode stress is 0.625 Vout.

Experimentally, only S1 is text-locked at almost 45 V, or about 0.1125 Vout. The exact measured Sc scalar and measured maximum diode scalar remain unresolved. Because multi-switch comparison uses the maximum controlled-switch vector, the record stays L4 rather than being promoted on S1 alone.

## Jazi decision

The 2025 IEEE Access paper is a genuine direct-scale 40 V -> 400 V / 200 W / 100 kHz experiment. The common schema now records 2 controlled switches, 4 discrete diodes, 6 discrete capacitors including the external snubber capacitor, 2 magnetic structures and 4 total windings.

The paper text-locks S1 at 120 V, or 0.30 Vout, and verifies wide-load soft-switching behavior, all-diode ZCS turn-off, continuous input current, shared ground and 96.5% measured full-load efficiency. However, the exact auxiliary-switch operational-voltage scalar and exact measured maximum diode scalar remain unresolved. Device ratings are not substituted.

The paper is therefore kept at L4. Its sub-lineage is `JAZI_KHORASANI_ADIB_ZVT`, but no new independent-family credit is assigned because of repeated core Ehsan Adib authorship and continuity with the existing Adib/Farzanehfard high-step-up soft-switching program represented by PC-CAND-0030.

## Stopping-test decision

A narrow stopping check found a different-author 2026 Scientific Reports experiment, DOI `10.1038/s41598-026-40326-8`, at 24 V -> 400 V. The primary article text-locks an experimentally shown switch stress of 62 V, D1 = 200 V, D2 = 300 V and 96.6% full-load efficiency. It also states two active switches with ZCS operation.

The exact rated/full-load Pout in watts was not reproducibly locked by the current primary HTML retrieval. This record is therefore not admitted to the frozen 150-300 W direct-scale set, but it is sufficiently close and structurally relevant that the stopping gate cannot be closed while its power boundary is unresolved.

Targeted marginal yield is `POSITIVE_UNRESOLVED` and `TARGETED_SEARCH_SATURATION_NOT_MET`.

## Pareto / research-gap decision

The burden-redistribution hypothesis remains supported: lowering controlled-switch stress can move burden into diode voltage, passive count, magnetic/winding structure, active-clamp/ZVT/snubber circuitry, input-current conditioning, common-ground constraints or control complexity. It is not promoted to a universal law.

Formal all-objective Pareto and a formal Research Gap remain withheld because:
1. independent review is missing;
2. PC-CAND-0024 and DOI `10.1155/etep/9317966` still lack exact maximum measured diode scalars;
3. Habibi and Jazi still have incomplete measured controlled-switch / diode vectors;
4. the new Salehi/Varjani candidate has an unresolved rated-power boundary;
5. several L5 members use theory-at-prototype or upper-bound stress evidence rather than complete measured vectors;
6. efficiency boundaries remain heterogeneous and efficiency stays descriptor-only.

## Authorized next node

`SALEHI POWER-BOUNDARY CLOSURE / FINAL TARGETED STOPPING RECHECK`

Only:
1. close the rated/full-load Pout of DOI `10.1038/s41598-026-40326-8` using a reproducible primary locator;
2. if outside 150-300 W, demote to context and rerun stopping immediately;
3. if inside 150-300 W, finish the common component / controlled-switch vector and lineage audit, then rerun stopping;
4. retry independent review only when an approved functioning route is available;
5. do not return to broad high-step-up keyword expansion.

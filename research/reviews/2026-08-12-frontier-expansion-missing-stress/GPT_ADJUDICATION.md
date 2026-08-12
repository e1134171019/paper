# GPT Adjudication — Direct-Scale Frontier Expansion + Missing-Stress Closure

Date: 2026-08-12

## Decision
- Research direction: `APPROVE_CONTINUE`
- Direct-scale bounded L5 membership: `EXPANDED_4_TO_5`
- New L5 member: DOI `10.1038/s41598-025-90093-1`
- DOI `10.1038/s41598-026-64796-y`: `L3_CONTEXT_SOURCE_CONFLICT`
- Controlled-switch stress model: `UPGRADED_TO_VECTOR_PLUS_MAX`
- DOI `10.1155/etep/9317966` measured maximum diode stress: `UNRESOLVED`
- PC-CAND-0024 measured maximum diode stress: `UNRESOLVED`
- New-candidate independent review: `FAILED_NO_SOURCE_ACCESS`
- Full-frontier independent-review gate: `NOT_COMPLETE`
- Formal all-objective Pareto calculation: `NOT_AUTHORIZED_YET`
- Research Gap Candidate: `NOT_AUTHORIZED`
- Stopping rule: `NOT_MET`

## 1. New bounded member
DOI `10.1038/s41598-025-90093-1` matches the direct-scale hardware band and has source-locked experimental conditions:
- 25 V → 400 V
- 200 W
- 50 kHz
- duty ≈ 0.51
- two controlled MOSFETs
- measured switch stresses ≈ 56 V and 110 V
- five measured diode stresses with maximum ≈ 235 V
- common ground
- continuous low-ripple input current
- measured full-load efficiency ≈ 95.9%

Because auxiliary/thermal/measurement efficiency boundaries are not normalized against every existing member, the paper is admitted only to `BOUNDED_TRADEOFF`. No efficiency leaderboard is authorized.

## 2. Why stress-vector normalization is required
A singular main-switch metric would characterize the new paper by the lower S1 stress (~56 V = 0.14 Vout) while hiding S2 (~110 V = 0.275 Vout). For multi-switch topologies, the frontier therefore preserves the vector and screens on the maximum controlled-switch stress. Existing single-switch records are unchanged in substance.

## 3. 2026 minimal-component paper remains context
DOI `10.1038/s41598-026-64796-y` is highly frontier-relevant and reports 25 V → 400 V hardware, 50 kHz operation, low component count and measured switch stress around 54 V. However the early-access/accepted manuscript contains a material output-power contradiction: abstract/Table IV/full-load-efficiency context identify 200 W while an experimental narrative says 250 W.

This is not reconciled by inference. Canonical Pout is stored as `200|250`, type `conflict`, and the paper remains outside the formal frontier. The manuscript also lacks a text-locked measured maximum diode-voltage scalar; PDF screenshot verification was attempted but unavailable.

## 4. Missing-stress closure result
The requested closure pass did not produce a lawful measured maximum diode-stress scalar for either:
- DOI `10.1155/etep/9317966`, or
- PC-CAND-0024 / DOI `10.1049/iet-pel.2015.0923`.

Both fields remain unresolved. Analytical values, device ratings and visual guesses are prohibited substitutes.

## 5. Independence and evidence-family credit
The new 2025 member includes author overlap with the existing Hasanpour-related frontier literature. It is admitted as a topology record, but it receives no additional independent-family credit until family dedup is explicitly adjudicated.

A neutral Firecrawl independent-review job was attempted for both new Nature records but failed before source acquisition. Therefore no new independent confirmation is claimed.

## 6. Frontier status
Current formal bounded members:
1. PC-CAND-0024
2. PC-CAND-0027
3. PC-CAND-0028
4. PC-CAND-0030
5. FEXP-CAND-0001 / DOI `10.1038/s41598-025-90093-1`

Context/excluded records include:
- B004-CAND-0002: permanent Vin conflict
- B004-CAND-0003: L4, measured max diode stress unresolved
- FEXP-CAND-0002: Pout conflict and measured max diode stress unresolved

## 7. Why final Pareto is still withheld
An all-objective Pareto declaration is not yet authorized because:
1. measured maximum diode stress is missing for PC-CAND-0024;
2. measured maximum diode stress is missing for B004-CAND-0003;
3. the 2026 direct-scale record is operating-point conflicted;
4. several stress values are bounds, not exact points;
5. family-independence dedup for the new L5 member is pending;
6. full-frontier independent duplicate extraction is incomplete;
7. efficiency boundaries remain unmatched;
8. direct-scale literature is still yielding new records.

A conservative pairwise/no-dominance screen may continue, but absence of a dominance certificate is not proof that every record is Pareto-optimal.

## 8. Authorized next node
`FRONTIER STABILIZATION + INDEPENDENT CORE REVIEW`

Priority:
1. monitor/fetch the final edited version of DOI `10.1038/s41598-026-64796-y` and re-check the 200/250 W conflict;
2. independently duplicate-extract all five bounded L5 members using a reviewer with successful source access;
3. perform explicit evidence-family dedup for Hasanpour-overlap records;
4. pursue figure-level lawful diode-stress closure for PC-CAND-0024 and `10.1155/etep/9317966` without visual guessing;
5. rerun frozen direct-scale search until marginal yield approaches the predefined stopping condition;
6. only then execute interval-aware multi-objective Pareto classification.

## Guardrails
- no efficiency leaderboard;
- no global best-topology claim;
- no single-main-switch metric for multi-switch topologies;
- no coercion of bounds/conflicts into exact values;
- no inferred diode peak from device rating or unverified figure image;
- no Research Gap Candidate while stopping and independent-review gates remain open.

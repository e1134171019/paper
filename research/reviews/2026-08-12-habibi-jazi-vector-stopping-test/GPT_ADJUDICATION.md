# GPT Adjudication — Habibi + Jazi Vector Closure / Targeted Stopping Test

Date: 2026-08-12

## Decision

- Research direction: `APPROVE_CONTINUE_TARGETED_ONLY`
- Bounded L5 records: `11`
- Independent L5 evidence families: `6`
- Habibi DOI 10.1109/TPEL.2023.3344719: `L4_THEORY_VECTOR_CLOSED_MEASURED_VECTOR_INCOMPLETE`
- Habibi L5 promotion: `NOT_AUTHORIZED`
- Jazi DOI 10.1109/ACCESS.2025.3573936: `L4_DIRECT_VECTOR_PARTIAL`
- Jazi family candidate: `JAZI_KHORASANI_ZVT_CI_VM`
- Jazi collapse into MOLAVI_SOFTSWITCH: `NO`
- Jazi independent L5 family credit: `NOT_YET_ELIGIBLE`
- new targeted direct-scale candidates: `10.3390/pr11041087; 10.1088/2631-8695/ae8f9a`
- targeted marginal yield: `POSITIVE`
- targeted search saturation: `NOT_MET`
- independent review: `NOT_COMPLETE`
- `independence_missing=true`
- formal all-objective Pareto: `NOT_AUTHORIZED_YET`
- Research Gap Candidate: `NOT_AUTHORIZED`

## 1. Habibi closure

The Habibi primary source permits a complete **theoretical-at-recalculated-prototype** semiconductor stress vector without inventing a measured duty value.

Using reported G=20, n21=0.5 and n31=2 in the paper's ideal gain relation gives recalculated D=0.52. At that point the theory gives both switches ~41.67 V (~0.1042 Vout), D1~208.3 V and D2/Do~250 V (maximum ~0.625 Vout).

Experimental text separately locks S1 at almost 45 V, but does not text-lock the exact Sc maximum or exact diode maxima. Therefore theory and measurement remain separate evidence layers.

The controlled-switch-vector rule is not relaxed: S1 alone cannot become the measured topology-wide maximum for a two-switch record.

Result: Habibi remains L4.

## 2. Jazi direct-scale audit

The 2025 IEEE Access paper is now structurally and numerically audited at the direct-scale boundary:

- 40 V -> 400 V;
- 200 W;
- 100 kHz;
- 2 controlled switches;
- 4 discrete diodes;
- 6 capacitors under the common schematic-discrete basis;
- 2 magnetic cores;
- 4 total windings;
- explicit shared ground;
- continuous input current;
- S1 measured at ~120 V (~0.30 Vout);
- S1 ZVS, SA ZCS-on/ZVZCS-off, all diodes ZCS-off;
- full-load measured efficiency ~96.5%.

The exact measured SA maximum and exact maximum measured diode stress remain unresolved. The source's ideal main-switch formula gives ~93 V at the design D~0.65, which differs from the measured ~120 V. This is preserved as a theory/measurement boundary difference rather than reconciled.

Result: Jazi remains L4.

## 3. Jazi family lineage

The current paper shares Ehsan Adib with the older Molavi/Adib/Farzanehfard program. Shared authorship alone is insufficient to collapse families.

An earlier 2021 Jazi-led ZVT high-step-up paper (`10.1049/pel2.12183`) establishes a separate Jazi lead topology-development line before the 2025 target. The 2025 architecture and lead roles are therefore treated as a distinct family candidate:

`JAZI_KHORASANI_ZVT_CI_VM`.

Because family count is based on admitted L5 evidence, no seventh independent-family credit is counted while Jazi remains L4.

## 4. Stopping test failed decisively

The targeted stopping search produced new direct-scale evidence even after excluding the already saturated author/program clusters.

### 10.3390/pr11041087

A published CC BY primary PDF documents a different-author 20-40 V -> 380 V / 150 W experimental converter. It is registered as a new direct-scale experiment-located candidate pending full common-schema stress extraction.

### 10.1088/2631-8695/ae8f9a

An IOP accepted-manuscript record dated 23 July 2026 documents another different-author 24 V -> 400 V / 200 W hardware converter, with two synchronous switches, continuous input current, three-winding coupled inductor, voltage-multiplier cell and passive clamp. Full-load efficiency is stated as 95.7% in the abstract. Full stress/count extraction is still pending.

A July-2026 direct-scale record appearing under a targeted stopping query is incompatible with a claim that the evidence frontier has stabilized.

Therefore:

`SEARCH_SATURATION_NOT_MET`.

## 5. Independent review remains blocked

The neutral packet was retried with the Firecrawl independent-agent route. The request failed to start because of insufficient credits.

No independent interpretation was returned. Same-assistant Exa/Sider/GitHub/Drive retrieval does not count as independent review.

`independence_missing=true` remains mandatory.

## 6. Frontier count remains unchanged

Neither Habibi nor Jazi receives L5 promotion in this node.

Current bounded frontier therefore remains:

- 11 L5 records;
- 6 independent L5 evidence families.

The two new stopping-test candidates are not counted before full extraction/admission.

## 7. Pareto and Research Gap remain withheld

Formal all-objective Pareto is not authorized because:

1. targeted marginal yield remains positive;
2. independent review remains missing;
3. Habibi measured controlled-switch and diode vectors are incomplete;
4. Jazi measured controlled-switch and diode vectors are incomplete;
5. PC-CAND-0024 and DOI 10.1155/etep/9317966 still lack maximum measured diode-stress scalars;
6. several admitted records retain theory-at-prototype or upper-bound stress evidence;
7. efficiency measurement/auxiliary boundaries are not matched.

The recurring burden-redistribution pattern remains a supported working hypothesis, not a formal Research Gap statement.

## Authorized next node

`KHAN + TRAN DIFFERENT-FAMILY FULL-VECTOR AUDIT / STOPPING ROUND 2`

Priority:

1. fully extract DOI `10.3390/pr11041087` under `SCHEMATIC_DISCRETE_POWER_STAGE_V1`, including exact measured switch/diode stresses, grounding, input ripple, efficiency and measurement conditions;
2. obtain the legal/readable accepted manuscript/full text for DOI `10.1088/2631-8695/ae8f9a` and extract the same vector;
3. perform role-weighted family adjudication for both new programs;
4. rerun targeted marginal yield after those two candidates are no longer merely uncaptured direct-scale evidence;
5. do not return to broad keyword search;
6. retry independent neutral review only when a functioning independent route exists;
7. keep formal Pareto and Research Gap locked.

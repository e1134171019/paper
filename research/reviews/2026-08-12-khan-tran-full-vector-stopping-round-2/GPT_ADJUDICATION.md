# GPT Adjudication — Khan + Tran Full-Vector Audit / Stopping Round 2

Date: 2026-08-12

## Decision

- research direction: `APPROVE_CONTINUE_TARGETED_ONLY`;
- bounded L5 records: `11`;
- independent L5 evidence families: `6`;
- Khan DOI `10.3390/pr11041087`: `L4_DIRECT_VECTOR_PARTIAL_WITH_STRESS_GAP`;
- Khan L5 promotion: `NOT_AUTHORIZED`;
- Tran DOI `10.1088/2631-8695/ae8f9a`: `L1_METADATA_VERIFIED / PRIMARY_ABSTRACT_VERIFIED / FULLTEXT_ACCESS_BLOCKED`;
- Tran L5 promotion: `NOT_AUTHORIZED`;
- new round-2 direct-scale candidate: `10.1007/s43236-022-00564-1`;
- targeted marginal yield: `POSITIVE`;
- targeted search saturation: `NOT_MET`;
- independent review: `NOT_COMPLETE`;
- `independence_missing=true`;
- formal all-objective Pareto: `NOT_AUTHORIZED_YET`;
- Research Gap Candidate: `NOT_AUTHORIZED`.

## 1. Khan moved from experiment-located to bounded L4, not L5

The legal/readable published full text permits a substantially fuller audit than the prior stopping node.

The proposed power stage is structurally locked as:

- 1 controlled switch;
- 7 discrete diodes;
- 5 capacitors;
- 3 explicit inductors.

The hardware program operates from 20–40 V to 380 V at 150 W and 50 kHz. The paper reports duty ratios from 0.54 at 20 V down to 0.35 at 40 V and condition-specific efficiencies from 90% to 96%.

However, the experimental figures used for the hardware section show gate, input/PV and output voltages rather than a text-locked `VDS` / diode reverse-voltage vector. The switch stress `Vo/2` is therefore preserved as a theory/design statement. The topology-wide measured maximum switch and diode stresses remain unresolved.

The paper also contains an internal simulation-parameter conflict: it states 150 W output is used to determine the load resistance, while Table 1 gives `Rload = 100 ohm` and the simulation regulates about 380 V. Those simultaneous values imply 1444 W, not 150 W. The conflict is recorded rather than repaired.

Result: Khan is useful direct-scale L4 evidence but not comparison-ready L5.

## 2. Tran remains access-bounded

IOPscience verifies an accepted manuscript online 23 July 2026. The publisher abstract supports:

- two synchronously gated power switches;
- an input inductor and continuous input current;
- a three-winding coupled inductor;
- a voltage-multiplier cell;
- a passive clamp;
- a 24 V -> 400 V / 200 W hardware prototype;
- 96.7% peak efficiency at 40% load and 95.7% at full load.

The current access route does not expose the complete manuscript body without subscription/login. The audit did not bypass that access boundary.

Therefore switching frequency, exact component counts, semiconductor stress vectors, common-ground status, switching-mode details and measurement locators remain unresolved. Abstract claims are not promoted to full-text evidence.

Result: Tran remains L1 under the current legal access state.

## 3. Family count remains six

Khan is retained as candidate program `RASHID_KHAN_LIU_LIN_HVGSU_MPPT` and Tran as `TRAN_NGUYEN_HO_PHAM_HIGH_STEPUP_PROGRAM`.

Both appear distinct from the six currently credited L5 programs, but family credit is admission-based. Neither target reaches L5, so neither becomes family credit seven.

## 4. Stopping Round 2 fails

The targeted search remained bounded to direct-scale/different-program hardware evidence and did not restart broad keyword search.

It surfaced DOI `10.1007/s43236-022-00564-1`, Fuwei Li et al., *Quadratic-type high step-up DC-DC converter with continuous input current integrating coupled inductor and voltage multiplier for renewable energy applications*.

The Journal of Power Electronics publisher page states a 20 V -> 400 V / 200 W experimental prototype, continuous input current, and reported peak/full-load efficiencies of 95.2% / 93.7%.

Exact DOI/title repository searches found no existing indexed record, and the paper is absent from the inspected BATCH-004 candidate register.

A previously uncaptured different-author direct-scale 20->400 V / 200 W hardware program is incompatible with declaring targeted-search saturation.

Therefore:

`SEARCH_SATURATION_NOT_MET`.

The record is registered only as a new candidate. It receives no L5 or family credit before full common-schema extraction.

## 5. Independent review is still missing

Firecrawl was attempted for source extraction and again failed for insufficient credits. No functioning external independent interpretation was returned.

Same-assistant work through Exa, Sider Scholar, GitHub, Drive or web does not satisfy the independent-review role.

Therefore:

`independence_missing=true`.

## 6. Pareto and Research Gap remain withheld

Formal all-objective Pareto remains locked because:

1. targeted marginal yield is still positive;
2. independent review is incomplete;
3. Khan measured switch/diode stress maxima remain unresolved;
4. Tran is full-text access-blocked;
5. the new Li/He/Luo direct-scale candidate is uncaptured at the full-vector level;
6. prior frontier records still contain measured/theory/upper-bound mismatches and missing diode-stress scalars;
7. efficiency boundaries remain heterogeneous and are not authorized for ranking.

The burden-redistribution pattern remains a supported working hypothesis, not a formal Research Gap.

## Authorized next node

`LI/HE/LUO 2023 FULL-VECTOR AUDIT / STOPPING ROUND 3`

Priority:

1. resolve a legal/readable complete source for DOI `10.1007/s43236-022-00564-1`;
2. extract its full semiconductor/component/magnetic/input-current/common-ground/soft-switching/efficiency vector with locators;
3. perform role/topology/program family adjudication;
4. recheck Tran only if legal full-text access changes;
5. run a new narrow stopping test after Li is no longer uncaptured evidence;
6. retry genuine independent review only through a functioning independent route;
7. keep formal Pareto and Research Gap locked until those gates close.

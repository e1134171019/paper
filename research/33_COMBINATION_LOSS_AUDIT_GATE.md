# 33 — Combination Loss Audit Gate v1

Status date: 2026-08-19  
Role: `POST-PG SURVIVAL / PRE-TOPOLOGY-SYNTHESIS LOSS GATE`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This document closes a missing accounting layer identified after the minimum falsification plan:

> A mechanism may reduce one existing loss by itself, but once two or more mechanisms are combined into one real circuit graph, the combination can create new RMS current, circulating current, commutation states, balancing paths, storage stress, support circuits and auxiliary losses that did not exist in either mechanism-level argument alone.

Therefore:

```text
single-PM benefit
≠ combination benefit

PG solved locally
≠ converter improved globally

P_saved,target > P_added,target
≠ sufficient final proof
```

The final comparison must be two-sided and graph-specific.

---

## 2. Position in the research sequence

The Combination Loss Audit Gate is inserted after a Physical Gap survives evidence/falsification and before any topology candidate is accepted.

```text
Physical-Gap hypothesis
↓
H1/H2/H3/H4 evidence + fair falsification
↓
PG survives
↓
select minimum mechanism set needed to address that surviving PG
↓
DEFINE ACTUAL COMBINATION GRAPH
↓
COMBINATION LOSS AUDIT GATE       ← THIS DOCUMENT
↓
matched total-loss comparison
↓
robust net benefit survives
↓
reclassify completed graph against #01...#09
↓
Topology candidate may be retained
↓
Candidate #10 only if #01...#09 cannot reasonably describe the main energy path
↓
Novelty evaluated separately
```

This gate does **not** authorize mechanism combination now. It defines the audit that every future combination must pass.

Current immediate NEXT remains the executable H1/H2/H3/H4 evidence-acquisition worksheet.

---

## 3. Fundamental accounting rule

The most reliable final comparison is not a sum of claimed savings. It is a matched-boundary total-loss difference:

```text
ΔP_total
= P_loss,baseline
- P_loss,candidate
```

A candidate survives nominal screening only if:

```text
ΔP_total > 0
```

When uncertainty bounds are available, the preferred robust test is:

```text
ΔP_total,low
= P_loss,baseline,low
- P_loss,candidate,high

ΔP_total,low > 0
```

This total-loss test is the final authority.

The earlier expression:

```text
P_saved > P_added
```

remains useful as a causal ledger, but both sides must include losses that emerge only after the mechanisms are physically combined.

---

## 4. Two ledgers are mandatory and must not be double-counted

Future combination audits must keep two separate views of the same candidate.

### Ledger A — physical loss ledger

This is the summable watt ledger.

```text
P_cond       semiconductor / copper / contact conduction
P_sw         switching-transition / Coss / recovery / commutation
P_mag        winding + core + leakage/magnetizing-associated loss
P_cap        ESR + dielectric + charge-redistribution loss
P_rect       diode / synchronous-rectification support loss
P_circ       incremental circulating / reactive RMS loss
P_buffer     storage-port / buffer conversion loss
P_aux        gate drive / control / sensing / auxiliary power where in boundary
P_other      explicitly declared remaining loss
```

For a matched candidate boundary:

```text
P_loss,candidate
= Σ physical loss terms
```

### Ledger B — causal / origin tags

These tags explain *why* a loss changed but are **not** a second additive watt total.

```text
REMOVED
= baseline loss term genuinely eliminated

REDUCED
= baseline loss remains but is smaller

RETAINED
= baseline loss remains approximately unchanged

RELOCATED
= burden moved to another element/domain rather than removed

INTRINSIC_NEW
= loss intrinsic to a newly introduced mechanism

INTERACTION_NEW
= loss that appears because two or more mechanisms operate together

SUPPORT_NEW
= loss from circuits/functions required to make the combination realizable

AUXILIARY_NEW
= new gate/control/sensing/auxiliary loss inside the declared contract
```

Critical anti-double-count rule:

```text
physical loss terms are summed
causal tags are labels on those terms

DO NOT sum physical terms + causal tags as two independent totals
```

Example:

```text
extra inductor copper loss caused by ZVS circulating current
= physical term: P_mag / P_cond as appropriate
= causal tag: INTERACTION_NEW
```

It is one loss, not two.

---

## 5. Combination-only interaction loss — mandatory audit item

`INTERACTION_NEW` is the key correction introduced by this gate.

Definition:

> A loss term or incremental stress that exists because mechanisms are coupled in the same operating graph and would not appear at the same magnitude in the standalone mechanism arguments.

Typical interaction paths include:

```text
soft-switching current requirement
→ higher RMS / circulating current

voltage stacking + multilevel synthesis
→ balancing current / charge redistribution / more series devices

active buffer + LV main path
→ extra shared-source RMS / switch current / common-bus conduction

integrated X1/X3 switching
→ new commutation sequence / bidirectional blocking / state-transition loss

shared magnetics or coupled branches
→ flux imbalance / current-sharing error / proximity-Rac interaction
```

A combination cannot pass if interaction loss is omitted merely because each mechanism looked favorable in isolation.

---

## 6. Loss relocation is not loss removal

Every claimed saving must identify the fate of the baseline burden.

Valid questions:

```text
Was the loss physically removed?
Was current reduced?
Was voltage stress redistributed?
Was the loss moved from MOS to inductor?
Was leakage dissipation moved into circulating RMS?
Was source 2ω current moved into a buffer converter?
Was transformer loss replaced by capacitor RMS / charge redistribution?
```

Formal rule:

```text
RELOCATED ≠ REMOVED
```

A mechanism does not receive `P_saved` credit for a burden that reappears elsewhere inside the matched comparison boundary.

---

## 7. Target-PG improvement is insufficient — cross-PG regression audit

A combination intended to solve one PG may worsen another.

Therefore every future combination must be re-audited against all current comparison axes:

```text
M1 extreme-LV RMS/conduction exposure before X1
M2 switching / commutation / dissipative-clamp energy
M3 total transformation / storage burden
M4 internal circulating / reactive RMS
M5 2ω energy reflected to LV source
M6 added active processing stages/functions
M7 matched isolation/protection/product contract
```

Examples:

```text
PM-2 + PM-4
may reduce M2 switching loss
but increase M1/M4 through circulating RMS

PM-3 + PM-7
may reduce magnetic dependence / stage count
but increase capacitor RMS, balancing and series-switch conduction

PM-6 active X2
may reduce M5 source 2ω
but increase M1/M4/M6 through another active path
```

Formal rule:

```text
improving target PG while causing larger regression elsewhere
→ NET_BENEFIT_FAIL
```

---

## 8. Baseline-to-candidate loss-fate map

Before calculating a net advantage, each material baseline loss term must be mapped to its candidate fate.

Required table fields:

| Baseline loss term | Baseline W / bound | Candidate fate | Candidate location | Candidate W / bound | Causal tag | Evidence |
|---|---:|---|---|---:|---|---|
| example: LV MOS conduction | TBD | REDUCED | new X1 switch path | TBD | REDUCED | measured/model |
| example: RC snubber | TBD | REMOVED or REDUCED | PM-4 path | TBD | REMOVED/REDUCED | waveform |
| example: transformer copper | TBD | RELOCATED | inductor/capacitor path | TBD | RELOCATED | matched model |

Then list candidate-only terms:

| Candidate-only loss term | Physical category | Origin tag | W / bound | Why required | Evidence |
|---|---|---|---:|---|---|
| circulating RMS | P_circ | INTERACTION_NEW | TBD | soft-commutation condition | waveform/model |
| balancing current | P_cap/P_cond | INTERACTION_NEW | TBD | stacked voltage states | model/measurement |
| added driver power | P_aux | SUPPORT_NEW/AUXILIARY_NEW | TBD | additional active switches | datasheet/measurement |

No candidate can pass with an incomplete material-loss fate map.

---

## 9. Combination Gate — CALG v1

Every future mechanism combination must pass all applicable gates.

### CALG-0 — Surviving-PG authorization

```text
Each mechanism must map to a PG that survived its required evidence/falsification gate,
or be explicitly necessary as a support mechanism for an already surviving solution path.
```

No speculative mechanism stacking before PG survival.

### CALG-1 — Minimality

```text
Every added mechanism must have a declared necessary function.
```

If removing one mechanism preserves the intended function with lower loss, the larger combination is rejected.

### CALG-2 — No duplicate function without proof

Two mechanisms may not perform the same function merely because both are individually attractive.

Examples:

```text
PM-5 + PM-6 both buffering the same 2ω energy
→ requires explicit reason and net-loss proof

multiple voltage-building mechanisms
→ requires proof that the second mechanism reduces total burden rather than stacking loss
```

### CALG-3 — Actual electrical graph resolved

The combination must be expressed as a real circuit/energy graph, not labels such as:

```text
PM-2 + PM-4 + PM-7
```

Required:

```text
source path
switch states
energy-storage elements
X1 start/completion
X2 location if any
X3 synthesis path
return path
support primitives
```

### CALG-4 — Matched functional contract

Baseline and candidate must match the declared comparison contract:

```text
Vin / Vout / Pout / load point
direction
isolation requirement
protection / sensing / precharge policy
output waveform / power-quality requirement
thermal / cooling basis
auxiliary-loss policy
```

A candidate cannot win by deleting a required function.

### CALG-5 — State and current-path closure

For every operating state required to make the claimed benefit:

```text
current path
voltage state
energy-storage change
commutation path
```

must be physically resolved.

### CALG-6 — Full physical loss ledger

All material terms in Section 4 Ledger A must be measured, modeled or conservatively bounded.

Unknown material terms force:

```text
LOSS_LEDGER_INCOMPLETE
```

not a pass.

### CALG-7 — Interaction-loss closure

Combination-only losses must be explicitly identified and bounded.

If interaction loss is material and unresolved:

```text
INTERACTION_UNBOUNDED
```

### CALG-8 — Relocation / double-count audit

Every claimed saved watt must be checked for relocation and duplicate accounting.

```text
same joule counted as saved twice = INVALID
same physical loss counted under two new-loss categories = INVALID
relocated burden credited as removed = INVALID
```

### CALG-9 — Cross-PG regression audit

Recalculate M1–M7 for the actual combination graph.

A target-PG improvement cannot override a larger total-loss regression elsewhere.

### CALG-10 — Net total-loss gate

Nominal preliminary pass:

```text
P_loss,candidate < P_loss,baseline
```

Preferred robust pass:

```text
P_loss,candidate,high < P_loss,baseline,low
```

Equivalent:

```text
ΔP_total,low > 0
```

### CALG-11 — Stress / feasibility sanity gate

A lower nominal watt total is not sufficient if the combination requires noncredible:

```text
peak current
RMS current
device voltage stress
capacitor ripple current
magnetic flux density
thermal density
control timing / dead-time sensitivity
```

These stresses must be within a defensible implementation envelope.

### CALG-12 — Reclassification gate

After the completed graph passes the loss audit:

```text
reclassify against #01...#09
```

If an existing family reasonably describes the graph:

```text
Candidate #10 = NOT JUSTIFIED BY TAXONOMY
```

This does not decide novelty; novelty remains a separate evidence question.

---

## 10. Combination-audit status vocabulary

```text
NOT_AUTHORIZED
= prerequisite PG has not survived

GRAPH_UNRESOLVED
= labels exist but actual circuit / current path is not defined

BOUNDARY_MISMATCH
= baseline and candidate contracts differ

LOSS_LEDGER_INCOMPLETE
= material candidate/baseline loss terms are missing

INTERACTION_UNBOUNDED
= combination-only losses are not bounded

RELOCATION_FAIL
= claimed saving is merely moved elsewhere

CROSS_PG_REGRESSION_FAIL
= target PG improves but another burden makes the total result worse

NET_BENEFIT_FAIL
= matched candidate total loss is not lower

PRELIMINARY_PASS
= nominal matched total loss is lower but robust uncertainty closure is absent

ROBUST_PASS
= matched conservative candidate upper loss is below baseline lower loss
```

Only `ROBUST_PASS` is strong evidence for retaining a combination as a superior loss path.

---

## 11. Example A — PM-2 + PM-4

Intended logic:

```text
PM-2 provides inductive / leakage-mediated energy transfer
+
PM-4 uses reactive energy for ZVS/ZCS
```

Possible saved losses:

```text
hard-switching overlap
Coss dissipation
RC/snubber dissipation
```

Mandatory new / interaction audit:

```text
extra circulating current required for ZVS
higher MOS RMS
higher inductor/transformer RMS
copper/Rac increase
reactive component loss
light-load ZVS loss of condition
control/dead-time burden
```

Therefore:

```text
P_switching saved > 0
```

is insufficient.

The combination passes only if the matched total candidate loss remains lower after the increased RMS/circulation is counted.

---

## 12. Example B — PM-3 + PM-7

Intended logic:

```text
PM-3 builds voltage through charge transfer / stacking
+
PM-7 synthesizes AC through semiconductor switching states
```

Potential removed/reduced terms:

```text
some magnetic transformation burden
some separate stage boundaries
possibly lower per-device voltage step
```

Mandatory new / interaction audit:

```text
capacitor RMS
charge redistribution
balancing current
series-device conduction
additional switching events
state-transition commutation
precharge / startup support
voltage-balancing control
```

A lower stage count is not loss evidence.

---

## 13. Example C — PM-1 + PM-6

Intended logic:

```text
PM-1 performs X1
+
PM-6 actively routes 2ω energy to a storage port
```

Potential saved burden:

```text
source 2ω RMS
incremental LV I²R caused by 2ω
```

Mandatory new / interaction audit:

```text
buffer MOS conduction/switching
buffer inductor copper/core
buffer capacitor/storage ESR
circulating current
shared-bus RMS interaction
gate/control/sensing power
```

If:

```text
P_LV,2ω saved <= total active-buffer added loss
```

then the combination fails even though PG-4 is locally reduced.

---

## 14. Required combination worksheet fields

When combination work is eventually authorized, every combination must have at least:

```text
combination_id
surviving_PG
mechanisms_used
mechanism_role_per_PG
actual_family_graph
X1_start
X1_completion
X2_location_or_none
X3_region
operating_states
baseline_contract
candidate_contract
baseline_loss_ledger
candidate_loss_ledger
baseline_loss_fate_map
interaction_loss_terms
support_loss_terms
auxiliary_loss_terms
M1...M7 regression audit
P_loss_baseline
P_loss_candidate
uncertainty_baseline
uncertainty_candidate
ΔP_total
ΔP_total_low
CALG_0...CALG_12 status
family_reclassification
candidate_status
novelty_status
```

---

## 15. Formal decision after this gate

```text
Combination Loss Audit Gate            = ESTABLISHED v1
Combination-only interaction loss       = MANDATORY ACCOUNTING ITEM
Loss relocation audit                   = MANDATORY
Cross-PG regression audit               = MANDATORY
Matched total-loss comparison           = FINAL LOSS AUTHORITY
Robust pass criterion                   = P_loss,candidate,high < P_loss,baseline,low

Mechanism combination execution         = NOT YET AUTHORIZED
Executable H1/H2/H3/H4 worksheet       = CURRENT NEXT
Candidate #10                           = HOLD / NOT_ASSIGNED
Novelty                                 = NOT_ESTABLISHED
```

The research sequence is therefore corrected to:

```text
PG evidence/falsification
↓
Surviving PG
↓
minimal mechanism selection
↓
actual combination graph
↓
Combination Loss Audit Gate
↓
robust matched total-loss advantage
↓
family reclassification
↓
retained topology candidate
↓
novelty evaluation
```

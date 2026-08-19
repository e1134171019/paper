# 32 — Minimum Falsification / Evidence Plan v1

Status date: 2026-08-19  
Role: `PHYSICAL-GAP VALIDATION / EVIDENCE AND FALSIFICATION GATE`  
Research object: retained primary `PG × PM` pairs from `research/31_PG_PM_COMPATIBILITY_SCREEN.md`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This document converts the retained compatibility pairs into a minimum evidence and falsification plan.

It does **not**:

```text
combine mechanisms
select a new topology
create Candidate #10
claim novelty
assume any Physical Gap is already verified
```

It answers four questions only:

```text
1. What is the minimum evidence needed to test each PG?
2. What quantity decides whether the burden is material?
3. Which fair comparator can falsify the PG?
4. What exact stop condition prevents further research on a weak PG?
```

Authoritative upstream records:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md
research/30_L3_PHYSICAL_MECHANISM_DICTIONARY.md
research/31_PG_PM_COMPATIBILITY_SCREEN.md
research/contracts/power_converter_comparison_contract_v0.1.md
```

Core rule remains:

```text
P_saved > P_added
```

but no `P_saved` / `P_added` comparison is valid unless the comparison boundary is matched.

---

## 2. Retained primary research pairs

```text
PG-1 × PM-1  magnetic-X1 fair falsifier
PG-1 × PM-2  inductive alternative-X1
PG-1 × PM-3  capacitive-transfer alternative-X1

PG-2 × PM-4  reactive-energy-assisted commutation

PG-3 × PM-1  magnetic transformation benchmark
PG-3 × PM-2  inductive transformation alternative
PG-3 × PM-3  capacitive-transfer transformation alternative

PG-4 × PM-5  passive 2ω buffering
PG-4 × PM-6  active storage-port routing
```

These are evidence targets, not topology candidates.

---

## 3. Common evidence rule — no post-hoc materiality threshold

A Physical Gap cannot be promoted merely because a nonzero loss is measured.

For each PG, define a predeclared materiality threshold:

```text
T_mat,PGk
```

v1 intentionally does **not** invent a universal fixed percentage such as 5% or 10%.

The threshold must be fixed before the final comparison result is interpreted and must satisfy all of the following:

```text
M-G1 — tied to the declared 12–24 V / 1–3 kW research envelope or an explicit loss budget
M-G2 — larger than the practical measurement/model uncertainty floor
M-G3 — large enough that removing the burden could materially change architecture choice or thermal design
M-G4 — identical decision rule for baseline and alternative mechanisms
M-G5 — not chosen after seeing which mechanism wins
```

For a measured burden `B` with uncertainty `U`:

```text
materiality cannot be claimed when B is not distinguishable from U
```

A conservative screening form is:

```text
B_low = B_est - U
```

and the burden is not promoted as material unless:

```text
B_low > T_mat,PGk
```

The exact numerical `T_mat,PGk` remains an explicit pre-measurement research parameter until justified from the project loss budget and achievable uncertainty.

Important existing anchor:

```text
20 W LV-conduction budget → R_eq,max ≈ 0.65 mΩ @ ~175.4 A
```

This is a useful PG-1 budget reference, but v1 does not arbitrarily declare a fixed fraction of 20 W to be the universal gap threshold.

---

## 4. Common net-benefit rule

For any alternative mechanism:

```text
ΔP_net = P_saved - P_added
```

where:

```text
P_saved
= loss removed from the declared baseline boundary

P_added
= all new conduction + switching + magnetic + capacitive + circulating + auxiliary loss caused by the alternative
```

If uncertainty bounds are available, the robust form is:

```text
ΔP_net,low = P_saved,low - P_added,high
```

Strong survival requires:

```text
ΔP_net,low > 0
```

If only nominal data exist:

```text
ΔP_net > 0
```

may be used only as a preliminary screen and must not be promoted as high-confidence verification.

Forbidden accounting:

```text
remove a fuse/protection/precharge/product function only from the candidate
→ call the removed watts topology savings
```

---

## 5. Comparison boundary gate

Before any quantitative comparator is accepted, declare:

```text
input voltage
output voltage
output power / load point
power-flow direction
isolation requirement
processed-power boundary
switching-frequency basis
semiconductor generation / device class where material
cooling / temperature basis
included auxiliary losses
measurement vs model basis
```

Use the existing comparison contract modes:

```text
DIRECT_QUANTITATIVE
BOUNDED_TRADEOFF
CONTEXT_ONLY
```

If a comparator cannot satisfy direct quantitative gates, it may still be useful as `BOUNDED_TRADEOFF` or `CONTEXT_ONLY`, but it cannot decide a scalar winner.

---

# 6. H1 — PG-1 minimum evidence gate

## 6.1 Research question

> Is the source-domain conduction/RMS burden before X1 completion materially large, and can PM-2 or PM-3 reduce it relative to a fair optimized PM-1 without adding equal/larger loss?

Primary quantity:

```text
P_preX1,cond
≈ Σ(I_rms,k² · R_eff,k)
 + Σ(P_semiconductor,cond,k)
```

Secondary observables:

```text
I_source,avg
I_source,rms
I_T1,rms / I_T2,rms where accessible
A/C switch current or defensible bank-current proxy
hot on-state VDS / R_eff
source-domain device / copper temperature
X1 completion voltage/current domain
```

## 6.2 Minimum A0 hardware evidence

Required minimum:

```text
H1-A — I_source,avg and I_source,rms at declared anchor/load point
H1-B — A/C on-state VDS + current evidence, or a bounded equivalent conduction estimate
H1-C — switch/device temperature during the same operating condition
H1-D — T1/T2 RMS current if safely accessible; otherwise explicitly mark OPEN
```

Useful but not independently gap-proving:

```text
existing >82 µm PCB geometry bounds
25°C datasheet MOS conduction scale
```

These may bound the problem but do not replace hot operating evidence.

## 6.3 A0 output

Produce:

```text
P_preX1,cond,A0 = measured or bounded source-domain conduction scale
U_H1              = uncertainty / unresolved component range
```

Do not include product-interface protection in intrinsic X1 loss unless the selected comparison contract includes the same function on every side.

## 6.4 Fair falsifiers

### A1 — PM-1 fair optimized magnetic benchmark

Role:

```text
PRIMARY FALSIFIER
```

Question:

> Can an optimized magnetic-X1 path reduce the observed A0 burden without leaving the PM-1 solution class?

If yes, the A0 burden may be implementation-limited rather than a cross-mechanism Physical Gap.

### C2 — PM-2-dominant non-isolated / inductive X1 comparator

Role:

```text
ALTERNATIVE MECHANISM COMPARATOR
```

Must expose:

```text
inductor copper/core
switch conduction
ripple/peak current
high-duty burden
circulating current where applicable
```

### C3 — PM-3-dominant charge-transfer / voltage-stacking comparator

Role:

```text
ALTERNATIVE MECHANISM COMPARATOR
```

Must expose:

```text
capacitor RMS
ESR/dielectric
charge redistribution
series switch-path loss
balancing/precharge burden
```

Important correction:

```text
one generic "high-gain C" comparator is insufficient
if it mixes PM-1 + PM-2 + PM-3 without separable loss accounting.
```

## 6.5 PG-1 stop / survive logic

```text
IF P_preX1,cond,A0 is not material above T_mat,PG1
→ PG-1 MATERIALITY_FAIL

ELSE IF fair A1 PM-1 reduces the burden below materiality
→ PG-1 FAIR_FALSIFIER_FAIL

ELSE IF PM-2 / PM-3 alternatives do not show positive ΔP_net
→ no alternative-X1 research advantage established

ELSE
→ PG-1 survives to matched mechanism comparison
```

PG-1 is not `VERIFIED PHYSICAL GAP` until all formal G1–G6 promotion gates are satisfied.

---

# 7. H2 — PG-2 minimum evidence gate

## 7.1 Research question

> Is avoidable dissipative commutation / leakage / Coss handling materially large enough to justify PM-4?

Primary burden:

```text
P_comm,avoidable
= P_snubber
+ avoidable switching-overlap / hard-commutation loss
+ unrecovered leakage/Coss dissipation where separately identifiable
```

Avoid double counting the same transition energy in multiple terms.

## 7.2 Minimum A0 hardware evidence

Required:

```text
H2-A — fs / duty / dead time at the tested operating point
H2-B — V_A-B / V_C-B switching-node waveforms
H2-C — synchronized relevant switch current
H2-D — V_R110 / V_R119 or another valid snubber-power observable
H2-E — actual VGS where needed to interpret timing / dead-time behavior
```

Hard rule:

```text
unsynchronized V × wrong-current integration = INVALID
```

## 7.3 Calculated outputs

At minimum:

```text
P_snubber
P_switching,transition
P_comm,avoidable estimate / bound
U_H2
```

## 7.4 Fair falsifier

### A1-S — optimized PM-1 baseline with reasonable commutation engineering

A0 passive RC damping is not assumed to be the PM-1 optimum.

### PM-4 comparator

A PM-4 implementation may use:

```text
resonant transition
ZVS
ZCS
leakage-energy-assisted switching
```

but the label is insufficient. It must report:

```text
P_saved,commutation
P_added,resonant / reactive network
ΔI_rms / circulating current
extra conduction
control / gate auxiliary burden where material
```

## 7.5 PG-2 hard stop

```text
IF P_comm,avoidable is not material above T_mat,PG2
→ PG-2 MATERIALITY_FAIL
→ PM-4 research direction CLOSED
```

If material:

```text
IF P_saved,commutation ≤ P_added,resonant+circulation+control
→ PM-4 NET_BENEFIT_FAIL

ELSE
→ PG-2 survives preliminary falsification
```

A visible RC snubber by itself is never enough to keep PG-2 alive.

---

# 8. H3 — PG-3 minimum evidence gate

## 8.1 Research question

> Under the extreme conversion ratio, is there a material total transformation burden that differs across PM-1, PM-2 and PM-3 after symmetric accounting?

PG-3 is mechanism-neutral.

Do not use:

```text
"magnetics are large"
```

as the research claim.

## 8.2 PM-1 minimum A0/A1 evidence

Required or bounded:

```text
H3-A — T1/T2 RMS current
H3-B — primary voltage / volt-second
H3-C — transformer temperature at declared operating point
H3-D — correct turns ratio when obtainable
H3-E — winding DCR / Rac when obtainable
H3-F — Lm / Lk when obtainable
H3-G — material / core parameters when obtainable
```

If exact A0 transformer P/N remains unresolved, report a bounded magnetic burden rather than substituting context-only PQ50 values.

## 8.3 Symmetric mechanism burden definitions

### PM-1 burden

```text
P_TR,PM1
= winding copper/Rac
+ core
+ leakage/magnetizing-associated burden
+ required switching/rectification support loss inside declared X1 boundary
```

### PM-2 burden

```text
P_TR,PM2
= inductor copper/core
+ switch conduction/switching
+ diode/rectification support where present
+ ripple / circulating-current incremental loss
```

### PM-3 burden

```text
P_TR,PM3
= capacitor ESR/dielectric
+ charge-redistribution loss
+ switch conduction/switching
+ balancing/precharge steady-state burden where applicable
```

All three must terminate at a comparable reduced-current / voltage-domain boundary.

## 8.4 Fair comparator roles

```text
A1 = PM-1 optimized magnetic reference
C2 = PM-2-dominant transformation comparator
C3 = PM-3-dominant transformation comparator
```

`B Direct HFL` is **not** a clean PM-2 or PM-3 comparator by name. It is an architecture-level integration comparator whose internal mechanisms must be decomposed before it can enter PG-3 quantitative ranking.

## 8.5 PG-3 stop / survive logic

```text
IF PM-1/PM-2/PM-3 burden cannot be defined on matched boundaries
→ PG-3 EVIDENCE_INSUFFICIENT

IF no mechanism shows a material transformation-burden difference above uncertainty / T_mat,PG3
→ PG-3 MATERIALITY_FAIL

IF optimized PM-1 is not materially worse than alternatives
→ reject any claim that magnetic transformation itself is the gap

IF one alternative reduces total transformation burden with positive robust ΔP_net
→ PG-3 survives mechanism-level falsification
```

PG-3 remains `OPEN` until this evidence exists.

---

# 9. H4 — PG-4 minimum evidence gate

## 9.1 Research question

> Is a material amount of single-phase 2ω pulsating power reflected into the expensive LV source path after the existing passive buffering is accounted for?

Primary observables:

```text
P_2ω,source
I_2ω,source
I_source,rms
HV-link ΔV_2ω
E_2ω,buffer
```

## 9.2 Minimum A0 hardware evidence

Required:

```text
H4-A — source-current time waveform over enough line cycles
H4-B — source-current spectrum / extracted 100/120-Hz component
H4-C — HV DC-link voltage ripple synchronized to the same load condition
H4-D — output real power / line frequency for energy-balance context
```

Useful derived quantities:

```text
I_2ω,source
P_2ω,source
incremental source RMS caused by 2ω
incremental LV I²R impact
estimated existing HV-link energy swing
```

## 9.3 First falsifier — existing PM-5 passive buffering

The existing HV DC-link may already perform sufficient PM-5 buffering.

Hard question:

> After the passive link does its job, is source-side 2ω still material?

If not:

```text
PG-4 MATERIALITY_FAIL
active X2 CLOSED
```

## 9.4 PM-5 versus PM-6 comparison only after H4 survives

### X2-P — PM-5 passive buffer comparator

Count:

```text
capacitor ESR / ripple heating
dielectric loss
required energy / volume
voltage ripple
lifetime burden where the contract includes it
```

### X2-A — PM-6 active storage-port comparator

Count:

```text
extra switch conduction/switching
buffer inductor/capacitor/storage loss
circulating RMS
gate/control/sensing
storage-port conversion loss
```

Net gate:

```text
P_LV,saved > P_X2,added
```

Robust form:

```text
P_LV,saved,low - P_X2,added,high > 0
```

## 9.5 Important comparator-stack correction

The existing `A1 / B / C` architecture stack does not by itself provide a clean PM-5 versus PM-6 comparison.

Therefore, only if H4 survives, introduce conditional X2 comparator roles:

```text
X2-P = passive PM-5 reference
X2-A = active PM-6 reference
```

These are comparator roles, not Candidate #10 or new topology families.

`B Direct HFL` may participate only if its actual storage path is explicitly identified as PM-5 and/or PM-6. Direct AC synthesis alone has no energy-storage capacity.

---

# 10. A1 / B / C comparator-role normalization

The architecture benchmark stack is retained, but each architecture must be decomposed into the relevant mechanism role before it can falsify a PG.

## A1 — Fair optimized magnetic HFT

Primary roles:

```text
PG-1 × PM-1 falsifier
PG-3 × PM-1 benchmark
PG-2 baseline after reasonable commutation optimization
```

A1 must not be artificially constrained to A0's exact device count, transformer construction or passive-snubber implementation if the comparison gives alternatives equivalent engineering freedom.

## B — Direct HFL

Primary role:

```text
architecture-integration comparator
```

Possible internal mechanisms:

```text
PM-1 magnetic HF-link
PM-4 soft commutation where implemented
PM-7 direct AC synthesis
PM-5 / PM-6 only if actual 2ω storage/routing exists
```

B is not allowed to win merely by saying:

```text
rectifier/HV bus/VSI removed
```

It must count:

```text
bidirectional switching
matrix/cycloconverter commutation
series-device conduction
circulating/reactive RMS
required storage / 2ω routing
```

## C — Non-isolated high-gain / current-distribution comparator

C must be split by dominant mechanism for mechanism-level comparison:

```text
C2 = PM-2-dominant inductive high-gain comparator
C3 = PM-3-dominant capacitive-transfer / stacking comparator
```

A coupled-inductor C variant must be decomposed as:

```text
PM-1 + PM-2 composite
```

and cannot be treated as a fourth primitive transformation mechanism.

---

# 11. Evidence lanes

Two evidence lanes are permitted and must not be confused.

## Lane H — A0 / hardware discriminator

Purpose:

```text
establish whether the burden actually exists and is material in a competent real product
```

Outputs:

```text
H1 / H2 / H3 / H4 measured or bounded quantities
```

## Lane E — fair external / modeled comparator evidence

Purpose:

```text
falsify the claim that the burden is unavoidable within existing mechanisms
```

Acceptable evidence can include:

```text
L4 numerically verified published prototypes
matched own analytical model
matched PLECS/LTspice model where measurement is unavailable
```

but evidence basis must be explicit.

A modeled alternative cannot be presented as experimentally superior to a measured baseline without labeling the evidence asymmetry.

---

# 12. Minimum evidence table

| PG | Hardware discriminator | Primary PM comparison | Hard stop | Output if survives |
|---|---|---|---|---|
| PG-1 | H1: source RMS + hot conduction evidence | PM-1 vs PM-2 vs PM-3 | burden not material; or fair A1 removes it; or alternatives have non-positive ΔP_net | matched pre-X1 burden comparison |
| PG-2 | H2: synchronized commutation + snubber power | PM-4 vs optimized hard/soft PM-1 baseline | avoidable commutation not material; or PM-4 added loss ≥ saved loss | commutation net-benefit comparison |
| PG-3 | H3: magnetic burden discriminator + matched alternative burdens | PM-1 vs PM-2 vs PM-3 | unmatched boundaries; no material difference; optimized PM-1 not worse | total transformation-burden comparison |
| PG-4 | H4: source 2ω + HV-link ripple | PM-5 vs PM-6 only after H4 | source 2ω not material; or active X2 added loss ≥ saved LV loss | 2ω routing net-benefit comparison |

---

# 13. Physical-Gap promotion state machine

Use the following state sequence per PG:

```text
UNTESTED
↓
BURDEN_MEASURED_OR_BOUNDED
↓
MATERIALITY_PASS / MATERIALITY_FAIL
↓
FAIR_FALSIFIER_PASS / FAIR_FALSIFIER_FAIL
↓
NET_BENEFIT_PASS / NET_BENEFIT_FAIL
↓
SURVIVES_PHYSICAL_GAP_FALSIFICATION
↓
VERIFIED PHYSICAL GAP only after formal G1–G6 are all satisfied
```

Stop states:

```text
MATERIALITY_FAIL
FAIR_FALSIFIER_FAIL
NET_BENEFIT_FAIL
EVIDENCE_INSUFFICIENT
```

No stop state may be silently converted into a topology-synthesis direction.

---

# 14. Evidence priority order

The minimum efficient order is:

```text
Priority 1 — H2 and H4 hard materiality gates
Priority 2 — H1 pre-X1 conduction scale
Priority 3 — H3 transformation-burden closure
Priority 4 — matched A1 / C2 / C3 comparator evidence
Priority 5 — B Direct-HFL integration comparison where relevant
```

Reason:

```text
H2 can immediately kill PG-2
H4 can immediately kill active-X2 / PG-4 work
H1 determines whether PG-1 has enough burden to justify X1 alternatives
H3 requires more magnetic parameter closure and symmetric alternative accounting
```

This priority is a research-efficiency ordering, not a claim that PG-2 or PG-4 is more important physically.

---

# 15. What is NOT required before the next comparison stage

Do not require:

```text
complete ASP bill-of-material loss closure
full product calorimetry of every component
exact optimization of R110/R119 snubbers
replacement-part study
complete transformer redesign
full Candidate #10 circuit
```

Only evidence that discriminates a retained PG is required.

---

# 16. Decision state after plan

```text
Minimum falsification/evidence plan       = ESTABLISHED v1
PG × PM compatibility                     = COMPLETE v1
mechanism combination                     = NOT EXECUTED

H1 PG-1 evidence                           = REQUIRED / NOT YET CLOSED
H2 PG-2 materiality gate                   = REQUIRED / HARD STOP
H3 PG-3 evidence                           = REQUIRED / NOT YET CLOSED
H4 PG-4 materiality gate                   = REQUIRED / HARD STOP

A1                                        = PM-1 FAIR FALSIFIER
B                                         = DIRECT-HFL ARCHITECTURE COMPARATOR / MUST DECOMPOSE PMs
C2                                        = PM-2-DOMINANT COMPARATOR
C3                                        = PM-3-DOMINANT COMPARATOR
X2-P                                      = CONDITIONAL PM-5 COMPARATOR AFTER H4
X2-A                                      = CONDITIONAL PM-6 COMPARATOR AFTER H4

T_mat,PG1...PG4                           = MUST BE PREDECLARED / NUMERICAL VALUES OPEN
Candidate #10                             = HOLD / NOT_ASSIGNED
Novelty                                   = NOT_ESTABLISHED
```

Next valid action:

```text
Create the executable evidence-acquisition worksheet
↓
for H1/H2/H3/H4 define:
  exact probe / signal
  instrument / method
  operating point
  sample window / synchronization
  calculation
  uncertainty field
  PASS / FAIL field
↓
separate measurements that can be done on A0 now
from external-comparator evidence that must be acquired from papers/models
↓
execute highest-information hard gates first
```

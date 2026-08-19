# 36 — Theoretical Mechanism Combination Screen v1

Status date: 2026-08-20  
Role: `PRE-PG EXPLORATORY THEORY / MECHANISM COMBINATION SCREEN`  
Evidence class: `THEORETICAL / MODELLED / NOT A0 MEASURED`  
Topology-candidate authorization: `NOT GRANTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose and workflow deviation

This file records a user-authorized exploratory branch that temporarily moves theoretical combination work ahead of energized H2/H4 acquisition.

The earlier readiness record remains valid:

```text
research/35_H2_H4_PREMEASUREMENT_READINESS_GATE.md
```

but it is **deferred from the immediate NEXT**, not deleted from the eventual validation chain.

This branch is allowed to:

```text
combine PM classes theoretically
calculate first-principles gain/current/stress relations
build parametric loss equations
reject structurally unattractive combinations early
select combinations for later circuit-level simulation
```

It is NOT allowed to:

```text
claim PG-1...PG-4 are verified
promote any combination to Topology Candidate
claim Candidate #10
claim novelty
use theoretical results as a substitute for later matched evidence
```

This creates a deliberate distinction:

```text
PRE-PG theoretical combination exploration
≠
POST-PG authorized topology synthesis under CALG-0
```

File 33 remains the authority for formal candidate promotion.

---

## 2. Research boundary used for first-principles calculations

Research anchor:

```text
Vin = 12 Vdc
Pout = 2 kW
Vout = 220 Vac / 1φ
```

The ideal AC peak is:

```text
Vout,pk = sqrt(2) × 220
         = 311.13 V
```

Therefore an idealized first voltage-domain gain floor is:

```text
G_req,min = 311.13 / 12
          = 25.93×
```

Important:

```text
25.93× is an optimistic static gain floor.
```

A real converter may require more voltage margin because of modulation, semiconductor drop, regulation, ripple and transient requirements.

Current scales:

```text
I_source,ideal @ 2 kW / 12 V = 166.67 A
I_source @ 95% reference      = 175.44 A
I_HV scale @ 2 kW / 311.13 V  = 6.43 A
```

Thus the fundamental X1 task is approximately:

```text
~167–175 A source-domain current
↓
first major V/I-domain transformation
↓
~6.4 A-class high-voltage-domain current scale
```

---

## 3. Hard theoretical burden of the three primary X1 mechanisms

### 3.1 PM-1 only — magnetic transformation

Using a generic static transformation-ratio proxy:

```text
G_PM1,proxy ≈ 25.93
```

This is NOT an exact transformer turns ratio because the required winding ratio depends on the switching topology, applied primary waveform, rectifier arrangement and duty/modulation.

Primary theoretical burden:

```text
large magnetic voltage ratio
LV primary RMS current
winding copper / Rac
core loss
leakage / magnetizing effects
```

However PM-1 can accomplish the large domain transformation without requiring an extreme boost duty ratio or a 26-cell ideal capacitor stack.

### 3.2 PM-2 only — ideal boost-type inductive transfer

Ideal boost relation:

```text
G = 1 / (1-D)
```

At 12 V → 311.13 V:

```text
D = 1 - 1/25.93
  = 0.9614
  = 96.14%
```

At 24 V → 311.13 V:

```text
D ≈ 92.29%
```

Therefore a single ideal PM-2 boost step is retained as a useful negative/extreme-ratio reference, but it has a strong structural duty/current-stress burden at the 12 V anchor.

### 3.3 PM-3 only — ideal capacitor voltage stacking

If the voltage-building mechanism is represented by an ideal integer stacking factor `k`:

```text
k_min = ceil(25.93)
      = 26
```

At 24 V:

```text
k_min = 13
```

This does NOT mean every practical switched-capacitor topology literally needs 26 identical cells. It is a lower-level voltage-factor indicator showing how severe the static ratio is if capacitor stacking carries the full 12 V → 311 V burden by itself.

Primary theoretical burden:

```text
large stacking / multiplication factor
capacitor RMS current
charge redistribution
switch count / series conduction
balancing / precharge
```

---

## 4. Gain-sharing equations for combined X1 mechanisms

Let:

```text
G_req = 25.93
G_M1  = magnetic transformation factor proxy
G_M2  = 1/(1-D)
G_M3  = k
```

For multiplicative first-order gain sharing:

```text
G_req ≈ G_M1 × G_M2 × G_M3
```

This is a static screening relation, not a complete converter model.

### 4.1 PM-1 + PM-2

```text
G_M1 = G_req / G_M2
     = G_req × (1-D)
```

At 12 V:

| PM-2 duty D | PM-2 gain | remaining PM-1 ratio proxy |
|---:|---:|---:|
| 0.50 | 2.00× | 12.96× |
| 0.60 | 2.50× | 10.37× |
| 0.70 | 3.33× | 7.78× |
| 0.80 | 5.00× | 5.19× |

Interpretation:

```text
PM-2 can reduce magnetic ratio burden,
but the gain is bought with another full-power inductive/switching path.
```

### 4.2 PM-1 + PM-3

```text
G_M1 = G_req / k
```

At 12 V:

| PM-3 stack factor k | remaining PM-1 ratio proxy |
|---:|---:|
| 2 | 12.96× |
| 3 | 8.64× |
| 4 | 6.48× |
| 6 | 4.32× |
| 8 | 3.24× |

Interpretation:

```text
capacitor stacking can reduce magnetic ratio,
but redistribution / ESR / extra switches must be counted as relocated/new loss.
```

### 4.3 PM-2 + PM-3

For ideal boost plus stacking:

```text
G_M2 = G_req / k
D = 1 - k/G_req
```

when `G_req/k > 1`.

At 12 V:

| PM-3 stack k | required PM-2 gain | required ideal duty |
|---:|---:|---:|
| 2 | 12.96× | 92.29% |
| 4 | 6.48× | 84.57% |
| 6 | 4.32× | 76.85% |
| 8 | 3.24× | 69.14% |
| 13 | 1.99× | 49.85% |

Theoretical consequence:

```text
PM-2 + PM-3 does not escape extreme ratio for free.
To reduce PM-2 duty to roughly 0.7,
about an 8× capacitor-stacking factor is still required in this idealized split.
```

### 4.4 PM-1 + PM-2 + PM-3

```text
G_M1 = G_req × (1-D) / k
```

Examples at 12 V:

```text
k=2, D=0.6 → G_M1≈5.19
k=3, D=0.6 → G_M1≈3.46
k=4, D=0.6 → G_M1≈2.59
```

This shares static stress very effectively, but immediately incurs a CALG-minimality risk because three different X1 mechanisms are carrying one voltage-domain transformation function.

It is therefore retained only as a reserve theoretical reference until simpler two-mechanism combinations fail on total loss.

---

## 5. Low-voltage current-domain resistance sensitivity

Using the 95% scaling current:

```text
I_source = 175.44 A
```

Every small resistance added while the full source current still flows has:

```text
P = I²R
```

| added full-current resistance | conduction loss |
|---:|---:|
| 0.05 mΩ | ~1.54 W |
| 0.10 mΩ | ~3.08 W |
| 0.25 mΩ | ~7.69 W |
| 0.50 mΩ | ~15.39 W |
| 0.65 mΩ | ~20.00 W |
| 1.00 mΩ | ~30.78 W |

Research consequence:

```text
an added mechanism located before X1 completion is expensive.
```

Therefore PM-2 / PM-4 / PM-6 paths that add full-current switch, inductor or circulation burden in the 12 V domain must clear a very high bar before their claimed savings are accepted.

This is a theoretical sensitivity, not a measured A0 resistance.

---

## 6. PM-4 theoretical admission equation

PM-4 does not create static voltage gain. It is an overlay whose purpose is to reduce commutation loss.

A first-order ZVS-type energy condition is:

```text
0.5 L_eq I_comm² >= 0.5 C_eq V_sw²
```

or:

```text
I_comm,min >= V_sw × sqrt(C_eq / L_eq)
```

This defines the minimum reactive/commutation current required to move the relevant node capacitance under the simplified energy condition.

The loss gate remains:

```text
P_hard-commutation,saved
>
P_circulation,added
+ P_resonant-component
+ P_control/drive,added
+ P_residual-switching
```

Therefore PM-4 is only theoretically attractive when the required `I_comm` does not create a larger RMS/conduction penalty.

---

## 7. First theoretical combination set

PM-7 is required in every complete 12 Vdc → 220 Vac candidate because AC synthesis must exist somewhere, although X1 and X3 may physically overlap.

The first theoretical screen intentionally defers PM-5 / PM-6 dedicated X2 mechanisms. This does NOT remove the single-phase 2ω energy-balance requirement; it only isolates the X1/X3 combination problem first.

### R1 — PM-1 + PM-7

```text
magnetic X1
+
AC synthesis
```

Role:

```text
baseline mechanism combination
```

Likely family after actual graph:

```text
#01 / #02 / #09 depending implementation
```

### R2 — PM-1 + PM-4 + PM-7

```text
magnetic X1
+
reactive-energy-assisted commutation
+
AC synthesis
```

Why retained first:

```text
smallest mechanism addition to magnetic baseline
PM-4 directly attacks PG-2 hypothesis
no second voltage-building mechanism is required
```

Main new loss to audit:

```text
circulating / resonant RMS
reactive component loss
control/dead-time sensitivity
```

Status:

```text
FIRST THEORETICAL PRIORITY
NOT TOPOLOGY CANDIDATE
```

### R3 — PM-2 + PM-7

Static burden:

```text
D≈96.14% ideal at 12 V → 311 V
```

Status:

```text
NEGATIVE / EXTREME-DUTY REFERENCE
```

### R4 — PM-2 + PM-4 + PM-7

PM-4 may reduce switching loss but does not remove the 96% static boost-duty requirement if PM-2 alone still carries the full voltage gain.

Status:

```text
SECONDARY NEGATIVE / COMMUTATION REFERENCE
```

### R5 — PM-3 + PM-7

Static burden:

```text
~26× ideal voltage-factor requirement at 12 V anchor
```

Status:

```text
NEGATIVE / HIGH-STACK REFERENCE
```

### R6 — PM-1 + PM-2 + PM-4 + PM-7

Representative gain split:

```text
D=0.6
PM-2 gain=2.5×
remaining PM-1 ratio proxy≈10.37×
```

Potential benefit:

```text
reduce magnetic ratio burden
use controlled inductive energy for transfer / commutation
```

Mandatory new loss:

```text
inductor/leakage RMS
circulating current
additional active-switch conduction/switching
magnetic + inductive interaction
```

Likely family:

```text
#03 active-HFT/DAB-like
or #04 coupled-inductor/high-gain depending actual graph
```

Status:

```text
SECOND THEORETICAL PRIORITY
NOT TOPOLOGY CANDIDATE
```

### R7 — PM-1 + PM-3 + PM-7

Representative split:

```text
k=3
remaining PM-1 ratio proxy≈8.64×
```

Potential benefit:

```text
reduce transformer ratio / secondary burden
build part of voltage collectively with charge transfer
```

Mandatory new loss:

```text
capacitor RMS / ESR
charge redistribution
extra switch/diode path
balancing/precharge
```

Likely family:

```text
#04 / #08 depending actual graph
```

Status:

```text
THIRD THEORETICAL PRIORITY
NOT TOPOLOGY CANDIDATE
```

### R8 — PM-2 + PM-3 + PM-7

Representative result:

```text
k=8 → D≈69.14%
```

Interpretation:

```text
meaningful duty reduction requires substantial capacitor stacking.
```

Status:

```text
RETAIN AS NON-MAGNETIC COMPARATOR
NOT FIRST SYNTHESIS PRIORITY
```

### R9 — PM-1 + PM-2 + PM-3 + PM-7

Representative result:

```text
k=3, D=0.6 → remaining PM-1 ratio proxy≈3.46×
```

This looks attractive by static gain sharing but is penalized by mechanism count and likely interaction loss.

Status:

```text
RESERVE ONLY
CALG-1 MINIMALITY RISK
```

---

## 8. Full theoretical loss ledgers

The first-principles total candidate loss must be written as:

```text
P_loss,total
= P_cond
+ P_sw
+ P_mag
+ P_cap
+ P_rect
+ P_circ
+ P_buffer
+ P_aux
+ P_other
```

### PM-1 dominant path

```text
P_PM1
= P_primaryCu
+ P_core
+ P_secondaryCu
+ P_leakage-associated
+ P_support-switch/rectification
```

### PM-2 dominant path

```text
P_PM2
= I_L,rms² R_L
+ P_core,L
+ P_switch,cond
+ P_switch,sw
+ P_rect/sync
+ P_ripple/circulation
```

### PM-3 dominant path

```text
P_PM3
= Σ(I_C,rms² ESR)
+ P_dielectric
+ P_charge-redistribution
+ P_switch,cond/sw
+ P_balance/precharge
```

### PM-4 overlay

```text
P_PM4,net_added
= P_circ,added
+ P_resonant-component
+ P_control/drive,added
+ P_residual-commutation
- P_hard-commutation,removed
```

PM-4 is beneficial only if this net term is negative after matched accounting.

### PM-7 AC synthesis

```text
P_PM7
= P_switch,cond
+ P_switch,sw/comm
+ P_deadtime/recovery
+ P_filter-associated where inside boundary
+ P_balance/circulation where applicable
```

---

## 9. First theoretical decision

Current first-principles screen does **not** establish a winner in watts because device/magnetic/capacitor parameters are not yet fixed.

It does establish structural ordering for the next circuit-model stage:

```text
Priority 1 — R2 = PM-1 + PM-4 + PM-7
Reason: minimum added mechanism count and direct commutation-loss hypothesis.

Priority 2 — R6 = PM-1 + PM-2 + PM-4 + PM-7
Reason: shares transformation burden and may reuse inductive energy for commutation, but adds RMS/circulation risk.

Priority 3 — R7 = PM-1 + PM-3 + PM-7
Reason: shares static voltage gain without extreme boost duty, but adds charge-transfer loss.

Comparator — R8 = PM-2 + PM-3 + PM-7
Reason: non-magnetic alternative, but still needs large stacking factor to avoid extreme duty.

Negative references — R3 / R5
Reason: PM-2-only requires ~96% ideal duty; PM-3-only requires ~26× ideal stacking at 12 V.

Reserve — R9
Reason: excellent static stress sharing but high mechanism-count / interaction-loss / minimality risk.
```

No combination is promoted beyond:

```text
THEORETICAL COMBINATION
```

---

## 10. Revised immediate research sequence

User-authorized exploratory sequence:

```text
#01...#09 architecture coverage
↓
X1/X2/X3 + PM-1...PM-7
↓
PG hypotheses remain unverified
↓
THEORETICAL COMBINATION SCREEN              ✅ v1 / THIS FILE
↓
construct actual circuit graph for R2 / R6 / R7 / R8
↓
parameterized circuit-level loss simulation
↓
early theoretical rejection / retention
↓
return to PG evidence / readiness gates before formal candidate promotion
↓
Combination Loss Audit under File 33
↓
matched total-loss result
↓
#01...#09 reclassification
↓
Topology Candidate only after formal gates
```

The H2/H4 readiness work is therefore:

```text
DEFERRED FROM IMMEDIATE NEXT
NOT CANCELLED
```

---

## 11. Next action

Build four actual theoretical circuit graphs in this order:

```text
R2 — PM-1 + PM-4 + PM-7
R6 — PM-1 + PM-2 + PM-4 + PM-7
R7 — PM-1 + PM-3 + PM-7
R8 — PM-2 + PM-3 + PM-7
```

For each graph, resolve:

```text
actual MOS / diode / L / C / transformer roles
switch states
current paths
X1 start / completion
X2 = none/dedicated/source-borne in first screen
X3 implementation
static gain equation
semiconductor voltage/current stress
RMS-current equation
switching / magnetic / capacitor loss equations
interaction-only losses
```

Then perform matched theoretical loss comparison at 12 V / 2 kW / 220 Vac before any hardware-readiness work resumes.

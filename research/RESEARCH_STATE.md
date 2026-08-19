# 低壓大電流 DC→AC — Current Research State

> 狀態日期：2026-08-19  
> Novelty：`NOT_ESTABLISHED`  
> Current phase：`Physical Gap Validation`

## 1. Research envelope

```text
Vin    = 12–24 Vdc
Pout   = 1–3 kW
Vout   = 220 Vac / 1φ
anchor = 12 V / 2 kW
```

Anchor scaling:

```text
Iin,ideal = 166.7 A
Iin@95% reference ≈175.4 A
20 W LV-conduction budget → R_eq,max≈0.65 mΩ
```

Core question:

> 不是研究怎麼升壓，而是研究低壓百安培能量怎麼走，才最少變成熱。

Mandatory rule:

```text
P_saved > P_added
```

---

## 2. Research-object correction — CRITICAL

ASP-2000 R52 is:

```text
A0 real-product benchmark
physical-evidence source
falsification reference
```

It is **not**:

```text
the product to optimize
an ASP redesign project
a component-replacement project
```

A0 work is now allowed only when it discriminates a topology-level physical-gap hypothesis.

Authoritative screen:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
```

---

## 3. Functional coordinates / family set — DEFINITION GATE v1

Authoritative definition:

```text
research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md
```

Functional coordinates are now explicitly defined as **functions / regions**, not fixed components or mandatory serial stages:

```text
X1 = first major voltage/current-domain transformation region
X2 = 2ω / bidirectional energy-buffer and routing coordinate
X3 = complete single-phase AC-synthesis region
```

Formal rules:

```text
X1 ≠ transformer by definition
X2 ≠ capacitor by definition
X3 ≠ H-bridge by definition

X1 / X2 / X3 MAY overlap physically
but MUST remain distinguishable by function and loss accounting
```

X1 operational boundary:

```text
start
= first main-path processing region that begins creating a new voltage/current domain

completion
= first boundary where majority main-path power is demonstrably in a sustained reduced-current domain
```

Normalized X1 quantities:

```text
G_V,X1 = V_domain,after / V_source
ρ_I,X1 = I_rms,after / I_source,rms
P_X1   = main-path power transferred through X1
η_X1   = P_after / P_before under declared boundary
```

PG-1 pre-X1 exposure is now operationalized primarily as:

```text
P_preX1,cond
≈ Σ(I_rms,k² · R_eff,k)
 + Σ(P_semiconductor,cond,k)
```

with product-interface / startup / packaging losses separated from intrinsic conversion loss.

Working families remain:

```text
#01 Low-Frequency Transformer Inverter
#02 HFT + Rectifier + HV DC Bus + VSI
#03 Active-HFT / DAB + VSI
#04 Non-Isolated High-Gain DC/DC + VSI
#05 Bidirectional DC/DC + VSI
#06 Single-Stage Boost / Buck-Boost Inverter
#07 Z/qZ-source
#08 Switched-Capacitor / Multilevel Main Path
#09 Direct High-Frequency-Link DC–AC
```

Current benchmark emphasis:

```text
#02 → A0/A1 magnetic benchmark
#03 → active-HFT benchmark
#04 → non-isolated/high-gain/current-distribution benchmark
#09 → direct-HFL benchmark
```

Definition cross-test completed at v1:

```text
A0 / #02 magnetic HFT path      = PASS
#04 distributed high-gain path  = PASS
#09 direct HFL path              = PASS
```

Nine-family normalization record:

```text
research/29_NINE_FAMILY_X1_X2_X3_NORMALIZATION.md
```

Key normalization findings:

```text
nine families = architecture coverage map
NOT nine mutually-exclusive physical mechanisms

#05 = energy-routing / architecture umbrella; X1 physics implementation-dependent
#08 = composite switched-capacitor + multilevel umbrella
#01/#06/#07/#08/#09 may contain physical X1/X3 overlap
```

Mechanism extraction records:

```text
research/26_NINE_FAMILY_MECHANISM_EXTRACTION_MATRIX.md
research/27_MECHANISM_POOL_CHECKPOINT_AND_PQ50_CONTEXT.md
research/30_L3_PHYSICAL_MECHANISM_DICTIONARY.md
research/31_PG_PM_COMPATIBILITY_SCREEN.md
```

```text
Candidate #10 = HOLD / NOT_ASSIGNED
```

---

## 4. Working architecture — still only a hypothesis

```text
12 V source
↓
very-short / very-low-R common LV path
↓
local bulk + HF decoupling
↓
early distributed branch power cells
↓
branch switching + X1
↓
reduced-current domain
↓
[optional active X2]
↓
X3
↓
220 Vac
```

Status:

```text
very-short common path = KEEP / physical constraint
local decoupling = KEEP / must prove local-loop benefit
early fan-out = HYPOTHESIS / NOT automatic loss reduction
branch switching + X1 = CORE RESEARCH REGION
active X2 = OPTIONAL / NOT_PROVEN
```

Important correction from Definition Gate:

```text
this drawing is a working architecture hypothesis
NOT a universal requirement that X1 / X2 / X3 be three separate serial stages
```

---

## 5. A0 structural baseline — ASP-2000 R52

### Positive distribution

```text
BAT+
├─ F2/F3/F5/F6 → local LV bulk → T1 center tap
└─ F7/F8/F9/F10 → local LV bulk → T2 center tap
```

### Primary switching

```text
A node = T1-A + T2-A → 10 parallel MOS → B
C node = T1-C + T2-C → 10 parallel MOS → B
```

All 20 main MOS sources return to common `B`.

Q19 is verified connected; the old 9+10 model is superseded.

Gate architecture:

```text
4 local driver subgroups
2 logical A/C functions
```

R52 also contains a U5-compatible buffered distribution path and direct 0Ω bypass options. Production stuffing remains open; do not treat the bypass or U5 option as a measured timing fact.

### Battery negative interface

```text
B
↓
7 × CSD18510KCS
↓
BAT-
```

ASP product function:

```text
Input reverse polarity protection (AUTO-RECOVERY)
= VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
```

Q39...Q65 as low-side ideal-diode-style implementation:

```text
STRONGLY_SUPPORTED
```

BOCP analog relation:

```text
ΔV_M5 = V_B - V_BAT-
V_BOCP - V_B ≈22.1 × ΔV_M5
```

This bank is product-interface protection/sensing overhead, not intrinsic X1 loss.

### X1→HV

```text
A/C LV switching begins X1 processing
↓
T1 + T2 PQ5050 magnetic transformation
↓
secondary high-voltage / reduced-current domain establishes X1 completion
↓
secondary collective/series formation
↓
RL1 + R40/R41 precharge/bypass region
↓
D1/D5 + D2/D6 rectification
↓
HV DC-link
↓
X3
```

RL1 precharge/bypass role is resolved at connectivity/net-name level. Startup precharge energy is not ordinary steady-state X1 loss.

### Primary commutation network

Direct A/C adjacency establishes two passive series-RC snubber branches across the primary switched nodes.

```text
direct primary-node damping
= passive dissipative RC network
```

Actual snubber watts and total commutation loss remain open.

---

## 6. Manufacturing-copper correction — ACTIVE

R52 manufacturing specification tied to the same Gerber requires:

```text
2 layers
base copper =2.0 oz
finished copper >82 µm
```

Therefore the old 35.56 µm as-built assumption is superseded.

Current geometry-only conservative bounds at the 12 V / 2 kW reference:

```text
BAT+ common PCB            ≤~3.32 W
T1 local PCB               ≤~1.17 W
T2 PCB excluding J8        ≤~0.48 W
partial positive PCB-only  ≤~4.98 W
```

Status:

```text
MANUFACTURING_GEOMETRY_BOUND / NOT_MEASURED
```

Research consequence:

```text
PCB distribution = MATERIAL / MUST NOT IGNORE
PCB distribution = NOT PROVEN DOMINANT
```

---

## 7. Other current non-measured scales

Main A/C MOS:

```text
20 × CSD18542KCS total
10 MOS per logical switch
simplified 25°C max-RDS conduction scale ≈12.3 W
```

Battery interface:

```text
7 × CSD18510KCS
simplified 25°C max-RDS scale ≈7.47 W
```

Do not sum these with geometry bounds into a claimed measured product total.

---

## 8. Transformer evidence gate

Verified:

```text
T1/T2 = PQ5050
center-tapped primary connectivity
secondary series relationship
```

Open for the actual A0 population:

```text
production transformer P/N
turns ratio
Lm / Lk
winding DCR / Rac
core material / Ae / Ve
actual magnetic watts
```

`M1-PQ50-V121-A` belongs to another ASP-3000/24 V variant and remains context-only.

A separately supplied private approval sheet for `M1-PQ50-V108-A` establishes useful PQ50-class industrial context:

```text
4-turn wide-foil low-voltage windings
30-turn secondary
No Gap core assembly
nonzero leakage-inductance test values
MnZn ferrite material options
```

but direct linkage to ASP-2000 R52 T1/T2 is not established.

Therefore:

```text
M1-PQ50-V108-A = PQ50-CLASS CONTEXT_ONLY / NOT A0 NUMERICAL EVIDENCE
A0 magnetic burden = OPEN
```

not `magnetics are the problem`.

---

## 9. Product-engineering items — STOP as independent research targets

The following may be measured/count under a matched product contract, but do not by themselves establish a topology research gap:

```text
PCB / bus / connector geometry
Fuse / J8 / contact resistance
battery reverse-protection MOS implementation
BOCP circuit
RL1 / precharge implementation
U5 / R212 / R213 stuffing
exact RC snubber value tuning
```

Continue tracing any of them only if the result discriminates PG-1…PG-4 below.

---

## 10. Current physical-gap hypotheses

Physical-Gap promotion is now governed by `research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md`:

```text
OBSERVATION
↓
TOPOLOGY-STRUCTURAL SIGNAL
↓
PHYSICAL-GAP HYPOTHESIS
↓
FAIR-FALSIFICATION TEST
↓
SURVIVES / REJECTED
↓
VERIFIED PHYSICAL GAP only if all gates pass
```

Promotion requires:

```text
G1 measurable physical quantity
G2 survives abstraction from A0 product details
G3 fair existing-method falsifier
G4 matched comparison boundary
G5 materiality criterion
G6 loss-shifting audit with P_saved > P_added
```

### PG-1 — extreme-LV conduction exposure before X1

Question:

> Under a matched contract, how much source-domain RMS / conduction burden is required before different X1 mechanisms complete the first major voltage/current-domain transformation, and can that burden be reduced with lower total added loss?

Status:

```text
HYPOTHESIS / TOPOLOGY-RELEVANT
```

A0 signal:

```text
~175 A reference input current
heavy copper already used
20 main LV MOS already used
~12.3 W simplified main-MOS conduction scale
```

Operational quantities now include:

```text
P_preX1,cond
I_source,rms
source-domain semiconductor conduction
source-domain current-path burden
```

Need fair A1 / alternative-X1 falsification before claiming a verified gap.

### PG-2 — dissipative commutation / leakage-energy handling

Question:

> Is a material amount of X1 switching/leakage/Coss energy disposed dissipatively, and can another mechanism reduce/recover it with lower total added loss?

A0 signal:

```text
passive A↔C RC damping network = VERIFIED
```

Status:

```text
HYPOTHESIS / STRONG STRUCTURAL SIGNAL
```

Need:

```text
P_snubber
P_switching overlap
commutation significance
soft-commutated A1 / active-HFT falsifier
```

RC-snubber existence proves a dissipative path, not gap materiality.

### PG-3 — total transformation burden at extreme ratio

Question:

> After fair optimization, does magnetic X1 retain a first-order total transformation burden versus alternative X1 mechanisms when all alternative inductor/capacitor/diode/charge-transfer/circulating losses are counted symmetrically?

Status:

```text
OPEN / NOT YET A GAP
```

Important correction:

```text
PG-3 comparison quantity = TOTAL TRANSFORMATION BURDEN
not magnetic loss alone
```

### PG-4 — single-phase 2ω energy reflection into LV source

Question:

> How much unavoidable 2ω pulsating energy returns through the expensive LV source path, and is local/post-X1 buffering net-beneficial?

Status:

```text
HYPOTHESIS / NOT_ESTABLISHED
active X2 = OPTIONAL / NOT_PROVEN
```

Operational observables:

```text
P_2ω,source
I_2ω,source
E_2ω,buffer
ΔV_buffer,2ω
P_X2,added
```

---

## 11. Things that are not research gaps

```text
early fan-out = DESIGN DIMENSION
more parallel MOS = DESIGN DIMENSION
earlier voltage rise / early X1 = STRATEGY
active X2 = SOLUTION HYPOTHESIS
remove HV DC bus = ARCHITECTURE OPTION
continuous-input current = RESULTING PROPERTY unless tied to a quantified mechanism
```

None of them is a novelty or research-gap claim by itself.

---

## 12. Minimum hypothesis-driven evidence gate

The research no longer requires an exhaustive ASP loss audit before mechanism comparison.

Only collect A0 evidence that discriminates the four PGs.

### H1 → PG-1

```text
I_source
I_T1 / I_T2 if accessible
A/C on-state VDS/current evidence
switch temperature
```

Output:

```text
measured/bounded P_preX1,cond scale
```

### H2 → PG-2

```text
fs / duty / dead time
V_A-B / V_C-B
relevant switch current
V_R110 / V_R119
```

Output:

```text
P_switching scale
P_snubber
```

### H3 → PG-3

```text
T1/T2 RMS current
primary volt-second
transformer temperature
correct L/ratio/DCR/material when obtainable
```

### H4 → PG-4

```text
source current waveform/spectrum at100/120 Hz
HV DC-link ripple
```

These are research-hypothesis measurements, not ASP optimization measurements.

---

## 13. Cross-X1 comparison axes

Compare surviving gaps across A1 / Direct-HFL / non-isolated high-gain using:

```text
M1 extreme-LV RMS/conduction exposure before X1
M2 switching / commutation / dissipative-clamp energy
M3 total transformation / storage burden
M4 internal circulating / reactive RMS
M5 2ω energy reflected to LV source
M6 added active processing stages/functions
M7 matched isolation/protection/product contract
```

No architecture wins merely by deleting a stage or product function.

---

## 14. PG × canonical physical-mechanism screen — COMPLETE v1

Authoritative records:

```text
research/30_L3_PHYSICAL_MECHANISM_DICTIONARY.md
research/31_PG_PM_COMPATIBILITY_SCREEN.md
```

Canonical mechanisms remain:

```text
PM-1 — Magnetic Flux-Linkage Transformation
PM-2 — Inductive Energy Transfer
PM-3 — Capacitive Charge-Transfer / Voltage-Stacking
PM-4 — Reactive-Energy-Assisted Commutation
PM-5 — Capacitive Field-Energy Buffering
PM-6 — Controlled Bidirectional Storage-Port Transfer
PM-7 — Semiconductor Switching-State AC Synthesis
```

The 28-cell screen is complete using:

```text
DIRECT / CONDITIONAL / TRADE-OFF / RISK / IRRELEVANT
```

where compatibility does not imply benefit or a verified gap.

Primary retained pairs:

```text
PG-1 × PM-1  fair optimized magnetic-X1 falsifier
PG-1 × PM-2  inductive alternative-X1 comparator
PG-1 × PM-3  capacitive-transfer alternative-X1 comparator

PG-2 × PM-4  direct commutation-loss mechanism

PG-3 × PM-1  magnetic transformation benchmark
PG-3 × PM-2  inductive transformation alternative
PG-3 × PM-3  capacitive-transfer transformation alternative

PG-4 × PM-5  passive 2ω buffering
PG-4 × PM-6  active storage-port routing, H4-gated
```

Conditional modifiers retained only for accounting / later architecture evaluation:

```text
PG-1 × PM-4
PG-2 × PM-2 / PM-7
PG-3 × PM-4 / PM-7
PG-4 × PM-2 / PM-7
```

Important stop-lines:

```text
PG-2 × PM-4 requires H2 materiality before becoming a research direction
PG-4 × PM-6 requires H4 materiality before active X2 is justified
PM-7 alone is not an X1 or X2 solution
PM-5/PM-6 are not primary PG-1/PG-3 mechanisms
```

Historical pools remain only as reasoning/search buckets:

```text
MP-A Early X1              = Strategy pool
MP-B Soft commutation      = primarily PM-4
MP-C Collective HV build   = PM-1 / PM-2 / PM-3 depending actual path
MP-D Integrated AC         = architecture strategy using PM-7 variants
MP-E 2ω routing            = PM-5 and/or PM-6
MP-F Continuous input      = L4 resulting property / control outcome
```

Formal consequence:

```text
PG × MP-A...MP-F = REJECTED
PG × canonical PM-1...PM-7 = COMPLETE v1
Mechanism combination = STILL CLOSED
```

---

## 15. Benchmark stack / next sequence

```text
A0 — actual ASP-2000 structural evidence
A1 — fair optimized magnetic HFT / PM-1 falsifier
B  — Direct HFL architecture comparator
C  — non-isolated high-gain/current-distribution architecture comparator
D  — later candidate only if a gap survives
```

Current sequence:

```text
A0 structural evidence freeze
↓
Physical-gap screen
↓
Nine-family mechanism extraction                         ✅ v1
↓
X1 / X2 / X3 + Physical-Gap Definition Gate              ✅ v1
↓
Nine-family common X1/X2/X3 normalization                ✅ v1
↓
Canonical L3 physical-mechanism dictionary               ✅ v1
↓
PG-1...PG-4 × PM-1...PM-7 compatibility screen          ✅ v1
↓
Build minimum falsification / evidence plan for retained pairs ← NEXT
↓
H1 / H2 / H3 / H4 only where they discriminate a surviving PG
↓
assign fair A1 / B / C comparator roles to retained PMs
↓
reject gaps that fail materiality or P_saved > P_added
↓
Topology synthesis only for surviving verified gap
↓
Candidate #10 only if existing #01–#09 do not reasonably cover the resulting main energy path
```

Immediate evidence logic:

```text
PG-1 → H1 establishes A0 pre-X1 conduction scale; compare PM-1 vs PM-2 vs PM-3
PG-2 → H2 is a hard materiality gate before PM-4 research direction
PG-3 → H3 prevents assuming magnetics are the problem; compare total PM-1/2/3 burden
PG-4 → H4 is a hard prerequisite before PM-5/PM-6 X2 work; active X2 remains conditional
```

---

## 16. Formal decision state

```text
Research phase                         = Physical Gap Validation
A0 role                                = REAL-PRODUCT EVIDENCE / NOT OPTIMIZATION TARGET
A0 structural reverse engineering      = SUFFICIENT_FOR_GAP_SCREEN
R52 finished copper                    = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm PCB model                 = SUPERSEDED
partial positive PCB geometry bound    = ≤~4.98 W / NOT_MEASURED
main-MOS conduction scale              = ~12.3 W / DATASHEET_BOUND
battery-interface scale                = ~7.47 W / PRODUCT-INTERFACE DATASHEET_BOUND
A/C passive RC damping                 = VERIFIED
A0 transformer numerical parameters    = OPEN
M1-PQ50-V108-A                         = CONTEXT_ONLY / NOT A0

X1 definition                          = ESTABLISHED v1 / FUNCTIONAL REGION
X2 definition                          = ESTABLISHED v1 / ENERGY-ROUTING COORDINATE
X3 definition                          = ESTABLISHED v1 / AC-SYNTHESIS REGION
X1/X2/X3 physical overlap              = ALLOWED
fixed three-stage interpretation       = REJECTED
Physical-Gap promotion gate            = ESTABLISHED v1

PG-1 extreme-LV conduction exposure    = HYPOTHESIS
PG-2 dissipative commutation handling  = HYPOTHESIS / STRONG SIGNAL
PG-3 total transformation burden       = OPEN
PG-4 2ω source reflection              = HYPOTHESIS

Nine-family mechanism extraction       = COMPLETE v1
Nine-family X1/X2/X3 normalization     = COMPLETE v1
Nine-family role                       = ARCHITECTURE COVERAGE MAP
#05 unique X1 physics                   = REJECTED
#08 single-ontology interpretation      = REJECTED
Ontology L1/L2/L3/L4                   = ESTABLISHED v1
Raw L3 PM-R1...PM-R13 direct screening = SUPERSEDED
Canonical L3 dictionary PM-1...PM-7   = ESTABLISHED v1
Canonical L3 mechanism count           = 7
Support primitive SP-1                 = ESTABLISHED
MP-A...MP-F direct PG crossing          = REJECTED
PG × canonical Physical Mechanism      = COMPLETE v1 / 28 CELLS SCREENED
Primary PG-1 mechanism set             = PM-1 / PM-2 / PM-3
Primary PG-2 mechanism set             = PM-4 / H2-GATED
Primary PG-3 mechanism set             = PM-1 / PM-2 / PM-3
Primary PG-4 mechanism set             = PM-5 / PM-6 / H4-GATED
Minimum falsification/evidence plan    = NEXT
Mechanism combination                  = NOT YET EXECUTED
fan-out benefit                        = NOT_PROVEN
active X2 benefit                      = NOT_PROVEN / H4-GATED
A1                                     = FAIR FALSIFICATION BENCHMARK / PM-1
Candidate #10                          = HOLD / NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

Detailed records:

```text
11_WORKING_ARCHITECTURE_LOSS_AUDIT.md
20_ASP2000_A0_RL1_HV_PRECHARGE_BYPASS.md
21_ASP2000_A0_TRANSFORMER_PARAMETER_EVIDENCE_GATE.md
22_ASP2000_A0_R52_MANUFACTURED_COPPER_CORRECTION.md
23_ASP2000_A0_PRIMARY_SNUBBER_AND_GATE_DRIVER_BOUNDARY.md
24_ASP2000_A0_U5_DRIVER_VARIANT_AND_SAVPP_GATE.md
25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
26_NINE_FAMILY_MECHANISM_EXTRACTION_MATRIX.md
27_MECHANISM_POOL_CHECKPOINT_AND_PQ50_CONTEXT.md
28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md
29_NINE_FAMILY_X1_X2_X3_NORMALIZATION.md
30_L3_PHYSICAL_MECHANISM_DICTIONARY.md
31_PG_PM_COMPATIBILITY_SCREEN.md
```

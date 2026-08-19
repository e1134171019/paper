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

## 3. Functional coordinates / family set

```text
X1 = first major impedance/current-domain transformation region
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC-synthesis region
```

Working families:

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

Mechanism extraction from #01–#09 is now recorded in:

```text
research/26_NINE_FAMILY_MECHANISM_EXTRACTION_MATRIX.md
research/27_MECHANISM_POOL_CHECKPOINT_AND_PQ50_CONTEXT.md
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
T1 + T2 PQ5050 magnetic transformation
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

### PG-1 — extreme-LV conduction exposure before X1

Question:

> How much loss remains structurally unavoidable while power is still processed in the 12 V / hundred-ampere domain before the first major transformation?

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

Need fair A1 before claiming a gap.

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
```

### PG-3 — magnetic transformation burden at extreme ratio

Question:

> After fair optimization, does magnetic X1 retain a first-order copper/core/leakage burden versus alternative X1 mechanisms?

Status:

```text
OPEN / NOT YET A GAP
```

### PG-4 — single-phase 2ω energy reflection into LV source

Question:

> How much unavoidable 2ω pulsating energy returns through the expensive LV source path, and is local buffering net-beneficial?

Status:

```text
HYPOTHESIS / NOT_ESTABLISHED
active X2 = OPTIONAL / NOT_PROVEN
```

---

## 11. Things that are not research gaps

```text
early fan-out = DESIGN DIMENSION
more parallel MOS = DESIGN DIMENSION
earlier voltage rise = STRATEGY
active X2 = SOLUTION HYPOTHESIS
remove HV DC bus = ARCHITECTURE OPTION
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

## 13. Cross-X1 mechanism comparison axes

After H1–H4, compare surviving gaps across A1 / Direct-HFL / non-isolated high-gain using:

```text
M1 extreme-LV RMS/conduction exposure before X1
M2 switching / commutation / dissipative-clamp energy
M3 magnetic or alternative energy-storage burden
M4 internal circulating / reactive RMS
M5 2ω energy reflected to LV source
M6 added active processing stages/functions
M7 matched isolation/protection/product contract
```

No architecture wins merely by deleting a stage or product function.

---

## 14. Mechanism extraction checkpoint — ACTIVE

Nine-family mechanism extraction is complete at v1.

Detailed matrix:

```text
research/26_NINE_FAMILY_MECHANISM_EXTRACTION_MATRIX.md
```

Current screening pools:

```text
MP-A — Early X1 / leave extreme-LV domain early
MP-B — Soft commutation / leakage-energy utilization
MP-C — Collective high-voltage building
MP-D — Direct / integrated AC synthesis
MP-E — Intentional 2ω energy routing
MP-F — Continuous-input / ripple-current shaping
```

Important gate:

```text
mechanism name alone ≠ physical-gap solution
```

Examples not admitted merely by label:

```text
LLC
DAB
high-gain
switched-capacitor
fan-out
interleaving
active X2 before PG-4 survives
```

Combination rules are locked in `research/27_MECHANISM_POOL_CHECKPOINT_AND_PQ50_CONTEXT.md`.

Next action:

```text
PG × Mechanism compatibility screen
↓
reject redundant / physically conflicting / loss-stacking pairs
↓
retain only 2–3 physically defensible combinations
↓
reclassify each against #01–#09
```

---

## 15. Benchmark stack / next sequence

```text
A0 — actual ASP-2000 structural evidence
A1 — fair optimized magnetic HFT
B  — Direct HFL
C  — non-isolated high-gain/current-distribution
D  — later candidate only if a gap survives
```

Current sequence:

```text
A0 structural evidence freeze
↓
Physical-gap screen
↓
Nine-family mechanism extraction                 ✅ v1
↓
PG × Mechanism compatibility screen              ← NEXT
↓
minimum H1–H4 evidence where needed to discriminate surviving PGs
↓
A1 / B / C X1 mechanism comparison
↓
reject gaps that disappear under fair optimization
↓
Topology synthesis only for surviving gap
↓
Candidate #10 only if existing #01–#09 do not already cover the solution path
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

PG-1 extreme-LV conduction exposure    = HYPOTHESIS
PG-2 dissipative commutation handling  = HYPOTHESIS / STRONG SIGNAL
PG-3 magnetic burden                   = OPEN
PG-4 2ω source reflection              = HYPOTHESIS

Nine-family mechanism extraction       = COMPLETE v1
Mechanism pool MP-A...MP-F              = ESTABLISHED FOR SCREENING
PG × Mechanism compatibility           = NEXT
Mechanism combination                  = NOT YET EXECUTED
fan-out benefit                        = NOT_PROVEN
active X2 benefit                      = NOT_PROVEN
A1                                     = FAIR MECHANISM BENCHMARK AFTER COMPATIBILITY/MINIMUM EVIDENCE
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
```

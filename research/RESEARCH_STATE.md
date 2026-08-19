# 低壓大電流 DC→AC — Current Research State

> 狀態日期：2026-08-19  
> Novelty：`NOT_ESTABLISHED`  
> Current phase：`Physical Gap Validation`

## 1. Research envelope

```text
Vin   = 12–24 Vdc
Pout  = 1–3 kW
Vout  = 220 Vac / 1φ
anchor = 12 V / 2 kW
```

Anchor scaling:

```text
Iin,ideal = 166.7 A
Iin@95% reference ≈ 175.4 A
20 W LV-conduction budget → R_eq,max ≈ 0.65 mΩ
```

Core question:

> **不是研究怎麼升壓，而是研究低壓百安培能量怎麼走，才最少變成熱。**

Necessary average source current cannot disappear before the first major impedance/current-domain transformation. The research variable is how much extra RMS current and how much resistive/commutation path remain in the expensive low-voltage domain.

---

## 2. Structural coordinates

```text
X1 = first major impedance / current-domain transformation region
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC-synthesis region
```

These are functional coordinates, not one component each and not automatically three converter stages.

Preferred ordering:

```text
extreme-LV full-current domain
↓
X1
↓
reduced-current domain
↓
[X2 only if net-beneficial]
↓
X3
```

---

## 3. Nine working power-path families

```text
#01 Low-Frequency Transformer Inverter
#02 HFT + Rectifier + HV DC Bus + VSI
#03 Active-HFT / DAB + VSI
#04 Non-Isolated High-Gain DC/DC + VSI
#05 Bidirectional DC/DC + VSI
#06 Single-Stage Boost / Buck-Boost Inverter
#07 Z-Source / Quasi-Z-Source
#08 Switched-Capacitor / Multilevel Main Path
#09 Direct High-Frequency-Link DC–AC
```

Current status:

```text
#01 = REFERENCE ONLY / poor fit for extreme-LV loss minimization
#02 = PRIMARY REAL-PRODUCT / EARLY-X1 BENCHMARK
#03 = PRIMARY ACTIVE-HFT / EARLY-X1 BENCHMARK
#04 = PRIMARY NON-ISOLATED / CURRENT-DISTRIBUTION BENCHMARK
#05 = KEEP AS ENERGY-ROUTING MECHANISM
#06 = HOLD / very high current-stress risk
#07 = HOLD / high-risk at 12 V
#08 = HOLD / high-risk at extreme LV
#09 = PRIMARY MODERN DIRECT-HFL BENCHMARK
```

Modularization, IPOS, current sharing, active buffer, capacitive isolation, partial power and soft switching remain orthogonal dimensions and do not create a new family by themselves.

---

## 4. A0 product benchmark — ASP-2000 R52

The user-supplied Altium source has progressed from component extraction to SchDoc + compiled-PCB net reconstruction and partial PCB-loss modeling.

### 4.1 Positive-side current distribution

```text
BAT+
├─ F2/F3/F5/F6 → local LV bulk → T1 center tap
└─ F7/F8/F9/F10 → local LV bulk → T2 center tap
```

Both PQ5050 primaries are center tapped:

```text
pin 9 = A
pin 8 = center tap
pin 7 = C
```

The two center taps remain separate supply/current paths.

### 4.2 Primary switched power nodes — RESOLVED

Compiled PCB establishes only two high-current switched primary-end nodes.

A node:

```text
NetC62_1
→ T1 A + T2 A
→ Q3 Q4 Q5 Q6 Q33
→ Q18 Q19 Q20 Q21 Q37
→ 10 connected MOS drains
```

C node:

```text
NetC65_1
→ T1 C + T2 C
→ Q11 Q12 Q13 Q14 Q36
→ Q24 Q25 Q26 Q27 Q38
→ 10 connected MOS drains
```

All twenty main-MOS Source pads connect to:

```text
B
```

Therefore the real low-voltage switch stage is:

```text
A logical switch = 10 parallel MOS
C logical switch = 10 parallel MOS
common source/return = B
```

The earlier `four independent five-MOS power branches` abstraction is superseded.

### 4.3 Q19 anomaly — RESOLVED

Earlier SchDoc-only extraction made Q19 Drain appear isolated.

Compiled PCB proves:

```text
Q19 Drain → NetC62_1
Q19 Source → B
```

Status:

```text
Q19 connectivity = VERIFIED IN PCB
A-side connected MOS count = 10
C-side connected MOS count = 10
Total connected main LV MOS = 20
```

### 4.4 Four physical drivers, two logical commands

Physical gate-driver groups:

```text
DA1-G → Q3 Q4 Q5 Q6 Q33
DA2-G → Q18 Q19 Q20 Q21 Q37
DB1-G → Q11 Q12 Q13 Q14 Q36
DB2-G → Q24 Q25 Q26 Q27 Q38
```

Each main MOS has an individual 27.4 Ω gate resistor.

Upstream command pairing:

```text
DR-A  ─ R213 = 0 Ω ─ DR-A2
DR-B  ─ R212 = 0 Ω ─ DR-B2
```

Therefore:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched power nodes
```

Connectivity-level command pairing is verified; actual propagation / edge mismatch remains a waveform measurement item.

### 4.5 Local E-label correction

SchDoc labels:

```text
DA1-E / DA2-E / DB1-E / DB2-E
```

must not be modeled as four isolated high-current return nets.

Compiled PCB establishes:

```text
all main MOS Sources → B
low-side local driver references → B
```

Thus `B` is the physical common source/return boundary.

### 4.6 Negative full-current return

Battery negative is separated from `B` by seven TO-220 MOS positions:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

All seven are annotated `CSD18510KCS`.

Status:

```text
negative-side full-current series MOS region = VERIFIED
exact protection/disconnect function = OPEN
```

A candidate may not claim a topology efficiency improvement by silently deleting equivalent required product functionality.

---

## 5. Verified X1-to-HV structure

```text
T1 pin 5 = T2 pin 2                     ← direct secondary series junction
T1 outer secondary → D1/D5 rectifier leg
T2 outer secondary → RL1 → D2/D6 rectifier leg
D1,D2 → BUS+
D5,D6 → BUS-
↓
HV DC-link
↓
HV inverter                              ← X3
```

`RL1` exact role remains open.

A0 therefore remains a real-product #02 benchmark:

```text
LV current distribution
→ switched T1/T2 magnetic X1
→ collective/series secondary voltage formation
→ HV rectification
→ HV DC-link
→ X3
→ AC
```

---

## 6. Correct current variables

Do not mix magnetic-path current with local silicon-subgroup current.

```text
I_T1 / I_T2
= actual transformer center-tap / winding-feed currents

I_A,total / I_C,total
= total current through the two electrical switch functions

I_DA1 / I_DA2 / I_DB1 / I_DB2
= local parallel-silicon subgroup currents
```

During stable A conduction:

```text
I_A,total ≈ I_T1,A + I_T2,A
```

During stable C conduction:

```text
I_C,total ≈ I_T1,C + I_T2,C
```

But generally:

```text
I_DA1 != I_T1
I_DA2 != I_T2
I_DB1 != I_T1
I_DB2 != I_T2
```

because DA1/DA2 are two parallel driver/silicon subgroups on the same A drain/source nodes, and DB1/DB2 are two parallel subgroups on the same C nodes.

Subgroup current division depends on hot RDS(on), local copper, gate timing, parasitic inductance and temperature; it must be measured/modelled rather than assumed 50/50.

During dead time / transition edges, Coss, body-diode, leakage, clamp and ringing currents require synchronous high-bandwidth waveform evidence.

---

## 7. Current working architecture — KEEP

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
[X2 active 2ω buffer — optional]
↓
X3
↓
220 Vac
```

Status:

```text
very-short common path  = KEEP / physical requirement
local decoupling        = KEEP / engineering requirement
early fan-out           = KEEP AS HYPOTHESIS
branch switching + X1   = CORE RESEARCH REGION
reduced-current node    = KEEP AS FUNCTIONAL CONCEPT
active X2               = OPTIONAL / NOT PROVEN
X3 after X1             = KEEP / structural requirement
```

`P_saved > P_added` remains mandatory.

---

## 8. Current A0 numerical bounds

### 8.1 PCB copper

PcbDoc stack:

```text
Top copper    ≈ 1.4 mil ≈ 35.56 µm
Bottom copper ≈ 1.4 mil ≈ 35.56 µm
```

Nominal room-temperature sheet resistance:

```text
R_sheet,1layer ≈ 0.485 mΩ/square
```

At 175.4 A:

```text
one full-current single-layer square ≈ 14.9 W
```

### 8.2 BAT+ common geometry

2D nominal-copper model:

```text
R_BAT+,common,geometry ≈ 0.249 mΩ
P @ 175.4 A ≈ 7.67 W
average modeled drop ≈ 43.7 mV
```

### 8.3 Post-fuse PCB geometry

```text
T1 local PCB:
R ≈ 0.351 mΩ
P @ 87.7 A ideal share ≈ 2.70 W

T2 PCB excluding J8:
R ≈ 0.144 mΩ
P @ 87.7 A ideal share ≈ 1.10 W
```

Partial positive PCB-only equivalent under ideal 50/50 T1/T2 sharing:

```text
R_eq,positive-PCB,partial ≈ 0.373 mΩ
P @ 175.4 A ≈ 11.5 W
```

Status:

```text
GEOMETRY MODEL / NOT MEASURED
```

This excludes connector/contact, fuse elements, J8, hot copper and assembly reinforcement.

### 8.4 J8

Two same-net `J8` high-current terminals are separated by about 93 mm with no ordinary PCB polygon spanning the complete gap.

```text
external high-current link intent = STRONGLY SUPPORTED
exact conductor = OPEN
R_J8 = MEASUREMENT_NEEDED
```

### 8.5 Main A/C MOS conduction — corrected 10+10 bound

12 V population:

```text
CSD18542KCS
RDS(on),max @ VGS=10 V = 4 mΩ
```

Each logical switch has ten connected devices:

```text
R_A,eq,25C,max ≈ 0.400 mΩ
R_C,eq,25C,max ≈ 0.400 mΩ
```

Using the same simplified 175.4 A / 50%-per-side sensitivity model:

```text
P_mainMOS,cond,25C-bound ≈ 12.3 W
```

Status:

```text
DATASHEET BOUND / NOT MEASURED
```

### 8.6 Negative seven-MOS region

For `CSD18510KCS`, using the official max-RDS(on) boundary previously locked:

```text
7 ideal parallel devices → R_eq ≈ 0.243 mΩ
175.4 A scaling → ≈ 7.47 W
```

Status:

```text
DATASHEET BOUND / NOT MEASURED
```

These different evidence-class values must not be summed into a claimed measured total.

---

## 9. Current BAT→X1 loss boundary

```text
BAT+
↓
connector + BAT+ common distribution
↓
8 fuse branches
↓
T1 local feed / T2 local feed + J8
↓
T1/T2 primary magnetic path
↓
A or C logical switch region: 10 MOS
↓
B return
↓
7-device BAT- MOS region
↓
BAT-
```

Formal decomposition:

```text
P_A0,BAT→X1 =
    P_positiveDistribution
  + P_fuse/J8
  + P_A/C_MOS,cond
  + P_A/C_MOS,sw
  + P_primary,Cu
  + P_core
  + P_commutation/clamp
  + P_BreturnCopper
  + P_negativeSeriesBank
```

---

## 10. Hardware measurement gates prepared

### 10.1 Static / Kelvin gate

Protocol:

```text
research/15_ASP2000_A0_KELVIN_MEASUREMENT_PROTOCOL.md
```

Priority segments:

```text
M0 BAT+ → fuse inputs
M1 individual fuses
M2 T1 local feed
M3 J8
M4 T2 local feed
M5 B ↔ BAT- seven-MOS region
M6 B return copper if accessible
```

For multi-terminal BAT+ distribution:

```text
P_BAT+ = Σ I_k ΔV_k
```

not `I_source × one arbitrary fuse-input drop`.

### 10.2 Dynamic switch / HFT gate

Protocol:

```text
research/16_ASP2000_A0_DYNAMIC_SWITCHING_AND_HFT_MEASUREMENT_PROTOCOL.md
```

Priority dynamic quantities:

```text
fs / duty / dead time
DA1↔DA2 timing mismatch
DB1↔DB2 timing mismatch
actual VGS on Q3/Q18/Q11/Q24
V_A-B / V_C-B
I_T1 / I_T2
primary volt-second
T1/T2 temperature
```

First system-level switch-region electrical power boundary:

```text
p_A(t) = v_A-B(t) i_A,total(t)
p_C(t) = v_C-B(t) i_C,total(t)
```

Only use waveform integration when voltage/current channels are synchronous, bandwidth-adequate and deskewed.

---

## 11. Benchmark stack

```text
A0 — actual ASP-2000 R52
A1 — fair optimized magnetic HFT
B  — Direct HFL
C  — non-isolated current-distribution / high-gain
D  — working candidate architecture
```

A1 remains blocked until the A0 loss target is localized tightly enough.

A1 must preserve equivalent relevant product functionality and may use:

```text
optimized distribution
heavy silicon paralleling
distributed local gate drivers
optimized magnetic X1
matched protection/disconnect function
collective HV formation
```

A candidate cannot claim advantage merely from features A0/A1 are already allowed to use.

---

## 12. X2 remains a later gate

Do not add active X2 before A0/A1 loss localization.

Required eventual ablation:

```text
Buffer OFF
vs
Buffer ON
```

Go condition:

```text
P_LV,saved > P_X2,added
```

If passive post-X1 energy storage already suppresses source 2ω sufficiently, active X2 must be rejected or restructured.

---

## 13. Current unresolved items

```text
exact switching frequency / duty / dead time
actual DA1-vs-DA2 / DB1-vs-DB2 dynamic mismatch
DA1/DA2 and DB1/DB2 subgroup current sharing
T1/T2 current balance
fuse sharing / hot fuse resistance
J8 physical conductor / resistance
hot main-MOS RDS(on)
B-return copper resistance
primary winding Rac / core loss
exact turns / core material
RL1 role
source 100/120 Hz ripple
HV DC-link ripple
thermal map
A0 measured distribution loss
A0 measured dynamic switch loss
A0 total BAT→X1 loss
A1 total loss
candidate superiority
```

---

## 14. Detailed current documents

```text
07_BENCHMARKS.md
08_DECISION_LOG.md
09_CANDIDATE10_SYNTHESIS_BOUNDARY.md
10_ASP2000_PRODUCT_BASELINE.md
11_WORKING_ARCHITECTURE_LOSS_AUDIT.md
12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
13_ASP2000_A0_NUMERICAL_LOSS_BOUNDS.md
14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
15_ASP2000_A0_KELVIN_MEASUREMENT_PROTOCOL.md
16_ASP2000_A0_DYNAMIC_SWITCHING_AND_HFT_MEASUREMENT_PROTOCOL.md
17_ASP2000_A0_PRIMARY_SWITCH_CURRENT_BOUNDARY.md
```

---

## 15. Current decision state

```text
Research phase:
    Physical Gap Validation

A0 main power/current graph:
    SUBSTANTIALLY RECONSTRUCTED

Q19 anomaly:
    RESOLVED / CONNECTED TO A NODE IN PCB

A logical switch:
    10 MOS / VERIFIED

C logical switch:
    10 MOS / VERIFIED

Four local drivers / two logical commands:
    VERIFIED AT CONNECTIVITY LEVEL

A0 positive PCB geometry model:
    ESTABLISHED AS NON-MEASURED BOUND

A0 negative-side full-current MOS region:
    VERIFIED / DATASHEET LOSS BOUND

A0 measured distribution loss:
    OPEN

A0 measured dynamic switch loss:
    OPEN

A0 total BAT→X1 loss:
    OPEN

A1 matched magnetic model:
    BLOCKED UNTIL A0 LOSS LOCALIZATION

Working architecture:
    KEEP

Early fan-out benefit:
    NOT PROVEN

Active X2 benefit:
    NOT PROVEN

Candidate #10:
    NOT ASSIGNED

Novelty:
    NOT ESTABLISHED

Next executable file-only action:
    trace Q39…Q65 control/function to determine the role of the full-current B↔BAT- MOS region.

Next hardware action:
    execute Kelvin + D0 timing measurements, then close A0 BAT→X1 Loss Budget v1.
```

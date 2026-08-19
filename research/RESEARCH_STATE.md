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

Necessary average source current cannot disappear before the first major impedance/current-domain transformation. The research variable is which additional RMS components and how much resistive path also remain in that expensive low-voltage domain.

---

## 2. Structural coordinates

```text
X1 = first major impedance / current-domain transformation region
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC-synthesis region
```

These are functional coordinates, not one component each and not automatically three converter stages.

Current preferred ordering:

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

The user-supplied Altium source has progressed from component extraction to substantial net-level and PCB-primitive reconstruction.

### 4.1 Verified low-voltage main path

```text
BAT+
├─ F2/F3/F5/F6 → local LV bulk → T1 center tap B
└─ F7/F8/F9/F10 → local LV bulk → T2 center tap B
```

Both PQ5050 primaries expose:

```text
A — B(center tap) — C
```

Direct reconstruction establishes:

```text
T1 A = T2 A → shared A-side paralleled MOS switching node
T1 C = T2 C → shared C-side paralleled MOS switching node
```

Therefore the earlier four-independent-five-MOS-bank abstraction is superseded.

MOS status:

```text
20 low-side MOS positions annotated
19 expected power connections directly reconstructed
Q19 drain appears isolated in SchDoc
Q19 footprint exists in PcbDoc
Q19 drain connectivity = OPEN
```

### 4.2 Verified X1-to-HV path

```text
T1 pin5 = T2 pin2                       ← direct secondary series junction
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

A0 abstraction:

```text
BAT+
→ two separately fused/local-bulk center-tap HFT feeds
→ shared heavily paralleled A/C switching nodes
→ T1/T2 magnetic X1
→ collective/series secondary voltage formation
→ HV bridge rectification
→ HV DC-link
→ X3
→ AC
```

Status:

```text
A0 main power graph = SUBSTANTIALLY RECONSTRUCTED
```

---

## 5. Newly verified full-current return path

Battery negative is not the same electrical net as the main low-side switching return `B`.

Seven TO-220 devices bridge the two:

```text
Q39 Q40 Q41 Q42 Q63 Q64 Q65
= CSD18510KCS
```

Verified boundary:

```text
main low-side return B
↓
7-device parallel MOS bank
↓
BAT−
```

Status:

```text
negative-side full-current series MOS region = VERIFIED
exact protection/disconnect/control function = OPEN
```

Using the official device maximum `RDS(on)` only as a 25°C datasheet boundary:

```text
7 ideal parallel devices → R_eq ≈ 0.243 mΩ
175.4 A scaling → conduction bound ≈ 7.47 W
```

This is `DATASHEET_BOUND / NOT MEASURED` and excludes hot RDS(on), current sharing, contacts and return copper.

Critical fair-comparison rule:

> A candidate may not claim a topology improvement by deleting a required protection/disconnect function that A0 contains. Equivalent functionality must be matched or removed from both comparison boundaries.

---

## 6. Current working architecture — KEEP

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
active X2               = OPTIONAL / NOT YET PROVEN
X3 after X1             = KEEP / structural requirement
```

`P_saved > P_added` remains mandatory.

---

## 7. A0 numerical loss localization — current bounds

### 7.1 PCB stack

PcbDoc stack extraction:

```text
Top copper    ≈ 1.4 mil ≈ 35.56 um
Bottom copper ≈ 1.4 mil ≈ 35.56 um
```

Nominal room-temperature sheet resistance:

```text
R_sheet,1layer ≈ 0.485 mΩ/square
```

At `175.4 A`, one full-current single-layer square is approximately:

```text
14.9 W/square
```

This is only a scaling relation, not the actual route resistance.

### 7.2 BAT+ common multi-terminal geometry model

Direct PCB primitive reconstruction identifies:

```text
3 large BAT+ connector power pads
8 main fuse-input pads
16 BAT+ stitching vias
major Top/Bottom BAT+ polygons
```

A converged 2D equal-eight-fuse-current sheet model gives:

```text
R_BAT+,common,geometry ≈ 0.249 mΩ
P @ 175.4 A ≈ 7.67 W
average modeled drop ≈ 43.7 mV
```

Status:

```text
GEOMETRY_MODEL / NOT MEASURED
```

The model also predicts different average copper drops toward the T1 and T2 fuse groups, so equal T1/T2 current sharing must be measured rather than assumed.

### 7.3 Post-fuse PCB models

T1 local PCB:

```text
R_T1local,PCB ≈ 0.351 mΩ
P @ 87.7 A ideal share ≈ 2.70 W
```

T2 PCB portions excluding the external link:

```text
R_T2local,PCB,excludingJ8 ≈ 0.144 mΩ
P @ 87.7 A ideal share ≈ 1.10 W
```

T2 contains two large same-net `J8` terminals about 93 mm apart with no ordinary reconstructed PCB polygon bridging the full gap.

Status:

```text
external high-current link intent = STRONGLY SUPPORTED
exact J8 conductor implementation = OPEN
R_J8 = MEASUREMENT_NEEDED
```

### 7.4 Partial positive-path bound

Under ideal 50/50 T1/T2 sharing:

```text
R_eq,positive-PCB,partial ≈ 0.373 mΩ
P @ 175.4 A ≈ 11.5 W
```

This excludes:

```text
connector/contact loss
8 fuse elements
J8 external link/contact
hot-copper increase
assembly reinforcement details
```

Therefore it is a geometry-only partial bound, not the positive-path measured loss.

---

## 8. Main low-side MOS bound remains separate

12 V population:

```text
CSD18542KCS
RDS(on),max @ VGS=10 V = 4 mΩ
Qg,typ = 44 nC
```

Current reconstructed A/C switching nodes:

```text
A-side = 9 directly connected expected positions
C-side = 10 directly connected positions
Q19 connectivity = OPEN
```

Simplified push-pull-like 9+10-device 25°C conduction boundary at `175.4 A`:

```text
P_mainMOS,cond ≈ 13 W
```

Status:

```text
DATASHEET_BOUND / NOT MEASURED
```

The result does not establish the dominant A0 loss because hot RDS(on), primary waveform, MOS switching/commutation, PCB and protection-path losses remain separate.

---

## 9. Current A0 BAT→X1 loss boundary

The boundary must now include both positive and negative full-current paths:

```text
BAT+
↓
connector + BAT+ common distribution
↓
8 fuse branches
↓
T1 local path / T2 local path + J8
↓
T1/T2 primary + A/C main switching MOS
↓
B return
↓
7-device negative-side series MOS bank
↓
BAT−
```

Formal decomposition:

```text
P_A0,BAT→X1 =
    P_positiveDistribution
  + P_mainMOS,cond
  + P_mainMOS,sw
  + P_primary,Cu
  + P_core
  + P_commutation/clamp
  + P_negativeSeriesBank
  + P_returnCopper
```

The present bounds are intentionally not summed into a claimed A0 total because they are different evidence classes and still omit measured/hot/assembly terms.

---

## 10. Immediate measurement gate — segmented Kelvin / millivolt drop

Geometry modeling has reached the point of diminishing return for unknown contacts, fuse elements, J8 and the return path.

Next gate:

```text
M0 BAT+ terminal → each fuse input
M1 each fuse input → output
M2 T1 fuse-output node → T1 center tap
M3 J8 left → J8 right
M4 J8 right → T2 center tap
M5 BAT− ↔ B across Q39...Q65 bank
M6 B return distribution, if separately accessible
```

Minimum current channels:

```text
I_source
I_T1
I_T2
```

Preferred reconstruction:

```text
P_segment = I_segment × ΔV_segment
R_segment = ΔV_segment / I_segment
```

Relevant component/connection temperatures must be recorded with the millivolt-drop data.

Detailed plan:

```text
research/14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
```

---

## 11. Benchmark stack

```text
A0 — actual ASP-2000 R52
A1 — fair optimized magnetic HFT
B  — Direct HFL
C  — non-isolated current-distribution / high-gain
D  — working candidate architecture
```

A1 is temporarily blocked until the A0 distribution-loss boundary is measured or bounded tightly enough that the optimization target is known.

A1 must preserve matched product functionality; it cannot win by deleting A0 protection/disconnect/current-distribution functions.

---

## 12. X2 remains later gate

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

If the passive A0/A1 HV DC-link already suppresses source 2ω sufficiently, active X2 is rejected or restructured.

---

## 13. Current unresolved items

```text
Q19 intended/assembled drain connection
exact T1/T2 turns ratio
exact switching timing/frequency
T1/T2 current balance
fuse sharing / hot fuse resistance
J8 physical conductor / resistance
MOS current sharing / hot RDS(on)
BAT− / B return-copper resistance
primary winding Rac/core loss
RL1 role
HV capacitor footprint/assembly semantics
source 100/120 Hz ripple
thermal map
A0 measured distribution loss
A0 total BAT→X1 loss
A1 total loss
candidate superiority
```

---

## 14. Detailed research documents

```text
01_SCOPE.md
02_TOPOLOGY_TAXONOMY.md
03_LOSS_PHYSICS.md
04_PRIOR_ART_CLOSURE.md
05_RESEARCH_HYPOTHESIS.md
06_VALIDATION_PLAN.md
07_BENCHMARKS.md
08_DECISION_LOG.md
09_CANDIDATE10_SYNTHESIS_BOUNDARY.md
10_ASP2000_PRODUCT_BASELINE.md
11_WORKING_ARCHITECTURE_LOSS_AUDIT.md
12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
13_ASP2000_A0_NUMERICAL_LOSS_BOUNDS.md
14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
```

---

## 15. Current decision state

```text
Research phase:
    Physical Gap Validation

A0 main power graph:
    SUBSTANTIALLY RECONSTRUCTED

A0 positive PCB geometry model:
    ESTABLISHED AS NON-MEASURED BOUND

A0 negative-side full-current MOS region:
    VERIFIED / DATASHEET LOSS BOUND

A0 measured distribution loss:
    OPEN

A0 total BAT→X1 loss:
    OPEN

A1 matched magnetic model:
    BLOCKED UNTIL A0 DISTRIBUTION BOUNDS / MEASUREMENT

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

Next action:
    segmented Kelvin / millivolt-drop measurement of A0 distribution path,
    then close the first measured BAT→X1 loss budget before A1 synthesis
```

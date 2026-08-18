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

> 不是研究怎麼升壓，而是研究低壓百安培能量怎麼走，才最少變成熱。

---

## 2. Structural coordinates

```text
X1 = first major impedance / current-domain transformation region
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC-synthesis region
```

They are functional coordinates, not one component each and not automatically three converter stages.

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

## 4. A0 product reality check — ASP-2000 R52

The user-supplied Altium source has now progressed from component extraction to substantial **net-level power-path reconstruction**.

### VERIFIED low-voltage structure

```text
BAT+
├─ F2/F3/F5/F6 → local LV bulk → T1 center tap B
└─ F7/F8/F9/F10 → local LV bulk → T2 center tap B
```

Both PQ5050 primaries expose:

```text
A — B(center tap) — C
```

and direct reconstruction establishes:

```text
T1 A = T2 A → shared A-side paralleled MOS switching node
T1 C = T2 C → shared C-side paralleled MOS switching node
```

This corrects the earlier simplified picture of four electrically independent five-MOS branches.

MOS status:

```text
20 low-side MOS positions annotated
19 expected power connections directly reconstructed
Q19 drain appears isolated in the SchDoc graph
→ SCHEMATIC_ANOMALY / VERIFY PCB-BOM-ASSEMBLY
```

### VERIFIED X1-to-HV structure

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

`RL1` exact operating role remains open.

Therefore A0 is now represented as:

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
A0 numerical loss budget = OPEN
```

Detailed evidence:

```text
research/10_ASP2000_PRODUCT_BASELINE.md
research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
```

---

## 5. Critical consequence for candidate comparison

A0 already uses:

```text
parallel MOS silicon
multiple magnetic paths
separate fused transformer feeds
local LV bulk
shared primary switching nodes
collective/series secondary voltage formation
HV DC-link before X3
```

Therefore a candidate cannot claim advantage merely from:

```text
N-way current distribution
parallel MOS
multiple transformers
voltage combining
early X1
```

A matched A1 magnetic benchmark must be allowed equivalent current-distribution/layout optimization.

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

## 7. First A0 loss-localization gate

Current formal boundary:

```text
BAT+ → common interconnect
→ two 4-fuse banks
→ local LV nodes / bulk
→ T1/T2 primary halves
→ active A/C MOS switching node
→ common LV return
```

Loss equation:

```text
P_A0,BAT→X1 =
    P_common
  + P_fuse
  + P_local_interconnect
  + P_bulk_ESR
  + P_MOS,cond
  + P_MOS,sw
  + P_primary,Cu
  + P_core
  + P_commutation/clamp
```

Required quantities:

```text
I_source,avg/RMS/2ω/HF
T1 center-feed current
T2 center-feed current
fuse current/voltage drop
R_common / local PCB R
A/C switching-node current
MOS VGS/VDS/current/Tj
T1/T2 primary current
fs / duty / dead time
winding Rdc/Rac / temperature
core/flux data
```

PCB resistance is still `OPEN` and should be measured and/or extracted with Q3D rather than guessed from schematic geometry.

---

## 8. Datasheet-bound reference for A0 MOS modeling

12 V schematic population:

```text
CSD18542KCS
RDS(on),max @ VGS=10 V = 4 mΩ
Qg,typ = 44 nC
```

24 V population:

```text
CSD19533KCS
RDS(on),max @ VGS=10 V = 10.5 mΩ
Qg,typ = 27 nC
```

For a purely illustrative 12 V ten-device parallel active node:

```text
R_eq,silicon,25C,max ≈ 0.40 mΩ
```

At the 175.4 A scaling current:

```text
I²R ≈ 12.3 W active-state silicon-only reference
```

This is **not actual product loss**; temperature, duty, waveform, mismatch, package/PCB resistance and switching loss are excluded.

---

## 9. Benchmark stack

```text
A0 — actual ASP-2000 R52
A1 — fair optimized magnetic HFT
B  — Direct HFL
C  — non-isolated current-distribution / high-gain
D  — working candidate architecture
```

A1 must first test whether A0 loss is removable by ordinary magnetic/current-distribution optimization.

Only loss mechanisms that survive A1 justify replacing X1 with a different physical mechanism.

---

## 10. X2 remains later gate

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

If passive A0/A1 HV DC-link already suppresses source 2ω sufficiently, active X2 is rejected or restructured.

---

## 11. Current unresolved items

```text
Q19 intended/assembled drain connection
exact T1/T2 turns ratio
exact switching timing/frequency
T1/T2 current balance
fuse sharing
MOS current sharing
PCB copper Rdc/Rac
primary winding Rac/core loss
RL1 role
HV capacitor footprint/assembly semantics
source 100/120 Hz ripple
thermal map
A0 total loss
A1 total loss
candidate superiority
```

Novelty remains:

```text
NOT_ESTABLISHED
```

Candidate #10 remains:

```text
NOT_ASSIGNED
```

---

## 12. Current next action

```text
A0 numerical loss localization
↓
A1 matched optimized HFT model
↓
compare X1 mechanisms
↓
X2 Buffer OFF/ON
↓
only then detailed candidate topology synthesis
```

Immediate goal:

> Identify the largest credible `BAT→X1` A0 loss buckets and determine which remain after a fair A1 optimization.

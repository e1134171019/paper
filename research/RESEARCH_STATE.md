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
#01 = REFERENCE ONLY / poor fit
#02 = PRIMARY REAL-PRODUCT / EARLY-X1 BENCHMARK
#03 = PRIMARY ACTIVE-HFT / EARLY-X1 BENCHMARK
#04 = PRIMARY NON-ISOLATED / CURRENT-DISTRIBUTION BENCHMARK
#05 = KEEP AS ENERGY-ROUTING MECHANISM
#06 = HOLD / very high current-stress risk
#07 = HOLD / high-risk at 12 V
#08 = HOLD / high-risk at extreme LV
#09 = PRIMARY MODERN DIRECT-HFL BENCHMARK
```

Modularization, IPOS, current sharing, capacitive isolation, active buffer, partial power and soft switching are orthogonal dimensions; they do not create a new family by themselves.

Candidate #10 remains:

```text
NOT_ASSIGNED
```

---

## 4. Current working architecture — KEEP

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
very-short common path = KEEP / physical requirement
local decoupling = KEEP
early fan-out = HYPOTHESIS, not automatic loss reduction
branch switching + X1 = CORE RESEARCH REGION
active X2 = OPTIONAL / NOT PROVEN
X3 after X1 = KEEP
```

Mandatory rule:

```text
P_saved > P_added
```

---

## 5. A0 real-product benchmark — ASP-2000 R52

### 5.1 Positive-side current distribution

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

The two center-tap supply paths remain separate.

### 5.2 Primary switch architecture — RESOLVED

Compiled PCB establishes two high-current switched primary-end nodes:

```text
A node = NetC62_1
→ T1 A + T2 A
→ Q3 Q4 Q5 Q6 Q33
→ Q18 Q19 Q20 Q21 Q37
→ 10 MOS drains

C node = NetC65_1
→ T1 C + T2 C
→ Q11 Q12 Q13 Q14 Q36
→ Q24 Q25 Q26 Q27 Q38
→ 10 MOS drains

all 20 main MOS Sources → B
```

Thus:

```text
A logical switch = 10 parallel MOS
C logical switch = 10 parallel MOS
common source/return = B
```

Q19 is verified connected in PCB; the old 9+10 model is superseded.

### 5.3 Four physical drivers, two logical commands

```text
DA1-G → 5 A-side MOS
DA2-G → 5 A-side MOS
DB1-G → 5 C-side MOS
DB2-G → 5 C-side MOS
```

Each main MOS has an individual 27.4 Ω gate resistor.

Control pairing:

```text
DR-A  ─ R213=0Ω ─ DR-A2
DR-B  ─ R212=0Ω ─ DR-B2
```

Therefore:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched nodes
```

Dynamic timing mismatch remains a measurement item.

### 5.4 Correct current variables

```text
I_T1 / I_T2
= transformer center-feed / winding currents

I_A,total / I_C,total
= total current through the two electrical switch functions

I_DA1 / I_DA2 / I_DB1 / I_DB2
= local silicon-subgroup currents
```

Stable conduction approximation:

```text
I_A,total ≈ I_T1,A + I_T2,A
I_C,total ≈ I_T1,C + I_T2,C
```

Do not equate DA1/DA2 with T1/T2 currents.

---

## 6. Battery-negative protection/sensing interface — FUNCTION NARROWED

Seven `CSD18510KCS` devices connect:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

Verified orientation:

```text
Source → B
Drain  → BAT-
```

Verified gate network for all seven:

```text
12VP → individual 68.1 Ω → Gate
Gate → individual 47.5 kΩ → B
```

No independent MAIN-board PWM/enable command was found for the bank.

Function status:

```text
low-side reverse-polarity / ideal-diode-style battery interface
= STRONGLY_SUPPORTED

commandable full battery disconnect by this bank alone
= NOT_SUPPORTED_BY_PRESENT_CIRCUIT
```

U4 (`LM2904`) monitors the same B↔BAT- boundary:

```text
U4 + input → B
BAT- → R153=1kΩ → U4 - input
R152=22.1kΩ feedback
U4 output → R154=100Ω → BOCP → CN4A pin 6
```

Therefore:

```text
B↔BAT- voltage-drop sensing → BOCP = VERIFIED
BOCP over-current / abnormal-drop protection role = STRONGLY_SUPPORTED
exact BOCP threshold / polarity / control-board response = OPEN
```

The seven-MOS loss is classified primarily as:

```text
battery-interface protection/sensing overhead
```

not intrinsic magnetic-X1 conversion loss.

Detailed evidence:

```text
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
```

---

## 7. Verified X1-to-HV structure

```text
T1 pin5 = T2 pin2                    ← direct secondary series junction
T1 outer secondary → D1/D5
T2 outer secondary → RL1 → D2/D6
D1,D2 → BUS+
D5,D6 → BUS-
↓
HV DC-link                           ← passive X2-capable node
↓
HV inverter                          ← X3
↓
AC
```

`RL1` exact role remains open.

A0 remains family `#02`.

---

## 8. A0 current numerical bounds — NOT MEASURED

### PCB stack

```text
Top copper ≈ 1.4 mil ≈ 35.56 µm
Bottom copper ≈ 1.4 mil ≈ 35.56 µm
R_sheet,1layer ≈ 0.485 mΩ/square
```

At 175.4 A:

```text
one full-current single-layer square ≈ 14.9 W
```

### BAT+ geometry

```text
R_BAT+,common,geometry ≈ 0.249 mΩ
P@175.4 A ≈ 7.67 W
average modeled drop ≈ 43.7 mV
```

### Post-fuse PCB

```text
T1 local PCB:
R≈0.351 mΩ
P@87.7 A ideal share≈2.70 W

T2 PCB excluding J8:
R≈0.144 mΩ
P@87.7 A ideal share≈1.10 W
```

Partial positive PCB-only equivalent:

```text
R_eq≈0.373 mΩ
P@175.4 A≈11.5 W
```

All are `GEOMETRY_MODEL / NOT_MEASURED` and exclude contacts, fuses, J8, hot copper and assembly reinforcement.

### Main A/C MOS

12 V CSD18542KCS, max `RDS(on)=4mΩ @ VGS=10V`.

Ten devices per logical switch:

```text
R_A,eq≈R_C,eq≈0.400mΩ
P_mainMOS,cond,25C-bound≈12.3W
```

`DATASHEET_BOUND / NOT_MEASURED`.

### Battery interface

CSD18510KCS max `RDS(on)=1.7mΩ @ VGS=10V`.

```text
7 ideal parallel → Req≈0.243mΩ
P@175.4A≈7.47W
```

`DATASHEET_BOUND / NOT_MEASURED`.

---

## 9. Product-level BAT→X1 loss decomposition

```text
P_A0,BAT→X1/product =
    P_positiveDistribution
  + P_fuse/J8
  + P_A/C_MOS,cond
  + P_A/C_MOS,sw
  + P_primary,Cu
  + P_core
  + P_commutation/clamp
  + P_BreturnCopper
  + P_batteryInterfaceProtection/Sensing
```

Two fair-comparison contracts:

```text
Contract P — product level
→ match required reverse-polarity/equivalent ideal-diode behavior and required fault/current information; count loss.

Contract C — core converter
→ exclude battery-interface overhead from A0/A1/candidate equally.
```

Forbidden:

```text
candidate deletes Q39...Q65 function
→ calls the removed watts an X1/topology improvement
```

---

## 10. Hardware measurement gates prepared

### Static / Kelvin

```text
M0 BAT+ → fuse inputs
M1 individual fuses
M2 T1 local feed
M3 J8
M4 T2 local feed
M5 B ↔ BAT- battery-interface bank
M6 B return copper
```

For multi-terminal BAT+:

```text
P_BAT+ = Σ I_k ΔV_k
```

For M5 record:

```text
I_source
ΔV(B↔BAT-)
12VP
MOS temperature
BOCP voltage/state if safe
```

### Dynamic switch / HFT

```text
fs / duty / dead time
DA1↔DA2 timing mismatch
DB1↔DB2 timing mismatch
actual VGS on representative MOS
V_A-B / V_C-B
I_T1 / I_T2
switch-region synchronous v×i
primary volt-second
T1/T2 temperature
```

First-order stable-conduction switch power boundary:

```text
p_A(t)=v_A-B(t)i_A,total(t)
p_C(t)=v_C-B(t)i_C,total(t)
```

Switching transitions require synchronous, bandwidth-adequate, deskewed measurements.

---

## 11. Benchmark stack

```text
A0 — actual ASP-2000 R52
A1 — fair optimized magnetic HFT
B  — Direct HFL
C  — non-isolated current-distribution/high-gain
D  — working candidate architecture
```

A1 is allowed:

```text
optimized distribution
heavy silicon paralleling
distributed local gate drivers
optimized magnetic X1
matched battery-interface protection/sensing function under Contract P
collective HV formation
```

A1 remains numerically blocked until A0 loss localization is measured or bounded tightly enough to identify the true target.

---

## 12. X2 remains later gate

Do not add active X2 before A0/A1 loss localization.

```text
Buffer OFF vs Buffer ON
Go iff P_LV,saved > P_X2,added
```

If passive post-X1 storage already suppresses source 2ω sufficiently, active X2 must be rejected/restructured.

---

## 13. Current unresolved items

```text
exact fs / duty / dead time
actual DA1-vs-DA2 / DB1-vs-DB2 timing mismatch
silicon subgroup current sharing
T1/T2 current balance
fuse sharing / hot fuse resistance
J8 physical conductor / resistance
hot main-MOS RDS(on)
B-return copper loss
T1/T2 winding Rac / core loss
leakage/clamp processed power
RL1 exact role
source 100/120 Hz ripple
HV DC-link ripple
exact BOCP threshold / active polarity / control-board response
12VP startup/shutdown sequence
A0 measured distribution loss
A0 dynamic switch/HFT loss
A0 total BAT→X1 loss
A1 total loss
candidate superiority
```

---

## 14. Detailed evidence records

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
18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
```

---

## 15. Current decision state

```text
Research phase                       = Physical Gap Validation
A0 main power/current graph          = SUBSTANTIALLY_RECONSTRUCTED
A logical switch                     = 10 MOS / VERIFIED
C logical switch                     = 10 MOS / VERIFIED
4 drivers / 2 logical commands       = VERIFIED_AT_CONNECTIVITY_LEVEL
positive PCB geometry loss bound     = ESTABLISHED / NOT_MEASURED
B↔BAT- seven-MOS power boundary      = VERIFIED
12VP common gate bias                = VERIFIED
reverse-polarity / ideal-diode role  = STRONGLY_SUPPORTED
B↔BAT- sensing → BOCP                = VERIFIED
BOCP exact control response          = OPEN
battery-interface measured loss      = OPEN
A0 measured distribution loss        = OPEN
A0 dynamic switch/HFT loss           = OPEN
A0 total BAT→X1 loss                 = OPEN
A1 matched model                     = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
Working architecture                 = KEEP
Early fan-out benefit                = NOT_PROVEN
Active X2 benefit                    = NOT_PROVEN
Candidate #10                        = NOT_ASSIGNED
Novelty                              = NOT_ESTABLISHED
```

Immediate next gate:

```text
A0 hardware data (M0–M6 + D0–D7)
↓
separate battery-interface overhead from intrinsic X1 loss
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized HFT
```
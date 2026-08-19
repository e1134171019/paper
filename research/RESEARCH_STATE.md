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

Necessary average source current cannot disappear before the first major impedance/current-domain transformation. The research variable is how much extra RMS current and resistive/commutation exposure remain in the expensive low-voltage domain.

---

## 2. Structural coordinates

```text
X1 = first major impedance / current-domain transformation region
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC-synthesis region
```

These are functional coordinates, not single components.

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

Mandatory rule:

```text
P_saved > P_added
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

Modularization, IPOS, current sharing, capacitive isolation, active buffer, partial power and soft switching are orthogonal dimensions and do not create a new family by themselves.

```text
Candidate #10 = NOT_ASSIGNED
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
early fan-out = HYPOTHESIS / not automatic loss reduction
branch switching + X1 = CORE RESEARCH REGION
active X2 = OPTIONAL / NOT_PROVEN
X3 after X1 = KEEP
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

Therefore:

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

Thus:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched nodes
```

Actual propagation/timing mismatch remains a waveform measurement item.

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

Do not equate DA1/DA2 subgroup current with T1/T2 current.

---

## 6. Battery-negative protection/sensing interface — FUNCTION NARROWED

Seven `CSD18510KCS` devices form one parallel full-current battery-return bank:

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

No independent MAIN-board PWM/enable command was found for this bank.

Function status:

```text
low-side reverse-polarity / ideal-diode-style battery interface
= STRONGLY_SUPPORTED

commandable full battery disconnect by this bank alone
= NOT_SUPPORTED_BY_PRESENT_CIRCUIT
```

This loss is classified primarily as:

```text
battery-interface protection/sensing overhead
```

not intrinsic magnetic-X1 loss.

---

## 7. BOCP analog sensing path — TRANSFER RELATION RESOLVED

Direct SchDoc wiring establishes that local `B` and `SIG` are the same analog reference in the U4 region.

U4 (`LM2904`) BOCP channel:

```text
U4 + input → B / SIG
BAT- → R153 = 1.00 kΩ → U4 - input
U4 output → R152 = 22.1 kΩ → U4 - input
U4 output → R154 = 100 Ω → BOCP → CN4A pin 6
U4 rails → 12VP / -12V
```

Define:

```text
ΔV_M5 = V_B - V_BAT-
```

Ideal closed-loop relation:

```text
V_U4out - V_B
= (R152/R153) ΔV_M5
≈ 22.1 × ΔV_M5
```

For a high-impedance BOCP receiver:

```text
V_BOCP - V_B ≈ 22.1 × ΔV_M5
```

The 1% resistor ratio gives an approximate nominal tolerance range:

```text
G_BOCP ≈ 21.66 … 22.55 V/V
```

before op-amp offset, temperature, loading and board effects.

At the existing `175.4 A` / seven-MOS 25°C datasheet scale reference:

```text
R_bank ≈ 0.243 mΩ
ΔV_M5 ≈ 42.6 mV
P_M5 ≈ 7.47 W
nominal BOCP above B ≈ 0.94 V
```

Status:

```text
BOCP analog transfer relation = VERIFIED_FROM_MAIN_BOARD
0.94 V = SCALE_REFERENCE / NOT_MEASURED / NOT_TRIP_THRESHOLD
BOCP measured gain/offset = OPEN
BOCP exact trip/control response = OPEN
```

BOCP is not a precision current measurement. LM2904-family input offset is mV-class and the seven-MOS sense resistance is strongly dependent on temperature, VGS, current sharing, package/PCB/contact resistance. The formal loss evidence remains direct M5 Kelvin drop plus source current.

Detailed evidence:

```text
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
research/19_ASP2000_A0_BOCP_TRANSFER_AND_M5_DIAGNOSTIC_GATE.md
```

---

## 8. Verified X1-to-HV structure

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

## 9. A0 numerical bounds — NOT MEASURED

### PCB / distribution

```text
Top copper ≈ 1.4 mil ≈ 35.56 µm
Bottom copper ≈ 1.4 mil ≈ 35.56 µm
R_sheet,1layer ≈ 0.485 mΩ/square

R_BAT+,common,geometry ≈ 0.249 mΩ
P@175.4 A ≈ 7.67 W

T1 local PCB:
R≈0.351 mΩ
P@87.7 A ideal share≈2.70 W

T2 PCB excluding J8:
R≈0.144 mΩ
P@87.7 A ideal share≈1.10 W

partial positive PCB-only:
R_eq≈0.373 mΩ
P@175.4 A≈11.5 W
```

All are `GEOMETRY_MODEL / NOT_MEASURED`.

### Main A/C MOS

12 V population `CSD18542KCS`, max `RDS(on)=4mΩ @ VGS=10V`.

```text
10 MOS per logical switch
R_A,eq≈R_C,eq≈0.400mΩ
P_mainMOS,cond,25C-bound≈12.3W
```

`DATASHEET_BOUND / NOT_MEASURED`.

### Battery interface

`CSD18510KCS`, max `RDS(on)=1.7mΩ @ VGS=10V`.

```text
7 ideal parallel → Req≈0.243mΩ
P@175.4A≈7.47W
```

`DATASHEET_BOUND / NOT_MEASURED`.

Do not sum mixed evidence classes into a claimed product loss.

---

## 10. Product-level BAT→X1 loss decomposition

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
→ match required reverse-polarity/equivalent ideal-diode behavior and fault/current information; count loss.

Contract C — core converter
→ exclude battery-interface overhead from A0/A1/candidate equally.
```

Forbidden:

```text
candidate deletes Q39...Q65 function
→ calls removed watts an X1/topology improvement
```

---

## 11. Hardware measurement gates prepared

### Static / Kelvin M0–M6

```text
M0 BAT+ → fuse inputs
M1 individual fuse banks
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

#### M5 upgraded diagnostic

At each controlled load point record:

```text
I_source
ΔV_M5 = V_B - V_BAT-
V_BOCP relative B/SIG
12VP
MOS-bank temperature
```

Then calculate:

```text
R_M5,eff = ΔV_M5 / I_source
P_M5     = I_source × ΔV_M5

G_BOCP,meas
= (V_BOCP - V_B) / ΔV_M5
```

Use load-sweep regression:

```text
ΔV_M5 vs I_source
→ hot effective R_M5

V_BOCP vs ΔV_M5
→ measured BOCP gain and intercept
```

Formal hierarchy:

```text
M5 Kelvin + I_source + temperature
= benchmark-grade loss evidence

BOCP
= product sense-chain cross-check
```

### Dynamic switch / HFT D0–D7

```text
fs / duty / dead time
DA1↔DA2 timing mismatch
DB1↔DB2 timing mismatch
actual VGS
V_A-B / V_C-B
I_T1 / I_T2
synchronous switch-region v×i
primary volt-second
T1/T2 temperature
```

Stable-conduction first-order boundary:

```text
p_A(t)=v_A-B(t)i_A,total(t)
p_C(t)=v_C-B(t)i_C,total(t)
```

Transitions require synchronous, bandwidth-adequate, deskewed measurements.

---

## 12. Benchmark stack

```text
A0 — actual ASP-2000 R52
A1 — fair optimized magnetic HFT
B  — Direct HFL
C  — non-isolated current-distribution/high-gain
D  — working candidate architecture
```

A1 is allowed equivalent:

```text
optimized distribution
heavy silicon paralleling
distributed local gate drivers
optimized magnetic X1
matched battery-interface protection/sensing function under Contract P
collective HV formation
```

A1 remains numerically blocked until A0 loss localization identifies the true target.

---

## 13. X2 remains later gate

Do not add active X2 before A0/A1 loss localization.

```text
Buffer OFF vs Buffer ON
Go iff P_LV,saved > P_X2,added
```

If passive post-X1 storage already suppresses source 2ω sufficiently, active X2 must be rejected or restructured.

---

## 14. Current unresolved items

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
BOCP measured gain/intercept
exact BOCP trip threshold / active polarity / control-board response
12VP startup/shutdown sequence
A0 measured distribution loss
A0 dynamic switch/HFT loss
A0 total BAT→X1 loss
A1 total loss
candidate superiority
```

---

## 15. Detailed evidence records

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
19_ASP2000_A0_BOCP_TRANSFER_AND_M5_DIAGNOSTIC_GATE.md
```

---

## 16. Current decision state

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
B / SIG analog reference relation    = VERIFIED
BOCP nominal analog gain             = ~22.1 V/V / VERIFIED_FROM_MAIN_BOARD
BOCP measured gain/intercept          = OPEN
BOCP exact trip/control response      = OPEN
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
M5 controlled load sweep first
→ I_source + ΔV_M5 + BOCP + temperature
→ close actual battery-interface R/P and verify sense-chain gain

then complete M0–M6 + D0–D7
↓
separate product-interface overhead from intrinsic X1 loss
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized HFT
```
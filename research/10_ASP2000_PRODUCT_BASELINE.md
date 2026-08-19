# 10 — ASP-2000 R52 Product Baseline

Status date: 2026-08-19  
Role: `A0 REAL-PRODUCT BENCHMARK`  
Evidence status: `SCHDOC + COMPILED-PCB NET RECONSTRUCTION / PARTIAL LOSS BOUNDS`  
Novelty relevance: `NONE — benchmark evidence only`

## 1. Purpose

This document records the real-product baseline derived from the user-supplied ASP-2000 MAIN R52 Altium source artifacts:

```text
PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc
PB-2200-0038-D_ASP-2000-MAIN-R52.PcbDoc
```

The raw company/product files are **not committed to this public repository**.

A0 exists to prevent unfair comparison against a fictional or under-optimized magnetic baseline.

Detailed records:

```text
research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
research/14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
research/16_ASP2000_A0_DYNAMIC_SWITCHING_AND_HFT_MEASUREMENT_PROTOCOL.md
research/17_ASP2000_A0_PRIMARY_SWITCH_CURRENT_BOUNDARY.md
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
research/19_ASP2000_A0_BOCP_TRANSFER_AND_M5_DIAGNOSTIC_GATE.md
research/20_ASP2000_A0_RL1_HV_PRECHARGE_BYPASS.md
```

---

## 2. Verified low-voltage power structure

### 2.1 Two PQ5050 HFT modules

```text
T1 = PQ5050
T2 = PQ5050
```

Both primary structures are center-tapped:

```text
pin 9 = A
pin 8 = center tap
pin 7 = C
```

### 2.2 BAT+ splits into two fused center-tap feeds

```text
BAT+
├─ F2/F3/F5/F6 → T1 center tap + local LV bulk
└─ F7/F8/F9/F10 → T2 center tap + local LV bulk
```

Fuse annotation:

```text
40 A / 32 V @12 V
20 A / 32 V @24 V
```

Local bulk groups include C2…C6 and C28…C32 with 12 V / 24 V capacitor alternatives.

### 2.3 Two shared primary switched nodes

Compiled PCB connectivity establishes:

```text
A switched node = NetC62_1
C switched node = NetC65_1
common source/return = B
```

A side:

```text
T1 A + T2 A
→ Q3 Q4 Q5 Q6 Q33
→ Q18 Q19 Q20 Q21 Q37
→ 10 connected MOS drains
```

C side:

```text
T1 C + T2 C
→ Q11 Q12 Q13 Q14 Q36
→ Q24 Q25 Q26 Q27 Q38
→ 10 connected MOS drains
```

All 20 main MOS Source pads connect to `B`.

Therefore the real power stage is not four independent five-MOS converter branches.

### 2.4 Q19 anomaly resolved

Compiled PCB proves:

```text
Q19 Drain → A node / NetC62_1
Q19 Source → B
```

Formal count:

```text
A-side MOS = 10
C-side MOS = 10
total main LV MOS = 20
```

The old `Q19 OPEN / 9+10` model is superseded.

### 2.5 Four local drivers, two logical commands

Physical gate groups:

```text
DA1-G → Q3 Q4 Q5 Q6 Q33
DA2-G → Q18 Q19 Q20 Q21 Q37
DB1-G → Q11 Q12 Q13 Q14 Q36
DB2-G → Q24 Q25 Q26 Q27 Q38
```

Each main MOS has an individual 27.4 Ω gate resistor.

Upstream pairing:

```text
DR-A ─ R213 = 0 Ω ─ DR-A2
DR-B ─ R212 = 0 Ω ─ DR-B2
```

Thus:

```text
4 physical driver subgroups
2 logical switch functions
2 high-current primary switched nodes
```

Actual edge/timing mismatch remains a waveform-measurement item.

---

## 3. Battery-negative protection/sensing interface

Battery negative is separated from primary return `B` by seven parallel TO-220 MOS positions:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

All are `CSD18510KCS`.

Verified hardware:

```text
Source → B
Drain  → BAT-
Gate → 12VP through individual 68.1 Ω
Gate → B through individual 47.5 kΩ pull-down
```

No independent MAIN-board PWM/enable command was found for the seven gates.

Independent ASP product specification explicitly lists:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Status:

```text
ASP reverse-polarity protection product function
= VERIFIED_AT_PRODUCT_FUNCTION_LEVEL

Q39...Q65 as low-side ideal-diode-style implementation
= STRONGLY_SUPPORTED_BY_HARDWARE_STRUCTURE

commandable full battery disconnect by this bank alone
= NOT_SUPPORTED_BY_PRESENT_CIRCUIT
```

The same B↔BAT- boundary is sensed by U4 (`LM2904`) and exported as BOCP.

Ideal MAIN-board transfer:

```text
ΔV_M5 = V_B - V_BAT-
V_BOCP - V_B ≈ 22.1 × ΔV_M5
```

The BOCP control-board threshold/action remains open because the receiver logic/firmware is not in the current evidence set.

Battery-interface loss is classified separately from intrinsic X1 loss.

---

## 4. Verified X1-to-HV connectivity

### 4.1 Secondary series formation

```text
T1 pin 5 = T2 pin 2
```

T1 outer secondary feeds the D1/D5 bridge leg.

### 4.2 T2 outer secondary precharge/bypass region — RESOLVED

Direct SchDoc graph:

```text
T2 pin 5
│
├── RL1 power contact ───────────────────────┐
│                                            │
└── R40 1k/5W ─┐                             │
                ├── R40||R41 = 500 Ω ───────┤
    R41 1k/5W ─┘                             │
                                             ↓
                                      D2 / D6 bridge AC node
```

RL1 identity/control:

```text
RL1 = OZ-SS-112LM1
annotation = 240VAC / 16A / 12VDC
coil pin 1 → 12VP
coil driver → Q29 / D9 / R74 / R78
control net → RELAY_SS1
RELAY_SS1 → CN5A pin 3
```

Formal role:

```text
HV-secondary precharge / soft-start bypass
= VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
```

Interpretation:

```text
startup / bypass inactive
→ secondary-to-bridge current is limited by 500 Ω

normal power state / bypass active
→ RL1 contact bypasses R40/R41
```

Exact relay timing, active polarity, threshold and contact resistance remain open.

### 4.3 HV bridge and DC-link

```text
D1,D2 → BUS+
D5,D6 → BUS-
```

HV DC-link region includes:

```text
C8 C11 C89 C90
= 680 µF / 315 V positions
```

Then:

```text
HV DC-link → HV inverter / X3 → AC output
```

---

## 5. Revised A0 power-path abstraction

```text
BAT+
│
├─ 4× fuse bank → local bulk → T1 center tap ─┐
└─ 4× fuse bank → local bulk → T2 center tap ─┤
                                              │
T1/T2 A half-primaries → A node → 10 MOS ─────┤
T1/T2 C half-primaries → C node → 10 MOS ─────┤
                                              ↓
                                              B
                                              ↓
                         7-MOS battery-interface protection/sensing bank
                                              ↓
                                             BAT-

T1 + T2 magnetic transformation               ← X1
↓
secondary series / collective formation
↓
RL1 + R40/R41 precharge / bypass region
↓
D1/D5 + D2/D6 HV rectification
↓
BUS+ / BUS-
↓
HV DC-link                                     ← passive X2-capable node
↓
HV inverter                                    ← X3
↓
AC output
```

Classification:

```text
A0 = #02 real-product magnetic HFT benchmark
```

---

## 6. Loss-map correction

Steady-state A0 loss decomposition must include:

```text
battery/source impedance
BAT+ connector/common copper
fuse distribution
T1/T2 local feed + J8
local LV bulk ESR/ripple
A/C 10-MOS conduction
A/C switching/Coss/gate/commutation
T1/T2 primary copper/core
secondary copper
leakage/clamp/snubber
RL1 normal-state contact drop if material
HV rectifier
HV DC-link
B return copper
battery-interface protection/sensing bank
HV inverter/output path
```

Do **not** classify startup-only R40/R41 precharge dissipation as ordinary steady-state X1 conversion loss.

Use:

```text
R40/R41 startup energy
= product precharge / inrush-management overhead

RL1 closed-contact drop
= normal steady-state post-X1/interconnect loss
```

---

## 7. Critical research consequences

A0 already contains:

```text
10-way silicon paralleling per logical switch
split local gate driving
multiple HFT magnetic paths
separate fused center-tap feeds
local LV energy support
shared primary-end switched nodes
secondary series voltage formation
HV-link precharge / soft-start bypass
HV DC-link before X3
input reverse-polarity protection
battery-return analog fault/current information
```

None of these alone can be credited as candidate novelty.

Candidate claims must still satisfy:

```text
P_saved > P_added
```

and must separate:

```text
battery-interface improvement
startup/precharge implementation improvement
intrinsic X1 conversion improvement
```

---

## 8. Required A1 comparison

A1 is allowed equivalent engineering freedom:

```text
optimized LV distribution
heavy parallel silicon
distributed local gate drivers
optimized magnetic X1
collective HV formation
matched reverse-polarity protection under product Contract P
matched fault/current information under product Contract P
matched HV-link precharge/inrush function under product Contract P
X3
```

For core-converter steady-state Contract C, product-interface overhead and startup-only precharge energy may be excluded only when excluded from every architecture equally.

---

## 9. Open evidence

```text
exact switching frequency / duty / dead time
DA1-vs-DA2 and DB1-vs-DB2 dynamic mismatch
silicon subgroup current sharing
T1/T2 turns ratio
T1/T2 current balance
fuse sharing / hot resistance
J8 conductor resistance
hot MOS RDS(on)
PCB/return Rac
transformer winding Rac / core loss
leakage/clamp processed power
RL1 contact resistance / timing / threshold
source 100/120 Hz current
HV DC-link ripple
BOCP receiver threshold/control response
A0 measured static loss
A0 dynamic switch/HFT loss
```

---

## 10. Formal status

```text
ASP A0 main power graph                   = SUBSTANTIALLY_RECONSTRUCTED
center-tap/fuse grouping                  = VERIFIED
A node / 10 MOS                           = VERIFIED
C node / 10 MOS                           = VERIFIED
all main MOS Sources → B                  = VERIFIED
4 local drivers / 2 logical commands      = VERIFIED_AT_CONNECTIVITY_LEVEL
secondary series/bridge graph             = VERIFIED
battery-interface seven-MOS boundary      = VERIFIED
ASP reverse-polarity product function     = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
BOCP analog transfer                      = VERIFIED_FROM_MAIN_BOARD
RL1 identity/contact path                 = VERIFIED
RELAY_SS1 control net                     = VERIFIED
RL1 precharge/soft-start bypass role      = VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
RL1 normal contact loss/timing            = OPEN
A0 numerical BAT→X1 loss budget           = OPEN
A0 benchmark                              = ESTABLISHED
candidate superiority                     = NOT_ESTABLISHED
active X2 benefit                         = NOT_ESTABLISHED
novelty                                   = NOT_ESTABLISHED
```

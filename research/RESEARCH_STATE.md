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

Mandatory rule:

```text
P_saved > P_added
```

---

## 2. Functional coordinates

```text
X1 = first major impedance / current-domain transformation region
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC-synthesis region
```

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

Current emphasis:

```text
#02 = PRIMARY REAL-PRODUCT / EARLY-X1 BENCHMARK
#03 = PRIMARY ACTIVE-HFT BENCHMARK
#04 = PRIMARY NON-ISOLATED / CURRENT-DISTRIBUTION BENCHMARK
#09 = PRIMARY MODERN DIRECT-HFL BENCHMARK
```

```text
Candidate #10 = NOT_ASSIGNED
```

Modularization, IPOS, current sharing, capacitive isolation, active buffer, partial power and soft switching remain orthogonal dimensions rather than automatic new families.

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
local decoupling       = KEEP
early fan-out          = HYPOTHESIS / not automatic loss reduction
branch switching + X1  = CORE RESEARCH REGION
active X2              = OPTIONAL / NOT_PROVEN
X3 after X1            = KEEP
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

Actual propagation/timing mismatch remains a waveform item.

### 5.4 Correct current variables

```text
I_T1 / I_T2
= transformer center-feed / winding currents

I_A,total / I_C,total
= total current through the two electrical switch functions

I_DA1 / I_DA2 / I_DB1 / I_DB2
= local silicon-subgroup currents
```

Stable-conduction approximation:

```text
I_A,total ≈ I_T1,A + I_T2,A
I_C,total ≈ I_T1,C + I_T2,C
```

Do not equate DA1/DA2 subgroup current with T1/T2 current.

---

## 6. Battery-negative protection/sensing interface — PRODUCT FUNCTION LOCKED

Seven `CSD18510KCS` devices form one full-current parallel bank:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

Verified hardware:

```text
Source → B
Drain  → BAT-
12VP → individual 68.1 Ω → Gate
Gate → individual 47.5 kΩ → B
```

ASP product specification independently lists:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Current status:

```text
ASP input reverse-polarity function
= VERIFIED_AT_PRODUCT_FUNCTION_LEVEL

Q39...Q65 as low-side ideal-diode-style implementation
= STRONGLY_SUPPORTED_BY_HARDWARE_STRUCTURE

commandable full disconnect by this bank alone
= NOT_SUPPORTED_BY_PRESENT_CIRCUIT
```

This loss is classified primarily as:

```text
battery-interface protection/sensing overhead
```

not intrinsic magnetic-X1 loss.

---

## 7. BOCP analog sensing — TRANSFER RELATION RESOLVED

Direct SchDoc wiring establishes:

```text
B = local SIG reference in the U4 analog region
```

U4 (`LM2904`) network:

```text
U4 + input → B / SIG
BAT- → R153 = 1.00 kΩ → U4 - input
U4 output → R152 = 22.1 kΩ negative feedback → U4 - input
U4 output → R154 = 100 Ω → BOCP → CN4A pin 6
U4 rails → 12VP / -12V
```

Define:

```text
ΔV_M5 = V_B - V_BAT-
```

Ideal linear relation:

```text
V_U4out - V_B ≈ 22.1 × ΔV_M5
```

For a high-impedance BOCP receiver:

```text
V_BOCP - V_B ≈ 22.1 × ΔV_M5
```

At the existing 175.4 A / seven-MOS 25°C datasheet scale:

```text
R_bank ≈ 0.243 mΩ
ΔV_M5 ≈ 42.6 mV
P_M5 ≈ 7.47 W
nominal BOCP above B ≈ 0.94 V
```

All are non-measured scale references.

```text
BOCP analog transfer relation = VERIFIED_FROM_MAIN_BOARD
BOCP measured gain/offset      = OPEN
BOCP exact trip/control action = OPEN / EVIDENCE_BLOCKED
```

Drive search did not locate the BOCP receiver/control-board logic or firmware.

Formal loss evidence remains:

```text
I_source + ΔV_M5 + temperature
```

BOCP is a sense-chain cross-check, not benchmark-grade current metrology.

---

## 8. X1→HV structure — RL1 ROLE RESOLVED

Secondary series connection:

```text
T1 pin 5 = T2 pin 2
```

Outer legs:

```text
T1 outer → D1 / D5 bridge leg
```

The T2 outer path is now resolved in detail:

```text
T2 pin 5
│
├── RL1 power contact ───────────────────────┐
│                                            │
└── R40 1k/5W ─┐                             │
                ├── 500 Ω precharge path ───┤
    R41 1k/5W ─┘                             │
                                             ↓
                                      D2 / D6 bridge AC node
```

Verified RL1 details:

```text
RL1 = OZ-SS-112LM1
annotation = 240VAC / 16A / 12VDC
coil pin 1 → 12VP
coil driver → Q29 / D9 / R74 / R78
control net → RELAY_SS1
RELAY_SS1 → CN5A pin 3
```

Formal decision:

```text
RL1 HV-secondary precharge / soft-start bypass
= VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
```

Functional sequence:

```text
startup / bypass not active
→ secondary current reaches bridge through R40 || R41 = 500 Ω
→ HV DC-link inrush/precharge current is limited

normal power state / bypass active
→ RL1 contact bypasses the 500 Ω path
→ normal secondary current reaches D2/D6 through the relay contact path
```

Open items:

```text
RELAY_SS1 active polarity
control-board precharge timing / bus threshold
relay contact resistance at operating temperature
```

Loss classification:

```text
R40/R41 startup dissipation
= precharge/inrush-management overhead
= NOT ordinary steady-state X1 loss

RL1 normal contact drop
= steady-state post-X1/interconnect loss
= MEASUREMENT_NEEDED
```

Detailed evidence:

```text
research/20_ASP2000_A0_RL1_HV_PRECHARGE_BYPASS.md
```

---

## 9. Revised A0 path

```text
BAT+
│
├─ 4-fuse bank → local bulk → T1 center tap ─┐
└─ 4-fuse bank → local bulk → T2 center tap ─┤
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
RL1 + R40/R41 precharge/bypass region
↓
D1/D5 + D2/D6 HV bridge rectification
↓
BUS+ / BUS-
↓
HV DC-link                                     ← passive X2-capable node
↓
HV inverter                                    ← X3
↓
AC
```

A0 remains family `#02`.

---

## 10. Current numerical bounds — NOT MEASURED

### Positive PCB / distribution

```text
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

`GEOMETRY_MODEL / NOT_MEASURED`.

### Main A/C MOS

```text
CSD18542KCS
10 MOS per logical switch
R_A,eq≈R_C,eq≈0.400 mΩ @ 25C max-data boundary
P_mainMOS,cond,25C-bound≈12.3 W
```

`DATASHEET_BOUND / NOT_MEASURED`.

### Battery interface

```text
CSD18510KCS
7 ideal parallel → Req≈0.243 mΩ
P@175.4 A≈7.47 W
```

`DATASHEET_BOUND / NOT_MEASURED`.

Do not sum mixed evidence classes into a claimed measured product loss.

---

## 11. Fair comparison contracts

### Contract P — product level

Match required functions, including as applicable:

```text
input reverse-polarity protection
battery-return fault/current information
fusing / fault isolation
HV DC-link precharge / inrush management
```

Their loss/cost may differ, but the function cannot be silently deleted on the candidate side.

### Contract C — steady-state core converter

```text
exclude battery-interface overhead equally
exclude startup-only precharge energy equally
compare intrinsic steady-state conversion path
```

Forbidden:

```text
candidate deletes A0 product function
→ counts removed watts as topology/X1 advantage
```

---

## 12. Hardware measurement gates

### M5 — current first hardware gate

Historical Drive search did not find a usable ASP-2000 BOCP/M5 load-sweep dataset.

At each controlled point record:

```text
I_source
ΔV_M5 = V_B - V_BAT-
V_BOCP relative B/SIG
12VP
MOS-bank temperature
ambient/cooling condition
```

Then:

```text
R_M5,eff = ΔV_M5 / I_source
P_M5     = I_source × ΔV_M5
G_BOCP   = (V_BOCP - V_B) / ΔV_M5
```

Template:

```text
research/templates/asp2000_a0_m5_bocp_sweep_template.csv
```

### Dynamic switch/HFT gate

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

---

## 13. Current unresolved items

```text
M0–M6 actual Kelvin data
M5 measured hot resistance/loss
BOCP measured gain/intercept
exact BOCP trip/control response
exact switching frequency / duty / dead time
silicon subgroup current sharing
T1/T2 current balance
fuse sharing / hot fuse resistance
J8 physical conductor / resistance
hot main-MOS RDS(on)
B-return copper loss
T1/T2 turns ratio
T1/T2 winding Rac / core loss
leakage/clamp processed power
RELAY_SS1 timing / bus threshold
RL1 contact resistance
source 100/120 Hz ripple
HV DC-link ripple
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
19_ASP2000_A0_BOCP_TRANSFER_AND_M5_DIAGNOSTIC_GATE.md
20_ASP2000_A0_RL1_HV_PRECHARGE_BYPASS.md
```

---

## 15. Current decision state

```text
Research phase                         = Physical Gap Validation
A0 main power/current graph            = SUBSTANTIALLY_RECONSTRUCTED
A logical switch                       = 10 MOS / VERIFIED
C logical switch                       = 10 MOS / VERIFIED
4 drivers / 2 logical commands         = VERIFIED_AT_CONNECTIVITY_LEVEL
positive PCB geometry loss bound       = ESTABLISHED / NOT_MEASURED
ASP reverse-polarity product function  = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
Q39...Q65 ideal-diode implementation   = STRONGLY_SUPPORTED
BOCP analog gain relation              = ~22.1 V/V / VERIFIED_FROM_CIRCUIT
BOCP exact trip/control response        = OPEN / EVIDENCE_BLOCKED
RL1 identity/contact path               = VERIFIED
RELAY_SS1 control net                   = VERIFIED
RL1 HV precharge/soft-start bypass      = VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
RL1 timing/contact loss                 = OPEN
historical ASP-2000 M5 dataset          = NOT_FOUND_IN_CURRENT_DRIVE_SEARCH
battery-interface measured loss         = OPEN
A0 measured distribution loss           = OPEN
A0 dynamic switch/HFT loss              = OPEN
A0 total BAT→X1 loss                    = OPEN
A1 matched model                        = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
Working architecture                    = KEEP
Early fan-out benefit                   = NOT_PROVEN
Active X2 benefit                       = NOT_PROVEN
Candidate #10                           = NOT_ASSIGNED
Novelty                                 = NOT_ESTABLISHED
```

Immediate next evidence gate:

```text
A0 hardware M5 load sweep when hardware is available
+
continue non-hardware closure of T1/T2 magnetic parameters from available files
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized HFT
```

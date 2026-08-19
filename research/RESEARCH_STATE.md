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

## 2. Functional coordinates

```text
X1 = first major impedance/current-domain transformation region
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

## 3. Working power-path families

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

Current emphasis:

```text
#02 = A0/A1 magnetic benchmark
#03 = active-HFT benchmark
#04 = non-isolated/current-distribution benchmark
#09 = direct-HFL benchmark
Candidate #10 = NOT_ASSIGNED
```

---

## 4. Working architecture — KEEP

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
very-short common path = KEEP
local decoupling = KEEP
early fan-out = HYPOTHESIS / NOT_AUTOMATIC_LOSS_REDUCTION
branch switching + X1 = CORE RESEARCH REGION
active X2 = OPTIONAL / NOT_PROVEN
```

---

## 5. A0 real-product benchmark — ASP-2000 R52

### 5.1 Positive-side current distribution

```text
BAT+
├─ F2/F3/F5/F6 → local LV bulk → T1 center tap
└─ F7/F8/F9/F10 → local LV bulk → T2 center tap
```

Both PQ5050 primaries:

```text
pin9 = A
pin8 = center tap
pin7 = C
```

### 5.2 Primary switch architecture — RESOLVED

```text
A node = NetC62_1
→ T1 A + T2 A
→ 10 parallel MOS
→ B

C node = NetC65_1
→ T1 C + T2 C
→ 10 parallel MOS
→ B
```

Q19 drain is verified in compiled PCB; old `9+10` model is superseded.

Gate structure:

```text
DA1 + DA2 → A function
DB1 + DB2 → C function
4 physical driver subgroups
2 logical commands
```

Correct current variables:

```text
I_T1/I_T2 = transformer feed currents
I_A,total/I_C,total = electrical switch currents
I_DA1/I_DA2/I_DB1/I_DB2 = local silicon-subgroup currents
```

Do not equate DA1/DA2 with T1/T2 currents.

---

## 6. Battery-negative protection/sensing interface

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
Drain → BAT-
12VP → individual 68.1Ω → Gate
Gate → individual 47.5kΩ → B
```

Independent ASP product specification explicitly lists:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Status:

```text
ASP reverse-polarity product function = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
Q39...Q65 ideal-diode-style implementation = STRONGLY_SUPPORTED
full commandable disconnect by this bank = NOT_SUPPORTED
```

### BOCP

MAIN-board U4 (`LM2904`) senses the same B↔BAT− boundary.

```text
ΔV_M5 = V_B - V_BAT-
V_BOCP - V_B ≈22.1 × ΔV_M5
```

Status:

```text
BOCP analog transfer = VERIFIED_FROM_MAIN_BOARD
BOCP measured gain/offset = OPEN
BOCP receiver/trip/control action = OPEN / EVIDENCE_BLOCKED
```

Formal loss evidence remains direct `I_source × ΔV_M5` with temperature.

---

## 7. X1→HV structure — RL1 ROLE RESOLVED

```text
T1 pin5 = T2 pin2      ← secondary series junction

T1 outer → D1/D5 bridge leg

T2 pin5
│
├─ RL1 power contact ─────────────┐
└─ R40 1k/5W || R41 1k/5W =500Ω ─┤
                                  ↓
                           D2/D6 bridge leg
↓
BUS+ / BUS-
↓
HV DC-link
↓
X3
```

RL1:

```text
OZ-SS-112LM1
240Vac /16A contact annotation
12Vdc coil
control net = RELAY_SS1
```

Decision:

```text
RL1 HV-secondary precharge / soft-start bypass
= VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
```

Loss classification:

```text
R40/R41 startup energy = precharge/inrush overhead / NOT steady-state X1 loss
RL1 normal contact loss = MEASUREMENT_NEEDED
```

---

## 8. PCB copper manufacturing correction — CRITICAL

Earlier geometry work used PcbDoc stack metadata:

```text
Top/Bottom =1.4 mil ≈35.56 µm
```

The R52 manufacturing specification tied to `PB-2200-0038-D_R52.RAR` instead requires:

```text
FR4 / 1.6 mm / 2 layer
base copper =2.0 oz
finished copper thickness >82 µm
```

Formal decision:

```text
35.56 µm as-built assumption = SUPERSEDED
R52 finished copper >82 µm = CURRENT MANUFACTURING BOUND
```

Using 82 µm as the conservative minimum and the same reconstructed geometry:

```text
R_sheet,1layer,max ≈0.210 mΩ/square
R_sheet,2layer,ideal,max ≈0.105 mΩ/square

BAT+ common PCB:
R≤~0.108 mΩ
P@175.4A≤~3.32 W

T1 local PCB:
R≤~0.152 mΩ
P@87.7A≤~1.17 W

T2 PCB excluding J8:
R≤~0.0624 mΩ
P@87.7A≤~0.48 W

partial positive PCB-only:
R_eq≤~0.162 mΩ
P@175.4A≤~4.98 W
```

All are:

```text
MANUFACTURING_GEOMETRY_BOUND / NOT_MEASURED
```

Superseded values:

```text
BAT+ common ≈7.67 W
partial positive PCB ≈11.5 W
```

Research consequence:

> PCB distribution remains material, but the former conclusion that BAT+ copper is approximately comparable to the entire main-MOS conduction bucket is no longer supported.

---

## 9. Other current numerical bounds — NOT MEASURED

### Main A/C MOS

```text
CSD18542KCS @12V
10 MOS per logical switch
R_A,eq≈R_C,eq≈0.400 mΩ @25C max-data scale
P_mainMOS,cond≈12.3 W
```

### Battery interface

```text
7 × CSD18510KCS ideal parallel
Req≈0.243 mΩ
P@175.4A≈7.47 W
```

Do not sum mixed evidence classes into a product-loss claim.

---

## 10. Transformer parameter evidence gate

R52 files verify only:

```text
T1/T2 = PQ5050
PCB model = DTRF-PQ5050-V
center-tapped primary connectivity
secondary series relationship
```

Current files do NOT establish:

```text
populated transformer internal P/N
turns ratio
A0 Lm/Lk
winding DCR/Rac
core material / Ae / Ve
```

Drive contains `M1-PQ50-V121-A` test data with Lm/Lk measurements, but model-matrix evidence ties that transformer to `ASP-3000W-24V-200ac-S9C`, not A0.

Therefore:

```text
M1-PQ50-V121-A data = CONTEXT_ONLY / DIFFERENT VARIANT
A0 transformer numerical parameters = OPEN
```

The R52 component-coordinate export and PCB-layout JPG also identify T1/T2 only as `PQ5050`; no production transformer P/N has been recovered from currently accessible R52 files.

Preferred closure:

```text
1. correct ASP-2000 BOM / transformer label / magnetic drawing
2. power-off LCR characterization
3. low-energy turns-ratio test
4. Kelvin winding DCR
5. core/material specification
```

---

## 11. Fair comparison contracts

```text
Contract P — product level
match reverse-polarity protection, required sensing/fusing and HV precharge/inrush functionality; count losses.

Contract C — steady-state core converter
exclude battery-interface overhead and startup-only precharge energy equally across A0/A1/candidate.
```

Never delete A0 product functions only on the candidate side and call removed watts a topology advantage.

---

## 12. Current hardware gates

Static/Kelvin:

```text
M0 BAT+ distribution
M1 fuse banks
M2 T1 local feed
M3 J8
M4 T2 local feed
M5 B↔BAT− battery-interface bank
M6 B return copper
```

First hardware priority:

```text
M5 load sweep:
I_source
ΔV_M5
V_BOCP relative B/SIG
12VP
MOS-bank temperature
```

Dynamic/HFT:

```text
fs / duty / dead time
actual VGS
V_A-B / V_C-B
I_T1 / I_T2
synchronous switch-region v×i
primary volt-second
T1/T2 temperature
correct-transformer L/ratio/DCR/material data
```

---

## 13. Benchmark stack

```text
A0 — actual ASP-2000 R52
A1 — fair optimized magnetic HFT
B  — Direct HFL
C  — non-isolated current-distribution/high-gain
D  — working candidate architecture
```

A1 remains blocked from a claimed quantitative advantage until A0 loss localization is sufficiently closed.

---

## 14. Current unresolved items

```text
M0–M6 actual mV/current data
M5 measured hot loss
BOCP receiver/trip logic
fs / duty / dead time
silicon subgroup sharing
T1/T2 current balance
fuse sharing/hot resistance
J8 conductor/resistance
hot main-MOS RDS(on)
B-return copper loss
A0 transformer populated P/N
A0 turns ratio / Lm / Lk / Rac / core material
RL1 contact resistance / RELAY_SS1 timing
source 100/120Hz ripple
HV DC-link ripple
A0 dynamic switch/HFT loss
A0 total BAT→X1 loss
A1 total loss
candidate superiority
```

---

## 15. Formal decision state

```text
Research phase                         = Physical Gap Validation
A0 main power/current graph            = SUBSTANTIALLY_RECONSTRUCTED
A logical switch                       = 10 MOS / VERIFIED
C logical switch                       = 10 MOS / VERIFIED
4 drivers /2 logical commands          = VERIFIED_AT_CONNECTIVITY_LEVEL
R52 finished copper                    = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm PCB loss model            = SUPERSEDED
BAT+ common PCB geometry bound         = ≤~3.32 W / NOT_MEASURED
partial positive PCB geometry bound    = ≤~4.98 W / NOT_MEASURED
ASP reverse-polarity function          = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
Q39...Q65 implementation               = STRONGLY_SUPPORTED
BOCP analog gain                       = ~22.1 V/V / VERIFIED_FROM_CIRCUIT
RL1 precharge/bypass role              = VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
A0 transformer numerical parameters    = OPEN
M1-PQ50-V121-A cross-model data         = CONTEXT_ONLY
A0 measured distribution loss          = OPEN
A0 dynamic switch/HFT loss             = OPEN
A0 total BAT→X1 loss                   = OPEN
A1 matched model                       = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
Early fan-out benefit                  = NOT_PROVEN
Active X2 benefit                      = NOT_PROVEN
Candidate #10                          = NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

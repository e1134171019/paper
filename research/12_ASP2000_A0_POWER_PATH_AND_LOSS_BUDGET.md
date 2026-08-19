# 12 — ASP-2000 A0 Power Path and Loss-Budget Gate

Status date: 2026-08-19  
Role: `A0 POWER-PATH / LOSS-LOCALIZATION GATE`  
Evidence status: `SCHDOC + COMPILED-PCB NET RECONSTRUCTION + LOSS BOUNDS`  
Measurement status: `PARTIAL MODEL / NOT YET HARDWARE-MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document defines the real ASP-2000 R52 `BAT → X1 → HV-link` path and the loss terms that must be closed before A1 optimized-HFT synthesis.

Central question:

> Where is A0 loss actually concentrated while the source current is still in the expensive 12 V / hundred-ampere domain, and which downstream losses are intrinsic steady-state conversion losses versus product startup/protection overhead?

Raw company source artifacts remain outside the public repository.

---

## 2. Verified positive-side power distribution

```text
BAT+
├─ F2 / F3 / F5 / F6 → T1 center tap + local bulk
└─ F7 / F8 / F9 / F10 → T2 center tap + local bulk
```

Main-fuse annotation:

```text
40 A / 32 V @12 V
20 A / 32 V @24 V
```

Both PQ5050 primaries use:

```text
pin 9 = A
pin 8 = center tap
pin 7 = C
```

The two center-tap supply/local-bulk paths remain separate.

---

## 3. Verified primary switch power nodes

### A-side

```text
NetC62_1
→ T1 A + T2 A
→ Q3 Q4 Q5 Q6 Q33
→ Q18 Q19 Q20 Q21 Q37
```

All ten sources → `B`.

### C-side

```text
NetC65_1
→ T1 C + T2 C
→ Q11 Q12 Q13 Q14 Q36
→ Q24 Q25 Q26 Q27 Q38
```

All ten sources → `B`.

Therefore:

```text
A logical switch = 10 parallel MOS
C logical switch = 10 parallel MOS
common source/return = B
```

Q19 is physically connected to the A node in compiled PCB; the old `Q19 OPEN / 9+10 MOS` model is superseded.

Physical gate-driver groups are paired into two logical commands:

```text
DR-A ─ R213 = 0 Ω ─ DR-A2
DR-B ─ R212 = 0 Ω ─ DR-B2
```

Thus:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched nodes
```

---

## 4. Correct current mapping

Define:

```text
i_T1(t), i_T2(t)
= transformer center-feed / winding currents

i_A,total(t), i_C,total(t)
= total current through the two electrical switch functions
```

During stable conduction:

```text
i_A,total ≈ i_T1,A + i_T2,A
i_C,total ≈ i_T1,C + i_T2,C
```

Do not equate DA1/DA2 subgroup currents with T1/T2 currents. DA1/DA2 are parallel silicon subgroups on one A node; DB1/DB2 are parallel subgroups on C.

During switching/dead time, Coss/body-diode/leakage/clamp/ringing current requires synchronous high-bandwidth evidence.

---

## 5. Battery-negative full-current protection/sensing interface

The main switching return `B` reaches battery negative through seven parallel `CSD18510KCS` devices:

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

No independent MAIN-board PWM/enable command exists between `12VP` and this seven-MOS gate bank.

Independent ASP product specification explicitly lists:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Status:

```text
ASP reverse-polarity product function
= VERIFIED_AT_PRODUCT_FUNCTION_LEVEL

Q39...Q65 low-side ideal-diode-style implementation
= STRONGLY_SUPPORTED_BY_HARDWARE_STRUCTURE

independent full-disconnect role of this bank
= NOT_SUPPORTED_BY_PRESENT_CIRCUIT
```

The same B↔BAT- boundary is monitored by U4 (`LM2904`).

Define:

```text
ΔV_M5 = V_B - V_BAT-
```

MAIN-board analog relation:

```text
V_BOCP - V_B ≈ 22.1 × ΔV_M5
```

for a high-impedance BOCP receiver in the linear region.

Formal status:

```text
BOCP analog transfer = VERIFIED_FROM_MAIN_BOARD
BOCP receiver threshold/control action = OPEN / EVIDENCE_BLOCKED
```

The seven-MOS loss is classified primarily as battery-interface protection/sensing overhead, not intrinsic magnetic-X1 loss.

---

## 6. X1-to-HV path — RL1 PRECHARGE ROLE RESOLVED

### 6.1 Secondary series junction

```text
T1 pin 5 = T2 pin 2
```

T1 outer secondary feeds the D1/D5 bridge leg.

### 6.2 T2 outer-secondary path

Direct SchDoc graph now establishes:

```text
T2 pin 5
│
├── RL1 power contact ───────────────────────┐
│                                            │
└── R40 1 kΩ / 5 W ─┐                        │
                     ├─ 500 Ω precharge ─────┤
    R41 1 kΩ / 5 W ─┘                        │
                                             ↓
                                      D2 / D6 bridge AC node
```

Therefore:

```text
R40 || R41 = 500 Ω
```

Verified relay identity/control:

```text
RL1 = OZ-SS-112LM1
annotation = 240VAC / 16A / 12VDC
coil pin 1 → 12VP
local coil driver → Q29 / D9 / R74 / R78
control net → RELAY_SS1
RELAY_SS1 → CN5A pin 3
```

Formal role:

```text
RL1 HV-secondary precharge / soft-start bypass
= VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
```

Structural operating sequence:

```text
startup / RL1 bypass inactive
→ T2 secondary-to-bridge path includes R40 || R41 = 500 Ω
→ HV-link charging/inrush is limited

normal conversion / RL1 bypass active
→ relay contact bypasses R40/R41
→ normal secondary current reaches D2/D6 through RL1 contact path
```

Exact `RELAY_SS1` polarity, delay, bus threshold and fault logic remain open because control-board evidence is not available.

### 6.3 HV bridge and DC-link

```text
D1,D2 → BUS+
D5,D6 → BUS-
↓
HV DC-link
↓
HV inverter / X3
↓
AC
```

---

## 7. Revised A0 power path

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
HV bridge rectification
↓
HV DC-link                                    ← passive X2-capable node
↓
HV inverter                                   ← X3
↓
AC
```

---

## 8. Anchor-current references

```text
Vin = 12 V
Pout = 2 kW
Iin,ideal = 166.7 A
Iin@95% scaling ≈ 175.4 A
```

Ideal equal-share references only:

```text
I_T1 ≈ I_T2 ≈ 87.7 A
I_fuse ≈ 21.9 A per fuse
```

They are not measured RMS currents.

---

## 9. Current numerical bounds

### Main A/C MOS

12 V population:

```text
CSD18542KCS
RDS(on),max @ VGS=10 V = 4 mΩ
```

Ten devices per logical switch:

```text
R_A,eq ≈ R_C,eq ≈ 0.400 mΩ
```

Same simplified 175.4 A / 50%-per-side sensitivity model:

```text
P_mainMOS,cond,25C-bound ≈ 12.3 W
```

`DATASHEET_BOUND / NOT_MEASURED`.

### Battery-interface seven-MOS bank

```text
CSD18510KCS
RDS(on),max @ VGS=10 V = 1.7 mΩ
7 ideal parallel → R_eq≈0.243 mΩ
175.4 A scaling → ≈7.47 W
```

`DATASHEET_BOUND / NOT_MEASURED`.

### RL1 / R40 / R41

```text
R40 = 1 kΩ / 5 W
R41 = 1 kΩ / 5 W
R40 || R41 = 500 Ω
```

The resistor path is a startup/precharge path and is **not** included in ordinary steady-state X1 efficiency.

Normal-state RL1 contact drop/resistance remains:

```text
MEASUREMENT_NEEDED
```

---

## 10. Loss-equation boundary correction

### Product-level steady-state BAT→HV-link accounting

```text
P_A0,steady/product =
    P_BAT+connector/commonCopper
  + P_fuseBanks
  + P_T1localFeed
  + P_T2localFeed/J8
  + P_bulkRipple
  + P_A/C_MOS,cond
  + P_A/C_MOS,sw
  + P_primary,Cu
  + P_core
  + P_commutation/clamp
  + P_secondary,Cu
  + P_RL1,contact
  + P_HVrectifier
  + P_BreturnCopper
  + P_batteryInterfaceProtection/Sensing
```

### Startup-only product-function energy

```text
E_precharge,R40/R41
```

belongs to:

```text
HV DC-link precharge / inrush-management overhead
```

not ordinary steady-state magnetic-X1 loss.

Do not mix startup joules with a steady-state watts comparison without an explicit duty/repetition contract.

---

## 11. Fair comparison contracts

### Contract P — product level

A0/A1/candidate must match required functions, including as applicable:

```text
input reverse-polarity protection
battery-return fault/current information
fusing / fault isolation
HV-link precharge / inrush management
```

Implementation may differ; its loss/energy must be counted under the same operating contract.

### Contract C — steady-state core converter

Product-interface overhead and startup-only precharge energy may be excluded only when excluded from A0, A1 and every candidate equally.

Forbidden inference:

```text
candidate removes A0 product function
→ calls removed watts/joules an X1/topology improvement
```

---

## 12. Measurement priorities

### Static / Kelvin

```text
M0 BAT+ distribution
M1 fuse banks
M2 T1 local feed
M3 J8
M4 T2 local feed
M5 B ↔ BAT- battery-interface bank
M6 B return copper
```

For M5:

```text
I_source
ΔV(B↔BAT-)
12VP
MOS temperature
BOCP voltage relative B/SIG if safely accessible
```

### Dynamic / switching / magnetic

```text
fs / duty / dead time
V_A-B / V_C-B
I_T1 / I_T2
actual VGS
switch-region synchronous v×i
primary volt-second
T1/T2 temperature
```

### Post-X1 steady-state

If RL1 contact loss is material and safely accessible:

```text
P_RL1,contact = I_secondary × ΔV_RL1
```

Do not measure across the 500 Ω precharge branch as though it were the normal full-power path.

---

## 13. Current loss-budget table

| Region | Current boundary | Loss model | Evidence status |
|---|---|---|---|
| BAT+ common distribution | multi-terminal branch currents | `Σ I_k ΔV_k` | `PARTIAL_GEOMETRY_BOUND` |
| 2 × four-fuse banks | branch/fuse current | `Σ IΔV` | `MEASUREMENT_NEEDED` |
| T1/T2 local + J8 | `I_T1`,`I_T2` | `IΔV` | `PARTIAL_GEOMETRY / J8_OPEN` |
| A logical switch / 10 MOS | `i_A,total` | `avg(v_A-B i_A)` | `DYNAMIC_MEASUREMENT_NEEDED` |
| C logical switch / 10 MOS | `i_C,total` | `avg(v_C-B i_C)` | `DYNAMIC_MEASUREMENT_NEEDED` |
| T1/T2 primary | winding current | copper + core | `Rac/fs/flux NEEDED` |
| B return copper | source-return current | `IΔV` | `MEASUREMENT_NEEDED` |
| battery-interface 7 MOS | `I_source` | `I×ΔV(B↔BAT-)` | `FUNCTION_CLASSIFIED / LOSS_OPEN` |
| secondary copper | secondary current | `I²Rac` | `OPEN` |
| RL1 closed contact | secondary current | `I×ΔV` | `FUNCTION_VERIFIED / LOSS_OPEN` |
| R40/R41 startup branch | precharge transient current | `∫v i dt` / pulse energy | `STARTUP_FUNCTION / NOT_STEADY_STATE_X1` |
| HV rectifier | secondary/bridge current | diode + commutation | `WAVEFORM_NEEDED` |

---

## 14. Historical-data check

Drive search did not locate a usable ASP-2000 M5 / BOCP load-sweep dataset.

A generic ASP no-load sheet was found for other units, but it must not be substituted for the ASP-2000 A0 benchmark.

Therefore:

```text
historical ASP-2000 M5 evidence
= NOT_FOUND_IN_CURRENT_DRIVE_SEARCH
```

---

## 15. Gate decision

Current sequence:

```text
A0 M5/static hardware data when available
+
continue non-hardware closure of T1/T2 magnetic parameters
↓
A0 distribution + dynamic loss localization
↓
separate product-interface/startup overhead from intrinsic steady-state X1 loss
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized HFT
↓
X1 mechanism comparison
↓
X2 Buffer OFF/ON
↓
Candidate synthesis only if a physical gap survives
```

Formal status:

```text
A0 topology/current graph                  = SUBSTANTIALLY_RECONSTRUCTED
battery-interface reverse-polarity function = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
BOCP analog transfer                       = VERIFIED_FROM_MAIN_BOARD
RL1 precharge/soft-start bypass             = VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
RL1 timing/contact loss                     = OPEN
A0 numerical loss budget                    = OPEN
A1                                         = BLOCKED UNTIL A0 LOSS LOCALIZATION
Candidate superiority                      = NOT_ESTABLISHED
Novelty                                    = NOT_ESTABLISHED
```

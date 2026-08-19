# 12 — ASP-2000 A0 Power Path and Loss-Budget Gate

Status date: 2026-08-19  
Role: `A0 POWER-PATH / LOSS-LOCALIZATION GATE`  
Evidence status: `SCHDOC + COMPILED-PCB NET RECONSTRUCTION + LOSS BOUNDS`  
Measurement status: `PARTIAL MODEL / NOT YET HARDWARE-MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document defines the real ASP-2000 R52 `BAT → X1` power path and the loss terms that must be closed before A1 optimized-HFT synthesis.

Central question:

> Where is A0 loss actually concentrated while the ~175 A-class source current is still in the expensive 12 V domain?

Raw company source artifacts remain outside the public repository.

---

## 2. Verified positive-side power distribution

```text
BAT+
├─ F2 / F3 / F5 / F6 ─→ T1 center tap + local bulk
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

Compiled PCB mapping identifies separate center-tap supply/local-bulk nets for T1 and T2.

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

Q19 is physically connected to the A node in the compiled PCB; the old `Q19 OPEN / 9+10 MOS` model is superseded.

Four physical gate-driver groups are paired into two commands:

```text
DR-A  ─ R213 = 0 Ω ─ DR-A2
DR-B  ─ R212 = 0 Ω ─ DR-B2
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

Do not equate DA1/DA2 subgroup currents with T1/T2 currents. DA1 and DA2 are parallel silicon subgroups on the same A node; DB1 and DB2 are parallel subgroups on C.

During switching/dead time, Coss/body-diode/leakage/clamp/ringing current requires synchronous high-bandwidth evidence.

---

## 5. Battery-negative full-current protection/sensing interface — FUNCTION NARROWED

The main switching return `B` reaches battery negative through seven parallel MOSFETs:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

All seven are `CSD18510KCS` with verified orientation:

```text
Source → B
Drain  → BAT-
```

Gate network for every device:

```text
12VP
↓
individual 68.1 Ω
↓
Gate
↓
individual 47.5 kΩ
↓
B
```

No independent MAIN-board PWM/enable command exists between `12VP` and this seven-MOS gate bank.

The orientation and common gate bias are structurally consistent with:

```text
low-side reverse-polarity / ideal-diode-style battery interface
```

Status:

```text
reverse-polarity / ideal-diode-style role = STRONGLY SUPPORTED
independent full-disconnect role of this bank = NOT SUPPORTED BY PRESENT CIRCUIT
```

The same electrical boundary is monitored by U4 (`LM2904`):

```text
U4 + input → B
BAT- → R153=1 kΩ → U4 - input
U4 output feedback → R152=22.1 kΩ → - input
U4 output → R154=100 Ω → BOCP → CN4A pin 6
```

Therefore:

```text
B↔BAT- drop sensing → BOCP = VERIFIED
BOCP over-current / abnormal-drop protection role = STRONGLY SUPPORTED
exact threshold / polarity / control-board response = OPEN
```

Detailed evidence:

```text
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
```

This seven-MOS loss is therefore classified primarily as `battery-interface protection/sensing overhead`, not as intrinsic magnetic-X1 loss.

---

## 6. Verified X1-to-HV path

```text
T1 pin 5 = T2 pin 2      ← secondary series junction
T1 outer → D1/D5
T2 outer → RL1 → D2/D6
D1,D2 → BUS+
D5,D6 → BUS-
↓
HV DC-link
↓
HV inverter / X3
↓
AC
```

`RL1` exact role remains open.

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
HV bridge rectifier
↓
HV DC-link                                    ← passive X2-capable node
↓
HV inverter                                   ← X3
↓
AC
```

---

## 8. Anchor current references

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

`DATASHEET_BOUND / NOT MEASURED`.

### Battery-interface seven-MOS bank

```text
CSD18510KCS
RDS(on),max @ VGS=10 V = 1.7 mΩ
7 ideal parallel → R_eq≈0.243 mΩ
175.4 A scaling → ≈7.47 W
```

`DATASHEET_BOUND / NOT MEASURED`.

Actual interface loss should be measured as:

```text
P_batteryInterface = I_source × ΔV(B↔BAT-)
```

with temperature and 12VP recorded.

---

## 10. BAT→X1 loss equation — boundary corrected

For a **product-level** A0 loss budget:

```text
P_A0,BAT→X1/product =
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
  + P_BreturnCopper
  + P_batteryInterfaceProtection/Sensing
```

For a **core-converter** comparison, the battery-interface protection/sensing term may be excluded only if it is excluded from A0, A1 and every candidate equally.

Forbidden inference:

```text
remove Q39...Q65 functionality
→ claim the removed watts as X1/topology improvement
```

If a candidate preserves equivalent product function with lower loss, classify that saving first as battery-interface/protection engineering improvement.

---

## 11. Measurement priorities

Static/Kelvin:

```text
M0 BAT+ distribution
M1 individual fuses
M2 T1 local feed
M3 J8
M4 T2 local feed
M5 B ↔ BAT- battery-interface bank
M6 B return copper
```

For M5 record:

```text
I_source
ΔV(B↔BAT-)
12VP
MOS temperature
BOCP voltage/state if safely accessible
```

Dynamic:

```text
fs / duty / dead time
V_A-B / V_C-B
I_T1 / I_T2
actual VGS
switching-region v×i
primary volt-second
T1/T2 temperature
```

---

## 12. Current loss-budget table

| Region | Current boundary | Loss model | Evidence status |
|---|---|---|---|
| BAT+ common distribution | multi-terminal branch currents | `Σ I_k ΔV_k` | partial geometry bound |
| 2 × four-fuse banks | individual fuse current | `Σ I ΔV` | measurement needed |
| T1/T2 local + J8 | `I_T1`,`I_T2` | `IΔV` | partial geometry / J8 open |
| A logical switch / 10 MOS | `i_A,total` | `avg(v_A-B i_A)` | dynamic measurement needed |
| C logical switch / 10 MOS | `i_C,total` | `avg(v_C-B i_C)` | dynamic measurement needed |
| T1/T2 primary | winding current | copper + core | Rac/fs/flux needed |
| B return copper | source-return current | `IΔV` | measurement needed |
| battery-interface 7 MOS | `I_source` | `I×ΔV(B↔BAT-)` | function classified / loss not measured |
| X1→rectifier | secondary current | copper + diode/commutation | waveform needed |

---

## 13. Gate decision

Current sequence remains:

```text
A0 static + dynamic loss measurement
↓
separate product-interface loss from intrinsic X1 loss
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
A0 topology/current graph                 = SUBSTANTIALLY RECONSTRUCTED
battery-interface power path              = VERIFIED
reverse-polarity / ideal-diode role       = STRONGLY SUPPORTED
B↔BAT- sensing → BOCP                     = VERIFIED
exact BOCP response                       = OPEN
A0 numerical loss budget                  = OPEN
A1                                        = BLOCKED UNTIL A0 LOSS LOCALIZATION
Candidate superiority                     = NOT ESTABLISHED
Novelty                                   = NOT ESTABLISHED
```
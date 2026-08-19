# 12 — ASP-2000 A0 Power Path and Loss-Budget Gate

Status date: 2026-08-19  
Role: `A0 POWER-PATH / LOSS-LOCALIZATION GATE`  
Evidence status: `SCHDOC + COMPILED-PCB NET RECONSTRUCTION + LOSS BOUNDS`  
Measurement status: `PARTIAL MODEL / NOT YET HARDWARE-MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document defines the real ASP-2000 R52 `BAT → X1` power path and the loss terms that must be closed before A1 optimized-HFT synthesis.

Raw source artifacts remain outside the public repository.

Central question:

> Where is A0 loss actually concentrated while the ~175 A-class source current is still in the expensive 12 V domain?

---

## 2. Verified positive-side power distribution

### 2.1 Two separately fused center-tap feeds

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

### 2.2 Center-tapped primaries

Both PQ5050 primaries use:

```text
pin 9 = A
pin 8 = center tap
pin 7 = C
```

Compiled PCB mapping identifies:

```text
T1 center tap → NetC2_1
T2 center tap → NetC28_1
```

These are separately supplied/local-bulk nodes.

---

## 3. Verified primary switch power nodes

### 3.1 A-side switched node

Compiled PCB net:

```text
NetC62_1
```

contains both transformer A ends and ten MOS drains:

```text
T1 A
T2 A
Q3 Q4 Q5 Q6 Q33
Q18 Q19 Q20 Q21 Q37
```

All ten corresponding MOS sources connect to:

```text
B
```

Therefore:

```text
A logical switch function = 10 parallel MOS
```

### 3.2 C-side switched node

Compiled PCB net:

```text
NetC65_1
```

contains both transformer C ends and ten MOS drains:

```text
T1 C
T2 C
Q11 Q12 Q13 Q14 Q36
Q24 Q25 Q26 Q27 Q38
```

All ten sources connect to:

```text
B
```

Therefore:

```text
C logical switch function = 10 parallel MOS
```

### 3.3 Q19 correction

Earlier SchDoc-only graph extraction made Q19 appear disconnected.

Compiled PCB evidence resolves it:

```text
Q19 Drain → NetC62_1
Q19 Source → B
```

Formal status:

```text
Q19 connectivity = VERIFIED IN PCB
A-side MOS count = 10
C-side MOS count = 10
```

The old 9+10 / Q19-OPEN model is superseded.

---

## 4. Four driver subgroups are not four power branches

Physical gate groups:

```text
DA1-G → Q3 Q4 Q5 Q6 Q33
DA2-G → Q18 Q19 Q20 Q21 Q37
DB1-G → Q11 Q12 Q13 Q14 Q36
DB2-G → Q24 Q25 Q26 Q27 Q38
```

Upstream controls:

```text
DR-A  ─ R213 = 0 ohm ─ DR-A2
DR-B  ─ R212 = 0 ohm ─ DR-B2
```

Therefore:

```text
A command → DA1 + DA2 local drivers → 10 MOS on one A power node
B command → DB1 + DB2 local drivers → 10 MOS on one C power node
```

Accurate abstraction:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched nodes
```

The local SchDoc `DA1-E / DB1-E / DA2-E / DB2-E` labels must not be treated as four separate physical source-return power nets. Compiled PCB source pads and low-side driver references all return to `B`.

---

## 5. Verified negative full-current path

Main primary switching return `B` is not identical to battery negative.

Seven TO-220 MOS devices bridge:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

All are annotated:

```text
CSD18510KCS
```

Status:

```text
negative-side full-current series MOS region = VERIFIED
exact protection/disconnect role = OPEN
```

This region must be included or boundary-matched in any fair A0/A1/candidate loss comparison.

---

## 6. Verified X1-to-HV path

Secondary reconstruction establishes:

```text
T1 pin 5 = T2 pin 2      ← direct series junction
T1 outer → D1/D5
T2 outer → RL1 → D2/D6
```

Rectifier outputs:

```text
D1,D2 → BUS+
D5,D6 → BUS-
```

Then:

```text
HV DC-link → HV inverter / X3 → AC
```

`RL1` exact role remains open.

---

## 7. Revised A0 power-path graph

```text
BAT+
│
├─ four-fuse bank → local bulk → T1 center tap ─┐
│                                               │
└─ four-fuse bank → local bulk → T2 center tap ─┤
                                                │
T1/T2 A half-primaries → A node → 10 MOS ───────┤
T1/T2 C half-primaries → C node → 10 MOS ───────┤
                                                ↓
                                                B
                                                ↓
                                      7-device BAT- MOS bank
                                                ↓
                                               BAT-

T1 + T2 magnetic transformation                 ← X1
↓
series/collective secondary formation
↓
HV bridge rectifier
↓
BUS+ / BUS-
↓
HV DC-link                                       ← passive X2-capable node
↓
HV inverter                                      ← X3
↓
AC
```

---

## 8. Current mapping for loss analysis

Define actual transformer center-tap/winding feed currents:

```text
i_T1(t)
i_T2(t)
```

During a stable A-side conduction interval:

```text
i_A,total(t) ≈ i_T1,A(t) + i_T2,A(t)
```

During a stable C-side conduction interval:

```text
i_C,total(t) ≈ i_T1,C(t) + i_T2,C(t)
```

But:

```text
i_DA1 != i_T1 in general
i_DA2 != i_T2 in general
```

because DA1/DA2 are parallel switch subgroups on the same A drain/source power nodes.

Similarly:

```text
i_DB1 + i_DB2 = i_C,total
```

while subgroup current division depends on hot silicon and interconnect/gate-drive parasitics.

During dead-time/commutation, Coss/body-diode/leakage/clamp currents invalidate a simple current-sum model unless synchronous high-bandwidth waveform evidence is available.

---

## 9. Anchor-current references

Primary anchor:

```text
Vin  = 12 V
Pout = 2 kW
```

Ideal source current:

```text
Iin,ideal = 166.7 A
```

95% scaling reference:

```text
Iin ≈ 175.4 A
```

Ideal equal T1/T2 average sharing reference only:

```text
I_T1 ≈ 87.7 A
I_T2 ≈ 87.7 A
```

Ideal four-fuse-per-feed average reference only:

```text
I_fuse ≈ 21.9 A
```

These are scaling references, not measured RMS currents.

---

## 10. Updated main-MOS conduction bound

12 V MOS population:

```text
CSD18542KCS
RDS(on),max @ VGS=10 V = 4 mOhm
```

With ten connected devices per logical switch:

```text
R_A,eq,25C,max ≈ 0.400 mOhm
R_C,eq,25C,max ≈ 0.400 mOhm
```

Using the same simplified alternating 50%-per-side / 175.4 A sensitivity model:

```text
P_mainMOS,cond,25C-bound
≈ 0.5 I^2 (R_A + R_C)
≈ 12.3 W
```

Status:

```text
DATASHEET BOUND / NOT MEASURED
```

This excludes hot RDS(on), dynamic current, package/contact/copper resistance and switching/commutation loss.

---

## 11. BAT→X1 loss equation

The physical boundary must include both source and return paths:

```text
P_A0,BAT→X1 =
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
  + P_negativeSeriesBank
```

Do not combine different evidence classes into a claimed measured total.

---

## 12. Current loss-budget table

| Region | Current boundary | Loss model | Evidence status |
|---|---|---|---|
| BAT+ common distribution | multi-terminal source/fuse currents | `Σ I_k ΔV_k` / geometry model | `PARTIAL GEOMETRY BOUND` |
| 2 × four-fuse banks | individual fuse current | `Σ I_fuse ΔV_fuse` | `MEASUREMENT NEEDED` |
| T1/T2 local feed + J8 | `I_T1`, `I_T2` | `I ΔV` | `PARTIAL GEOMETRY / J8 OPEN` |
| A logical switch / 10 MOS | `i_A,total` | `avg(v_A-B i_A)` | `DYNAMIC MEASUREMENT NEEDED` |
| C logical switch / 10 MOS | `i_C,total` | `avg(v_C-B i_C)` | `DYNAMIC MEASUREMENT NEEDED` |
| T1/T2 primary | transformer winding current | copper + core | `Rac / fs / flux NEEDED` |
| B return copper | source-return current | `I²R` / `IΔV` | `MEASUREMENT NEEDED` |
| 7-device BAT- MOS bank | source current | `I ΔV` preferred | `REGION VERIFIED / LOSS BOUND` |
| X1→rectifier | secondary current | copper + diode/commutation | `WAVEFORM NEEDED` |

---

## 13. What is verified

```text
two separately fused center-tap feeds
local LV bulk at both feeds
both transformer A ends share one power node
both transformer C ends share one power node
A node has 10 connected MOS drains
C node has 10 connected MOS drains
all 20 main MOS sources connect to B
Q19 physical connectivity is verified
four local drivers are paired into two logical commands by 0R links
secondary series junction and HV bridge rectifier exist
negative-side seven-MOS full-current region exists
post-BUS X3 exists
```

---

## 14. What remains open

```text
dominant A0 loss bucket
actual source/T1/T2 RMS and ripple
subgroup current sharing DA1↔DA2 / DB1↔DB2
exact fs / duty / dead time
actual A/C switching loss
hot fuse/contact/J8 loss
B return copper loss
T1/T2 Rac/core loss
source 100/120 Hz ripple
active X2 value
candidate superiority
novelty
```

---

## 15. Gate decision

Current order remains:

```text
A0 distribution + dynamic loss measurement
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized HFT
↓
X1 mechanism comparison
↓
X2 Buffer OFF/ON
↓
Candidate topology synthesis only if a physical gap survives
```

Formal status:

```text
A0 topology/current graph      = SUBSTANTIALLY RECONSTRUCTED
Q19 anomaly                    = RESOLVED
A0 numerical loss budget       = OPEN
A1                             = BLOCKED UNTIL A0 LOSS LOCALIZATION
Candidate superiority          = NOT ESTABLISHED
Novelty                        = NOT ESTABLISHED
```

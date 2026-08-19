# 08 — Decision Log

Purpose: preserve why a research direction was kept, narrowed, corrected, or rejected.

This file records research decisions, not final truth. Later evidence may reverse a decision; newer dated corrections supersede older abstractions without erasing the reasoning history available in Git history and the detailed research records.

---

## 2026-08-16 — Research focus fixed

```text
Focus = low-voltage high-current DC→single-phase AC loss/topology study
Anchor = 12 V / 2 kW / ~166.7 A ideal
```

Reason: milliohm-scale resistance is first-order at hundred-ampere current.

## 2026-08-16 — UPS/BESS system function not the topic

```text
UPS/BESS system function = NOT FOCUS
local bidirectional energy exchange = KEEP AS MECHANISM
```

## 2026-08-16 — Electric-field remains candidate mechanism

Rejected assumption:

```text
remove HFT → automatically lower loss
```

Capacitive/electric-field transfer must still pay ESR/dielectric, reactive/circulating VA, switching, balancing, common-mode and isolation/EMI costs.

## 2026-08-16 — Broad novelty claims closed

Do not claim novelty from IPOS/modularization, CPT, bidirectional buffer, APD/PPB, partial power, HF-link buffer, single-stage inversion, or direct HFL alone.

```text
OPEN_INTERSECTION
NOVELTY_NOT_ESTABLISHED
```

## 2026-08-17 — Research envelope generalized

```text
12–24 Vdc / 1–3 kW / 220 Vac / 1φ
```

Keep 12 V / 2 kW as the extreme-current anchor.

## 2026-08-17 — Nine-family taxonomy retained

Use nine main power-path families. Modular/IPOS/current sharing/matrix/capacitive isolation/active buffer/partial power/soft switching are orthogonal dimensions unless a genuinely different main energy path is demonstrated.

## 2026-08-17 — Loss-Driven Topology Synthesis fixed

```text
Loss mechanism
→ current/energy path
→ structural constraint
→ topology candidate
```

Mandatory rule:

```text
P_saved > P_added
```

## 2026-08-17 — Validation order fixed

```text
PLECS
→ LTspice
→ Maxwell/Q3D
→ hardware validation
```

---

## 2026-08-19 — Working architecture retained

```text
12 V source
→ very-short / very-low-R common LV path
→ local bulk + HF decoupling
→ early distributed branch power cells
→ branch switching + X1
→ reduced-current domain
→ [optional active X2]
→ X3
→ 220 Vac
```

Important:

```text
X1/X2/X3 = functional coordinates, not one component each.
```

Status:

```text
very-short common path = KEEP
local decoupling = KEEP
early fan-out = HYPOTHESIS
branch switching + X1 = CORE RESEARCH REGION
active X2 = OPTIONAL / NOT PROVEN
X3 after X1 = KEEP
```

## 2026-08-19 — ASP-2000 promoted to A0 real-product benchmark

```text
ASP-2000 R52 = A0 REAL-PRODUCT BENCHMARK
```

Parallel MOS, multiple HFTs, current sharing, early distribution and secondary voltage combination cannot be credited as candidate novelty.

## 2026-08-19 — Magnetic benchmark split A0 / A1

```text
A0 = actual ASP product
A1 = fair optimized magnetic HFT
```

A1 receives equivalent current-distribution, silicon-paralleling, gate-drive and packaging freedom.

## 2026-08-19 — Early fan-out not assumed loss-saving

Splitting current alone does not guarantee lower total I²R.

```text
P_common + ΣP_branch + P_added < matched baseline
```

must be demonstrated.

## 2026-08-19 — Active X2 remains optional

Required later ablation:

```text
Buffer OFF vs Buffer ON
P_LV,saved > P_X2,added
```

## 2026-08-19 — Four-independent-bank abstraction rejected

SchDoc established two separate center-tap feeds but shared primary-end nodes:

```text
BAT+
├─ 4-fuse feed → T1 center tap
└─ 4-fuse feed → T2 center tap

T1 A = T2 A
T1 C = T2 C
```

Thus `4 × independent five-MOS converter branches` was rejected as an electrical model.

## 2026-08-19 — BAT+ distribution became first-order loss bucket

Nominal PCB geometry model:

```text
R_BAT+,common ≈ 0.249 mΩ
P @175.4 A ≈ 7.67 W

partial positive PCB-only:
R_eq ≈ 0.373 mΩ
P ≈ 11.5 W
```

Status `GEOMETRY_MODEL / NOT_MEASURED`.

## 2026-08-19 — T2 J8 external-link boundary identified

```text
external high-current link intent = STRONGLY_SUPPORTED
exact conductor / R_J8 = OPEN / MEASUREMENT_NEEDED
```

## 2026-08-19 — Negative battery return seven-MOS region verified

```text
B
↔ Q39 Q40 Q41 Q42 Q63 Q64 Q65
↔ BAT-
```

All seven are CSD18510KCS. Datasheet-scale 25°C reference:

```text
Req≈0.243 mΩ
P@175.4 A≈7.47 W
```

Do not treat as measured loss.

## 2026-08-19 — Kelvin measurement promoted ahead of A1

Static high-current regions are to be closed by:

```text
current + segment mV drop + temperature
```

Priority: BAT+ distribution, fuses, T1/T2 local feeds, J8, B↔BAT- and return copper.

## 2026-08-19 — Dynamic measurement gate defined

Required:

```text
fs / duty / dead time
actual VGS
A/C switched-node voltage
T1/T2 primary current
volt-second
switching/commutation energy
```

No switching-loss integration from unsynchronized/invalid V-I boundaries.

## 2026-08-19 — Compiled PCB resolved Q19 and primary-switch architecture

```text
A node = NetC62_1
→ T1 A + T2 A
→ 10 MOS

C node = NetC65_1
→ T1 C + T2 C
→ 10 MOS

all 20 main MOS sources → B
```

Q19 Drain is verified on the A node. Old 9+10 model superseded.

Updated simplified 12 V conduction bound:

```text
R_A≈R_C≈0.400 mΩ
P_mainMOS,cond≈12.3 W
```

`DATASHEET_BOUND / NOT_MEASURED`.

## 2026-08-19 — Four physical drivers paired into two logical commands

```text
DA1 / DA2 → A node
DB1 / DB2 → C node

DR-A ─ R213=0Ω ─ DR-A2
DR-B ─ R212=0Ω ─ DR-B2
```

Decision:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched nodes
```

## 2026-08-19 — Transformer and silicon-subgroup currents separated

```text
I_T1/I_T2 = transformer feed currents
I_A,total/I_C,total = electrical switch currents
I_DA1/I_DA2/I_DB1/I_DB2 = local silicon subgroup currents
```

Stable conduction:

```text
I_A,total≈I_T1,A+I_T2,A
I_C,total≈I_T1,C+I_T2,C
```

But DA1/DA2 are not T1/T2 currents. This prevents invalid `VDS × wrong current` switching-loss calculations.

Detailed record: `research/17_ASP2000_A0_PRIMARY_SWITCH_CURRENT_BOUNDARY.md`.

---

## 2026-08-19 — Seven-MOS battery-interface function narrowed

New SchDoc trace resolves the gate and sensing architecture.

Seven devices:

```text
Q39 Q40 Q41 Q42 Q63 Q64 Q65
Source → B
Drain  → BAT-
```

Every gate is driven from common `12VP` through an individual 68.1 Ω resistor and has an individual 47.5 kΩ pull-down to `B`.

```text
12VP → 68.1Ω → Gate
Gate → 47.5kΩ → B
```

No independent MAIN-board PWM/enable command was found for the bank.

Decision:

```text
reverse-polarity / ideal-diode-style battery-interface role
= STRONGLY_SUPPORTED

commandable full battery disconnect by this bank alone
= NOT_SUPPORTED_BY_PRESENT_CIRCUIT
```

U4 (`LM2904`) directly monitors the same B↔BAT- boundary:

```text
U4 + input → B
BAT- → 1kΩ → U4 - input
22.1kΩ output feedback → - input
U4 output → 100Ω → BOCP → CN4A pin 6
```

Therefore:

```text
B↔BAT- voltage-drop sensing → BOCP = VERIFIED
BOCP over-current / abnormal-drop protection role = STRONGLY_SUPPORTED
exact BOCP threshold / polarity / control-board response = OPEN
```

Research consequence:

> The seven-MOS loss is classified primarily as battery-interface protection/sensing overhead, not intrinsic magnetic-X1 loss.

Fair comparison now uses either:

```text
Contract P — product level:
matched reverse-polarity / equivalent ideal-diode behavior + required fault/current information; count its loss.

Contract C — core converter:
exclude battery-interface overhead from A0/A1/candidate equally.
```

Forbidden:

```text
Candidate deletes Q39...Q65 functionality
→ calls the removed watts an X1/topology advantage
```

Detailed record: `research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md`.

---

## Current decision state

```text
Research phase                       = Physical Gap Validation
A0 main power graph                  = SUBSTANTIALLY_RECONSTRUCTED
Q19 anomaly                          = RESOLVED
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
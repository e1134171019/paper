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

A0 exists to prevent unfair comparison. Any candidate must be compared with the real product structure rather than a simplified fictional single-transformer / single-switch path.

Detailed follow-up records:

```text
research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
research/14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
research/16_ASP2000_A0_DYNAMIC_SWITCHING_AND_HFT_MEASUREMENT_PROTOCOL.md
research/17_ASP2000_A0_PRIMARY_SWITCH_CURRENT_BOUNDARY.md
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
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

### 2.2 BAT+ splits into two separately fused center-tap feeds

```text
BAT+
├─ F2 / F3 / F5 / F6 ─→ T1 center tap + local LV bulk
└─ F7 / F8 / F9 / F10 → T2 center tap + local LV bulk
```

Main fuse annotation:

```text
40 A / 32 V @12 V
20 A / 32 V @24 V
```

Local bulk groups include the C2…C6 and C28…C32 regions with 12 V / 24 V capacitor alternatives.

### 2.3 T1/T2 primary ends share only two high-current switched nodes

Compiled PCB connectivity establishes:

```text
A switched node = NetC62_1
C switched node = NetC65_1
common low-side return = B
```

Both transformer A ends are on `NetC62_1`.
Both transformer C ends are on `NetC65_1`.

Therefore the real primary power stage does **not** contain four electrically independent 5-MOS converter branches.

### 2.4 A-side switch function = 10 connected MOS

Compiled PCB drain connectivity:

```text
Q3 Q4 Q5 Q6 Q33
Q18 Q19 Q20 Q21 Q37
→ NetC62_1
```

All ten source pads connect to:

```text
B
```

### 2.5 C-side switch function = 10 connected MOS

Compiled PCB drain connectivity:

```text
Q11 Q12 Q13 Q14 Q36
Q24 Q25 Q26 Q27 Q38
→ NetC65_1
```

All ten source pads connect to:

```text
B
```

### 2.6 Q19 anomaly is resolved

Earlier SchDoc-only extraction made Q19 drain appear isolated.

The compiled PCB proves:

```text
Q19 Drain → NetC62_1
Q19 Source → B
```

Formal status:

```text
A-side connected MOS = 10
C-side connected MOS = 10
Total connected main LV MOS = 20
Q19 connectivity = VERIFIED IN PCB
```

The previous `Q19 drain = OPEN` statement is superseded.

### 2.7 Four physical gate-driver groups, two logical commands

Physical gate groups:

```text
DA1-G → Q3 Q4 Q5 Q6 Q33
DA2-G → Q18 Q19 Q20 Q21 Q37
DB1-G → Q11 Q12 Q13 Q14 Q36
DB2-G → Q24 Q25 Q26 Q27 Q38
```

Each device has an individual 27.4 ohm gate resistor.

Upstream control connectivity:

```text
DR-A  ─ R213 = 0 ohm ─ DR-A2
DR-B  ─ R212 = 0 ohm ─ DR-B2
```

Therefore the correct abstraction is:

```text
logical A command
→ 2 local driver subgroups
→ 10 parallel A-side MOS

logical B command
→ 2 local driver subgroups
→ 10 parallel C-side MOS
```

So A0 has:

```text
4 physical driver subgroups
2 logical switch functions
2 high-current switched primary-end nodes
```

Exact dynamic synchronization still requires waveform measurement.

### 2.8 Local E-label interpretation

SchDoc local labels:

```text
DA1-E / DB1-E / DA2-E / DB2-E
```

must not be treated as four isolated high-current source-return power nets.

Compiled PCB evidence shows:

```text
all 20 main MOS Source pads → B
low-side local driver reference devices → B
```

Thus `B` is the physical common source/return boundary for A0 loss analysis.

---

## 3. Verified X1-to-HV connectivity

### 3.1 Secondary series / collective formation

```text
T1 pin 5 = T2 pin 2
```

The outer secondary nodes feed the two high-voltage rectifier legs:

```text
T1 outer → D1/D5
T2 outer → RL1 → D2/D6
```

`RL1` exact operating role remains open.

### 3.2 HV bridge rectifier

```text
D1 pin 2 → BUS+
D2 pin 2 → BUS+
D5 pin 1 → BUS-
D6 pin 1 → BUS-
```

### 3.3 HV DC-link / X2-capable energy node

The HV region contains:

```text
C8 C11 C89 C90
= 680 uF / 315 V positions
```

Safe conclusion:

```text
HV DC-link region = VERIFIED
exact capacitor assembly topology = NOT YET VERIFIED
```

### 3.4 X3

A distinct high-voltage inverter / AC-synthesis stage exists after BUS+/BUS-.

---

## 4. Battery-negative full-current protection/sensing interface

Battery negative is not identical to the primary switching return `B`.

Seven TO-220 MOS positions bridge:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

All are annotated `CSD18510KCS`.

Direct SchDoc trace now establishes for all seven:

```text
Drain  → BAT-
Source → B
Gate   → 12VP through an individual 68.1 Ω resistor
Gate   → B through an individual 47.5 kΩ pull-down
```

There is no independent MAIN-board PWM/enable command between `12VP` and the seven gates.

The verified orientation and common gate bias are strongly consistent with a low-side reverse-polarity / ideal-diode-style battery interface rather than a commandable full battery disconnect.

The same `B ↔ BAT-` voltage is monitored by U4 (`LM2904`):

```text
U4 + input → B
U4 - input → BAT- through R153 = 1 kΩ
U4 feedback → R152 = 22.1 kΩ
U4 output → R154 = 100 Ω → BOCP → CN4A pin 6
```

Therefore:

```text
B↔BAT- voltage-drop sensing feeding BOCP = VERIFIED
reverse-polarity / ideal-diode-style function = STRONGLY SUPPORTED
over-current / abnormal-drop protection role = STRONGLY SUPPORTED
exact BOCP threshold/control-board response = OPEN
independent disconnect role of Q39...Q65 = NOT SUPPORTED BY PRESENT CIRCUIT
```

Detailed evidence:

```text
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
```

---

## 5. Revised A0 power-path abstraction

```text
BAT+
│
├─ 4× fuse bank → local bulk → T1 center tap ─┐
│                                             │
└─ 4× fuse bank → local bulk → T2 center tap ─┤
                                              │
      T1/T2 A half-primaries ─→ A node ─→ 10 MOS ─┐
      T1/T2 C half-primaries ─→ C node ─→ 10 MOS ─┤
                                                   ↓
                                                   B
                                                   ↓
                              7-device battery-interface MOS bank
                              reverse-polarity / BOCP sensing region
                                                   ↓
                                                  BAT-

T1 + T2 magnetic transformation                  ← X1
↓
series / collective secondary formation
↓
D1/D5 + D2/D6 bridge rectification
↓
BUS+ / BUS-
↓
HV DC-link                                        ← passive X2-capable node
↓
HV inverter                                       ← X3
↓
AC output
```

Classification:

```text
A0 = #02 real-product magnetic HFT benchmark
```

---

## 6. X1 / X2 / X3 mapping

```text
X1 = switched center-tapped T1/T2 magnetic transformation region
X2 reference = post-rectification HV DC-link / BUS region
X3 = post-BUS high-voltage inverter / AC-synthesis region
```

Important:

```text
existing passive DC-link != proposed active bidirectional 2ω buffer
```

A0 already follows:

```text
X1 → reduced-current/HV energy node → X3
```

---

## 7. A0 loss map

Minimum decomposition now includes both positive and negative full-current paths:

```text
battery/source impedance
→ BAT+ connector / common copper
→ 2 × four-fuse banks
→ T1/T2 local feed + J8 boundary
→ local bulk ESR / ripple
→ A/C 10-MOS switch-function conduction
→ MOS switching / Coss / gate / commutation
→ T1/T2 primary copper + core
→ secondary copper
→ leakage / clamp / snubber
→ B return copper
→ seven-device battery-interface protection/sensing bank
→ BAT-
```

The seven-MOS bank is classified primarily as product battery-interface overhead, not as the magnetic X1 conversion mechanism itself.

Post-X1 losses then include rectifier, DC-link, X3 and output-filter losses.

---

## 8. Critical research consequences

The real A0 already contains:

```text
10-way silicon paralleling per logical low-side switch
split local gate driving
multiple HFT magnetic paths
separate fused center-tap feeds
local LV energy support
shared primary-end switched nodes
collective/series secondary voltage formation
HV DC-link before X3
```

Therefore none of these alone can be credited as candidate novelty or automatic loss advantage.

A candidate must demonstrate matched improvement in quantities such as:

```text
R_common
I_common,RMS
A/C switch-region loss
primary copper/core loss
commutation/clamp loss
source 2ω RMS
P_total
```

under:

```text
P_saved > P_added
```

Battery-interface savings must be separated from X1-topology savings.

---

## 9. Required A1 comparison

A1 must be allowed equivalent structural freedom:

```text
optimized low-voltage distribution
+ matched battery-interface protection/sensing functionality
+ heavy parallel silicon
+ distributed gate driving
+ optimized magnetic X1
+ collective HV formation
+ X3
```

For product-level comparison, the matched battery interface must provide equivalent required reverse-polarity behavior and fault/current information, although the implementation may differ.

For core-converter comparison, the battery-interface overhead may be excluded only when excluded from A0, A1 and every candidate equally.

Do not compare a new modular candidate against an artificially monolithic or under-optimized HFT baseline.

---

## 10. What remains unverified

```text
exact switching frequency / duty / dead time
actual DA1-vs-DA2 and DB1-vs-DB2 dynamic timing mismatch
subgroup current sharing
exact T1/T2 turns ratio
T1/T2 current balance
fuse sharing / hot resistance
J8 conductor resistance
hot MOS RDS(on)
PCB/return Rac
transformer winding Rac / core loss
leakage/clamp processed power
RL1 operating role
source 100/120 Hz current
HV DC-link ripple
exact BOCP trip threshold / active polarity / control-board response
12VP startup/shutdown sequence
stage efficiencies / thermal map
```

---

## 11. Formal status

```text
ASP A0 main power graph                 = SUBSTANTIALLY RECONSTRUCTED
center-tap/fuse grouping                = VERIFIED
A node / 10 MOS                         = VERIFIED
C node / 10 MOS                         = VERIFIED
all main MOS sources → B                = VERIFIED
Q19 drain connectivity                  = VERIFIED IN PCB
4 local driver groups / 2 logical cmds  = VERIFIED AT CONNECTIVITY LEVEL
secondary series/rectifier graph        = VERIFIED
B↔BAT- seven-MOS boundary               = VERIFIED
12VP common gate bias                    = VERIFIED
B↔BAT- sensing → BOCP                    = VERIFIED
reverse-polarity / ideal-diode role      = STRONGLY SUPPORTED
BOCP protection interpretation           = STRONGLY SUPPORTED / EXACT RESPONSE OPEN
A0 numerical BAT→X1 loss budget         = OPEN
A0 benchmark                            = ESTABLISHED
candidate superiority                   = NOT ESTABLISHED
active X2 benefit                       = NOT ESTABLISHED
novelty                                 = NOT ESTABLISHED
```
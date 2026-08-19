# 08 — Decision Log

Purpose: preserve why a research direction was kept, narrowed, corrected or rejected. Newer dated corrections supersede older abstractions; Git history preserves the detailed previous versions.

---

## 2026-08-16 — Research focus fixed

```text
Focus = low-voltage high-current DC→single-phase AC loss/topology study
Anchor = 12 V /2 kW / ~166.7 A ideal
```

Core rule:

```text
loss mechanism → current/energy path → structural requirement → topology candidate
P_saved > P_added
```

Broad novelty claims from modularization, IPOS/current sharing, capacitive isolation, bidirectional buffering, partial power, HF-link or single-stage/direct-HFL alone are closed.

```text
Novelty = NOT_ESTABLISHED
```

---

## 2026-08-17 — Research envelope and family taxonomy fixed

```text
12–24 Vdc /1–3 kW /220 Vac /1φ
```

Nine working power-path families retained. Candidate #10 remains unassigned until a physical gap survives matched benchmarks.

Validation order:

```text
PLECS → LTspice → Maxwell/Q3D → hardware
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
→220 Vac
```

```text
early fan-out = HYPOTHESIS / not automatic loss saving
active X2 = OPTIONAL / must pass P_LV,saved > P_X2,added
```

---

## 2026-08-19 — ASP-2000 R52 promoted to A0 real-product benchmark

A0 already contains heavy MOS paralleling, multiple HFT paths, separate fused center feeds, local LV energy support, collective/series secondary formation and HV DC-link before X3.

Therefore those features alone cannot be credited as candidate novelty or automatic advantage.

A1 is defined as a fair optimized magnetic benchmark and receives equivalent engineering freedom.

---

## 2026-08-19 — Four-independent-bank abstraction rejected

Verified primary structure:

```text
BAT+
├─ four-fuse feed → T1 center tap
└─ four-fuse feed → T2 center tap

T1 A = T2 A → common A switch node
T1 C = T2 C → common C switch node
```

Thus `4 independent 5-MOS converter branches` is rejected as an electrical model.

---

## 2026-08-19 — Q19 and primary-switch architecture resolved

Compiled PCB establishes:

```text
A node →10 connected MOS →B
C node →10 connected MOS →B
Q19 Drain → A node
```

Old `9+10 / Q19 OPEN` model is superseded.

Four physical driver groups serve the two A/C power functions.

Correct current variables:

```text
I_T1/I_T2 = transformer currents
I_A,total/I_C,total = electrical switch currents
DA1/DA2/DB1/DB2 currents = local silicon-subgroup currents
```

Do not use T1/T2 current as an unquestioned proxy for one 5-MOS subgroup switching current.

---

## 2026-08-19 — Battery-negative seven-MOS region classified

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

Verified hardware:

```text
Source →B
Drain →BAT-
12VP → individual 68.1Ω →Gate
Gate → individual 47.5kΩ →B
```

Independent ASP product specification explicitly lists:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Decision:

```text
ASP input reverse-polarity function = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
Q39...Q65 ideal-diode-style implementation = STRONGLY_SUPPORTED
commandable full disconnect by this bank alone = NOT_SUPPORTED
```

This loss is battery-interface protection/sensing overhead, not intrinsic magnetic-X1 loss.

---

## 2026-08-19 — BOCP analog transfer resolved

MAIN-board U4 network is a closed-loop analog amplifier, not the earlier comparator/hysteresis interpretation.

```text
ΔV_M5 = V_B - V_BAT-
V_BOCP - V_B ≈22.1 × ΔV_M5
```

```text
BOCP transfer relation = VERIFIED_FROM_MAIN_BOARD
BOCP exact receiver/trip/control action = OPEN / EVIDENCE_BLOCKED
```

Formal benchmark loss evidence remains:

```text
I_source + ΔV_M5 + temperature
```

BOCP is a product sense-chain cross-check.

---

## 2026-08-19 — Kelvin and dynamic measurement gates defined

Static/Kelvin:

```text
M0 BAT+ distribution
M1 fuse banks
M2 T1 local feed
M3 J8
M4 T2 local feed
M5 B↔BAT− seven-MOS bank
M6 B return copper
```

Dynamic:

```text
fs / duty / dead time
actual VGS
V_A-B / V_C-B
I_T1 / I_T2
synchronous switch-region v×i
primary volt-second
```

No unsynchronized V×wrong-current switching-loss integration is accepted.

---

## 2026-08-19 — RL1 role resolved as HV precharge/soft-start bypass

Direct SchDoc graph:

```text
T2 pin5
│
├─ RL1 power contact ──────────────┐
└─ R40 1k/5W || R41 1k/5W =500Ω ─┤
                                   ↓
                            D2/D6 bridge AC node
```

RL1 identity/control:

```text
OZ-SS-112LM1
12Vdc coil
control net RELAY_SS1
```

Decision:

```text
RL1 HV-secondary precharge / soft-start bypass
= VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
```

Loss accounting:

```text
R40/R41 startup energy = inrush/precharge overhead / not ordinary steady-state X1 loss
RL1 steady contact loss = measurement item
```

---

## 2026-08-19 — Transformer parameter evidence gate tightened

R52 currently establishes only:

```text
T1/T2 = PQ5050
center-tapped primary connectivity
secondary series relationship
```

It does not provide a defensible A0 value for:

```text
populated transformer P/N
turns ratio
Lm/Lk
winding DCR/Rac
core material / Ae / Ve
```

Drive contains `M1-PQ50-V121-A` transformer test data, but model-matrix evidence associates it with `ASP-3000W-24V-200ac-S9C`, not A0.

Decision:

```text
M1-PQ50-V121-A data = CONTEXT_ONLY / DIFFERENT VARIANT
A0 transformer numerical parameters = OPEN
```

---

## 2026-08-19 — PCB copper-loss model corrected by manufacturing specification — CRITICAL

Initial PcbDoc-stack calculations used approximately 35.56 µm copper and produced an ~11.5 W partial-positive-PCB scale.

The direct R52 manufacturing specification tied to the same Gerber instead specifies:

```text
FR4
1.6mm
2 layer
base copper =2.0oz
finished copper thickness >82µm
```

Therefore:

```text
old 35.56 µm geometry-loss model = SUPERSEDED
```

Using 82 µm as the conservative minimum and the same 2D geometry:

```text
BAT+ common ≤~3.32 W @175.4A
T1 local ≤~1.17 W @87.7A
T2 PCB excl. J8 ≤~0.48 W @87.7A
partial positive PCB ≤~4.98 W
```

Research consequence:

```text
PCB distribution remains material
but is NOT proven dominant
```

---

## 2026-08-19 — Primary RC damping and U5 stuffing boundary resolved

Direct A/C adjacency establishes two passive series-RC snubber/damping branches across the primary switched nodes and no direct active recovery branch attached to those A/C nodes.

Decision:

```text
direct primary-node damping = PASSIVE / DISSIPATIVE RC STRUCTURE
P_snubber = OPEN / WAVEFORM_NEEDED
```

R52 also supports U5 buffered command distribution and direct 0Ω bypass options. The exact production stuffing of U5/R212/R213 remains open.

Therefore older wording that treated R212/R213 as definitely populated production timing links is superseded.

---

## 2026-08-19 — A0 optimization is NOT the research task — CRITICAL DIRECTION CORRECTION

A0 reverse engineering has reached the point where continued component-level tracing risks turning the work into an ASP optimization project.

Formal decision:

```text
ASP-2000 R52
= real-product benchmark / evidence source
≠ optimization target
```

A0 structural evidence is now sufficient for a physical-gap screen.

Product-engineering items are no longer independent research targets:

```text
PCB / bus / connector geometry
Fuse / J8 / contacts
battery reverse-protection / BOCP
RL1 / precharge implementation
U5 / stuffing details
exact RC snubber value tuning
```

Continue them only when they discriminate a topology-level hypothesis.

Current physical-gap hypotheses:

```text
PG-1 extreme-LV conduction exposure before X1
= HYPOTHESIS / TOPOLOGY-RELEVANT

PG-2 dissipative commutation / leakage-energy handling
= HYPOTHESIS / STRONG STRUCTURAL SIGNAL

PG-3 magnetic transformation burden at extreme ratio
= OPEN / NOT YET A GAP

PG-4 single-phase 2ω energy reflection into LV source
= HYPOTHESIS / NOT_ESTABLISHED
```

Authoritative screen:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
```

---

## 2026-08-19 — Exhaustive A0 loss closure no longer blocks mechanism comparison

The previous broad workflow:

```text
measure/close every A0 static + dynamic watt
→ only then build A1 and compare mechanisms
```

is superseded because it over-serves product characterization rather than the research question.

New minimum-evidence workflow:

```text
A0 structural evidence freeze
↓
physical-gap screen
↓
H1 PG-1 conduction discriminator
H2 PG-2 commutation/snubber discriminator
H3 PG-3 magnetic discriminator
H4 PG-4 2ω-routing discriminator
↓
A1 / Direct-HFL / non-isolated X1 mechanism comparison
↓
reject gaps that disappear under fair optimization
↓
only then topology synthesis
```

A1 is therefore no longer blocked by a requirement to fully close every ASP loss term. It begins after the minimum evidence needed to make the mechanism comparison meaningful.

Candidate #10 remains:

```text
HOLD / NOT_ASSIGNED
```

---

## Fair comparison contracts

```text
Contract P — product level
→ match reverse-polarity protection, sensing/fusing and precharge/inrush functions; count losses.

Contract C — steady-state core converter
→ exclude battery-interface overhead and startup-only precharge energy equally across all compared architectures.
```

Forbidden:

```text
candidate deletes A0 product functionality
→ calls removed watts an X1/topology advantage
```

---

## Current decision state

```text
Research phase                         = Physical Gap Validation
A0 role                                = REAL-PRODUCT EVIDENCE / NOT OPTIMIZATION TARGET
A0 structural reverse engineering      = SUFFICIENT_FOR_GAP_SCREEN
R52 finished copper                    = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm geometry-loss model       = SUPERSEDED
partial positive PCB geometry bound    = ≤~4.98 W / NOT_MEASURED
main-MOS conduction scale              = ~12.3 W / DATASHEET_BOUND
battery-interface scale                = ~7.47 W / PRODUCT-INTERFACE DATASHEET_BOUND
A/C passive RC damping                 = VERIFIED
A0 transformer numerical parameters    = OPEN
PG-1                                   = HYPOTHESIS
PG-2                                   = HYPOTHESIS / STRONG SIGNAL
PG-3                                   = OPEN
PG-4                                   = HYPOTHESIS
A1                                     = NEXT AFTER MINIMUM H1-H4 EVIDENCE
Early fan-out benefit                  = NOT_PROVEN
Active X2 benefit                      = NOT_PROVEN
Candidate #10                          = HOLD / NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

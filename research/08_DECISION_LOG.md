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

Four physical driver groups are paired into two logical commands:

```text
DA1 + DA2 → A function
DB1 + DB2 → C function
DR-A ↔ DR-A2 through 0Ω
DR-B ↔ DR-B2 through 0Ω
```

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

R52 coordinate export and layout image also expose only `PQ5050`; no populated production P/N has been recovered from current R52 files.

---

## 2026-08-19 — PCB copper-loss model corrected by manufacturing specification — CRITICAL

### Superseded assumption

Initial geometry calculations used PcbDoc stack metadata:

```text
Top ≈35.56 µm
Bottom ≈35.56 µm
R_sheet,1layer≈0.485 mΩ/square
```

This produced:

```text
BAT+ common ≈0.249 mΩ /≈7.67 W @175.4A
T1 local ≈0.351 mΩ /≈2.70 W @87.7A
T2 PCB excl. J8 ≈0.144 mΩ /≈1.10 W @87.7A
partial positive PCB ≈0.373 mΩ /≈11.5 W
```

Those values are now:

```text
SUPERSEDED_BY_R52_MANUFACTURING_SPEC
```

### New authoritative manufacturing evidence

`PB-2200-0038-D_R52_231206_PCB製作規格.xlsx`, tied to the same R52 Gerber, specifies:

```text
FR4
1.6mm
2 layer
base copper =2.0oz
finished copper thickness >82µm
```

Decision:

```text
R52 finished copper >82µm
= AUTHORITATIVE AS-BUILT MANUFACTURING BOUND
```

Using 82µm as the conservative minimum and rescaling the same 2D geometry:

```text
R_sheet,1layer,max≈0.210 mΩ/square
R_sheet,2layer,ideal,max≈0.105 mΩ/square

BAT+ common:
R≤~0.108 mΩ
P@175.4A≤~3.32 W

T1 local:
R≤~0.152 mΩ
P@87.7A≤~1.17 W

T2 PCB excl. J8:
R≤~0.0624 mΩ
P@87.7A≤~0.48 W

partial positive PCB:
R_eq≤~0.162 mΩ
P@175.4A≤~4.98 W
```

Research consequence:

```text
OLD conclusion:
common PCB copper ~ entire main-MOS conduction bucket

CURRENT conclusion:
PCB distribution remains material but is substantially smaller than the old stack-based model; main MOS / protection interface / contacts / fuses / J8 / HFT must not be ranked before measurement.
```

The architecture requirement `very-short common LV path` remains physically sensible, but its quantitative justification is weaker than previously stated.

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
A0 main power/current graph            = SUBSTANTIALLY_RECONSTRUCTED
A logical switch                       = 10 MOS / VERIFIED
C logical switch                       = 10 MOS / VERIFIED
4 drivers /2 logical commands          = VERIFIED_AT_CONNECTIVITY_LEVEL
R52 finished copper                    = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm geometry-loss model       = SUPERSEDED
BAT+ common geometry bound             = ≤~3.32 W / NOT_MEASURED
partial positive PCB geometry bound    = ≤~4.98 W / NOT_MEASURED
ASP reverse-polarity function          = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
BOCP analog gain                       = ~22.1 V/V / VERIFIED_FROM_MAIN_BOARD
RL1 precharge/bypass role              = VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
A0 transformer populated P/N           = OPEN
A0 transformer numerical parameters    = OPEN
M1-PQ50-V121-A data                     = CONTEXT_ONLY
A0 measured distribution loss          = OPEN
A0 dynamic switch/HFT loss             = OPEN
A0 total BAT→X1 loss                   = OPEN
A1 matched model                       = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
Early fan-out benefit                  = NOT_PROVEN
Active X2 benefit                      = NOT_PROVEN
Candidate #10                          = NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

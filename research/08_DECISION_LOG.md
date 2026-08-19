# 08 — Decision Log

Purpose: preserve why a research direction was kept, narrowed, corrected, or rejected.

This file records research decisions, not final truth. Later evidence may reverse a decision; newer dated corrections supersede older abstractions without erasing the reasoning history.

---

## 2026-08-16 — Research focus fixed

```text
Focus = low-voltage high-current DC→single-phase AC loss/topology study
Anchor = 12 V / 2 kW / ~166.7 A ideal
```

Reason: at hundred-ampere current, milliohm-scale resistance is a first-order loss term. Current path / RMS exposure is therefore more important than voltage-gain labels alone.

---

## 2026-08-16 — UPS/BESS function is not the topic

```text
UPS/BESS system function = NOT FOCUS
local bidirectional energy exchange = KEEP AS MECHANISM
```

Use terms such as `Bidirectional Energy Buffer` / `Bidirectional Power-Decoupling Port` only when discussing local energy routing.

---

## 2026-08-16 — Electric-field remains a candidate mechanism

Rejected assumption:

```text
remove HFT → automatically lower loss
```

Electric-field/capacitive transfer must still pay capacitor ESR/dielectric loss, reactive/circulating VA, switching, balancing, common-mode and isolation/EMI costs.

---

## 2026-08-16 — Broad novelty claims closed

Do not claim novelty from any one of:

```text
IPOS / modularization
CPT / capacitive isolation
bidirectional buffer
APD / PPB
partial power
HF-link buffer
single-stage inverter
direct HFL DC–AC
```

Current status remains:

```text
OPEN_INTERSECTION
NOVELTY_NOT_ESTABLISHED
```

---

## 2026-08-17 — Research envelope generalized

```text
12–24 Vdc / 1–3 kW / 220 Vac / 1φ
```

Keep `12 V / 2 kW` as the primary extreme-current stress anchor.

---

## 2026-08-17 — Nine-family working taxonomy retained

Use nine main power-path families. Treat modular/IPOS/current sharing/matrix/capacitive isolation/active buffer/partial power/soft switching as orthogonal dimensions rather than automatic new families.

Direct HFL remains a required modern benchmark.

---

## 2026-08-17 — Loss-Driven Topology Synthesis defined

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

---

## 2026-08-17 — Validation order fixed

```text
PLECS first
LTspice second
Maxwell/Q3D third
hardware validation
```

System-level mechanism validation precedes detailed topology/device optimization.

---

## 2026-08-19 — Current working architecture retained

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
X1 / X2 / X3 are functional coordinates,
not one component each and not automatically three converter stages.
```

Status:

```text
very-short common path  = KEEP
local decoupling        = KEEP
early fan-out           = HYPOTHESIS
branch switching + X1   = CORE RESEARCH REGION
active X2               = OPTIONAL / NOT PROVEN
X3 after X1             = KEEP
```

---

## 2026-08-19 — ASP-2000 R52 promoted to A0 real-product benchmark

Decision:

```text
ASP-2000 R52 = A0 REAL-PRODUCT BENCHMARK
```

Real product evidence includes two PQ5050 HFTs, extensive low-side silicon paralleling, eight main input fuses, local LV bulk, HV rectification, HV DC-link and post-bus AC synthesis.

Consequence: `parallel MOS`, `multiple HFT`, `current sharing`, `early distribution`, and `secondary voltage combination` cannot be credited as candidate novelty.

---

## 2026-08-19 — Magnetic benchmark split into A0 and A1

```text
A0 = actual ASP product
A1 = fair optimized magnetic HFT
```

A1 must be allowed equivalent current-distribution, silicon-paralleling, gate-drive and packaging freedom. Reject comparison against an artificially monolithic HFT baseline.

---

## 2026-08-19 — Early fan-out is not assumed loss-saving

Current splitting alone does not guarantee lower total I²R if conductor resources are merely divided, and added branches add gate/Coss/parasitic/control burden.

Required gate:

```text
P_common + ΣP_branch + P_added
< matched baseline
```

---

## 2026-08-19 — Active X2 remains optional

Required ablation:

```text
Buffer OFF
vs
Buffer ON
```

Go condition:

```text
P_LV,saved > P_X2,added
```

If the passive post-X1 DC-link already suppresses source 2ω sufficiently, active X2 must be removed or restructured.

---

## 2026-08-19 — ASP net-level reconstruction superseded the four-independent-bank abstraction

SchDoc reconstruction established:

```text
BAT+
├─ 4-fuse feed → T1 center tap
└─ 4-fuse feed → T2 center tap

T1 A = T2 A
T1 C = T2 C
```

Therefore the earlier spatial description `4 × independent five-MOS converter branches` was rejected as an electrical model.

---

## 2026-08-19 — BAT+ distribution geometry became a first-order loss bucket

PcbDoc copper extraction established a nominal geometry bound:

```text
R_BAT+,common ≈ 0.249 mΩ
P @ 175.4 A ≈ 7.67 W
```

Partial positive PCB-only model including local feed geometry:

```text
R_eq,positive-PCB,partial ≈ 0.373 mΩ
P @ 175.4 A ≈ 11.5 W
```

Status:

```text
GEOMETRY MODEL / NOT MEASURED
```

Research consequence: low-voltage distribution is a topology/packaging variable, not a layout afterthought.

---

## 2026-08-19 — T2 contains a J8 external-link boundary

Two same-net J8 terminals are separated by ~93 mm without an ordinary reconstructed PCB polygon spanning the full gap.

Decision:

```text
external high-current link intent = STRONGLY SUPPORTED
exact physical conductor = OPEN
R_J8 = MEASUREMENT_NEEDED
```

Do not guess the assembly conductor resistance.

---

## 2026-08-19 — Negative battery return contains a seven-device full-current MOS region

Verified boundary:

```text
B
↔ Q39 Q40 Q41 Q42 Q63 Q64 Q65
↔ BAT-
```

All seven are annotated `CSD18510KCS`.

25°C datasheet boundary:

```text
7 ideal parallel devices → R_eq ≈ 0.243 mΩ
175.4 A scaling → ≈ 7.47 W
```

Critical benchmark rule:

> A candidate may not create a false efficiency advantage by deleting protection/disconnect functionality that A0 must provide.

---

## 2026-08-19 — Kelvin / millivolt-drop measurement promoted ahead of A1

Static high-current regions should be closed by:

```text
current + segment mV drop + temperature
```

rather than extending uncertain geometry assumptions.

Priority regions include BAT+ distribution, individual fuses, T1/T2 local feeds, J8, B↔BAT- and return copper.

---

## 2026-08-19 — Dynamic measurement gate defined

Dynamic closure requires:

```text
fs / duty / dead time
actual device VGS
A/C switched-node voltage
T1/T2 primary current
volt-second
switching/commutation energy
```

Do not calculate switching loss from unsynchronized V/I channels or an invalid current boundary.

---

## 2026-08-19 — Compiled PCB resolves Q19 and the real primary-switch architecture

New compiled-PCB evidence establishes:

```text
A node = NetC62_1
→ T1 A + T2 A
→ Q3 Q4 Q5 Q6 Q33
→ Q18 Q19 Q20 Q21 Q37
→ 10 connected MOS total

C node = NetC65_1
→ T1 C + T2 C
→ Q11 Q12 Q13 Q14 Q36
→ Q24 Q25 Q26 Q27 Q38
→ 10 connected MOS total

all 20 main MOS sources → B
```

Therefore:

```text
Q19 drain connectivity = VERIFIED IN PCB
```

The previous `Q19 OPEN / 9+10 MOS` abstraction is superseded.

Updated 12 V conduction sensitivity bound:

```text
10 A-side + 10 C-side
R_A ≈ R_C ≈ 0.400 mΩ @ 25C/max datasheet boundary
P_mainMOS,cond ≈ 12.3 W under the same simplified 175.4 A / 50%-per-side model
```

---

## 2026-08-19 — Four physical driver groups are paired into two logical switch commands

Physical groups:

```text
DA1 / DA2 → A power node
DB1 / DB2 → C power node
```

Control trace:

```text
DR-A  ─ R213 = 0R ─ DR-A2
DR-B  ─ R212 = 0R ─ DR-B2
```

Decision:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched primary-end nodes
```

This is now the formal A0 primary-switch model.

Dynamic timing mismatch between the two local drivers under one command remains a measurement item.

---

## 2026-08-19 — Transformer current and MOS subgroup current are separated conceptually

Correct variables:

```text
I_T1 / I_T2
= transformer center-tap / winding-feed currents

I_A,total / I_C,total
= currents through the two electrical switch functions

I_DA1 / I_DA2 / I_DB1 / I_DB2
= local silicon subgroup currents
```

During stable conduction:

```text
I_A,total ≈ I_T1,A + I_T2,A
I_C,total ≈ I_T1,C + I_T2,C
```

But in general:

```text
I_DA1 != I_T1
I_DA2 != I_T2
```

because DA1/DA2 are parallel on the same A drain/source nodes. The same applies to DB1/DB2 on C.

This correction prevents invalid `VDS × wrong current` switching-loss calculations.

Detailed record:

```text
research/17_ASP2000_A0_PRIMARY_SWITCH_CURRENT_BOUNDARY.md
```

---

## Current decision state

```text
Research phase                    = Physical Gap Validation
A0 main power graph               = SUBSTANTIALLY RECONSTRUCTED
Q19 anomaly                       = RESOLVED
A logical switch                  = 10 MOS / VERIFIED
C logical switch                  = 10 MOS / VERIFIED
4 drivers / 2 logical commands    = VERIFIED AT CONNECTIVITY LEVEL
positive PCB geometry loss bound  = ESTABLISHED / NOT MEASURED
negative series MOS region        = VERIFIED / BOUND ESTABLISHED
A0 measured distribution loss     = OPEN
A0 dynamic switch loss            = OPEN
A0 total BAT→X1 loss              = OPEN
A1 matched model                  = BLOCKED UNTIL A0 LOSS LOCALIZATION
Working architecture              = KEEP
Early fan-out benefit             = NOT PROVEN
Active X2 benefit                 = NOT PROVEN
Candidate #10                     = NOT ASSIGNED
Novelty                           = NOT ESTABLISHED
```

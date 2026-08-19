# 08 — Decision Log

Purpose: preserve why a research direction was kept, narrowed, corrected, or rejected.

This file records research decisions, not final truth. Later evidence may reverse a decision; corrections supersede earlier abstractions without erasing the audit trail.

---

## 2026-08-16 — Research focus fixed

```text
Focus = low-voltage high-current DC→single-phase AC loss/topology study
Anchor = 12 V / 2 kW / ~166.7 A ideal
```

Reason: milliohm-scale resistance is already material at this current, so current path/RMS exposure matters more than voltage-gain labels alone.

---

## 2026-08-16 — UPS/BESS function is not the topic

```text
UPS/BESS system function = NOT FOCUS
local bidirectional energy exchange = KEEP AS MECHANISM
```

Working terms:

```text
Bidirectional Energy Buffer
Bidirectional Power-Decoupling Port
```

---

## 2026-08-16 — Electric-field remains a candidate mechanism

Rejected assumption:

```text
remove HFT → automatically lower loss
```

Electric-field/capacitive transfer must account for capacitor ESR/dielectric loss, reactive/circulating VA, extra switches, balancing, common-mode and isolation/EMI burden.

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

Current narrow intersection remains:

```text
OPEN_INTERSECTION
NOVELTY_NOT_ESTABLISHED
```

---

## 2026-08-17 — Research envelope generalized

```text
12–24 Vdc / 1–3 kW / 220 Vac / 1φ
```

Keep `12 V / 2 kW` as the extreme-current stress anchor.

---

## 2026-08-17 — Nine-family working taxonomy retained

Use nine main power-path families. Treat modular/IPOS/current-sharing/matrix/capacitive-isolation/active-buffer/partial-power/soft-switching as orthogonal design dimensions rather than automatic new families.

Direct HFL remains a required modern benchmark; Xi'an-type HFL + power-decoupling work is not a new ninth-family origin.

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
hardware last
```

System-level mechanism validation precedes detailed device/transient optimization.

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

Important correction:

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

Initial component/stage extraction established two PQ5050 HFT modules, extensive parallel low-side MOS silicon, eight main input fuse positions, local low-voltage bulk, HV rectification, HV DC-link and a post-bus inverter.

Decision:

```text
ASP-2000 R52 = A0 REAL-PRODUCT BENCHMARK
```

Consequence: parallel MOS, multiple magnetic paths and current sharing cannot be credited as candidate novelty or automatic efficiency advantage.

---

## 2026-08-19 — Magnetic benchmark split into A0 and A1

```text
A0 = actual ASP product
A1 = fair optimized magnetic HFT
```

A1 must be allowed equivalent current-distribution/layout freedom. Reject comparison of a new modular candidate against an artificially monolithic HFT baseline.

---

## 2026-08-19 — Early fan-out is not assumed loss-saving

Splitting current into N branches does not automatically reduce total copper loss if conductor resources are merely divided, while added branches increase gate/Coss/parasitic/control/circulation burden.

Required gate:

```text
P_common + ΣP_branch + P_gate/Coss/parasitic
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

If the passive HV DC-link already suppresses source 2ω sufficiently, active X2 is rejected or restructured.

---

## 2026-08-19 — ASP net-level reconstruction supersedes the four-independent-bank abstraction

New direct SchDoc net reconstruction establishes:

```text
BAT+
├─ F2/F3/F5/F6 → local bulk → T1 center tap B
└─ F7/F8/F9/F10 → local bulk → T2 center tap B

T1 A = T2 A → shared A-side paralleled MOS switching node
T1 C = T2 C → shared C-side paralleled MOS switching node
```

Therefore the earlier spatial description:

```text
4 × independent five-MOS banks
```

is **superseded** as an electrical model.

More accurate interpretation:

```text
two separately fused/local-bulk center-tap HFT feeds
+ two shared high-parallel-count A/C switching nodes
```

MOS extraction status:

```text
20 annotated positions
19 expected power connections directly reconstructed
Q19 drain appears isolated in SchDoc
Q19 footprint exists in PcbDoc
Q19 drain connectivity = OPEN / requires deeper PCB-BOM-assembly verification
```

The secondary graph also establishes:

```text
T1 pin5 = T2 pin2                    ← direct series junction
T1 outer → D1/D5 rectifier leg
T2 outer → RL1 → D2/D6 rectifier leg
D1,D2 → BUS+
D5,D6 → BUS-
```

Research consequence:

> A0 already combines current sharing, multiple magnetic paths, and collective/series secondary voltage formation. A new candidate must beat this real structure, not a simplified #02 cartoon.

Detailed records:

```text
research/10_ASP2000_PRODUCT_BASELINE.md
research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
```

---

## 2026-08-19 — A0 numerical loss localization becomes the immediate gate

Do not jump directly from connectivity reconstruction to a new topology.

First quantify/bound:

```text
P_common
P_fuse
P_local_interconnect
P_bulk_ESR
P_MOS,cond
P_MOS,sw
P_primary,Cu
P_core
P_commutation/clamp
```

for the `BAT→X1` boundary.

Only loss mechanisms that remain material after a fair A1 optimized-HFT model justify replacing X1 with another physical mechanism.

Current order:

```text
A0 loss localization
↓
A1 optimized HFT
↓
X1 mechanism comparison
↓
X2 Buffer OFF/ON
↓
Candidate topology synthesis
```

---

## 2026-08-19 — BAT+ PCB distribution receives a geometry-based loss bound

Direct PcbDoc primitive reconstruction establishes:

```text
BAT+ connector
→ Top/Bottom large copper polygons
→ 8 main fuse-input pads
```

with sixteen BAT+ stitching vias in the local distribution region.

A nominal-copper 2D sheet model, using the extracted 1.4 mil Top/Bottom copper stack and equal current per fuse as the balanced reference, gives:

```text
R_BAT+,common,geometry ≈ 0.249 mΩ
P @ 175.4 A ≈ 7.67 W
```

Adding the modeled post-fuse PCB portions gives a partial positive-path PCB-only equivalent:

```text
R_eq,positive-PCB,partial ≈ 0.373 mΩ
P @ 175.4 A ≈ 11.5 W
```

Status:

```text
GEOMETRY_MODEL / NOT MEASURED
```

This does not include connector/contact, fuse-element, hot-copper, solder reinforcement or the T2 external-link resistance.

Research consequence:

> ordinary low-voltage power distribution can already consume a material fraction of the 0.65 mΩ / 20 W research budget before main MOS/HFT conversion loss is counted.

---

## 2026-08-19 — T2 local feed contains an external-link boundary

PcbDoc reconstruction shows two large same-net `J8` terminals separated by approximately 93 mm, with no ordinary reconstructed PCB polygon spanning the complete gap.

Decision:

```text
external high-current link intent = STRONGLY SUPPORTED
exact J8 conductor implementation = OPEN
R_J8 = MEASUREMENT_NEEDED
```

Do not substitute a guessed copper-wire/busbar resistance for the physical assembly.

---

## 2026-08-19 — Negative battery return contains a seven-device full-current MOS bank

Direct SchDoc/PcbDoc reconstruction establishes that battery negative and the main low-side switching return `B` are separated by seven TO-220 MOS positions:

```text
Q39 Q40 Q41 Q42 Q63 Q64 Q65
```

All seven are annotated `CSD18510KCS`.

Verified electrical boundary:

```text
BAT−
↔ seven-device MOS bank
↔ B main low-side return
```

The exact protection/disconnect/control role remains open.

Using the official 1.7 mΩ maximum `RDS(on)` @ 10 V as a datasheet boundary:

```text
7 ideal parallel devices → R_eq ≈ 0.243 mΩ
175.4 A continuous-enhancement scaling → ≈ 7.47 W
```

Status:

```text
full-current series MOS region = VERIFIED
dissipation value = DATASHEET_BOUND / NOT MEASURED
```

Critical benchmark rule:

> A candidate may not claim a topology loss advantage by deleting a required protection/disconnect function that exists in A0. Equivalent product functionality must be matched or removed from both comparison boundaries.

Detailed distribution/measurement gate:

```text
research/14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
```

---

## 2026-08-19 — Kelvin/millivolt-drop measurement promoted ahead of A1

The geometry model is now sufficient to identify priority measurements but not to close the A0 loss budget.

Next gate:

```text
segmented Kelvin / millivolt-drop measurement
```

Priority segments:

```text
BAT+ → each fuse input
individual fuse input→output
T1 local feed
J8 external link
T2 local feed
BAT− ↔ B across Q39...Q65
B-return distribution
```

Reason:

At mΩ-class resistance and ~175 A, small layout/contact/protection resistances produce multi-watt losses. Direct `I × ΔV` measurement is more defensible than extending the PCB geometry model into unknown assembly elements.

---

## Current decision state

```text
A0 main power graph             = SUBSTANTIALLY RECONSTRUCTED
A0 positive PCB geometry model  = ESTABLISHED AS NON-MEASURED BOUND
A0 negative series MOS region   = VERIFIED / LOSS BOUND ESTABLISHED
A0 measured distribution loss   = OPEN
A0 numerical loss budget        = OPEN
A1 matched model                = BLOCKED UNTIL A0 DISTRIBUTION BOUNDS / MEASUREMENT
Working architecture            = KEEP
Early fan-out benefit           = NOT PROVEN
Active X2 benefit               = NOT PROVEN
Candidate #10                   = NOT ASSIGNED
Novelty                         = NOT ESTABLISHED
```

# 08 — Decision Log

Purpose: preserve why a research direction was kept, narrowed, or rejected.

This file records research decisions, not final truth. Later evidence may reverse a decision.

---

## 2026-08-16 — Research state consolidated

Decision:

```text
Focus = low-voltage high-current DC→single-phase AC loss/topology study
```

Primary anchor:

```text
12 V / 2 kW / ~166.7 A ideal
```

Reason:

At this operating point, milliohm-scale common-path resistance is already a material loss term, so topology must be evaluated through current path and RMS exposure rather than voltage-gain capability alone.

---

## 2026-08-16 — UPS/BUS is not the research topic

Decision:

```text
UPS/BESS system function = NOT FOCUS
local bidirectional energy exchange = KEEP AS MECHANISM
```

Reason:

The useful idea is local energy absorption/return, especially for single-phase 2ω power pulsation. Generic bidirectional bus and storage architectures are established prior art.

---

## 2026-08-16 — “Adaptive” clarified

Decision:

The intended adaptive behavior is not AI/ML or adaptive modulation.

Working meaning:

```text
UPS-like bidirectional energy compensation
```

Use terms:

```text
Bidirectional Energy Buffer
Bidirectional Power-Decoupling Port
```

---

## 2026-08-16 — Electric-field remains candidate, not conclusion

Decision:

```text
Electric-field / capacitive isolation = CANDIDATE MECHANISM
```

Rejected assumption:

```text
remove HFT → automatically lower loss
```

Reason:

Loss may migrate to capacitor ESR/dielectric loss, resonant/circulating RMS, extra switching, balancing, common-mode and isolation/EMI burden.

---

## 2026-08-16 — Broad novelty claims closed

Do not claim novelty from any one of:

```text
IPOS
CPT / capacitive isolation
bidirectional buffer
APD / PPB
partial power
HF-link buffer
single-stage inverter
high-frequency-link direct AC
```

Reason:

Each has substantial prior art. Only a narrower physical intersection may remain.

---

## 2026-08-16 — Candidate research intersection narrowed

Working intersection:

```text
12–24 V
+ 1–3 kW
+ 220 Vac / 1φ
+ electric-field/capacitive main conversion
+ intentional bidirectional 2ω energy routing
+ low-side RMS / total-loss objective
```

Status:

```text
OPEN_INTERSECTION
NOVELTY_NOT_ESTABLISHED
```

---

## 2026-08-17 — Research envelope generalized

Updated general envelope:

```text
12–24 Vdc / 1–3 kW / 220 Vac / 1φ
```

Keep:

```text
12 V / 2 kW
```

as primary extreme-current stress anchor.

Reason:

The wider envelope allows scaling/crossover analysis while preserving a concrete high-current design point.

---

## 2026-08-17 — Topology taxonomy recalibrated

Decision:

Use nine working main power-path families.

Treat the following as orthogonal design dimensions rather than automatic new numbered families:

```text
IPOS / modular
matrix connection
capacitive isolation
current sharing
active buffer
partial power
soft switching
```

The Xi'an high-frequency-link work is a #09 direct-HFL benchmark, not the historical origin of a “ninth topology.”

---

## 2026-08-17 — Xi'an line promoted to required benchmark

Decision:

```text
Conventional HFT two-stage alone is not enough as benchmark.
```

Required benchmark classes:

```text
A. HFT + Rectifier + HV Bus + VSI
B. Direct High-Frequency-Link DC–AC
C. Candidate electric-field/energy-routing architecture
```

Reason:

Modern direct-HFL work already removes the complete rectifier/HV-bus/VSI chain and can integrate AC-side 2ω decoupling. A candidate that only beats the conventional two-stage architecture may still be weak against closer prior art.

---

## 2026-08-17 — Loss-driven topology wording defined

Working method name:

```text
Loss-Oriented / Loss-Driven Topology Synthesis
```

Meaning:

```text
Loss mechanism
→ current/energy path causing it
→ structural constraint
→ topology candidate
```

Rule:

> Every added branch/component must identify which loss it reduces and prove that saved loss exceeds added loss.

---

## 2026-08-17 — First validation tool selected

Decision:

```text
PLECS first
LTspice second
Maxwell/Q3D third
```

Initial PLECS gate:

```text
idealized impedance transformation
+ single-phase inverter
+ Buffer OFF/ON comparison
```

Measure:

```text
I_LV,RMS
I_2ω
P_saved from declared R_LV
P_buffer added
```

Only after the mechanism passes should the transformation block be replaced by a specific electric-field network.

---

## 2026-08-19 — Current working architecture retained

Decision:

```text
KEEP current working architecture
```

Working structure:

```text
12 V source
→ very-short / very-low-R common LV path
→ local bulk + HF decoupling
→ early distributed branch power cells
→ branch switching + X1
→ reduced-current domain
→ [optional active X2 2ω buffer]
→ X3
→ 220 Vac
```

Important correction:

```text
X1 / X2 / X3 are functional coordinates,
not automatically three added converter stages.
```

Status by region:

```text
very-short common path      = KEEP / physical requirement
local decoupling            = KEEP / engineering requirement
early fan-out               = KEEP AS HYPOTHESIS
branch switching + X1       = CORE RESEARCH REGION
reduced-current node        = KEEP AS FUNCTIONAL CONCEPT
active X2 buffer            = OPTIONAL / NOT YET PROVEN
X3 after X1                 = KEEP / structural requirement
```

Reason:

The ordering is retained because it attempts to place each necessary RMS / energy component in a less expensive voltage-current domain, while preserving the rule:

```text
P_saved > P_added
```

Detailed added-loss audit:

```text
research/11_WORKING_ARCHITECTURE_LOSS_AUDIT.md
```

---

## 2026-08-19 — ASP-2000 R52 promoted from abstract #02 to A0 product baseline

Decision:

```text
ASP-2000 R52 = A0 REAL-PRODUCT BENCHMARK
```

Direct component/stage extraction from the user-supplied Altium schematic establishes:

```text
2 × PQ5050 HFT modules
4 × low-side switch banks
5 parallel LV MOS devices per bank
20 LV main MOS positions total
8 high-current input fuse positions
2 groups of LV bulk capacitance
4 HV rectifier devices
HV DC-link capacitor region
separate HV AC-synthesis stage
```

Research consequence:

```text
parallel MOS
current sharing
multiple HFT paths
early current distribution
```

are already present in the real product and therefore cannot be credited as candidate novelty or automatic loss advantage.

Detailed baseline:

```text
research/10_ASP2000_PRODUCT_BASELINE.md
```

---

## 2026-08-19 — Magnetic benchmark split into A0 and A1

Decision:

```text
A0 = actual ASP-2000 product abstraction
A1 = fair optimized modular-HFT benchmark
```

A1 must be allowed the same current-distribution freedom as any new N-branch candidate:

```text
12 V short bus
→ N-way fan-out
→ N × [switching + HFT X1]
→ HV combine / rectification
→ reduced-current node
→ X3
```

Rejected comparison:

```text
new modular candidate
vs
artificially monolithic HFT benchmark
```

Reason:

A topology claim is only meaningful if the alternative X1 mechanism still produces a benefit after magnetic conversion is optimized under a matched structural boundary.

---

## 2026-08-19 — Early fan-out benefit is no longer assumed

Decision:

```text
early fan-out = design hypothesis, not efficiency conclusion
```

Reason:

Splitting current into N branches does not automatically reduce total copper loss if total conductor cross-section is unchanged, and additional branches increase gate-drive, Coss/Qoss, parasitic mismatch, control, and possible circulating-current burden.

Required gate:

```text
P_common + ΣP_branch + P_gate/Coss/parasitic
must be lower than the matched baseline
```

---

## 2026-08-19 — Active X2 remains optional

Decision:

```text
active post-X1 2ω buffer = OPTIONAL / MUST PASS ABLATION
```

Do not add it merely because post-X1 placement is physically attractive.

Required comparison:

```text
Buffer OFF
vs
Buffer ON
```

Go condition:

```text
P_LV,saved > P_X2,added
```

If the existing passive HV DC-link already suppresses source 2ω sufficiently, the active X2 must be rejected or restructured.

---

## Current next decision

Pending results:

```text
1. Where is A0 ASP loss actually concentrated from battery to X1?
2. Does early current distribution reduce total loss versus A0 and fair A1?
3. Which X1 class gives the lowest total matched loss?
4. Does post-X1 active 2ω buffering produce positive net loss benefit?
```

Current comparison classes:

```text
A0 — actual ASP-2000 R52 product
A1 — optimized modular HFT
B  — Direct HFL
C  — non-isolated current-distribution / high-gain
D  — working candidate architecture
```

If candidate changes do not satisfy:

```text
P_saved > P_added
```

stop or reframe rather than preserving the preferred architecture by assumption.

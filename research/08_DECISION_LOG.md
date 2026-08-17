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

Previous working state centered on:

```text
12 V / 1–2 kW
```

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

Important correction:

The Xi'an high-frequency-link work is not “a ninth topology invented by Xi'an.” Direct high-frequency-link DC–AC was already present in the previous taxonomy. The updated nine-family map is a cleaner decomposition of main power paths.

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

Not a claimed established topology name and not itself a novelty contribution.

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

Reason:

First question is system-level energy routing and RMS/loss benefit, not semiconductor transient detail.

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

## Current next decision

Pending result:

```text
Does local HV-side / post-X1 2ω buffering produce a positive net loss benefit
across 12–24 V and 1–3 kW after declared buffer losses?
```

If yes:

```text
proceed to candidate topology synthesis
```

If no:

```text
reframe the research around the actual dominant low-voltage loss/stress boundary
```

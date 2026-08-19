# 07 — Benchmarks

Status date: 2026-08-19  
Purpose: define fair reference architectures before claiming improvement

## 1. Benchmark rule

Benchmark is not selected to make the candidate look better.

All comparisons must match or explicitly bound:

```text
Vin
Pout
Vout
power-flow direction
isolation requirement
load point
semiconductor technology class
switching-frequency scope
thermal boundary
auxiliary-loss policy
battery-interface protection/sensing functionality
measurement basis
```

Core rule:

```text
P_saved > P_added
```

Two contracts remain valid:

```text
Contract P — product level
→ match required protection/sensing/precharge/product functions and count their loss

Contract C — core converter
→ exclude product-interface/startup-only overhead equally
```

A0 ASP-2000 is a real-product evidence source, **not an optimization target**.

Authoritative research-problem screen:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
```

---

## 2. Benchmark A — magnetic HFT class

Working family:

```text
#02 HFT + Rectifier + HV DC Bus + VSI
```

### A0 — ASP-2000 R52 real-product baseline

Current structural abstraction:

```text
BAT+
├─ four-fuse/local-bulk feed → T1 center tap
└─ four-fuse/local-bulk feed → T2 center tap

T1-A + T2-A → common A node → 10 parallel MOS → B
T1-C + T2-C → common C node → 10 parallel MOS → B

B
↓
7-MOS battery-interface protection/sensing region
↓
BAT-

T1/T2 magnetic transformation                    ← X1
↓
secondary collective/series voltage formation
↓
HV rectification
↓
HV DC-link                                        ← passive X2-capable node
↓
HV inverter                                       ← X3
↓
AC
```

A0 also contains:

```text
manufactured finished copper >82 µm
4 local main-gate driver subgroups / 2 logical A-C functions
passive A↔C RC snubber/damping network
HV precharge/bypass function
```

Important classification:

```text
PCB / fuse / J8 / connector / protection / BOCP / precharge / driver stuffing
= product-engineering evidence unless needed to discriminate a physical-gap hypothesis
```

A0 is not assumed inefficient.

### A1 — fair optimized magnetic benchmark

A1 may use equivalent engineering freedom:

```text
short/heavy LV distribution
optimized silicon paralleling
optimized local gate drive
optimized magnetic X1
appropriate soft-commutation/clamp strategy
collective HV formation
reduced-current node
X3
```

A1 exists to answer:

> If magnetic X1 receives fair optimization under the same specification and product contract, which A0-derived physical gaps remain?

A1 is **not** an ASP repair project. It is a mechanism-level reference model.

---

## 3. Benchmark B — Direct High-Frequency-Link DC–AC

Working family:

```text
#09 Direct High-Frequency-Link DC–AC
```

Typical path:

```text
LV DC
→ HF switching / HFT link
→ bidirectional matrix / cycloconverter
→ AC
```

Potentially removed functions:

```text
full HV rectifier
complete HV DC bus
separate VSI
```

But it must count added:

```text
bidirectional-switch conduction
HF circulating RMS
commutation burden
AC-side energy decoupling if used
```

Removed stages are not automatically a win.

---

## 4. Benchmark C — Non-Isolated High-Gain / Current-Distribution

Working family:

```text
#04 Non-Isolated High-Gain DC/DC + VSI
```

Fair form:

```text
12 V short bus
→ current distribution
→ high-gain / coupled-L / switched network X1
→ collective HV node
→ X3
```

Must count:

```text
LV conduction/switching
inductor/coupled-inductor copper/core
leakage/clamp
rectifier/diode loss
capacitor ESR/charge redistribution
internal circulating current
```

Direct 12 V / 2 kW / ~400 V evidence remains incomplete; use bounded comparisons rather than unsupported ranking.

---

## 5. Candidate D — HOLD

Previous working architecture remains a hypothesis:

```text
12–24 Vdc
→ very-short common LV path
→ local decoupling
→ early distribution
→ branch switching + candidate X1
→ reduced-current domain
→ [optional X2]
→ X3
→ 220 Vac
```

But:

```text
Candidate #10 = HOLD / NOT_ASSIGNED
```

No topology synthesis is active until a physical gap survives comparison with existing families.

---

## 6. Current physical-gap axes

The benchmark is now driven by four A0-derived research hypotheses rather than by an exhaustive ASP component audit.

```text
PG-1 — extreme-LV conduction exposure before X1
PG-2 — dissipative commutation / leakage-energy handling
PG-3 — magnetic transformation burden at extreme ratio
PG-4 — 2ω energy reflected into the LV source path
```

Status:

```text
PG-1 = HYPOTHESIS / TOPOLOGY-RELEVANT
PG-2 = HYPOTHESIS / STRONG STRUCTURAL SIGNAL
PG-3 = OPEN / NOT YET A GAP
PG-4 = HYPOTHESIS / NOT_ESTABLISHED
```

Detailed authority:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
```

---

## 7. Fair mechanism-comparison matrix

All A1/B/C comparisons should expose at least:

```text
M1 — extreme-LV RMS / conduction exposure before X1
M2 — switching / commutation / dissipative-clamp energy
M3 — magnetic or alternative energy-storage/conversion burden
M4 — internal circulating / reactive RMS
M5 — source-side 2ω reflection
M6 — added active processing functions / stages
M7 — matched isolation / protection / product contract
```

A scalar efficiency number without decomposition is insufficient to explain a physical gap.

---

## 8. Minimum A0 evidence before mechanism comparison

Do **not** require every ASP watt to be closed first.

Collect only hypothesis-discriminating evidence:

```text
H1 / PG-1
→ source/transformer/switch current + hot conduction evidence

H2 / PG-2
→ fs/duty/deadtime + A/C V-I overlap + RC-snubber watts

H3 / PG-3
→ T1/T2 RMS + volt-second + magnetic parameter/loss bound

H4 / PG-4
→ source 100/120 Hz ripple + HV-link ripple
```

If a PG is falsified early, stop spending A0 effort on that direction.

---

## 9. Current benchmark gate — REVISED

Old broad workflow:

```text
close every A0 static + dynamic watt
→ then begin mechanism comparison
```

is superseded.

Current workflow:

```text
A0 structural evidence freeze
↓
Physical-gap screen
↓
minimum H1–H4 discriminating evidence
↓
A1 optimized magnetic / B Direct-HFL / C non-isolated mechanism comparison
↓
reject gaps that disappear under fair optimization
↓
only then topology synthesis
↓
Candidate #10 only if an existing-family solution does not already close the surviving gap
```

Formal status:

```text
A0 role = EVIDENCE SOURCE / NOT OPTIMIZATION TARGET
A1 = NEXT FAIR MAGNETIC MECHANISM BENCHMARK AFTER MINIMUM EVIDENCE
B/C = REQUIRED CROSS-MECHANISM REFERENCES
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
```

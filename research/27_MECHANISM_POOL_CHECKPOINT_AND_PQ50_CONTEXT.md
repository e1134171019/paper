# 27 — Mechanism Pool Checkpoint + PQ50 Context Evidence

Status date: 2026-08-19  
Role: `PHYSICAL-GAP VALIDATION / MECHANISM-COMBINATION CHECKPOINT`  
Research object: `PG-1...PG-4 × EXISTING-MECHANISM SCREEN`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This checkpoint records the transition from:

```text
nine-family taxonomy
→ mechanism extraction
→ mechanism pool
```

without prematurely entering topology synthesis.

Authoritative detailed matrix:

```text
research/26_NINE_FAMILY_MECHANISM_EXTRACTION_MATRIX.md
```

Core rule remains:

```text
loss mechanism
→ current/energy path
→ physical gap
→ existing-method falsification
→ only then topology synthesis

P_saved > P_added
```

---

## 2. Current physical-gap hypotheses

```text
PG-1 — extreme-LV conduction / RMS exposure before X1
       = HYPOTHESIS / TOPOLOGY-RELEVANT

PG-2 — dissipative commutation / leakage / Coss energy handling
       = HYPOTHESIS / STRONG STRUCTURAL SIGNAL

PG-3 — transformation-element burden at extreme conversion ratio
       = OPEN / NOT YET A GAP

PG-4 — single-phase 2ω energy reflection into the LV source
       = HYPOTHESIS / NOT_ESTABLISHED
```

No mechanism may be added to a candidate merely because it is a known high-performance technique. It must address a surviving PG under a matched loss boundary.

---

## 3. Mechanism pools admitted for screening

### MP-A — Early X1 / leave the extreme-LV domain early

Sources:

```text
#02 HFT
#03 Active-HFT / DAB
#04 Non-Isolated High-Gain
#09 Direct HFL
```

Primary PG:

```text
PG-1
```

Risk:

```text
earlier voltage rise may still add switching, magnetics, circulation or charge-transfer loss
```

### MP-B — Soft commutation / leakage-energy utilization

Sources:

```text
#02 resonant / soft-switched HFT variants
#03 DAB / active-HFT
```

Primary PG:

```text
PG-2
```

Required comparison:

```text
saved switching / snubber energy
vs
added resonant / circulating RMS + gate/control loss
```

### MP-C — Collective high-voltage building

Sources:

```text
#04 high-gain / multiplier
#08 switched-capacitor / multilevel
```

Primary PGs:

```text
PG-1 / PG-3
```

Required comparison:

```text
removed magnetic / low-side exposure
vs
inductor / diode / capacitor / charge-redistribution loss
```

### MP-D — Direct / integrated AC synthesis

Sources:

```text
#06 single-stage boost/buck-boost inverter
#08 multilevel / switched-capacitor
#09 direct HFL
```

Purpose:

```text
reduce or relocate post-X1 conversion boundaries
```

Required comparison:

```text
removed rectifier / full-DC-link / VSI loss
vs
boost / multilevel / matrix-commutation burden
```

### MP-E — Intentional 2ω energy routing

Sources:

```text
#02 passive HV-link storage
#05 bidirectional buffer / ripple port
#09 AC-side / HFL-integrated decoupling
```

Primary PG:

```text
PG-4
```

Hard gate:

```text
DO NOT ADD unless PG-4 survives H4 measurement / fair benchmark.
```

### MP-F — Continuous-input / ripple-current shaping

Sources:

```text
selected #04 interleaved/high-gain variants
selected #07 qZ-source variants
```

Primary PG contribution:

```text
PG-1 source-RMS / ripple component
```

Required comparison:

```text
reduced source ripple
vs
added inductor / circulating current / magnetic loss
```

---

## 4. Mechanisms not admitted merely by name

The following are NOT independent research-gap solutions and may not enter combination screening by label alone:

```text
more MOS in parallel
fan-out by itself
interleaving by itself
LLC label by itself
DAB label by itself
high-gain label by itself
switched-capacitor label by itself
remove HV DC bus by itself
active X2 before PG-4 survives
```

Rule:

```text
technique name ≠ physical-gap solution
```

---

## 5. Combination gate

Every future mechanism combination must satisfy:

```text
C1 — each mechanism maps to a surviving PG
C2 — do not stack two mechanisms that only duplicate one function while adding loss
C3 — actual circuit graph must be physically compatible
C4 — quantify new RMS / circulating / commutation burden
C5 — P_saved > P_added
C6 — reclassify the completed circuit graph against #01...#09
C7 — if it reasonably belongs to an existing family, it is not Candidate #10
C8 — discuss #10 only if the physical gap survives and existing families cannot reasonably describe the resulting main energy path
```

Current next research action:

```text
PG × Mechanism compatibility screen
↓
reject redundant / physically conflicting / loss-stacking pairs
↓
retain only 2–3 mechanism combinations with a defensible physical reason
↓
reclassify each against #01...#09
```

---

## 6. M1-PQ50-V108-A — context evidence only

A user-supplied private approval sheet for `M1-PQ50-V108-A` provides useful industrial PQ50-class magnetic context.

Only abstracted structural evidence is recorded here; the raw approval PDF is NOT committed.

Approval-sheet evidence:

```text
Part No. = M1-PQ50-V108-A
Customer = source-company manufacturing context

low-voltage foil windings:
N1 = 4 turns, 6 mil × 28 mm copper foil
N2 = 4 turns, 6 mil × 28 mm copper foil
N4 = 4 turns, 6 mil × 28 mm copper foil
N5 = 4 turns, 6 mil × 28 mm copper foil

secondary:
N3 = 30 turns

core assembly:
No Gap

secondary-side test data:
inductance samples = 6.62 mH / 7.69 mH
leakage inductance samples = 4.15 µH / 4.17 µH
secondary DCR samples = 38.6 mΩ / 38.9 mΩ
core-material options include DMR95 / DP95 MnZn ferrite
```

Research interpretation:

```text
- demonstrates a real PQ50-class transfer-type HFT using very-low-turn, wide-foil low-voltage windings;
- supports the physical reality behind PG-1 extreme-LV copper/current burden;
- demonstrates nonzero leakage as a real magnetic design quantity relevant to PG-2;
- provides context for PG-3 magnetic-burden comparisons.
```

Critical boundary:

```text
M1-PQ50-V108-A ≠ established ASP-2000 R52 T1/T2 part number
```

Therefore these numerical values are:

```text
PQ50-CLASS CONTEXT EVIDENCE
NOT A0 NUMERICAL EVIDENCE
```

Do not substitute its turns ratio, L, Lk, DCR or core material into the ASP-2000 A0 loss model without direct part-number linkage.

---

## 7. Decision state

```text
Nine-family taxonomy             = KEEP
Mechanism extraction             = COMPLETE v1
Mechanism pool MP-A...MP-F       = ESTABLISHED FOR SCREENING
PG × Mechanism compatibility     = NEXT
Mechanism combination            = NOT YET EXECUTED
Candidate #10                    = HOLD / NOT_ASSIGNED
Novelty                          = NOT_ESTABLISHED
A0 ASP role                      = EVIDENCE SOURCE / NOT OPTIMIZATION TARGET
M1-PQ50-V108-A                   = CONTEXT_ONLY / NOT A0
```

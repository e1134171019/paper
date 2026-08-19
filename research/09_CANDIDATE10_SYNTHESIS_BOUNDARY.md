# 09 — Candidate #10 Topology-Synthesis Boundary

Status date: 2026-08-19  
Status: `HOLD — PHYSICAL GAP VALIDATION FIRST`  
Novelty: `NOT_ESTABLISHED`

## 0. Supersession / workflow correction

This file preserves the previously defined candidate search boundary, but **topology synthesis is not the current research action**.

Current authority:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
research/RESEARCH_STATE.md
```

Current sequence:

```text
A0 structural evidence freeze
↓
physical-gap screen
↓
minimum hypothesis-discriminating evidence
↓
A1 / Direct-HFL / non-isolated mechanism comparison
↓
only if a gap survives
→ resume Candidate #10 synthesis
```

Therefore every previous statement in this file that says "next action = synthesize Block ⑥" is now dormant until the physical-gap gate is passed.

---

## 1. Research target retained

```text
12–24 Vdc
→ low-voltage / high-current power conversion
→ 220 Vac / 1φ
→ 1–3 kW
```

Primary anchor:

```text
12 V / 2 kW
I_in,ideal ≈166.7 A
```

The purpose is not to rename a known topology as #10.

```text
Candidate #10 = NOT_ASSIGNED
```

---

## 2. Dormant working front-end boundary

The previous working synthesis boundary remains available as a hypothesis if synthesis is later re-opened:

```text
① 12 V Battery
↓
② very-short / very-low-R Main LV Bus
↓
③ local Bulk + MLCC decoupling
↓
④ early fan-out into N branches
↓
⑤ branch MOS switching cells
↓
⑥ candidate common transformation / AC-synthesis mechanism
↓
⑦ 220 Vac / 1φ
```

Important corrections:

```text
fan-out = design dimension / NOT proven benefit
N = optimization variable / NOT fixed research truth
MOS cells = switching elements / NOT automatically X1
Block ⑥ = only a future search region, not a presumed new family
```

The earlier N=4 reference was only a synthesis convenience and is not a formal optimum.

---

## 3. What remains valid from the earlier boundary

### Common LV region

```text
P_common = I_common,RMS² R_common
```

At extreme-LV input, common series impedance must remain small. This is a physical constraint, not a novelty claim.

### Local decoupling

Bulk/MLCC are shunt/local energy-storage elements, not series devices that divide the source average current.

### Fan-out

Splitting current alone does not automatically reduce total I²R. It is retained only if equivalent conduction/commutation loss falls after added hardware is counted.

### Candidate mechanism

If synthesis later resumes, the mechanism must simultaneously address:

```text
voltage/current-domain transformation
AC synthesis or compatible downstream synthesis
collective branch-energy handling
loss reduction under the same declared boundary
```

---

## 4. Relation to the nine-family taxonomy

Every future candidate graph must still be classified against:

```text
#01 Low-Frequency Transformer Inverter
#02 HFT + Rectifier + HV DC Bus + VSI
#03 Active-HFT / DAB + VSI
#04 Non-Isolated High-Gain DC/DC + VSI
#05 Bidirectional DC/DC + VSI
#06 Single-Stage Boost/Buck-Boost Inverter
#07 Z/qZ-source
#08 Switched-Capacitor / Multilevel Main Path
#09 Direct High-Frequency-Link DC–AC
```

Examples:

```text
branch MOS → HFT → Rectifier → HV Bus → VSI
= #02

branch MOS → high-gain DC/DC → HV Bus → VSI
= #04

branch MOS → HF link → matrix/cycloconverter
= #09
```

A new family can only be discussed if the main energy path is materially different and cannot reasonably be described as #01–#09.

---

## 5. New prerequisite — a physical gap must survive

Candidate synthesis may resume only if at least one of the current research hypotheses survives fair comparison:

```text
PG-1 — extreme-LV conduction exposure before X1
PG-2 — dissipative commutation / leakage-energy handling
PG-3 — magnetic transformation burden at extreme ratio
PG-4 — 2ω energy reflected into the LV source path
```

And the proposed mechanism must show:

```text
P_saved > P_added
```

relative to a fair existing-family benchmark.

If A1 / #03 / #04 / #09 can close the gap with known architecture, Candidate #10 is unnecessary.

---

## 6. Future candidate loss gate

If synthesis is reopened, every graph must still expose:

```text
I_common,RMS
I_branch,RMS
I_MOS,RMS
I_circulating,RMS
P_MOS,cond
P_MOS,sw
P_interconnect
P_magnetic if present
P_cap / dielectric / redistribution
P_rectification if present
P_resonant / circulating
P_buffer if present
P_total
```

No structural novelty claim is retained unless the same-spec total loss/mechanism evidence survives A1/B/C comparison.

---

## 7. Current formal status

```text
Working front-end concept = RETAINED AS DORMANT HYPOTHESIS
Early fan-out benefit = NOT_PROVEN
N = NOT_FIXED
Block ⑥ = UNRESOLVED / NOT ACTIVE
Candidate #10 = HOLD / NOT_ASSIGNED
Topology synthesis = BLOCKED_BY_PHYSICAL_GAP_GATE
Novelty = NOT_ESTABLISHED
```

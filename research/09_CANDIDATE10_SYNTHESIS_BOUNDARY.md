# 09 — Candidate #10 Topology-Synthesis Boundary

Status date: 2026-08-17
Status: `TOPOLOGY_SYNTHESIS / HYPOTHESIS`
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This document freezes the front-end boundary for the next topology-synthesis stage.

The research target remains:

```text
12–24 Vdc
→ low-voltage / high-current power conversion
→ 220 Vac / 1φ
→ 1–3 kW
```

Primary stress anchor:

```text
12 V / 2 kW
I_in,ideal = 2000 / 12 ≈ 166.7 A
```

The purpose is not to rename a known topology as “#10.” The front end below is fixed only to prevent repeated redesign of the already-understood low-voltage current-distribution region. The actual Candidate #10 search is confined to Block ⑥.

---

## 2. Fixed seven-block boundary

```text
① 12 V Battery
        ↓
② Main LV Bus
   共用低壓主母線
   ← carries the full ~166.7 A ideal average current before fan-out
        ↓
③ Bulk + MLCC on the LV bus / local power nodes
   ← shunt energy-storage / impedance-control elements, not a series power path
        ↓
④ Immediate parallel fan-out into N branches
   ← 166.7 A → N lower-current branches
        ↓
⑤ One MOS switching cell per branch
   ← converts branch DC energy into controllable high-frequency switched energy
        ↓
⑥ NEW COMMON BOOST / AC-SYNTHESIS NETWORK
   ← Candidate #10 search region
        ↓
⑦ 220 Vac / 1φ
```

For the first synthesis pass, use:

```text
N = 4
```

as a reference architecture, not as a final optimum.

Ideal equal sharing at 12 V / 2 kW gives:

```text
I_bus,avg   ≈ 166.7 A
I_branch,avg ≈ 166.7 / 4 ≈ 41.7 A per branch
P_branch     ≈ 500 W per branch
```

Real input current must later use measured / declared efficiency:

```text
I_in = P_out / (V_in η)
```

---

## 3. Main LV Bus decision

Decision:

```text
Use one extremely-low-impedance Main LV Bus
and fan out as early as practical.
```

Do **not** create N independent VBUS stages merely for naming or symmetry.

Preferred physical interpretation:

```text
12 V Battery
   ↓
very short / low-R common current region
   ↓
fan-out point
 ┌──────┬──────┬──────┬──────┐
 ↓      ↓      ↓      ↓
P1     P2     P3     P4
```

The common path before fan-out is expensive because:

```text
P_common = I_common,RMS² R_common
```

At 166.7 A:

```text
1 mΩ → ~27.8 W
0.1 mΩ → ~2.78 W
```

Therefore the common hundred-ampere region should be physically short, wide, low-inductance, and low-resistance.

---

## 4. “Local VBUS” terminology corrected

Previous discussion used “N local VBUS” as a shorthand. This is now narrowed.

Use:

```text
Main LV Bus + N Local Power Nodes
```

rather than:

```text
N independent VBUS
```

unless future circuitry actually creates independently controlled or electrically separated DC buses.

If all branches are hard-connected to the same 12 V source:

```text
V_P1 ≈ V_P2 ≈ ... ≈ V_PN ≈ 12 V
```

then they are local power-distribution nodes of the same bus, not separate electrical buses.

This avoids adding unnecessary series impedance or an unnecessary intermediate conversion stage before the MOS cells.

---

## 5. Bulk capacitor and MLCC placement

Bulk capacitors and MLCCs are not placed in series with the 166.7 A average power path.

Correct interpretation:

```text
Main LV Bus+
   │
   ├── Bulk capacitor ──┐
   ├── MLCC bank ───────┤
   ├── Branch 1 → MOS   │
   ├── Branch 2 → MOS   │
   ├── Branch 3 → MOS   │
   └── Branch 4 → MOS   │
                        │
Main LV Bus− ───────────┘
```

Preferred implementation for high-frequency current localization:

```text
Main LV Bus
   ↓
fan-out
   ├→ Local Bulk + Local MLCC → MOS Cell 1
   ├→ Local Bulk + Local MLCC → MOS Cell 2
   ├→ Local Bulk + Local MLCC → MOS Cell 3
   └→ Local Bulk + Local MLCC → MOS Cell 4
```

Role separation:

```text
Battery / Main LV Bus
→ average real power

Bulk capacitor
→ lower-frequency local bus support / pulse-energy support

Local MLCC
→ switching-frequency and commutation-current localization
```

MLCC does not divide the 166.7 A average DC current and does not eliminate the battery’s average-current requirement.

---

## 6. MOS-cell role fixed

Each branch contains a MOS switching cell.

The MOS cell is responsible for:

```text
branch DC energy
→ controllable high-frequency switched voltage/current
```

The MOS itself is **not** X1.

Definition retained:

```text
X1 = first major impedance / voltage transformation
```

For Candidate #10 synthesis, X1 is located inside or is integrated with Block ⑥.

The four MOS branches may later use interleaving, current sharing, or parallel semiconductor devices, but those are design dimensions and do not create a new topology family by themselves.

---

## 7. ASP benchmark relation

ASP remains the real-product magnetic benchmark.

Its low-voltage engineering principle is useful:

```text
low-voltage high-current source
→ early current sharing / multiple MOS power paths
→ high-frequency magnetic transformation
→ rectification
→ high-voltage DC bus
→ inverter
→ 220 Vac
```

The Candidate #10 front end intentionally keeps the useful low-voltage principle:

```text
early distribute the hundred-ampere current
```

but Block ⑥ must not automatically copy ASP’s:

```text
HFT → Rectifier → HV DC Bus → VSI
```

if the objective is to find a genuinely different main power path.

---

## 8. Candidate #10 search region

The research variable is now confined to:

```text
N low-voltage MOS switched-energy injection branches
                  ↓
       [ Block ⑥: ????? ]
                  ↓
             220 Vac
```

Block ⑥ must simultaneously be evaluated for:

```text
1. voltage transformation
   12 V-class branch energy → >311 Vpk output capability

2. AC synthesis
   v_o(t) ≈ 311 sin(ωt) for 220 Vrms

3. collective energy combination
   N branches should cooperate through a common conversion mechanism,
   rather than simply becoming N complete independent converters unless that structure proves necessary.

4. low-voltage loss reduction
   the new mechanism must not re-create a high-R / high-RMS hundred-ampere path.
```

Working design language:

```text
Low-voltage side:
Parallel Current Acquisition / current distribution

High-voltage side:
Collective Voltage / AC Synthesis
```

These are working descriptions, not novelty claims or established topology names.

---

## 9. Relation to the nine-family taxonomy

The fixed front end does **not** create a tenth family.

The following remain known design dimensions:

```text
parallel MOS devices
multicell / modular branches
input current sharing
interleaving
local MLCC decoupling
IPOS-like organization
```

Block ⑥ must be classified against the existing nine working families after every proposed circuit graph.

Examples of immediate fallback into known families:

```text
MOS branches → HFT → Rectifier → HV Bus → VSI
= #02

MOS branches → high-gain DC/DC → HV Bus → VSI
= #04

MOS branches → single-stage boost/buck-boost AC synthesis
= #06

MOS branches → Z/qZ impedance network → inverter
= #07

MOS branches → switched-capacitor / multilevel stacking
= #08

MOS branches → HF link → cycloconverter / matrix AC stage
= #09
```

Therefore:

```text
Candidate #10 = NOT ASSIGNED
```

A new family can only be discussed if Block ⑥ creates a materially different main power / energy path that cannot be reasonably described as a variant of #01–#09.

---

## 10. Loss gate for every Block ⑥ candidate

A circuit is not retained merely because it is structurally unusual.

At minimum evaluate:

```text
I_common,RMS
I_branch,RMS
I_MOS,RMS
I_circulating,RMS
P_MOS,cond
P_MOS,sw
P_bus / interconnect
P_magnetic if present
P_cap / ESR / dielectric if present
P_resonant / circulating
P_rectification if present
P_total
```

Core rule:

```text
P_saved > P_added
```

and specifically:

```text
Total loss of Candidate #10
< fair same-spec benchmark loss
```

must eventually be demonstrated.

---

## 11. Next synthesis action

Do not redesign Blocks ①–⑤ unless evidence later invalidates them.

Next action:

```text
Enumerate physical / circuit-graph methods for combining
N MOS high-frequency branch outputs
into a high-voltage 220 Vac waveform.
```

For every candidate:

```text
A. draw actual current / energy path
B. identify voltage-gain mechanism
C. identify AC-polarity / amplitude mechanism
D. classify against #01–#09
E. reject if it is only a renamed known family
F. estimate low-side RMS and dominant added loss
G. retain only structures that remain physically plausible
```

Current formal status:

```text
Fixed front end = DECISION
Block ⑥ circuit = UNRESOLVED
Candidate #10 = NOT ASSIGNED
Novelty = NOT_ESTABLISHED
```

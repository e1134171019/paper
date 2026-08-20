# 54 — G23-A X2+X3 Shared-Storage Synthesis and Multi-Route Gate A v1

Status date: 2026-08-20  
Role: `O23 ACTUAL-GRAPH SYNTHESIS / X2-X3 INTERACTION SCREEN / PRIOR-ART GATE A`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Evidence status: `FIRST-PRINCIPLES + MULTI-ROUTE PRIOR-ART SCREEN`  
Simulation status: `NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File 53 stopped the first O13 graph because a primary bridge + HFT + secondary cycloconverter/matrix converter is an established HF-link inverter graph, and power-decoupled variants are also prior art.

File 54 therefore executes the next coordinate branch:

```text
O23 = X1 physically separate
    + X2 and X3 physically overlapping after X1 completion
```

The core question is:

> Can the unavoidable single-phase 2ω energy-storage elements themselves become load-bearing AC-synthesis voltage states, so that storage and synthesis are not implemented as two independent hardware functions?

The required sequence is:

```text
actual graph
→ X2 energy closure
→ X3 switching-state closure
→ X2/X3 interaction constraints
→ loss/stress screen
→ multi-route Gate A
→ STOP or retain
```

No PSIM is authorized unless a graph survives this file.

---

## 2. G23-A1 normalized actual graph — split-storage three-level synthesis

### 2.1 Main graph

X1 is intentionally left as a matched front-end converter that has already completed the extreme-LV current-domain transition.

```text
N0  12-V source
 |
 v
X1  matched isolated/non-isolated voltage/current-domain converter
 |
 |  majority power now in reduced-current HV domain
 v
N3  high-voltage post-X1 node p-n
 |
 |---- C1 ---- m ---- C2 ----|
 |                         |
 p                         n
 |
 +---- three-level / T-type / NPC-capable AC switching network ----+
                                                                  |
                                                         pre-filter AC node
                                                                  |
                                                               Lout/Cout
                                                                  |
                                                               220 Vac
```

Normalized storage rails:

```text
C1 between p and midpoint m
C2 between m and n
V1 = V(p)-V(m)
V2 = V(m)-V(n)
Vdc = V1 + V2
```

Coordinate assignment:

```text
X1 = upstream front end; completes before p-n rail.
X2 = energy stored in C1+C2 and intentionally cycled at 2ω.
X3 = three-level switching network uses p/m/n voltage states to synthesize AC.
```

The same physical capacitors therefore provide both:

```text
low-frequency energy buffer
+
multilevel AC voltage states
```

This is genuine X2+X3 overlap at the component/state level.

### 2.2 Generic X3 states

A full three-level bridge may select output differential voltage from a normalized set:

```text
+Vdc
+V1 or +V2    (nominally +Vdc/2)
0
-V1 or -V2    (nominally -Vdc/2)
-Vdc
```

The half-level states are redundant with respect to output voltage when `V1≈V2`, but are not redundant with respect to capacitor current.

For a given output-current sign, selecting the upper or lower half-level state can preferentially charge/discharge C1 or C2.

Therefore the switching network has two simultaneous control freedoms:

```text
1. output-voltage synthesis
2. capacitor-energy / neutral-point steering
```

This satisfies the File-52 requirement that X2 storage elements participate directly in X3 voltage-state synthesis.

---

## 3. X2 energy closure

For unity-PF single-phase output:

```text
p_out(t) = P[1 - cos(2ωt)]
```

with:

```text
P = 2000 W
f = 50 Hz
ω = 2πf
```

If X1 is controlled to process approximately constant average power `P`, then the post-X1 storage must absorb:

```text
p_buf(t) = P cos(2ωt)
```

and:

```text
dEbuf/dt = p_buf(t)
```

so:

```text
Ebuf(t) = E0 + [P/(2ω)] sin(2ωt)
```

Energy swing amplitude:

```text
E2ω,pk = P/(4πf) = 3.183 J
```

Peak-to-peak swing:

```text
E2ω,pp = 6.366 J
```

For equal split capacitors `C1=C2=C` and balanced common-mode swing:

```text
V1≈V2≈Vdc/2
```

stored energy is:

```text
EΣ = 0.5 C V1² + 0.5 C V2²
   = C Vdc² / 4
```

Therefore the required capacitor value for an allowed total-link swing from `Vmin` to `Vmax` is:

```text
C_each = 4 E2ω,pp / (Vmax² - Vmin²)
```

At `Vdc,center = 350 V`:

| allowed total-link swing | Vmin–Vmax | required C1=C2 |
|---|---:|---:|
| ±5% | 332.5–367.5 V | ~1.04 mF each |
| ±10% | 315–385 V | ~520 µF each |
| ±20% | 280–420 V | ~260 µF each |

The ±20% line is not automatically usable because of X3 voltage headroom, discussed next.

---

## 4. X2/X3 interaction constraint — modulation headroom

For 220 Vac:

```text
Vout,pk = sqrt(2) × 220 = 311.13 V
```

If the X3 bridge has no additional voltage-gain mechanism, the instantaneous available rail must satisfy:

```text
Vdc(t) >= 311.13 V
```

Ignoring control and device-drop margin, the maximum downward voltage swing around a 350-V center is only:

```text
(350 - 311.13)/350 = 11.1%
```

Thus:

```text
350-V center + ±20% buffer swing
→ impossible for full 220-Vac peak synthesis without another gain mechanism.
```

At 350 V, a ±10% swing leaves:

```text
Vmin = 315 V
```

which provides only ~1.2% ideal voltage margin above the 311.13-V AC peak.

Therefore a practical 350-V design likely needs a smaller swing and hence larger C, or a higher average link voltage.

Example at `Vdc,center = 400 V`:

```text
±10% → 360–440 V
±20% → 320–480 V
```

and split-cap values become approximately:

```text
±10% → C1=C2≈398 µF each
±20% → C1=C2≈199 µF each
```

but this buys capacitance reduction by increasing semiconductor voltage stress and switching loss exposure.

Formal interaction rule:

```text
larger X2 voltage swing
→ lower capacitance
but
→ lower X3 modulation headroom or higher required average Vdc
→ higher device voltage stress
```

This is `INTERACTION_NEW`, not a free X2+X3 synergy.

---

## 5. Current and loss implications

Under small relative Vdc ripple, the low-frequency buffer-current scale is approximately:

```text
Ibuf,pk ≈ P/Vdc
```

At 350 V:

```text
Ibuf,pk ≈ 5.71 A
Ibuf,rms,2ω ≈ 4.04 A
```

This is structurally much cheaper than processing the same pulsating power at 12 V, but the split capacitors also carry inverter rail/switching current.

Therefore:

```text
I_C,rms,total
≠ only 4.04 A
```

and must later include:

```text
2ω common-mode energy current
+ multilevel state-selection current
+ switching ripple
+ neutral-point balancing current
```

Capacitor ESR loss must be evaluated as:

```text
Pcap = I_C1,rms² ESR1 + I_C2,rms² ESR2
```

and semiconductor loss includes the additional conduction/switching associated with three-level state realization and neutral-point steering.

The main structural benefit is therefore not automatic watt reduction. It is:

```text
same split/storage capacitors
serve both X2 and X3 voltage-state functions
```

The main physical risks are:

```text
neutral-point / capacitor balancing current
extra switching-state constraint
higher semiconductor count than a 2-level VSI
higher Vdc requirement if large buffer swing is desired
capacitor RMS current and thermal density
control coupling between voltage synthesis and energy buffering
```

---

## 6. G23-A2 normalized alternate — integrated flying-capacitor PPB

A second O23 realization was screened because G23-A1 could otherwise be rejected merely as a split-link special case.

Normalized graph:

```text
post-X1 HV rail
→ flying-capacitor multilevel bridge leg(s)
→ AC output filter

flying capacitor(s):
- provide intermediate multilevel voltage states for X3
- intentionally cycle low-frequency stored energy for X2
```

The key state-level principle is:

```text
redundant states produce the same output voltage
but charge or discharge the flying capacitor differently.
```

Therefore the control can modulate FC energy without losing the requested AC voltage average.

This is a stronger X2+X3 overlap than attaching a separate auxiliary decoupling converter.

However it carries the same fundamental trade:

```text
buffer-energy swing
↔ flying-cap voltage range
↔ switch blocking-voltage requirement
↔ available output voltage states
↔ RMS/current-balancing burden
```

---

## 7. Multi-route Gate A

File 43 requires multiple independent retrieval routes. G23-A used IEEE-direct web search, Exa semantic search, and Sider/OpenAlex/Scholar routes.

### Route A — IEEE-direct / exact architecture search

Recovered close IEEE records include:

1. A. Omomo et al., “T-type NPC Inverter with Active Power Decoupling Method using Discontinuous Current Mode for Micro-Inverter,” ICRERA 2018, DOI `10.1109/ICRERA.2018.8566755`.

Structural relevance:

```text
T-type NPC inverter
+ split DC-link capacitor voltages intentionally oscillated
+ neutral-point current used for active power decoupling
+ no separate decoupling magnetic stage required
```

This directly occupies the G23-A1 functional concept: the inverter states and split capacitors jointly perform AC synthesis and 2ω power decoupling.

2. Y. Xia, J. Roy, and R. Ayyanar, “A Single Stage Common Ground Three-Level PV Inverter With Integrated Power Decoupling,” IEEE Open Journal of Power Electronics, 2020, DOI `10.1109/OJPEL.2020.3010227`.

Structural relevance:

```text
three-level inverter states
+ dynamic dc-link voltage swing
+ double-line-frequency power decoupling
+ reduced decoupling-capacitor requirement
```

This establishes that dynamic-link / three-level synthesis integration is an explicit prior-art design objective.

3. IEEE Xplore record `7468041`, “DC to single-phase AC Voltage Source Inverter with power decoupling circuit based on flying capacitor topology for PV system.”

Structural relevance:

```text
DC→single-phase AC
+ flying-capacitor-based power decoupling
```

This blocks a generic claim that using flying-capacitor storage for DC-AC 2ω decoupling is itself new.

Route-A result:

```text
G23-A1 generic split-link/NPC integration = ESTABLISHED PRIOR ART REGION
G23-A2 generic flying-capacitor decoupling = ESTABLISHED PRIOR ART REGION
```

### Route B — Exa semantic / behavior search

Exa recovered:

1. Omomo/Itoh T-type NPC work describing capacitor-voltage oscillation and neutral-point current as the power-decoupling mechanism without additional components.

2. Menzi, Weihe, Azurza Anderson, Everts, and Kolar, “Single-Phase PFC Rectifier With Integrated Flying Capacitor Power Pulsation Buffer,” IEEE Open Journal of Power Electronics, 2022, DOI `10.1109/OJPEL.2022.3221679`.

Although the demonstrated power-flow direction is AC→DC, its physical mechanism is directly relevant under bidirectional/topological duality:

```text
flying capacitor normally used for multilevel voltage synthesis
→ intentionally cycled at twice mains frequency
→ no additional power components required for PPB function
```

3. The same literature explicitly notes that redundant flying-capacitor bridge-leg states can be used to charge/discharge the FC while preserving the main converter voltage-control objective.

Route-B result:

```text
shared multilevel state + integrated power-pulsation buffer is not an unexplored mechanism.
```

### Route C — Sider / OpenAlex / Scholar cross-check

The academic search recovered established power-decoupling primitives including:

- Y. Tang, F. Blaabjerg, P. C. Loh, C. Jin, and P. Wang, “Decoupling of Fluctuating Power in Single-Phase Systems Through a Symmetrical Half-Bridge Circuit,” IEEE Transactions on Power Electronics, 2015, DOI `10.1109/TPEL.2014.2327134`.

This work uses split dc-link capacitors as ripple-energy storage and confirms that split-capacitor active decoupling is itself mature.

The same search corpus also contains extensive switched-capacitor and multilevel-inverter literature, confirming that capacitor-voltage-state steering is a mature converter mechanism rather than a new physical primitive.

Route-C result:

```text
split-capacitor power decoupling = mature
multilevel capacitor-state steering = mature
```

---

## 8. Gate-A decision

### G23-A1 — split-storage three-level/T-type/NPC

```text
STATE / ENERGY CLOSURE = PASS
X2+X3 PHYSICAL OVERLAP = REAL
GENERIC GRAPH NOVELTY = STOP
PRIOR-ART CLASS = SAME_GRAPH / NEAR_GRAPH
PSIM AS PROPOSED TOPOLOGY = NO
```

Reason:

> Intentionally oscillating split-link capacitor energy while the same three-level/NPC/T-type network synthesizes AC is already an established active-power-decoupling research direction.

### G23-A2 — flying-capacitor multilevel PPB

```text
STATE / ENERGY PRINCIPLE = PASS
X2+X3 PHYSICAL OVERLAP = REAL
GENERIC MECHANISM NOVELTY = STOP
PRIOR-ART CLASS = SAME_MECHANISM / NEAR_GRAPH
PSIM AS PROPOSED TOPOLOGY = NO
```

Reason:

> Flying capacitors used both as multilevel voltage-state elements and as twice-line-frequency power-pulsation buffers are already explicitly present in the literature.

---

## 9. What File 54 establishes physically

The failure is not that O23 is physically bad.

In fact, O23 has a sound location advantage:

```text
2ω energy processing after X1
→ ampere scale rather than ~167-A source-domain scale
```

and shared storage/synthesis can avoid a completely separate APD converter.

However the obvious implementation space is mature.

The strongest new analytical result retained from this file is the X2/X3 interaction inequality:

```text
Vdc,min >= Vout,pk
```

which couples:

```text
allowable 2ω storage-voltage swing
↔ required capacitance
↔ average rail voltage
↔ semiconductor voltage stress
```

Thus an O23 candidate cannot claim high power density merely from larger capacitor voltage swing; the voltage-stress and modulation-headroom penalty must be paid.

---

## 10. New constraints for any surviving O23 graph

Future O23 graph synthesis must satisfy all of:

```text
G23-G1
Do not propose generic split-DC-link, T-type/NPC dynamic-link APD as the contribution.

G23-G2
Do not propose generic flying-capacitor PPB / redundant-state energy buffering as the contribution.

G23-G3
X2 and X3 must share a load-bearing energy-transfer or switching edge, not merely be connected to the same DC bus.

G23-G4
The graph must preserve Vdc,min >= required AC synthesis voltage, or explicitly add and account for another gain mechanism.

G23-G5
Any capacitance reduction obtained by wider voltage swing must be charged against increased voltage stress, switching loss and control range.

G23-G6
Neutral-point / FC balancing current is INTERACTION_NEW and must be bounded before simulation.

G23-G7
No extra full-power active-decoupling converter may be hidden under an “integrated” label unless its hardware is functionally shared with X3.
```

---

## 11. Mainline decision after G23-A

Current coordinate map:

```text
G13-A standard HF-link cycloconverter
→ STOP_AS_NOVELTY / reference

G23-A1 split-link three-level integrated APD
→ STOP_AS_NOVELTY / reference

G23-A2 integrated flying-capacitor PPB
→ STOP_AS_GENERIC_MECHANISM / reference
```

O23 is not declared universally exhausted, but its two most obvious shared-storage realizations are no longer candidate directions.

The next admissible O23 search must move away from:

```text
split dc-link as buffer
flying capacitor as PPB
separate auxiliary APD converter
```

A reasonable next graph target is:

```text
G23-B = differential-storage AC synthesis
```

where two post-X1 storage-port voltages are modulated differentially so that:

```text
vout = vA - vB
```

while their common-mode stored energy carries the 2ω swing.

This is only a next search target, not a novelty claim. It must receive an exact graph and immediate Gate A before any PSIM.

Candidate #10 remains `HOLD / NOT_ASSIGNED`.  
Novelty remains `NOT_ESTABLISHED`.

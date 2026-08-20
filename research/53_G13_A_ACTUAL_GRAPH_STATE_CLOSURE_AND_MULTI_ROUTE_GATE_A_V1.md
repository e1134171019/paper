# 53 — G13-A Actual Graph, State Closure, X2 Cost and Multi-Route Gate A v1

Status date: 2026-08-20  
Role: `O13 ACTUAL-GRAPH SYNTHESIS / STATE CLOSURE / X2 COST DISCOVERY / PRIOR-ART GATE A`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Evidence status: `FIRST-PRINCIPLES + MULTI-ROUTE PRIOR-ART SCREEN`  
Simulation status: `NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`  
G13-A novelty status: `STOP_AS_NOVELTY / REFERENCE-CLASS GRAPH`

## 1. Purpose

File 52 promoted `O13 = X1+X3 with X2 separately identifiable` as the first coordinate-overlap branch to convert from a conceptual skeleton into an actual graph.

This file executes that step.

The question is not whether a high-frequency-link inverter can be drawn. The required test is:

> Can one real graph merge X1 and X3 near/after current reduction, avoid a full rectifier + stiff HV bus + independent VSI sequence, close the single-phase 2ω energy balance, and still expose a graph that is not already a known high-frequency-link / cycloconverter primitive?

The sequence is:

```text
actual graph
→ exact switching states
→ X1 completion proof
→ X3 synthesis proof
→ X2 energy closure
→ loss/stress consequences
→ multi-route Gate A
→ STOP or continue
```

No PSIM is authorized unless the graph survives this file.

---

## 2. G13-A normalized actual graph

### 2.1 Main power path

The minimum O13 graph is normalized as:

```text
N0  12-V source
 |
 |  product interface / protection
 v
N1  primary full bridge QP1...QP4
 |   produces +Vin / 0 / -Vin HF states
 v
T_HF  isolated high-frequency transformer
 |
 |  secondary terminals a,b
 |  bipolar HF voltage v_ab = ±Vs (plus zero intervals where commanded)
 v
N3  reduced-current HF-link boundary
 |
 |  secondary cycloconverter / 2×2 bidirectional matrix
 |  S_ax, S_ay, S_bx, S_by
 v
N6  bipolar PWM AC-envelope node x,y
 |
 v
Lout / Cout
 |
 v
N7  220 Vac / 50 Hz
```

Mechanism set:

```text
PM1 = magnetic flux-linkage transformation
PM7 = semiconductor switching-state AC synthesis
```

Coordinate assignment:

```text
X1 starts at QP switching / transformer excitation.
X1 completes at the secondary HF-link when majority power is in the high-voltage/reduced-current domain.
X3 overlaps X1 completion because the secondary matrix immediately converts HF-link states into the required low-frequency AC polarity/amplitude states.
```

There is no mandatory physical:

```text
HF bridge rectifier
→ stiff 350–360 V DC link
→ independent VSI H-bridge
```

in the main average-power path.

### 2.2 Voltage/current scale

For 220 Vac:

```text
Vout,pk = sqrt(2) × 220 = 311.13 V
Iout,rms = 2000 / 220 = 9.09 A
Iout,pk  = sqrt(2) × 9.09 = 12.86 A
```

At 12 V and a 95% current reference:

```text
I_source ≈ 175.44 A
```

If the transformer secondary square-wave amplitude is `Vs`, the active-state averaged output satisfies the first-order bound:

```text
|v_xy,avg| = d(t) × Vs
```

where `0 ≤ d(t) ≤ 1`.

Therefore:

```text
Vs ≥ 311.13 V
```

before practical regulation margin.

Critical consequence:

> O13 stage-boundary integration does **not** automatically reduce the transformer voltage-ratio burden. The magnetic path still must provide an HF-link amplitude high enough to synthesize the AC peak unless another gain mechanism is added.

Thus G13-A attacks duplicated stage boundaries, not the PM1 gain ratio itself.

---

## 3. Exact secondary matrix states

Define transformer secondary terminals `a,b` and pre-filter output terminals `x,y`.

Bidirectional switch cells:

```text
S_ax : a ↔ x
S_ay : a ↔ y
S_bx : b ↔ x
S_by : b ↔ y
```

Each cell must conduct commanded current bidirectionally and block the required off-state polarity. A practical implementation may require anti-series MOSFETs, reverse-blocking devices, or an equivalent AC-switch cell. Device realization is intentionally not fixed at this gate.

Let:

```text
σh = sign(v_ab)      HF-link polarity
σo = desired AC output polarity
```

### State P1 — positive HF link, positive output

```text
v_ab > 0
S_ax = ON
S_by = ON
S_ay = OFF
S_bx = OFF

x ← a
b → y
v_xy = +|v_ab|
```

### State P2 — negative HF link, positive output

```text
v_ab < 0
S_bx = ON
S_ay = ON
S_ax = OFF
S_by = OFF

x ← b
a → y
v_xy = +|v_ab|
```

### State N1 — positive HF link, negative output

```text
v_ab > 0
S_ay = ON
S_bx = ON
S_ax = OFF
S_by = OFF

v_xy = -|v_ab|
```

### State N2 — negative HF link, negative output

```text
v_ab < 0
S_by = ON
S_ax = ON
S_ay = OFF
S_bx = OFF

v_xy = -|v_ab|
```

The two physical crossbar orientations are therefore selected according to the product of HF-link polarity and requested output polarity.

### Zero/freewheel states

A usable PWM graph also needs a state that preserves output-inductor current without applying `±Vs`.

Candidate local zero states are:

```text
Z_a:
S_ax + S_ay ON
x and y clamped to node a

Z_b:
S_bx + S_by ON
x and y clamped to node b
```

so ideally:

```text
v_xy ≈ 0
```

while the output-filter current has a local freewheel path.

This avoids forcing every zero interval through the transformer. However, transition sequencing must prevent:

```text
secondary winding short circuit
output-inductor open circuit
unsafe commutation of transformer leakage current
```

A multi-step commutation sequence is therefore a mandatory later waveform/control item.

---

## 4. X3 synthesis closure

Within one switching period, select:

```text
active state fraction = d(t)
zero state fraction   = 1 - d(t)
```

with:

```text
d(t) ≈ |Vref,pk sin(ωt)| / Vs
σo   = sign(sin(ωt))
```

Then the switching-period average is:

```text
v_xy,avg(t) ≈ Vref,pk sin(ωt)
```

and the output low-pass filter removes the HF pulse content.

Therefore the normalized graph is capable, at the ideal state level, of direct AC polarity/amplitude synthesis without a stiff intermediate DC bus.

Status:

```text
X3 STATE CLOSURE = THEORETICALLY CLOSED
```

This is not a switching-loss or THD validation.

---

## 5. X1 completion and pre-X1 burden

The G13-A main path adds no AC-synthesis switch in series with the 12-V source before the transformer.

Therefore the basic pre-X1 full-current edge count can remain comparable to a conventional PM1 primary bridge.

At the secondary HF-link:

```text
Vs ≈ 311–360 V class
main power current scale ≈ P/Vs ≈ 5.6–6.4 A class
```

while the output sinusoidal RMS current is:

```text
9.09 A
```

because the AC voltage varies through the line cycle.

The majority power has left the 12-V / ~175-A conduction domain before the matrix/cycloconverter performs the AC-synthesis function.

Status:

```text
X1 COMPLETION PLACEMENT = CONSISTENT WITH FILE-28 RULE
PRE-X1 ADDED X3 SERIES EDGE = NONE IN NORMALIZED GRAPH
```

This is the principal structural reason O13 was ranked ahead of pre-X1 overlap classes.

---

## 6. Hidden X2 problem exposed by the actual graph

The direct HF-link main graph contains no large stiff DC-link energy store.

For a unity-PF single-phase load:

```text
p_out(t) = P[1 - cos(2ωt)]
```

with:

```text
P = 2000 W
f = 50 Hz
```

The 2ω buffer-energy amplitude is:

```text
E_2ω,pk = P/(4πf)
         = 3.183 J
```

and peak-to-peak swing is:

```text
E_2ω,pp = 6.366 J
```

### 6.1 If no X2 buffer is provided

The source must supply the pulsating instantaneous output power.

Ideal current-ripple amplitude scale at 12 V:

```text
I_2ω,source,pk ≈ P/Vin
               ≈ 166.7 A
```

This makes an unbuffered G13-A graph unacceptable as a complete low-ripple battery-interface answer unless the product contract explicitly permits the source to absorb this 2ω current.

Therefore:

```text
G13-A-unbuffered
= X1/X3 closed
but X2 requirement unresolved / source-ripple penalty severe
```

### 6.2 Minimum separately identifiable post-X1 X2 branch

A normalized separate X2 can be attached to the reduced-current HF-link:

```text
secondary HF-link a,b
        |
        +→ bidirectional buffer interface QB
             + small current-shaping Lb
             + Cbuf
```

Control target:

```text
p_buf(t) = P cos(2ωt)
```

so that ideally:

```text
p_source ≈ P constant
p_source = p_out + p_buf
```

The buffer has zero average energy transfer but its instantaneous power magnitude reaches approximately:

```text
|p_buf|max = 2 kW
```

Thus active power decoupling is not a low-power auxiliary merely because its average power is zero.

The important advantage is location:

```text
at ~350 V: 2-kW current scale ≈ 5.7 A
vs
at 12 V:    2-kW current scale ≈ 166.7 A
```

So X2 is expensive in semiconductor rating but cheap relative to the source domain in I²R sensitivity.

### 6.3 Buffer capacitance scale

Using:

```text
E_pp = 0.5 C (Vmax² - Vmin²)
```

for 6.366 J peak-to-peak energy:

At 400 V center voltage:

```text
±5%  (380–420 V) → C ≈ 398 µF
±10% (360–440 V) → C ≈ 199 µF
±20% (320–480 V) → C ≈ 99.5 µF
```

At 350 V center voltage:

```text
±5%  → C ≈ 520 µF
±10% → C ≈ 260 µF
±20% → C ≈ 130 µF
```

Hence active decoupling can reduce storage capacitance only by allowing a larger buffer-voltage swing and paying for the buffer power interface.

---

## 7. Loss-fate audit versus O0 baseline

Normalize O0 as:

```text
12 V primary bridge
→ HFT
→ secondary rectifier
→ stiff HV DC link / passive X2
→ VSI
→ output filter
```

G13-A removes the explicit rectifier/DC-link/VSI series sequence, but it does not remove all corresponding physical burden.

| O0 burden | G13-A fate | Status |
|---|---|---|
| primary LV switch conduction | remains | RETAINED |
| transformer copper/core | remains at full gain requirement | RETAINED / geometry TBD |
| bridge rectifier conduction | no separate bridge | potentially REMOVED |
| VSI conduction | replaced by secondary AC matrix | RELOCATED |
| rectifier commutation | replaced by matrix commutation | RELOCATED / interaction TBD |
| VSI switching | replaced by HF-link matrix switching/PDM/PWM | RELOCATED / may increase frequency |
| passive HV DC-link X2 | removed from main path | REMOVED as stiff link |
| 2ω energy storage requirement | remains | RELOCATED to Cbuf / source |
| dedicated active buffer switches | absent in O0 passive X2 | INTRINSIC_NEW if active X2 used |
| matrix bidirectional-switch conduction | absent in O0 | INTRINSIC_NEW |
| matrix four-step/overlap commutation burden | absent in O0 conventional VSI form | INTERACTION_NEW |

Critical conclusion:

```text
stage count reduction ≠ guaranteed loss reduction
```

A practical bidirectional matrix switch may itself require two anti-series MOSFETs or another bidirectional-blocking realization. Therefore two conducting matrix cells can correspond to four semiconductor dies in the instantaneous path. The direct graph cannot claim a conduction advantage until matched device technology and current waveforms are specified.

The key possible savings remain:

```text
- elimination of a distinct diode-bridge forward-drop bucket
- elimination of a stiff main-path DC-link boundary
- possible reduction of duplicated switching stages
```

The key possible penalties are:

```text
- HF commutation of the secondary matrix
- bidirectional-switch die count / R_on
- leakage-current commutation difficulty
- added X2 active-buffer interface if source ripple must be suppressed
```

---

## 8. Pre-simulation state/stress decision

### Passed conceptually

```text
X1/X3 state relation                         = CLOSED
AC polarity synthesis                         = CLOSED
output amplitude relation                     = CLOSED with Vs ≥ 311 V
no new 175-A X3 series device                  = PASSED
X2 energy magnitude                            = CLOSED analytically
```

### Still unresolved by analytical graph

```text
matrix commutation current during leakage-energy transfer
actual matrix switch RMS current
switch voltage overshoot
zero-state current path parasitics
primary RMS under envelope/power-decoupling control
active-buffer RMS/current ripple
full matched total loss
EMI/common-mode behavior
```

Thus, on physics alone:

```text
G13-A = FEASIBLE / CONDITIONAL
```

not a robust loss winner.

Gate A is therefore required before simulation.

---

## 9. Multi-route prior-art Gate A

File 43 requires independent retrieval routes. This file used three materially different routes.

### Route A — IEEE-direct / exact title and architecture search

Recovered IEEE/peer-reviewed records include:

1. S. K. Mazumder and A. K. Rathore, “Primary-Side-Converter-Assisted Soft-Switching Scheme for an AC/AC Converter in a Cycloconverter-Type High-Frequency-Link Inverter,” IEEE Transactions on Industrial Electronics, vol. 58, no. 9, 2011. DOI: `10.1109/TIE.2010.2098375`.

   Structural relevance:

   ```text
   primary converter
   → HF transformer
   → cycloconverter-type HF-link inverter
   → direct AC synthesis
   ```

2. “Improved Control for Isolated Cycloconverter-type Dual Active Bridge DC/AC Converter,” IEEE record `9161451`.

   Structural relevance: isolated cycloconverter-type direct DC/AC conversion with HFT and secondary-side AC synthesis.

3. “Soft-Switching Modulation Method for Full-Bridge DC-AC HF-Link Inverter,” IEEE record `8927186`.

   Structural relevance: DC-side full bridge + HF link + AC-side cycloconverter, explicitly without a conventional DC link.

Route-A result:

```text
The core X1+X3 graph is established prior art.
```

### Route B — Exa semantic / graph-behavior search

Exa recovered several close records, most importantly:

1. Z. Salam, N. C. Lim, and S. M. Ayob, “Analysis and Design of a Bidirectional Cycloconverter-Type High Frequency Link Inverter with Natural Commutated Phase Angle Control,” Journal of Power Electronics, 2011. DOI: `10.6113/JPE.2011.11.5.677`.

   The work explicitly contrasts the three-stage `dc-ac → rectification/DC bus → dc-ac` route against a cycloconverter HF-link approach with fewer conversion stages.

2. Experimental/earlier matrix-converter HF-link work from the Itoh group using primary HF inverter + transformer + secondary matrix converter/PDM.

3. Contemporary implementation evidence: TI 600-W GaN single-phase cycloconverter reference design, using a DC-side full bridge, HFT, AC-side bidirectional cycloconverter and no high-voltage intermediate stage. This is implementation evidence, not the novelty authority.

Route-B result:

```text
The normalized main graph and its stage-elimination rationale are mature and repeatedly implemented.
```

### Route C — Scholar/OpenAlex/Google-Scholar route

Scholar search independently recovered:

- experimental isolated DC-AC converter with matrix converter + PDM;
- three-phase cycloconverter-type HF-link inverter literature;
- earlier HF-link/cycloconverter families.

More importantly, the power-decoupling extension was found in:

1. H. Takahashi, N. Takaoka, R. R. Rodriguez Gutierrez, and J.-I. Itoh, “Power decoupling method for isolated DC to single-phase AC converter using matrix converter,” IECON 2014. DOI: `10.1109/IECON.2014.7048991`.

   Structure:

   ```text
   full bridge inverter
   + high-frequency transformer
   + matrix converter
   + center-tapped transformer / small LC buffer for single-phase power ripple
   ```

2. N. Takaoka, H. Takahashi, and J.-I. Itoh, “Isolated Single-Phase Matrix Converter Using Center-Tapped Transformer for Power Decoupling Capability,” IEEE Transactions on Industry Applications, 2018, vol. 54, no. 2, pp. 1523–1531. DOI: `10.1109/TIA.2017.2774760`.

   Reported architecture/behavior includes:

   ```text
   full bridge primary
   + high-frequency center-tapped transformer
   + secondary matrix converter
   + no bulky conventional DC-link capacitor
   + small capacitor / common-mode transformer state for power decoupling
   ```

   Published prototype context: 1 kW; reported large reduction of DC input ripple and low output-voltage THD.

Route-C result:

```text
Not only the O13 main graph, but the explicit O13 + single-phase X2-decoupling problem has close prior art.
```

---

## 10. Gate-A graph comparison

### G13-A normalized graph

```text
DC source
→ primary full bridge
→ HFT
→ secondary bidirectional matrix/cycloconverter
→ sinusoidal AC synthesis

+ separate/identifiable 2ω buffer function near the reduced-current HF link
```

### Closest prior-art normalized graph

Takaoka/Takahashi/Itoh family:

```text
DC source
→ primary full bridge
→ center-tapped HFT
→ secondary matrix converter
→ single-phase AC

+ transformer/common-mode + small LC/capacitor power-decoupling function
```

Comparison:

```text
X1 magnetic transfer                          = SAME PRINCIPLE
X1+X3 secondary matrix/cycloconverter overlap = SAME GRAPH CLASS
absence of stiff DC-link main path             = SAME STRATEGY
single-phase 2ω decoupling near HFT/matrix     = SAME / MORE INTEGRATED PRIOR ART
battery-side ripple suppression objective       = SAME SYSTEM PROBLEM
```

The exact switch-count implementation can differ, but that does not establish a new normalized power graph.

Formal result:

```text
G13-A Gate A = SAME_GRAPH / NEAR_GRAPH
G13-A topology-novelty path = STOP
PSIM as proposed new topology = NO
```

This result does **not** say O13 is a bad architecture. It says the obvious O13 realization is already a mature research family.

---

## 11. What remains useful from G13-A

G13-A is retained as a comparator/reference because it directly tests the project's coordinate-overlap hypothesis.

Reference role:

```text
G13-REF1 = isolated HF-link / secondary cycloconverter matrix inverter
```

Strong reference variant:

```text
G13-REF2 = Takaoka/Takahashi/Itoh center-tapped matrix converter with power decoupling
DOI 10.1109/TIA.2017.2774760
```

These references establish that:

```text
X1+X3 overlap is physically practical.
X2 can also be addressed without a conventional stiff HV DC link.
```

But they also expose the hard questions a new graph must improve:

```text
1. matrix AC-switch conduction count
2. HF commutation / leakage-energy handling
3. transformer still carries full AC-peak voltage-ratio burden
4. 2ω buffer is not free
5. control coupling is substantial
```

---

## 12. Mainline consequence

File 52's coordinate search remains valid, but the first O13 graph is no longer a novelty branch.

Updated branch status:

```text
O13 coordinate class
= VALID / MATURE REFERENCE SPACE

G13-A standard full-bridge + HFT + secondary matrix
= STOP_AS_NOVELTY

G13-REF1 / REF2
= RETAIN AS COMPARATORS

PSIM for G13-A as proposed topology
= NOT AUTHORIZED
```

The next topology-search move should **not** be a cosmetic switch-count mutation of the same HF-link cycloconverter.

Immediate next priority returns to the coordinate matrix:

```text
G23-A = X1 separate, X2+X3 shared post-X1
```

Reason:

> G23-A asks a different structural question: can the unavoidable 2ω storage elements themselves become load-bearing AC-synthesis states, so that storage hardware and X3 hardware are shared after current reduction? This is not answered merely by the standard direct HF-link cycloconverter graph.

Any future G13-B is admissible only if it removes/changes a load-bearing edge relative to the known cycloconverter/matrix family, not merely modulation, switch technology, or rating.

---

## 13. Formal decision

```text
G13-A actual graph synthesis        = EXECUTED
state closure                        = THEORETICALLY FEASIBLE
X1 completion                        = CLOSED at reduced-current HF link
X3 synthesis                         = CLOSED at ideal switching-state level
X2 requirement                       = QUANTIFIED; 3.183-J amplitude / 6.366-J pp
unbuffered source-ripple consequence = SEVERE at 12 V
active/post-X1 X2 cost               = MATERIAL; up to ±2-kW instantaneous exchange
multi-route Gate A                   = EXECUTED
Gate A result                        = SAME_GRAPH / NEAR_GRAPH
PSIM authorization                   = NO
Candidate #10                        = HOLD / NOT_ASSIGNED
Novelty                              = NOT_ESTABLISHED
Immediate NEXT                       = G23-A actual graph synthesis
```

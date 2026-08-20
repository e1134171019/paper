# 50 — R7-C1A / R7-C1B Actual Graph Synthesis and Multi-Assistant IEEE Gate-B v1

Status date: 2026-08-20  
Role: `R7 ACTUAL GRAPH SYNTHESIS / MULTI-ASSISTANT IEEE GATE B / EARLY NOVELTY REJECTION`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ; 350 Vdc working HV-link target`  
Evidence status: `THEORETICAL GRAPH + FIRST-PRINCIPLES LOSS SCREEN + MULTI-ROUTE PRIOR-ART SEARCH`  
Simulation status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File 49 restored the original mainline and retained R7 only for **actual graph differentiation**, not because `PM1 + PM3` itself is new.

This file executes the next required step:

```text
R7-C1 concept
→ generate two concrete graphs
→ lock nodes / edges / states
→ derive first-order gain and loss burdens
→ run multi-assistant IEEE Gate B
→ kill known / trivial-composition graphs before PSIM
```

The two graphs screened are:

```text
R7-C1A = post-rectifier active 3:1 series-parallel switched-capacitor tripler
R7-C1B = post-HFT passive full-wave voltage-doubler rectifier
```

Neither is allowed to become a candidate unless its complete graph survives Gate B.

---

## 2. Shared R7 design authority

The project authority remains:

```text
12 V / ~175 A source domain
→ leave extreme-LV domain with minimum all-current impedance
→ perform added voltage-building complexity only after major current reduction
```

At the working 350-V bus:

```text
I_source,95 ≈ 2000/(12×0.95) = 175.44 A
I_HV,ideal ≈ 2000/350 = 5.714 A
```

The R7-C1 family must therefore obey:

```text
PM3 is downstream of PM1 current reduction.
No PM3 capacitor/switch is in the 175-A source-series path.
Charge-transfer / ESR / switch loss is explicit.
Known voltage-doubler / multiplier / series-parallel SC graphs cannot be renamed as new topology.
```

---

# PART A — R7-C1A

## 3. R7-C1A normalized graph

Identifier:

```text
R7-C1A = POST-RECTIFIER ACTIVE SERIES-PARALLEL 3:1 CHARGE-STACKING GRAPH
```

### 3.1 PM1 front end

```text
12-V source
→ low-impedance primary switching stage
→ HFT
→ full-wave secondary rectifier
→ intermediate rail N1/N0
```

Working ideal rail:

```text
V_R = 350/3 ≈ 116.67 V
G_PM1,proxy ≈ 116.67/12 ≈ 9.72×
I_R,95 ≈ 2000/(0.95×116.67) ≈ 18.05 A
```

A reservoir capacitor `C0` holds `N1-N0 ≈ V_R`.

### 3.2 PM3 flying-capacitor network

Flying capacitors:

```text
Cf1
Cf2
```

HV bus capacitor:

```text
CHV between N3 and N0
```

Switch edges:

```text
S1: N1 ↔ Cf1+
S2: N0 ↔ Cf1-
S3: N1 ↔ Cf2+
S4: N0 ↔ Cf2-

S5: N1   ↔ Cf1-
S6: Cf1+ ↔ Cf2-
S7: Cf2+ ↔ N3
```

### 3.3 State Q — parallel charge

```text
S1,S2,S3,S4 = ON
S5,S6,S7    = OFF
```

Then:

```text
Cf1 ≈ V_R
Cf2 ≈ V_R
```

Both flying capacitors charge in parallel from the post-HFT intermediate rail.

During this state, `CHV` supplies the load.

### 3.4 State S — series stack / HV-bus recharge

```text
S1,S2,S3,S4 = OFF
S5,S6,S7    = ON
```

Series path:

```text
N0
→ base rail source V_R (N0→N1)
→ Cf1
→ Cf2
→ N3 / CHV
```

Ideal output:

```text
V_HV ≈ V_R + V_Cf1 + V_Cf2
     ≈ 3 V_R
```

so:

```text
V_HV,ideal ≈ 350 V
```

A non-overlap transition is mandatory between State Q and State S to avoid shorting a charged flying capacitor or directly shorting the intermediate rail.

---

## 4. R7-C1A voltage-stress proxy

Under ideal `V_R = 116.67 V`:

During State S:

```text
Cf1- ≈ 116.7 V
Cf1+ ≈ 233.3 V
Cf2- ≈ 233.3 V
Cf2+ ≈ 350 V
```

Therefore some reconfiguration switches see approximately:

```text
~V_R ≈ 117 V
```

while other off-state edges can see approximately:

```text
~2V_R ≈ 233 V
```

The PM3 switches are therefore no longer 60-V-class LV devices, but they also do not process the 175-A source-domain current.

---

## 5. R7-C1A first charge-transfer loss screen

Use a first screen:

```text
f_SC = 50 kHz
I_HV = 5.714 A
Q_load/cycle = I_HV/f_SC ≈ 114.3 µC
```

If each flying capacitor is allowed voltage ripple `ΔV`, a first sizing proxy is:

```text
Cf ≈ Q_load / ΔV
```

For `V_R=116.67 V`:

| flying-cap ripple | ΔV | Cf per flying capacitor |
|---:|---:|---:|
| 1% | 1.167 V | ~98.0 µF |
| 2% | 2.333 V | ~49.0 µF |
| 3% | 3.500 V | ~32.7 µF |
| 5% | 5.833 V | ~19.6 µF |
| 10% | 11.667 V | ~9.8 µF |

For direct hard recharge of two flying capacitors from a stiff rail, a first-order charge-redistribution energy proxy is:

```text
E_redist/cycle ≈ 2 × 0.5 Cf ΔV²
```

which gives:

```text
P_redist,proxy ≈ I_HV × ΔV
```

Numerically:

| ripple | hard-charge redistribution proxy |
|---:|---:|
| 1% | ~6.67 W |
| 2% | ~13.33 W |
| 3% | ~20.0 W |
| 5% | ~33.33 W |
| 10% | ~66.67 W |

Status:

```text
FIRST-ORDER HARD-CHARGE PROXY
NOT A FINAL SCC LOSS MODEL
```

It nevertheless exposes a real R7-C1A burden:

```text
placing PM3 after PM1 solves the 175-A I²R problem,
but a hard series-parallel SC stage can create charge-sharing / pulse-current loss of its own.
```

Adding a deliberate resonant inductor to soft-charge the flying capacitors would change the mechanism set by introducing an explicit inductive / resonant mechanism and must not be silently counted as pure R7.

---

## 6. R7-C1A multi-assistant Gate-B search

The normalized graph above was searched using the File-43 protocol.

### Role A — IEEE-direct route

Search dimensions:

```text
isolated DC/DC + secondary-side switched capacitor
series-parallel switched-capacitor step-up
parallel charge / series discharge
isolated resonant switched-capacitor
high-frequency-link switched-capacitor DC transformer
```

Closest IEEE set includes:

1. Lei Yang, Wenqian Yu, Jiaxiang Zhang, **“High Voltage Gain Ratio Isolated Resonant Switched-Capacitor Converter for Sustainable Energy,”** IEEE Access, 2019, DOI `10.1109/ACCESS.2019.2893981`.
   - isolated transformer + switched-capacitor energy-transfer states;
   - 500-W experimental converter;
   - confirms isolated SC conversion is an established graph family.

2. IEEE Xplore `8769854`, **“A Family of Step-Up Series–Parallel Dual Resonant Switched-Capacitor Converters With Wide Regulation Range.”**
   - series-parallel SC step-up family;
   - flying capacitors are deliberately resonantly charged/discharged to avoid hard charge-sharing spikes.

3. IEEE literature on high-frequency-link DC transformers based on switched capacitors and general series-parallel switched-capacitor converters.

### Role B — Exa semantic route

Independent semantic search recovered:

1. IEEE Xplore `5764525`, **“Novel High Step-Up DC–DC Converter With Coupled-Inductor and Switched-Capacitor Techniques.”**
   - capacitors explicitly charge in parallel and discharge in series;
   - experimental 24-V to 400-V prototype;
   - demonstrates that `parallel-charge → series-discharge` is established power-converter prior art.

2. The same isolated-resonant switched-capacitor family and step-up series-parallel resonant SC family.

### Role C — Sider Scholar / OpenAlex route

Independent academic search returned, among others:

- **“High-Frequency-Link DC Transformer Based on Switched Capacitor for Medium-Voltage DC Power Distribution Application.”**
- broad switched-capacitor DC-conversion literature and isolated/nonisolated high-gain families.

The academic route independently confirms that both:

```text
isolated HFT conversion
+
series-parallel switched-capacitor voltage transformation
```

are mature graph families.

---

## 7. R7-C1A Gate-B adjudication

Normalized project graph:

```text
HFT + rectifier
→ stiff ~116.7-V intermediate rail
→ independent 3:1 series-parallel switched-capacitor stage
→ 350-V bus
```

The search set did not establish one exact IEEE paper with every one of the seven switch edges `S1...S7` in precisely this post-rectifier cascade.

However, the load-bearing graph property is not differentiated:

```text
known isolated DC/DC subgraph
+
known stiff intermediate dc rail
+
known series-parallel switched-capacitor 3:1 subgraph
```

There is no shared device, shared commutation state, or merged energy-transfer edge between PM1 and PM3.

Therefore the project graph is a **serial composition of known converter subgraphs**, not yet a defensible new power-conversion graph.

Formal result:

```text
R7-C1A Gate B
= NEAR_GRAPH / COMPOSITION_OF_KNOWN_SUBGRAPHS

Topology novelty path
= STOP_AS_NOVELTY

Comparator value
= RETAIN

PSIM authorization as proposed topology
= NO
```

This is stronger than saying “no exact paper was found.”

A search-negative exact edge list does not rescue a graph whose functional subgraphs remain a trivial cascade.

---

# PART B — R7-C1B

## 8. R7-C1B normalized graph

Identifier:

```text
R7-C1B = HFT + PASSIVE FULL-WAVE VOLTAGE-DOUBLER RECTIFIER
```

Power path:

```text
12-V source
→ low-impedance primary switching
→ HFT
→ bipolar secondary waveform
→ conventional full-wave / Delon-type voltage-doubler rectifier
→ two series output capacitors
→ HV link
```

Functional states:

```text
positive secondary half-cycle
→ upper doubler capacitor charges

negative secondary half-cycle
→ lower doubler capacitor charges

output
→ series sum of the two capacitor voltages
```

Ideal gain of the PM3 rectifier block:

```text
k_PM3 ≈ 2
```

For a 350-V bus:

```text
Vsecondary amplitude proxy ≈ 175 V
G_PM1,proxy ≈ 175/12 ≈ 14.58×
PM3-domain current @95% ≈ 2000/(0.95×175) ≈ 12.03 A
```

This respects the post-magnetic current-domain constraint, but gives less magnetic-ratio relief than C1A.

---

## 9. R7-C1B multi-assistant Gate-B result

### Role A — IEEE-direct route

Direct IEEE search recovered:

- IEEE Xplore `9047805`, **“A High Frequency Planar Transformer Isolated DC-DC Power Converter with Secondary-Side ZCS Active Switches and Voltage-Doubler Rectifier.”**

This is already the same architecture primitive:

```text
HFT isolation
+
secondary-side voltage-doubler rectification
```

### Role B — Exa semantic route

Recovered multiple transformer/coupled-magnetic + voltage-doubler / multiplier implementations, including:

- Weichen Li et al., **“Interleaved High Step-Up ZVT Converter With Built-In Transformer Voltage Doubler Cell for Distributed PV Generation System,”** IEEE TPEL 2013, DOI `10.1109/TPEL.2012.2199771`.
  - transformer windings + two doubler diodes + two doubler capacitors;
  - capacitors alternately charge/discharge;
  - 1-kW, 40-V to 380-V prototype.

- isolated push-pull / transformer converters using voltage-doubling rectification are widespread prior art.

### Role C — Sider Scholar / OpenAlex route

Independent academic search returned high-step-up coupled-magnetic and voltage-multiplier/doubler families, confirming the same established mechanism and secondary architecture.

Formal Gate-B classification:

```text
R7-C1B Gate B
= SAME_GRAPH / KNOWN_SECONDARY_RECTIFIER_PRIMITIVE

Topology novelty path
= STOP_AS_NOVELTY

Role
= KEEP_AS_R7_REFERENCE COMPARATOR

PSIM as proposed topology
= NO
```

---

## 10. Comparison of the two executed graphs

| Graph | PM3 factor | Post-PM1 current scale | Main attraction | Gate-B result |
|---|---:|---:|---|---|
| R7-C1A | ~3× | ~18.05 A | stronger magnetic-ratio relief | `NEAR_GRAPH / known-block cascade / STOP` |
| R7-C1B | ~2× | ~12.03 A | simple passive rectifier | `SAME_GRAPH / STOP` |

The important retained physical result is not either topology.

It is the design constraint:

```text
PM3-after-PM1 is still structurally sensible for extreme-LV loss,
but simple cascading of a known HFT stage and a known SC/VDR stage does not create a research topology.
```

---

## 11. New R7 graph constraints created by this Gate-B run

The failed C1A/C1B graphs add three new hard constraints:

```text
R7-G8  No independent stiff intermediate DC rail may separate PM1 and PM3
       if the resulting system is only a cascade of two known converter blocks.

R7-G9  PM3 must share at least one load-bearing switching state / rectification edge /
       energy-transfer edge with the HFT secondary process.

R7-G10 A generic voltage-doubler / multiplier rectifier alone is a reference primitive,
        not a project topology contribution.
```

A further caution:

```text
Adding an explicit resonant inductor solely to soft-charge the flying capacitors
would introduce another physical mechanism and must be reclassified rather than hidden inside R7.
```

---

## 12. Next surviving R7 direction

Working concept only:

```text
R7-C2 = SECONDARY-STATE-INTEGRATED CHARGE-STACKING
```

Required idea:

```text
HFT secondary switching state
and
PM3 capacitor charge/stack state
must be the SAME coordinated power-transfer sequence,
not two cascaded stages.
```

Target skeleton:

```text
12 V
→ low-impedance primary switching
→ HFT
→ secondary polarity/state directly selects which flying capacitor is charged
→ another HFT secondary state stacks that stored capacitor voltage with instantaneous secondary voltage
→ HV bus
```

Hard requirements before actual graph generation:

```text
no 175-A PM3 path
no independent post-HFT SC converter clock
no generic VDR-only graph
no stiff intermediate dc bus used merely to cascade known blocks
periodic capacitor charge balance
transformer volt-second balance
explicit diode/switch current paths
explicit charge-redistribution loss
```

Status:

```text
R7-C2 = CONCEPT-LEVEL SYNTHESIS TARGET ONLY
Actual graph = NOT YET BUILT
Gate B = NOT STARTED
PSIM = NOT AUTHORIZED
Candidate #10 = HOLD
Novelty = NOT_ESTABLISHED
```

---

## 13. Mainline decision

```text
R7-C1A
→ STOP as proposed topology
→ retain only as post-PM1 series-parallel SC comparator

R7-C1B
→ STOP as proposed topology
→ retain as known transformer + VDR comparator

R7 branch
→ CONTINUE
→ but only through integrated secondary-state graph synthesis

R8
→ remains reserve comparator

Ryan / R2
→ remains paused comparator branch
```

This execution therefore does not produce a new topology.

It narrows the topology-synthesis space by eliminating two obvious R7 constructions before simulation and converts the original broad rule `PM3 after current reduction` into a stronger graph rule:

> **PM1 and PM3 must be physically/state integrated after current reduction; merely cascading an HFT and a known switched-capacitor/voltage-doubler block is insufficient.**

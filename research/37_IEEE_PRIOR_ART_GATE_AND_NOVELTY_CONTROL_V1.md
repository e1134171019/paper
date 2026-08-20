# 37 — IEEE Prior-Art Gate and Novelty-Control Protocol v1

Status date: 2026-08-20  
Role: `IEEE PUBLICATION / PRIOR-ART CONTROL / PRE-SIMULATION NOVELTY GATE`  
Primary publication corpus: `IEEE Xplore`  
Research boundary anchor: `12 Vdc / 2 kW / 220 Vac / 1φ`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This file adds a mandatory prior-art control layer to the theoretical mechanism-combination branch in:

```text
research/36_THEORETICAL_MECHANISM_COMBINATION_SCREEN_V1.md
```

The purpose is to prevent a failure mode in which substantial analytical, simulation and hardware effort is invested before discovering that the same mechanism combination, circuit graph, switching law or claimed contribution already exists in IEEE literature.

From this point forward:

```text
NEW PM COMBINATION
↓
IEEE PRIOR-ART GATE A
↓
FIRST-PRINCIPLES THEORY
↓
ACTUAL CIRCUIT GRAPH
↓
IEEE PRIOR-ART GATE B
↓
SIMULATION / LOSS AUDIT
↓
CLAIMED TECHNICAL FINDING
↓
IEEE PRIOR-ART GATE C
↓
ONLY THEN:
contribution drafting / candidate promotion / novelty evaluation
```

This protocol does **not** assume that an IEEE paper must contain a completely unprecedented circuit diagram to be publishable. A contribution may instead be a defensible new operating principle, analytical result, loss boundary, modulation law, design criterion, comparison framework or experimentally validated engineering finding.

However:

```text
known topology + same known operating principle + same known loss trade-off
≠ novelty
```

Changing only the input voltage or repeating an existing topology in simulation is not sufficient by itself.

---

## 2. Publication-policy distinction

The current publication target uses IEEE as the primary evidence corpus for prior-art control.

Therefore:

```text
PRIMARY SEARCH AUTHORITY FOR THIS PROJECT
= IEEE Xplore
```

Non-IEEE literature may still be used later for completeness, background or final novelty-risk reduction, but every mechanism combination must first survive the IEEE gate before deeper project investment.

Important limitation:

```text
IEEE search pass
≠ universal proof of novelty
```

The gate controls research efficiency and IEEE publication risk; it does not make a legal or universal claim that no related work exists elsewhere.

---

## 3. IEEE Prior-Art Gate A — mechanism / family gate

### Trigger

Run immediately when a new theoretical PM combination is proposed, before detailed circuit derivation or circuit-level simulation.

### Required search dimensions

Search the combination using multiple equivalent topology/physics vocabularies rather than the internal PM labels alone.

Example for:

```text
PM-1 + PM-2 + PM-4 + PM-7
```

required search terms include combinations of:

```text
current-fed isolated converter
current-fed push-pull
current-fed full bridge
current-fed DAB
high-step-up isolated converter
active-clamped isolated converter
resonant current-fed converter
ZVS / ZCS isolated converter
low-voltage high-current inverter
high-frequency-link inverter
bidirectional inverter
```

### Gate-A statuses

```text
KNOWN_MECHANISM_COMBINATION
= the same physical mechanism combination is clearly established in IEEE literature.

CLOSE_PRIOR_ART
= mechanism combination and major power path are already very close, but the actual graph / boundary / analytical question may differ.

POSSIBLY_DIFFERENTIATED
= no close IEEE mechanism/family match is found after a multi-query search.

STOP_AS_NOVELTY
= do not use the combination itself as a novelty claim.

KEEP_AS_COMPARATOR
= retain because it is a strong benchmark/falsifier.

CONTINUE_FOR_DIFFERENTIATION
= continue only to test a different technical question, boundary or graph.
```

A Gate-A failure as novelty does not imply the topology is useless. It may become the strongest comparator.

---

## 4. IEEE Prior-Art Gate B — actual circuit graph gate

### Trigger

Run after a concrete electrical graph exists.

The comparison must be graph-to-graph, not name-to-name.

### Mandatory comparison fields

```text
source connection
input inductor placement / absence
number and connection of LV switches
bridge / push-pull / current-fed arrangement
transformer / coupled-magnetic connection
turns-ratio role
leakage / series-L role
active/passive clamp connection
resonant capacitor placement
voltage multiplier / flying-capacitor placement
rectifier type
HV-link existence / absence
X1 start and completion
X2 location or none
X3 implementation
switching-state sequence
current paths by state
static conversion-gain equation
ZVS / ZCS condition
voltage/current stress equations
```

### Gate-B statuses

```text
SAME_GRAPH
NEAR_GRAPH
STRUCTURALLY_DIFFERENT_GRAPH
GRAPH_MATCH_INCONCLUSIVE
```

Decision rule:

```text
SAME_GRAPH + same technical claim
→ STOP as topology novelty

NEAR_GRAPH
→ require explicit structural and quantitative differentiation

STRUCTURALLY_DIFFERENT_GRAPH
→ continue, but contribution novelty still requires Gate C
```

---

## 5. IEEE Prior-Art Gate C — contribution-level gate

### Trigger

Run after analytical/simulation results exist and before writing a novelty/contribution statement.

The question is no longer:

```text
Is the circuit different?
```

It is:

```text
Is the claimed finding different?
```

### Mandatory claim comparison

For the closest 5–10 IEEE papers, compare whether they already establish the same:

```text
loss scaling law
RMS-current criterion
soft-switching boundary
circulating-current trade-off
magnetic design relation
voltage-gain condition
extreme-LV operating boundary
architecture crossover point
loss-relocation conclusion
modulation law
control law
component-stress reduction
comparison methodology
```

### Gate-C statuses

```text
CLAIM_ALREADY_KNOWN
CLAIM_INCREMENTAL
CLAIM_DIFFERENTIATED
CLAIM_NOVELTY_NOT_ESTABLISHED
```

Only `CLAIM_DIFFERENTIATED` may proceed toward a formal contribution statement, and even then the final manuscript must not overclaim beyond the evidence.

---

## 6. Initial IEEE Gate-A findings for current theoretical combinations

### R1 — PM-1 + PM-7

Role:

```text
magnetic X1 + AC synthesis baseline
```

Initial IEEE status:

```text
KNOWN_MECHANISM_COMBINATION
KEEP_AS_COMPARATOR
NOT A NOVELTY SOURCE
```

Reason:

Transformer/HFT conversion followed by inverter AC synthesis is a mature converter architecture class.

### R2 — PM-1 + PM-4 + PM-7

Role:

```text
magnetic X1
+ reactive-energy-assisted commutation
+ AC synthesis
```

Initial IEEE status:

```text
KNOWN_MECHANISM_COMBINATION
STOP_AS_MECHANISM_NOVELTY
KEEP_AS_STRONG_MAGNETIC / SOFT-SWITCHING COMPARATOR
```

IEEE literature already contains broad families of:

```text
phase-shift full-bridge ZVS converters
resonant isolated converters
active-clamped push-pull / full-bridge converters
HFT converters exploiting leakage / Coss for soft switching
```

Therefore the valid R2 research question is not whether `PM-1 + PM-4` is new.

The valid question is whether an optimized R2-type path remains loss-optimal at the project's extreme-low-voltage, high-current boundary.

### R6 — PM-1 + PM-2 + PM-4 + PM-7

Role:

```text
inductive/current-fed gain participation
+ HFT transformation
+ soft commutation
+ AC synthesis
```

Initial IEEE status:

```text
CLOSE_PRIOR_ART / KNOWN MECHANISM COMBINATION
STOP_AS_MECHANISM-COMBINATION NOVELTY
CONTINUE_FOR_EXTREME-LV DIFFERENTIATION
```

Directly relevant IEEE prior art includes current-fed soft-switching isolated converters and current-fed soft-switching inverter front ends.

Representative IEEE records identified in the first screen include:

1. **Current-Fed Soft-Switching Push–Pull Front-End Converter-Based Bidirectional Inverter for Residential Photovoltaic Power System**  
   IEEE Xplore document: `6716999`

2. **Isolated High Step-Up Current-Fed DC-DC Converter With Low Input Current Ripple and Wide Full-Soft-Switching Capability**  
   IEEE Transactions on Industry Applications, 2025  
   DOI: `10.1109/TIA.2025.3544985`

3. DAB / current-fed DAB literature that jointly treats:

```text
HFT transformation
series/leakage inductive transfer
ZVS boundary
RMS / peak current
circulating power
conduction-versus-switching-loss trade-off
```

Therefore R6 may only continue on a differentiated question such as:

> Does the loss-optimal conclusion of known current-fed / HFT / soft-switching structures change when the input is driven into the 12 V, ~167–175 A, 2 kW source domain?

### R7 — PM-1 + PM-3 + PM-7

Initial IEEE status:

```text
GATE A = PENDING
```

Required search clusters before deep simulation:

```text
transformer + voltage multiplier inverter
isolated high-step-up + voltage-doubler + inverter
switched-capacitor assisted isolated converter
HFT + capacitive voltage stacking
multilevel / flying-capacitor assisted HF-link inverter
```

No novelty assumption is allowed before this screen.

### R8 — PM-2 + PM-3 + PM-7

Initial IEEE status:

```text
GATE A = PENDING
```

Required search clusters:

```text
inductor + switched-capacitor high-gain inverter
boost + voltage multiplier inverter
hybrid switched-inductor switched-capacitor inverter
transformerless high-step-up single-phase inverter
high-gain impedance-source / switched-boost inverter
```

No novelty assumption is allowed before this screen.

### R9 — PM-1 + PM-2 + PM-3 + PM-7

Initial status:

```text
GATE A = PENDING
CALG-1 MINIMALITY RISK = HIGH
```

This combination must not receive extra novelty credit merely because it stacks more mechanisms. Close prior art is expected in coupled-inductor / current-fed / voltage-multiplier / active-clamp families.

---

## 7. IEEE prior art already constraining the research methodology

The following classes are already established in IEEE literature and cannot be claimed broadly as new by this project:

### 7.1 Graph / systematic topology derivation

Representative:

**From Components to Converters: A Fundamental Topology Derivation Method for Nonresonant DC–DC Converters Based on Graph Theory**  
IEEE Transactions on Power Electronics  
DOI: `10.1109/TPEL.2023.3323597`

Implication:

```text
systematically combining components / graphs
≠ project novelty by itself
```

### 7.2 Automated topology derivation including AC / isolation

Representative:

**Automated Power Converter Topology Derivation Methodology Based on Exhaustive Graph Search**  
IEEE Transactions on Power Electronics  
DOI: `10.1109/TPEL.2024.3518758`

Implication:

```text
automated circuit graph generation
including AC ports / isolated structures
≠ project novelty by itself
```

### 7.3 AI-assisted power-converter topology generation

IEEE literature already includes reinforcement-learning / AI-assisted converter topology-generation approaches.

Implication:

```text
AI helps generate converter topology
≠ sufficient novelty claim
```

### 7.4 Loss / RMS / ZVS multi-objective optimization

IEEE literature already studies the trade among:

```text
ZVS range
RMS current
peak current
circulating current
switching loss
conduction loss
```

Implication:

```text
soft switching reduces switching loss but may increase RMS / circulation
≠ new observation by itself
```

---

## 8. Current potentially differentiated research direction

The first IEEE screen shifts the research emphasis away from:

```text
"invent PM-1 + PM-2 + PM-4"
```

because that mechanism combination is already represented in IEEE prior art.

The stronger open question is now:

```text
EXTREME-LOW-VOLTAGE / HIGH-CURRENT ARCHITECTURE SELECTION
```

with anchor:

```text
Vin = 12 V
Pout = 2 kW
I_source,ideal = 166.67 A
I_source @95% reference = 175.44 A
Vout = 220 Vac / 1φ
```

At fixed power:

```text
I ∝ 1 / Vin
P_cond ∝ I²R
```

Therefore moving a converter from 40 V to 12 V at the same power increases ideal source-current magnitude by about `3.33×`, which increases an equal-resistance `I²R` burden by about `11.1×`.

This means a mechanism that is beneficial at 25–50 V may cease to be beneficial when it adds:

```text
input inductor DCR
extra LV switch RDS(on)
primary winding Rac
bus/contact resistance
circulating/reactive current
```

before X1 completes.

Potential contribution direction, not yet novelty-established:

> Establish whether a normalized loss crossover exists in the extreme-LV / kW-class domain where the additional RMS/conduction burden of current-fed, resonant or multi-mechanism X1 structures exceeds their switching/transformation savings, and derive a fair architecture-selection criterion under a matched product boundary.

Status:

```text
POTENTIAL CONTRIBUTION
NOT YET NOVELTY-ESTABLISHED
```

---

## 9. Mandatory IEEE Prior-Art Matrix for every R candidate

Every retained combination must maintain the following fields:

| Field | Required content |
|---|---|
| Candidate ID | R1...Rn |
| PM set | canonical PM classes |
| Research boundary | Vin / Pout / Vout / phase / isolation contract |
| IEEE Gate A status | mechanism/family prior art |
| Closest IEEE papers | 5–10 when mature |
| Same PM set? | YES / PARTIAL / NO |
| Same main circuit graph? | YES / NEAR / NO / TBD |
| Same gain mechanism? | YES / PARTIAL / NO / TBD |
| Same soft-switching mechanism? | YES / PARTIAL / NO / TBD |
| Same switching states? | YES / NEAR / NO / TBD |
| Same loss question? | YES / PARTIAL / NO / TBD |
| Same analytical result? | YES / PARTIAL / NO / TBD |
| Same operating boundary? | YES / NEAR / NO |
| Same experimental power scale? | YES / NEAR / NO |
| Novelty risk | HIGH / MEDIUM / LOW |
| Research decision | STOP / COMPARATOR / CONTINUE |
| Gate B status | after actual graph |
| Gate C status | after technical findings |

Unknown fields must remain `TBD`; they may not be inferred from paper titles alone.

---

## 10. Stop / continue rule

### STOP deep research when

```text
same/near graph
+
same switching principle
+
same analytical contribution
+
no meaningful boundary-dependent finding
```

The candidate may still be kept as a comparator.

### CONTINUE when at least one strong differentiator is defensible

Examples:

```text
new circuit graph with physically meaningful reduced loss
new operating principle
new analytical design law
new normalized loss crossover
new extreme-LV scaling result
new matched comparison showing a commonly preferred solution reverses ranking
new experimentally validated loss-relocation effect
```

The differentiator must survive Gate C before being called a contribution.

---

## 11. Relationship to existing research files

This file does not delete or invalidate File 36 theoretical calculations.

Instead:

```text
File 36
= theoretical mechanism-combination search space

File 37
= IEEE publication / prior-art control over that search space
```

Where File 36 calls R2/R6 theoretical priorities, File 37 adds the stricter interpretation:

```text
priority for analysis
≠ novelty priority
```

Current override:

```text
R2
= strong comparator / optimized magnetic soft-switching baseline
= NOT mechanism novelty

R6
= close prior-art mechanism combination
= continue only for extreme-LV differentiated analysis
= NOT mechanism-combination novelty

R7 / R8 / R9
= IEEE Gate A required before deep simulation
```

---

## 12. Formal state after File 37

```text
IEEE as primary publication corpus             = ESTABLISHED
IEEE Prior-Art Gate A/B/C                       = MANDATORY
R2 mechanism novelty                            = CLOSED / KNOWN
R2 comparator value                             = RETAINED
R6 mechanism-combination novelty                = CLOSED / CLOSE PRIOR ART
R6 extreme-LV differentiated research           = OPEN
R7 IEEE Gate A                                  = PENDING
R8 IEEE Gate A                                  = PENDING
R9 IEEE Gate A                                  = PENDING
12 V / 2 kW extreme-LV loss crossover novelty  = NOT_ESTABLISHED
methodological novelty                          = NOT_ESTABLISHED
Candidate #10                                   = HOLD
```

## 13. Immediate NEXT

Before any deep R7/R8/R9 simulation:

```text
1. Execute IEEE Gate A for R7.
2. Execute IEEE Gate A for R8.
3. Execute IEEE Gate A for R9 only if it survives CALG-1 minimality interest.
4. Build an IEEE Prior-Art Matrix for R2/R6 using the closest papers.
5. Continue R2/R6 theory only on questions not already closed by IEEE prior art.
```

No energized hardware activity is authorized or required by this file.

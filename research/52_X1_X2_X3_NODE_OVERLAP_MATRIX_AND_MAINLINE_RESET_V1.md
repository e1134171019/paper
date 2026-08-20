# 52 — X1 / X2 / X3 Node-Overlap Matrix and Mainline Reset v1

Status date: 2026-08-20  
Role: `FUNCTIONAL-COORDINATE GRAPH SEARCH / NODE-OVERLAP SCREEN / MAINLINE RESET`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Evidence status: `FIRST-PRINCIPLES / STRUCTURAL SCREEN`  
Simulation status: `NOT EXECUTED`  
IEEE Gate status: `NOT STARTED FOR NEW OVERLAP BRANCHES`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Why this reset is required

Files 49–51 intentionally drilled into one R7 branch. That work remains useful falsification evidence, but it exposed a search-space problem:

```text
R1...R9
mostly vary the L3 mechanism set used around X1,
while X2 was deliberately deferred and X1/X2/X3 physical overlap was not exhaustively enumerated.
```

Therefore the research must not interpret the weak R7 result as exhaustion of the topology space.

The search is reset to the orthogonal architecture question:

> Where are X1, X2 and X3 physically realized, which boundaries between them are real power-stage boundaries, and which functions may share the same switching/energy-transfer state without increasing the 12-V / ~175-A burden?

File 28 remains authoritative:

```text
X1 = first major voltage/current-domain transformation region
X2 = 2ω / bidirectional energy-buffer and routing coordinate
X3 = complete single-phase AC-synthesis region
```

and:

```text
X1, X2, X3 MAY overlap physically.
They are functions, not mandatory serial stages.
```

---

## 2. Normalized node map

The graph search now uses normalized nodes/regions rather than assuming a conventional DC-link architecture.

```text
N0  source terminal / product interface
    12 V battery domain

N1  X1 excitation start
    first main power-switching / conversion edge

N2  intra-X1 energy-transfer state
    magnetic / inductive / capacitive / commutation states

N3  X1 completion boundary
    first sustained reduced-current domain carrying majority power

N4  post-X1 intermediate node
    may be DC, HF-AC, pulsating DC, split rails, multilevel rails, etc.

N5  X2 storage / 2ω routing node if physically distinct

N6  X3 AC-synthesis node/region if physically distinct

N7  output-conditioning boundary
    filter → 220 Vac load
```

Important:

```text
N3 does NOT have to be a 350–360 V DC bus.
```

A valid X1 completion may be a reduced-current HF link or another sustained energy domain if the majority of power has left the source-level current domain.

---

## 3. Single-phase X2 quantitative anchor

For unity-power-factor 220-Vac output at 50 Hz and average power `P = 2 kW`, the instantaneous output power contains a 2ω component:

```text
p_out(t) = P[1 - cos(2ωt)]
```

Therefore the oscillating power amplitude is approximately:

```text
P_2ω,pk = 2 kW
```

The required buffer-energy swing amplitude is:

```text
E_2ω,pk = P/(2ω)
         = P/(4πf)
         ≈ 3.18 J
```

Peak-to-peak energy swing:

```text
≈ 6.37 J
```

If this power ripple were reflected ideally all the way to an unbuffered 12-V source, its current-ripple amplitude scale would be:

```text
I_2ω,source,pk ≈ P/Vin
               ≈ 166.7 A
```

This is not a prediction of A0. It is a first-principles reason why X2 placement cannot remain indefinitely deferred when comparing complete DC→single-phase-AC graphs.

---

## 4. Two independent search axes

The research now separates two axes that were previously easy to mix.

### Axis A — mechanism set

Examples:

```text
R1 = PM1 + PM7
R2 = PM1 + PM4 + PM7
R7 = PM1 + PM3 + PM7
R8 = PM2 + PM3 + PM7
```

This says **what physical mechanisms exist**.

### Axis B — coordinate placement / overlap

Examples:

```text
X1 | X2 | X3          all physically separate
X1+X3 | X2            X1 and X3 share states/network
X1 | X2+X3            X2 and X3 share states/network
X1+X2 | X3            X1 and X2 share states/network
X1+X2+X3              all three overlap
```

This says **where the functions occur and which stage boundaries are removed**.

Formal rule:

```text
same PM set ≠ same architecture graph
```

Example:

```text
PM1 + PM7
```

can describe both:

```text
HFT → rectifier → HV bus → VSI
```

and:

```text
HF-link magnetic transfer → secondary/matrix AC synthesis
```

The mechanism set alone is insufficient to distinguish them.

---

## 5. Node-overlap classes

### O0 — X1 | X2 | X3 physically separate

Canonical structure:

```text
12 V
→ X1 conversion
→ reduced-current / HV node
→ X2 DC-link energy buffer
→ X3 VSI
→ AC
```

Role:

```text
REFERENCE / BASELINE ARCHITECTURE
```

Advantages:

```text
clear functional separation
mature controllability
strong 2ω isolation if HV-link storage is adequate
```

Penalties:

```text
multiple full-power stage boundaries
rectification / DC-link / VSI duplication may remain
component/volume duplication
```

### O13 — X1 + X3 overlap; X2 remains separate

Preferred placement:

```text
X1 starts in LV domain
→ majority power reaches reduced-current HF/intermediate domain
→ the same transfer/switching states complete X1 and synthesize AC polarity/amplitude
→ X2 is kept on a reduced-current or AC-side storage coordinate
```

Conceptual skeleton:

```text
12 V
→ HF primary switching
→ HFT / reduced-current HF link
→ secondary switching / unfolding / matrix state
→ AC envelope
→ filter
→ 220 Vac

X2 = separate reduced-current / AC-side energy buffer
```

Potential structural benefit:

```text
remove or merge:
rectifier boundary
full stiff HV-DC-link requirement
independent VSI power-processing boundary
```

Critical requirement:

```text
AC-synthesis integration must NOT add a new full-current series edge before X1 completion.
```

Status:

```text
PRIMARY NEXT COORDINATE BRANCH
ACTUAL GRAPH = NOT YET LOCKED
IEEE GATE A = NOT STARTED
NOVELTY = NOT_ESTABLISHED
```

### O23 — X1 separate; X2 + X3 overlap post-X1

Skeleton:

```text
12 V
→ conventional/optimized X1
→ reduced-current domain
→ shared storage + AC-synthesis network
→ 220 Vac
```

Possible functional intent:

```text
flying/split/differential storage capacitors
serve both AC synthesis and 2ω energy handling
```

Potential benefit:

```text
reduce dedicated bulky DC-link/storage duplication
keep added complexity after current reduction
```

Limitation:

```text
does not directly solve pre-X1 175-A conduction burden
```

Status:

```text
SECONDARY PRIORITY
PROMISING FOR VOLUME / X2-X3 INTEGRATION
NOT YET A TOPOLOGY CANDIDATE
```

### O12 — X1 + X2 overlap; X3 separate

Skeleton:

```text
12 V
→ X1 network also absorbs/routes 2ω energy
→ reduced-current DC/other node
→ separate X3
```

Potential benefit:

```text
remove a separate buffer stage
```

Major risk:

```text
2ω energy handling may modulate/circulate current inside the 12-V / ~175-A X1 path
```

Admission rule:

```text
O12 is low priority unless the X2 energy path is demonstrably outside the full-source-current series path or is realized mainly after current reduction inside distributed X1.
```

Status:

```text
CONDITIONAL / DEPRIORITIZED
```

### O123 — X1 + X2 + X3 all overlap

Concept:

```text
one integrated switching/energy-storage graph performs
voltage/current-domain transformation
+ 2ω energy routing
+ AC synthesis
```

Potential benefit:

```text
minimum explicit stage count
maximum opportunity for shared devices/states
```

Major risks:

```text
interaction loss
circulating RMS
control coupling
startup/precharge complexity
2ω reflection into LV source
fault isolation complexity
loss attribution becomes difficult
```

Status:

```text
RESERVE / HIGH-RISK HIGH-INTEGRATION
NOT FIRST SYNTHESIS PRIORITY
```

---

## 6. Location rule — overlap is not automatically beneficial

The same overlap has very different loss implications depending on **where** it occurs relative to X1 completion.

### L0 — pre-X1 overlap

```text
function-sharing while ~175 A still flows
```

Penalty sensitivity:

```text
0.10 mΩ added full-current resistance ≈ 3.08 W
0.50 mΩ ≈ 15.39 W
0.65 mΩ ≈ 20 W
```

Therefore any X2/X3 integration that adds source-domain switch/inductor/circulation edges receives a severe penalty.

### L1 — inside X1 but near completion

Potentially acceptable if:

```text
added function shares existing switching edges
and does not materially increase source-domain RMS
```

This is the main target region for O13.

### L2 — post-X1 overlap

```text
additional switching/storage occurs after substantial current reduction
```

This is structurally cheaper in `I²R` terms and is the preferred location for O23 and for distinct X2 functions.

Formal rule:

```text
OVERLAP QUALITY
= function sharing benefit
- added RMS/commutation/circulation burden at the overlap location
```

---

## 7. First structural ranking matrix

This is a qualitative first-principles screen, not an efficiency prediction.

| Class | Stage-boundary reduction | LV 2ω isolation potential | Added pre-X1 burden risk | Interaction risk | Current priority |
|---|---|---|---|---|---|
| O0 `X1|X2|X3` | LOW | HIGH | depends on X1 | LOW | REFERENCE |
| O13 `X1+X3|X2` | HIGH | HIGH if X2 stays separate/post-X1 | LOW–MED if overlap near X1 completion | MED | **PRIMARY** |
| O23 `X1|X2+X3` | MED–HIGH | HIGH | LOW | MED | **SECONDARY** |
| O12 `X1+X2|X3` | MED | LOW–MED | **HIGH** if 2ω enters LV path | MED–HIGH | DEPRIORITIZE |
| O123 `X1+X2+X3` | MAX | uncertain | HIGH unless graph is exceptional | **HIGH** | RESERVE |

The ranking follows the project loss authority, not novelty:

```text
1. avoid added all-current edges in the 12-V domain
2. eliminate duplicated full-power boundaries where possible
3. keep the unavoidable 2ω energy swing from becoming source-domain RMS burden
4. count interaction/circulating loss explicitly
```

---

## 8. Reclassification of recent R7 work

R7 work remains valid evidence but is no longer the immediate mainline.

```text
R7-C1A
= known-block cascade / STOP as topology novelty

R7-C1B
= known voltage-doubler primitive / STOP

R7 gain-sharing k=2/k=3
= WEAK / CONDITIONAL physical branch
```

File 51's transformer-geometry crossover is now:

```text
DEFERRED
```

not deleted.

Reason:

```text
The current search-space question is broader than whether PM3 can reduce one magnetic burden.
We must first test whether removing/merging whole functional stage boundaries at X1/X3 or X2/X3 gives a stronger structural opportunity.
```

---

## 9. Mechanism combinations reopened by the coordinate matrix

### 9.1 R1 must be split by coordinate graph

Original:

```text
R1 = PM1 + PM7
```

This is no longer treated as one architecture.

At minimum:

```text
R1-S = PM1 + PM7 with X1 and X3 physically separate
       reference / #02-like

R1-O13 = PM1 + PM7 with X1 and X3 physically overlapping
         direct-HF-link / secondary-synthesis search branch
```

This is a major reopened branch because the mechanism set is simple while the architecture can remove full-power boundaries.

### 9.2 X2 mechanisms return to active search

File 36 deliberately deferred PM5/PM6. File 52 reopens them, but with placement control:

```text
PM5 = capacitive field-energy buffering
PM6 = controlled bidirectional storage-port transfer
```

They are not automatically added to X1.

Preferred initial placement:

```text
post-X1 / reduced-current domain
or
shared with X3 if that removes duplicate storage/synthesis hardware
```

### 9.3 No automatic new R-number yet

File 52 changes architecture placement before creating another mechanism-combination ID.

Formal rule:

```text
Do not create R10/R11 merely because X1/X2/X3 overlap differently.
First lock the actual graph and identify whether the physical mechanism set truly changed.
```

---

## 10. Immediate next graph candidates

The coordinate screen authorizes **graph synthesis**, not PSIM.

### G13-A — reduced-current HF-link + secondary AC synthesis

Required constraints:

```text
- PM1 carries X1
- X3 shares secondary/HF-link switching states near X1 completion
- no full-power diode bridge + stiff 360-V DC bus + independent VSI sequence unless functionally required
- X2 remains separately identifiable and is preferentially post-X1 / AC-side
- no added full-current LV series switch solely for AC polarity synthesis
```

Status:

```text
PRIMARY ACTUAL-GRAPH TARGET
```

### G23-A — post-X1 shared X2/X3 storage-synthesis network

Required constraints:

```text
- X1 completes first
- X2 storage elements participate directly in X3 voltage-state synthesis
- 2ω buffer function and AC synthesis use shared capacitors/switch states
- added capacitor RMS / balancing / semiconductor loss must be explicit
```

Status:

```text
SECOND ACTUAL-GRAPH TARGET
```

### G123-A — fully integrated reserve

Do not synthesize until G13-A/G23-A fail or reveal a missing function.

---

## 11. Pre-simulation gates for G13-A / G23-A

Every graph must pass, in order:

```text
1. exact node / edge / state closure
2. X1 start and completion proof
3. X2 energy-balance closure (~3.18-J amplitude at 2 kW / 50 Hz)
4. X3 AC synthesis closure
5. pre-X1 full-current edge count / equivalent resistance
6. charge / flux / energy conservation
7. physical loss lower/upper bounds
8. interaction-loss audit
9. multi-assistant IEEE Gate A/B
10. only then PSIM/LTspice
```

PSIM remains unauthorized at this file.

---

## 12. Mainline decision

Effective immediately:

```text
R2 / Ryan
→ comparator only / paused

R7
→ weak conditional branch / deferred

R8
→ dense-prior-art comparator / low priority

O13 = X1+X3 with separate/post-X1 X2
→ PRIMARY MAINLINE

O23 = X2+X3 after X1 completion
→ SECONDARY MAINLINE

O12
→ conditional / generally penalized by 2ω interaction with extreme-LV path

O123
→ reserve / high interaction risk
```

Research interpretation:

> The project has not exhausted the node space. The previous R1–R9 work explored mechanism combinations primarily around X1. File 52 adds the missing coordinate-placement axis and moves the mainline toward functional-stage overlap that can remove duplicated full-power conversion boundaries without adding new 175-A source-domain impedance.

Candidate #10 remains `HOLD / NOT_ASSIGNED` and novelty remains `NOT_ESTABLISHED`.

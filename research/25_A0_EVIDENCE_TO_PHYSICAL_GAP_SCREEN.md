# 25 — A0 Evidence → Physical-Gap Screen

Status date: 2026-08-19  
Role: `PHYSICAL GAP VALIDATION / RESEARCH-PROBLEM SCREEN`  
A0 role: `REAL-PRODUCT EVIDENCE SOURCE — NOT OPTIMIZATION TARGET`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This document prevents the A0 reverse-engineering work from drifting into product optimization.

ASP-2000 R52 is used only to answer:

> Which loss mechanisms are actually present in a competent 12 V / kW-class product, which are merely implementation/product-engineering overhead, and which may indicate a topology-level physical gap worth comparing across X1 mechanisms?

The objective is **not**:

```text
make ASP-2000 better
replace ASP parts
optimize its snubber values
redesign its transformer
reduce its BOM
```

The objective is:

```text
A0 evidence
→ loss-mechanism abstraction
→ physical-gap hypothesis
→ matched mechanism comparison
→ topology synthesis only if a gap survives
```

---

## 2. Evidence classes used in this screen

```text
PE — PRODUCT ENGINEERING
A real loss / function in A0, but not evidence by itself that a new power-path topology is required.

TS — TOPOLOGY-STRUCTURAL SIGNAL
A0 contains direct evidence of a mechanism that may be tied to the chosen X1 energy path rather than only to implementation quality.

PG — PHYSICAL-GAP HYPOTHESIS
A cross-architecture research question that can survive abstraction away from ASP.

OPEN — NOT ENOUGH EVIDENCE
Do not promote to a research gap yet.
```

A component-level loss may contribute evidence to a PG without the component itself becoming the research target.

Example:

```text
A0 has RC snubber loss
→ do NOT conclude "optimize R110/R119"
→ ask whether the chosen X1 commutation mechanism intrinsically disposes significant leakage/Coss energy dissipatively
```

---

## 3. A0 findings that are PRODUCT ENGINEERING, not topology proof

### PE-1 — PCB / connector / common-copper resistance

Current manufacturing-aware geometry bound:

```text
R52 finished copper >82 µm
partial positive PCB-only geometry loss ≤~4.98 W @175.4 A
```

Classification:

```text
PE / CONSTRAINT
```

Reason:

- heavy copper, busbar, connector geometry and current spreading can improve this without changing the main conversion topology;
- the earlier 35.56 µm model was superseded by the R52 manufacturing specification;
- therefore PCB copper is material but no longer evidence of a dominant topology deficiency.

Research use:

```text
retain "minimize unavoidable full-current common impedance"
reject "shorter PCB path = new topology contribution"
```

### PE-2 — fuses, J8, contacts and local feed hardware

These are real product losses and must be counted under a product-level contract, but they are primarily packaging/protection/interconnect engineering.

```text
classification = PE
```

A candidate cannot delete required functions only on its side, but improving fuse/contact/busbar details does not establish a new X1 mechanism.

### PE-3 — Q39...Q65 battery-interface bank / BOCP

A0 product evidence establishes reverse-polarity protection and B↔BAT− analog sensing.

```text
classification = PE / PRODUCT FUNCTION
```

Its ~7.47 W datasheet scale is not intrinsic magnetic-X1 loss.

Valid use:

```text
Contract P → match equivalent function
Contract C → exclude equally
```

Invalid use:

```text
delete protection on candidate
→ count removed watts as topology gain
```

### PE-4 — RL1 + R40/R41 precharge

```text
classification = PE / STARTUP FUNCTION
```

R40/R41 startup energy and RL1 contact behavior belong to HV-link inrush/precharge implementation. They are not proof of a steady-state X1 physical gap.

### PE-5 — U5 / R212 / R213 stuffing choice and local driver implementation

The R52 design supports direct-bypass and buffered command-distribution options.

```text
classification = PE / IMPLEMENTATION DETAIL
```

Production stuffing affects timing and switching loss, but choosing one driver IC or stuffing option is not the research question.

### PE-6 — RC snubber component-value tuning

The existence of the snubber is mechanism evidence; the exact resistor/capacitor tuning is product engineering.

```text
R110/R119/C62/C65 value optimization = PE
```

Do not turn the research into an R/C tuning exercise.

---

## 4. PG-1 — Minimum extreme-LV full-current exposure before X1

### Research question

> For 12–24 V / 1–3 kW conversion, how much conduction loss is structurally unavoidable while power remains in the extreme-low-voltage / hundred-ampere domain before the first major impedance/current-domain transformation?

This is more precise than saying:

```text
"12 V has high current"
```

because source average current is unavoidable. The variable is **how much hardware and how much RMS-current exposure remain in that domain before X1, and what added loss is required to leave it earlier.**

### A0 evidence

```text
12 V / 2 kW ideal source current ≈166.7 A
95%-reference source current ≈175.4 A
A0 uses 10-MOS A switch + 10-MOS C switch
main-MOS 25°C datasheet conduction scale ≈12.3 W
R52 already uses heavy manufactured copper >82 µm
```

A0 therefore already applies substantial conventional mitigation:

```text
heavy copper
parallel silicon
multiple magnetic paths
local gate driving
early magnetic X1
```

### Status

```text
PG-1 = HYPOTHESIS / TOPOLOGY-RELEVANT
```

Why not VERIFIED:

- actual hot A/C conduction loss is not measured;
- branch/current waveform is not yet closed;
- a fair A1 may reduce this further without changing family.

### Discriminating evidence

Only measure enough to establish the mechanism:

```text
A/C switch current waveform or defensible bank-current proxy
actual on-state VDS / hot effective resistance
source / transformer RMS current
```

The research output is not "which MOS should ASP use?". It is whether a different X1 mechanism materially reduces total extreme-LV RMS/conduction exposure after all added losses are counted.

---

## 5. PG-2 — Dissipative commutation / leakage-energy handling at X1

### Research question

> Does the early magnetic X1 require a material amount of switching/leakage/Coss energy to be dissipated during commutation, and can another X1 mechanism reduce or recover that energy with lower total added loss?

### A0 structural signal

Direct A/C adjacency reconstruction establishes two passive series-RC branches across the primary switched nodes and no direct diode/TVS/active recovery branch attached to those A/C nodes.

Therefore:

```text
direct primary-node damping = passive dissipative RC network
```

This is a stronger research signal than the exact R/C values.

### Status

```text
PG-2 = HYPOTHESIS / STRONG STRUCTURAL SIGNAL
```

Not yet a verified gap because:

```text
P_snubber = OPEN
P_switching overlap = OPEN
leakage processed energy = OPEN
```

### Falsifier

If measured:

```text
P_snubber + avoidable commutation loss
```

is small compared with conduction/magnetic loss, do not build a research direction around energy recovery or soft commutation.

### Go condition

Only retain a soft-commutation / recovery research direction if:

```text
P_saved,commutation > P_added,resonant/recovery/control/circulation
```

Do not optimize ASP's snubber as the main research deliverable.

---

## 6. PG-3 — Magnetic transformation burden under extreme conversion ratio

### Research question

> After fair optimization, does an HFT-based early X1 incur a structural copper/core/leakage burden that remains materially higher than alternative X1 mechanisms at 12 V-class input and ~311 Vpk-class output requirement?

### A0 evidence

Verified:

```text
2 × PQ5050
center-tapped primaries
shared A/C logical switches
series / collective secondary formation
```

Not established:

```text
correct populated transformer P/N
turns ratio
A0 Lm/Lk
winding DCR/Rac
core material / Ae / Ve
actual magnetic watts
```

The separate `M1-PQ50-V121-A` data belongs to a different ASP-3000/24 V variant and remains context only.

### Status

```text
PG-3 = OPEN / NOT YET A GAP
```

Important discipline:

```text
"uses two PQ5050 transformers"
≠
"magnetics are the problem"
```

A1 exists specifically to prevent an unfair conclusion based on an unoptimized or incompletely characterized magnetic reference.

### Minimum closure

Use only evidence that distinguishes mechanism-level burden:

```text
T1/T2 RMS current
primary volt-second
transformer temperature / loss estimate
correct ratio/L/DCR/material when available
```

Do not redesign the ASP transformer as the research task.

---

## 7. PG-4 — Single-phase 2ω energy reflection into the LV domain

### Research question

> How much of the unavoidable single-phase 2ω pulsating power is reflected back through the expensive 12 V current path, and is local post-X1 buffering net-beneficial?

Single-phase output imposes a fundamental power pulsation. The research issue is its **energy-routing location**, not whether 2ω exists.

### A0 evidence

A0 contains a passive HV DC-link after X1, but current evidence does not establish how strongly source-side 100/120 Hz ripple remains.

### Status

```text
PG-4 = HYPOTHESIS / NOT ESTABLISHED
active X2 = OPTIONAL / NOT PROVEN
```

### Minimum discriminating measurement

```text
source current spectrum / waveform at 100 or120 Hz
HV DC-link ripple
same load point / same cooling
```

### Falsifier

If the passive HV link already keeps source 2ω sufficiently small, an active X2 is not justified.

Retention rule remains:

```text
P_LV,saved > P_X2,added
```

---

## 8. Items that are dimensions/falsifiers, not independent research gaps

### Early fan-out / N-way sharing

```text
NOT A GAP
NOT A NOVELTY CLAIM
```

It is a design dimension that may help PG-1 only if total equivalent conduction/commutation loss falls.

### More parallel MOS

```text
NOT A GAP
```

A0 already uses heavy silicon paralleling. More devices trade conduction against Qg/Coss/commutation/cost/area.

### Earlier voltage rise

```text
STRATEGY / NOT A GAP
```

It is useful only if the mechanism that raises voltage early has lower total loss.

### Active buffering

```text
SOLUTION HYPOTHESIS / NOT A GAP
```

It is only relevant if PG-4 survives measurement.

### "Remove the HV DC bus"

```text
ARCHITECTURE OPTION / NOT A GAP
```

Direct-HFL must prove that removed rectifier/DC-link/VSI losses exceed added bidirectional switching, commutation and circulating RMS.

---

## 9. Research stop-line for A0 reverse engineering

A0 structural reverse engineering is now sufficient for research screening.

Do **not** continue tracing arbitrary ASP components unless the result discriminates PG-1…PG-4.

### Continue A0 work only if it answers one of:

```text
PG-1: actual extreme-LV conduction exposure?
PG-2: actual commutation/snubber/switching energy?
PG-3: actual magnetic burden?
PG-4: actual 2ω reflection?
```

### Stop / defer if the task is only:

```text
which replacement part improves ASP?
which PCB trace can be widened?
which snubber value is better?
which relay/contact should be used?
which gate-driver stuffing is cheaper/faster?
```

unless that item is needed as evidence for one of the four PG hypotheses.

---

## 10. Minimum hypothesis-driven hardware gate

The former plan of completely closing every A0 watt before any mechanism comparison is unnecessarily broad for the research question.

Use a minimum discriminating set.

### H1 — PG-1 conduction exposure

```text
I_source
I_T1 / I_T2 if accessible
A/C on-state VDS/current evidence
switch/device temperature
```

Output:

```text
measured/bounded pre-X1 conduction scale
```

### H2 — PG-2 commutation

```text
fs / duty / dead time
V_A-B / V_C-B
relevant switch current
V_R110 / V_R119
```

Output:

```text
P_switching / overlap scale
P_snubber
commutation significance
```

### H3 — PG-3 magnetics

```text
T1/T2 RMS current
primary voltage / volt-second
transformer temperature
correct L/ratio/DCR/material when obtainable
```

Output:

```text
magnetic-loss burden / uncertainty bound
```

### H4 — PG-4 2ω routing

```text
source current waveform/spectrum
HV-link ripple
```

Output:

```text
2ω source-reflection scale
```

These measurements are **research-hypothesis discriminators**, not an ASP optimization campaign.

---

## 11. Cross-X1 comparison axes after this screen

A1 / Direct-HFL / non-isolated high-gain / any later candidate must be compared on the same mechanism axes:

```text
M1 — extreme-LV RMS / conduction exposure before X1
M2 — commutation / switching / dissipative-clamp energy
M3 — magnetic or alternative energy-storage/conversion burden
M4 — internal circulating/reactive current
M5 — 2ω energy reflected to the LV source
M6 — number and loss of added active processing functions
M7 — isolation / protection / product functions under matched contract
```

No architecture wins merely by deleting a stage; removed loss must exceed added loss.

---

## 12. Decision after A0 screen

Current classification:

```text
PCB/common copper                         = PE / CONSTRAINT
Fuse/J8/contact/local interconnect        = PE
Battery reverse-protection / BOCP         = PE / PRODUCT FUNCTION
RL1 precharge                             = PE / STARTUP FUNCTION
U5 / local driver stuffing                = PE
RC snubber value tuning                   = PE

PG-1 extreme-LV conduction exposure       = HYPOTHESIS / TOPOLOGY-RELEVANT
PG-2 dissipative commutation handling     = HYPOTHESIS / STRONG STRUCTURAL SIGNAL
PG-3 magnetic transformation burden       = OPEN / NOT YET A GAP
PG-4 2ω source-energy reflection          = HYPOTHESIS / NOT ESTABLISHED

Candidate #10                             = HOLD / NOT_ASSIGNED
Novelty                                   = NOT_ESTABLISHED
```

### Current research sequence

```text
A0 structural evidence freeze
↓
Physical-gap screen                        ← CURRENT
↓
minimum H1–H4 discriminating evidence
↓
A1 / Direct-HFL / non-isolated X1 mechanism comparison
↓
reject gaps that disappear under fair optimization
↓
only then topology synthesis
↓
Candidate #10 only if a physical gap survives existing families
```

This supersedes any workflow that treats exhaustive ASP optimization as the next research stage.

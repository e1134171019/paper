# 2026-09-16 — Delta → Trade-Off → Residual-RQ Traceability Matrix v1

Status: `WORKING_BRANCH / TRACEABILITY / PRE-COMBINATION / PRE-MATH`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

This file performs the next step after the lineage / improvement-Delta search.

The objective is no longer to ask only:

```text
Which Delta blocks look compatible?
```

Instead every Delta is traced through:

```text
Delta
-> what problem it actually solves
-> what burden it creates or relocates
-> which repeated trade-off it belongs to
-> which residual research question it can inform
-> where it could physically live inside the 12 V / 2 kW boundary
```

Only after this traceability is clear should a W1/W2 circuit candidate be synthesized.

---

## 2. Canonical-ID correction

The v1 and v2 working files accidentally reused a few Delta IDs for different descendants. This file does **not** silently overwrite them. It introduces a canonical registry for forward use.

Canonicalization rules:

```text
A1...A9  = Push-Pull / Current-Fed / Weinberg lineage
B1...B6  = Y / quasi-Y / impedance-source lineage
C1...C7  = LLC / reconfigurable-ratio / secondary-state lineage
D1...D5  = DAB / MAB / QAB / SST multiport lineage
E1...E5  = Matrix-transformer / integrated-magnetics lineage
```

Resolved collisions:

- old v2 `Delta-C4` (secondary selection changes both `Neff` and `Lr`) is treated as a **refinement of canonical C3**, not a separate unrelated C4.
- canonical `C4` remains the adjustable-ratio / near-fixed-frequency DCX-like operation step.
- old v2 `Delta-D1` (current-fed MAB with deliberate decoupling) is treated as **D2a**, a concrete implementation of canonical D2 hardware decoupling.
- old v2 star-shaped MWT `Delta-D2` is moved to the integrated-magnetics family as canonical **E3**.
- old v2 `Delta-E3` (matrix winding arrangement realizes target leakage) becomes canonical **E4**.
- old v2 `Delta-E4` (reluctance-controlled noninteger ratio) becomes canonical **E5**.

No source is deleted; only the working identifiers are normalized.

---

## 3. Repeated trade-off axes

`TO-1` — low-voltage current distribution vs copper / termination / duplicated-device burden  
`TO-2` — integrated leakage / resonant function vs port decoupling  
`TO-3` — structural gain / reconfiguration vs transition, circulation and connection stress  
`TO-4` — soft switching vs reactive RMS / capacitor / winding burden  
`TO-5` — magnetic integration vs manufacturability, tolerance and controllability  
`TO-6` — lower semiconductor count vs current concentration / shared-fault responsibility  
`TO-7` — low input ripple vs hidden stored-energy / capacitor / core burden  
`TO-8` — peer multiwinding power ports vs cross-coupling and control interaction  
`TO-9` — winding-role reassignment vs power continuity / legal transition states  
`TO-10` — full-power processing vs partial-power / correction-path processing

These are not assumptions that every improvement has an equal penalty. They are repeated engineering tensions observed across the collected lineages.

---

## 4. Residual research questions

### RQ-A — Equal-resource low-side benefit

Under approximately equal total copper, semiconductor and magnetic resources, can a multiwinding / matrix structure actually reduce the 12-V-side total loss or local stress, rather than only splitting the same `I^2R` burden among more paths?

### RQ-B — How much inductive function should be integrated?

Can a useful design region be established in which enough leakage / differential inductance is retained for commutation or resonance, but not so much that port cross-coupling, circulating current and RMS loss dominate?

Conceptually:

```text
L_required_for_commutation <= L_selected <= L_max_before_circulation_penalty
```

### RQ-C — One physical state controls more than one useful quantity

Can one legal winding / magnetic state produce a useful coupled change such as:

```text
q -> {Neff(q), Zref(q), Lcomm(q)}
```

without inserting a prohibitive extra selector loss into the raw 12-V / hundred-ampere path?

### RQ-D — Separate bulk-power and commutation functions inside one magnetic assembly

Can the same magnetic structure carry bulk transfer in one mode and commutation / balancing energy in another mode while the saved switching loss exceeds the added copper/core/reactive loss?

### RQ-E — Small processed-power path controlling a larger bulk path

Can a lower-VA winding / port perform correction, regulation or state control while processing only a fraction

```text
alpha = |Preg| / Pout
```

of the 2-kW output power?

---

# 5. Traceability matrix

Legend for physical placement:

- `RAW-12V`: directly in the 12-V high-current domain.
- `POST-RISE`: after the first meaningful voltage rise, current already reduced.
- `SECONDARY`: high-voltage / lower-current winding or rectifier side.
- `MAGNETIC`: mainly implemented by magnetic geometry / winding arrangement.
- `SYSTEM`: architecture-level; not a local W1/W2 block by itself.

| Canonical Delta | Documented change | What it solves / adds | Main burden created or relocated | Likely placement | Trade-off axes | Residual RQ contribution | Transplantability |
|---|---|---|---|---|---|---|---|
| `A1` | Push-Pull → Current-Fed Push-Pull | continuous source current; controllable current slope before HFT | input inductor copper/core loss; current-source path can never be opened illegally | RAW-12V | TO-1, TO-7 | RQ-A | CONDITIONAL |
| `A2` | CFPP → 3-phase CFPP | distributes transfer over phase-shifted branches; lower input/output ripple | more branches, coupling, matching and magnetic complexity | RAW-12V + MAGNETIC | TO-1, TO-7, TO-8 | RQ-A, RQ-D | CONDITIONAL |
| `A3` | 3-phase CFPP → active-clamp CFPP | leakage spike suppression; leakage energy reused for ZVS | clamp switch/capacitor; reactive/circulating current | RAW-12V / POST-RISE | TO-2, TO-4 | RQ-B, RQ-D | YES, mechanism-level |
| `A4` | efficiency-aware CFPP operating-point optimization | exposes that minimum ripple and maximum efficiency do not coincide | no new graph; adds design constraint on duty/core region | ANALYTICAL | TO-4, TO-7 | RQ-A, RQ-B | YES, as falsification rule |
| `A5` | Weinberg multi-interval transfer/storage donor | useful transfer can occur in distinct intervals instead of one fixed role | interval-specific stress and control | RAW-12V / MAGNETIC | TO-9 | RQ-D | CONDITIONAL |
| `A6` | active-clamp CFPP + primary blocking capacitor | blocks sustained dc-flux bias while retaining clamp/ZVS | capacitor RMS/stored-energy stress; new resonance | RAW-12V, but high-current penalty severe | TO-4, TO-5, TO-7 | RQ-D | CONDITIONAL; raw-side capacitor must be loss-checked |
| `A7` | resonant Push-Pull reuses `Llk`, `Lm`, transformer capacitance | reduces separate resonant parts; ZVS/ZCS | resonance becomes geometry/tolerance sensitive; RMS risk | MAGNETIC + RAW-12V | TO-2, TO-4, TO-5 | RQ-B, RQ-D | HIGH conceptual value |
| `A8` | Weinberg leakage selected from target switching loss | converts `Llk` from accident to mathematically chosen design variable | larger leakage can increase output-cap RMS / degrade output quality | ANALYTICAL + MAGNETIC | TO-2, TO-4 | RQ-B | HIGH as design-law donor |
| `A9` | PSR active-clamp Weinberg | soft switching + primary-side estimation reduces reliance on optocoupler feedback | estimator/control dependence; clamp hardware remains | CONTROL + MAGNETIC | TO-9 | RQ-E secondary relevance | LOW/MEDIUM for power graph; useful for winding-role reassignment |
| `B1` | Y-source → quasi-Y | continuous input current and dc blocking while retaining winding-factor gain | more storage states / transient sensitivity | RAW-12V | TO-3, TO-7 | RQ-A, RQ-C | CONDITIONAL |
| `B2` | Y / improved-Y → active-clamped Y | suppresses leakage spike; recycles leakage energy | extra devices and control; possible reactive current | RAW-12V / POST-RISE | TO-2, TO-4 | RQ-B, RQ-D | YES, mechanism-level |
| `B3` | quasi-Y → active-clamped quasi-Y | combines continuous-input behavior with leakage recovery | cumulative component/state complexity | RAW-12V | TO-3, TO-4, TO-7 | RQ-A, RQ-B | CONDITIONAL |
| `B4` | Y-source + quasi-Z hybrid | combines magnetic gain law with smoother/continuous input path | more stored-energy elements and parasitic-sensitive states | RAW-12V | TO-3, TO-7 | RQ-A, RQ-C | CONDITIONAL |
| `B5` | Y-source + zero-input-ripple / extended-ZVS branch | shapes switch-transition current while reducing input ripple and dc bias | hidden reactive/RMS current, added branch/capacitors | RAW-12V | TO-4, TO-7 | RQ-A, RQ-D | CONDITIONAL |
| `B6` | Y-source leakage + quasi-resonance + switched-cap clamp | `Llk` sets `di/dt`, supports ZCS and feeds clamp/stack node | multi-mechanism current stress and more storage paths | RAW-12V / POST-RISE | TO-2, TO-3, TO-4 | RQ-B, RQ-D | CONDITIONAL |
| `C1` | fixed-ratio LLC → adjustable-turn LLC | coarse gain change without extreme frequency sweep | ratio-state switch/transition stress | SECONDARY preferred | TO-3 | RQ-C | YES, especially if selector is off raw 12-V path |
| `C2` | split-HB phase state controls center-limb flux and effective ratio | changes magnetic ratio without increasing total switch/diode count in source design | magnetic-state interaction and phase-control dependence | MAGNETIC + bridge | TO-3, TO-5 | RQ-C | HIGH conceptual value |
| `C3` | reconfigurable secondary LLC; winding selection changes `Neff`, and in the documented implementation also `Lr` | structural output regulation; state simultaneously affects ratio and leakage | secondary switch stress; both modes need valid resonant/ZVS operation | SECONDARY | TO-2, TO-3, TO-9 | RQ-B, RQ-C | VERY HIGH donor for coupled-state question |
| `C4` | adjustable-turn LLC near fixed resonance / DCX-like operation | coarse structural gain keeps resonant tank near efficient region | discrete gain management / mode transitions | SECONDARY + MAGNETIC | TO-3, TO-4 | RQ-C | YES |
| `C5` | multibridge-leg turn-ratio reconfiguration | uses existing bridge legs as structural ratio actuators; lowers inductor RMS and extends ZVS range | state coupling; extra bridge-leg constraints | POST-RISE / SECONDARY preferred | TO-3, TO-6 | RQ-C | HIGH if raw-side selector avoided |
| `C6` | adjustable-turn + voltage-doubling multimode rectifier | puts coarse gain on lower-current side; keeps resonance near optimum | more rectifier states/capacitors; transition sequencing | SECONDARY | TO-3, TO-9 | RQ-C | HIGH |
| `C7` | matrix-transformer LLC + selective secondary phase shift | selected winding temporarily changes role / partial-short to inject tank energy | local circulation, synchronization, partial-short stress | SECONDARY + MAGNETIC | TO-4, TO-9 | RQ-D | CONDITIONAL but conceptually strong |
| `D1` | DAB → MAB | converts windings into peer active power ports / shared magnetic router | port cross-coupling, circulating power, harder control | SYSTEM + MAGNETIC | TO-8 | RQ-D, RQ-E | ARCHITECTURE donor |
| `D2` | hardware-decoupled MAB | modifies inductance/coupling graph so ports are less strongly coupled | more inductors / reduced integration / added magnetics | MAGNETIC + POST-RISE | TO-2, TO-5, TO-8 | RQ-B | HIGH counterexample / falsification donor |
| `D2a` | current-fed MAB with deliberate external inductors | concrete case where selected inductive functions are externalized for inherent balancing/decoupling | external inductor count / volume | RAW-12V + MAGNETIC | TO-2, TO-8 | RQ-B, RQ-A | HIGH counterexample to “integrate everything” |
| `D3` | MAB → reduced-switch MAB / RS-SQAB | shares bridge legs and reduces duplicated semiconductor / HFT resources | shared-device current concentration and fault/state coupling | POST-RISE / SYSTEM | TO-6 | RQ-E, indirectly RQ-A | CONDITIONAL |
| `D4` | QAB → open-winding QAB | endpoint accessibility adds fault/reconfiguration states | more endpoint/control complexity; not directly a gain benefit | SYSTEM + MAGNETIC | TO-9 | RQ-C, RQ-D secondary relevance | LOW for first candidate, retain as structural donor |
| `D5` | modular MAB → MWT + shared HF link | shares HF infrastructure across several magnetic substructures | coupling/control architecture complexity | SYSTEM | TO-5, TO-8, TO-10 | RQ-E | ARCHITECTURE donor |
| `E1` | conventional HFT → matrix transformer | current distribution, flux cancellation, lower termination/AC resistance through geometry | manufacturing / layout complexity | MAGNETIC | TO-1, TO-5 | RQ-A | VERY HIGH for 12-V boundary |
| `E2` | matrix HFT → intentional leakage via PCB/shield geometry | HFT also acts as resonant inductor | reactive RMS and tolerance sensitivity | MAGNETIC | TO-2, TO-4, TO-5 | RQ-B, RQ-D | VERY HIGH |
| `E3` | generic MWT → radially symmetric star-shaped MWT with controlled leakage | strong bulk coupling plus designed port leakage / symmetry | 3-D magnetic complexity and fabrication constraints | MAGNETIC | TO-2, TO-5, TO-8 | RQ-B, RQ-D | VERY HIGH |
| `E4` | matrix winding arrangement directly sets target leakage | obtains resonant inductance without extra core legs | leakage tolerance tied to winding placement | MAGNETIC | TO-2, TO-5 | RQ-B | HIGH |
| `E5` | planar transformer → reluctance-controlled noninteger effective ratio | uses magnetic reluctance / flux split to obtain finer `Neff` than integer turns permit | sensitivity to magnetic tolerances, flux balance and saturation | MAGNETIC | TO-3, TO-5 | RQ-C | HIGH conceptual value |

---

# 6. What the matrix says before any new circuit is drawn

## 6.1 RQ-A is not simply “parallel more windings”

The relevant donors are:

```text
A1, A2, B1, B4, D2a, E1
```

But only `E1` directly attacks physical termination / winding-current geometry rather than merely changing source-current waveform or branch count.

Therefore the correct RQ-A comparison must hold approximately constant:

```text
total copper volume / mass
semiconductor conduction area or total Rdson resource
core material / usable flux density
switching frequency
power and voltage boundary
```

Then compare:

```text
Pcu_winding
+ Ptermination
+ PMOS_cond
+ Pcore
+ extra branch loss
```

If a multiwinding split only duplicates hardware and produces the same aggregate `I^2R`, it does not close RQ-A.

---

## 6.2 RQ-B now has a genuine two-sided literature conflict

Integration donors:

```text
A3, A7, A8, B2, B6, E2, E3, E4
```

Decoupling donors:

```text
D2, D2a
```

So RQ-B should not be framed as:

```text
Can leakage be used beneficially?
```

That is already established in many lineages.

The stronger question is:

```text
For a multiwinding low-voltage/high-current converter,
which leakage / modal inductance should be shared and which should be decoupled?
```

Candidate mathematical closure later must contain at least:

```text
0.5 * Lcomm * Icomm^2 >= Etransition_required
```

and an upper-side penalty relation containing circulating / cross-port RMS current.

The research target is therefore a **window or design boundary**, not simply maximum integration.

---

## 6.3 RQ-C is already partially demonstrated by literature, so our question must move one step further

Strong donors:

```text
C2, C3, C5, C6, E5
```

The literature already demonstrates that connection / phase / magnetic state can alter effective turns ratio. `C3` further shows that winding selection can also change resonant leakage.

Therefore a weak statement such as:

```text
“we propose a variable turns-ratio transformer”
```

is not enough.

The residual project question should instead be something like:

```text
Can the W1/W2 multiwinding structure use a state change that simultaneously produces
useful Neff/Zref adaptation and an intentional commutation inductance change,
while the state actuator is kept out of the raw 12-V full-current series path?
```

That is narrower and more defensible than the old `M4 + M6` wording.

---

## 6.4 RQ-D is a multifunctional-magnetics question, not “get ZVS somehow”

Relevant donors:

```text
A3, A7, B2, B5, B6, C7, E2, E3
```

ZVS/ZCS itself is mature. The open issue for this project is whether the **same physical magnetic structure** can provide bulk transfer and useful transient commutation energy without creating more total RMS/core/capacitor loss than it saves.

The decisive inequality later is not only:

```text
Ecomm >= Erequired
```

but also:

```text
Psw_saved > Pcu_added + Pcore_added + Pcap_ESR_added + Pcirc_added
```

If this fails, the multifunctional magnetic state is physically possible but not beneficial.

---

## 6.5 RQ-E remains architecture-level until alpha is proven small

Relevant donors:

```text
A9, D1, D3, D5
```

None of these alone proves a useful 12-V / 2-kW partial-power W1/W2 solution.

Any future proposal must define:

```text
alpha = |Preg| / Pout
```

and show that the correction path does not secretly process nearly the full 2 kW over the operating range.

Until then RQ-E should remain secondary, not the first circuit-generation target.

---

# 7. Preliminary synthesis constraints derived from the traceability map

These constraints are now mandatory for the next W1/W2 combination stage.

### SC-1 — No raw-side selector without a loss reason

A reconfiguration switch placed in the 12-V full-current series path is rejected from the first-pass synthesis unless its removed hardware/loss can plausibly exceed its conduction loss.

### SC-2 — Leakage has to be assigned a job

Every candidate must state whether each important leakage/modal inductance is:

```text
TRANSFER
COMMUTATION
RESONANCE
BALANCING
UNWANTED
```

No candidate may simply say “leakage is used” without identifying the mode and energy path.

### SC-3 — Integration and decoupling are both legal

A separate inductor is not automatically a design failure. If decoupling lowers circulating loss enough, an external element can be the correct answer.

### SC-4 — Current sharing must be resource-normalized

`I/N` arithmetic alone is not accepted as a benefit. Termination, winding length, copper section and semiconductor resource must be normalized.

### SC-5 — Reconfiguration must change something worth changing

A legal state change should modify at least one useful physical quantity:

```text
Neff, Zref, Lcomm/Lr, Ppath, winding role, gain state
```

and its transition must have a legal current/flux path.

### SC-6 — Soft switching is not a sufficient contribution

ZVS/ZCS is treated as a means. The candidate must also improve or clarify another project-relevant trade-off.

### SC-7 — First candidate generation should focus on RQ-A/B/C/D, not RQ-E

RQ-E is retained, but partial-power architecture should not distract the first low-voltage multiwinding synthesis pass unless a naturally low `alpha` path emerges.

---

# 8. Next execution after this matrix

Do **not** generate every pair of Deltas.

Create four constrained synthesis lanes, one per primary residual question:

```text
Lane-A: RQ-A — equal-resource low-side current / termination improvement
Lane-B: RQ-B — integrated-vs-decoupled leakage boundary
Lane-C: RQ-C — coupled Neff / Zref / Lcomm state
Lane-D: RQ-D — bulk-transfer + commutation magnetic modes
```

For each lane, select only Delta donors that address that RQ, then generate a small number of concrete W1/W2 power graphs.

Every graph must explicitly state:

```text
1. baseline named topology
2. imported Delta(s)
3. exact new connection / magnetic change
4. what existing component is removed or repurposed
5. q-state graph
6. raw 12-V current path
7. flux/reset path
8. intended benefit
9. predicted new penalty
10. mathematical quantity that can falsify the idea
```

Only then proceed to the mathematical gate.

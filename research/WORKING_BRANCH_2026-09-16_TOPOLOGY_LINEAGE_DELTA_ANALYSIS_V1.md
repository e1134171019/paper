# 2026-09-16 — Topology Lineage Improvement-Delta Analysis v1

Status: `WORKING_BRANCH / LINEAGE_DELTA_EXTRACTION / PRE_COMBINATION / NO_PRUNING`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

This file changes the synthesis granularity.

The previously extracted `M1...M10` mechanisms remain useful as a **physics/mechanism dictionary**, but they are too coarse to serve as the main combination blocks. Directly combining `Mi + Mj` creates a very large and weakly traceable search space.

The new main synthesis unit is the **improvement delta** between a named base topology and a documented improved descendant:

```text
named base topology
-> documented improved topology
-> identify the original limitation
-> identify exactly what changed in the power graph / magnetic graph
-> identify the new legal state or new energy path
-> identify the obtained function
-> identify the added cost / new failure mode
-> extract transplantable delta
```

Notation:

```text
Delta-Xn = one concrete, literature-traceable improvement step
```

The intended future synthesis becomes:

```text
Delta-A + Delta-B -> W1/W2 candidate
```

rather than:

```text
M_i + M_j -> very broad candidate
```

`M1...M10` remain as tags used to classify each delta after it has been extracted from a real lineage.

---

## 2. Evidence rule

For this v1, each retained delta must be supported by one of the following:

1. a primary IEEE/IET/Nature/publisher paper;
2. an institutional publication record giving title/DOI/abstract;
3. a recent review that explicitly compares the base and improved topology.

Historical genealogy and structural derivability must remain separate. For example, a later Y-source framework may mathematically derive structures that historically predate it; this does not make them historical descendants.

No delta in this file is a novelty claim.

---

# 3. Lineage A — Push-Pull / Current-Fed Push-Pull / Weinberg neighborhood

This lineage is directly relevant to the 12-V high-current input boundary.

## A0 — Base Push-Pull

Baseline power idea:

```text
low-voltage DC
-> alternating primary excitation
-> HF transformer
-> secondary rectification
```

Baseline limitations relevant to this research:

- pulsating / locally concentrated low-side current;
- switch and transformer leakage stress;
- hard-commutation risk depending on implementation;
- fixed power-path role of the two primary halves.

The following deltas show how literature progressively changed the **power hardware**, not only the control law.

---

## Delta-A1 — Push-Pull -> Current-Fed Push-Pull

### Physical modification

Add a current-fed input condition, typically through an input/boost inductive path, so the bridge is driven from a current-source-like entry rather than directly from a stiff low-voltage source.

### Power-graph difference

```text
Voltage-fed:
Vin -> switch/primary directly

Current-fed:
Vin -> Lin -> current-fed switching node -> transformer primary
```

### Function gained

- source-current continuity / controllable current slope;
- better suitability for low-voltage, high-current sources;
- input energy is temporarily stored in `Lin`, so switch state and transformer state are coupled through an explicit energy reservoir.

### New cost / problem

- the current-source path must never be opened illegally;
- boost-inductor copper/core loss appears;
- clamp/freewheel behavior becomes mandatory.

### M-tags

`M1 Current-fed power entry`, partly `M2 stored-energy transfer`.

### W1/W2 transplant concept

Do not copy an entire CFPP converter. Import the rule:

```text
W1/W2 state transitions must preserve a legal low-side current path,
and current slope can be shaped before the first major voltage rise.
```

---

## Delta-A2 — Single-phase CFPP -> Three-Phase Current-Fed Push-Pull

Representative paper:

- R. L. Andersen, I. Barbi, “A Three-Phase Current-Fed Push-Pull DC-DC Converter,” IEEE TPEL, 2009, DOI `10.1109/TPEL.2008.2007727`.

### Original problem addressed

Single-phase current-fed structures still concentrate ripple/current processing into fewer switching/magnetic paths.

### Physical modification

Replace the single push-pull power-transfer set with a three-phase HF transformer / three active switching branches.

### New state-space

Instead of one transfer pair, branch states can be phase-displaced. The 2009 topology uses a three-phase transformer and achieves lower input-current ripple and lower output-voltage ripple than equivalent single-phase arrangements.

### Function gained

- phase-displaced power transfer;
- lower input ripple;
- lower output ripple;
- current/power processing distributed across multiple branches.

### Added cost / problem

- more magnetic/electrical coupling relationships;
- branch matching matters;
- more switching states and greater magnetic design complexity.

### M-tags

`M7 Polyphase role/phase coordination`, `M1 Current-fed`.

### W1/W2 transplant concept

The useful delta is **not** “make the final output three-phase.” It is:

```text
multiple internal power branches can be time-displaced before final single-phase AC synthesis.
```

This keeps `0/120/240°` as an internal power-processing degree of freedom.

---

## Delta-A3 — Three-Phase CFPP -> Active-Clamped Three-Phase CFPP

Representative paper:

- S. Lee, J. Park, S. Choi, “A Three-Phase Current-Fed Push-Pull DC-DC Converter With Active Clamp for Fuel Cell Applications,” IEEE TPEL, 2011, DOI `10.1109/TPEL.2010.2096477`.

### Original problem addressed

Transformer leakage inductance creates transient switch voltage stress and wastes commutation energy.

### Physical modification

Add an active-clamp energy path.

### Critical power-state change

Leakage energy is no longer treated only as a parasitic spike source. It participates in a clamp/recovery transition and is used to enable natural ZVS turn-on of the main switches.

Conceptually:

```text
old:
L_lk energy -> voltage spike / dissipation

improved:
L_lk energy -> clamp path -> Coss/transition support -> recovered/redirected energy
```

### Function gained

- leakage-spike clamping;
- leakage energy reutilization for soft switching;
- main-switch ZVS;
- clamp-switch soft switching;
- reduced rectifier reverse-recovery stress.

### Added cost / problem

- added clamp switches/capacitor/current path;
- new circulating/reactive current;
- timing and component-stress interactions.

### M-tags

`M6 Controllable leakage/integrated commutation`, `M1`, partially `M5` if later integrated magnetically.

### W1/W2 transplant concept

This is a strong transplantable delta:

```text
Delta-A3 = promote leakage energy from unwanted parasitic energy
           into an intentional commutation-energy path.
```

It is much more concrete than simply combining `M1 + M6`.

---

## Delta-A4 — Active-Clamp CFPP -> efficiency-aware magnetic operating-point optimization

Representative recent paper:

- “Impact of Duty Ratio and Saturation Cycling on Efficiency in Current-Fed Push-Pull DC/DC Converter With Active-Clamp,” IEEE TPEL, vol. 41, no. 3, 2026; DOI `10.1109/TPEL.2025.3611905`.

### What changed relative to earlier active-clamp work

The converter graph is not fundamentally new. The important evolution is that the input inductor’s magnetic operating region and duty ratio are treated as a system efficiency tradeoff.

The reported result explicitly shows that minimizing input-current ripple and maximizing efficiency cannot both be achieved simultaneously under the studied design because saturation cycling and loss move with duty ratio.

### Research lesson

This delta is not a new combination block by itself. It is a **falsification rule** for future W1/W2 designs:

```text
continuous / low-ripple input current != automatically lower total loss.
```

Therefore every imported current-fed delta must retain inductor RMS, core loss and saturation-margin accounting.

---

## A5 — Weinberg as a related current-fed branch, not assumed to be a direct descendant

NASA’s 2021 high-power converter-topology study describes a Weinberg converter as a push-pull converter fed by an input inductor, followed by an isolating transformer and rectification. A 2025 paper also reports a “Primary-Side Regulation Active-Clamp Weinberg Converter for Constant Current Control” (DOI `10.1109/PRECEDE63178.2025.11131048`).

For synthesis purposes, Weinberg is retained as a **related donor branch** with current-fed and multi-interval transfer behavior. Its exact historical lineage must not be collapsed into a simple `Push-Pull -> Weinberg` arrow without source-level proof.

### Delta-A5 candidate donor concept

```text
use different switch intervals for different transfer/storage roles,
rather than assuming all useful power transfer occurs in one interval.
```

Tag: `M2 Direct + stored-energy transfer`.

---

# 4. Lineage B — Y-Source family

This is a useful lineage because each descendant modifies a visible weakness of the previous magnetic/impedance network.

## B0 — Original Y-Source Impedance Network

Representative paper:

- Y. P. Siwakoti, P. C. Loh, F. Blaabjerg, G. E. Town, “Y-Source Impedance Network,” IEEE TPEL 2014, DOI `10.1109/TPEL.2013.2296517`.

### Original structural idea

A tightly coupled three-winding magnetic network makes the winding factor part of the converter voltage-gain law. The paper emphasizes high gain with a small duty ratio and increased design freedom.

This is qualitatively different from a normal transformer used only for isolation and fixed turns ratio.

### M-tag

`M3 Winding-factor / impedance-state gain`.

---

## Delta-B1 — Y-Source -> Quasi-Y-Source

Representative paper:

- Y. P. Siwakoti, F. Blaabjerg, P. C. Loh, “Quasi-Y-Source Boost DC-DC Converter,” IEEE TPEL 2015, DOI `10.1109/TPEL.2015.2440781`.

### Original Y-source weakness addressed

The original Y-source input behavior is less suitable when a continuous source current is desired; DC bias/core-saturation issues also matter.

### Physical modification

The quasi-Y topology rearranges the impedance network and includes DC-current-blocking capacitive behavior.

### Function gained

- continuous input current;
- DC current blocking that helps prevent coupled-inductor core saturation;
- retains high-gain Y-source behavior.

### Added cost / problem

- additional energy-storage elements and start/transient interactions;
- more state variables and parasitic-sensitive behavior.

### M-tags

`M3` plus `M1`-like continuous-current objective, but note that this is not the same circuit as a classical current-fed bridge.

### W1/W2 transplant concept

```text
Delta-B1 = alter the surrounding connection of a multiwinding magnetic network
           so the input-current property changes without discarding the gain mechanism.
```

This is more specific than saying “combine current-fed + Y-source.”

---

## Delta-B2 — Y / improved-Y -> Active-Clamped Y-Source

Representative paper:

- R. Reddivari, D. Jena, “Novel active clamped Y-source network for improved voltage boosting,” IET Power Electronics, 2019, DOI `10.1049/iet-pel.2018.6212`.

### Problem addressed

Loose/imperfect magnetic coupling causes leakage-inductance energy, high-voltage spikes and poorer voltage regulation.

### Physical modification

Add an active clamping/absorbing path to the Y-source network.

### New energy path

```text
leakage energy
-> clamp/absorbing branch
-> stored temporarily
-> reused to increase useful voltage gain / suppress spike
```

### Function gained

- voltage-spike suppression;
- leakage-energy reutilization;
- better behavior with nonideal coupling.

### Added cost / problem

- extra semiconductor/passive components;
- more switching states/control burden.

### M-tags

`M3 + M6` after extraction, but the actual reusable block is `Delta-B2`, not the abstract pair.

### W1/W2 transplant concept

If W1/W2 are deliberately imperfectly coupled to create useful `L_lk`, a clamp/recovery path can make that leakage functional rather than purely lossy.

---

## Delta-B3 — Quasi-Y -> Active-Clamped Quasi-Y descendants

The 2024 Y-source review documents active-clamped quasi-Y-source branches which add a switch, diodes and a capacitor to absorb leakage energy and clamp the bus voltage. It also notes the tradeoff: increased switch count and control complexity.

A 2026 paper titled “Active Clamped Quasi-Y-Source Inverter and Its PWM Control Method,” DOI `10.23919/CJEE.2026.000028`, continues this line by embedding a clamp network into qY behavior to suppress DC-bus spikes while preserving boosting action.

### Delta-B3 synthesis lesson

The evolution is cumulative:

```text
Y-source gain freedom
+ quasi rearrangement for input-current/core behavior
+ active clamp for leakage/spike recovery
```

This is exactly why lineage deltas are a better synthesis unit than isolated mechanisms.

---

# 5. Lineage C — LLC -> adjustable-turn / reconfigurable LLC

## C0 — Conventional LLC

Baseline useful properties:

- HF isolation;
- resonant energy transfer;
- soft-switching region;
- transformer `Lm` and resonant network jointly shape gain.

Baseline wide-range problem:

A fixed turns ratio often forces a large switching-frequency excursion when the required input/output voltage range is wide. That can increase RMS/current stress and move the converter away from its best soft-switching/efficiency region.

---

## Delta-C1 — Fixed-ratio LLC -> Adjustable Turns Ratio Transformer LLC

A documented line includes:

- D. Shu, H. Wang, “An Adjustable Turns Ratio Transformer Based LLC Converter for Deeply-depleted PEV Charging Applications,” APEC 2020.
- D. Shu, H. Wang, “An Ultrawide Output Range LLC Resonant Converter Based on Adjustable Turns Ratio Transformer and Reconfigurable Bridge,” IEEE TIE 2021.

### Physical modification

The transformer effective turns ratio itself becomes a discrete power-state variable.

### New state variable

```text
q_N -> N_eff(q_N)
```

instead of relying only on:

```text
f_s -> gain
```

### Function gained

- coarse structural gain change;
- smaller required frequency-regulation span;
- potential to keep the resonant tank nearer a favorable operating region.

### Added cost / problem

- winding/reconfiguration switch implementation;
- transition sequencing and voltage/current stress between ratio states.

### M-tag

`M4 Reconfigurable effective turns`.

---

## Delta-C2 — Adjustable-turn LLC -> flux-controlled adjustable ratio without increasing switch/diode count

Representative paper:

- P. Jia, M. Liu, “A Wide Range LLC Resonant Converter Realized by an Adjustable Turns Ratio Transformer,” IEEE TPEL 2025, DOI `10.1109/TPEL.2025.3561804`.

### Physical modification

A full-bridge LLC is represented by two split half-bridge units in parallel. Their relative phase controls the magnetic flux of the transformer’s center limb, thereby changing the effective turns-ratio behavior. The paper reports no increase in the total switch and diode count compared with a regular full-bridge LLC.

### Why this delta is important

This is not merely “add a tap switch.” It demonstrates a stronger idea:

```text
semiconductor phase state
-> magnetic flux distribution
-> effective turns-ratio state
```

### W1/W2 transplant concept

This is a direct donor for the question:

```text
Can W1/W2 connection/phase change magnetic state and effective transformation ratio
without placing a new series switch in the raw 12-V, hundred-ampere path?
```

Tags: `M4 + M5` after extraction.

---

## Delta-C3 — Fixed secondary LLC -> Reconfigurable Secondary-Side LLC

Representative paper:

- S. S. Queiroz, L. F. Costa, “LLC Resonant Converter With Reconfigurable Secondary-Side for Output Voltage Regulation,” IEEE TCAS-II, 2025, DOI `10.1109/TCSII.2025.3625415`.

### Physical modification

A center-tapped transformer and a secondary-side switch reconfigure the rectifier/effective transformer ratio.

### Function gained

- output regulation through secondary structural reconfiguration;
- fixed-frequency operation;
- primary stage remains unchanged;
- fewer additional active devices in the main current path than many full topology-morphing alternatives.

### W1/W2 transplant concept

This delta supports a practical design rule for the present 12-V problem:

```text
put structural reconfiguration on the higher-voltage / lower-current side whenever possible,
so the raw high-current input path does not carry extra reconfiguration switches.
```

This rule is more concrete than `M4` alone.

---

## Delta-C4 — Reconfigurable LLC with adjustable turns ratio for fixed-frequency DCX-like operation

Representative paper:

- L. Li, S. S. Queiroz, L. F. Costa, “A Reconfigurable LLC Resonant Converter Based on an Adjustable Turns Ratio Transformer,” IECON 2025, DOI `10.1109/IECON58223.2025.11221156`.

The reported concept dynamically changes effective transformer ratio with a secondary-side switch and operates at a fixed frequency near resonance rather than using wide frequency modulation.

### Delta-C4 concept

```text
coarse structural gain by N_eff state
+
resonant stage kept near efficient DC-transformer operation
```

This aligns strongly with a possible W1/W2 architecture in which one magnetic structure supplies bulk transfer while structural states handle coarse voltage adaptation.

---

# 6. Lineage D — DAB -> MAB -> topology/hardware decoupling -> reduced-switch MAB

## D0 — DAB baseline

Classic DAB literature/patent work around 1989–1992 established two actively switched bridges coupled through an HF transformer, enabling bidirectional power flow and soft-switching operation.

Conceptual power law:

```text
Bridge A phase state
<-> link inductance / transformer
<-> Bridge B phase state
```

The transformer's leakage/link inductance is already part of the power-transfer law, not only a parasitic.

---

## Delta-D1 — DAB -> TAB / MAB

The MAB literature treats the converter as a natural extension of DAB: each additional active bridge is coupled to an additional winding of a multiwinding HFT.

### Physical modification

```text
DAB: 2 active power ports / 2 windings
MAB: N active power ports / N-winding HFT
```

### Function gained

- multiport power routing;
- fewer cascaded conversion stages for systems with multiple sources/loads;
- one shared magnetic component can act as a power router.

### New problem created

The 2023 MAB review emphasizes that port power flows become coupled. Shared leakage/linking inductance and multiwinding magnetic coupling can cause circulating power, harder control design and unfavorable transient interactions.

### M-tag

`M5 Common/differential/coupled magnetic modes`, plus multiport routing beyond the original M1-M10 shorthand.

### W1/W2 transplant concept

The useful concept is not “add more ports.” It is:

```text
W1 and W2 may be peer load-bearing power ports, not main + feedback windings.
```

---

## Delta-D2 — MAB -> hardware-level power-flow decoupling

Documented approaches in the MAB review include:

- changing port equivalent inductance with added series inductors;
- selectively inserting/bypassing inductance;
- replacing one multiwinding transformer by multiple two-winding transformers.

### Original problem addressed

Power-flow cross-coupling and circulating current caused by shared magnetic/linking relationships.

### Physical modification

The magnetic/electrical coupling graph itself is modified, not just the controller.

### Function gained

- weaker port coupling;
- easier independent power-flow regulation;
- reduced risk of some multiwinding magnetic interaction problems.

### Added cost

- more magnetics or inductors;
- reduced integration density;
- more copper/core/termination hardware.

### W1/W2 research lesson

This is a direct warning:

```text
more shared magnetic integration is not automatically better.
```

If W1/W2 share too many states through one core, the residual research problem may become decoupling rather than power transfer.

---

## Delta-D3 — MAB -> Reduced-Switch MAB / RS-SQAB for modular SST

Representative paper:

- S. Khani, S. H. Hosseini, M. Sabahi, “Reduced switch multiple active bridge DC-DC converter for modular solid-state transformers,” Scientific Reports 2025, DOI `10.1038/s41598-025-23427-8`.

### Physical modification

Adjacent bridge functions share/integrate semiconductor switches instead of allocating a fully independent bridge to every winding port.

### Function gained

- lower switch count;
- lower transformer/module count in the intended SST architecture;
- preserves multiwinding/MAB-type power routing while reducing duplicated hardware.

### New stress concentration

The paper shows common switches can carry higher current than non-common switches; therefore switch sharing moves current stress rather than making it disappear.

### W1/W2 transplant concept

Very important design principle:

```text
if two W1/W2 functions require similar semiconductor states,
look for a shared switch/state implementation before adding a complete extra power cell.
```

But the shared element must be audited for doubled or concentrated RMS/peak current.

---

# 7. Lineage E — Matrix Transformer / Integrated Magnetics

This lineage may be more directly relevant to the user's multiwinding objective than broad converter-family labels because the **magnetic geometry itself** is the changed object.

## E0 — Conventional transformer in LLC

A conventional HF transformer provides isolation and voltage ratio, while leakage inductance and termination parasitics are often treated as unwanted or separately compensated parameters.

---

## Delta-E1 — Conventional LLC transformer -> Matrix Transformer LLC

Representative paper:

- D. Huang, S. Ji, F. C. Lee, “LLC Resonant Converter With Matrix Transformer,” IEEE TPEL 2014, DOI `10.1109/TPEL.2013.2292676`.

### Physical modification

Use a matrix of elemental transformer structures and co-design secondary conductors, rectifiers and output capacitors around the magnetic structure.

### Problems addressed

- winding AC resistance;
- leakage;
- termination-related loss;
- core utilization / power density.

### Function gained

- distributed current handling;
- flux cancellation opportunities;
- lower termination and via-related loss through physical integration;
- transformer geometry becomes part of the converter-loss solution.

### Important research lesson

This is not equivalent to simply saying:

```text
I_total / N branches
```

The claimed benefit comes from physical winding/termination/flux layout, not only arithmetic current division.

### M-tags

`M5`, `M8` where primary-parallel / secondary-combination is used, but again the true donor block is `Delta-E1`.

---

## Delta-E2 — Matrix Transformer -> controllable integrated leakage as resonant inductor

Representative paper:

- “Utilization of EMI Shielding in PCB Matrix Transformer for Inductor Integration in High Power Density Resonant Converter,” APEC 2023, DOI `10.1109/APEC43580.2023.10131391`.

### Original problem addressed

A resonant LLC stage usually needs a designed series resonant inductance in addition to the transformer.

### Physical modification

Use PCB transformer EMI-shield layers to intentionally create and control leakage flux.

### New function

The matrix transformer now performs:

```text
HF isolation / turns ratio
+
intentional series resonant inductance
```

### W1/W2 transplant concept

This is a very high-value delta because it exactly demonstrates the desired research style:

```text
one physical magnetic assembly
-> two power functions
```

The correct question for W1/W2 becomes not “can leakage be reduced?” but:

```text
what leakage value and mode should be intentionally retained for useful commutation/resonance?
```

---

## Delta-E3 — Generic multiwinding HFT -> star-shaped multiwinding transformer with controllable magnetic integration

Representative paper:

- Y. Cai et al., “A Radially Symmetrical Star-Shaped Core Multiwinding Transformer With Controllable Magnetic Integration for N-Port MAB Converters,” IEEE TPEL 2025, DOI `10.1109/TPEL.2024.3519698`.

### Physical modification

The core geometry, extension legs, pillars, air gaps, winding turns and winding distribution ratio are deliberately designed so port leakage inductances can be adjusted over a wide range while port consistency is maintained with flux barriers.

### Function gained

- multiport magnetic symmetry;
- controllable leakage-inductance integration;
- series-inductor functionality integrated into the HF transformer;
- magnetic geometry becomes a designed control variable at the hardware-design stage.

### W1/W2 transplant concept

This delta supports a sharper research question than `M5 + M6`:

```text
Can one shared core be shaped so the W1/W2 bulk-transfer coupling remains strong,
while a selected leakage/differential path provides the exact commutation inductance needed?
```

This is now a physically traceable donor concept.

---

# 8. Delta registry v1

The first extracted donor blocks are:

| ID | Literature-traceable improvement block | Parent lineage | Main hardware change | Main obtained function | Main new cost/problem | M-tags |
|---|---|---|---|---|---|---|
| `Delta-A1` | Voltage-fed Push-Pull -> Current-Fed Push-Pull | Push-Pull | add current-fed inductive entry | current continuity/current-slope authority | mandatory freewheel/clamp, inductor loss | M1,M2 |
| `Delta-A2` | CFPP -> Three-Phase CFPP | CFPP | three active branches + 3-phase HFT | phase-displaced transfer / lower ripple | coupling + branch complexity | M7,M1 |
| `Delta-A3` | 3-phase CFPP -> Active-Clamp CFPP | CFPP | active clamp path | reuse leakage for clamp/ZVS | extra switch/cap/reactive current | M6,M1 |
| `Delta-A5` | Weinberg multi-interval transfer concept | Weinberg | related current-fed/multi-interval path | direct + stored-energy roles | stress / custom control | M2 |
| `Delta-B1` | Y -> quasi-Y | Y-source | rearranged impedance network + DC-blocking capacitive state | continuous input + anti-DC-bias behavior | more storage states | M3,M1-tag |
| `Delta-B2` | Y/improved-Y -> active-clamped Y | Y-source | active leakage clamp/recovery path | spike suppression + leakage reuse | extra devices/control | M3,M6 |
| `Delta-B3` | qY -> active-clamped qY | Y-source | combine qY input behavior with clamp | continuous-input branch + leakage clamp | cumulative complexity | M3,M6 |
| `Delta-C1` | LLC -> adjustable-turn LLC | LLC | make `N_eff` discrete state | wide gain without extreme `f_s` range | transition/switch stress | M4 |
| `Delta-C2` | LLC -> flux-controlled adjustable-ratio LLC | LLC | split HB phase controls center-limb flux | magnetic-state ratio control | magnetic-state interaction | M4,M5 |
| `Delta-C3` | LLC -> secondary reconfigurable LLC | LLC | center tap + secondary switch/rectifier state | move structural regulation to lower-current side | secondary switch stress | M4 |
| `Delta-C4` | reconfigurable LLC -> near-fixed-frequency DCX-style operation | LLC | coarse `N_eff` change + fixed resonance | keep tank near efficient region | discrete gain management | M4,M6 |
| `Delta-D1` | DAB -> MAB | DAB/MAB | N active ports on MWT | multiport magnetic power routing | cross-coupling/circulation | M5 |
| `Delta-D2` | MAB -> hardware decoupled MAB | MAB | reshape inductance/transformer coupling graph | reduce power-flow cross coupling | less integration/more magnetics | M5,M6 |
| `Delta-D3` | MAB -> RS-MAB / RS-SQAB | MAB/SST | share/integrate bridge switches | fewer duplicated switches/transformers | shared-switch current concentration | multi-function implementation |
| `Delta-E1` | conventional HFT -> matrix transformer | Matrix Transformer | distributed elemental magnetics + integrated terminations | current distribution/flux/termination improvement | geometry/manufacturing complexity | M5,M8 |
| `Delta-E2` | matrix HFT -> integrated controllable leakage | Matrix Transformer | deliberately create leakage via PCB/shield geometry | transformer + resonant inductor in one assembly | reactive RMS / design tolerance | M6 |
| `Delta-E3` | generic MWT -> controllable star-core MWT | MAB magnetics | core/gap/winding geometry sets port leakage | multiport symmetry + integrated inductance | 3D magnetic complexity | M5,M6 |

This registry is `PRE_COMBINATION`. It is not a ranking.

---

# 9. What happens to M1-M10 now

`M1...M10` are retained, but their role changes:

```text
BEFORE:
M1 + M4 -> generate candidate directly

NOW:
Delta-C3 -> tag as M4
Delta-E2 -> tag as M6
Delta-A3 -> tag as M1/M6
...
then combine concrete deltas whose parent circuits and power paths are known.
```

This solves two problems:

1. each future combination is traceable to a documented circuit change;
2. the added components, energy path and tradeoff are already known before synthesis.

The broad `G01...G28` mechanism combinations remain useful as a coverage map, but they are demoted from the primary synthesis route.

---

# 10. Next synthesis question

The next step is **not yet mathematics** and **not yet PSIM**.

First perform compatibility analysis between deltas.

For any two deltas `Delta-X + Delta-Y`, record:

```text
1. Do they act on the same voltage/current domain?
2. Do they require incompatible switch states?
3. Do they compete for the same leakage/magnetizing energy?
4. Does one delta already contain the other function?
5. Can both be realized by the same W1/W2 magnetic assembly?
6. Which components disappear because of integration?
7. Which new components/stresses appear?
8. What is the new research question after combination?
```

Only after a concrete `Delta-X + Delta-Y` graph is formed should the research return to:

```text
state graph
-> mathematical verification
-> loss ledger
-> PSIM
```

---

# 11. Source anchors used in this v1

- Andersen, Barbi, “A Three-Phase Current-Fed Push-Pull DC-DC Converter,” IEEE TPEL, 2009, DOI `10.1109/TPEL.2008.2007727`.
- Lee, Park, Choi, “A Three-Phase Current-Fed Push-Pull DC-DC Converter With Active Clamp for Fuel Cell Applications,” IEEE TPEL, 2011, DOI `10.1109/TPEL.2010.2096477`.
- “Impact of Duty Ratio and Saturation Cycling on Efficiency in Current-Fed Push-Pull DC/DC Converter With Active-Clamp,” IEEE TPEL, DOI `10.1109/TPEL.2025.3611905`.
- Siwakoti et al., “Y-Source Impedance Network,” IEEE TPEL, 2014, DOI `10.1109/TPEL.2013.2296517`.
- Siwakoti et al., “Quasi-Y-Source Boost DC-DC Converter,” IEEE TPEL, 2015, DOI `10.1109/TPEL.2015.2440781`.
- Reddivari, Jena, “Novel active clamped Y-source network for improved voltage boosting,” IET Power Electronics, DOI `10.1049/iet-pel.2018.6212`.
- “Active Clamped Quasi-Y-Source Inverter and Its PWM Control Method,” CJEE 2026, DOI `10.23919/CJEE.2026.000028`.
- Shu, Wang, adjustable-turn-ratio LLC papers, APEC 2020 / IEEE TIE 2021.
- Jia, Liu, “A Wide Range LLC Resonant Converter Realized by an Adjustable Turns Ratio Transformer,” IEEE TPEL 2025, DOI `10.1109/TPEL.2025.3561804`.
- Queiroz, Costa, “LLC Resonant Converter With Reconfigurable Secondary-Side for Output Voltage Regulation,” IEEE TCAS-II 2025, DOI `10.1109/TCSII.2025.3625415`.
- Li, Queiroz, Costa, “A Reconfigurable LLC Resonant Converter Based on an Adjustable Turns Ratio Transformer,” IECON 2025, DOI `10.1109/IECON58223.2025.11221156`.
- Koohi et al., “A Survey on Multi-Active Bridge DC-DC Converters: Power Flow Decoupling Techniques, Applications, and Challenges,” Energies 2023.
- Khani et al., “Reduced switch multiple active bridge DC-DC converter for modular solid-state transformers,” Scientific Reports 2025, DOI `10.1038/s41598-025-23427-8`.
- Huang, Ji, Lee, “LLC Resonant Converter With Matrix Transformer,” IEEE TPEL 2014, DOI `10.1109/TPEL.2013.2292676`.
- “Utilization of EMI Shielding in PCB Matrix Transformer for Inductor Integration in High Power Density Resonant Converter,” APEC 2023, DOI `10.1109/APEC43580.2023.10131391`.
- Cai et al., “A Radially Symmetrical Star-Shaped Core Multiwinding Transformer With Controllable Magnetic Integration for N-Port MAB Converters,” IEEE TPEL 2025, DOI `10.1109/TPEL.2024.3519698`.

Further lineage expansion is still required before any novelty claim.
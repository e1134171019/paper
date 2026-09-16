# 2026-09-16 — Multi-AI Lineage Delta Expansion v2

Status: `WORKING_BRANCH / LINEAGE_DELTA_EXPANSION / PRE_COMBINATION / NO_PRUNING`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

Continue the lineage-first search using several independent retrieval/search routes and expand the improvement-delta library beyond v1.

The synthesis granularity remains:

```text
base named topology
-> documented descendant / modification
-> original limitation
-> exact circuit / magnetic change
-> new state or energy path
-> gained function
-> new cost / failure mode
-> transplantable Delta block
```

`M1...M10` remain classification tags only. They are not the main combination blocks.

## 2. Multi-search lanes used

Independent routes used in this pass:

1. Exa semantic literature/web search.
2. Tavily real-time web search with IEEE / publisher domain bias.
3. Firecrawl research-paper search.
4. Sider Scholar / Scholar-index route as supplementary discovery; one OpenAlex call returned malformed metadata and one Scholar query had low relevance, so it is not used as sole evidence for any new Delta below.

Adoption rule for this file:

- `CROSS_CONFIRMED`: same paper/mechanism surfaced in at least two independent routes, or a primary/publisher page plus another route.
- `PRIMARY_STRONG`: one strong primary/publisher source with sufficiently explicit topology description.
- `DISCOVERY_ONLY`: promising but not yet promoted to a Delta block.

No entry is a novelty claim.

---

# 3. Lineage A extension — Current-Fed Push-Pull / Resonant Push-Pull / Weinberg

## Delta-A6 — Modified Active-Clamped CFPP: add primary blocking capacitor to attack flux imbalance

Representative source:

- E. M. Miranda-Terán et al., “Modified Active-Clamped Current-Fed DC–DC Push–Pull Converter,” Energies, 2023, DOI `10.3390/en16176300`.

Evidence status: `CROSS_CONFIRMED` (Exa + Firecrawl discovery context).

### Previous problem

Active-clamped current-fed push-pull can suppress leakage spikes and obtain ZVS, but asymmetric gating can still create transformer dc-flux bias / saturation risk.

### Physical modification

Add a blocking capacitor in series with the primary winding while retaining the active-clamp network.

### Delta power/magnetic effect

```text
old:
asymmetric volt-second error -> possible dc bias in HFT

modified:
primary series blocking capacitor -> prevents sustained dc current component
active clamp -> handles leakage spike / soft transition
```

### Function gained

- flux-bias / saturation robustness without relying only on complex control correction;
- ZVS retained through the active-clamp path;
- leakage-spike suppression retained.

### Cost / question

- capacitor RMS current and stored-energy stress;
- extra resonant interaction with leakage/magnetizing inductance;
- not automatically suitable for 12-V / 175-A placement.

### Transplantable block

```text
Delta-A6 = use a passive series dc-blocking state constraint to make an otherwise
            asymmetric multiwinding power path magnetically self-protecting against dc bias.
```

Tags: `M1`, `M6`, flux-balance constraint.

---

## Delta-A7 — Resonant Push-Pull: deliberately reuse transformer parasitics as the resonant tank

Representative source:

- Y. Gu et al., “Analysis and Design of High Frequency Resonant Push–Pull Converter for Space Traveling-Wave Tube Amplifier Applications,” IEEE Access, 2026, DOI `10.1109/ACCESS.2026.3652559`.

Evidence status: `PRIMARY_STRONG` (Exa primary/DOI result).

### Physical modification

Instead of suppressing all HFT parasitics, the design deliberately uses:

```text
transformer parasitic capacitance -> parallel resonant C contribution
leakage inductance                -> series resonant L
magnetizing inductance            -> parallel resonant L
```

with only one extra resonant capacitor reported as necessary in the proposed implementation.

### Function gained

- ZVS + ZCS with very small added resonant hardware;
- parasitics become designed power-processing states.

### Cost / question

- resonant point becomes strongly dependent on transformer geometry and tolerance;
- high gain does not imply suitable high-current behavior at 12 V;
- device/winding RMS must be checked.

### Transplantable block

```text
Delta-A7 = co-design HFT parasitics so Llk, Lm, Cp/Coss are part of the intended resonant state
           instead of separately adding every resonant element.
```

Tags: `M6`.

---

## Delta-A8 — Weinberg: specify leakage inductance from a target switching-loss level

Representative source:

- A. S. Naprienko, D. A. Shtein, “Optimization of switching losses of the Weinberg converter,” IJPEDS, 2023, DOI `10.11591/ijpeds.v14.i3.pp1544-1552`.

Evidence status: `PRIMARY_STRONG` (Exa full source).

### Evolution step

This work does not primarily change the converter graph. It turns leakage inductance into a **design variable selected from an allowed switching-loss target**.

### Function gained

- ZCS turn-on interval can be intentionally sized;
- switching-loss target maps to required leakage inductance.

### Important tradeoff exposed

Increasing the leakage used for soft switching increases output-capacitor current stress / can worsen output-voltage quality.

### Transplantable block

```text
Delta-A8 = do not ask only “how much leakage gives ZVS/ZCS?”;
           solve Llk from a matched switching-loss target and carry the resulting capacitor/RMS penalty.
```

This is mainly a mathematical design rule for later W1/W2 candidates.

---

## Delta-A9 — Weinberg -> Primary-Side-Regulated Active-Clamp Weinberg

Representative source:

- C. Wang et al., “A Primary-Side Regulation Active-Clamp Weinberg Converter for Constant Current Control,” PRECEDE 2025, DOI `10.1109/PRECEDE63178.2025.11131048`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Original problems addressed

- hard switching in conventional Weinberg implementations;
- optocoupler drift / aging / nonlinear transfer in isolated feedback.

### Modification

```text
Weinberg power stage
+ active clamp
+ primary-side estimation/control of output current
```

### Gained function

- soft switching;
- regulation without conventional secondary optocoupler feedback.

### Transplantable concept

For W1/W2, the useful idea is not the control algorithm itself. It is that a power winding’s existing primary-side variables can sometimes provide enough information for regulation, allowing the auxiliary winding/isolated-feedback role to be reconsidered.

Tags: `M2`, `M6`, sensing-role reassignment.

---

# 4. Lineage B extension — Y / quasi-Y / hybrid impedance-source

## Delta-B4 — Y-Source + quasi-Z hybridization: preserve continuous input while adding winding-factor gain

Representative source:

- H. Li, J. Lin, T. Jin, “A High Step-Up Hybrid Y-Source-Quasi-Z Source DC–DC Converter for Renewable Energy Applications,” IEEE TIE, 2024 issue, DOI `10.1109/TIE.2023.3333022`.

Evidence status: `CROSS_CONFIRMED` (Exa + review context).

### Physical idea

Instead of choosing only one impedance network, combine the Y-source coupled-winding gain mechanism with quasi-Z-source current-path behavior.

### Gained function

- high step-up gain with winding-factor freedom;
- continuous / smoother input-current behavior inherited from qZ-style structure;
- reduced need to obtain all gain from one turns ratio or one shoot-through duty.

### Added cost

- more stored-energy states and components;
- harder parasitic and stress analysis.

### Transplantable block

```text
Delta-B4 = preserve the favorable input-current path of one network while importing the
           magnetic gain law of another, instead of replacing the whole front-end.
```

Tags: `M3`, continuous-input behavior.

---

## Delta-B5 — Y-source -> zero-input-current-ripple / extended-ZVS branch

Representative recent branch:

- “A Y-Source DC–DC Converter With Zero Input Current Ripple and Extended ZVS Range,” IEEE JESTPE, 2025 (publisher metadata surfaced by Exa).

Evidence status: `PRIMARY_STRONG` for mechanism; full DOI should be rechecked before formal bibliography entry.

### Physical modification

- blocking capacitors prevent dc current through the three-terminal coupled inductor;
- an additional branch drives input-current ripple toward zero and modifies the current available at main-switch turn-on.

### Function gained

- zero/near-zero input ripple;
- zero magnetic dc bias in the coupled element;
- wider ZVS region.

### Cost / question

- “zero ripple” can increase hidden reactive/circulating current elsewhere;
- added branch and capacitors must be included in matched loss comparison.

### Transplantable block

```text
Delta-B5 = use one additional magnetic/electrical branch to reshape the current at the
           switching transition, not merely to filter the source current.
```

---

## Delta-B6 — Y-source coupled inductor + quasi-resonance: leakage controls current slew and diode recovery

Representative source:

- C. Li, H. Li, X. Sun, “A High Step-Up Quadratic DC–DC Converter-Based Y-Source Coupled Inductor With Quasi-Resonance Operation,” IEEE TIE, 2025, DOI `10.1109/TIE.2025.3608016`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

The Y-source coupled-inductor leakage is not only clamped; it limits `di/dt` and participates in quasi-resonant transitions. A switched-capacitor / clamp path absorbs leakage energy.

### Gained function

- ZCS-related transitions;
- lower diode reverse-recovery stress;
- high gain shared by Y-source winding factor + switched capacitor + quadratic stage.

### Transplantable block

```text
Delta-B6 = let Llk simultaneously set current slew and transition energy, while a separate
           clamp/stack node receives the leakage energy instead of dissipating it.
```

Tags: `M3`, `M6`, `M8`.

---

# 5. Lineage C extension — Reconfigurable LLC / DAB / secondary rectifier

## Delta-C4 — Reconfigurable secondary LLC: one winding state changes BOTH effective turns ratio and resonant leakage

Representative source:

- S. S. Queiroz, L. F. Costa, “LLC Resonant Converter With Reconfigurable Secondary-Side for Output Voltage Regulation,” IEEE TCAS-II, 2025, DOI `10.1109/TCSII.2025.3625415`.

Evidence status: `CROSS_CONFIRMED` (Exa + Tavily/IEEE result family).

### Physical modification

A center-tapped MFT receives auxiliary secondary winding sections and a secondary-side unidirectional switch. LV mode uses part of the winding; HV mode inserts the auxiliary sections.

### Key result for our research

The source explicitly shows that the connection state changes not only turns ratio but also total secondary leakage and therefore the primary-referred resonant inductance:

```text
q_LV -> Ntr(LV), Lr(LV)
q_HV -> Ntr(HV), Lr(HV)
```

with the reported design having `Lr(HV) < Lr(LV)`.

### Why this matters

This is a literature-backed realization of the abstract state we previously wrote as:

```text
q -> {Neff(q), Zref(q), Lcomm/Lr(q)}
```

### Added cost

- reconfiguration transition stress;
- one added secondary switch and auxiliary winding sections;
- both resonant modes must still satisfy ZVS/gain constraints.

### Transplantable block

```text
Delta-C4 = exploit the fact that selecting winding sections inherently changes both
           transformation ratio and leakage/resonant parameters.
```

This Delta should be treated as a high-priority donor for later W1/W2 synthesis, without ranking it as a final candidate.

---

## Delta-C5 — DAB/LLC multi-bridge-leg turn-ratio reconfiguration

Representative source:

- H. Xie et al., “An Approach to Reconfiguring Transformer Turn Ratio Using Multibridge-Legs for Wide-Voltage-Gain DAB and LLC Converters,” IEEE TIE, 2025, DOI `10.1109/TIE.2025.3541279`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

Use multibridge-leg connection states to generate multiple effective transformer ratio combinations with a limited set of auxiliary hardware.

### Function gained

- discrete ratio matching across wide voltage range;
- lower inductor RMS current;
- wider ZVS range.

### Transplantable block

```text
Delta-C5 = use existing bridge legs as structural connection actuators for winding ratio,
           so ratio matching reduces reactive/RMS current rather than relying on wide modulation only.
```

Tags: `M4`, `M6` indirectly through ZVS/RMS effect.

---

## Delta-C6 — Adjustable-turn rectifier + voltage-doubling modes

Representative source:

- Q. Wu et al., “Multimode Rectifiers With Ultra-Wide Voltage Gain Based on Adjustable Turns Ratio Transformer and Voltage Doubling Structures,” IEEE TPEL, 2025, DOI `10.1109/TPEL.2025.3627572`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

Combine secondary winding selection with voltage-doubling rectifier states so the rectifier itself has several gain modes.

### Function gained

- multiple discrete gain states;
- switching frequency can stay near resonant frequency over a much wider output range;
- soft-switching region is preserved more easily than one wide frequency sweep.

### Transplantable block

```text
Delta-C6 = place coarse gain-state changes on the lower-current secondary/rectifier side
           and reserve the resonant tank for fine conversion.
```

Tags: `M4`, `M8`.

---

## Delta-C7 — Matrix-Transformer LLC + selective secondary phase-shift: temporarily short selected windings to boost tank energy

Representative source:

- P. R. Prakash, Q. Li, “Selective Secondary Phase-Shift Control for High Gain in LLC Converters with Matrix Transformers,” ECCE 2024, DOI `10.1109/ECCE55643.2024.10861374`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical/state change

One or more synchronous secondary rectifiers are phase shifted relative to the others. This creates intervals in which selected transformer windings are partially shorted, injecting extra energy into the resonant tank and increasing gain while operating near resonance.

### New state

```text
all elemental secondary paths transfer normally
<->
selected elemental secondary path temporarily enters partial-short / energy-boost state
```

### Why this matters

This is a concrete example of **role reassignment among matrix-transformer elemental windings**. A winding/cell is not always just a fixed transfer path.

### Cost / question

- local circulating current / partial-short stress;
- synchronization and current sharing;
- whether such a state scales safely to a 12-V high-current input direction is open.

### Transplantable block

```text
Delta-C7 = use matrix-transformer element-level secondary states to alter resonant energy
           without changing the whole converter topology.
```

Tags: `M5`, `M6`, role reassignment.

---

# 6. Lineage D extension — MAB / QAB / multiwinding SST

## Delta-D1 — Conventional MAB -> Current-Fed MAB with inherent output-voltage balancing

Representative source:

- X. Zhu et al., “Current-Fed Multiactive Bridge Converter With Inherently Output Voltage Balance for Distributed Photovoltaics MVDC Integration,” IEEE TIE, 2024, DOI `10.1109/TIE.2024.3429647`.

Evidence status: `CROSS_CONFIRMED` (Exa + Firecrawl MAB search context).

### Previous problem

In a shared multiwinding transformer, port leakage coupling can strongly couple port power flows, making independent balancing difficult.

### Physical modification

The paper deliberately uses external inductors in place of relying on MWT leakage for key power-transfer inductance, while driving selected grid-side equivalent inductance toward a decoupled condition.

### Function gained

- inherently improved output-voltage balance / port decoupling;
- current-fed input behavior;
- ZVS retained.

### Important counter-lesson

This is a **counterexample to “integrate all leakage into the transformer.”** In some MAB problems, deliberate externalization/decoupling of inductance can be better because MWT leakage cross-couples ports.

### Transplantable block

```text
Delta-D1 = choose which inductive function should be shared magnetically and which should
           be deliberately decoupled; integration is not automatically beneficial.
```

This should become a falsification check against over-integrated W1/W2 concepts.

---

## Delta-D2 — MAB -> radially symmetrical star-shaped MWT with controllable integrated leakage

Representative source:

- Y. Cai et al., “A Radially Symmetrical Star-Shaped Core Multiwinding Transformer With Controllable Magnetic Integration for N-Port MAB Converters,” IEEE TPEL, 2024/2025, DOI `10.1109/TPEL.2024.3519698`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

Use a radially symmetric star-shaped magnetic core, split windings, controlled air gaps / leg geometry and flux barriers.

### Function gained

- intentionally adjustable port leakage inductances;
- integrated series-inductor function;
- improved port symmetry/consistency.

### Transplantable block

```text
Delta-D2 = treat core geometry and flux barriers as part of the electrical power-state design,
           not merely as packaging after the circuit is chosen.
```

Tags: `M5`, `M6`.

---

## Delta-D3 — MAB -> Reduced-Switch MAB / RS-SQAB

Representative source:

- S. Khani, S. H. Hosseini, M. Sabahi, “Reduced switch multiple active bridge DC-DC converter for modular solid-state transformers,” Scientific Reports, 2025, DOI `10.1038/s41598-025-23427-8`.

Evidence status: `CROSS_CONFIRMED` (Exa + Tavily + Firecrawl).

### Physical modification

Neighboring bridge functions share semiconductor legs/switches instead of assigning a completely independent H-bridge to every winding port.

### Function gained

- fewer switches and HFT resources for the same general multiport power-routing role;
- lower total semiconductor-voltage burden / component count in the studied RS-SQAB comparison.

### New cost

- shared devices carry combined/concentrated currents;
- modulation constraints become coupled;
- a device fault can affect multiple paths.

### Transplantable block

```text
Delta-D3 = before adding another full power cell, ask whether two winding roles can share
           a semiconductor leg without losing the required independent states.
```

Tags: hardware sharing / state coupling.

---

## Delta-D4 — QAB -> Open-Winding QAB for fault tolerance

Representative source:

- M. Xin et al., “Open-Winding Transformer-Based Quadruple-Active-Bridge DC–DC Converter With Reliable Fault-Tolerance,” IEEE TIE, 2025, DOI `10.1109/TIE.2025.3577385`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

Use open-winding transformer connections and corresponding bridge/control states.

### Function gained

- new fault-current interruption / reconfiguration paths;
- tolerance to selected dc-side and switch open/short fault conditions without relying only on external DC breakers.

### Relevance to W1/W2

Not a primary gain/current-sharing donor, but it demonstrates that winding endpoint accessibility can itself create useful protective states. Keep it in the Delta library for later if W1/W2 reconfiguration exposes fault-management opportunities.

---

## Delta-D5 — Modular MAB -> MWT + common high-frequency link hybrid (MMAB-MH)

Representative source:

- Y. Zhang et al., “A Modular Multiactive-Bridge Converter Combining Multiwinding Transformers and High-Frequency Link With Fewer Elements and Power Loss,” IEEE TIE, 2026, DOI `10.1109/TIE.2026.3663730`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

Multiple H-bridge power ports connect to a shared HFL through multiple MWTs, reducing the total number of transformers versus a conventional modular MAB arrangement.

### Function gained

- preserves scalable multiport expansion;
- reduces transformer count / core and copper burden in the reported comparison.

### Transplantable block

```text
Delta-D5 = share a high-frequency link across several magnetic substructures instead of
           forcing every port pair to own a complete transformer path.
```

This is relevant if future W1/W2 synthesis starts duplicating too many independent magnetic cells.

---

# 7. Lineage E extension — Matrix / planar integrated magnetics

## Delta-E3 — Matrix transformer winding arrangement fixes designed leakage without extra core legs

Representative source:

- J. Wang, C. Hu, “An integrated matrix transformer suitable for LLC resonant converter,” ZPEC 2025, DOI `10.1109/ZPEC67225.2025.11213287`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

A matrix-transformer winding arrangement is selected specifically to obtain a target leakage inductance without adding separate magnetic core legs.

### Function gained

```text
transformer + resonant inductor function
```

in one magnetic assembly.

### Transplantable block

```text
Delta-E3 = synthesize Llk from winding distribution first, rather than design a transformer
           and later accept whatever leakage remains.
```

Tags: `M6`.

---

## Delta-E4 — Conventional/fractional-turn planar transformer -> reluctance-controlled arbitrary noninteger ratio

Representative source:

- D. Yang et al., “Reluctance-Controlled Planar Transformer With Arbitrary Noninteger Turns Ratio for High-Current LLC DCX,” IEEE TPEL, 2025/2026, DOI `10.1109/TPEL.2025.3649073`.

Evidence status: `PRIMARY_STRONG` (Exa DOI result).

### Physical modification

Split the center magnetic column and place primary windings on separate columns in series. Adjust the reluctance ratio of the magnetic paths so flux division produces an effective noninteger transformation ratio with fewer physical turns.

### Function gained

- effective turns ratio becomes partly a magnetic-reluctance design quantity, not only an integer copper-turn count;
- useful for high-current / PCB-layer-limited transformers.

### Transplantable block

```text
Delta-E4 = use controlled flux division / reluctance ratio to synthesize effective turns ratio
           when physical turn count is too coarse.
```

Tags: `M3`, `M5`.

---

# 8. Architecture-level donors retained separately

These are useful but should NOT be mixed with circuit-level Deltas without marking the layer.

## Arch-F1 — Highly Modular Interphase SST (2025)

A 2025 interphase QAB SST architecture connects QAB primary ports to CHB submodules from different grid phases rather than grouping all ports from one phase. The reported purpose is to keep multiwinding component reduction while improving modularity / redundancy granularity.

Use: architecture-level lesson about **rewiring which system ports share one MWT**.

Not yet a W1/W2 circuit Delta.

## Arch-F2 — Single-stage matrix-type resonant AC/DC branches (2025–2026)

Recent single-stage matrix-type LCL/LLC resonant converters show direct synthesis of multilevel HF excitation and reduced intermediate conversion stages, while still requiring explicit commutation and energy-balance closure.

Use: X1/X3 boundary donor only.

Do not import it into the 12-V DC-input front end without re-deriving the graph.

---

# 9. Cross-search convergence found in this pass

Independent search routes repeatedly converged on several evolution patterns:

1. `parasitic leakage -> designed commutation/resonant energy`;
2. `fixed turns ratio -> state-dependent effective turns ratio`;
3. `state-dependent turns ratio -> state-dependent leakage/resonant inductance as a coupled side effect`;
4. `full independent bridge per port -> shared bridge legs / reduced-switch multiport`;
5. `multiwinding integration -> sometimes intentional decoupling is needed to prevent port cross-coupling`;
6. `matrix transformer as passive current-sharing hardware -> elemental winding states actively participate in gain/resonant control`;
7. `continuous input / low ripple -> must still be audited for hidden core, capacitor and circulating-current penalties`;
8. `fixed winding role -> winding section / port / rectifier state can change role by operating mode`.

This reinforces the decision that the next combination blocks should be literature-traceable `Delta-X` units, not raw `M1...M10` labels.

---

# 10. Delta library status after v2

The v1 library had the first set of lineage deltas. This pass adds/clarifies the following concrete blocks:

```text
Delta-A6  primary dc-blocking + active-clamp CFPP
Delta-A7  push-pull HFT parasitics as resonant tank
Delta-A8  Weinberg leakage chosen from switching-loss target
Delta-A9  PSR active-clamp Weinberg

Delta-B4  hybrid Y-source + quasi-Z current-path behavior
Delta-B5  zero-input-ripple / extended-ZVS Y-source branch
Delta-B6  Y-source leakage used for quasi-resonant current shaping

Delta-C4  secondary winding selection changes Neff AND Lr
Delta-C5  multibridge-leg turn-ratio reconfiguration
Delta-C6  adjustable-turn + voltage-doubling multimode rectifier
Delta-C7  matrix-secondary phase state boosts resonant-tank energy

Delta-D1  current-fed MAB with deliberate power-path decoupling
Delta-D2  star-shaped MWT with controllable integrated leakage
Delta-D3  reduced-switch MAB / shared bridge legs
Delta-D4  open-winding QAB fault-state extension
Delta-D5  MMAB + multiwinding transformer + shared HFL

Delta-E3  matrix winding layout realizes target leakage
Delta-E4  reluctance-controlled arbitrary noninteger ratio
```

These are still a **library**, not candidate circuits.

---

# 11. Strongest conceptual conflicts to preserve before combination

Do not only collect compatible ideas. The literature now exposes important opposing design rules:

### Conflict 1 — integrate leakage vs decouple leakage

```text
Delta-E3 / Delta-D2:
use transformer leakage as desired series/resonant inductance

Delta-D1:
replace / externalize selected leakage inductance to decouple multiport power flow
```

Therefore the research question is not “how do we maximize magnetic integration?” It is:

```text
which inductive modes should be shared and which must remain independent?
```

### Conflict 2 — structural gain vs transition complexity

`Delta-C4/C5/C6` reduce wide modulation range by reconfiguring turns / rectifier states, but create additional transition states and connection stress.

### Conflict 3 — zero ripple vs hidden RMS / storage burden

Y-source and current-fed descendants can reduce source ripple, but the removed ripple can reappear as capacitor RMS, magnetic bias burden or internal circulation.

### Conflict 4 — fewer switches vs shared-device stress

`Delta-D3` reduces bridge count but concentrates current/state responsibility in shared switches.

These conflicts should be kept explicitly in the next compatibility matrix rather than filtered out.

---

# 12. Next execution

The next step should NOT immediately combine every Delta pair.

First build a **Delta comparison sheet** with one row per lineage step and fixed columns:

```text
Base topology
Improved topology
Original problem
Exact components/connections changed
New q-state / energy path
Function gained
Function lost / degraded
New loss/stress introduced
M-tags
Applicable side: raw 12-V / post-first-rise / secondary / magnetic-only
Requires full-power processing? YES/NO/PARTIAL
Can transplant without copying full topology? YES/CONDITIONAL/NO
```

Then use this sheet to define compatibility constraints before any `Delta-X + Delta-Y` synthesis.

No mathematics or PSIM should begin until a selected Delta combination has an explicit legal power graph.

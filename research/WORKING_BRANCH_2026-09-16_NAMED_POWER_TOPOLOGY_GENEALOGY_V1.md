# WORKING BRANCH — Named Power-Topology Genealogy V1

Date: 2026-09-16  
Status: `WORKING_BRANCH / BROAD_LITERATURE_SYNTHESIS / NO_PRUNING`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 0. Purpose

This file expands the existing 1–80 named-topology seed list into a genealogy-oriented research map. The goal is **not** to choose a winner yet. The goal is to identify named historical and modern converter families whose already-established power mechanisms may be adapted into the W1/W2 region of the 12 V / 2 kW research boundary.

The central question is:

> Which named circuit families already demonstrate that one magnetic/power structure can simultaneously perform more than one of the following: current-fed input conditioning, early current splitting, voltage gain, impedance transformation, direct and stored-energy transfer, leakage-energy utilization, resonant commutation, topology reconfiguration, multiport power routing, current balancing, or voltage stacking?

The search specifically avoids reducing the problem to self-oscillation/control. Royer/self-oscillation remains a possible timing/commutation host; this genealogy focuses on the **power graph** and the **magnetic power-processing graph**.

## 1. Multi-search method

Independent search lanes used in this synthesis:

1. Exa semantic web/literature search.
2. Firecrawl research-paper search.
3. Sider Scholar / scholarly-index search.
4. Tavily independent web search.
5. Direct web cross-checks against IEEE/Wiley/MDPI and publisher/repository pages.

A name is treated as a useful genealogy node when at least one of the following holds:

- it is a stable, widely used topology-family name;
- it is explicitly identified in a review as a derived topology;
- it is a repeatedly cited named variant with a distinct power graph;
- it is a recent topology with an experimentally demonstrated mechanism directly relevant to W1/W2.

A paper-specific label is not automatically promoted to a general topology family.

---

# 2. Genealogy A — Royer / Baxandall / Current-Fed Push-Pull / Weinberg

This is the closest historical neighborhood to the present W1/W2 concept.

## A0 — Oscillator / resonant ancestry

- Royer Oscillator
- Baxandall Class-D Oscillator
- Current-Fed Push-Pull Parallel-Resonant Inverter (CFPPRI)
- Self-Adjusting CFPPRI
- Autonomous / Self-Oscillating CFPPRI
- Current-Source Parallel-Resonant Push-Pull Inverter

The useful mechanism is not the name “Royer” itself. The useful progression is from a magnetic-state oscillator toward **current-fed resonant power processing**, where input-current behavior, transformer excitation and commutation become coupled.

## A1 — Current-fed push-pull family

Named/established branches found in the literature include:

- Current-Fed Push-Pull Converter (CFPP)
- Single-Inductor Current-Fed Push-Pull Converter
- Dual-Inductor Current-Fed Push-Pull Converter
- ZVS Clamping-Mode Current-Fed Push-Pull Converter
- Active-Clamped ZVS Current-Fed Push-Pull Converter
- Naturally-Clamped ZCS/ZVS Current-Fed Push-Pull Converter
- Impulse-Commutated ZCS Current-Fed Push-Pull Converter
- Soft-Switching Current-Fed Push-Pull Converter
- CL-Resonant Current-Fed Push-Pull Converter
- LCL-Resonant Push-Pull Converter
- Quasi-Resonant Current-Fed Push-Pull Converter
- High-Step-Up Resonant Push-Pull Converter
- Bidirectional Current-Fed Resonant Push-Pull Converter
- Current-Fed Soft-Switching Push-Pull Front-End Bidirectional Inverter
- Three-Phase Current-Fed Push-Pull Converter
- Three-Phase Current-Fed Push-Pull Converter with Active Clamp
- ZVS-PWM Three-Phase Current-Fed Push-Pull Converter
- Naturally-Clamped Snubberless Soft-Switching Bidirectional Three-Phase Current-Fed Push-Pull Converter
- Naturally-Commutated Current-Fed Three-Phase Bidirectional Soft-Switching Converter with 120° Modulation
- Impulse-Commutated High-Frequency Soft-Switching Modular Current-Fed Three-Phase Converter

Important historical/engineering sequence:

`Push-Pull → Current-Fed Push-Pull → Clamp/Resonant/Impulse-Commutated CFPP → Three-Phase / Bidirectional / Modular CFPP`

This branch is directly relevant because it already attacks low-voltage/high-current sources using a power-side input inductor/current-source behavior rather than treating current shaping as only a control problem.

## A2 — Weinberg family

Named and recent variants include:

- Weinberg Converter / Current-Fed Weinberg Converter
- Improved Weinberg Converter
- Three-Phase Weinberg Converter
- Active-Clamp Weinberg Converter
- Active-Clamping Soft-Switching Weinberg Converter
- ZVS/ZCS Weinberg Converter
- High-Power-Density Weinberg Converter
- Low-Output-Current-Ripple Weinberg Converter
- Bidirectional / improved bidirectional Weinberg regulator variants
- Primary-Side-Regulation Active-Clamp Weinberg Converter

Recent confirmed development line:

- 2005–2006: multi-kW satellite battery-discharge Weinberg implementations.
- 2009: active-clamping soft-switching Weinberg variant.
- 2011: Three-Phase Weinberg Isolated DC-DC Converter.
- 2018: ZVS/ZCS and high-power-density Weinberg variants.
- 2019: high-efficiency/high-power-density Weinberg with reduced conduction loss and output-current ripple.
- 2023: improved Weinberg BDR with lower output-current ripple; 750 W prototype.
- 2023: isolated Weinberg for Hall-thruster anode supply using parasitics for ZVS/ZCS.
- 2025: Primary-Side Regulation Active-Clamp Weinberg Converter.

### W1/W2 transferable mechanisms from Genealogy A

- current-fed input behavior;
- ON/OFF-interval energy transfer rather than only one transfer interval;
- direct-transfer + stored magnetic-energy transfer;
- leakage energy used for soft switching instead of being only a parasitic loss;
- active-clamp energy recycling;
- 120° polyphase power delivery;
- possible role rotation among equivalent power branches;
- continuous input/output-current behavior.

---

# 3. Genealogy B — Magnetically Coupled Impedance-Source (MCIS)

This family is important because the transformer/coupled inductor is **inside the gain law and impedance network**, not merely an isolation block.

## B0 — Base impedance-source line

- Z-Source Inverter / Z-Source Network
- Quasi-Z-Source (qZ)
- Embedded Z-Source
- Embedded Quasi-Z-Source
- Extended-Boost Z-Source
- Switched-Inductor Z-Source
- Switched-Capacitor Z-Source
- Diode/Capacitor-Assisted Z-Source

## B1 — Magnetically coupled two-winding line

- T-Source
- Trans-Z-Source
- Trans-Quasi-Z-Source
- Improved Trans-Z-Source
- Improved Trans-qZ-Source
- Cascaded Multicell Trans-Z-Source
- LCCT-Z-Source
- LCCT-qZ-Source
- Γ-Z-Source
- Asymmetrical Γ-Z-Source
- Σ-Source / Sigma-Z-Source
- A-Source

## B2 — Three-winding generalized line

- Y-Source
- Improved Y-Source Type I
- Improved Y-Source Type II
- Quasi-Y-Source
- Modified Y-Source
- Δ-Source
- Active-Clamped Y-Source
- Voltage-Double Quasi-Y-Source
- Low-Voltage-Overshoot High-Efficiency qY variants
- High-Step-Up Cascaded qY variants
- Optimized qY-Source
- LCD-qY-Source
- Boost-Combined qY-Source
- Boost-Combined Modified Y-Source
- Switched-Inductor Y-Source variants
- Quasi-Z + Y hybrid step-up variants
- Switched-Coupled-Inductor Y variants
- Zero-Input-Current-Ripple Modified Y-Source (ZICR-M-YSC)
- Isolation-Type ZCS qY-Source
- Soft-Switching High-Gain Modified Y-Source

The 2024 Y-source review gives an especially useful conceptual result: a Y-source converter can be separated into a **basic structure** plus **characteristic circuits** (clamp, absorption, boost, filter, resonant cells). That is directly useful to topology synthesis because it shows how one named topology family evolves by assigning additional physical functions to the same power-processing neighborhood.

### W1/W2 transferable mechanisms from Genealogy B

- winding factor becomes an active voltage-gain degree of freedom;
- same magnetic structure participates in gain and impedance shaping;
- continuous-input-current variants;
- DC-blocking winding paths to control core bias/saturation;
- leakage-clamp/absorption networks that return energy instead of dissipating it;
- three-winding state relationships;
- coupled-inductor + switched-capacitor hybrid gain;
- possible route from W1/W2 “transformer windings” to W1/W2 “power-processing impedance-network windings.”

---

# 4. Genealogy C — Topology Morphing / Reconfigurable Power Converters

This family is directly relevant to the desired idea that W1/W2 should change **power function**, not merely timing.

Established/reviewed mechanisms include:

- Full-Bridge ↔ Half-Bridge topology morphing
- Full-Bridge ↔ Forward / Flyback morphing
- Multimode two-/three-level front-end bridge reconfiguration
- Full-Bridge Rectifier ↔ Voltage-Doubler Rectifier reconfiguration
- Multimode active/passive rectifier reconfiguration
- Adjustable Transformer Turns-Ratio Converter
- Fractional-Turn Transformer / Variable-Effective-Turns Ratio approaches
- Parallel/Series Transformer Reconfiguration
- Double-Full-Bridge LLC using reconfigurable three-leg inverter
- Dual-Half-Bridge LLC reconfiguration
- LLC ↔ LLCC Reconfigurable Resonant Tank
- Topology-Morphing Multi-Element Resonant Converter
- Topology-Reconfigurable LLC Resonant Converter
- Structure-Reconfigurable Series Resonant Converter
- Multimode Series-Resonant Isolated Bidirectional Converter
- Isolated Hexa-Mode Converter
- Multi-Track DC-DC Converter Architecture
- Series-Parallel Auto Regulated Converter (SPARC)
- Topology-Morphing Partial-Power Converter with Variable Turns Ratio
- ZCS/ZVS Partial-Power Converter with Reconfigurable H-Bridge and Variable Turns Ratio
- Reconfigurable DAB cells with Full-Bridge / Half-Bridge / Hybrid modes

Recent trajectory:

- 2015: “On-the-Fly Topology-Morphing Control” formalized the term in LLC research.
- 2018–2022: topology morphing expanded to rectifiers, multi-element resonant tanks and systematic classification.
- 2024–2025: partial-power converters use reconfigurable bridge states + variable turns ratio.
- 2025: reconfigurable LLC with adjustable turns-ratio transformer.
- 2025–2026: SPARC reappears in generalized analysis and closed-loop regulation, dynamically combining series/parallel transformer configurations with a continuous control variable.

### W1/W2 transferable mechanisms from Genealogy C

The strongest target mechanism is:

`q → {N_eff(q), Z_ref(q), power-path(q), possibly L_comm(q)}`

This is more valuable than a control-only state because the same commanded state physically changes which turns/sections/paths process load power.

---

# 5. Genealogy D — Resonant Isolated Converter Evolution

Base names:

- Series Resonant Converter (SRC)
- Parallel Resonant Converter (PRC)
- Series-Parallel Resonant Converter (SPRC)
- LCC Resonant Converter
- LLC Resonant Converter
- CLLC Resonant Converter
- CLL / LCL / LCLC / C³L³ higher-order resonant families
- Dual-Bridge Series-Resonant Converter
- Series-Resonant DAB

Derived modern branches include:

- Interleaved LLC
- Three-Phase LLC
- Three-Phase CLLC
- Wye-Delta Three-Phase LLC
- Multiphase LLC with Integrated Magnetics
- Matrix-Transformer LLC
- Dual-Transformer LLC
- Inductor-Less Dual-Transformer LLC
- Reconfigurable LLC
- Adjustable-Turns-Ratio LLC
- Multi-Mode CLLC
- Three-Port LLC
- Multiport LLC
- Three-Port Series-Resonant Converter
- Four-Port Resonant Converter
- TAB-LCL / multiport higher-order resonant converter

Recent direction is no longer simply “use LLC for ZVS.” The tank, transformer, rectifier, bridge state and turns ratio are increasingly treated as co-designed power-state variables.

### W1/W2 transferable mechanisms from Genealogy D

- promote `L_m` / `L_lk` from parasitic parameters to designed energy states;
- locate resonant burden on a higher-voltage/lower-current side when beneficial;
- use different magnetic modes/paths for transfer and commutation;
- fixed-frequency DCX-like bulk-power transfer plus a smaller regulating degree of freedom;
- reconfigure tank or turns ratio rather than forcing a wide frequency sweep.

---

# 6. Genealogy E — DAB / TAB / QAB / MAB / Multiwinding Multiport

## E0 — DAB line

- Dual Active Bridge (DAB)
- Current-Fed DAB
- Hybrid Current-Fed DAB
- Series-Resonant DAB
- Three-Level DAB
- T-Type Multilevel DAB
- Five-Level DAB
- Flying-Capacitor DAB
- Three-Phase DAB
- Reconfigurable DAB

## E1 — Multi-active bridge line

- Triple Active Bridge (TAB)
- Quadruple Active Bridge (QAB)
- Penta Active Bridge (PAB)
- Multiple / Multi-Active Bridge (MAB)
- Modular Multi-Active Bridge (MMAB)
- Resonant MAB
- Reduced-Switch MAB
- Open-Winding QAB (OW-QAB)
- Current-Fed QAB (CF-QAB)
- MMAB with Multiwinding Transformers and shared High-Frequency Link (MMAB-MH)

## E2 — Multiwinding transformer line

- Multiwinding-Transformer-Based DC-DC Converter (MTB DC-DC)
- Three-Port LLC
- Multiport LLC
- Three-Port Series-Resonant Converter
- Series-Resonant Three-Port Converter with magnetic integration
- Multiport resonant converter with actively controlled inductors
- Self-Tuning Multiport Resonant Converter

Recent evolution:

- 2021 assessment: MWT main flux + self/mutual leakage flux are explicitly treated as design variables; cross-coupling becomes the dominant challenge.
- 2023–2025: research moves toward topology-level power-flow decoupling, resonant MAB, open-winding fault-tolerant structures, current-fed QAB, and multiwinding resonant ports.
- 2026: MMAB-MH reduces transformer count by combining MWTs and a common high-frequency link; generalized MAB modeling now includes resonant/non-resonant behavior and transformer parasitics.

### W1/W2 transferable mechanisms from Genealogy E

- winding role is a true power-port role, not only feedback sensing;
- leakage inductance can intentionally mediate power flow;
- multiple winding currents can create common and differential magnetic modes;
- a port can change role between transfer/regulation/energy exchange if the state graph permits it;
- W1/W2 can be studied as a minimal two-port projection of a broader MWT/MAB state space.

---

# 7. Genealogy F — Matrix Transformer / Integrated Magnetics

This is not just “a transformer shape.” It is a family of power-stage + magnetic-geometry co-design methods.

Named/repeated structures found:

- Matrix Transformer
- Matrix-Transformer LLC
- Integrated Planar Matrix Transformer LLC
- Matrix Transformer + Matrix Inductor LLC
- Scalable Matrix Integrated Transformer with Controllable Leakage Inductance
- Four-Element Matrix Transformer
- Cross-Coupled Integrated Matrix Transformer
- Pentacentra Transformer for Multiphase LLC
- Vertically Integrated Four-Leg Matrix Transformer
- Fractional-Turn Matrix Transformer
- Radially Symmetrical Star-Shaped Core Multiwinding Transformer for N-Port MAB
- Symmetrical Multi-Winding Split Planar Transformer
- 3D-Matrix Inductor-Transformer for CLLC
- Double-B Integrated Magnetic Transformer for IPOP LLC
- Matrix-Transformer-Based Single-Stage Resonant DC-AC Converter
- LLC DCX with Matrix Transformer

Recent trajectory:

- 2014–2019: matrix transformer used primarily for high-current distribution, winding resistance and termination reduction.
- 2021–2023: matrix transformer and matrix inductor are co-optimized; resonant inductance begins to be embedded deliberately.
- 2024–2025: four-leg, split-planar, cross-coupled, pentacentra and star-core MWT structures explicitly target current sharing, controllable leakage and multiport symmetry.
- 2026: controllable leakage, fractional turns, integrated air-gap geometry and 11 kW-class CLLC matrix magnetics are active research topics.

A particularly relevant 2025 result is a **Matrix-Transformer-Based Single-Stage Resonant DC-AC Converter** demonstrated at 40–60 Vdc → 220 Vrms / 50 Hz, 600 W. The matrix transformer plus multiple switching units distributes low-voltage-side current and provides segmented voltage-gain states. This does not prove suitability at 12 V / 2 kW, but it directly connects the matrix-transformer branch to the same DC→single-phase AC functional boundary.

### W1/W2 transferable mechanisms from Genealogy F

- distributed low-voltage current paths;
- primary parallel / secondary series behavior;
- current sharing through magnetic/winding geometry rather than only semiconductor paralleling;
- intentionally controlled leakage inductance;
- fractional turns;
- flux cancellation;
- transformer + resonant inductor integration;
- segmented gain states in the same magnetic assembly.

---

# 8. Genealogy G — Voltage Multiplier / Switched-Capacitor / Coupled-Inductor High-Step-Up

Historical and modern named cells remain relevant because they show how voltage gain can be divided between magnetic and electric-field mechanisms.

Seed names retained:

- Villard
- Greinacher
- Cockcroft-Walton
- Symmetrical Cockcroft-Walton
- Dickson Charge Pump
- Favrat Charge Pump
- Mandal-Sarpeshkar Multiplier
- Wu / Umeda / Nakamoto / Bergeret multipliers
- Pelliconi / Ker / Starzyk charge pumps
- Switched-Capacitor Voltage Multiplier (SC-VM)
- Voltage Multiplier Cell (VMC)
- Bi-fold Dickson
- Interleaved Boost + VMC
- Voltage-Lift Cell
- Coupled-Inductor VMC
- Active-Network VMC
- Hybrid Cockcroft-Walton/Dickson
- Switched-Capacitor Multilevel Inverter
- ANPC-based SC Multilevel Inverter
- Resonant Switched-Capacitor Isolated Converter

Additional recurrent hybrid directions:

- voltage-doubler rectifier current-fed push-pull;
- current-fed half-bridge with quasi-switched-capacitor cell;
- three-winding coupled-inductor + VMC;
- switched-capacitor + coupled-inductor ultra-high-gain converters;
- dual-charge-pump-cell isolated converters;
- trans-inverse three-winding coupled-inductor converters.

### W1/W2 transferable mechanisms from Genealogy G

The desired use is **not** to place a large switched-capacitor current loop directly in the raw 12 V / ~175 A domain. The useful mechanism is to let W1/W2 perform the first magnetic voltage rise/current reduction, then allow secondary winding sections / capacitors to stack voltage in a lower-current domain.

---

# 9. Genealogy H — Direct HF-Link / Single-Stage Isolated DC-AC

Named families/structures include:

- Isolated Matrix Inverter
- High-Frequency-Link Matrix Inverter
- Series-Resonant Matrix Converter
- Current-Fed Push-Pull Front-End Bidirectional Inverter
- Matrix-Transformer-Based Single-Stage Resonant DC-AC Converter
- Direct HF-Link / matrix-routing isolated inverter families

This line is relevant to X1/X3 overlap because it challenges the mandatory chain:

`HFT → rectifier → stiff HVDC → VSI`

However, it does not remove the single-phase 2ω energy constraint. X2 remains a separate physical problem unless an explicit buffer state is demonstrated.

---

# 10. Cross-family evolution pattern found by all search lanes

Across otherwise different topology families, recent evolution repeatedly moves toward the following physical changes:

1. `continuous input current` rather than pulsating low-voltage source current;
2. `smaller transformer turns ratio` with gain shared by other mechanisms;
3. `leakage inductance as a designed state` rather than a parasitic only;
4. `active clamp as energy-processing path`, not only voltage protection;
5. `multiwinding / multiport magnetic structures` that replace separate conversion stages;
6. `reconfigurable turns ratio / bridge / rectifier / resonant tank`;
7. `multiphase / 120° power processing` for current distribution and ripple reduction;
8. `matrix / distributed magnetics` for high-current winding and termination control;
9. `DCX-like bulk power path + smaller regulating path`;
10. `single-stage or reduced-stage conversion` while keeping soft switching.

This convergence is important because it independently supports the research direction:

`W1/W2 should be promoted from fixed transformer windings to load-bearing power-processing states.`

---

# 11. W1/W2 mechanism source map — do not prune yet

The following source mechanisms should now be synthesized against W1/W2 without assuming their original full topology:

### M1 — Current-Fed Power Entry
Source families: CFPP, Weinberg, current-fed DAB.

Potential W1/W2 role: continuous source current, earlier current-domain control, reduced dependence on large raw-bus current pulses.

### M2 — Direct + Stored-Energy Transfer
Source families: Weinberg, flyback-forward hybrids.

Potential W1/W2 role: one state performs direct transformer transfer while another magnetic state carries stored/released energy.

### M3 — Winding-Factor / Impedance-State Gain
Source families: Trans-Z, Y-source, A-source, LCCT, Γ-source.

Potential W1/W2 role: winding relationship participates in the converter gain law, not only fixed isolation ratio.

### M4 — Reconfigurable Load-Bearing Turns
Source families: TMC, adjustable-turns LLC, SPARC, variable-turns partial-power converters.

Potential W1/W2 role: same physical winding assembly changes `N_eff`, `Z_ref`, current path, and possibly commutation inductance.

### M5 — Common / Differential Magnetic Mode
Source families: MWT/MAB, integrated magnetics, multiphase structures.

Potential W1/W2 role: common mode carries bulk power; differential mode handles balance/commutation/energy redistribution.

### M6 — Controllable Leakage / Integrated Resonance
Source families: matrix transformer, CLLC/LLC, MAB, integrated magnetics.

Potential W1/W2 role: `L_lk` / `L_comm` intentionally shaped by winding/core geometry and used for ZVS/resonance.

### M7 — Polyphase Role Rotation
Source families: three-phase CFPP, three-phase DAB, three-phase LLC.

Potential W1/W2 extension: N branches at `0°, 120°, 240°` or generalized `2πk/N`, with transfer/commutation roles staggered in time.

### M8 — Secondary Voltage Stacking
Source families: VMC, voltage doubler, matrix transformer, fractional-turn reconfiguration.

Potential W1/W2 extension: first raise voltage magnetically, then stack/reconfigure in a lower-current domain.

### M9 — Bulk-Power + Small-Regulator Split
Source families: resonant push-pull DCX + active-clamp flyback regulator, partial-power converters.

Potential W1/W2 role: high-efficiency nearly fixed-ratio bulk transfer with only a fraction of total power subjected to fine regulation.

### M10 — Direct DC→AC Magnetic/Matrix State Synthesis
Source families: isolated matrix inverter, matrix-transformer single-stage resonant DC-AC.

Potential W1/W2 extension: segmented or state-dependent magnetic voltage contributions later combined into the 220 Vac waveform.

---

# 12. Immediate synthesis set

The next synthesis pass should not ask “which whole topology wins?” It should cross the above mechanisms with the W1/W2 physical operators.

Required first combinations:

1. `M1 current-fed + M4 reconfigurable turns`
2. `M1 current-fed + M6 controllable leakage`
3. `M2 direct/stored transfer + M5 common/differential magnetic mode`
4. `M3 impedance-state gain + M6 integrated commutation energy`
5. `M4 reconfigurable turns + M5 magnetic modal selection`
6. `M4 reconfigurable turns + M7 0/120/240° scheduling`
7. `M5 modal selection + M7 role rotation`
8. `M6 controllable leakage + M8 secondary stacking`
9. `M1 current-fed + M9 bulk-path/small-regulator split`
10. `M5/M7 matrix-magnetic state + M10 direct DC→AC segmented synthesis`

For each combination, record:

- exact load-bearing W1/W2 connection in each state;
- current path from 12 V source;
- `N_eff(q)`;
- reflected impedance `Z_ref(q)`;
- active magnetic mode(s);
- `L_comm(q)` / leakage participation;
- source RMS current;
- whether power is direct-transfer or stored-energy transfer;
- whether the function is genuinely hardware-shared or only co-located;
- additional full-power switches/components introduced.

No novelty statement is permitted at this stage.

---

# 13. Key literature anchors

- Rathore, A. K., overview of current-fed DC/DC converters for high-voltage gain and low-voltage high-current applications, PEDES 2016.
- Pan et al., overview/comparative evaluation of current-fed isolated bidirectional DC/DC converters, IEEE TPEL 2019.
- Lee, Park, Choi, Three-Phase Current-Fed Push-Pull DC-DC Converter with Active Clamp, IEEE TPEL 2011.
- Miranda-Terán et al., Modified Active-Clamped Current-Fed DC-DC Push-Pull Converter, Energies 2023.
- Kim et al., High Efficiency and High Power Density Weinberg Converter..., APEC 2019.
- Bae, Park, Han, Low-Output-Current-Ripple Weinberg Converter / satellite BDR, IEEE Access 2023.
- Wang et al., Primary-Side Regulation Active-Clamp Weinberg Converter, PRECEDE 2025.
- Siwakoti et al., Y-Source / new magnetically coupled impedance-source networks, 2014–2015.
- Yadav et al., A Topological Advancement Review of Magnetically Coupled Impedance Source Network Configurations, Sustainability 2022.
- Wang et al., A Review of Non-Isolated High-Gain Y-Source Converter Topologies, Energies 2024.
- Sidorov et al., Survey of Topology Morphing Control Techniques for Galvanically Isolated DC-DC Converters, IEEE OJIES 2022.
- Jovanović & Irving, On-the-Fly Topology-Morphing Control for LLC, IEEE TPEL 2015.
- Lequeu et al., SPARC, IEEE TIA 2004; Giles et al., generalized/SPARC regulation work 2025–2026.
- Pereira et al., A Comprehensive Assessment of Multiwinding Transformer-Based DC-DC Converters, IEEE TPEL 2021.
- Koohi et al., Survey on Multi-Active Bridge DC-DC Converters, Energies 2023.
- Takeshita et al., Trends in Isolated Power Converters Using High-Frequency Transformers, IEEJ TEEE 2026.
- Nabih & Li, matrix transformer + matrix inductor LLC work, IEEE TPEL 2023.
- Cai et al., star-shaped multiwinding transformer with controllable magnetic integration for N-port MAB, IEEE TPEL 2024/2025.
- Liang et al., Matrix-Transformer-Based Single-Stage Resonant DC-AC Converter, IEEE JESTPE 2025/2026 publication cycle.

---

# 14. State of conclusion

The 1–80 list should now be treated as a **seed catalog**, not the full topology search space. The literature search shows that once genealogy and recent derived variants are included, the useful named-space clearly exceeds the original 80 entries.

Most important correction:

> The research should not ask only “which named topology can replace Royer?” It should ask which *power mechanism* from each named topology can be transferred into W1/W2 so that the same physical magnetic/power structure performs multiple load-bearing functions.

Current highest-value search intersection, without selecting a winner:

`Current-Fed + Multiwinding + Reconfiguration + Integrated Leakage/Resonance + Polyphase/Matrix Magnetic States`

This remains a synthesis space, not a novelty claim.

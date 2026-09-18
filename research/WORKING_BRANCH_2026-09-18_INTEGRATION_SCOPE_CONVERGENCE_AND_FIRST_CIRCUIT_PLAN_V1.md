# 2026-09-18 — Integration-Scope Convergence and First-Circuit Validation Plan v1

Status: WORKING_BRANCH / CONVERGENCE / PRE-SCHEMATIC / PRE-MATH
Novelty: NOT_ESTABLISHED
PSIM: NOT_EXECUTED
Hardware: NOT_EXECUTED
Candidate #10: HOLD / NOT_ASSIGNED

## 1. Purpose

This file records the current convergence after the topology-lineage, improvement-Delta, trade-off, multiwinding-function, state-graph, and recent discussion reviews.

It does not replace the authoritative A0 physical-measurement mainline in research/CURRENT_MAINLINE_OVERRIDE_2026-08-20.md.

It fixes the exploratory synthesis branch so later discussion does not keep changing the research core whenever a new mechanism is raised.

Research sequence:

existing literature-traceable circuit structures / Deltas
-> fixed named host
-> explicit physical nodes and legal states
-> mathematics
-> PSIM waveform validation
-> loss ledger
-> prior-art closure
-> hardware

Topology evolution search has already been performed. Do not restart broad lineage mining unless a specific evidence gap appears.

## 2. Fixed system boundary

Vin = 12 Vdc anchor
Pout = 2 kW anchor
Vout = 220 Vac / single phase / 50 Hz

Iin,ideal = 2000 / 12 = 166.7 A

This current is a boundary condition, not the novelty claim. The topology can change which devices and conductors carry the current, RMS / peak / circulating content, where the first meaningful voltage rise occurs, and how much extra current must be created for auxiliary functions.

## 3. Fixed research host

The preferred research host is a center-tapped, self-oscillating push-pull / Royer-derived power stage.

The host must retain a real power role:

12-V source
-> center-tapped magnetic power structure
-> alternating Q1 / Q2 main-switch paths
-> HF magnetic transfer
-> secondary power transfer

The host is chosen because it gives a concrete named circuit whose power graph and modifications can be traced. This is not an efficiency ranking and does not establish that self-oscillation is superior to external excitation at 12 V / 2 kW.

Classical core-saturation-triggered Royer operation and resonant / magnetic-feedback self-oscillation must not be merged into one undefined model. The first actual schematic must select one explicit host variant.

## 4. Fixed core research question

Can the switches, windings and magnetic current already required for the main power-transfer stage be re-used to perform commutation, reset and/or energy recovery, so that the same required functions need less added full-power hardware and less added RMS current under a fair resource comparison?

A more specific commutation form is:

Can current already present at the end of a transfer interval be handed into a legal commutation path to move the switch-node capacitances and enter the next transfer state, without requiring a large dedicated circulating current to be maintained for the whole switching period?

Important correction: qK does not create inductor current from nothing. Commutation current must come from current already present in the preceding transfer state, magnetizing / leakage / reflected-load current, or current deliberately built during a transition interval, with its time/stress/loss counted.

Therefore the target is re-use and reduced incremental burden, not zero commutation cost.

## 5. What the previous literature work already tells us

### 5.1 Keep integrated when physically useful

Relevant evidence families: Royer / self-oscillating push-pull; resonant push-pull; active-clamp / leakage-energy-recovery push-pull; matrix transformer / controlled-leakage integrated magnetics.

Supported design direction:
- the transformer is already a required main-power element;
- leakage, magnetizing state, parasitic/device capacitance and winding geometry can be deliberate design variables;
- existing magnetic current may support switch-node transition;
- winding/termination geometry can matter more than simple arithmetic current splitting.

### 5.2 Do not force every function into the main magnetic element

MAB / hardware-decoupling / externalized-inductance work provides the counterexample: excessive integration can create cross-coupling; required commutation/balancing inductance may conflict with best bulk-transfer coupling; some inductive or reset function may be better partially externalized.

Therefore the research is not 'integrate everything'. The actual question is which functions should share the main hardware, and which should remain separate.

## 6. Converged integration scope

The first design should converge on partial / selective integration.

### 6.1 Functions that should be inside the first research cell

A. center-tapped main HF power transfer
B. Q1 / Q2 alternating main-switch paths
C. self-oscillating / magnetic-resonant feedback mechanism
D. explicit Lm / Llk / device-Coss interaction
E. winding / termination / magnetic geometry as a design variable
F. a legal transfer -> commutation -> transfer energy path

### 6.2 Functions that may be external if required

- small additional Lcomm
- small Cr
- clamp / reset / recovery path
- startup assistance
- flux-balance correction
- frequency-window limiting
- over-current / fault shutdown

They are not automatically rejected for adding components. Their cost must be compared with what they save.

### 6.3 Functions deferred to layer 2

- reconfigurable Neff
- reconfigurable Zref
- secondary stacking
- flying-capacitor gain sharing
- SST multi-cell series/parallel architecture
- direct HF-link AC synthesis
- active 2omega power decoupling

They return only if the first-circuit result exposes a specific gain / reflected-impedance / system-level bottleneck that they solve.

## 7. S1 and S2 are implementation bounds, not different research topics

S1 — more integrated commutation: use as much of the existing magnetic structure as is useful for main transfer + designed Llk / magnetic mode + self-oscillation feedback + commutation support.

S2 — partially externalized commutation: keep the main magnetic path optimized for bulk transfer and add only the commutation/reset element that cannot be efficiently obtained from the shared structure.

Both answer the same question: at what integration level does saved hardware / switching loss exceed the added RMS, copper, core, stress and control burden?

No assumption that S1 is more advanced or S2 is a failure.

## 8. First actual circuit must now be node-level, not only functional

Minimum host skeleton:

                  Vin = 12 V
                     |
                    NCT
                 /       \
              P1           P2
               |            |
             ND1           ND2
               |            |
              Q1            Q2
               |            |
               +-----GND-----+

           shared HF magnetic core
                    |
               secondary S
                    |
             rectifier / load

magnetic / resonant feedback
      -> Q1 gate / Q2 gate

This is only a skeleton. The real first graph must explicitly model Lm, Llk1/Llk2, Q1/Q2 Coss, winding polarity, gate-feedback path, secondary load / reflected load, and any Cr / Lext / clamp path if used.

Ideal transformer + ideal switch alone is insufficient because the research question is about transition energy and current path.

## 9. Minimum switching-state sequence

qT1   Q1-side main transfer
  ->
qK12  Q1-to-Q2 commutation / Coss transition / reset
  ->
qT2   Q2-side main transfer
  ->
qK21  Q2-to-Q1 commutation / Coss transition / reset
  -> repeat

For every state answer:
1. Which switch is ON / OFF?
2. Which winding section carries current?
3. Where did the current come from?
4. Where is energy stored?
5. What causes the outgoing switch to stop conducting?
6. What physical variable creates the incoming gate condition?
7. How are Q1/Q2 Coss charged/discharged?
8. Where does residual leakage/magnetic energy go?
9. Is there a legal current-return path at all times?
10. Does net volt-second / flux balance close over a cycle?

If any item is unknown, mark it OPEN; do not hide it with a functional label.

## 10. Required PSIM / oscilloscope signals

The first PSIM model is for mechanism validation, not immediate 2-kW optimization.

Mandatory waveforms:
CH1  VGS1
CH2  VDS1
CH3  IQ1
CH4  VGS2
CH5  VDS2
CH6  IQ2
CH7  primary / magnetizing current
CH8  leakage / commutation current
CH9  secondary current or rectifier-input current
CALC/TRACE  flux or B(t)
CALC/TRACE  VHV / rectified output

Minimum questions the waveforms must answer:
V1  Does self-oscillation sustain without an external PWM edge generator?
V2  Does flux remain bounded / balanced?
V3  Can the qT current be traced into the qK commutation path?
V4  Is Coss transition actually supported by that current?
V5  Does residual energy have a legal recovery/reset destination?
V6  What are VDS peak, current peak and RMS penalties?

Do not claim ZVS merely because VDS falls. Gate timing and actual turn-on condition must be checked.

## 11. Comparison structure

After the first graph works, compare at least:
Case A  selected named self-oscillating center-tapped host
Case B  same host + proposed integrated / re-used commutation path
Case C  reasonable established external/clamp commutation solution

Matched quantities must include the same Vin / Pout / voltage domain, approximately matched semiconductor conduction resource, copper/core-resource accounting, and declared switching-frequency/work range.

Measure / calculate: Irms / Ipk, VDS,pk, MOS conduction loss, switching energy / loss, winding + termination copper loss, core loss, circulating/reactive RMS, clamp / auxiliary loss, gate/control loss, and total candidate loss.

A result is only useful if it shows what was removed, what was added, and where the loss moved.

## 12. What is now fixed versus still open

Fixed for the next branch:
- System boundary = 12 V / 2 kW -> 220 Vac single phase
- Research host = center-tapped self-oscillating push-pull / Royer-derived family
- Core question = hardware / magnetic-current functional re-use with lower incremental cost
- Integration policy = selective / partial integration
- First focus = transfer + commutation + reset/recovery
- External control = supervisory/corrective, not assumed to command every switching edge
- Next artifact = explicit first schematic + probes + state graph

Still open:
- exact Royer-derived host variant
- exact winding count / placement
- exact Llk / Lm target
- whether Cr is required
- whether external Lcomm is required
- whether active clamp / reset path is required
- whether self-oscillation remains practical at 12 V / 2 kW
- whether S1 or S2 is lower-loss
- whether the resulting structure is novel

## 13. Research-state protection

This convergence does not alter the formal A0 measurement authority.

Novelty = NOT_ESTABLISHED
PSIM = NOT_EXECUTED
Hardware = NOT_EXECUTED
Candidate #10 = HOLD / NOT_ASSIGNED

The next exploratory action is not another broad literature search. It is:

re-open the already-collected donor circuit structures
-> select one explicit Royer-derived host variant
-> extract the real commutation / recovery connections from the closest donor circuits
-> draw First Circuit v1 with named nodes
-> derive the minimum state equations
-> run PSIM and capture the mandatory waveforms
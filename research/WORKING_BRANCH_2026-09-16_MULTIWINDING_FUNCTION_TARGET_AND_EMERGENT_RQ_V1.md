# 2026-09-16 — Multiwinding Function Target and Emergent Research-Question Workflow v1

Status: `WORKING_BRANCH / SYNTHESIS_PRE-MATH / NO_PRUNING`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

Before combining named topology mechanisms or the current `M1...M10` mechanism set, define what the multiwinding transformer is originally intended to accomplish inside the 12 V / 2 kW research boundary.

The combination process is **not** required to preserve the original problem statement unchanged. A combination may expose a different useful function, a different bottleneck, or a different research question. Such a result is not automatically rejected. It must be recorded as an emergent research question and then subjected to mathematical validation before PSIM.

The workflow is therefore:

```text
original multiwinding intent
-> mechanism/topology combination
-> actual state graph
-> compare obtained functions against intended functions
-> record unexpected/emergent functions and new research questions
-> mathematical validation
-> PSIM only after mathematical closure is sufficient
```

This file does not rank candidates and does not establish novelty.

---

## 2. Historical baseline: what the original multiwinding idea was trying to do

The recovered historical intent was not merely to modify Royer timing. The starting idea was a shared magnetic structure with multiple power-primary/winding sections, magnetic feedback/self-commutation, and an output winding, with the low-voltage high-current input power distribution as an early concern.

The original design intent can be stated more cleanly as:

```text
12 V high-current source
        |
        +--> W1 power path
        +--> W2 power path
        +--> possibly additional winding/port roles
                 |
          shared magnetic structure
                 |
            voltage-domain rise
                 |
           downstream 220 Vac synthesis
```

The critical correction is that `W1/W2` should begin as **load-bearing magnetic/power ports**, not be predefined as `main winding + feedback winding`.

---

## 3. Multiwinding target-function set

The following target set defines what we originally hope the W1/W2 region can do. It is a design target set, not a requirement that every candidate must satisfy all functions.

### T1 — Early low-voltage current distribution

Desired effect:

```text
Iin = iW1 + iW2 + ...
```

The purpose is to prevent one local switch/winding/interconnect path from carrying the entire low-voltage input current. This is not considered a benefit unless RMS, copper allocation, termination loss, semiconductor loss, or current-path geometry improves under a fair resource comparison.

### T2 — High-frequency magnetic power transfer

W1/W2 must be able to participate in the first high-frequency power-transfer event, rather than being only sensing or auxiliary windings.

### T3 — Voltage/current-domain transformation

The magnetic structure should contribute materially to moving the system away from the 12-V / hundred-ampere domain toward a higher-voltage/lower-current domain.

### T4 — Reflected-impedance transformation

The state of the winding structure may affect:

```text
Zref(q) = [Np(q)/Ns(q)]^2 * Zload
```

The research interest is not only output voltage gain but whether the low-voltage source and switches see a more useful effective impedance/current condition.

### T5 — Main-power sharing with non-fixed winding roles

A winding is not permanently classified as `main`, `feedback`, or `auxiliary` before the state graph is known. A winding may be allowed to move among transfer, commutation, reset, balancing, or sensing roles if its VA and energy path are physically closed.

### T6 — Structural gain / effective-turn reconfiguration

Explore whether winding connection can change:

```text
Neff(q), G(q), Zref(q)
```

using series/parallel, tap, polarity, winding-section, or other legal connection states.

### T7 — Intentional leakage / resonant / commutation function

Explore whether leakage, differential mode, or another magnetic mode can be promoted from parasitic behavior to an intentional function:

```text
Lcomm(q), Lr(q), Ecomm(q)
```

rather than always adding a separate external commutation inductor.

### T8 — Current balancing / spatial magnetic distribution

Explore matrix, multi-primary, multi-secondary, coupled, or integrated-magnetic arrangements that affect current sharing, termination loss, flux cancellation, or winding utilization.

### T9 — Secondary voltage stacking / vector formation

Explore whether secondary winding sections can provide additive/subtractive or series-stacked voltage states instead of relying solely on one large fixed turns ratio.

### T10 — Phase/polyphase coordination

Explore whether multiple load-bearing branches can be phase shifted or role rotated while the final system remains single-phase at 220 Vac.

### T11 — Partial-power or conductive/magnetic path sharing

Keep open the possibility that not all output power must be processed in exactly the same magnetic path if a legal isolated/partial-power architecture appears.

### T12 — Direct HF-link / AC-state contribution

This is optional, not a starting requirement. If a combination naturally creates useful HF-link voltage vectors or direct AC-synthesis states, record it rather than forcing the system back into a conventional rectifier + HV bus + inverter structure.

### T13 — Single-phase `2omega` participation only if real storage exists

Do **not** require the multiwinding transformer to solve the single-phase double-line-frequency energy problem. It becomes a valid function only if a real storage/routing state is identified. The HFT core alone is not assumed to be the 100/120-Hz energy buffer.

---

## 4. Original expectation versus mechanism-matrix / SST expansion

| Area | Original expectation | What the mechanism matrix / named-topology / SST search adds | Possible changed research question |
|---|---|---|---|
| Input current | Multiple primaries or cells split the 12-V current | Matrix transformer, multiphase, ISOP/IPOS, interphase SST suggest spatial and modular current distribution | Is geometry/termination/magnetic integration more important than simple branch count? |
| Voltage gain | Transformer turns ratio raises voltage | Y/Trans-Z/A-source, voltage stacking, adjustable turns, topology morphing add structural gain states | Can gain and reflected impedance be changed by the same winding state? |
| Winding role | Main winding + feedback/auxiliary role was initially considered | MAB/QAB/multiwinding SST treat windings as peer power ports | Can W1/W2 remain symmetric load-bearing ports and rotate secondary roles? |
| Soft switching | Royer/self-oscillation and later external correction were considered | LLC/CLLC, controllable leakage, MAB ZVS, matrix integrated magnetics shift attention to magnetic energy state | Can the same winding/magnetic state that transfers power also provide commutation energy? |
| Current sharing | Parallel paths expected to reduce local current | Matrix transformer literature highlights termination, flux distribution, winding geometry, and integrated current sharing | Can current sharing be obtained structurally without simply duplicating copper/silicon? |
| Gain flexibility | Fixed transformer ratio or external control | Topology morphing and adjustable-turn transformers provide `Neff(q)` as a power-state variable | Can `q` change `Neff`, `Zref`, and `Lcomm` together? |
| Phase coordination | Mainly considered as interleaving / 0-120-240 deg current distribution | Multiport/MAB/polyphase SST suggests phase can also determine port power and role | Can a branch rotate between transfer and commutation while aggregate transfer continues? |
| Output synthesis | Conventional post-HFT rectification / HV bus / inverter was the default reference | Matrix-type SST and direct HF-link converters show alternative voltage-state formation | Does a useful W1/W2 combination expose a new X1/X3 overlap worth studying? |
| Power processing fraction | Assumed nearly all power follows the main transformer path | Hybrid SST and partial-power concepts show full-power processing is not mandatory in every controllable branch | Can a small processed-power path control or correct a larger bulk-power path? |

The right response to an unexpected useful function is **not** “this is not what we originally wanted, reject it.” The right response is:

```text
1. identify the new function;
2. determine which physical state creates it;
3. state the new research question explicitly;
4. check whether it remains inside the system boundary;
5. mathematically validate it before simulation.
```

---

## 5. M1–M10 interpreted against the multiwinding target set

The current mechanism set is retained as a synthesis vocabulary:

```text
M1  current-fed
M2  direct + stored-energy transfer
M3  winding / impedance-source gain
M4  reconfigurable effective turns
M5  common/differential magnetic modes
M6  controllable leakage / resonance
M7  polyphase role rotation
M8  secondary voltage stacking
M9  bulk-power path + small regulating path
M10 direct DC-AC magnetic/matrix states
```

Their purpose is not to be combined blindly. For each combination, ask which target functions `T1...T13` are actually obtained.

Examples:

```text
M1 + M4
-> expected: T1, T3, T4, T6
-> possible emergent: T7 if reconfiguration also changes leakage

M4 + M5
-> expected: T4, T6
-> possible emergent: one q-state simultaneously changes Neff, Zref and Leff

M5 + M7
-> expected: T5, T7, T10
-> possible emergent: rotating commutation role without a fixed auxiliary winding

M3 + M8
-> expected: T3, T4, T9
-> possible emergent: lower required transformer turns ratio through secondary stacking

M9 + multiwinding SST principle
-> expected: T11
-> possible emergent: small regulating winding/port controls a larger bulk-power path

M10 + matrix-type SST principle
-> expected: T12
-> possible emergent: reduced post-HFT processing or a different X1/X3 boundary
```

No example above is yet a legal converter topology.

---

## 6. Combination record: required before mathematics

Every generated combination must have this record before mathematical validation:

```text
Combination ID:
Donor named topologies/mechanisms:
M-set:

Original target functions expected:
Emergent functions actually suggested:
Functions not obtained:

W1 role in q1/q2/...:
W2 role in q1/q2/...:
Other windings/ports:

Main power path:
Temporary stored-energy path:
Commutation/reset path:
Secondary combination path:

Connection states:
Neff(q):
Zref(q):
Leff/Lcomm(q):
phase relation:

New research question exposed by this combination:
Still inside 12 V -> 220 Vac / 2 kW boundary? YES/NO/CONDITIONAL
```

The field `New research question exposed by this combination` is mandatory. This prevents the synthesis process from being trapped by the original wording of the problem.

---

## 7. Emergent research-question registry

Initial questions to keep open while combinations are generated:

### ERQ-1 — Current split versus real loss relocation

Can a shared multiwinding/matrix structure reduce local 12-V current stress and termination/copper loss under equal total copper and semiconductor resources, rather than merely dividing the same `I^2R` loss?

### ERQ-2 — One state controls gain and commutation

Can one legal winding connection state produce:

```text
q -> {Neff(q), Zref(q), Lcomm(q)}
```

so that gain/impedance transformation and soft-commutation energy are structurally coupled?

### ERQ-3 — Common-power / differential-commutation magnetic modes

Can the same magnetic assembly carry bulk transfer in a common mode and transient commutation/balancing energy in a differential mode without unacceptable circulating current or added core loss?

### ERQ-4 — Load-bearing role rotation

Can W1/W2/other symmetric power windings rotate through transfer and commutation roles while total output power remains continuous enough to avoid a dedicated auxiliary magnetic branch?

### ERQ-5 — Parallel-primary / series-secondary multifunctionality

Can the same elemental transformer set simultaneously create early current distribution on the 12-V side and useful voltage stacking on the high-voltage side with stable sharing and acceptable secondary RMS current?

### ERQ-6 — Structural gain instead of extreme fixed turns ratio

Can winding-state reconfiguration or coupled impedance-source behavior reduce the required fixed transformer ratio while preserving controllable current and device stress?

### ERQ-7 — Multiwinding power router instead of main/feedback hierarchy

Does treating W1/W2 as peer power ports reveal a more useful power-routing problem than the original main-winding + feedback-winding interpretation?

### ERQ-8 — New X1/X3 overlap

If a winding/vector/matrix combination naturally provides useful HF-link output states, can post-HFT rectification/inversion work be reduced without creating a worse RMS-current, commutation, filtering, or single-phase `2omega` problem?

### ERQ-9 — Partial-power magnetic control

Can a lower-VA winding/port regulate or correct a bulk-power path so that some desired function does not require processing the full 2 kW through every active element?

### ERQ-10 — Magnetic integration becomes the research problem

If topology combinations collapse to known converter graphs, is the actual residual research question instead the integrated magnetic structure: current sharing, leakage shaping, modal inductance, winding termination, or controllable magnetic rank?

These questions are deliberately broader than the original Royer-centered wording. They are hypotheses to be mathematically tested, not novelty claims.

---

## 8. Mathematics must precede PSIM

Once a combination has a legal state graph, the first-pass mathematical gate is:

### MG1 — State legality and power continuity

Explicitly identify switch/winding connections and current return paths for every q-state.

### MG2 — Volt-second / flux balance

For each independent magnetic mode:

```text
vk = sk * Nk * dPhi/dt
integral(v_mode dt) over Ts = 0   [steady periodic operation]
```

Check flux excursion and saturation margin.

### MG3 — Ampere-turn / current-sharing consistency

```text
sum(Nk * ik) = Rm * Phi
```

or the corresponding multi-mode inductance/magnetic-circuit model. Explicitly calculate circulation when parallel/equal-voltage constraints are imperfect.

### MG4 — Gain and reflected impedance

For every structural state:

```text
G(q) = Vo/Vin
Zref(q) = [Np(q)/Ns(q)]^2 * Zload
```

or the appropriate generalized multiport equivalent.

### MG5 — Winding and switch VA / RMS / peak stress

Calculate actual RMS and peak currents. Average branch sharing is not sufficient.

### MG6 — Resonance / commutation energy

If ZVS/resonance is claimed:

```text
Ecomm = 0.5 * Lcomm * Icomm^2
```

must be checked against required capacitor/transition energy, including relevant `Coss` and parasitic energy.

### MG7 — Power and energy conservation

For each q-state and over a switching period:

```text
sum(pin) - sum(pout) = dWstored/dt + Ploss
```

Any stored-energy interval must have a defined release/reset path.

### MG8 — First loss ledger

At minimum include:

```text
MOS conduction
switching / Coss
winding copper RMS
core loss
capacitor ESR
resonant / clamp / circulating-current loss
added gate/control/auxiliary power where material
```

A multifunctional state only becomes interesting if the saved/removed loss and hardware burden are not simply relocated into larger added losses.

### MG9 — Single-phase boundary closure

If the combination reaches toward direct AC synthesis or removes an intermediate stage, check where the 50/60-Hz output envelope and single-phase `2omega` energy go. Do not assume internal polyphase removes `2omega`.

Only after these mathematics are sufficiently closed should the candidate enter PSIM.

---

## 9. PSIM entry criterion

A candidate is ready for PSIM when all of the following are explicit enough to simulate without inventing missing physics during model construction:

```text
- q-state graph exists
- winding endpoints and polarity are defined
- power/current return paths are closed
- magnetic modes / effective inductances are defined
- Neff / gain state is defined
- expected current direction and stress are analytically bounded
- commutation/resonant claim has an energy equation
- no unresolved flux-reset contradiction
```

PSIM then tests whether the derived state behavior actually appears. PSIM does not replace the mathematics.

---

## 10. Immediate next execution

Generate a broad first batch of actual W1/W2 combinations from:

```text
M1...M10
+
named-topology genealogy
+
SST/multiwinding/matrix/MAB mechanisms
```

For every generated combination:

1. state original target functions `T1...T13` expected;
2. identify unexpected functions;
3. write one explicit emergent research question;
4. define the minimum state graph;
5. do not prune merely because the result differs from the original Royer-centered problem;
6. select a small coverage set only after the broad batch exists, then perform `MG1...MG9` mathematics before PSIM.

This preserves the original intent while allowing the combination process to discover a better research problem inside the same 12-V-to-single-phase-220-V system boundary.

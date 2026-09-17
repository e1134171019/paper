# 2026-09-17 — Self-Oscillation × Existing-Delta Synthesis v1

Status: `WORKING_BRANCH / SYNTHESIS / PRE-STATE-GRAPH / PRE-MATH`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

This file resumes the research at the correct point after the topology-evolution work was already completed.

We are **not** re-searching topology evolution and we are **not** looking for one published converter that already contains every desired function.

The current task is:

```text
existing literature-traceable Deltas
+
self-oscillation / externally bounded correction
+
abstract multiwinding magnetic structure
+
SST architecture layer
->
small set of our own synthesis directions
```

The role of literature is evidential: each imported physical idea must have prior technical support. The combined method remains ours to define and later validate.

Primary existing evidence files:

```text
WORKING_BRANCH_2026-09-16_TOPOLOGY_LINEAGE_DELTA_ANALYSIS_V1.md
WORKING_BRANCH_2026-09-16_MULTI_AI_LINEAGE_DELTA_EXPANSION_V2.md
WORKING_BRANCH_2026-09-16_DELTA_TRADEOFF_RQ_TRACEABILITY_MATRIX_V1.md
WORKING_BRANCH_2026-09-16_MULTIWINDING_FUNCTION_TARGET_AND_EMERGENT_RQ_V1.md
```

---

## 2. Boundary and notation

System boundary remains:

```text
Vin = 12 Vdc
Pout = 2 kW
Vout = 220 Vac
single phase
```

The present synthesis concerns the first HF magnetic conversion region. The final 220-Vac synthesis and single-phase 2ω energy obligation remain separate system constraints.

`W1/W2/W3` below are **abstract winding sections / magnetic ports**, not fixed Royer labels.

Their physical identity is intentionally not frozen before the state graph exists.

A concrete later candidate may map them to:

```text
main power sections
feedback/sensing winding
commutation winding
reconfigurable winding section
secondary section
```

but that mapping must come from the candidate state graph, not from the symbol name.

---

## 3. Literature-backed building blocks already available

### B1 — Natural self-oscillation / magnetic-resonant commutation

Evidence role:

```text
Royer / Baxandall / modern self-oscillating push-pull-resonant work
```

Supported idea:

```text
the next switching event can arise from magnetic/resonant state,
not necessarily from a fixed external PWM timer.
```

### B2 — Leakage / transformer parasitics can become intentional resonant resources

Strong donors:

```text
A7 — resonant push-pull reuses Llk, Lm and parasitic C in the resonant state
A8 — leakage is selected from a soft-switching / loss target
E2/E4 — winding / PCB geometry can deliberately set useful leakage
```

Supported idea:

```text
Llk is not automatically a defect to minimize;
it can be a designed commutation variable.
```

### B3 — Some inductive function should sometimes be externalized

Strong counterexample donors:

```text
D2  — hardware-decoupled MAB
D2a — current-fed MAB with selected external inductors
```

Supported idea:

```text
full magnetic integration is not automatically optimal.
A selected commutation/balancing inductance may be separated from the bulk-transfer coupling path.
```

### B4 — One connection state can change more than one magnetic/electrical quantity

Strong donors:

```text
C3/C4 — reconfigurable winding state changes effective ratio and resonant/leakage parameter
C5    — bridge-leg connection state reconfigures effective turns ratio
E5    — reluctance state changes effective ratio behavior
```

Supported idea:

```text
q can become a structural power state,
not only a PWM duty/frequency state.
```

Possible abstract consequence:

```text
q -> {Neff, Zref, Lcomm}
```

This remains an extension, not a requirement for the first proof.

### B5 — Multiwinding geometry can change real high-current implementation quality

Strong donors:

```text
E1 — matrix transformer: current distribution, termination reduction, flux cancellation
E3 — controlled-leakage/symmetric multiwinding transformer
E4 — winding layout directly sets target leakage
```

Supported idea:

```text
multiwinding value must come from real geometry / termination / magnetic behavior,
not merely from arithmetic current splitting.
```

### B6 — SST / MAB is an architecture donor, not the inner self-oscillating circuit

Supported ideas:

```text
low-side parallel power cells
high-side series / stacked contribution
shared magnetic infrastructure
peer active ports
reduced-switch multiport arrangements
partial-power correction branches
```

Constraint:

```text
SST does not determine the inner W1/W2/W3 self-oscillation mechanism.
It is applied after a valid inner magnetic cell/state graph exists.
```

---

# 4. Synthesis class S1 — Integrated self-commutating magnetic structure

## 4.1 Core idea

Use the same shared magnetic structure for:

```text
bulk HF transfer
+
deliberately designed leakage / differential commutation energy
+
magnetic/resonant self-oscillation timing
```

The external controller only constrains the natural behavior.

Conceptual structure:

```text
12 V
 |
 +---- W1 / power section ----+
 |                            |
 +---- W2 / power section ----+--> shared magnetic structure --> raised-voltage side
                              |
                         designed Llk / modal energy
                              |
                         natural commutation

W3, if used, is initially a sensing/feedback function only;
it is not assumed to carry full output power.
```

## 4.2 Evidence chain

```text
self-oscillation        <- Royer/Baxandall/self-oscillating resonant lineage
intentional Llk/Cp use <- A7
loss-based Llk sizing  <- A8
physical leakage design<- E2/E4
high-current geometry  <- E1/E3
```

No source is claimed to contain this exact combination.

## 4.3 Original target functions addressed

Primary:

```text
T2 HF magnetic power transfer
T3 voltage/current-domain transformation
T7 intentional leakage / commutation
T8 spatial/magnetic current distribution
```

Possible but not yet proven:

```text
T1 low-side current distribution
T5 non-fixed role use during commutation
```

Not required in S1:

```text
T6 structural gain reconfiguration
T9 secondary stacking
T12 direct HF-link AC synthesis
```

## 4.4 Minimum state concept

```text
qT-A: useful HF power transfer
qK-AB: designed leakage/modal energy moves the switching node toward the opposite state
qT-B: opposite transfer state
qK-BA: mirror commutation
qR: any residual resonant / leakage energy returns to a legal state
```

The exact switch/winding connections remain OPEN.

## 4.5 New research question exposed

```text
RQ-S1:
Can the same magnetic geometry that efficiently transfers 2-kW-class power
also retain just enough controlled leakage/modal energy to generate robust natural commutation,
without the added RMS/core/circulation losses exceeding the switching-loss reduction?
```

This is the cleanest direct continuation of the original `self-oscillation + externally bounded correction` idea.

---

# 5. Synthesis class S2 — Decoupled self-commutating branch

## 5.1 Core idea

Do not force the bulk-power magnetic path to provide all required commutation inductance.

Separate the roles:

```text
W1/W2 magnetic structure -> optimized mainly for bulk HF power transfer

Lcomm / PCOMM branch     -> optimized mainly for natural commutation energy

feedback/sensing path    -> determines or observes natural switching condition
```

Possible implementation families later:

```text
external Lcomm
auxiliary commutation winding
separate magnetic leg
hybrid: Lcomm = Llk,designed + Lext
```

## 5.2 Evidence chain

```text
why leakage can be useful     <- A7/A8
why integration can be harmful<- D2/D2a
why geometry can separate modes<- E3/E4
self-oscillation              <- self-oscillating lineage
```

## 5.3 Target functions addressed

Primary:

```text
T2 HF transfer
T7 intentional commutation energy
```

Potentially:

```text
T5 winding-role specialization by state
T8 magnetic spatial distribution
T11 lower-VA correction/commutation branch
```

## 5.4 Minimum state concept

```text
qT: bulk power flows mainly through the tightly coupled transfer path
qK: selected commutation branch temporarily receives/releases transition energy
qR: commutation energy returns to source/load/next state
```

Important distinction:

```text
bulk-transfer energy path != commutation-energy path
```

## 5.5 New research question exposed

```text
RQ-S2:
For the 12-V / 2-kW boundary, what fraction of the required commutation inductive function
should remain integrated in the transformer and what fraction should be externalized?
```

A later design variable can be retained:

```text
rho_L = Lintegrated_comm / Lcomm_total
```

with no assumption that `rho_L = 0` or `1` is best.

---

# 6. Synthesis class S3 — Reconfigurable self-oscillating magnetic state

## 6.1 Core idea

Only after S1/S2 physical legality is understood, allow one winding/connection state `q` to modify the magnetic/electrical operating point.

Desired abstract state:

```text
q -> {Neff(q), Zref(q), Lcomm(q)}
```

Because self-oscillation is retained, this may also change:

```text
f_nat(q)
Ecomm(q)
```

## 6.2 Evidence chain

```text
reconfigurable turns / leakage coupling <- C3/C4
bridge-state ratio reconfiguration      <- C5
magnetic reluctance / ratio control      <- E5
intentional leakage design               <- E2/E4
self-oscillation                         <- self-oscillating lineage
```

Again, the sources support the individual physical operations; no claim is made that they already implement our combined method.

## 6.3 Target functions addressed

Primary extension functions:

```text
T4 reflected-impedance transformation
T6 effective-turn / structural gain reconfiguration
T7 state-dependent commutation
```

Possible secondary functions:

```text
T5 role reassignment
T9 secondary voltage stacking
```

## 6.4 Minimum state concept

```text
qN1: base effective-ratio / leakage state
qN2: alternate effective-ratio / leakage state

inside each qN state:
  natural transfer/commutation sequence still exists
```

Critical rule:

```text
reconfiguration must not require a high-loss selector carrying the full raw 12-V / ~170-A path
unless the loss ledger proves it worthwhile.
```

## 6.5 New research question exposed

```text
RQ-S3:
Can one legal magnetic connection state simultaneously improve transformation ratio,
source-side reflected impedance and commutation conditions,
without turning structural reconfiguration into a larger conduction/RMS penalty?
```

S3 is deliberately retained as an advanced branch rather than being forced into the first proof.

---

# 7. SST layer after the inner cell

SST concepts are now reinserted at the correct system level.

If one self-oscillating magnetic cell becomes valid, SST-derived architecture options include:

```text
12-V side:
parallel cells / distributed current entry

raised-voltage side:
series / stacked voltage contribution

system integration:
shared HF link
reduced-switch interconnection
partial-power correction
multiport routing
```

This creates an important separation:

```text
INNER METHOD:
self-oscillation + magnetic/commutation function

OUTER ARCHITECTURE:
SST-style series/parallel/shared-port organization
```

The SST layer is therefore not discarded and not fused blindly into the inner converter.

---

# 8. What is ours versus what literature supports

## Literature supports

```text
natural self-oscillation is physically realizable
transformer leakage/parasitics can be designed as useful resonant elements
some leakage/inductance should sometimes be externalized
winding connection states can change effective ratio and resonant parameters
matrix/multiwinding geometry can change real current/termination behavior
SST/MAB architectures can arrange multiple active magnetic power paths
```

## Our synthesis question

```text
Can these separately supported mechanisms be arranged under the 12-V / 2-kW boundary
so that the magnetic structure itself performs useful HF transfer and natural commutation,
while external control only bounds the behavior,
and optional structural states later improve gain/impedance/commutation together?
```

That combined statement is a research hypothesis, not a literature fact and not a novelty claim.

---

# 9. Immediate result

The synthesis space is now reduced to three architecture classes rather than a large unrestricted combination set:

```text
S1 — integrated self-commutating magnetic structure
S2 — decoupled / hybrid commutation branch
S3 — reconfigurable self-oscillating magnetic state
```

No ranking is assigned yet.

The next step is **not another literature survey**.

The next step is to create one minimal, concrete state graph for S1 and one for S2, because these two differ by the central unresolved trade-off:

```text
integrate commutation inductance
vs
externalize commutation inductance
```

For each state graph, define only:

```text
which winding/branch is connected
where input current flows
where useful power flows
where commutation energy is stored
what triggers the opposite switch state
where residual energy returns
```

Only after those two graphs are legal should mathematics resume.

S3 remains parked until S1/S2 reveal whether state-dependent `Neff/Zref/Lcomm` is genuinely useful rather than added complexity.

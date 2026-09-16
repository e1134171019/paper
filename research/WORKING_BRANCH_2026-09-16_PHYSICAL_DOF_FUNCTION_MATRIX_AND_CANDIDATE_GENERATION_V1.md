# 2026-09-16 — Physical DOF × Function Matrix and Broad Candidate Generation v1

Status: `WORKING_BRANCH / SYNTHESIS_ONLY / NOT_FALSIFIED`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

This file executes the immediate next task from `WORKING_BRANCH_2026-09-15_MAGNETIC_POLYPHASE_SYNTHESIS_RESET_V1.md`.

The order in this file is deliberately generative:

```text
enumerate physical DOFs
-> map DOF-to-function authority
-> generate broad state-combination hypotheses
-> do NOT prune here
```

This is not a prior-art gate, loss ranking, topology selection or Candidate #10 assignment. The formal A0 / File64 measurement mainline remains unchanged.

## 2. Ontology guardrail

Keep three layers separate:

```text
DOF = what physical/configuration state can be changed
PM  = what energy-transfer/storage/commutation mechanism occurs
F   = what function/result is obtained
```

File30 remains authoritative for canonical L3 mechanisms: PM-1 magnetic flux-linkage transformation, PM-2 inductive energy transfer, PM-3 capacitive charge-transfer/stacking, PM-4 reactive-energy-assisted commutation, PM-5 capacitive field-energy buffering, PM-6 controlled bidirectional storage-port transfer, PM-7 semiconductor switching-state AC synthesis.

The matrix below adds upstream controllable state-space; it does not replace the PM ontology.

## 3. Expanded physical-DOF basis

| ID | Physical DOF | First-principles meaning |
|---|---|---|
| D1 | `M` magnetic mode / flux-path authority | Which independent magnetic mode or limb carries active flux: main, differential, balancing, common/zero-sequence where physically realizable |
| D2 | `N` effective turns / tap state | Which turns participate; induced voltage/current ratio and reflected impedance change with state |
| D3 | `POL` winding polarity / vector orientation | Dot orientation, sign, phase-vector mapping, additive/subtractive induced voltage |
| D4 | `CONN` winding connection topology | Series/parallel, enable/disable, bypass, center-tap, fractional-turn or section recombination |
| D5 | `PORT` port-role assignment | Transfer, sensing, idle, reset, commutation actuator, temporary energy port or output-routing port |
| D6 | `L` intentional `Lm/Llk/Lcomm` state | Magnetizing/leakage/integrated inductive energy used intentionally for transfer/commutation |
| D7 | `SPACE` spatial/matrix current-flux distribution | Multi-primary/multi-secondary geometry, elemental transformers, termination placement and flux cancellation |
| D8 | `PHI` phase/polyphase schedule | Interleaving, `0/120/240 deg`, N-phase displacement, staggered switching and role rotation |
| D9 | `BIAS` magnetic operating-point control | Controlled permeability/bias/saturation-state movement; retained as available DOF without efficiency assumption |
| D10 | `PATH` conductive + magnetic path split | Part of power passes conductively and another part magnetically, including partial-power/autotransformer principles |
| D11 | `QS` semiconductor connection state | Minimum switch graph that realizes winding/port/output states; implementation-enabling DOF, not a magnetic mechanism by itself |

`D1...D11` are synthesis coordinates, not novelty claims.

## 4. Function basis

| ID | Function |
|---|---|
| F1 | Galvanic isolation |
| F2 | Voltage/current-domain transformation |
| F3 | Reflected-impedance transformation |
| F4 | Polarity / phase mapping |
| F5 | Multiport energy routing / port-role reassignment |
| F6 | Current splitting/recombination and/or flux cancellation |
| F7 | Flux / magnetic-state sensing |
| F8 | Short-time storage, reset, commutation or ZVS support |
| F9 | Structural gain/path reconfiguration |
| F10 | Staggered transfer / continuity while another branch commutates |
| F11 | HF-link voltage-state availability for later AC synthesis |
| F12 | 2omega storage/routing participation only when a real storage state exists |

Matrix symbols: `P` direct/primary authority, `S` supporting/conditional contribution, `-` not provided by the DOF alone. These symbols do not imply efficiency, novelty or complete realizability.

## 5. Physical DOF × Function matrix

| DOF | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1 `M` | S | S | S | S | S | P | P | P | S | S | S | S |
| D2 `N` | - | P | P | S | - | S | S | S | P | - | S | - |
| D3 `POL` | - | S | - | P | S | S | S | S | S | S | P | - |
| D4 `CONN` | S | P | P | P | P | P | - | S | P | S | P | S |
| D5 `PORT` | S | S | S | S | P | S | P | P | P | P | S | P |
| D6 `L` | - | S | S | - | S | S | S | P | S | S | - | S |
| D7 `SPACE` | S | S | S | S | S | P | S | S | S | S | S | - |
| D8 `PHI` | - | S | S | P | S | P | S | P | S | P | P | - |
| D9 `BIAS` | - | S | S | - | S | S | P | P | P | S | - | S |
| D10 `PATH` | - | P | P | - | P | S | - | - | P | S | S | S |
| D11 `QS` | - | S | S | P | P | S | - | P | P | P | P | P |

### Interpretation

1. `PHI` is more than ripple reduction. With `PORT` and `L`, it can separate transfer and commutation authority in time.
2. `CONN` is broader than a tap. It can change `Neff`, polarity, port availability, current distribution and sometimes `Lcomm`.
3. `M` and `SPACE` are not the same: one physical core may contain multiple modes; multiple physical branches may still collapse to one effective mode.
4. `PORT` is central to multifunctionality because a winding can change role across states.
5. `QS` is to be derived after the state graph, not used to predefine the topology family.
6. Internal polyphase coordination does not automatically provide F12; single-phase 2omega energy remains open without explicit storage/routing.

## 6. Broad candidate generation rule

Each candidate records state variables, magnetic-rank requirement, winding/connection state, phase relation, port roles, main power path, commutation path, shared functions and still-open functions.

All entries below are `GENERATED / NOT_FALSIFIED / NOT_PRIOR_ART_CLOSED`. There is intentionally no STOP/REJECT/winner in this file.

## 7. Candidate set

### C01 — Three-branch rotating commutation role
DOFs: `D5 PORT + D6 L + D8 PHI + D11 QS`

```text
phi = {0,120,240 deg}
(T,T,K) -> (T,K,T) -> (K,T,T)
```

Two branches remain in transfer while the third becomes commutation/reset/ZVS-support. Shared functions: current sharing, ripple cancellation, staggered commutation, role rotation. Open: common-core realization, current continuity, K-energy path, output synthesis.

### C02 — N-phase generalized role rotation
DOFs: `D5 + D6 + D8 + D11`

```text
phi_k = 2*pi*k/N
K role rotates through N symmetric cells
```

Expose `N` as a variable instead of assuming 3 phases. Open: optimal N, silicon normalization, magnetic layout and control burden.

### C03 — Polyphase tap-state rotation
DOFs: `D2 N + D4 CONN + D8 PHI`

Phase sets time location; tap state sets `Neff/Zref`. Hypothesis: the branch entering commutation may use a different effective-turn state from the branches still transferring. Open: avoid structural switches in the 12-V hundred-ampere path.

### C04 — State-dependent leakage reconfiguration
DOFs: `D4 CONN + D6 L`

```text
q -> {Neff(q), Zref(q), Lcomm(q)}
Ecomm(q) = 0.5*Lcomm(q)*Icomm(q)^2
```

One connection state controls gain/path and commutation-energy geometry. Open: realizable winding geometry and controllable leakage separation.

### C05 — Sense-to-actuator transient winding
DOFs: `D5 PORT + D6 L`

```text
T: auxiliary port = sensing
K: same port = reset / transient commutation actuator
T': returns to sensing
```

Same copper performs observation and transient magnetic authority. Open: auxiliary VA, reset voltage, energy direction and sensing isolation during actuation.

### C06 — Rotating sense-to-actuator port
DOFs: `D5 PORT + D6 L + D8 PHI`

No permanent auxiliary power branch is assumed. Each symmetric branch can rotate through transfer/support/commutation roles. Open: simultaneous sensing during power transfer and gate-reference implementation.

### C07 — Common-power / differential-commutation magnetic modes
DOFs: `D1 M + D6 L`

```text
Phi_m     -> bulk power transfer
Phi_delta -> balancing / transition / commutation
```

Same magnetic assembly, different modes with different jobs. Open: modal rank, energy capacity of secondary mode, residual leakage and physical inductance matrix.

### C08 — Three-limb common/differential/zero-sequence scheduling
DOFs: `D1 M + D7 SPACE + D8 PHI`

Analyze a multi-limb core in modal coordinates instead of as three independent transformers. Hypothesis: one mode temporarily supports reset/commutation while balanced branch modes continue transfer. Open: return-path reluctance, zero-sequence path and HF saturation.

### C09 — Matrix transformer with role-rotating elemental cells
DOFs: `D5 PORT + D7 SPACE + D8 PHI`

Spatially distributed elemental cells manage current/termination while their roles are scheduled rather than fixed. Open: secondary combination, current equalization and whether role rotation remains physically distinct.

### C10 — Polyphase series-primary / parallel-secondary state matrix
DOFs: `D4 CONN + D7 SPACE + D8 PHI`

Connection state changes participating primary/secondary sections while phases are staggered. Shared functions: high-current distribution, gain configuration, phase staggering. Open: safe reconfiguration under current and circulating-current control.

### C11 — Fractional-turn / vector-secondary state combiner
DOFs: `D2 N + D3 POL + D4 CONN + D11 QS`

Sectioned secondary voltages become discrete vectors rather than one fixed secondary:

```text
+Va, +Vb, +(Va+Vb), 0, -(Va+Vb), ...
```

Shared functions: turn state, polarity and HF-link level generation. Open: bidirectional blocking, commutation and output filter.

### C12 — Polyphase secondary vector synthesis
DOFs: `D3 POL + D8 PHI + D11 QS`

```text
vo_state = qa*va + qb*vb + qc*vc
```

Use phase-displaced secondary vectors to explore direct AC-state synthesis support. Open: safe state set, flux balance, switch count and matrix-converter equivalence.

### C13 — Reconfigurable vector stacking with phase scheduling
DOFs: `D2 + D3 + D4 + D8`

Effective turns, polarity, connection and phase are scheduled together. Question: can one structural state genuinely control gain/vector/phase rather than several independent subcircuits?

### C14 — Polyphase flyback-like temporary storage branch
DOFs: `D5 PORT + D6 L + D8 PHI`

The K branch temporarily stores/releases magnetic energy while other branches continue transformer transfer. Open: peak current, flux excursion and whether stored energy reduces commutation burden or merely adds RMS loss.

### C15 — Local magnetic release with global polyphase coordination
DOFs: `D5 PORT + D8 PHI`

```text
local magnetic state -> release proposal
global phase coordinator -> admission/delay/role assignment
```

Preserves local state timing while maintaining system phase. It does not itself claim ZVS or gain; those require coupling to D6/D4.

### C16 — Polyphase gain-state smoothing
DOFs: `D2 N + D8 PHI`

Discrete `Neff` changes are staggered across phases so aggregate gain can move gradually while each branch stays in a discrete structural state. Open: branch imbalance, output ripple and dwell optimization.

### C17 — Conductive/magnetic partial-power polyphase branch
DOFs: `D8 PHI + D10 PATH`

A conductive/direct portion and an isolated magnetic correction portion are phase-scheduled. Open: isolation boundary, very large 12-to-311-V ratio and actual processed-power fractions.

### C18 — Polyphase transfer with explicit high-voltage 2omega storage port
DOFs: `D5 PORT + D8 PHI + D11 QS` plus actual PM-5/PM-6 only if storage exists.

Polyphase branches smooth HF transfer while a post-transformation storage port handles single-phase 2omega energy. Internal three-phase operation alone does NOT solve 2omega.

### C19 — Bias-assisted transient commutation mode
DOFs: `D1 M + D6 L + D9 BIAS`

Low-VA magnetic bias acts only during K to shape reset/commutation. Open: nonlinear core loss, temperature/material tolerance and whether ordinary switching achieves the same result more simply.

### C20 — Bias + polyphase role rotation
DOFs: `D5 PORT + D8 PHI + D9 BIAS`

Bias/support duty rotates with phase so no branch is permanently assigned the auxiliary role. Open: C19 magnetic-bias concerns plus phase coordination.

## 8. Coverage summary

| Candidate | Main DOFs | Core synthesis question |
|---|---|---|
| C01 | PORT+L+PHI+QS | Can one phase rotate into K while others keep transferring? |
| C02 | PORT+L+PHI+QS | Is N useful as a design variable? |
| C03 | N+CONN+PHI | Can gain/impedance state rotate with phase? |
| C04 | CONN+L | Can one reconfiguration alter both gain path and commutation inductance? |
| C05 | PORT+L | Can one winding switch from sensor to transient actuator? |
| C06 | PORT+L+PHI | Can the auxiliary role rotate between power branches? |
| C07 | M+L | Can separate magnetic modes divide transfer and commutation jobs? |
| C08 | M+SPACE+PHI | Can a multi-limb core support a distinct temporary commutation mode? |
| C09 | PORT+SPACE+PHI | Can matrix cells rotate roles, not only share current? |
| C10 | CONN+SPACE+PHI | Can spatial distribution and series/parallel state share one graph? |
| C11 | N+POL+CONN+QS | Can winding sections create useful voltage-state vectors? |
| C12 | POL+PHI+QS | Can phase-displaced secondary vectors support direct AC states? |
| C13 | N+POL+CONN+PHI | Can gain/vector/phase be one structural state? |
| C14 | PORT+L+PHI | Can K use temporary storage without interrupting total transfer? |
| C15 | PORT+PHI | Can local magnetic release coexist with global phase admission? |
| C16 | N+PHI | Can discrete gain transitions be staggered across phases? |
| C17 | PHI+PATH | Can partial-power processing coexist usefully with polyphase scheduling? |
| C18 | PORT+PHI+QS | Can polyphase transfer share an explicit HV 2omega storage port? |
| C19 | M+L+BIAS | Can magnetic bias be limited to commutation only? |
| C20 | PORT+PHI+BIAS | Can bias/support duty rotate between symmetric branches? |

## 9. State variables required next

For every C01-C20, derive the smallest explicit state set:

```text
Phi_j(t)       independent magnetic-mode fluxes
i_branch,k(t)  branch currents
Neff,k(q)      effective turns state
Lcomm,k(q)     commutation-path inductance
r_k(t)         port role: T/K/SENSE/IDLE/BUFFER
phi_k(t)       phase schedule
s_k(t)         semiconductor connection state
vo_state(t)    available output/HF-link voltage state
```

A candidate becomes ready for falsification only after these variables define a legal state graph.

## 10. Magnetic-rank constraint

For every claimed independent phase or magnetic role:

```text
number of commanded independent magnetic states
<= physically available magnetic modal rank
```

A single ideal common-flux path cannot support three independently commanded `0/120/240 deg` fluxes. Candidates may share one physical core only if the coupling/inductance matrix supports the claimed independent states.

## 11. 12-V / 2-kW boundary reminder

The synthesis branch remains anchored to:

```text
Vin = 12 Vdc
Pout = 2 kW
Vout = 220 Vac
single phase
historical repository anchor fout = 50 Hz
```

Input current is about 167 A ideal and about 175 A near 95% efficiency. Later falsification must explicitly mark whether every reconfiguration device is in the LV hundred-ampere path, the higher-V/lower-I post-transformation path, or a low-VA control/commutation port.

## 12. Deliberately not done here

This file does not rank C01-C20, declare novelty, close prior art, claim N=3 is optimal, claim ZVS from phase shifting alone, claim shared core gives equal current sharing, claim internal three-phase states solve single-phase 2omega energy, assign Candidate #10, or execute PSIM/hardware.

## 13. Next gate

The broad synthesis set now exists. Next: state-equation closure before pruning.

For coverage rather than ranking, start with `C01`, `C04`, `C07`, `C11`, and `C16`; together they span polyphase role rotation, structural/leakage coupling, multimode magnetics, vector-secondary states, and staggered gain states.

For each:

1. write exact legal states/transitions;
2. derive flux/volt-second equations;
3. derive current-continuity paths;
4. identify whether multifunctionality is one inseparable physical state or colocated subcircuits;
5. only then begin equivalent-reduction, loss and prior-art falsification.

Formal status remains:

```text
Candidate #10: HOLD / NOT_ASSIGNED
Novelty: NOT_ESTABLISHED
PSIM: NOT_EXECUTED
Hardware: NOT_EXECUTED
```

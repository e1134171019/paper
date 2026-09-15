# 2026-09-15 — Magnetic / Polyphase Synthesis Reset v1

Status: `WORKING_BRANCH / MECHANISM_SYNTHESIS_RESET`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose of this update

This update corrects the synthesis method used for the low-voltage high-current 12 Vdc -> 220 Vac research branch.

The previous working process pruned too early: when a mechanism had prior art, added loss, or an incomplete degree of freedom, it was often rejected before the complete magnetic design space had been synthesized. That process is too restrictive for topology discovery.

The revised order is:

```text
SYNTHESIS first
  -> enumerate magnetic/electrical degrees of freedom
  -> generate state combinations
  -> identify shared-hardware / shared-state functions

FALSIFICATION second
  -> conservation / flux / current constraints
  -> equivalent-reduction kill test
  -> total-loss comparison
  -> closest-prior-art closure
  -> PSIM only after mechanism survives
  -> hardware only after simulation and measurement plan closure
```

This file does not supersede the formal A0 measurement mainline. It opens a controlled synthesis branch only.

## 2. Key correction: self-oscillation is not predefined as a two-MOS Royer

The synthesis space must not begin with:

```text
self-oscillation = two MOS + center-tapped primary
```

That is only one implementation family.

The first-principles starting point is the magnetic power-processing structure itself:

```text
magnetic paths / core modes
+ winding turns / polarity / taps / series-parallel connection
+ port roles
+ leakage / magnetizing energy
+ phase coordination
+ semiconductor connection states
```

Only after the required state transitions are known should the minimum switch realization be chosen.

Royer remains a valid timing/commutation host and historical implementation anchor, but it is no longer allowed to constrain the upstream synthesis space.

## 3. Transformer / magnetic-structure functional map

At the current abstraction level, a transformer or integrated magnetic structure can participate in at least the following functions:

1. Galvanic isolation.
2. Voltage/current transformation through turns ratio.
3. Reflected-impedance transformation.
4. Polarity / phase mapping.
5. Multiport energy routing.
6. Current splitting / recombination and flux cancellation.
7. Flux / magnetic-state sensing through auxiliary windings.
8. Short-time energy storage / commutation / ZVS support through `Lm`, `Llk` or intentional resonant paths.
9. Structural reconfiguration through taps, series/parallel connection, winding enable/disable, polarity selection, or equivalent turns-ratio change.

These are functions, not nine independent physical degrees of freedom.

## 4. Underlying physical degrees of freedom

The current synthesis basis is:

- `M` — magnetic state / magnetic mode: main flux, differential/balancing mode, leakage/commutation-related state, and where physically meaningful common/zero-sequence modes.
- `N/qw` — turns and winding-connection state: tap, series/parallel, polarity, winding enable/disable, effective turns ratio.
- `L` — `Lm`, `Llk`, intentionally integrated resonant/commutation inductance and their dependence on geometry or connection state.
- `P` — port role: transfer, sensing, idle, reset, commutation actuator, temporary energy port.
- `phi` — phase / scheduling state, including interleaving and polyphase coordination.
- `qs` — semiconductor connection state implementing the required electrical graph.

A useful general state description is therefore:

```text
q = { magnetic mode, winding connection, port role, phase schedule, semiconductor state }
```

The objective is not to maximize the number of functions. The objective is to find states where the same load-bearing hardware performs more than one required function without creating a larger loss or complexity penalty than the function it removes.

## 5. Reconfiguration and multiport result

A winding-connection state `q` can change more than voltage gain. In general:

```text
q -> Neff(q)
q -> G(q)
q -> Zref(q)
```

For an ideal transformer section:

```text
G(q) = Ns(q) / Np(q)
Zref(q) = [Np(q) / Ns(q)]^2 ZL
```

Therefore a true load-bearing winding reconfiguration simultaneously changes gain and reflected load. However, a tap change that only rescales a sensing voltage is not a new power state.

A multiwinding structure must likewise not be predefined as `primary + feedback + output`. Before VA assignment, each winding is treated as a magnetic port. A low-VA winding may later be classified as sensing-only, transient actuator, reset/commutation port, or main-power port depending on the derived state equations.

## 6. Commutation-energy coupling

The soft-switching condition remains an energy condition, not a claim of zero total loss:

```text
Ecomm >= Eoss,total
```

A first-order form is:

```text
0.5 * Lcomm * Icomm^2 >= Eoss,total
```

The important synthesis question is whether the same structural state that changes gain or port role also changes `Lcomm`, `Icomm`, or the available commutation trajectory.

A particularly important falsifier was retained:

- If secondary/load decoupling becomes perfect during a zero/commutation state, reflected load current may no longer control `Ecomm`.
- Therefore `gain-state -> ZVS-energy` is not automatically coupled.
- A stronger candidate exists when the same winding/core reconfiguration also changes the intentional leakage/commutation path `Lcomm(q)`.

Hence the current high-value mechanism is not merely `tap + auxiliary winding + ZVS`. It is a state in which structural reconfiguration, port-role reassignment and the magnetic commutation path are physically coupled.

## 7. New polyphase degree of freedom

A new synthesis degree of freedom is formally added:

```text
E = phase / polyphase magnetic-state coordination
```

The first concrete example is three branches at:

```text
phiA = 0 deg
phiB = 120 deg
phiC = 240 deg
```

This does not mean the required load becomes three-phase. The final research boundary remains single-phase 220 Vac. The internal polyphase state is an implementation/synthesis degree of freedom.

Potential functions opened by the `0/120/240 deg` state include:

- current sharing across power branches,
- source-ripple cancellation,
- staggered switching and commutation,
- staggered thermal loading,
- flux cancellation / shared return-path opportunities in multi-leg magnetic structures,
- rotation of the temporary commutation/support role between otherwise symmetric power branches,
- separation of transfer and commutation windows in time without a permanently dedicated auxiliary power branch.

Three-way current splitting alone does not guarantee lower total `I^2R`; with conserved copper resistance the idealized total conduction loss can remain unchanged. The value must come from reduced ripple, improved device/winding utilization, termination loss, magnetic geometry, commutation scheduling, or another measurable system benefit.

## 8. Polyphase role-rotation hypothesis

The first high-value state cycle is:

```text
(T, T, K)
 -> (T, K, T)
 -> (K, T, T)
 -> repeat
```

where:

- `T` = main power transfer,
- `K` = commutation / flux-reset / ZVS-support interval.

The hypothesis is that three symmetric power branches can rotate roles rather than assigning one permanent auxiliary branch.

This opens the possibility that at any instant two branches continue power transfer while the third branch obtains a controlled commutation window, followed by cyclic role exchange.

This is a mechanism hypothesis only. It is not yet proven distinct from ordinary three-phase/interleaved conversion.

## 9. Magnetic-mode condition for true polyphase operation

Three phase commands cannot be imposed as three independent fluxes on a single ideal one-mode magnetic path.

For one common flux mode:

```text
v1/N1 = v2/N2 = v3/N3 = dPhi/dt
```

Therefore genuine independent `0/120/240 deg` magnetic states require enough independent magnetic degrees of freedom, e.g. multiple limbs / branch fluxes / a higher-rank magnetic inductance matrix.

A polyphase branch system may still share a physical core, but the modal rank and coupling matrix must support the claimed independent states. Shared core does not imply independent phase authority, and shared flux does not imply current sharing.

## 10. Single-phase 2omega energy is not solved by internal three-phase states

Internal polyphase power processing may reduce switching ripple and improve transfer continuity, but it does not eliminate the single-phase output power pulsation:

```text
po(t) = P [1 - cos(2*w*t)]
```

The 2omega energy-routing problem remains a separate system requirement until a specific storage/routing state is derived and loss-accounted.

Therefore no claim is made that three-phase internal coordination closes X2.

## 11. Revised synthesis tree

The previous `A+B+C` shorthand is expanded:

- `A` = winding / structural reconfiguration.
- `B` = state-dependent multiport role.
- `C` = intentional commutation magnetic energy.
- `E` = phase / polyphase magnetic state and role scheduling.

The next synthesis stage should generate combinations before pruning, including at minimum:

```text
A+B
A+C
A+E
B+C
B+E
C+E
A+B+C
A+B+E
A+C+E
B+C+E
A+B+C+E
```

Each combination must be judged on whether the functions are truly carried by the same physical state or merely colocated as separate subcircuits.

## 12. Research-method correction

From this point forward, mechanism discovery and mechanism falsification are separate phases.

### Synthesis phase

Do not reject a mechanism merely because:

- similar prior art exists,
- one operating point looks lossy,
- the first implementation appears switch-heavy,
- the current drawing cannot yet realize the full function.

Instead first ask:

```text
What new controllable physical state does this mechanism add?
What other required functions can share that state?
What state combinations become possible when it is crossed with other magnetic DOFs?
```

### Falsification phase

Only after a concrete state graph exists, apply:

```text
flux / volt-second balance
current continuity
energy conservation
magnetic saturation limits
commutation-energy sufficiency
RMS / I^2R / switching / magnetic loss ledger
equivalent-circuit reduction
closest-prior-art intersection
```

This correction is intended to prevent premature pruning from collapsing the exploration back into only one historical topology family.

## 13. Current formal status

No Candidate #10 is assigned by this update.

```text
Candidate #10: HOLD / NOT_ASSIGNED
Novelty: NOT_ESTABLISHED
PSIM: NOT_EXECUTED
Hardware: NOT_EXECUTED
```

The formal A0 physical-measurement mainline and File64 M1-M4 contract remain unchanged.

This branch is a mechanism-synthesis expansion only. Any future topology must still pass the existing loss, evidence, prior-art and validation gates before it can replace the formal mainline.

## 14. Immediate next task

Build a complete `physical DOF x function` matrix and deliberately generate a broad candidate set before applying any stop gate.

For each candidate, record:

```text
state variables
magnetic mode rank required
winding/connection state
phase relationship
port role in each state
power path
commutation path
which functions genuinely share hardware
which functions are still separate
```

Only after that synthesis table exists should candidates be reduced by first-principles math and prior art.

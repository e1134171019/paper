# 2026-09-16 — Proposed Method: Bounded Self-Oscillating Multiwinding Front-End v1

Status: `WORKING_BRANCH / METHOD_PROPOSAL / PRE-MATH / NO_TOPOLOGY_CLAIM`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Research boundary

Anchor boundary:

```text
Vin = 12 Vdc
Pout = 2 kW
Vout = 220 Vac
single phase
HF isolated conversion region under study
```

The immediate research target is the first high-frequency / magnetic power-conversion region. The downstream 2ω energy buffer and final 220-Vac synthesis remain explicit system obligations and are not assumed to be solved by the HFT core.

---

## 2. Method statement

The proposed method is **not** a forced combination of SST + LLC + MAB + Y-source + Royer.

The method is:

> Use multiple load-bearing windings/ports to distribute the low-voltage high-current power, deliberately design the magnetic leakage/differential energy needed for natural commutation, and preserve self-oscillating switching as the inner commutation mechanism while an external controller only bounds frequency/phase/current sharing/startup. Structural winding-state control may later be added if it improves effective turns ratio, reflected impedance or commutation inductance without imposing prohibitive raw-12-V selector loss.

Compact form:

```text
SST / multiport architecture ideas
        -> define what may be shared / series / parallel / partial-power
Topology-Delta knowledge
        -> define useful local circuit modifications
Matrix / integrated magnetics
        -> realize current distribution and designed leakage physically
Self-oscillation
        -> generate natural commutation timing from magnetic/resonant state
External coordination
        -> bound drift, phase, sharing, startup and abnormal recovery
```

Working name only:

```text
Bounded Self-Oscillating Multiwinding Front-End
```

This is a working research label, not an established topology name and not a novelty claim.

---

## 3. What is actually being proposed

### 3.1 W1 / W2 — peer load-bearing power windings

W1 and W2 begin as symmetric or near-symmetric main power paths.

Desired first-order relation:

```text
Iin = iW1 + iW2 + ...
```

But simple arithmetic current splitting is not accepted as a benefit. Any claimed improvement must survive approximately equal-resource comparison in copper, silicon and magnetic material.

The SST / MAB contribution at this layer is conceptual:

```text
W1 and W2 are peer power ports,
not predefined as main winding + feedback winding.
```

### 3.2 W3 — commutation / magnetic-feedback / correction candidate

W3 is **not** assumed to be a full-power third port.

Possible roles to test:

```text
1. magnetic feedback / self-oscillation sensing
2. leakage / differential-energy routing
3. flux reset / balancing
4. low-VA correction port, only if |PW3| / Pout << 1 is proven
```

The W3 role must be determined by the state graph and VA calculation, not by name.

### 3.3 Designed commutation inductance

The method does not assume that all leakage should be minimized or all leakage should be integrated.

Three implementation branches remain legal:

```text
A. integrated:
   Lcomm mainly synthesized from transformer leakage / differential mode

B. externalized:
   W1/W2 remain tightly coupled for bulk transfer;
   a separate Lext supplies most commutation energy

C. hybrid:
   Lcomm = Llk,designed + Lext
```

This directly imports the literature conflict:

```text
integrated-magnetics lineages -> leakage can be a useful resonant / commutation element
multiport-decoupling lineages -> some inductance should be externalized to avoid cross-coupling
```

The research question is therefore not “is leakage good?” but “how much inductive function should be integrated into this specific low-voltage multiwinding front end?”

---

## 4. Inner and outer control hierarchy

### Inner layer — natural commutation

The inner layer should allow magnetic/resonant state to determine the next switching transition.

Conceptually:

```text
current / flux / leakage energy
        -> charges / discharges Coss or Cres
        -> switch-node voltage moves toward next legal state
        -> natural commutation point appears
```

This preserves the original self-oscillation objective.

### Outer layer — bounded external coordination

External control is not intended to generate every switching edge from scratch.

Its allowed functions are:

```text
frequency bounding
phase correction
W1/W2 current-balance correction
startup forcing / kick
abnormal-state recovery
protection / shutdown
optional slow operating-state selection
```

Working principle:

```text
natural commutation + bounded external correction
```

This is distinct from a fully externally clocked converter.

---

## 5. Minimum state skeleton

This file does not yet define exact MOSFET connections. It defines the minimum physical states that a later circuit must realize.

### qT — bulk-transfer state

```text
W1/W2 = load-bearing transfer
W3 = sensing / weak commutation role or inactive
secondary = receives HF power
```

Required result:

```text
Pbulk flows through W1/W2
```

### qK — commutation state

A portion of magnetic/leakage/differential energy is deliberately redirected to a transition path.

Required function:

```text
Ecomm = 0.5 * Lcomm * Icomm^2
```

must be available to support the next switch-node transition.

Potential paths to be explored later:

```text
Llk/differential mode -> Coss
Llk/differential mode -> Cres -> Coss
Llk/differential mode -> W3 -> clamp/resonant node -> next transition
```

### qR — reset / recovery state

Any energy placed into W3, Cres, clamp or differential magnetic mode must have a defined return/release path.

No stored-energy state is allowed without reset closure.

### qF — safe startup / freewheel / abnormal state

If any current-fed behavior is adopted, the input-current path must never be opened illegally.

qF must also support controlled startup because a self-oscillator cannot be assumed to start from a perfectly symmetric zero-energy condition.

### qG — optional structural-gain state

qG is **not required for v1 proof**.

If later retained, it may alter:

```text
Neff(q)
Zref(q)
Lcomm(q)
```

without adding prohibitive selector conduction loss in the raw 12-V / hundred-ampere path.

---

## 6. SST contribution retained explicitly

The SST literature remains an architecture donor, not a converter to copy wholesale.

The method retains five SST-derived rules:

### SST-R1 — peer power ports

W1/W2 may be treated as equal power ports rather than hierarchical main/feedback windings.

### SST-R2 — low-voltage parallel / higher-voltage series or stacked processing is legal as an architectural option

This may later support:

```text
low-side current distribution
+
high-side voltage addition
```

but only after current sharing and series-voltage balance are proven.

### SST-R3 — not every port needs a full independent bridge

Reduced-switch MAB/QAB work motivates checking whether W1/W2/W3 can share semiconductor states instead of linearly adding complete power cells.

### SST-R4 — shared magnetics can over-couple ports

The design must be allowed to externalize selected inductance or separate magnetic modes if full integration creates unacceptable circulation or power-flow coupling.

### SST-R5 — a low-VA correction port is possible only after processed-power fraction is proven

If W3 becomes a correction port, define:

```text
alpha = |PW3| / Pout
```

Only if `alpha << 1` may W3 be described as partial-power.

---

## 7. What this method may provide beyond original self-oscillation + external correction

The complete method may produce the following functions. Only the first three are mandatory for the first proof.

### F1 — natural HF commutation

Self-generated HF switching remains the core inner mechanism.

### F2 — bounded external correction

Frequency, phase and current-sharing drift are constrained without completely replacing natural commutation.

### F3 — real load-bearing low-side power distribution

W1/W2 both process meaningful power and distribute the 12-V-side current path.

### F4 — leakage energy becomes useful commutation energy

Instead of:

```text
Llk energy -> spike / dissipative clamp
```

study:

```text
Llk / differential energy -> next natural commutation
```

### F5 — designed division between bulk-transfer and commutation magnetic modes

The magnetic assembly may use strong bulk coupling and a deliberately weaker commutation/differential path.

### F6 — optional structural gain control

A later q-state may change `Neff` rather than relying entirely on extreme fixed turns ratio or wide frequency control.

### F7 — optional reflected-impedance shaping

If q changes `Neff`, the source-side apparent impedance may also change:

```text
Zref(q) = [Np(q)/Ns(q)]^2 * Zload
```

This may change low-side current stress as well as voltage gain.

### F8 — optional state-dependent commutation inductance

A later enhanced version may achieve:

```text
q -> {Neff(q), Zref(q), Lcomm(q)}
```

and, because self-oscillation is retained, potentially also:

```text
q -> {Neff, Zref, Lcomm, fosc, Ecomm}
```

This is an advanced research extension, not a requirement for the first circuit.

### F9 — optional low-VA W3 correction function

If demonstrated by VA/power analysis, W3 may become a partial-power correction/commutation port rather than only a sensing winding.

### F10 — possible downstream stage reduction is an architecture question only

Matrix-type SST/direct-HF-link ideas remain open for later X1/X3 overlap analysis, but are explicitly excluded from the first front-end proof. Single-phase 2ω energy must remain accounted for elsewhere.

---

## 8. First research hypotheses

### H1 — commutation-energy hypothesis

There exists an operating region where designed magnetic/leakage energy is sufficient for natural commutation:

```text
0.5 * Lcomm * Icomm^2 >= Etransition_required
```

while added reactive/RMS loss remains acceptable.

### H2 — bounded-self-oscillation hypothesis

An external coordination loop can bound frequency / phase / sharing while preserving an inner natural commutation mechanism rather than degenerating into ordinary forced PWM.

### H3 — equal-resource distribution hypothesis

A physically integrated W1/W2 structure may reduce termination / winding / local semiconductor burden under matched total resource conditions; simple `I/2` arithmetic alone is not accepted.

### H4 — magnetic-mode allocation hypothesis

A design window may exist where:

```text
bulk-transfer coupling is high enough for efficient 2-kW transfer
while
commutation/differential inductance is high enough for switching transition energy
```

without excessive cross-coupling or circulation.

### H5 — optional coupled-state hypothesis

A later winding state may jointly alter `Neff`, `Zref` and `Lcomm` without placing high-loss selector hardware in the raw 12-V path.

---

## 9. Falsifiers

The method should be rejected or reduced in scope if any of the following is found:

1. self-oscillation only works by letting frequency or flux drift outside controllable bounds;
2. W1/W2 current splitting gives no benefit after equal-copper / equal-silicon comparison and adds more loss than it removes;
3. the magnetic energy needed for natural commutation causes unacceptable circulating current, core loss or capacitor RMS;
4. external control must dictate essentially every edge, meaning self-oscillation contributes no meaningful commutation function;
5. W3 processes near-full power despite being justified as a correction/commutation port;
6. state-dependent gain requires selector switches whose raw-12-V conduction loss dominates the benefit;
7. cross-coupling between winding ports prevents stable sharing or creates destructive transition states.

---

## 10. Required mathematical order before PSIM

The next execution should now be mathematics for this **method**, not a random topology simulation.

### Math-1 — minimum self-oscillation / commutation energy model

Define symbolic:

```text
Lcomm
Ceq = relevant Coss + Cres contribution
Icomm
Vsw
```

Check transition-energy sufficiency and natural resonant interval.

### Math-2 — magnetic volt-second / flux-balance model

For W1/W2/W3:

```text
vk = sk * Nk * dPhi/dt
```

and verify periodic flux balance. If more than one magnetic mode is needed, use common/differential coordinates rather than one-flux oversimplification.

### Math-3 — natural oscillation sensitivity

Derive at minimum the dependence:

```text
fosc = f(Lcomm, Ceq, Zref, operating current, magnetic state)
```

The simple resonance expression may only be used as a local approximation:

```text
fnat ~= 1 / (2*pi*sqrt(Leq*Ceq))
```

### Math-4 — W1/W2 equal-resource current-distribution check

Compare baseline versus split path under approximately equal total copper and semiconductor resource.

### Math-5 — external-correction authority

Define what variable the external loop is allowed to perturb:

```text
phase reference
frequency window
turn-on inhibit/advance
startup kick
current-balance trim
```

and prove that the natural oscillator still determines the base transition event.

### Math-6 — only after Math-1...5: optional q-state extension

Test whether adding one structural state can produce a useful coupled change in:

```text
{Neff, Zref, Lcomm}
```

without making the first proof dependent on topology morphing.

---

## 11. Immediate next execution

Start with **Math-1** only.

Do not yet draw a production schematic and do not yet enter PSIM.

The first mathematical question is:

> What minimum `Lcomm-Icomm-Ceq` relationship is required for the magnetic/leakage energy left by one transfer interval to create the next natural switch-node transition under the 12-V / 2-kW boundary?

This gives the first hard test of whether “self-oscillation + designed leakage” is a real power-conversion method or only a descriptive idea.

# 2026-09-16 — Math-2: Multiwinding Flux / Modal Balance Model v1

Status: `WORKING_BRANCH / METHOD_MATH / MATH02_SYMBOLIC_CLOSURE / PRE_PSIM`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

Math-1 established the minimum commutation-energy condition:

```text
0.5 * Lcomm * Icomm^2 >= Etransition
```

Math-2 asks the next physical question:

> Can W1/W2 carry bulk power while a distinct magnetic/leakage mode supplies commutation energy, without flux walk, saturation, or an internally contradictory W3 role?

This file does **not** yet select a production schematic. It derives the minimum magnetic conditions that any later W1/W2/W3 realization must satisfy.

Research boundary remains:

```text
Vin = 12 Vdc
Pout = 2 kW
Vout = 220 Vac
single phase
HF isolated front-end under study
```

---

## 2. First-pass assumptions

For symbolic closure only:

1. W1 and W2 are approximately symmetric peer power windings.
2. Local magnetic behavior is first approximated as linear around an operating point.
3. Core saturation, hysteresis and frequency-dependent copper/core loss are deferred to the later loss model; their allowable limits are retained as constraints.
4. Winding signs are referenced to magnetic dot polarity before modal transformation.
5. W3 is not pre-assigned as sensing-only, commutation-only or full-power.
6. Additional 3-D magnetic modes may exist in a real core. The two-mode derivation below is the minimum model, not a claim that all geometries reduce exactly to two modes.

Define signed winding quantities:

```text
itilde_k = s_k * i_k
vtilde_k = s_k * v_k
s_k in {+1,-1}
```

so that the selected signs correspond to the same magnetic reference direction.

---

## 3. W1/W2 symmetric inductance model

For W1/W2 with equal self inductance `L` and mutual inductance `M`:

```text
[lambda1]   [ L  M ][i1]
[lambda2] = [ M  L ][i2]
```

with:

```text
M = k * L
0 <= k < 1    [for the simple positive-coupling case]
```

Use the orthonormal modal transform:

```text
ic = (itilde1 + itilde2) / sqrt(2)
id = (itilde1 - itilde2) / sqrt(2)

vc = (vtilde1 + vtilde2) / sqrt(2)
vd = (vtilde1 - vtilde2) / sqrt(2)
```

This transformation preserves instantaneous power:

```text
vtilde1*itilde1 + vtilde2*itilde2 = vc*ic + vd*id
```

The inductance matrix diagonalizes:

```text
vc = Lc * dic/dt
vd = Ld * did/dt
```

where:

```text
Lc = L + M = L(1+k)
Ld = L - M = L(1-k)
```

Interpretation:

- `Lc` = strongly coupled / bulk-transfer magnetic mode.
- `Ld` = weakly coupled / differential-leakage mode.

For high coupling `k -> 1`:

```text
Lc -> approximately 2L
Ld -> small positive value
```

This is the first mathematical basis for the proposed method:

```text
bulk-transfer energy can live mainly in a strongly coupled mode,
while commutation energy can be assigned to a smaller differential/leakage mode.
```

Important convention warning:

`Ld = L-M` is the modal inductance under the orthonormal coordinates above. A leakage inductance measured at physical terminals under a different series/short-circuit connection can differ by a factor set by the connection and coordinate scaling. Do not substitute a datasheet/measurement leakage value into `Ld` without mapping the terminal state.

---

## 4. Modal magnetic energy

Under the two-mode model:

```text
Wmag = 0.5*Lc*ic^2 + 0.5*Ld*id^2
```

The desired conceptual allocation is:

```text
0.5*Lc*ic^2 -> mainly bulk transfer / common linked flux
0.5*Ld*id^2 -> mainly commutation / balancing / leakage energy
```

The Math-1 commutation quantity must therefore be mapped from the physical switching state into the differential mode:

```text
0.5 * Lcomm * Icomm^2
= 0.5 * Ld * id,qK^2
  + any external-inductor contribution
  + any other deliberately retained resonant magnetic energy
```

Hence `Lcomm` is **not automatically equal to transformer leakage inductance**. It is a state-dependent equivalent seen by the actual qK commutation current.

If a hybrid implementation is used:

```text
Ecomm = 0.5*Ld*id,qK^2 + 0.5*Lext*Iext,qK^2 + Ecoupled,other
```

This preserves the earlier integration fraction concept:

```text
rho_L = Lintegrated / Lcomm_equivalent
```

but now `Lintegrated` must be defined from the actual modal/terminal mapping.

---

## 5. Minimum self-oscillation state refinement

The earlier generic `qT/qK/qR/qF` skeleton is refined here.

A two-power-winding self-oscillating cycle needs at least:

```text
qT1  -> qK12 -> qT2 -> qK21 -> repeat
```

with qR/recovery actions either explicit or embedded in qK intervals.

### qT1 — W1-dominant transfer

```text
W1 carries one bulk-transfer interval
W2 is non-dominant / recovering / blocked according to final circuit
secondary receives useful power
```

### qK12 — W1 -> W2 commutation

```text
differential/leakage magnetic energy
-> Coss / Cres / W3 commutation path
-> next legal switch-node state
```

### qT2 — W2-dominant transfer

Mirror of qT1 with magnetic polarity reversed as required by the transformer dot convention.

### qK21 — W2 -> W1 commutation

Mirror of qK12.

### qR — reset / energy return

Any energy parked in W3, Cres, clamp nodes or differential flux must return to a defined state before periodic steady state is claimed.

### qF — startup / freewheel / abnormal state

Still required if current-fed behavior or startup asymmetry exists.

This refinement matters because flux balance must be checked over the **entire** sequence, not only over qT1 and qT2.

---

## 6. Bulk-flux volt-second balance

For any magnetic mode `m`:

```text
vm = Nm_eff * dPhi_m/dt
```

Periodic steady state requires:

```text
DeltaPhi_m(Ts) = integral_0^Ts [vm(t)/Nm_eff] dt = 0
```

For the bulk/common mode:

```text
integral_0^Ts vc(t) dt = 0
```

under a fixed effective common-mode turns basis.

A push-pull-like first-order approximation gives:

```text
V1*t1/N1 - V2*t2/N2 + DeltaPhi_KR = 0
```

where `DeltaPhi_KR` is the net common-mode flux contribution from qK/qR intervals.

For symmetric W1/W2 and negligible qK/qR common-mode volt-seconds:

```text
V1*t1 ~= V2*t2
```

but this is only an approximation. A self-oscillator is not allowed to assume perfect 50/50 timing a priori.

Define per-cycle bulk flux-walk error:

```text
DeltaPhi_walk
= integral_0^Ts [vc/Nc_eff] dt
```

or in flux density:

```text
DeltaB_walk = DeltaPhi_walk / Ae
```

If this is nonzero and not corrected:

```text
B[n] = B[0] + n*DeltaB_walk
```

so even a small systematic timing or voltage asymmetry eventually drives the core toward saturation.

Therefore the external correction layer has a physically necessary flux-balance role:

```text
average volt-seconds must be trimmed toward zero
```

without necessarily dictating every individual switching edge.

---

## 7. Flux-excursion bound and why a lower frequency limit is mandatory

For a simple symmetric square excitation `+Vp/-Vp` with approximately equal half-cycles and negligible qK/qR volt-seconds:

```text
Bpk ~= Vp / (4 * Np * Ae * fosc)
```

Therefore:

```text
Np*Ae >= Vp / (4 * fmin * Ballow)
```

or equivalently:

```text
fosc >= Vp / (4 * Np * Ae * Ballow)
```

where `Ballow` includes saturation and core-loss margin.

This gives a major method-level result:

```text
external frequency bounding is not only a control convenience;
it is part of magnetic saturation protection.
```

For the real waveform the correct calculation is still:

```text
B(t) = B(0) + integral[vcore(t) dt] / (Np*Ae)
```

including qT, qK and qR intervals.

---

## 8. Differential-mode reset condition

The differential/leakage state must also be periodic.

If it is represented by `Ld`:

```text
id(Ts) = id(0)
```

and therefore:

```text
integral_0^Ts vd(t) dt = 0
```

for constant `Ld` in the first-order model.

This is the magnetic version of the qR requirement.

A commutation scheme that uses `Ld` to charge/discharge Coss but leaves a net differential current or flux offset every cycle is not a valid steady-state solution.

Hence both must close:

```text
bulk/common mode:        DeltaPhi_c = 0
differential/commutation: Deltaid   = 0   [or equivalent DeltaPhi_d = 0]
```

---

## 9. W3 coupling model — key result

Add W3 to the linear inductance model:

```text
L3-port =
[ L   M   m1 ]
[ M   L   m2 ]
[ m1  m2  L3 ]
```

Transform only W1/W2 into common/differential coordinates.

The W3 couplings become:

```text
mc = (m1 + m2) / sqrt(2)
md = (m1 - m2) / sqrt(2)
```

so the modal inductance matrix is:

```text
[ Lc   0   mc ]
[  0  Ld   md ]
[ mc  md   L3 ]
```

For high-impedance W3 sensing (`i3 ~= 0`):

```text
v3 ~= mc * dic/dt + md * did/dt
```

This immediately gives three physically different W3 realizations.

### Case W3-C — same-sense coupling to W1/W2

If:

```text
m1 = m2 = m
```

then:

```text
mc = sqrt(2)*m
md = 0
```

W3 senses/couples strongly to the bulk/common magnetic mode and is largely blind to the ideal differential mode.

Usefulness:

```text
magnetic feedback / core-flux sensing
```

Limitation:

```text
poor direct access to differential leakage energy
```

### Case W3-D — opposite-sense coupling

If:

```text
m1 = +m
m2 = -m
```

then:

```text
mc = 0
md = sqrt(2)*m
```

W3 couples to the differential/commutation mode while rejecting the ideal common mode.

Usefulness:

```text
commutation-energy sensing/routing
```

Limitation:

```text
it no longer behaves like a conventional common-flux feedback winding
```

### Case W3-M — mixed/asymmetric coupling

If:

```text
m1 != +m2
and
m1 != -m2
```

then W3 couples to both modes.

This appears attractive but creates a new issue:

```text
one physical winding now mixes bulk-flux feedback and differential commutation energy
```

so imbalance, RMS current and unwanted cross-coupling must be audited.

---

## 10. Fundamental reduced-model constraint on “W3 does everything”

The modal inductance matrix must be positive definite for positive magnetic energy.

For:

```text
[ Lc   0   mc ]
[  0  Ld   md ]
[ mc  md   L3 ]
```

one necessary/sufficient reduced-model condition is:

```text
Lc > 0
Ld > 0
L3 > 0
L3 - mc^2/Lc - md^2/Ld > 0
```

Define modal coupling coefficients:

```text
kc = mc / sqrt(Lc*L3)
kd = md / sqrt(Ld*L3)
```

then:

```text
kc^2 + kd^2 < 1
```

This is a key Math-2 result.

Within this reduced linear three-winding model, one W3 winding cannot be arbitrarily close to perfect coupling with **both** the bulk/common mode and the orthogonal differential/commutation mode at the same time.

Illustrative sensitivity only:

```text
if kc = 0.90 -> |kd| < 0.436
if kc = 0.95 -> |kd| < 0.312
```

This does not prove that every real 3-D magnetic structure obeys exactly this two-mode decomposition; a more complex core can add additional modes. But it is a strong warning against casually assigning W3 all roles simultaneously.

### Immediate design consequence

Three implementation branches should remain open:

```text
M2-A:
W3 = common-flux feedback only
Lcomm = W1/W2 designed leakage and/or Lext

M2-B:
W3c = common-flux sensing winding
W3d = separate differential/commutation winding or magnetic leg

M2-C:
one mixed W3 couples to both modes
only retain if RMS / cross-coupling / flux-balance math later proves acceptable
```

No branch is selected yet.

---

## 11. Current sharing and differential mode are not the same objective

Because:

```text
id = (itilde1 - itilde2) / sqrt(2)
```

any W1/W2 instantaneous current difference creates differential-mode energy:

```text
Wd = 0.5 * Ld * id^2
```

But the proposed method may deliberately need nonzero `id` during qK to perform commutation.

Therefore the outer current-sharing loop must **not** be defined as:

```text
iW1(t) = iW2(t) at every instant
```

That could destroy the commutation mode we are trying to use.

The more appropriate target is cycle/transfer balance, for example:

```text
integral_qT1 v1*i1 dt ~= integral_qT2 v2*i2 dt
```

or matched average/RMS branch loading over equivalent transfer windows.

Hence:

```text
slow / cycle-averaged sharing correction
can coexist with
fast intentional differential commutation current
```

This is another reason the “bounded external correction” layer should be slower/higher-level than the inner natural commutation event.

---

## 12. Connection to SST / multiport architecture

Math-2 does not remove the SST layer; it makes it physical.

SST/MAB architecture contributed:

```text
W1/W2 may be peer load-bearing power ports
shared magnetics can reduce duplicated hardware
but shared ports can over-couple
```

Math-2 translates that into magnetic coordinates:

```text
strong common-mode coupling -> efficient shared bulk transfer
controlled differential mode -> commutation / balancing degree of freedom
excess differential/common cross-coupling -> unwanted circulation / instability
```

Thus the SST-derived architectural question:

```text
what should be shared and what should be decoupled?
```

becomes the magnetic design question:

```text
choose Lc, Ld, mc, md and any Lext so bulk power and commutation remain compatible.
```

---

## 13. Math-2 pass/fail gates

A later concrete W1/W2/W3 circuit is not allowed into PSIM unless these are explicit.

### M2-G1 — common-mode periodicity

```text
integral_0^Ts vc(t) dt = 0
```

or the exact generalized modal flux equation.

### M2-G2 — differential-mode periodicity

```text
id(Ts) = id(0)
```

or equivalent differential-flux reset.

### M2-G3 — flux-density limit

```text
|Bc(t)| <= Ballow
```

including the minimum possible self-oscillation frequency and qK/qR volt-seconds.

### M2-G4 — commutation-energy mapping

The circuit must identify which physical/modal inductance supplies Math-1 `Lcomm`:

```text
Ld / external L / additional mode / hybrid
```

and map physical `Icomm` to modal current.

### M2-G5 — W3 role closure

State explicitly whether W3 couples mainly to:

```text
common bulk mode
or
differential commutation mode
or
both
```

and calculate the resulting VA/RMS implications later.

### M2-G6 — current-sharing definition

Sharing must be defined over a physically meaningful averaging window, not as an instantaneous equality that suppresses required commutation current.

### M2-G7 — outer control does not replace the inner oscillator

External correction may remove average flux walk and bound frequency, but the qK transition must still be generated by the magnetic/resonant state if the self-oscillation claim is retained.

---

## 14. Main result of Math-2

The proposed method is now more specific than “multiple windings + self-oscillation.”

The minimum physically meaningful magnetic target is:

```text
strongly coupled bulk-transfer mode
+
controlled differential/leakage commutation mode
+
periodic reset of both modes
+
W3 coupling chosen deliberately rather than assigned several incompatible roles by name
```

Compactly:

```text
Bulk:
Lc, Phi_c -> 2-kW transfer

Commutation:
Ld / Lext, id -> qK natural transition

Feedback/correction:
W3 coupling {mc, md} -> selected sensing/routing role
```

The strongest new finding is that a single W3 doing both near-perfect common-flux feedback and near-perfect differential-energy routing is **not free**. In the reduced model:

```text
kc^2 + kd^2 < 1
```

so the W3 role itself becomes a magnetic-allocation problem.

---

## 15. Immediate next execution — Math-3

Math-3 should now derive natural oscillation sensitivity using the qT1/qK12/qT2/qK21 sequence.

Required variables:

```text
Lcomm(q)
Ceq(q)
Zref(q)
Icomm(q)
Phi_c / Bc operating point
W3 coupling case
```

The next question is:

> How does the natural switching period move with load/reflected impedance, commutation inductance, switch capacitance and magnetic operating state, and how much frequency/phase authority must the external correction layer have before it stops being meaningfully self-oscillating?

Only after Math-3 should the research decide which W3 realization (M2-A / M2-B / M2-C) deserves an explicit circuit candidate.
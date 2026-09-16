# 2026-09-16 — Math-3: Self-Oscillation Frequency / Sensitivity Model v1

Status: `WORKING_BRANCH / METHOD_MATH / MATH03_SYMBOLIC_CLOSURE / PRE_PSIM`  
Method: `Bounded Self-Oscillating Multiwinding Front-End`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

---

## 1. Purpose

Math-1 established a minimum natural-commutation condition:

```text
0.5 * Lcomm * Icomm^2 >= Etransition
```

Math-2 established that the W1/W2 magnetic system must be treated at least as common/bulk and differential/commutation modes, and that W3 coupling can target one or both modes.

Math-3 asks:

> How does the natural oscillation period move when `Lcomm`, `Ceq`, reflected load, commutation current, common-mode flux excursion, or W3 coupling changes; and how much external correction can be allowed before the method degenerates into ordinary forced PWM?

This file is intentionally topology-agnostic. No production MOSFET graph is selected yet.

Research boundary remains:

```text
Vin = 12 Vdc
Pout = 2 kW
Vout = 220 Vac single phase
HF isolated front-end under study
```

---

# 2. First correction: `fosc` is not the LC resonant frequency

For the minimum symmetric self-oscillating sequence:

```text
qT1 -> qK12 -> qR12 -> qT2 -> qK21 -> qR21 -> repeat
```

if the two half-cycles are approximately symmetric, define:

```text
tH = tT + tK + tR + td
```

where:

```text
tT = useful bulk-transfer interval
tK = natural commutation interval
tR = reset / recovery interval
td = any additional dead / eligibility interval
```

Then:

```text
Tosc = 2 * tH
fosc = 1 / [2*(tT+tK+tR+td)]
```

Therefore:

```text
1 / [2*pi*sqrt(Lcomm*Ceq)]
```

is only a local natural frequency associated with the qK transition. It is not, by itself, the complete converter switching frequency.

This distinction is central: `Lcomm` may strongly control whether natural commutation is possible while only weakly controlling total `fosc` if `tK << tT`.

---

# 3. Exact ideal qK transition-time sensitivity

From Math-1:

```text
tK = sqrt(Lcomm*Ceq) * asin(1/lambda)
```

with:

```text
lambda = Icomm*sqrt(Lcomm/Ceq) / Vtr
```

and natural-transition feasibility requires:

```text
lambda > 1
```

for positive residual-current margin.

Define:

```text
r = 1/lambda
0 < r < 1

theta = asin(r)

A(lambda) = r / [theta*sqrt(1-r^2)]
```

Then the normalized local sensitivities of qK transition time are:

```text
S_L^tK = d ln(tK) / d ln(Lcomm)
       = (1 - A)/2

S_C^tK = d ln(tK) / d ln(Ceq)
       = (1 + A)/2

S_I^tK = d ln(tK) / d ln(Icomm)
       = -A

S_V^tK = d ln(tK) / d ln(Vtr)
       = +A
```

This result gives two important regimes.

### 3.1 Near the energy boundary: `lambda -> 1+`

Then:

```text
A -> very large
```

so transition time becomes extremely sensitive to tolerances in:

```text
Icomm
Ceq / Qoss
Vtr
Lcomm
```

A design that merely satisfies `lambda ~= 1` is therefore mathematically fragile even before nonlinearity and loss are included.

### 3.2 Strong-commutation regime: `lambda >> 1`

For small `r`:

```text
asin(r) ~= r
A -> 1
```

and:

```text
S_L^tK -> 0
S_C^tK -> 1
S_I^tK -> -1
S_V^tK -> 1
```

Thus:

```text
tK ~= Ceq*Vtr/Icomm
```

which is the charge-limited result. In this regime, making `Lcomm` even larger does little to shorten qK directly; it mainly increases stored energy / current-stress consequences.

This gives a first design warning:

```text
more Lcomm is not automatically better once adequate commutation margin exists.
```

---

# 4. Sensitivity envelope versus `lambda`

Illustrative values from the exact ideal expression:

| `lambda` | `A(lambda)` | `S_L^tK` | `S_C^tK` | `S_I^tK` | `S_V^tK` |
|---:|---:|---:|---:|---:|---:|
| 1.01 | 4.933 | -1.966 | 2.966 | -4.933 | +4.933 |
| 1.05 | 2.477 | -0.739 | 1.739 | -2.477 | +2.477 |
| 1.10 | 1.912 | -0.456 | 1.456 | -1.912 | +1.912 |
| 1.20 | 1.530 | -0.265 | 1.265 | -1.530 | +1.530 |
| 1.50 | 1.226 | -0.113 | 1.113 | -1.226 | +1.226 |
| 2.00 | 1.103 | -0.051 | 1.051 | -1.103 | +1.103 |
| 5.00 | 1.014 | -0.007 | 1.007 | -1.014 | +1.014 |

Interpretation:

```text
lambda barely above 1 -> tolerance-sensitive / fragile commutation
lambda much larger     -> robust voltage reachability, but extra magnetic/current energy may be wasted as RMS/circulation
```

No optimum `lambda` is selected yet. A later loss model must find the useful window.

---

# 5. Reflected impedance enters mainly through `Icomm` and damping

At this stage, do not assume:

```text
Icomm = Vin/Zref
```

because the actual commutation current may contain:

```text
reflected-load current
magnetizing current
differential/leakage current
current-fed inductor contribution
W3 / clamp / resonant contribution
```

Define the local current sensitivity to reflected impedance:

```text
eta_I,Z = d ln(|Icomm|) / d ln(Zref)
```

Then, through qK current dependence alone:

```text
S_Z^tK,current = d ln(tK)/d ln(Zref)
               = -A * eta_I,Z
```

Examples of interpretation only:

```text
voltage-fed, load-current-dominated:
Icomm roughly proportional to 1/Zref
=> eta_I,Z roughly -1
=> tK increases as Zref rises

current-fed / magnetizing-current-dominated:
eta_I,Z may be much closer to 0
=> direct load sensitivity of qK may be weaker
```

The exact sign and magnitude must come from the eventual state graph.

---

# 6. qK damping condition when the load remains visible

The ideal Math-1 trajectory was lossless. If the commutation state still sees an effective resistance `RK`, the local transition is approximately an underdamped RLC process.

Define:

```text
alphaK = RK / (2*Lcomm)
omega0 = 1/sqrt(Lcomm*Ceq)
omega_d = sqrt(omega0^2 - alphaK^2)
```

A necessary underdamped condition is:

```text
RK < 2*sqrt(Lcomm/Ceq)
```

or:

```text
zetaK = RK/2 * sqrt(Ceq/Lcomm) < 1
```

`RK` is **not automatically equal to `Zref`**. It is the effective damping seen by the qK commutation mode after the actual secondary/clamp/device state is referred to that mode.

This introduces a second way that load can affect natural commutation:

```text
Zref -> Icomm at qK entry
Zref -> effective damping RK during qK
```

Therefore a future concrete circuit must identify whether the secondary/load is:

```text
fully visible
partially visible
clamped
or effectively isolated
```

during qK.

---

# 7. Transfer interval `tT`: two legal trigger families

Self-oscillation requires a physical event that ends qT and allows qK to begin. At this point two broad trigger families remain open.

## 7.1 Flux-excursion / magnetic-state trigger

For approximately constant common-mode winding voltage during qT:

```text
dB_c/dt = Vc / (Nc*Ae)
```

If the natural event occurs after a designed common-mode flux excursion `DeltaB_trig`:

```text
tT,flux ~= Nc*Ae*DeltaB_trig / |Vc|
```

This does **not** require intentional hard saturation. `DeltaB_trig` may be set below `Bsat` by a magnetic-feedback threshold / nonlinear magnetic event / sensing network.

Normalized local sensitivities are:

```text
S_N^tT      = +1
S_Ae^tT     = +1
S_DeltaB^tT = +1
S_Vc^tT     = -1
```

Math-2 flux protection remains:

```text
Bpk <= Ballow
```

and the external controller must prevent the self-oscillator from drifting below the minimum safe frequency.

## 7.2 Current / feedback-threshold trigger

If qT ends when an effective magnetic/branch current reaches a threshold and its slope is approximately constant:

```text
di/dt ~= Veff/Leff
```

then:

```text
tT,current ~= Leff*DeltaI_trig / Veff
```

This family makes `fosc` more directly load/current-state dependent.

The eventual circuit may also use a mixed criterion. Math-3 therefore does not force one Royer-style saturation mechanism.

---

# 8. W3 coupling enters the oscillation through an event equation

From Math-2, with W1/W2 modalized:

```text
v3 ~= mc * dic/dt + md * did/dt
```

for a high-impedance W3 sensing approximation.

The actual feedback/trigger network can be represented generically as an event function:

```text
g[x(t), mc, md, Zref, u] = 0
```

where:

```text
x(t) = magnetic/electrical state vector
u    = bounded external correction variable
```

A natural event exists only if the state trajectory crosses the trigger surface with nonzero slope:

```text
g = 0
and
dg/dt != 0
```

The second condition is a transversality condition. If `dg/dt ~= 0`, tiny tolerances/noise can create large timing uncertainty.

For any parameter `p`, event-time sensitivity follows from implicit differentiation:

```text
dt_event/dp = - (partial g/partial p) / (partial g/partial t)
```

This gives a rigorous future route for studying:

```text
kc / kd variation
W3 turns variation
Zref variation
threshold variation
magnetic tolerance
external trim authority
```

without pretending that W3 always sets frequency through one simple LC formula.

---

# 9. W3 modal selectivity metrics

Because W3 may couple to both modes, define state-specific contamination ratios.

During bulk transfer qT:

```text
epsilon_T = |md * did/dt| / |mc * dic/dt|
```

when the desired role is common-flux feedback.

During commutation qK:

```text
epsilon_K = |mc * dic/dt| / |md * did/dt|
```

when the desired role is differential-mode commutation sensing/routing.

Interpretation:

```text
epsilon << 1 -> relatively clean modal observation
epsilon ~ 1  -> strong mixing of bulk and commutation states
epsilon >> 1 -> intended modal interpretation breaks down
```

This supplements Math-2's reduced magnetic constraint:

```text
kc^2 + kd^2 < 1
```

A single W3 mixed-role implementation is therefore only plausible if both magnetic coupling limits and event-timing contamination remain acceptable.

---

# 10. Total oscillation-frequency sensitivity is interval-weighted

For a symmetric half-cycle:

```text
tH = tT + tK + tR + td
```

Define interval weights:

```text
wT = tT/tH
wK = tK/tH
wR = tR/tH
wd = td/tH
```

with:

```text
wT + wK + wR + wd = 1
```

For any parameter `p`:

```text
S_p^f = d ln(fosc) / d ln(p)
      = -[ wT*S_p^tT + wK*S_p^tK + wR*S_p^tR + wd*S_p^td ]
```

This is a key Math-3 result.

It means that even if qK is highly sensitive to `Lcomm` or `Ceq`, the **overall switching frequency may not be** if qK occupies only a small fraction of the half-cycle.

Example only:

```text
tT = 5 us
tK = 50 ns
tR,td negligible
```

then approximately:

```text
wK ~= 0.0099
```

So a very large local qK timing sensitivity is attenuated by roughly two orders of magnitude in the direct total-frequency path.

However, `Lcomm/Ceq/Zref` may still affect `tT` indirectly by changing the state reached after qK, the feedback threshold, residual current, or W3 signal. Those indirect couplings must be included in the later state model.

This corrects an earlier oversimplification:

```text
self-oscillation frequency is not necessarily set mainly by Lcomm-Ceq resonance.
```

In many realizations the transfer/feedback interval may dominate the period, while `Lcomm-Ceq` mainly determines whether the edge can occur naturally.

---

# 11. External correction authority without destroying self-oscillation

Let the uncorrected natural event time be:

```text
tnat(p)
```

and let an external bounded variable `u` perturb the trigger surface / eligibility window so that:

```text
tedge = tnat + Delta t_u
```

Possible `u` variables remain:

```text
feedback threshold trim
phase window
turn-on inhibit window
current-balance bias
frequency-bound clamp
startup kick
```

Define a normalized external timing-authority measure:

```text
Gamma_u = |Delta t_u| / tH
```

No fixed numerical limit is selected yet. Instead the method keeps four structural requirements.

### EC-1 — natural edge existence

At nominal conditions with bounded correction removed:

```text
u = 0
```

there must still be a physically reachable natural event:

```text
g[x(t),p,0] = 0
```

within a safe interval.

### EC-2 — external control perturbs the event; it does not invent an unrelated edge

The preferred mechanism is:

```text
change threshold / eligibility / phase bias
-> natural state crossing occurs earlier or later
```

rather than:

```text
controller timer expires
-> MOS gate toggled irrespective of magnetic state
```

### EC-3 — bounded correction authority

There must exist a finite correction range able to cover expected drift:

```text
|Delta t_drift| <= |Delta t_u,max|
```

while remaining inside flux and commutation-energy limits.

### EC-4 — control-removal meaning test

At nominal design conditions, removing the slow correction should not eliminate the underlying natural crossing mechanism. It may worsen balance/drift, but the inner plant must still possess the physical commutation event.

These conditions define `bounded self-oscillation` more precisely than simply saying “self-excited plus externally driven.”

---

# 12. Frequency safety window

Math-2 gives a magnetic lower bound. For a simple symmetric square-excitation approximation:

```text
fosc >= f_flux,min = Vp / (4*Np*Ae*Ballow)
```

Natural commutation adds additional event constraints:

```text
lambda > 1
Ires >= Ires,min
tK <= tK,available
```

Therefore the allowed autonomous operating band must satisfy all of:

```text
f_flux,min <= fosc <= f_device/thermal,max
```

and within that band every qK transition must still satisfy the Math-1 energy / charge conditions.

The upper bound is not derived numerically yet because switching devices, core material, winding AC loss and gate-driver implementation are not selected.

---

# 13. Self-oscillation requires a stable closed cycle, not only repeated zero crossings

Define a Poincare / cycle-to-cycle state vector at the same point each oscillation cycle:

```text
x_n = [Phi_c, id, vCres, other stored-energy states, ...]_n
```

The natural plant plus any bounded slow correction creates a return map:

```text
x_(n+1) = F(x_n, p, u)
```

A periodic operating point must satisfy:

```text
x* = F(x*, p, u*)
```

Local cycle stability requires the eigenvalues of the Jacobian to remain inside the unit circle:

```text
rho( dF/dx |x* ) < 1
```

for the relevant closed-loop state set.

This gives an important correction to the research method:

```text
Math-1: one natural edge is reachable
Math-2: magnetic modes / flux can close over a cycle
Math-3: the repeated cycle must have bounded timing sensitivity and a stable return map
```

Therefore observing repeated oscillation in PSIM later is not enough by itself; perturbation / load-step recovery must also be checked.

---

# 14. New design deductions from Math-3

## D3-1 — `lambda` must have margin, not merely satisfy the energy equality

Because timing sensitivity diverges as `lambda -> 1+`, a practical design must choose a commutation-strength margin greater than the exact energy boundary.

The final numerical margin will be selected only after real `Qoss/Eoss`, tolerance and loss are known.

## D3-2 — very large `Lcomm` eventually stops buying transition speed

When `lambda >> 1`:

```text
tK ~= Ceq*Vtr/Icomm
```

so transition becomes charge/current limited. Further increasing leakage can then add RMS/circulation/cross-coupling with little direct timing benefit.

This supports the earlier research question:

```text
how much leakage should be integrated, rather than whether leakage is useful at all?
```

## D3-3 — load sensitivity is architecture-dependent

`Zref` does not have one universal effect on `fosc`.

It can act through:

```text
Icomm at qK entry
qK damping
qT current/flux trajectory
W3 trigger signal
reset-state duration
```

Therefore a self-oscillating converter cannot be characterized by one fixed `f = 1/(2*pi*sqrt(LC))` law over load.

## D3-4 — W3 coupling is part of timing design

The pair:

```text
{kc, kd}
```

is not merely a transformer detail. It changes the trigger surface and therefore the oscillator timing sensitivity.

## D3-5 — the outer controller should control the event surface, not replace the event

This is the cleanest mathematical interpretation of the original “self-oscillation + externally driven correction” idea.

---

# 15. What is now symbolically established

Math-3 establishes, at first-pass symbolic level:

1. complete oscillation frequency is the inverse of the sum of transfer, commutation, reset and dead/eligibility intervals;
2. the ideal qK timing sensitivity to `Lcomm`, `Ceq`, `Icomm`, and `Vtr` can be derived exactly;
3. designs close to `lambda=1` are intrinsically timing-sensitive;
4. reflected load influences the oscillator through both commutation-entry current and possible qK damping, with topology-dependent sign/magnitude;
5. W3 coupling affects event timing through a general trigger-surface relation;
6. total `fosc` sensitivity is interval-weighted, so qK resonance may govern edge feasibility without governing the whole switching frequency;
7. bounded external correction can be defined as perturbation of a naturally existing event surface;
8. sustained oscillation ultimately requires a stable cycle-to-cycle return map.

---

# 16. NOT yet established

Math-3 does not establish:

```text
exact operating frequency
exact safe frequency window
exact W3 turns/coupling
real MOSFET Qoss/Eoss margin
actual load-to-frequency curve
startup reliability
closed-loop stability margins
net efficiency gain
novelty
```

These require the first concrete minimum circuit/state graph.

---

# 17. Result and next mathematical gate

Math-3 status:

```text
SYMBOLIC FIRST-PASS CLOSED
```

The strongest result is that the natural oscillator has **two different design jobs**:

```text
qT / feedback dynamics -> largely set the oscillation period
qK / Lcomm-Ceq dynamics -> prove that the edge can occur naturally and robustly
```

They are coupled, but they should not be collapsed into one LC-frequency equation.

The next mandatory step is **Math-4: equal-resource W1/W2 current-distribution comparison**.

Math-4 must answer whether the proposed peer-winding architecture gives a real low-voltage/high-current advantage under matched resources, rather than merely replacing one 175-A path by two nominal 87.5-A paths.

Required baseline comparison:

```text
single-path baseline
vs
W1/W2 split-path method
```

with approximately matched:

```text
total copper volume / cross-sectional resource
total semiconductor conduction resource
core material / usable flux density
switching frequency and power boundary
```

and accounting for:

```text
winding DC + AC copper loss
termination/interconnect loss
MOS conduction loss
commutation-related extra RMS
core-loss consequence of geometry / flux modes
added W3 / balancing burden where material
```

Only after Math-4 should the method claim any real benefit from low-side power distribution.
# 2026-09-16 — Math-1: Self-Oscillation / Commutation-Energy Model v1

Status: `WORKING_BRANCH / MATH01 / SYMBOLIC_CLOSED_FIRST_PASS / PRE-PSIM`  
Method: `Bounded Self-Oscillating Multiwinding Front-End`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

---

## 1. Scope

This is the first mathematical gate for the proposed method.

It does **not** yet select the exact MOSFET arrangement, transformer geometry, W3 connection, or production schematic. It tests only the minimum physical claim:

> Can magnetic / leakage / differential inductive energy left by one transfer interval move the switch node to the next legal voltage state strongly enough and quickly enough that a natural commutation event can exist?

The system boundary remains:

```text
Vin  = 12 Vdc
Pout = 2 kW
Vout = 220 Vac single phase
```

The present calculation applies only to the HF magnetic front end. The 2ω single-phase energy buffer and final 220-Vac synthesis remain downstream obligations.

---

# 2. Minimum commutation-cell abstraction

For one natural transition, define:

```text
Lcomm  = effective inductance participating in the commutation mode
Icomm  = signed inductive current at the beginning of qK
Ceq    = total effective capacitance referred to the switching node
Vtr    = required switch-node voltage excursion for the next legal state
```

`Lcomm` may later be realized by:

```text
A. integrated leakage / differential magnetic mode
B. external Lext
C. hybrid: Lcomm = Llk,designed + Lext
```

`Ceq` may include:

```text
MOSFET Coss
winding / PCB capacitance that actually participates
intentional Cres
clamp capacitance referred to the transition node, where applicable
```

For real MOSFETs, `Coss` is nonlinear. Therefore the final device calculation must use `Eoss(V)` and `Qoss(V)` or the corresponding integrals, not a single datasheet capacitance number.

---

# 3. Necessary energy condition

At the beginning of the commutation state qK, the available inductive energy is

```text
EL0 = 0.5 * Lcomm * Icomm^2
```

For a first-pass linear-capacitance model, the energy associated with moving an equivalent capacitance through voltage `Vtr` is

```text
EC,tr = 0.5 * Ceq * Vtr^2
```

The minimum ideal reachability condition is therefore

```text
0.5 * Lcomm * Icomm^2 >= 0.5 * Ceq * Vtr^2
```

or

```text
Icomm * sqrt(Lcomm / Ceq) >= Vtr
```

Equivalent design forms:

```text
Lcomm,min = Ceq * (Vtr / Icomm)^2
```

```text
Icomm,min = Vtr * sqrt(Ceq / Lcomm)
```

```text
Ceq,max = Lcomm * (Icomm / Vtr)^2
```

This is a **necessary first-pass condition**, not sufficient proof of sustained self-oscillation.

For a real transition, include loss and margin:

```text
0.5 * Lcomm * Icomm^2 >= kE * Etransition,real
```

where `kE > 1` is a design margin and

```text
Etransition,real = Eoss,net + Eparasitic + Edeadtime_loss + Erecovery_loss + ...
```

For nonlinear output capacitance, use the energy integral / datasheet energy:

```text
Eoss(V) = integral[0->V] v * Coss(v) dv
```

and sum only the capacitor energies that actually need net energy from the commutation current for the selected topology.

Important: in complementary half-bridge-like transitions, one device capacitance can discharge while the other charges. The final device/topology model must therefore use the **net transition energy / charge of the actual node**, not blindly add `0.5*Coss*V^2` for every transistor.

---

# 4. Ideal natural-transition trajectory

Use the simplest lossless series-LC commutation interval to test whether a natural switching-node crossing is physically reachable.

Initial conditions at qK entry:

```text
vC(0) = 0
 iL(0) = Icomm
```

Natural frequency and characteristic impedance:

```text
omega0 = 1 / sqrt(Lcomm * Ceq)
Z0     = sqrt(Lcomm / Ceq)
```

The ideal trajectory is

```text
vC(t) = Icomm * Z0 * sin(omega0 * t)
```

```text
iL(t) = Icomm * cos(omega0 * t)
```

The maximum reachable voltage from this initial state is

```text
Vpk,natural = Icomm * sqrt(Lcomm / Ceq)
```

Therefore the same energy criterion appears again:

```text
Vpk,natural >= Vtr
```

Define a commutation-strength ratio

```text
lambda = Vpk,natural / Vtr
       = Icomm * sqrt(Lcomm / Ceq) / Vtr
```

Interpretation:

```text
lambda < 1  -> next voltage state is unreachable in the ideal LC model
lambda = 1  -> exact energy boundary; node just reaches Vtr with zero residual current
lambda > 1  -> node reaches Vtr with residual current available for diode clamp / continued transition
```

The time required to reach `Vtr` is

```text
ttr = sqrt(Lcomm * Ceq)
      * asin[ Vtr / (Icomm * sqrt(Lcomm / Ceq)) ]
```

or

```text
ttr = sqrt(Lcomm * Ceq) * asin(1/lambda)
```

At the exact boundary `lambda = 1`:

```text
ttr,boundary = (pi/2) * sqrt(Lcomm * Ceq)
```

The residual commutation current when the node reaches `Vtr` is

```text
Ires = sqrt[ Icomm^2 - (Ceq/Lcomm) * Vtr^2 ]
```

or

```text
Ires = Icomm * sqrt(1 - 1/lambda^2)
```

This residual-current expression is useful later because a practical natural transition normally should not terminate exactly at `Ires = 0`; some current margin is needed to establish the next diode/channel conduction state under tolerances and loss.

---

# 5. Charge / dead-time condition

Energy sufficiency alone is not enough. The switch node must also move before the legal commutation window closes.

Define the required node charge:

```text
Qtr = integral Cnode(v) dv over the required voltage excursion
```

For a linear first-pass capacitance:

```text
Qtr ~= Ceq * Vtr
```

A rough constant-current lower-bound estimate is

```text
tQ ~= Qtr / |Icomm|
```

The resonant trajectory from Section 4 gives the more appropriate ideal LC transition time `ttr`.

A legal natural transition therefore requires both:

```text
EL0 >= Etransition,real
```

and

```text
ttr <= tK,available
```

where `tK,available` is the maximum interval before the next state would violate flux, device, current-source, or control constraints.

Later device-level work must check nonlinear `Qoss`, diode conduction, gate threshold timing, reverse recovery (if applicable), and propagation delay.

---

# 6. Connection to self-oscillation

Math-1 proves only that a **natural commutation event can be energetically/dynamically possible**.

It does **not** yet prove that a complete self-oscillating limit cycle exists.

A full self-oscillation cycle will require at least:

```text
qT: bulk-transfer interval
 -> qK: natural commutation interval
 -> qR: residual-energy reset / recovery
 -> opposite qT
 -> ...
```

The base switching period is therefore not automatically

```text
1 / [2*pi*sqrt(Lcomm*Ceq)]
```

because the total period also contains transfer and recovery intervals.

Conceptually:

```text
Tosc = sum(tT + tK + tR + any safe/dead intervals)
```

and

```text
fosc = 1 / Tosc
```

Math-3 will derive sensitivity of this period to `Lcomm`, `Ceq`, reflected load, current and magnetic state.

---

# 7. W1 / W2 / W3 interpretation at Math-1 level

No exact winding graph is assumed yet.

### W1 / W2

At qT they are the load-bearing transfer paths. At qK their leakage or differential-mode energy may contribute to `Lcomm`.

### W3

W3 is allowed to perform one or more of the following during qK/qR:

```text
magnetic feedback sensing
commutation-energy routing
reset / recovery
low-VA correction, only if later VA analysis proves it
```

Math-1 does not assume W3 is a full-power winding.

### Integrated / external / hybrid comparison parameter

Define

```text
rhoL = Lintegrated_comm / Lcomm
```

so that

```text
rhoL = 1   -> fully integrated commutation inductance
rhoL = 0   -> fully externalized commutation inductance
0<rhoL<1   -> hybrid
```

Later optimization can test whether the useful region occurs at an interior `rhoL`, rather than assuming either full integration or full externalization.

---

# 8. 12-V / 2-kW boundary numbers

The anchor input current is large:

```text
Iin,ideal = Pout / Vin
          = 2000 / 12
          = 166.67 A
```

At an illustrative 95% front-to-output efficiency assumption:

```text
Iin,95% = 2000 / (12 * 0.95)
        = 175.44 A
```

If W1 and W2 share average input current equally:

```text
Ibranch,avg ~= 87.72 A   [95% illustrative case]
```

But **do not set `Icomm = 87.72 A` automatically**.

Define

```text
beta = |Icomm| / Ibranch,avg
```

because the current available at the commutation instant depends on ripple, magnetizing current, leakage/differential mode, load, phase and state timing.

Thus

```text
Icomm = beta * Ibranch,avg
```

must later be obtained from the actual state graph.

---

# 9. Parametric numerical envelope — NOT a device selection

The following examples are only sensitivity checks. `Ceq`, `Vtr` and `Icomm` are not selected hardware values.

### Example P1

```text
Vtr   = 24 V
Ceq   = 10 nF
Icomm = 20 A
```

Then

```text
Etransition,linear = 0.5*Ceq*Vtr^2 = 2.88 uJ
Lcomm,min          = Ceq*(Vtr/Icomm)^2 = 14.4 nH
ttr at exact energy boundary = 18.85 ns
```

### Example P2

```text
Vtr   = 48 V
Ceq   = 10 nF
Icomm = 20 A
```

Then

```text
Etransition,linear = 11.52 uJ
Lcomm,min          = 57.6 nH
ttr at exact energy boundary = 37.70 ns
```

### Example P3

```text
Vtr   = 48 V
Ceq   = 20 nF
Icomm = 20 A
```

Then

```text
Etransition,linear = 23.04 uJ
Lcomm,min          = 115.2 nH
ttr at exact energy boundary = 75.40 ns
```

These examples show the expected scaling:

```text
Lcomm,min proportional to Ceq
Lcomm,min proportional to Vtr^2
Lcomm,min proportional to 1/Icomm^2
```

Therefore the eventual use of several low-voltage MOSFETs in parallel can materially increase the required commutation charge/energy because total effective `Coss/Qoss` rises even while conduction resistance falls. This is a direct conduction-loss / commutation-energy trade-off to preserve.

---

# 10. First hard design inequalities

For any later concrete W1/W2/W3 circuit, the following must all be checked.

### M1. Energy reachability

```text
0.5 * Lcomm * Icomm^2 >= kE * Etransition,real
```

### M2. Voltage-state reachability

```text
Icomm * sqrt(Lcomm/Ceq) >= Vtr
```

### M3. Time-window legality

```text
ttr <= tK,available
```

### M4. Residual-current margin

```text
Ires > Ires,min
```

where `Ires,min` is later set from the required diode/channel latch, loss and tolerance margin.

### M5. Reset closure

Any energy remaining after the node reaches the target state must have a qR return path:

```text
EL,residual + EC,residual -> source / load / next transfer state / defined storage
```

No unexplained trapped-energy state is legal.

### M6. Self-oscillation meaning test

The physical state crossing must be capable of generating the base commutation event. If the external controller must command essentially every transition regardless of the natural LC/magnetic crossing, then the method has degenerated into ordinary forced PWM and H2 is falsified.

---

# 11. What Math-1 establishes and does not establish

## Established at symbolic first-pass level

A mathematically explicit minimum condition exists for converting inductive commutation energy into the next switch-node voltage state:

```text
Lcomm,min = Ceq * (Vtr/Icomm)^2
```

for the ideal linear LC abstraction, together with an exact ideal transition-time expression and residual-current expression.

This gives a concrete design axis for comparing:

```text
integrated leakage
external commutation inductance
hybrid leakage + external inductance
```

and it directly connects magnetic design to natural commutation feasibility.

## NOT established

Math-1 does not yet prove:

```text
sustained self-oscillation
startup from zero energy
flux balance
ZVS over load range
W1/W2 equal current sharing
net efficiency improvement
W3 low-VA behavior
novelty
hardware feasibility
```

Those remain later gates.

---

# 12. Result / next mathematical gate

Math-1 status:

```text
SYMBOLIC FIRST-PASS CLOSED
NUMERIC DEVICE DESIGN NOT YET POSSIBLE
```

The reason numeric device design is not yet possible is that the exact commutation node and semiconductor set are intentionally not selected yet, so actual `Eoss(V)`, `Qoss(V)`, `Vtr`, `Icomm` and the winding-mode inductance matrix remain unknown.

The next mandatory step is **Math-2: W1/W2/W3 magnetic volt-second and flux-balance model**.

Math-2 must answer:

```text
1. Can W1 and W2 alternate / share transfer without dc flux walk?
2. What magnetic modes are required: one common flux only, or common + differential modes?
3. Where can W3 couple without forcing unwanted bulk-power circulation?
4. Which mode actually owns Lcomm?
5. Can qT -> qK -> qR close flux and energy every cycle?
```

Only after Math-2 should a concrete self-oscillating winding connection be drawn.
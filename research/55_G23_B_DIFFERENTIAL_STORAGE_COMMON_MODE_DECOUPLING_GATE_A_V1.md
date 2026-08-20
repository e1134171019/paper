# 55 — G23-B Differential-Storage / Common-Mode Decoupling Gate A v1

Status date: 2026-08-20  
Role: `O23 DIFFERENTIAL-STORAGE ACTUAL GRAPH / COMMON-DIFFERENTIAL ENERGY CLOSURE / PRIOR-ART GATE A`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Evidence status: `FIRST-PRINCIPLES + MULTI-ROUTE PRIOR-ART SCREEN`  
Simulation status: `NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`  
G23-B novelty status: `STOP_AS_NOVELTY / REFERENCE-CLASS DIFFERENTIAL-INVERTER REGION`

## 1. Purpose

File 54 stopped the two most obvious O23 graphs:

```text
G23-A1 = split-link / T-type / NPC storage + AC synthesis
G23-A2 = flying-capacitor multilevel storage + power-pulsation buffering
```

The next admissible O23 target was deliberately moved away from a single common DC link:

```text
G23-B = differential-storage AC synthesis
```

The intended physical separation was:

```text
differential voltage  -> X3 / AC synthesis
common-mode energy    -> X2 / 2ω buffering
```

The question is whether this produces a genuinely different unexplored power graph or merely rediscovers the established differential-inverter / active-power-decoupling class.

No PSIM is authorized unless this file survives both physics and prior-art gates.

---

## 2. Normalized actual graph

X1 remains upstream and completes before the differential inverter/storage stage.

```text
N0  12-V source
 |
 v
X1  matched voltage/current-domain converter
 |
 | majority power leaves ~175-A domain
 v
N3  post-X1 reduced-current DC domain
 |\
 | \-------------------------------\
 |                                  \
 v                                   v
Port A DC/DC or half-bridge          Port B DC/DC or half-bridge
 |                                   |
 +-- CA, storage/output capacitor    +-- CB, storage/output capacitor
 |                                   |
 vA                                  vB
  \                                 /
   \--------- differential load ----/
                |
              filter
                |
             220 Vac
```

For the generic voltage-source form:

```text
vout = vA - vB
```

and `CA` / `CB` are not passive spectators: their voltages are intentionally modulated so that the two converter ports simultaneously provide AC synthesis and low-frequency energy storage.

Coordinate assignment:

```text
X1 = upstream converter and is physically separate.
X2 = energy in CA + CB intentionally cycled at 2ω.
X3 = differential voltage vA-vB produces the AC output.
```

This is a genuine O23 graph because X2 and X3 share the same output/storage capacitors and the same port switching states.

---

## 3. Common-mode / differential-mode decomposition

For equal storage capacitors:

```text
CA = CB = C
```

define:

```text
vc = (vA + vB)/2
vd = (vA - vB)/2
```

Therefore:

```text
vA = vc + vd
vB = vc - vd
vout = 2vd
```

For the required sinusoidal output:

```text
vout(t) = Vm sin(ωt)
Vm = sqrt(2) × 220 = 311.13 V
```

so:

```text
vd(t) = Vm/2 × sin(ωt)
      = 155.56 sin(ωt) V
```

The intuitive research hypothesis would be:

```text
vd controls X3
vc controls X2
```

but the energy equation shows that these controls are not perfectly orthogonal.

---

## 4. Total storage-energy closure

The total capacitor energy is:

```text
Ecap = 0.5 C vA² + 0.5 C vB²
```

Substituting `vA=vc+vd` and `vB=vc-vd`:

```text
Ecap = C(vc² + vd²)
```

Therefore the AC-synthesis differential voltage contributes directly to the total low-frequency stored energy.

Since:

```text
vd² = (Vm²/4) sin²(ωt)
    = (Vm²/8)[1 - cos(2ωt)]
```

we obtain:

```text
Ecap(t)
= C vc²(t)
+ C Vm²/8
- C Vm²/8 cos(2ωt)
```

This is the first major interaction result:

> `X3 differential-mode synthesis itself creates a 2ω term in the storage-energy equation.`

Thus common-mode energy control must compensate not only the load/source power mismatch but also the differential-mode squared-voltage energy term.

This is `INTERACTION_NEW` for the project ledger.

---

## 5. Required X2 energy trajectory

For unity-PF single-phase output:

```text
pout(t) = P[1 - cos(2ωt)]
```

If X1 is regulated to process approximately constant power `P`, then:

```text
pbuf(t) = P - pout(t)
        = P cos(2ωt)
```

and:

```text
dEbuf/dt = pbuf(t)
```

so:

```text
Etarget(t) = E0 + ΔE sin(2ωt)
```

where:

```text
ΔE = P/(2ω)
   = P/(4πf)
   = 3.183 J
```

at `P=2 kW`, `f=50 Hz`.

Equating capacitor energy to the required trajectory gives:

```text
C vc²(t)
= E0
+ ΔE sin(2ωt)
- C Vm²/8
+ C Vm²/8 cos(2ωt)
```

or:

```text
vc²(t)
= E0/C - Vm²/8
+ (ΔE/C) sin(2ωt)
+ (Vm²/8) cos(2ωt)
```

Therefore the common-mode squared-voltage command contains two quadrature 2ω components.

Its 2ω amplitude in `vc²` is:

```text
A_vc² = sqrt[(ΔE/C)² + (Vm²/8)²]
```

Critical interpretation:

```text
Differential mode and common-mode decoupling are control-separable,
but not energy-orthogonal.
```

The X3 term must be explicitly paid in common-mode voltage range, capacitor RMS current, or both.

---

## 6. Voltage-domain feasibility constraint

For unipolar storage capacitors/ports:

```text
vA >= 0
vB >= 0
```

requires:

```text
vc >= |vd|
```

and at the AC-voltage peak:

```text
|vd|max = 155.56 V
```

so the common-mode bias cannot collapse below this level for the normalized buck-type differential realization.

Increasing common-mode bias relaxes this constraint but raises:

```text
capacitor voltage rating
switch blocking voltage
stored baseline energy
switching loss exposure
```

Reducing capacitor value increases `ΔE/C` and therefore increases the required common-mode voltage excursion.

Thus G23-B carries the same general power-density trade-off found in File 54, but in a differential/common-mode form:

```text
smaller C
→ larger vc modulation
→ larger port voltage/current stress
→ potentially higher semiconductor and capacitor loss
```

---

## 7. Loss-fate audit

Compared with a conventional post-X1 H-bridge + passive DC-link buffer:

| Physical burden | G23-B fate |
|---|---|
| upstream X1 conduction/magnetic loss | RETAINED |
| separate large passive 2ω link capacitor | potentially REDUCED/RELOCATED |
| conventional H-bridge AC synthesis | replaced by two differential converter ports |
| CA/CB storage capacitors | INTRINSIC / shared X2+X3 |
| two-port switching conduction | INTRINSIC_NEW relative to simple VSI comparison |
| common-mode circulating/decoupling current | INTERACTION_NEW |
| differential-output filter | RETAINED |
| capacitor ESR/dielectric loss | RETAINED/RELOCATED |
| sensor/control burden for APD | SUPPORT_NEW or INCREASED |

The topology can reduce dedicated decoupling hardware because the converter output capacitors are also the APD storage elements, but it does not eliminate 2ω energy and cannot claim lower total loss without matched semiconductor, inductor and capacitor models.

---

## 8. Multi-route Gate A

Three materially different retrieval routes were used.

### Route A — IEEE-direct architecture search

IEEE search recovered an exact class-level match:

R. Musona and I. Serban,
“Differential Single-Phase Inverters With Active Power Decoupling: A Survey,”
IEEE Access, vol. 11, pp. 53654–53670, 2023,
DOI `10.1109/ACCESS.2023.3280228`.

The survey explicitly identifies the generic differential single-phase inverter as:

```text
two half-bridge / DC-DC converter ports
+ differential mode for main output power
+ common mode for active power decoupling
```

and covers:

```text
differential buck
differential boost
differential buck-boost
and derived structures
```

This is not merely similar terminology; it occupies the defining G23-B mechanism and coordinate relation.

Route-A result:

```text
G23-B generic differential/common-mode APD = ESTABLISHED PRIOR-ART CLASS
```

### Route B — semantic / detailed implementation search

Close records include:

1. R. Rajamony, S. Wang, R. Navaratne, and W. Ming,
“Multi-Objective Design of Single-Phase Differential Buck Inverters With Active Power Decoupling,”
IEEE Open Journal of Power Electronics, vol. 3, pp. 105–114, 2022,
DOI `10.1109/OJPEL.2022.3147769`.

Structural relevance:

```text
two differential buck converter outputs
+ output capacitors used for active power decoupling
+ common-mode compensation voltage
+ explicit efficiency / power-density / capacitor trade-off
```

The reported capacitor-voltage expressions use complementary sinusoidal terms plus a common compensation voltage, matching the normalized decomposition:

```text
vA = vc + vd
vB = vc - vd
```

2. S. Xu, L. Chang, R. Shao, and A. R. H. Mohomad,
“Power decoupling method for single-phase buck-boost inverter with energy-based control,”
APEC 2017,
DOI `10.1109/APEC.2017.7931188`.

Structural relevance:

```text
differential buck-boost inverter
+ energy-based active power decoupling
+ no separate additional APD semiconductor stage
```

Route-B result:

```text
both the graph and the energy-control intent are established.
```

### Route C — academic cross-check / survey corpus

Academic search confirms that differential inverter APD is now a consolidated literature class rather than an isolated paper.

The 2023 survey presents a unified mathematical treatment of differential buck/boost/buck-boost APD and explicitly states that the primary differential-mode loop and common-mode decoupling loop are the standard control decomposition.

Route-C result:

```text
COMMON-MODE APD + DIFFERENTIAL-MODE AC SYNTHESIS
= mature mechanism family
```

---

## 9. Gate-A decision

```text
ACTUAL GRAPH CLOSURE = PASS
X2 ENERGY CLOSURE = PASS
X3 DIFFERENTIAL SYNTHESIS = PASS
X2/X3 PHYSICAL OVERLAP = REAL
ENERGY ORTHOGONALITY = FAIL (interaction exists but controllable)
GENERIC NOVELTY = STOP
PRIOR-ART CLASS = SAME_CLASS / SAME_MECHANISM / NEAR_GRAPH
PSIM AS PROPOSED TOPOLOGY = NO
```

Reason:

> The defining G23-B concept — two converter/storage ports whose differential mode synthesizes single-phase AC while common mode actively handles twice-line-frequency power — is explicitly established and surveyed in IEEE literature.

Adding an upstream 12-V-to-HV X1 converter does not rescue topology novelty because it would be a cascade of a known X1 front end and an already-known differential APD inverter unless a future graph shares a genuinely new load-bearing edge across that boundary.

---

## 10. What G23-B contributes to the project despite novelty STOP

The branch produces a reusable interaction equation:

```text
Ecap = C(vc² + vd²)
```

which proves that:

```text
X3 differential voltage
and
X2 common-mode energy control
```

are not energy-independent.

For any future differential or multiport graph, the `vd²` 2ω term must be included in the loss/stress/voltage-range audit.

This prevents a future candidate from falsely claiming that common-mode buffering is an independent “free” degree of freedom.

---

## 11. O23 closure status after Files 54–55

The following generic O23 regions are now prior-art references rather than candidate directions:

```text
split-link / T-type / NPC integrated APD
flying-capacitor multilevel integrated PPB
differential buck APD
differential boost APD
differential buck-boost APD
common-mode decoupling of differential single-phase inverters
```

This does NOT prove that every possible O23 graph is exhausted.

However, the obvious generic mechanisms are sufficiently mature that O23 should no longer be the immediate candidate-synthesis mainline without a materially different shared energy-transfer edge.

Status:

```text
O23 = REFERENCE-RICH / DEFER NEW GENERIC SYNTHESIS
```

---

## 12. Immediate next coordinate branch

With the obvious O13 and O23 realizations closed as novelty directions, the next coordinate branch is the constrained admissible subset of O12:

```text
G12-A = X1+X2 overlap located near/after X1 current reduction
      + X3 physically separate
```

The key constraint is NOT to buffer 2ω energy in the 12-V / ~175-A series path.

Required G12-A placement:

```text
12 V source
→ minimal LV X1 switching
→ magnetic/other main transfer
→ reduced-current secondary/intermediate X1 region
   where X2 shares an existing X1 switching / magnetic / energy-transfer edge
→ stabilized/controlled output of X1
→ separate X3 VSI
→ 220 Vac
```

Admission requirements:

```text
G12-G1: X2 must not add a full-current series edge at N0/N1.
G12-G2: X2 must share an existing load-bearing X1 edge/state, not be a separate APD converter attached to the bus.
G12-G3: the 3.183-J 2ω energy must be stored at reduced-current voltage/current domain.
G12-G4: any increase in transformer/secondary RMS is INTERACTION_NEW.
G12-G5: generic DAB/LLC/FCC power-decoupling control is reference prior art unless the actual graph changes the physical energy path.
```

`G12-A` is only the next graph target. Novelty remains `NOT_ESTABLISHED` and PSIM remains unauthorized.

Candidate #10 remains `HOLD / NOT_ASSIGNED`.

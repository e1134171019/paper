# 56 — G12-A X1+X2 Shared Front-End Power-Decoupling Gate A v1

Status date: 2026-08-20  
Role: `O12 ACTUAL-GRAPH / X1-X2 ENERGY CLOSURE / TRANSFORMER-RMS AUDIT / PRIOR-ART GATE A`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Canonical post-X1 rail used for first-principles screen: `350 Vdc`  
Evidence status: `FIRST-PRINCIPLES + MULTI-ROUTE PRIOR-ART SCREEN`  
Simulation status: `NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

Files 53–55 closed the obvious O13 and O23 realizations as novelty directions. The next admissible coordinate branch is:

```text
G12-A = X1 + X2 overlap
      + X3 physically separate
```

with a hard placement constraint:

```text
X2 must not add another full-current series edge in the 12-V / ~175-A source path.
```

The test is whether the unavoidable single-phase 2ω energy can be handled by an energy-storage state controlled through the existing X1 converter, preferably at the post-X1 high-voltage/reduced-current boundary, without adding a second active power-decoupling converter.

Two subcases are screened:

```text
G12-A1 = existing X1 transfer states + post-X1 HV-link capacitor energy swing
G12-A2 = stronger magnetic/common-mode integration in which the buffer state shares transformer/secondary current paths
```

No PSIM is authorized unless a graph survives physics and prior-art gates.

---

## 2. G12-A1 normalized actual graph — DAB/HFT-controlled post-X1 buffer

```text
N0  12-V source
 |
 v
N1  primary active bridge
 |
 v
T_HF + leakage/transfer inductance
 |
 v
secondary active bridge / synchronous rectification
 |
 |    X1 completes here: majority power is now HV / reduced-current
 v
N3  350-V-class DC node
 |
 +---- Cbuf / Cdc ---- return
 |
 v
X3  separate VSI
 |
 v
output filter
 |
 v
220 Vac / 50 Hz
```

Coordinate assignment:

```text
X1 = active isolated DC/DC transfer from 12 V to the HV node.
X2 = deliberate 2ω energy swing in Cbuf/Cdc.
X3 = separate VSI downstream.
```

The same X1 phase-shift/duty/power-control states determine the energy delivered into the storage node; there is no independent APD semiconductor leg.

This satisfies the minimum O12 hardware-sharing requirement, although the storage capacitor itself remains located at the X1 output boundary.

---

## 3. X2 energy closure for G12-A1

For unity-PF single-phase output:

```text
pout(t) = P[1 - cos(2ωt)]
```

If X1 draws approximately constant source power `P`, then:

```text
pC(t) = P - pout(t)
      = P cos(2ωt)
```

and the required storage-energy trajectory is:

```text
EC(t) = E0 + [P/(2ω)] sin(2ωt)
```

At:

```text
P = 2000 W
f = 50 Hz
```

energy swing amplitude is:

```text
E2ω,pk = P/(4πf) = 3.183 J
```

and peak-to-peak energy is:

```text
E2ω,pp = 6.366 J
```

For one HV-link capacitor:

```text
E = 0.5 C Vdc²
```

therefore:

```text
C = 2 E2ω,pp / (Vmax² - Vmin²)
```

At a 350-V center rail:

| rail swing | Vmin–Vmax | required C |
|---|---:|---:|
| ±5% | 332.5–367.5 V | ~520 µF |
| ±10% | 315–385 V | ~260 µF |

A separate 220-Vac VSI with no extra gain requires, ideally:

```text
Vdc,min >= sqrt(2) × 220 = 311.13 V
```

Hence the 350-V rail has only about:

```text
(350 - 311.13)/350 = 11.1%
```

ideal downward swing before AC peak-voltage headroom is lost.

Therefore the File-54 modulation-headroom constraint also applies to O12:

```text
larger X2 voltage swing
→ smaller C
but
→ less X3 headroom / higher required average rail
→ higher semiconductor voltage stress
```

---

## 4. Current/loss location for G12-A1

At 350 V, the low-frequency capacitor-current scale is:

```text
Ibuf,pk ≈ P/Vdc = 5.71 A
Ibuf,rms,2ω ≈ P/(sqrt(2)Vdc) = 4.04 A
```

This is structurally preferable to allowing the 2ω power to appear at 12 V, where the corresponding source-current amplitude is approximately:

```text
2000/12 = 166.7 A
```

The low-frequency capacitor ESR contribution alone is:

```text
Pcap,2ω = Ibuf,rms² ESR
          ≈ 16.3 × ESR[Ω] W
```

before HF ripple/dielectric loss is added.

Critical distinction:

> In the ideal G12-A1 energy picture, X1 can transfer approximately constant average power while Cbuf alone supplies/absorbs the line-frequency power mismatch. The full 2ω energy does not need to cross the transformer a second time.

Therefore G12-A1 avoids the strongest transformer-RMS penalty of deeper magnetic-buffer integration.

However, real DAB phase-shift/duty control, ZVS boundaries and link-voltage variation may change HF RMS/circulating current. Any such increase is `INTERACTION_NEW` and must be measured/modelled before a loss claim.

---

## 5. G12-A2 adversarial stronger-integration screen — transformer/common-mode buffer

A stronger interpretation of X1+X2 would place the buffer energy-transfer path inside an existing transformer/secondary common-mode or center-tap path rather than merely at the X1 output capacitor.

Normalized intent:

```text
12-V bridge
→ HFT
→ reduced-current secondary region
   ↕ shared transformer/common-mode state
   Cbuf
→ controlled HV output of X1
→ separate X3
```

This is attractive because X2 would share a genuinely load-bearing magnetic/switching edge with X1 and could avoid an independent APD switch leg.

But it creates an unavoidable current-rating question.

The 2ω buffer-power RMS magnitude is:

```text
Pbuf,rms = P/sqrt(2) = 1.414 kW
```

At a normalized 350-V secondary/storage domain:

```text
Ibuf,rms,LB ≈ 4.04 A
```

while the ideal constant-power secondary current scale is:

```text
Imain,eq = P/350 = 5.71 A
```

Thus:

```text
(Ibuf,rms,LB / Imain,eq)² ≈ 0.50
```

If the same transformer winding/current path must carry both components, the buffer mechanism introduces an order-0.5 additional current-square exposure relative to the ideal constant-power current scale before HF waveform, covariance, leakage and commutation penalties are included.

This is not an exact transformer-loss prediction. It is a lower-order warning that:

```text
deep X1/X2 magnetic integration
can trade APD switch count for transformer RMS/current-rating burden.
```

This burden is classified as `INTERACTION_NEW`.

---

## 6. Loss-fate audit versus O0

Normalize O0 as:

```text
12-V switching
→ HFT
→ rectifier
→ stiff HV DC link / passive X2
→ independent VSI
```

### G12-A1

| O0 burden | G12-A1 fate |
|---|---|
| pre-X1 LV conduction | RETAINED |
| transformer copper/core | RETAINED; DAB/control-specific change TBD |
| separate APD switch leg | NOT ADDED |
| 2ω energy requirement | RETAINED |
| bulky stiff-link capacitance | potentially REDUCED by allowed voltage swing |
| HV capacitor RMS | RETAINED / may increase |
| X1 control complexity | INCREASED |
| X3 VSI | RETAINED |

### G12-A2

| burden | fate |
|---|---|
| APD active-switch count | potentially REDUCED |
| transformer/common-mode RMS | INTERACTION_NEW / increased |
| magnetic VA/current rating | potentially INCREASED |
| buffer capacitor | RETAINED |
| X3 VSI | RETAINED |

The central physical conclusion is:

```text
X1+X2 overlap can be well located after current reduction,
but integration depth determines where the unavoidable 2ω cost appears.
```

---

## 7. Multi-route Gate A

Three materially different retrieval routes were used: IEEE-targeted direct web retrieval, Exa semantic retrieval, and Sider/OpenAlex academic cross-check.

### Route A — direct DAB/two-stage prior art

S. Amin, H.-H. Lee, and W. Choi,
“A Novel Power Decoupling Control Method to Eliminate the Double Line Frequency Ripple of Two Stage Single-Phase DC-AC Power Conversion Systems,”
Electronics, 2020,
DOI `10.3390/electronics9060931`.

Structural relevance:

```text
DAB DC/DC front end
+ separate single-phase inverter
+ no additional APD hardware
+ front-end voltage/power control suppresses source-side double-line ripple
+ DC-link voltage is intentionally allowed to oscillate
```

The paper reports simulation and experiment with a 5-kW DAB + single-phase inverter system.

This occupies the defining G12-A1 graph/control region.

Result:

```text
G12-A1 generic DAB-controlled post-X1 2ω buffering = ESTABLISHED PRIOR ART
```

### Route B — integrated DAB ripple steering / no-extra-switch prior art

J. You, D. M. Vilathgamuwa, N. Ghasemi, and W. L. Malan,
“An Active Power Decoupling Method for Single Phase DC/AC DAB Converters,”
IEEE Access, vol. 7, 2019, pp. 12964–12972,
DOI `10.1109/ACCESS.2019.2893286`.

Structural relevance:

```text
existing primary full-bridge switching devices
+ integrated LLC/ripple-steering passive network
+ 100-Hz ripple-current suppression
+ no additional switching components
```

Although its complete DC/AC graph is not identical to G12-A1, it establishes that multiplexing existing DAB/HF-link switching states with a ripple-energy network is already a developed physical mechanism.

Result:

```text
“reuse X1 switches for X2 without an extra APD switch” is not a novel primitive.
```

### Route C — transformer center-tap/common-mode APD corpus

Prior-art reviews and isolated converter papers explicitly report decoupling capacitors connected to the center tap of an isolation transformer and use common-mode transformer voltage to absorb single-phase pulsating power without extra switches.

A directly relevant established example is the center-tapped-transformer matrix-converter power-decoupling family already locked in File 53, including Takaoka/Takahashi/Itoh work and DOI `10.1109/TIA.2017.2774760`.

The literature also explicitly identifies the penalty:

```text
center-tap/common-mode decoupling
→ increased transformer current rating / transformer loss burden
```

This matches the G12-A2 first-principles RMS warning.

Result:

```text
G12-A2 generic transformer/common-mode shared-buffer primitive = ESTABLISHED PRIOR-ART REGION
```

---

## 8. Gate-A decision

### G12-A1 — DAB/HFT-controlled HV-link buffer + separate VSI

```text
ENERGY CLOSURE = PASS
X2 LOCATION = GOOD / POST-X1
NO NEW 175-A SERIES EDGE = PASS
SEPARATE APD POWER STAGE = NOT REQUIRED
GENERIC NOVELTY = STOP
PRIOR-ART CLASS = SAME_GRAPH / SAME_CONTROL INTENT
PSIM AS PROPOSED TOPOLOGY = NO
```

### G12-A2 — transformer/common-mode deeper integration

```text
PHYSICAL PRINCIPLE = FEASIBLE CLASS
X1/X2 EDGE SHARING = REAL
TRANSFORMER RMS PENALTY = MATERIAL / INTERACTION_NEW
GENERIC NOVELTY = STOP
PRIOR-ART CLASS = SAME_MECHANISM / NEAR_GRAPH
PSIM AS PROPOSED TOPOLOGY = NO
```

Therefore:

```text
G12-A = STOP_AS_NOVELTY / REFERENCE-RICH
```

but G12-A1 is retained as a useful physical comparator because it demonstrates a clean way to keep the 2ω energy at the post-X1 HV node without forcing that energy back through the 12-V source domain.

---

## 9. What File 56 adds to the project

### Result 1 — O12 location can be physically good even when novelty fails

The branch confirms the core location rule:

```text
buffer at ~350 V / ~4-A-rms low-frequency scale
>> preferable to
buffer reflected to 12 V / ~167-A amplitude scale
```

### Result 2 — two different X1+X2 integration depths must not be confused

```text
A1: X1 controls energy into post-X1 capacitor
    → clean current location; transformer need not carry buffer energy twice

A2: buffer path is embedded in transformer/common-mode current
    → fewer auxiliary switches possible, but transformer RMS/current rating rises
```

### Result 3 — stage sharing is not automatically a loss saving

The relevant comparison is:

```text
saved capacitor volume / removed APD hardware
versus
added transformer RMS / control-induced circulating current / voltage stress
```

### Result 4 — G12 is not a fresh generic topology region

DAB control-oriented decoupling, DAB-integrated ripple steering, and transformer-center-tap/common-mode decoupling are all established literature directions.

---

## 10. Coordinate-map status after Files 53–56

```text
O13 = X1+X3, X2 separate
  G13-A standard HFT cycloconverter/matrix
  → reference / novelty STOP

O23 = X1 separate, X2+X3
  G23-A split-link / FC APD
  G23-B differential/common-mode APD
  → reference-rich / defer

O12 = X1+X2, X3 separate
  G12-A DAB-controlled HV buffer
  transformer/common-mode integrated buffer
  → reference-rich / novelty STOP
```

This leaves the triple-overlap coordinate as the remaining unexecuted overlap class from File 52:

```text
O123 = X1 + X2 + X3
```

However O123 is high-risk because many single-stage isolated converters with integrated power decoupling already exist. It must receive immediate prior-art screening before any detailed synthesis.

---

## 11. Immediate next

Next target:

```text
G123-A = triple-overlap falsification
```

Admission rules:

```text
G123-G1
Do not merely cascade known X1, APD and inverter cells under a “single-stage” label.

G123-G2
At least one load-bearing switching/energy-transfer state must simultaneously affect X1 transformation, X2 2ω routing and X3 AC synthesis.

G123-G3
No added full-current 12-V series energy-buffer edge.

G123-G4
The 3.183-J 2ω energy location and current path must be explicit.

G123-G5
Any common-mode/differential-mode, transformer-center-tap, flying-capacitor, split-link or differential-inverter primitive already closed in Files 53–56 is reference material, not a contribution.

G123-G6
Prior-art Gate A occurs before detailed PSIM/state optimization because the integrated single-stage literature is dense.
```

Candidate #10 remains `HOLD / NOT_ASSIGNED`.  
Novelty remains `NOT_ESTABLISHED`.  
PSIM/LTspice remain `NOT EXECUTED / NOT AUTHORIZED` for a proposed topology.

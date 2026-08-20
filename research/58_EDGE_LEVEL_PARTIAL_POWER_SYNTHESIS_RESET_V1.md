# 58 — Edge-Level Partial-Power Synthesis Reset v1

Status date: 2026-08-20  
Role: `EDGE-LEVEL POWER-PATH RESET / PARTIAL-POWER BOUNDS / PRIOR-ART GATE A`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Canonical post-X1 comparison rail: `350 Vdc-class`  
Evidence status: `FIRST-PRINCIPLES + MULTI-ROUTE PRIOR-ART SCREEN`  
Simulation status: `NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File 57 closed the generic `X1/X2/X3` overlap matrix as a topology-generation method. The coordinates remain mandatory for analysis, but merely choosing another overlap does not create a useful research direction.

The new synthesis variable is the fraction of system power processed by each added edge:

```text
Paux = α Pout
```

However, this file deliberately rejects the shortcut:

```text
small active Paux  =>  small converter / low loss
```

A partial-power candidate must also disclose nonactive/apparent processing, current stress, voltage stress, and whether a full-power baseline edge is actually removed.

The main question is:

> Can a reduced-power corrective edge remove or materially relax a full-power baseline burden without recreating comparable VA/RMS stress elsewhere?

---

## 2. Baseline edge map

The normalized A0-like two-stage path is represented as:

```text
E0  12-V source / bus                     ~full power, ~175-A source domain
 |
E1  primary switching edge               full power
 |
E2  HFT isolation / transformation edge  full power
 |
E3  secondary rectification edge         full power
 |
E4  HV DC-link distribution edge         full power
 |
E5  VSI AC-synthesis edge                full power
 |
E6  output filter / AC load edge          full power
```

The single-phase low-frequency buffer is a separate oscillatory edge:

```text
EX2  2ω buffer edge
```

with zero average signed power but nonzero instantaneous and RMS power.

This distinction is important: `average power = 0` does not mean `power rating = 0`.

---

## 3. Required partial-power metrics

Every future auxiliary edge must report at least four normalized quantities.

### 3.1 Active processed-power fraction

```text
αP = Pprocessed,active / Pout
```

For bidirectional corrective paths, use both signed average and average absolute processed power. A zero signed average does not qualify as zero processed power.

### 3.2 Apparent / stress fraction

```text
αS = Sprocessed / Pout
```

where `Sprocessed` is a topology-appropriate VA or nonactive-power stress metric.

### 3.3 Current-domain ratio

```text
αI = Irms,aux / Irms,baseline-edge
```

### 3.4 Voltage-domain ratio

```text
αV = Vstress,aux / Vstress,baseline-edge
```

A candidate is not considered genuinely partial simply because `αP` is low. It must also have a credible reduction in component stress and total loss.

This follows the established distinction in the PPP literature between active processed power and total/nonactive processed power.

---

## 4. Fundamental bound: 12 V → 350 V is a bad location for series partial-power processing

For an ideal series voltage-injection architecture in which a direct path supplies `Vbase` and the auxiliary converter supplies only:

```text
ΔV = Vout - Vbase
```

while carrying the output current, the ideal active processed-power fraction is:

```text
αP = ΔV / Vout
   = 1 - Vbase/Vout
```

If the direct base is only the 12-V source and `Vout=350 V`:

```text
αP = 1 - 12/350
   = 0.9657
```

so:

```text
Paux ≈ 1.931 kW
```

This is effectively full-power processing.

Therefore:

```text
12 V -> 350 V series PPC = REJECT AS A PARTIAL-POWER MAINLINE
```

The extreme conversion ratio itself destroys the supposed processed-power advantage.

---

## 5. Isolation boundary makes the upstream limitation stronger

The project requires galvanic isolation between the low-voltage source domain and the output-side power domain.

If the HFT is the only galvanic isolation path, there is no conductive feed-forward path that can bypass it. Therefore essentially all delivered energy must still cross an isolation mechanism.

Formal consequence:

```text
A partial-power auxiliary converter cannot make E2 (the isolation-transfer edge)
process α << 1 of Pout unless another load-bearing isolation path carries the remainder.
```

Thus the project should not expect PPP alone to remove the full-power HFT burden.

Partial-power ideas are structurally more plausible after the isolation/current-reduction boundary, or as local correction/recovery mechanisms around an already-existing full-power isolation path.

---

## 6. Post-X1 DC trim can be genuinely partial, but only after a majority-power path already exists

For a 350-V target:

| Majority-path base voltage | Auxiliary ΔV | ideal αP | auxiliary active power at 2 kW |
|---:|---:|---:|---:|
| 180 V | 170 V | 0.486 | 971 W |
| 250 V | 100 V | 0.286 | 571 W |
| 300 V | 50 V | 0.143 | 286 W |
| 315 V | 35 V | 0.100 | 200 W |
| 325 V | 25 V | 0.071 | 143 W |
| 335 V | 15 V | 0.043 | 86 W |
| 340 V | 10 V | 0.029 | 57 W |

This produces a useful rule:

```text
PPP becomes attractive only when the majority path already lands close to the required state.
```

But this does not remove the full-power isolation/HFT edge that created the majority path. It can only replace or relax a downstream full-power regulation/synthesis burden.

---

## 7. X2 is not a low-power edge under full decoupling

At unity power factor:

```text
pout(t) = P[1 - cos(2ωt)]
```

If the source/main transfer is held at approximately constant average power `P`, the buffer must process:

```text
pbuf(t) = P cos(2ωt)
```

Therefore at `P=2 kW`:

```text
|pbuf|max = 2 kW
pbuf,rms  = 2 kW/sqrt(2) = 1.414 kW
```

Hence:

```text
αP,peak = 1.0
αP,rms  = 0.707
signed average = 0
```

The signed average being zero does not make the APD hardware a low-power converter.

Formal conclusion:

```text
FULL 2ω DECOUPLING MUST NOT BE LABELLED α << 1 PARTIAL POWER
```

X2 can still be advantageous when located at high voltage/reduced current, but not because its instantaneous power rating disappears.

---

## 8. Waveform-correction edge: low active processed power can still hide large VA stress

A more relevant post-X1 use of PPP is to let a low-frequency/coarse main path provide most of the AC voltage and let an auxiliary series edge correct only the residual waveform.

### 8.1 Single square-wave majority path

Take:

```text
vout = Vm sin(ωt)
Vm   = 311.13 V
```

and a coarse main path:

```text
vbase = ±Vb
```

with a series correction:

```text
vaux = vout - vbase
```

For the zero-net-energy choice:

```text
Vb = π Vm / 4 ≈ 244.36 V
```

under a 2-kW unity-PF sinusoidal load, the ideal numerical screen gives approximately:

```text
average signed Paux ≈ 0
average |Paux|      ≈ 462 W ≈ 23.1% Pout
Vaux,rms             ≈ 106.3 V
Iaux,rms             = full load current ≈ 9.09 A
Saux proxy            ≈ 967 VA ≈ 48.3% Pout
```

Thus an architecture can appear to process only about one quarter of the active power while its auxiliary semiconductors still experience roughly one-half-system VA exposure.

This is precisely why `αP` alone is not an admissible ranking metric.

### 8.2 Coarse stepped majority path

As an optimistic topology-independent bound, let the majority path provide the nearest level from:

```text
{0, 175, 350 V}
```

with polarity unfolding, while the auxiliary series edge corrects the residual to the sinusoidal target.

The ideal screen gives approximately:

```text
peak |Vaux|      ≈ 87.5 V
Vaux,rms         ≈ 53.6 V
average |Paux|   ≈ 418 W ≈ 20.9% Pout
Saux proxy       ≈ 487 VA ≈ 24.3% Pout
```

Adding more coarse levels reduces residual correction stress further, but the main path then pays additional taps, devices, commutation states, magnetic complexity, or duplicated voltage sources.

These are bounds only; they are not an actual converter graph.

---

## 9. Prior-art Gate A

### Route A — IEEE / architecture review

Jon Anzola et al.,
“Review of Architectures Based on Partial Power Processing for DC-DC Applications,”
IEEE Access, 2020,
DOI `10.1109/ACCESS.2020.2999062`.

The paper consolidates PPP into differential-power, partial-power-converter, and mixed strategies and confirms that reduced converter-processed power is an established architectural objective.

Gate consequence:

```text
PPP AS A GENERIC IDEA = PRIOR ART / NOT A CANDIDATE CONTRIBUTION
```

### Route B — processed-power/stress falsification

J. R. R. Zientarski et al.,
“Evaluation of Power Processing in Series-Connected Partial-Power Converters,”
IEEE Journal of Emerging and Selected Topics in Power Electronics,
DOI `10.1109/JESTPE.2018.2869370`.

This work explicitly distinguishes active and nonactive processed power and demonstrates that some apparent series partial-power architectures do not actually reduce total processed stress compared with conventional conversion.

Gate consequence:

```text
αP ALONE = INSUFFICIENT
```

The project therefore adopts `αP + αS + αI + αV` as the minimum partial-power ledger.

### Route C — coarse-main + correction inverter prior art

Yuichi Noge, Mingcong Deng, and Mitsuru Miyashita,
“Multilevel Inverter for Grid Interconnection with Square Wave Voltage Sources and Series Connected Active Filter,”
ICAMechS 2018,
DOI `10.1109/ICAMechS.2018.8506740`.

The reported architecture combines gradational/square-wave voltage sources, a series active filter, and unfolding; the authors report a converted-power requirement around one eighth of a conventional inverter in their studied arrangement.

A later journal extension again uses multiple-step voltage sources plus a series active filter and explicitly minimizes active-filter capacity.

Gate consequence:

```text
COARSE MAIN VOLTAGE + SERIES PART-RATED CORRECTION
= ESTABLISHED ARCHITECTURE FAMILY
```

### Route D — master/slave partial-power DC-AC conversion

C. Liu et al.,
“Hybrid SiC-Si DC–AC Topology: SHEPWM Si-IGBT Master Unit Handling High Power Integrated With Partial-Power SiC-MOSFET Slave Unit Improving Performance,”
IEEE Transactions on Power Electronics,
DOI `10.1109/TPEL.2021.3114322`.

This directly establishes the general idea of a bulk-power master stage plus a partial-power high-frequency corrective slave stage in DC-AC conversion.

Gate consequence:

```text
FULL-POWER MASTER + PARTIAL-POWER WAVEFORM-CORRECTION SLAVE
= PRIOR-ART CLASS
```

---

## 10. Edge-level decision matrix

| Edge idea | Processed-power result | Physical value | Novelty/mainline decision |
|---|---|---|---|
| `PP-E1` 12→350 series voltage correction | `αP≈0.966` | poor | STOP |
| `PP-E2` post-X1 300→350 trim | `αP≈0.143` | physically good for regulation trim | generic PPC prior art; reference only |
| `PP-E3` full 2ω APD | peak `α=1`, rms `0.707` | useful only because current domain is lower | not a low-power edge |
| `PP-E4` square main + series correction | active ~0.23 but VA ~0.48 | conditional | generic prior art |
| `PP-E5` coarse multilevel main + residual correction | can reach ~0.2 active and ~0.24 VA in ideal 3-level bound | physically interesting | generic architecture prior art; exact graph required for any future claim |
| `PP-E6` commutation/leakage/Coss recovery edge | potentially very small energy fraction | potentially high-value | already mature R2/active-clamp/snubber region in this project |
| `PP-E7` mismatch/differential processing between modules | α can scale with mismatch | useful for modular mismatch | does not directly solve present single-source majority-power burden |

---

## 11. Main conclusion

Partial-power processing is useful for this project as a **power-path accounting discipline**, but not as a new topology family by itself.

Three hard conclusions now apply:

```text
1. The 12→350-V / isolation edge cannot be made genuinely partial merely by reconnecting a converter.
2. Full single-phase 2ω decoupling is not a low-power function; its peak buffer power remains Pout.
3. Post-X1 waveform/regulation correction can be partial, but the generic master/slave and series-active-filter forms are already established and must be judged by VA/RMS stress, not active power alone.
```

Therefore File 58 does NOT assign Candidate #10.

---

## 12. Immediate next

The next synthesis step must become A0-specific rather than another generic architecture search:

```text
A0 EDGE-LOSS / REMOVABILITY TARGET SELECTION
```

For each real A0 majority-power edge, quantify:

```text
baseline watt loss or bounded loss
edge current/voltage domain
whether the edge is physically removable
what function would be lost if removed
minimum power/VA required by any replacement edge
closest prior art for that specific replacement
```

Priority should be given to a replacement only when:

```text
removed full-power loss > added partial-edge loss + interaction loss
```

and the replacement does not merely shift the same current/VA stress into another component.

The first target-selection artifact should rank at least:

```text
primary conduction edge
primary commutation/snubber edge
HFT transfer edge
secondary rectification edge
HV-link/VSI switching edge
2ω buffer edge
```

Candidate #10 remains `HOLD / NOT_ASSIGNED`.
Novelty remains `NOT_ESTABLISHED`.
PSIM/LTspice remain unauthorized for the generic PP-E1…PP-E7 classes.
# 57 — G123-A Triple-Overlap State Falsification and Gate A v1

Status date: 2026-08-20  
Role: `O123 ACTUAL-GRAPH / STATE-DOF FALSIFICATION / 2ω INTERACTION / PRIOR-ART GATE A`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Canonical post-X1 comparison rail: `350 Vdc-class`  
Evidence status: `FIRST-PRINCIPLES + MULTI-ROUTE PRIOR-ART SCREEN`  
Simulation status: `NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

Files 53–56 screened the obvious pairwise coordinate overlaps:

```text
O13 = X1+X3, X2 separate
O23 = X1 separate, X2+X3
O12 = X1+X2, X3 separate
```

The final generic coordinate partition from File 52 is:

```text
O123 = X1 + X2 + X3
```

This file does not accept a loose marketing definition of “single-stage” or “integrated.” A genuine triple-overlap candidate must show a load-bearing switching-state degree of freedom that participates in all three functions:

```text
X1 = main 12-V-to-reduced-current power transformation
X2 = 2ω energy routing / storage
X3 = 220-Vac synthesis
```

If the same semiconductor package is merely time-multiplexed between separate X1 and X2 states, while another network performs X3, the result is classified as `PAIRWISE/TIME-MULTIPLEXED INTEGRATION`, not a new triple-state primitive.

At 2 kW and 50 Hz the unavoidable single-phase buffer requirement remains:

```text
E2ω,pk = P/(4πf) = 3.183 J
E2ω,pp = 6.366 J
```

No PSIM is authorized unless a graph survives both the state-DOF and prior-art gates.

---

## 2. G123-A1 — center-tapped HFT + common-mode buffer + secondary matrix converter

### 2.1 Normalized graph

```text
12-V source
   |
primary full bridge
   |
center-tapped HFT
   |\
   | \---- small LC / Cbuf power-decoupling branch
   |
secondary matrix / cycloconverter
   |
AC filter
   |
220 Vac
```

Functional assignment:

```text
X1 = primary differential HF excitation + HFT transfer
X2 = common-mode / center-tap controlled buffer-current path
X3 = secondary matrix/cycloconverter AC synthesis
```

At the hardware/block level this appears to be `X1+X2+X3`.

### 2.2 Primary two-level full-bridge state table

Let the two bridge-leg pole states be `SA, SB ∈ {0,1}`, with pole voltages `0` or `Vdc`.

Define:

```text
vdiff = Vdc(SA-SB)
vcm   = Vdc(SA+SB)/2
```

Then:

| SA | SB | vdiff | vcm | dominant function |
|---:|---:|---:|---:|---|
| 0 | 0 | 0 | 0 | zero/common-mode state |
| 1 | 0 | +Vdc | Vdc/2 | active transformer excitation |
| 0 | 1 | -Vdc | Vdc/2 | active transformer excitation |
| 1 | 1 | 0 | Vdc | zero/common-mode state |

Critical result:

```text
active differential states:
  vdiff = ±Vdc
  vcm is fixed at Vdc/2

zero states:
  vdiff = 0
  vcm can be selected as 0 or Vdc
```

Therefore, in a conventional two-level full bridge, the independent common-mode control authority used for X2 comes mainly from zero-state allocation, while the active differential states used for X1 do not provide an independent X2 command.

This means the apparent X1+X2 overlap is fundamentally time-multiplexed at the switching-state level.

The secondary matrix converter then performs X3 from the HF-link pulses.

Strict state-DOF result:

```text
G123-A1 STRICT TRIPLE-STATE OVERLAP = FAIL
classification = pairwise/time-multiplexed shared hardware
```

The graph can still be physically excellent, but it is not evidence of a new three-function switching primitive.

---

## 3. Time-sharing lower bound

Suppose a fraction `β` of each switching-period control authority must be reserved for buffer/common-mode steering, leaving at most:

```text
δtransfer <= 1 - β
```

for the main differential transfer state.

For fixed transferred charge/power and voltage, the ideal rectangular-current RMS lower bound scales approximately as:

```text
Irms,new / Irms,base >= 1/sqrt(1-β)
```

and the corresponding conduction-exposure factor is:

```text
I²R factor >= 1/(1-β)
```

Examples:

| β reserved for X2 steering | minimum Irms multiplier | minimum I²R exposure multiplier |
|---:|---:|---:|
| 0.10 | 1.054 | 1.111 |
| 0.20 | 1.118 | 1.250 |
| 0.30 | 1.195 | 1.429 |
| 0.40 | 1.291 | 1.667 |

This is only a lower-bound scheduling penalty. It does not yet include the buffer-current RMS itself, transformer leakage/ringing, matrix-converter current, or semiconductor switching loss.

At the 350-V reduced-current domain:

```text
main average current scale = 2000/350 = 5.714 A
2ω buffer-current RMS scale = 2000/(sqrt(2)*350) = 4.041 A
```

Thus X2 is not a negligible auxiliary function even after X1 current reduction.

---

## 4. G123-A2 — DAB/direct-AC bridge with simultaneous differential/common-mode modulation

A stronger triple-overlap interpretation is to use a DAB/direct-AC structure in which the active bridges provide multiple modulation coordinates:

```text
primary/secondary bridge phase relation
  -> X1 net HF power transfer

AC-side differential component
  -> X3 output voltage/current synthesis

AC-side common-mode / buffer component
  -> X2 2ω energy routing
```

Normalized graph:

```text
12-V source
   |
active bridge
   |
HFT / HF transfer inductance
   |
AC-side active bridge / direct AC port
   |\
   | \-- buffer energy state
   |
AC filter
   |
220 Vac
```

This is the strongest admissible `G123-A` concept because the same bridge timing variables can influence main transfer, AC differential output and decoupling energy within one switching-period control law.

However, the three controls are still not free degrees of freedom. They must share:

```text
switching-period state time
transformer volt-seconds
HF-link current
semiconductor current rating
ZVS/commutation margin
```

so any triple integration must pay an `INTERACTION_NEW` term in RMS current, modulation headroom or circulating energy.

---

## 5. Multi-route Gate A

### Route A — IEEE-direct / exact architecture search

The generic triple-functional region is already occupied by established isolated single-stage converter work.

1. Nagisa Takaoka, Hiroki Takahashi, Jun-ichi Itoh, “Isolated Single-Phase Matrix Converter Using Center-Tapped Transformer for Power Decoupling Capability,” IEEE Transactions on Industry Applications, 2018, DOI `10.1109/TIA.2017.2774760`.

Structural match:

```text
full bridge inverter
+ high-frequency center-tapped transformer
+ matrix converter
+ common-mode transformer voltage
+ small buffer capacitor
+ no additional APD switches
```

This directly occupies the G123-A1 hardware graph. The published control separates differential transformer excitation from common-mode buffer control while the matrix converter synthesizes the single-phase AC output.

2. Davide Gottardo et al., “Single Stage Dual Active Bridge AC-DC Converter with Active Power Decoupling,” SPEEDAM 2018, DOI `10.1109/SPEEDAM.2018.8445410`.

Structural match:

```text
isolated single-stage DAB/direct-AC conversion
+ active power decoupling on AC side of transformer
+ only two full bridges
+ no additional active APD component
+ differential/common-mode bridge-voltage use
```

This occupies the stronger G123-A2 functional region.

Route-A result:

```text
GENERIC ISOLATED SINGLE-STAGE + APD + DIRECT AC SYNTHESIS
= ESTABLISHED PRIOR-ART REGION
```

### Route B — semantic architecture/behavior search

Independent semantic search recovered the same two classes plus related DC/AC DAB ripple-steering work:

- Gottardo et al. 2018: single-stage DAB with AC-side APD and shared bridge functions.
- Takaoka/Takahashi/Itoh: center-tapped transformer common-mode buffer + matrix converter.
- Jiang You et al., “An Active Power Decoupling Method for Single Phase DC/AC DAB Converters,” IEEE Access, 2019: existing primary bridge switches plus an integrated ripple-reduction network controlled through bridge duty, without additional switching devices.

Route-B result:

```text
shared bridge / HFT / buffer-state integration is not an unexplored mechanism.
```

### Route C — academic/OpenAlex cross-check

OpenAlex/Sider search recovered:

- Jiang You et al. 2019, DC/AC DAB active power decoupling.
- “Floating Capacitor Integrated DAB for Single-Phase, Single-Stage PFC in Wireless Battery Charging Application,” IEEE OJPEL 2023, showing continued integration of power-pulsation buffering into a DAB/HF-link structure.
- modern integrated power-decoupling and single-stage DAB literature across EV chargers and microinverters.

Route-C result:

```text
DAB/HF-link + APD integration is a mature and actively developed research family.
```

---

## 6. Gate-A decision

### G123-A1

```text
ENERGY FEASIBILITY = PASS
PAIRWISE HARDWARE SHARING = PASS
STRICT ONE-STATE X1+X2+X3 OVERLAP = FAIL
PRIOR ART = SAME / NEAR GRAPH
PSIM AS PROPOSED TOPOLOGY = NO
```

Reason:

> The conventional two-level bridge does not provide independent X1 differential transfer and X2 common-mode control in the same active state; the useful control is largely time-multiplexed between active and zero states, while X3 is performed by the secondary matrix stage. The exact hardware family is already prior art.

### G123-A2

```text
FUNCTIONAL TRIPLE INTEGRATION = PHYSICALLY PLAUSIBLE / ESTABLISHED
STRICT NOVELTY = STOP
PRIOR ART = SAME CLASS / SAME MECHANISM / NEAR GRAPH
PSIM AS PROPOSED TOPOLOGY = NO
```

Reason:

> Single-stage isolated DAB/direct-AC converters with active power decoupling and shared differential/common-mode bridge functions have already been published. Additional modulation freedom does not create a topology contribution unless a future graph changes the load-bearing energy path itself.

---

## 7. Coordinate-matrix status after File 57

The File-52 generic coordinate partitions now have representative closure results:

```text
O0   = X1 | X2 | X3              -> baseline/reference
O13  = X1+X3 | X2                -> obvious graph prior-art rich
O23  = X1 | X2+X3                -> obvious graphs prior-art rich
O12  = X1+X2 | X3                -> obvious graphs prior-art rich
O123 = X1+X2+X3                  -> generic triple integration prior-art rich / state-DOF constrained
```

This does NOT prove that every circuit graph in these coordinate classes is known.

It does establish that simple coordinate overlap by itself is no longer a useful novelty generator.

Formal conclusion:

```text
X1/X2/X3 OVERLAP MATRIX = CLOSED FOR GENERIC OVERLAP SYNTHESIS
```

The coordinates remain mandatory analysis tools, but the next candidate search must introduce a new edge-level power-routing idea rather than merely choosing another overlap partition.

---

## 8. New synthesis rule derived from the failures

Future candidate generation must be edge-level rather than block-level.

A new candidate must specify:

```text
1. which exact majority-power edge is removed or reduced;
2. what fraction of total power each added edge processes;
3. whether X2 energy crosses the HFT/main path or bypasses it;
4. whether a claimed shared switch acts simultaneously or only by time multiplexing;
5. the unavoidable RMS/current/volt-second penalty caused by sharing;
6. the closest prior-art graph before simulation.
```

A particularly important new variable is the processed-power fraction `α` of an auxiliary mechanism:

```text
Paux = α Pout
```

If a new edge only processes a fraction of the 2-kW power instead of being another full-power conversion stage, its conduction, magnetic and semiconductor rating may scale materially differently from the full-power overlap candidates screened so far.

This does not itself define Candidate #10.

---

## 9. Immediate next

Do not continue by inventing another X1/X2/X3 overlap label.

Immediate next research task:

```text
EDGE-LEVEL / PARTIAL-POWER SYNTHESIS RESET
```

Construct a matrix of candidate power paths classified by:

```text
majority-power edge
partial-power edge
processed-power fraction α
voltage/current domain of each edge
which PG1–PG4 burden is actually removed
which new interaction loss is created
```

The first gate must ask whether an auxiliary path can process materially less than full 2-kW power while genuinely reducing a full-power baseline burden.

Candidate #10 remains `HOLD / NOT_ASSIGNED`.
Novelty remains `NOT_ESTABLISHED`.
PSIM/LTspice remain unauthorized for G123-A.

# 22 — ASP-2000 A0 R52 Manufactured-Copper Correction

Status date: 2026-08-19  
Role: `A0 PCB MANUFACTURING-EVIDENCE CORRECTION`  
Evidence status: `R52 PCB MANUFACTURING SPEC + EXISTING 2D GEOMETRY MODEL`  
Hardware resistance status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark correction`

## 1. Purpose

Correct the A0 positive-distribution resistance model after discovering a direct manufacturing specification for the same R52 PCB/Gerber.

The earlier PcbDoc stack metadata was treated as if it were the manufactured copper thickness. That assumption is now superseded.

---

## 2. Conflicting evidence

### Earlier design metadata

PcbDoc stack metadata exposed approximately:

```text
Top copper ≈1.4 mil ≈35.56 µm
Bottom copper ≈1.4 mil ≈35.56 µm
```

This value drove the first sheet-resistance model.

### Direct R52 manufacturing specification

`PB-2200-0038-D_R52_231206_PCB製作規格.xlsx` is explicitly tied to:

```text
GERBER = PB-2200-0038-D_R52.RAR
```

and specifies:

```text
board material = FR4
board thickness =1.6 mm
layer count =2
base copper =2.0 oz
finished copper thickness >82 µm
surface treatment = lead-free HASL
```

Formal evidence priority:

```text
manufacturing specification for the same R52 Gerber
>
EDA design-stack metadata
```

for as-built conductor-thickness bounds.

---

## 3. Sheet-resistance correction

Using `82 µm` as the conservative minimum finished-copper thickness:

```text
R_sheet,1layer,max ≈0.210 mΩ/square
R_sheet,2layer,ideal,max ≈0.105 mΩ/square
```

The former 35.56 µm model used approximately:

```text
R_sheet,1layer≈0.485 mΩ/square
```

Thus the prior geometry-only resistances are rescaled by approximately:

```text
35.56 /82 ≈0.434
```

for the same 2D current-spreading geometry.

Because the specification states `>82 µm`, these corrected copper-only resistances are conservative upper bounds within the geometry model.

---

## 4. Corrected A0 positive PCB bounds

### BAT+ common distribution

```text
OLD:
R≈0.249 mΩ
P@175.4A≈7.67 W

CURRENT:
R≤~0.108 mΩ
P@175.4A≤~3.32 W
average modeled drop≤~18.9 mV
```

### T1 local feed PCB

```text
OLD:
R≈0.351 mΩ
P@87.7A≈2.70 W

CURRENT:
R≤~0.152 mΩ
P@87.7A≤~1.17 W
```

### T2 local PCB excluding J8

```text
OLD:
R≈0.144 mΩ
P@87.7A≈1.10 W

CURRENT:
R≤~0.0624 mΩ
P@87.7A≤~0.48 W
```

### Partial positive PCB input-referred equivalent

```text
OLD:
R_eq≈0.373 mΩ
P@175.4A≈11.5 W

CURRENT:
R_eq≤~0.162 mΩ
P@175.4A≤~4.98 W
```

All current values remain:

```text
MANUFACTURING_GEOMETRY_BOUND / NOT HARDWARE-MEASURED
```

---

## 5. Research-conclusion correction

The former wording that BAT+ PCB/common copper could be approximately comparable to the entire main-MOS conduction bucket was based on the superseded 35.56 µm assumption.

Current comparison scale:

```text
partial positive PCB geometry bound ≤~4.98 W
main 20-MOS 25°C datasheet conduction bound ≈12.3 W
battery-interface 7-MOS 25°C datasheet bound ≈7.47 W
```

These still use different evidence classes and must not be summed or scalar-ranked as measured losses.

Decision:

```text
PCB distribution = MATERIAL / MUST MEASURE
PCB distribution = NOT PROVEN DOMINANT
```

The physical preference for a short full-current path remains valid, but the quantitative case for making PCB copper the first dominant loss target is weakened.

---

## 6. What this correction does not include

The corrected copper bound still excludes or does not close:

```text
connector/contact resistance
fuse element/contact resistance
J8 external conductor/contact
hot-copper resistivity rise
current-crowding details beyond the existing 2D model
assembly-specific solder / bus reinforcement
B-return path resistance
```

Therefore direct Kelvin/mV measurements remain required.

---

## 7. Measurement consequence

Use the corrected manufacturing bounds for geometry sanity checks:

```text
BAT+ common ≤~0.108 mΩ
T1 local ≤~0.152 mΩ
T2 PCB excl. J8 ≤~0.0624 mΩ
partial positive PCB ≤~0.162 mΩ
```

If measured segment resistance exceeds the relevant geometry-only bound materially, investigate non-copper terms, hot operation, current bottlenecks or boundary mismatch rather than immediately treating the manufacturing specification as wrong.

---

## 8. Formal supersession

Superseded model:

```text
PcbDoc 35.56 µm as manufactured copper
→ old R/P bounds
```

Current model:

```text
R52 base copper 2 oz
R52 finished copper >82 µm
→ corrected manufacturing-geometry bounds
```

Authoritative current-state files:

```text
research/08_DECISION_LOG.md
research/13_ASP2000_A0_NUMERICAL_LOSS_BOUNDS.md
research/14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
research/15_ASP2000_A0_KELVIN_MEASUREMENT_PROTOCOL.md
research/RESEARCH_STATE.md
```

---

## 9. Formal status

```text
R52 manufacturing spec identity           = VERIFIED
same-Gerber link PB-2200-0038-D_R52.RAR   = VERIFIED
base copper 2.0 oz                        = VERIFIED_FROM_MANUFACTURING_SPEC
finished copper >82 µm                    = VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm as-built assumption          = SUPERSEDED
BAT+ common PCB bound                     = ≤~3.32 W / NOT_MEASURED
partial positive PCB bound                = ≤~4.98 W / NOT_MEASURED
PCB dominance                             = NOT_ESTABLISHED
A0 measured distribution loss             = OPEN
candidate superiority                     = NOT_ESTABLISHED
novelty                                   = NOT_ESTABLISHED
```

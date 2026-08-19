# 14 — ASP-2000 A0 Distribution Resistance and Kelvin Measurement Gate

Status date: 2026-08-19  
Role: `A0 DISTRIBUTION-LOSS / MEASUREMENT GATE`  
Evidence status: `PCB PRIMITIVE RECONSTRUCTION + 2D SHEET MODEL + DEVICE/FUNCTION TRACE`  
Measurement status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

Quantify/bound the real high-current distribution and return losses surrounding ASP-2000 A0 before assigning loss to the magnetic X1 mechanism.

Raw product files remain outside the public repository.

Key distinction:

```text
ordinary distribution / protection / sensing loss
!=
intrinsic X1 conversion loss
```

A candidate cannot create a topology advantage by deleting required product functionality only on its side of the comparison.

---

## 2. BAT+ distribution — VERIFIED GEOMETRY

PcbDoc identifies:

```text
3 large BAT+ connector pads
8 main fuse-input pads
16 BAT+ stitching vias
large Top/Bottom BAT+ polygons
```

Fuse grouping:

```text
T1: F2 F3 F5 F6
T2: F7 F8 F9 F10
```

PCB copper:

```text
Top ≈ 1.4 mil ≈ 35.56 µm
Bottom ≈ 1.4 mil ≈ 35.56 µm
R_sheet,1layer ≈ 0.485 mΩ/square
```

Converged nominal-copper 2D model:

```text
R_BAT+,common,geometry ≈ 0.249 mΩ
P@175.4A ≈ 7.67 W
average modeled drop ≈ 43.7 mV
```

Status:

```text
GEOMETRY_MODEL / NOT_MEASURED
```

The balanced model predicts different average drops to the T1/T2 fuse groups, so equal current sharing must be measured rather than assumed.

---

## 3. Post-fuse local paths

### T1 local PCB

```text
R_T1local,PCB ≈ 0.351 mΩ
P@87.7A ideal share ≈ 2.70 W
```

### T2 local PCB excluding J8

```text
R_T2local,PCB,excludingJ8 ≈ 0.144 mΩ
P@87.7A ideal share ≈ 1.10 W
```

Two same-net `J8` power terminals are separated by about 93 mm without an ordinary PCB polygon spanning the complete gap.

```text
external high-current link intent = STRONGLY_SUPPORTED
exact J8 conductor = OPEN
R_J8 = MEASUREMENT_NEEDED
```

Partial positive PCB-only input-referred model under ideal 50/50 T1/T2 sharing:

```text
R_eq,positive-PCB,partial ≈ 0.373 mΩ
P@175.4A ≈ 11.5 W
```

This excludes connector/contact, fuse elements, J8, hot copper and assembly reinforcement.

---

## 4. B↔BAT- battery-interface bank — FUNCTION UPDATED

Seven parallel `CSD18510KCS` devices connect:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

Verified orientation:

```text
Source → B
Drain → BAT-
```

Verified gate bias:

```text
12VP → individual 68.1 Ω → Gate
Gate → individual 47.5 kΩ → B
```

No independent MAIN-board PWM/enable command was found.

Function status:

```text
reverse-polarity / ideal-diode-style battery interface = STRONGLY_SUPPORTED
independent full-disconnect role = NOT_SUPPORTED_BY_PRESENT_CIRCUIT
```

U4 (`LM2904`) monitors `B` relative to `BAT-` and exports `BOCP`:

```text
B↔BAT- drop sensing → BOCP = VERIFIED
BOCP over-current / abnormal-drop protection role = STRONGLY_SUPPORTED
exact threshold / control response = OPEN
```

Detailed function evidence is authoritative in:

```text
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
```

The earlier completely-OPEN functional wording for this bank is superseded.

---

## 5. Seven-MOS loss scale — NOT MEASURED

Using official device max `RDS(on)=1.7mΩ @ VGS=10V` only as a boundary:

```text
7 ideal parallel → Req≈0.243mΩ
P@175.4A≈7.47W
```

This is:

```text
DATASHEET_BOUND / NOT_MEASURED
```

Actual battery-interface loss is to be measured directly:

```text
P_batteryInterface = I_source × ΔV(B↔BAT-)
```

with MOS temperature and `12VP` recorded.

---

## 6. Fair-comparison boundary

Two valid contracts:

```text
Contract P — product level
match required reverse-polarity/equivalent ideal-diode behavior,
required current/fault information,
fusing/fault isolation,
and count their losses.

Contract C — core converter
exclude battery-interface protection/sensing overhead
from A0/A1/candidate equally.
```

Forbidden:

```text
remove Q39...Q65 functionality
→ count removed watts as X1/topology gain
```

A lower-loss equivalent product interface is allowed, but its benefit is classified first as battery-interface/protection engineering improvement.

---

## 7. Kelvin segmentation

```text
M0 BAT+ terminal → each fuse input
M1 each main fuse input → output
M2 T1 fuse-output node → T1 center tap
M3 J8 left → J8 right
M4 J8 right → T2 center tap
M5 B ↔ BAT- battery-interface bank
M6 B-return distribution if separately accessible
```

Minimum currents:

```text
I_source
I_T1
I_T2
```

For a simple series segment:

```text
P_segment = I_segment × ΔV_segment
R_segment = ΔV_segment / I_segment
```

For the multi-terminal BAT+ distribution:

```text
P_BAT+ = Σ I_k ΔV_k
```

not `I_source × one arbitrary fuse-input drop`.

---

## 8. M5 measurement extension

For the newly classified battery interface record:

```text
I_source
ΔV(B↔BAT-)
12VP
MOS-bank temperature
BOCP voltage/state if safely accessible
```

A load sweep may test correlation between B↔BAT- drop and BOCP, but an intentional protection-trip test requires a separate approved hardware-safety procedure.

---

## 9. Distribution loss reconstruction

First measured product-level distribution total:

```text
P_distribution,meas =
    P_BAT+common
  + ΣP_fuse
  + P_T1local
  + P_J8
  + P_T2local
  + P_BreturnCopper
  + P_batteryInterface
```

Do not mix this directly with magnetic/core loss until the comparison boundary is explicitly declared.

---

## 10. Gate logic

```text
A0 measured distribution + battery-interface loss
↓
A0 main switch + HFT dynamic loss
↓
separate product-interface overhead from intrinsic X1 loss
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized magnetic benchmark
```

Current status:

```text
BAT+ geometry bound = ESTABLISHED / NOT_MEASURED
T1/T2 local geometry bounds = ESTABLISHED / NOT_MEASURED
J8 resistance = OPEN
B↔BAT- power boundary = VERIFIED
reverse-polarity / ideal-diode role = STRONGLY_SUPPORTED
B↔BAT- sensing → BOCP = VERIFIED
battery-interface measured loss = OPEN
A0 total BAT→X1 loss = OPEN
A1 = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
```
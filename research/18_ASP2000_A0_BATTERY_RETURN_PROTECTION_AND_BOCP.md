# 18 — ASP-2000 A0 Battery-Return Protection and BOCP Function

Status date: 2026-08-19  
Role: `A0 BATTERY-INTERFACE FUNCTION / FAIR-BOUNDARY CORRECTION`  
Evidence status: `DIRECT SCHDOC CONNECTIVITY + COMPILED-PCB POWER-NET CONFIRMATION`  
Hardware waveform status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark/function-boundary evidence`

## 1. Purpose

This document resolves the product-function ambiguity around the seven full-current MOSFETs between the ASP-2000 R52 main low-side return `B` and battery negative.

Previous research notes correctly established the power boundary:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

but left the exact function as `OPEN`.

The present SchDoc trace resolves the gate-bias and BOCP sensing architecture far enough to classify the function without pretending that the control-board firmware or exact trip threshold is known.

Raw company source files remain outside this public repository.

---

## 2. Seven-device power orientation — VERIFIED

All seven devices are annotated:

```text
Q39 Q40 Q41 Q42 Q63 Q64 Q65
= CSD18510KCS
```

SchDoc + PCB mapping establishes:

```text
Drain  → BAT-
Source → B
```

for all seven positions.

Therefore they form one parallel low-side battery-return interface, not seven series devices and not seven independently switched branches.

The main converter return current reaches battery negative through this parallel bank.

---

## 3. Gate-bias architecture — VERIFIED

Each MOS gate has the same local network.

Examples/generalized form:

```text
12VP
↓
68.1 Ω individual gate resistor
↓
MOS Gate
↓
47.5 kΩ Gate-to-Source pull-down
↓
B
```

Direct component mapping:

```text
Q39: R145 = 68R1, R144 = 47K5
Q40: R147 = 68R1, R146 = 47K5
Q41: R149 = 68R1, R148 = 47K5
Q42: R151 = 68R1, R150 = 47K5
Q63: R184 = 68R1, R183 = 47K5
Q64: R186 = 68R1, R185 = 47K5
Q65: R188 = 68R1, R187 = 47K5
```

The seven `68R1` resistor inputs are tied to the same `12VP` power rail.

No independent PWM / enable command is present between `12VP` and these seven individual gates in the reconstructed MAIN-board circuit.

Research consequence:

```text
seven-MOS bank = common continuously-enhanced battery-return interface when 12VP is present
```

not:

```text
seven independently commanded disconnect switches
```

The exact startup behavior still depends on how `12VP` itself rises and is controlled.

---

## 4. Reverse-polarity / ideal-diode-style interpretation — STRONGLY SUPPORTED

For the annotated N-channel MOS devices, the verified orientation is:

```text
normal return direction:
B → BAT-

MOS terminals:
Source = B
Drain  = BAT-
```

This orientation places the intrinsic body-diode direction in the normal return direction while the enhanced MOS channel bypasses the diode with low resistance when the gate is biased from `12VP`.

That is structurally consistent with a low-side reverse-polarity / ideal-diode-style battery interface:

```text
correct polarity
→ initial allowed return direction
→ gate bias enhances parallel MOS bank
→ low conduction drop

reverse polarity
→ intrinsic diode orientation blocks the opposite battery-current direction
```

Status:

```text
low-side reverse-polarity / ideal-diode-style function = STRONGLY SUPPORTED
```

A separate commandable full-disconnect function is **not supported by the present seven-MOS topology alone**, because the body-diode path remains in the normal return direction when the gates are not enhanced.

This does not exclude the possibility that some other product element provides system disconnect functionality.

---

## 5. BOCP sensing path — VERIFIED

The same `B ↔ BAT-` boundary is explicitly monitored by U4 (`LM2904`).

Reconstructed comparator/amplifier section:

```text
U4 pin 5 (+ input) → B

BAT-
↓
R153 = 1 kΩ
↓
U4 pin 6 (- input)
↑
R152 = 22.1 kΩ feedback from U4 output

U4 pin 7 output
↓
R154 = 100 Ω
↓
BOCP
↓
CN4A pin 6
```

Therefore the directly sensed electrical quantity is based on:

```text
V_B - V_BAT-
```

with feedback/hysteresis around the U4 decision point.

When the seven MOSFETs are enhanced and operating in the ohmic region:

```text
V_B-BAT- ≈ I_source × R_bank,hot
```

so the battery-return MOS bank is also a natural current/fault-sensing element.

Status:

```text
B↔BAT- voltage-drop sensing feeding BOCP = VERIFIED
BOCP exact firmware/control interpretation = OPEN
exact trip threshold / output-state meaning = OPEN
```

The signal name `BOCP` and the measured quantity are strongly consistent with an over-current / abnormal-return-drop protection role, but the acronym expansion and final control action are not promoted to verified without the control-board logic/firmware.

---

## 6. Function classification

### VERIFIED

```text
7 × CSD18510KCS are physically parallel between B and BAT-
Drain → BAT-
Source → B
all seven gates are biased from common 12VP through individual 68.1 Ω resistors
all seven gates have individual 47.5 kΩ pull-downs to B
U4 senses B relative to BAT-
U4 output is exported as BOCP to CN4A pin 6
```

### STRONGLY SUPPORTED

```text
low-side reverse-polarity / ideal-diode-style battery interface
B↔BAT- MOS-bank drop reused as battery-current / fault information
BOCP participates in over-current / abnormal-drop protection logic
```

### NOT SUPPORTED BY CURRENT EVIDENCE

```text
independently commanded battery disconnect by Q39...Q65
PWM operation of Q39...Q65 during normal conversion
seven separate current branches with separate control
```

### OPEN

```text
exact BOCP trip threshold
exact BOCP active polarity
control-board response to BOCP
whether BOCP distinguishes over-current, short-circuit, MOS-not-enhanced, reverse condition, or multiple conditions
12VP startup/shutdown sequence
```

---

## 7. Loss consequence

The previously established datasheet boundary remains useful only as a scale reference.

For `CSD18510KCS`:

```text
RDS(on),max @ VGS=10 V = 1.7 mΩ
```

Seven ideal parallel devices:

```text
R_eq,25C,max ≈ 1.7 mΩ / 7 ≈ 0.243 mΩ
```

At the research scaling current `175.4 A`:

```text
P_25C,bound ≈ I²R ≈ 7.47 W
```

Status:

```text
DATASHEET BOUND / NOT MEASURED
```

The actual product loss must still be obtained from the M5 hardware measurement:

```text
P_batteryInterface,meas
= I_source × ΔV(B↔BAT-)
```

with temperature recorded.

---

## 8. Benchmark-boundary correction

The seven-MOS loss is now classified primarily as a **battery-interface protection/sensing loss**, not as the magnetic X1 conversion mechanism itself.

Fair comparisons must use one of two explicit contracts.

### Contract P — product-level comparison

Every architecture must provide matched required functions such as:

```text
reverse-polarity protection / equivalent ideal-diode behavior
battery-current or abnormal-return-drop protection sensing
required fusing / fault isolation
```

Implementation may differ, but its loss must be counted.

### Contract C — core-converter comparison

If the research question is only the intrinsic conversion path:

```text
battery-interface protection/sensing overhead
```

may be excluded **only when excluded from A0, A1 and every candidate equally**.

Forbidden comparison:

```text
Candidate removes Q39...Q65 functionality
→ counts ~7 W saving
→ claims new X1/topology advantage
```

A candidate may legitimately reduce this loss while preserving the same product function, but that saving is classified first as:

```text
battery-interface / protection engineering improvement
```

not evidence by itself of a new power-conversion topology.

---

## 9. Measurement correction

M5 remains a priority measurement:

```text
BAT- terminal ↔ B main-return reference
```

Record synchronously:

```text
I_source
ΔV_B-BAT-
12VP
MOS-bank temperature
BOCP state/voltage if safely accessible
```

Then:

```text
R_bank,hot = ΔV / I_source
P_bank     = I_source × ΔV
```

A load sweep can later test whether BOCP changes with the bank drop, but no trip test should be performed without an approved hardware-safety procedure.

---

## 10. Research consequence for A1

A1 no longer needs to preserve a vague `disconnect` assumption for this specific seven-MOS block.

Instead, its matched product-function requirement should be written as:

```text
matched battery-interface protection/sensing function
with reverse-polarity behavior and equivalent fault/current information as required
```

The A1 implementation is free to use a lower-loss realization.

This sharpens the central topology question:

```text
A0 product-interface loss
vs
A0 magnetic X1 loss
```

must be separated before deciding that the X1 physics itself should be replaced.

---

## 11. Formal status

```text
B↔BAT- seven-MOS power boundary                = VERIFIED
gate bias from 12VP through 7 × 68.1 Ω         = VERIFIED
7 × 47.5 kΩ gate-source pull-downs to B        = VERIFIED
independent disconnect command on this bank     = NOT FOUND / NOT SUPPORTED
reverse-polarity / ideal-diode-style role       = STRONGLY SUPPORTED
U4 senses B relative to BAT-                    = VERIFIED
BOCP exported to CN4A pin 6                     = VERIFIED
over-current / abnormal-drop protection role    = STRONGLY SUPPORTED
exact BOCP threshold/control response            = OPEN
battery-interface measured loss                 = OPEN
A0 total BAT→X1 loss                             = OPEN
A1                                               = BLOCKED UNTIL A0 LOSS LOCALIZATION
Candidate #10                                    = NOT ASSIGNED
Novelty                                          = NOT ESTABLISHED
```

This document supersedes earlier wording that left the Q39...Q65 product role completely unclassified.
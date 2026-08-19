# 18 — ASP-2000 A0 Battery-Return Protection and BOCP Function

Status date: 2026-08-19  
Role: `A0 BATTERY-INTERFACE FUNCTION / FAIR-BOUNDARY CORRECTION`  
Evidence status: `SCHDOC + COMPILED-PCB + ASP PRODUCT SPEC`  
Hardware waveform status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark/function-boundary evidence`

## 1. Purpose

This document resolves the product-function ambiguity around the seven full-current MOSFETs between the ASP-2000 R52 main low-side return `B` and battery negative.

Verified power boundary:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

The evidence now comes from two independent directions:

```text
1. MAIN-board SchDoc / compiled-PCB structure
2. ASP-series product specification
```

The product specification explicitly lists:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Therefore reverse-polarity protection is no longer merely inferred to exist at product level.

Raw company source files remain outside this public repository.

---

## 2. Seven-device power orientation — VERIFIED

All seven devices are annotated:

```text
Q39 Q40 Q41 Q42 Q63 Q64 Q65
= CSD18510KCS
```

SchDoc + PCB mapping establishes for all seven:

```text
Drain  → BAT-
Source → B
```

They form one parallel low-side battery-return interface, not seven series devices and not seven independently switched branches.

The main converter return current reaches battery negative through this parallel bank.

---

## 3. Gate-bias architecture — VERIFIED

Every MOS gate has the same network:

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

The seven 68.1 Ω resistor inputs are tied to common `12VP`.

No independent MAIN-board PWM / enable command is present between `12VP` and these seven gates.

Thus, when 12VP is established:

```text
seven-MOS bank = common enhanced low-resistance battery-return interface
```

not:

```text
seven separately commanded disconnect switches
```

The detailed 12VP startup/shutdown sequence remains open.

---

## 4. Reverse-polarity function — PRODUCT LEVEL VERIFIED

The ASP standard specification explicitly declares:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Therefore:

```text
ASP product reverse-polarity protection function
= VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
```

The seven-MOS hardware orientation is:

```text
normal return direction:
B → BAT-

MOS terminals:
Source = B
Drain  = BAT-
```

This orientation plus common gate enhancement is structurally consistent with a low-side ideal-diode-style implementation:

```text
correct polarity
→ intrinsic diode permits the intended initial direction
→ 12VP enhances the MOS bank
→ MOS channel reduces normal conduction drop

reverse polarity
→ intrinsic body-diode orientation blocks the opposite battery-current direction
```

Therefore the combined evidence status is:

```text
reverse-polarity protection exists in ASP product
= VERIFIED

Q39...Q65 are a low-side ideal-diode-style implementation of that function
= STRONGLY_SUPPORTED_BY_HARDWARE_STRUCTURE
```

A separate commandable full-disconnect function is not supported by this seven-MOS topology alone because the body-diode path remains in the normal return direction with the gates off.

---

## 5. B / SIG reference relationship — VERIFIED

In the U4 schematic region, the `B` net label and `SIG` reference port are on the same connected wire.

Thus for the BOCP analog section:

```text
B = local signal reference SIG
```

This allows the BOCP voltage to be interpreted relative to the same local reference used by the seven-MOS return bank.

---

## 6. BOCP sensing path — LINEAR AMPLIFIER VERIFIED

The same `B ↔ BAT-` boundary is monitored by U4 (`LM2904`).

Reconstructed channel:

```text
U4 + input → B / SIG

BAT-
↓
R153 = 1.00 kΩ
↓
U4 - input
↑
R152 = 22.1 kΩ negative feedback from U4 output

U4 output
↓
R154 = 100 Ω
↓
BOCP
↓
CN4A pin 6

U4 supply:
V+ → 12VP
V- → -12V
```

Important correction:

```text
this is a closed-loop analog amplifier
NOT a Schmitt/comparator hysteresis interpretation
```

Define:

```text
ΔV_M5 = V_B - V_BAT-
```

For an ideal op-amp in the linear region:

```text
V_U4out - V_B
= (R152/R153) ΔV_M5
≈ 22.1 × ΔV_M5
```

If BOCP receiver loading through R154 is negligible:

```text
V_BOCP - V_B ≈ 22.1 × ΔV_M5
```

Status:

```text
B↔BAT- analog sensing path = VERIFIED
nominal circuit gain ≈ 22.1 V/V = VERIFIED_FROM_COMPONENT_VALUES
BOCP measured gain/offset = OPEN
BOCP exact firmware/control interpretation = OPEN
exact trip threshold / final protection action = OPEN
```

Detailed transfer and diagnostic gate:

```text
research/19_ASP2000_A0_BOCP_TRANSFER_AND_M5_DIAGNOSTIC_GATE.md
```

---

## 7. Function classification

### VERIFIED

```text
7 × CSD18510KCS physically parallel between B and BAT-
Drain → BAT-
Source → B
all seven gates biased from common 12VP through individual 68.1 Ω
all seven gates have individual 47.5 kΩ pull-downs to B
B = SIG in the U4 analog region
U4 senses B relative to BAT-
U4 closed-loop resistor gain = 22.1 nominal
U4 output exported as BOCP to CN4A pin 6
ASP product explicitly includes input reverse-polarity protection / AUTO-RECOVERY
```

### STRONGLY SUPPORTED

```text
Q39...Q65 implement the declared reverse-polarity function as a low-side ideal-diode-style bank
B↔BAT- MOS-bank drop is reused as current/fault information
BOCP participates in over-current / abnormal-drop protection logic
```

### NOT SUPPORTED BY CURRENT EVIDENCE

```text
independently commanded battery disconnect by Q39...Q65
PWM operation of Q39...Q65 during normal conversion
seven separate current branches with separate control
BOCP is itself a digital comparator output
```

### OPEN

```text
exact BOCP trip threshold
exact BOCP active polarity at the control-board decision level
control-board response to BOCP
whether firmware distinguishes over-current / short-circuit / weak MOS enhancement / multiple conditions
12VP startup/shutdown sequence
```

Drive search did not locate a BOCP receiver/control-board schematic or firmware artifact in the currently accessible ASP files, so these items remain evidence-blocked rather than guessed.

---

## 8. Loss consequence

For `CSD18510KCS`, the existing 25°C datasheet boundary is:

```text
RDS(on),max @ VGS=10 V = 1.7 mΩ
```

Seven ideal parallel devices:

```text
R_eq,25C,max ≈ 0.243 mΩ
```

At `I_source = 175.4 A` scaling:

```text
ΔV_M5,25C-bound ≈ 42.6 mV
P_25C,bound ≈ 7.47 W
```

Nominal BOCP scale from the 22.1× amplifier:

```text
V_BOCP - V_B ≈ 0.94 V
```

Status:

```text
DATASHEET / TRANSFER SCALE ONLY
NOT MEASURED
NOT A VERIFIED TRIP THRESHOLD
```

The actual product loss must be obtained from M5 hardware measurement:

```text
P_batteryInterface,meas
= I_source × ΔV(B↔BAT-)
```

with temperature and 12VP recorded.

---

## 9. Why BOCP is not benchmark-grade current metrology

The current-to-voltage element is the MOS bank itself:

```text
R_bank = f(Tj, VGS, sharing, package, PCB, contacts)
```

and LM2904-family input offset is in the millivolt class, while the desired M5 signal is also only tens of millivolts.

Therefore:

```text
M5 Kelvin + I_source + temperature
= benchmark-grade loss evidence

BOCP
= product protection/sense-chain cross-check
```

A BOCP-derived current value must not replace direct M5 loss measurement unless an independent product calibration is established.

---

## 10. Benchmark-boundary correction

The seven-MOS loss is classified primarily as a battery-interface protection/sensing loss, not magnetic-X1 loss.

### Contract P — product-level comparison

Every architecture must provide matched required functionality such as:

```text
input reverse-polarity protection / equivalent ideal-diode behavior
AUTO-RECOVERY-equivalent product behavior if required by comparison contract
battery-current / abnormal-return-drop fault information
required fusing / fault isolation
```

Implementation may differ, but its loss must be counted.

### Contract C — core-converter comparison

Battery-interface protection/sensing overhead may be excluded only when excluded from A0, A1 and every candidate equally.

Forbidden:

```text
Candidate removes Q39...Q65 functionality
→ counts the removed watts
→ claims X1/topology advantage
```

A lower-loss implementation preserving the product function is a valid battery-interface engineering improvement, but not by itself proof of a new conversion topology.

---

## 11. M5 measurement requirement

At each stable load point record:

```text
I_source
ΔV_M5 = V_B - V_BAT-
V_BOCP relative B/SIG
12VP
-12V if safely accessible
MOS-bank temperature
ambient/cooling condition
```

Calculate:

```text
R_M5,eff = ΔV_M5 / I_source
P_M5     = I_source × ΔV_M5

G_BOCP,meas
= (V_BOCP - V_B) / ΔV_M5
```

Use a load sweep rather than one point:

```text
ΔV_M5 vs I_source
→ hot effective battery-interface resistance

V_BOCP vs ΔV_M5
→ analog-chain gain and intercept
```

No intentional protection trip test should be performed without an approved hardware-safety procedure.

---

## 12. Research consequence for A1

A1 must no longer preserve a vague generic `disconnect` assumption for this block.

Under Product Contract P it must preserve the now-verified product requirement:

```text
input reverse-polarity protection
```

and match required sensing/fault information to the extent established by the product boundary.

This sharpens the central comparison:

```text
A0 product-interface loss
vs
A0 intrinsic magnetic X1 loss
```

before deciding whether X1 physics itself should be replaced.

---

## 13. Formal status

```text
B↔BAT- seven-MOS power boundary                    = VERIFIED
gate bias from 12VP through 7 × 68.1 Ω             = VERIFIED
7 × 47.5 kΩ gate-source pull-downs to B            = VERIFIED
ASP input reverse-polarity protection feature      = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
Q39...Q65 ideal-diode-style implementation link    = STRONGLY_SUPPORTED
independent disconnect command on this bank         = NOT_SUPPORTED
B = SIG at U4 analog section                        = VERIFIED
U4 senses B relative to BAT-                        = VERIFIED
BOCP nominal analog gain ≈22.1 V/V                  = VERIFIED_FROM_CIRCUIT
BOCP exported to CN4A pin 6                         = VERIFIED
over-current / abnormal-drop protection role        = STRONGLY_SUPPORTED
BOCP receiver/control-board artifact                 = NOT_FOUND_IN_CURRENT_DRIVE_SEARCH
exact BOCP threshold/control response                = OPEN
battery-interface measured loss                     = OPEN
A0 total BAT→X1 loss                                = OPEN
A1                                                  = BLOCKED UNTIL A0 LOSS LOCALIZATION
Candidate #10                                       = NOT_ASSIGNED
Novelty                                             = NOT_ESTABLISHED
```

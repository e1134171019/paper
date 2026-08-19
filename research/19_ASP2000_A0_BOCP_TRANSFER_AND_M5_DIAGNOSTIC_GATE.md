# 19 — ASP-2000 A0 BOCP Transfer Function and M5 Diagnostic Gate

Status date: 2026-08-19  
Role: `A0 BATTERY-INTERFACE ANALOG-SENSE / M5 DIAGNOSTIC GATE`  
Evidence status: `DIRECT SCHDOC CONNECTIVITY + RESISTOR VALUES + DEVICE-FAMILY SANITY BOUNDS`  
Hardware result status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark diagnostic evidence`

## 1. Purpose

Previous work established that the seven `CSD18510KCS` devices between `B` and `BAT-` form a full-current battery-interface region and that U4 (`LM2904`) monitors the same electrical boundary.

This note resolves the analog relationship more tightly:

```text
M5 Kelvin drop:  ΔV_M5 = V_B - V_BAT-
                    ↓
                 U4 analog gain
                    ↓
                   BOCP
```

The goal is to separate two different quantities:

```text
ΔV_M5 + I_source
→ actual battery-interface loss

BOCP
→ product protection/sense-chain response
```

BOCP is useful as a cross-check but is not a substitute for Kelvin loss measurement.

---

## 2. Verified reference relationship: B = SIG on this schematic region

Direct SchDoc wiring in the U4 region places the `B` net label and the `SIG` power/reference port on the same connected wire.

Therefore, for this analog section:

```text
B = local signal reference SIG
```

This is important because the BOCP output can be interpreted relative to `B/SIG`, while the sensed quantity is the small difference between `B` and `BAT-`.

---

## 3. U4 analog topology — VERIFIED

The BOCP channel uses U4 (`LM2904`) with:

```text
non-inverting input (+) → B

BAT-
↓
R153 = 1.00 kΩ, 1%
↓
inverting input (-)
↑
R152 = 22.1 kΩ, 1%
↑
U4 output

U4 output
↓
R154 = 100 Ω
↓
BOCP
↓
CN4A pin 6
```

The U4 supply rails in the same schematic region are:

```text
V+ → 12VP
V- → -12V
```

Thus this channel is configured as a closed-loop analog amplifier around the `B ↔ BAT-` millivolt difference, not merely as an uncalibrated comparator symbol.

---

## 4. Ideal closed-loop transfer equation

Define:

```text
ΔV_M5 = V_B - V_BAT-
```

For an ideal op-amp in the linear region:

```text
V- ≈ V+ = V_B
```

KCL at the inverting input gives:

```text
(V_B - V_BAT-) / R153
+
(V_B - V_U4out) / R152
= 0
```

Therefore:

```text
V_U4out - V_B
= (R152 / R153) (V_B - V_BAT-)
```

With the populated values:

```text
R152 / R153 = 22.1k / 1k = 22.1
```

so the nominal transfer is:

```text
V_U4out - V_B ≈ 22.1 × ΔV_M5
```

If the BOCP receiver is high impedance so that the 100 Ω output resistor has negligible drop:

```text
V_BOCP - V_B ≈ 22.1 × ΔV_M5
```

This is the first-order product sense-chain equation.

---

## 5. Gain tolerance from the fitted resistors

Both `R152` and `R153` are annotated 1% parts.

Nominal:

```text
G = 22.1
```

Worst-case resistor-ratio limits from ±1% individual tolerance are approximately:

```text
G_min ≈ 21.66
G_max ≈ 22.55
```

or roughly:

```text
±2% ratio uncertainty
```

before op-amp offset, bias current, output loading, temperature, PCB leakage and control-board input effects are included.

The 100 Ω `R154` means the measured BOCP pin voltage can differ from U4 output if the downstream receiver draws non-negligible current.

---

## 6. 12 V / 2 kW scale reference

The existing research anchor uses:

```text
I_source ≈ 175.4 A
```

The existing 25°C datasheet boundary for seven ideal parallel `CSD18510KCS` devices is:

```text
R_bank,25C,max ≈ 0.243 mΩ
```

This gives a scale-only M5 drop:

```text
ΔV_M5 ≈ I R
       ≈ 175.4 A × 0.243 mΩ
       ≈ 42.6 mV
```

and corresponding loss:

```text
P_M5 ≈ I × ΔV
     ≈ 7.47 W
```

The nominal BOCP analog level predicted by the resistor gain is then:

```text
V_BOCP - V_B
≈ 22.1 × 42.6 mV
≈ 0.94 V
```

Status:

```text
0.94 V = DATASHEET/TRANSFER SCALE REFERENCE
NOT measured BOCP
NOT a verified trip threshold
```

Example scale table using the same 0.243 mΩ device-only boundary:

| I_source | ΔV_M5 | P_M5 | nominal BOCP above B |
|---:|---:|---:|---:|
| 50 A | 12.1 mV | 0.61 W | 0.27 V |
| 100 A | 24.3 mV | 2.43 W | 0.54 V |
| 150 A | 36.4 mV | 5.46 W | 0.81 V |
| 175.4 A | 42.6 mV | 7.47 W | 0.94 V |
| 200 A | 48.6 mV | 9.71 W | 1.07 V |

Actual hot-device/contact/copper loss may differ materially.

---

## 7. BOCP is not a precision current measurement

The fitted amplifier uses an LM2904-family device. Its input offset is in the millivolt class, which is non-negligible compared with a `~10–50 mV` M5 sense signal.

For planning, the op-amp output error caused by input offset is amplified by the closed-loop noise gain:

```text
noise gain = 1 + R152/R153
           = 23.1
```

Therefore even a few millivolts of input offset can create tens of millivolts of BOCP output offset.

In addition, the current-to-voltage element is the seven-MOS bank itself:

```text
R_bank = f(Tj, VGS, current sharing, package, PCB, contacts)
```

so BOCP cannot be treated as a precision calibrated ammeter unless the product calibration/control logic proves otherwise.

Research decision:

```text
M5 Kelvin + I_source = benchmark-grade loss evidence
BOCP                 = protection/sense-chain cross-check
```

---

## 8. M5 measurement upgraded to a two-transfer diagnostic

At each stable operating point record simultaneously or under repeatable conditions:

```text
I_source
V_B
V_BAT-
ΔV_M5 = V_B - V_BAT-
V_BOCP relative to B/SIG
12VP
-12V if accessible
MOS-bank temperature
ambient / cooling condition
```

Then calculate two independent quantities.

### 8.1 Electrical loss path

```text
R_M5,eff = ΔV_M5 / I_source
P_M5     = I_source × ΔV_M5
```

This is the quantity used in the A0 loss budget.

### 8.2 Product sense-chain gain

```text
G_BOCP,meas = (V_BOCP - V_B) / ΔV_M5
```

Expected first-order linear-region value:

```text
G_BOCP,nom ≈ 22.1 V/V
```

Do not force measured data to 22.1; deviations are diagnostic evidence.

---

## 9. Load-sweep regression

Do not judge M5 from one operating point only.

Across a controlled load sweep, fit:

```text
ΔV_M5 = a_R + R_eff I_source
```

Interpretation:

```text
slope R_eff
→ hot effective battery-interface resistance at that thermal regime

intercept a_R
→ measurement offset / boundary error indicator
```

Also fit:

```text
V_BOCP - V_B = a_B + G_meas ΔV_M5
```

Interpretation:

```text
slope G_meas
→ analog-chain gain

intercept a_B
→ op-amp / reference / measurement offset indicator
```

This is much stronger than comparing one measured point with the 25°C MOSFET datasheet number.

---

## 10. Diagnostic interpretation matrix

### Case A — M5 drop rises normally with current, BOCP tracks at ~22.1×

```text
power path plausible
sense chain plausible
```

Then use measured `I × ΔV` for loss accounting.

### Case B — M5 drop is high and BOCP rises proportionally

Likely the high signal is real at the selected boundary.

Investigate:

```text
hot RDS(on)
low/abnormal VGS
current-sharing imbalance
MOS/package/contact heating
B/BAT- copper/contact resistance included in the sense boundary
```

### Case C — M5 drop is high but BOCP does not follow

Investigate the sense chain:

```text
U4 saturation or rail issue
12VP / -12V issue
R152/R153/R154 fault
BOCP downstream loading
wrong BOCP reference
probe/reference error
```

### Case D — M5 drop is normal but BOCP is abnormally high

Investigate:

```text
op-amp offset / fault
resistor-ratio error
BOCP loading/reference issue
measurement ground/reference mistake
```

Do not conclude real battery-interface loss is high from BOCP alone.

### Case E — BOCP clips/saturates while M5 remains linear

The product sense channel has reached its usable analog range.

```text
M5 Kelvin data may still remain valid
BOCP no longer gives proportional current information
```

### Case F — sign reversal / unexpected polarity

Stop interpretation and verify:

```text
probe polarity
B/SIG reference
battery polarity / operating state
MOS-bank conduction state
startup/shutdown transient
```

Do not map a reverse-sign transient into steady-state loss.

---

## 11. BOCP threshold remains OPEN

This analysis verifies an analog transfer path but does not establish the final protection threshold.

Still required:

```text
control-board BOCP receiver circuit
ADC/comparator threshold if any
firmware interpretation
active polarity
filter/debounce timing
fault response
```

Therefore the correct status is:

```text
BOCP analog transfer relation = VERIFIED FROM MAIN-BOARD CIRCUIT
BOCP current/fault information role = STRONGLY SUPPORTED
BOCP exact trip threshold/control action = OPEN
```

Do not infer a trip current from the ~0.94 V scale reference.

---

## 12. Research consequence

The seven-MOS region now has three separable roles/quantities:

```text
1. battery reverse-polarity / ideal-diode-style interface
   → STRONGLY SUPPORTED

2. actual full-current conduction loss
   → OPEN until M5 measured

3. analog drop amplification to BOCP
   → TRANSFER RELATION VERIFIED
```

This improves the fairness of later A1/candidate comparisons:

```text
Contract P:
match battery-interface function and compare real loss

Contract C:
exclude battery-interface overhead equally
```

BOCP itself is not an X1 topology advantage and must not be mixed with magnetic-conversion loss.

---

## 13. Formal next gate

The next hardware action for this region is now precisely defined:

```text
load sweep
↓
measure I_source
measure ΔV_M5 = V_B - V_BAT-
measure BOCP relative B/SIG
record MOS temperature + 12VP
↓
fit R_M5,eff
fit G_BOCP,meas
↓
calculate P_M5 = I × ΔV
↓
classify product-interface loss separately from intrinsic X1
```

Until those data exist:

```text
M5 actual loss         = OPEN
BOCP measured gain     = OPEN
BOCP exact trip        = OPEN
A0 total BAT→X1 loss   = OPEN
A1                     = BLOCKED
Candidate #10          = NOT_ASSIGNED
Novelty                = NOT_ESTABLISHED
```

# 62 — A0 Post-X1 and HFT Parameter Closure v1

Status date: 2026-08-20  
Role: `A0-REAL POST-X1 DEVICE/GRAPH RECOVERY + HFT EVIDENCE CLOSURE CONTRACT`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Canonical matched-comparison point: `350 Vdc-class`  
A0 physical design source: `PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc`  
Evidence status: `RAW R52 SCHDOC RECOVERY + PRODUCT-SPEC CROSS-CHECK + OFFICIAL/DEVICE-DATASHEET PARAMETERIZATION`  
Simulation status: `ANALYTICAL / REDUCED-ORDER ONLY; PSIM/LTspice NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File61 showed that the known direct-HF-link matrix/cycloconverter comparator is only a nominal/conditional loss survivor under a modern matched-device contract and is not a robust loss winner.

File62 therefore stops generic topology generation and returns to the real ASP-2000 R52 source files.

The objectives are:

```text
A. recover the actual R52 post-X1 rectifier identity
B. recover the actual 220-V X3 semiconductor identity and bridge population
C. recover the actual R52 HV-link capacitor design population/connectivity
D. search for the actual X3 switching-frequency/modulation evidence
E. close as much of the A0 HFT identity/parameter state as the source set permits
F. separate A0-REAL loss accounting from A0-MODERN-MATCHED topology accounting
```

The key governance correction is:

> Legacy-device loss in A0 is not topology novelty. A new architecture must eventually beat a fair modern matched implementation, not merely outperform the old R52 semiconductor population.

---

## 2. Raw evidence source set

### 2.1 R52 design folder

Google Drive source folder:

```text
PB-2200-0038-D_R52
folder id = 15egRx1ZG3-3NHipedBeOR_0WEIo3-P6z
```

Relevant files include:

```text
PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc
id = 11XKkK3mqinbyYSKlGpOrk8z4E-mLBzeW

PB-2200-0038-D_ASP-2000-MAIN-R52.PcbDoc
id = 1D27amP1IzZjMyHNx4TrN6fWvUbaWBy6s

PB-2200-0038-D_R52_元件位置圖.pdf
PB-2200-0038-D_R52_元件座標檔.csv / .txt
PB-2200-0038-D_R52_231206_PCB製作規格.xlsx
```

The binary Altium SchDoc was directly inspected at record/string level rather than relying only on earlier research summaries.

### 2.2 Product specification cross-check

Drive source:

```text
ASP standard spec 251023.pdf
id = 1B3qSTDFgiv6_ExdLzDZ-WePQ9xpGbu9D
```

The product specification confirms for ASP-2000:

```text
rated power = 2000 W
output family = 200 / 220 / 230 / 240 Vac
output frequency = 50 / 60 Hz selectable
reported maximum efficiency up to 94%
```

It does not state the X3 PWM carrier frequency.

---

## 3. A0-REAL E4 rectifier identity — CLOSED AT SCHEMATIC DESIGN LEVEL

Raw SchDoc records identify:

```text
D1 = KSU60D60N
D2 = KSU60D60N
D5 = KSU60D60N
D6 = KSU60D60N
```

and the verified graph remains:

```text
T1/T2 collective secondary
→ D1/D2/D5/D6 full-wave bridge
→ BUS+ / BUS-
```

Device class from the manufacturer catalog:

```text
KSU60D60N
fast-recovery silicon power diode
VRRM = 600 V
Io = 60 A
IFSM = 400 A
manufacturer-catalog VFM point ≈ 1.95 V @60 A
Tj range to 175°C
```

Evidence classification:

```text
A0 rectifier DEVICE IDENTITY
= SCHEMATIC-VERIFIED DESIGN INTENT

actual physical-unit population
= NOT HARDWARE-VERIFIED

actual rectifier watts / junction temperature / charging-pulse waveform
= OPEN
```

### 3.1 Correction to Files59–61

The File60/File61 `IDW10G65C5` SiC-Schottky result:

```text
~17.14 W matched rectifier floor
```

must be classified only as:

```text
A0-MODERN-MATCHED / TOPOLOGY-FAIRNESS COMPARATOR
```

It is **not** the physical R52 rectifier.

Do not mix:

```text
old KSU60D60N R52 loss
with
modern SiC rectifier topology-normalized loss
```

### 3.2 Device-aware R52 rectifier model

The actual rectifier model must use:

```text
Prect,A0
= Σ ∫ vF,KSU(iD(t),Tj) · iD(t) dt / T
```

not:

```text
2 × constant VF × average DC current
```

because a capacitor-input bridge can have pulsed secondary/diode current substantially different from the 5.714-A average HV power-current scale.

Therefore:

```text
A0 E4 identity = CLOSED
A0 E4 watts    = OPEN
```

---

## 4. A0-REAL X3 semiconductor graph — MAJOR CLOSURE

The R52 SchDoc contains the population annotation:

```text
NGTB50N65FL2W @110-V version
IRG7PH35UDPBF @220-V version
```

and separate notes:

```text
IRG7PH35UDPBF x4 @220V
```

at both high-voltage bridge banks.

For the 220-V population, the recovered X3 power stage is therefore:

```text
BUS+
 |
 |-- left high switch position:  Q2 || Q31
 |                              IRG7PH35UDPBF
 |
 |-- right high switch position: Q1 || Q32
 |                              IRG7PH35UDPBF
 |
bridge midpoints → ACL1 / ACN1 → output network
 |
 |-- left low switch position:   Q10 || Q35
 |                              IRG7PH35UDPBF
 |
 |-- right low switch position:  Q9 || Q34
 |                              IRG7PH35UDPBF
 |
BUS-
```

Total 220-V X3 population:

```text
8 × IRG7PH35UDPBF
= 4 full-bridge switch positions
= 2 IGBTs in parallel per switch position
```

Evidence classification:

```text
X3 topology / device design intent
= SCHEMATIC-VERIFIED

actual physical-unit population
= NOT HARDWARE-VERIFIED
```

This materially changes the A0-real loss ledger.

### 4.1 Actual device class

IRG7PH35UDPBF official datasheet values include approximately:

```text
VCES = 1200 V
INOMINAL = 20 A
IC @25°C max rating = 50 A
VCE(on),typ ≈ 1.9 V @20 A, VGE=15 V, Tj=25°C
VCE(on),typ ≈ 2.3 V @20 A, Tj=150°C
Eon,typ ≈ 1.06 mJ @600 V / 20 A / 25°C
Eoff,typ ≈ 0.62 mJ @600 V / 20 A / 25°C
Etotal,typ ≈ 1.68 mJ
Etotal,typ @150°C ≈ 2.87 mJ
co-pack diode trr ≈ 105 ns
```

This is a 1200-V trench IGBT, not the 650-V low-RDS(on) SiC MOSFET used in the File60 modern matched screen.

### 4.2 Correct A0-real conduction form

For two IGBTs in parallel at each switch position and two positions conducting in the H-bridge power path:

```text
P_X3,cond,A0
= 2 · < VCE( |iout|/2 , Tj ) · |iout| >
```

The parallel devices reduce current per die; they do **not** reduce the series count of two active switch positions.

Do not substitute a MOSFET `2 R I²` expression into this A0-real IGBT stage.

A constant `VCE=1.9 V` rated-point substitution would yield roughly:

```text
2 × 1.9 V × average(|iout|)
average(|iout|) = 2 Ipk / π ≈ 8.18 A
proxy ≈ 31 W
```

but this is only a **rated-point sensitivity**, not an A0 conduction-loss claim, because each die actually carries roughly half the branch current and the lower-current VCE curve must be used.

### 4.3 X3 switching frequency remains the dominant OPEN quantity

No explicit X3 SPWM/PWM carrier frequency was recovered from:

```text
R52 MAIN SchDoc
R52 design folder metadata/files searched
ASP standard product specification
Drive searches for ASP PWM/SPWM/control firmware
```

The product specification establishes only the 50/60-Hz output fundamental.

Therefore:

```text
A0 X3 switching frequency = OPEN
A0 X3 modulation details  = OPEN
A0 X3 switching watts     = OPEN
```

This is now a targeted evidence gap, not a generic unknown.

### 4.4 Why fs now has high information value

A crude switching-energy sensitivity can be written using the datasheet 25°C reference and linear `V×I` scaling only:

```text
Ebar,die
≈ 1.68 mJ
 × (Vbus / 600 V)
 × [Ipk/(2×20 A)]
 × (2/π)
```

At `Vbus=315 V`, `Ipk=12.856 A`:

```text
Ebar,die ≈ 0.180 mJ/event-equivalent
```

For eight IGBTs:

```text
Psw,sensitivity ≈ 8 Ebar,die fs
                ≈ 1.44e-3 × fs  [W, fs in Hz]
```

Illustrative only:

| assumed fs | 25°C linear sensitivity | 150°C linear sensitivity using 2.87-mJ datum |
|---:|---:|---:|
| 10 kHz | ~14.4 W | ~24.7 W |
| 20 kHz | ~28.9 W | ~49.3 W |
| 50 kHz | ~72.2 W | ~123 W |
| 100 kHz | ~144 W | ~247 W |

These are **NOT A0 switching-loss results**.

They omit/approximate:

```text
actual PWM state/event count
actual DC bus voltage
actual current at each switching event
parallel current sharing
RG and gate-drive waveform
freewheel/diode intervals
reverse recovery
dead time
temperature
soft/hard transition details
```

The table exists only to show why recovering `fs` and an actual gate/current waveform has higher decision value than further topology sketching.

---

## 5. A0-REAL HV-link / passive X2 — CAPACITOR GRAPH CLOSED

Raw SchDoc identifies:

```text
C8  = 680 µF / 315 V
C11 = 680 µF / 315 V
C89 = 680 µF / 315 V
C90 = 680 µF / 315 V
```

Connectivity records place all four positions directly across the same:

```text
BUS+ ↔ BUS-
```

rather than a 2-series/2-parallel string.

Therefore the R52 schematic design population is:

```text
Cbus,schematic = 4 × 680 µF
               = 2720 µF
```

Evidence status:

```text
value/count/connectivity = SCHEMATIC-VERIFIED DESIGN INTENT
actual capacitor manufacturer/P/N/ESR = OPEN
actual physical-unit population = NOT HARDWARE-VERIFIED
```

### 5.1 2ω energy ripple with 2720 µF

For `E2ω,pk=3.183 J`, the small-ripple approximation is:

```text
ΔVpk ≈ E2ω,pk / (Cbus Vbus)
```

Sensitivity:

| assumed A0 bus | ΔVpk | ΔVpp |
|---:|---:|---:|
| 300 V | ~3.90 V | ~7.80 V |
| 315 V | ~3.72 V | ~7.43 V |
| 350 V | ~3.34 V | ~6.69 V |

The corresponding total 100-Hz capacitor-current scale is:

```text
IC,rms ≈ P/(sqrt(2) Vbus)
```

or approximately:

```text
300 V → 4.71 Arms total
315 V → 4.49 Arms total
350 V → 4.04 Arms total
```

Ideal equal sharing across four capacitors gives about `1.0–1.2 Arms/cap`.

### 5.2 ESR-loss threshold

At 315 V:

```text
IC,rms,total ≈ 4.49 A
```

A 2-W total capacitor-ESR loss would require approximately:

```text
ESR_eq ≈ 2 / 4.49² ≈ 0.099 Ω
```

For four equal capacitors in parallel:

```text
ESR_each ≈ 4 × ESR_eq ≈ 0.40 Ω
```

Thus the passive HV-link X2 is not automatically a large watt-loss bucket.

Formal interpretation:

> Eliminating the large electrolytic bank can have strong volume/lifetime value, but File62 does not establish a correspondingly large A0 loss saving.

Actual ESR and ripple heating remain OPEN until the populated capacitor P/N or measurement is obtained.

---

## 6. A0 bus voltage — DO NOT EQUATE SCHEMATIC CAP RATING WITH OPERATING VBUS

The project-wide matched comparison point remains:

```text
350 Vdc-class
```

but this is not an established A0 measured bus value.

The R52 schematic uses `315-V` capacitor positions while the product family supports `200/220/230/240 Vac` variants.

For 220 Vac:

```text
Vac,pk = 311.13 V
```

which already creates little headroom if a two-level bridge is supplied near a 315-V-class bus.

This tension is evidence that:

```text
actual production population may vary by output-voltage variant
actual A0 bus setpoint must be recovered/measured
```

It is **not** evidence that the bus is exactly 315 V and is not permission to overwrite the canonical 350-V matched-comparison point.

Status:

```text
A0 actual BUS voltage = OPEN
```

---

## 7. A0 HFT closure state

Raw R52 SchDoc confirms:

```text
T1 = PQ5050
T2 = PQ5050
center-tapped primary structure already established
secondary collective/series path already established
```

But the available R52 source set does not establish:

```text
T1/T2 manufacturer part number
turns count / exact ratio
winding DCR
frequency-dependent Rac
core material
Lm
Lk
actual secondary RMS waveform
actual copper/core watts
```

Drive searches find other PQ50-family artifacts such as:

```text
M1-PQ50-V121-A transformer test sheet
M1-PQ50-V108-A context data from prior work
```

but no direct part-number linkage to A0 T1/T2 has been established.

Therefore they remain:

```text
PQ50-CLASS CONTEXT_ONLY
```

and may not be substituted into A0.

Formal state:

```text
A0 HFT physical class / graph = VERIFIED
A0 HFT numerical DCR/Rac/RMS = OPEN
```

---

## 8. Two ledgers are now mandatory

File62 creates a hard separation between:

### 8.1 A0-REAL R52 ledger

Use when answering:

> Where does the physical legacy ASP-2000 R52 actually lose power?

Current recovered state:

```text
E4 rectifier = 4 × KSU60D60N design intent
E5 X2       = 4 × 680 µF / 315 V in parallel, Cbus≈2720 µF design intent
E6 X3       = 8 × IRG7PH35UDPBF for 220-V population,
              2 parallel IGBTs per H-bridge switch position
X3 fs       = OPEN
A0 BUS      = OPEN
E3 HFT DCR/Rac/RMS = OPEN
```

### 8.2 A0-MODERN-MATCHED ledger

Use when answering:

> Is a topology itself better if both baseline and alternative are implemented with a fair modern semiconductor contract?

Retain Files60–61 normalization:

```text
modern SiC rectifier/MOSFET technology
matched voltage/current stress
soft-switched known G13 direct-HF-link comparator
robust baseline-low / candidate-high accounting
```

Hard rule:

```text
A0-REAL old-device saving
!=
new-topology saving
```

A proposed topology cannot claim novelty or structural efficiency merely because it replaces 1200-V legacy IGBTs / silicon fast-recovery diodes with modern SiC devices.

---

## 9. Revised interpretation of E4+E6

File59 selected E4+E6 as a plausible double-processing target.

Files60–61 showed that under modern matched devices:

```text
nominal win = possible
robust win  = not established
prior art   = dense
```

File62 adds:

```text
A0-real E4/E6 uses legacy silicon FRD + 1200-V IGBT technology
```

so the physical R52 may indeed have a materially larger post-X1 semiconductor loss than the modern matched baseline.

But that observation increases the importance of the dual-ledger rule rather than reviving generic direct-HF-link novelty.

Formal status:

```text
E4+E6 as A0 physical modernization target
= HIGH PRACTICAL INTEREST

E4+E6 as new-topology research target
= CONDITIONAL / COMPARATOR BRANCH

E4+E6 generic novelty
= STOP / PRIOR-ART-RICH
```

---

## 10. Decision-efficient remaining evidence

File62 reduces the main uncertainty set substantially.

### Closed/recovered

```text
A0 E4 rectifier identity          = CLOSED at SchDoc design level
A0 220-V X3 device identity       = CLOSED at SchDoc design level
A0 X3 parallel/device graph       = CLOSED at SchDoc design level
A0 HV-link C count/value/parallel = CLOSED at SchDoc design level
```

### Still decisive OPEN items

```text
1. actual A0 X3 switching frequency / modulation / gate waveform
2. actual A0 BUS voltage at the chosen operating point
3. A0 T1/T2 exact part link or winding DCR/Rac
4. A0 secondary RMS current waveform
5. actual HV-link capacitor P/N / ESR if E5 watts are required
6. physical-unit population confirmation for the tested output-voltage variant
```

The first four dominate the next loss ranking.

---

## 11. Immediate next formal gate

Do not generate another generic topology.

Immediate next artifact:

```text
research/63_A0_X3_SWITCHING_AND_HFT_COPPER_CLOSURE_V1.md
```

Priority order:

```text
P1 — recover X3 PWM carrier from control-board source/firmware if available
     OR acquire a valid gate waveform from the physical A0

P1 — establish actual BUS voltage at the same operating point

P1 — establish T1/T2 DCR/Rac or direct winding-loss bound

P1 — acquire secondary RMS current / waveform

P2 — identify HV-link capacitor P/N and ESR/ripple rating
```

If energized measurement is used, existing File34/File35 safety and metadata gates remain mandatory. No scope-derived switching-energy number is benchmark-grade without proper probe rating, current measurement and deskew.

After File63, recompute:

```text
A0-REAL post-X1 loss ledger
A0-MODERN-MATCHED baseline ledger
G13-REF2 matched comparator ledger
```

and only then select whether the research returns to:

```text
E4+E6 conditional branch
E2 commutation branch
or no new-topology branch under the present boundary
```

---

## 12. Formal File62 verdict

```text
A0 rectifier identity             = CLOSED / KSU60D60N DESIGN INTENT
A0 220-V X3 identity              = CLOSED / IRG7PH35UDPBF DESIGN INTENT
A0 X3 device count                = CLOSED / 8 TOTAL / 2 PARALLEL PER SWITCH POSITION
A0 passive X2 schematic C         = CLOSED / 2720 µF TOTAL
A0 X3 switching frequency         = OPEN
A0 actual BUS voltage             = OPEN
A0 HFT DCR/Rac/RMS                = OPEN
A0 HV-link ESR watts              = OPEN

E4+E6 physical modernization      = MATERIAL / WORTH QUANTIFYING
E4+E6 new-topology priority       = CONDITIONAL / NOT PRIMARY
E4+E6 novelty                     = NOT_ESTABLISHED / PRIOR-ART-RICH

Candidate #10                     = HOLD / NOT_ASSIGNED
PSIM                              = NOT EXECUTED
LTspice                           = NOT EXECUTED
hardware measurement              = NOT EXECUTED
```

The research mainline is now **A0 X3 switching + HFT copper/RMS evidence closure**, not another topology sketch.

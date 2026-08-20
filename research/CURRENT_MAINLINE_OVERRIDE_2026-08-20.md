# Current Mainline Override — 2026-08-20

Status: `AUTHORITATIVE CURRENT-MAINLINE OVERRIDE`

This file supersedes stale phase/header language in `research/RESEARCH_STATE.md` when determining the immediate research mainline. It does **not** erase historical evidence or governance.

## 1. Research boundary and governance

```text
Vin = 12–24 Vdc
Pout = 1–3 kW
anchor = 12 V / 2 kW
Vout = 220 Vac / 1φ / 50 Hz
canonical matched post-X1 comparison point = 350 Vdc-class
```

Anchor scales:

```text
Iin,ideal = 166.7 A
Iin@95% reference ≈ 175.4 A
350-V / 2-kW current scale = 5.714 A
220-Vac / 2-kW output current = 9.09 Arms
E2ω,pk = 3.183 J
E2ω,pp = 6.366 J
```

Evidence vocabulary:

```text
VERIFIED / MODELLED / HYPOTHESIS / OPEN / NOT_ESTABLISHED
```

Loss authority:

```text
ΔP_total = P_loss,baseline - P_loss,candidate
robust survive: P_loss,candidate,high < P_loss,baseline,low
```

Explicit state:

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
```

---

## 2. Generic novelty-generation dimensions already closed

Files52–57 screened representative `X1/X2/X3` overlap classes and closed generic overlap as a novelty generator.

File58 closed generic partial-power processing as a novelty generator while retaining:

```text
αP / αS / αI / αV
```

as mandatory edge-accounting dimensions.

Files53–57 remain hard-comparator/prior-art maps; their graphs are not Candidate #10.

---

## 3. Files59–61 — edge target and matched crossover

File59 ranked A0 edges:

```text
E1 source/LV conduction
E2 primary commutation/snubber
E3 HFT
E4 secondary rectification
E5 HV-link / X2
E6 VSI / X3
E7 output filter
```

Current mixed-evidence anchors remain:

```text
E1 main-MOS conduction proxy ≈ 12.31 W  MODELLED
E2 commutation bucket        ≈ 25.10 W  MODELLED / NOT MEASURED
E4 modern-matched rectifier  ≈ 17.14 W  MATCHED-TECH FLOOR
E3/E5/E6/E7 actual watts     = OPEN or partially closed only
```

File60 compared:

```text
rectifier → HV-link/X2 → VSI
vs
known soft-switched direct-HF-link matrix/cycloconverter + explicit X2
```

and found modern SiC conduction can survive, but only with roughly `7–15 W` nominal headroom before dynamic/X2/magnetic interaction.

File61 added hot-device and transformer-current uncertainty:

```text
40-mΩ SiC class robust conduction margin ≈ 2–4 W
60-mΩ class can fail conduction before dynamic/X2 loss
PDM direct-HF-link main transformer differential RMS ≈ 7.9 Arms @Vs≈350 V
κ² buffer/main interaction sensitivity ≈ 0.26–0.80 for Vbuf≈200–350 V
```

Therefore:

```text
E4+E6 nominal = CONDITIONAL_SURVIVOR
E4+E6 robust win = NOT_ESTABLISHED
E4+E6 novelty = PRIOR-ART-RICH / NOT A CANDIDATE
E4+E6 topology-synthesis priority = DOWNGRADED FROM PRIMARY
```

---

## 4. File62 executed — A0-REAL post-X1 device graph recovered

Authoritative artifact:

```text
research/62_A0_POST_X1_AND_HFT_PARAMETER_CLOSURE_V1.md
```

Raw source:

```text
PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc
Drive id = 11XKkK3mqinbyYSKlGpOrk8z4E-mLBzeW
```

### 4.1 Actual R52 rectifier design identity

Recovered from raw SchDoc:

```text
D1/D2/D5/D6 = KSU60D60N
```

Manufacturer class:

```text
600-V / 60-A fast-recovery silicon diode
```

Status:

```text
DEVICE IDENTITY = SCHEMATIC-VERIFIED DESIGN INTENT
actual physical-unit population = NOT HARDWARE-VERIFIED
actual hot/waveform rectifier watts = OPEN
```

Critical correction:

```text
File60/61 SiC-Schottky ~17.14-W value
= A0-MODERN-MATCHED comparator only
!= physical R52 rectifier loss
```

### 4.2 Actual 220-V X3 design identity and graph

Raw SchDoc annotates:

```text
IRG7PH35UDPBF @220-V population
NGTB50N65FL2W @110-V population
```

The 220-V X3 bridge is:

```text
Q2 || Q31   left high switch
Q10|| Q35   left low switch
Q1 || Q32   right high switch
Q9 || Q34   right low switch
```

Therefore:

```text
8 × IRG7PH35UDPBF total
4 H-bridge switch positions
2 parallel IGBTs per switch position
```

IRG7PH35UDPBF is a 1200-V trench IGBT with co-pack diode, not a 650-V SiC MOSFET.

Status:

```text
X3 device/topology = SCHEMATIC-VERIFIED DESIGN INTENT
X3 switching frequency = OPEN
X3 modulation details = OPEN
X3 switching watts = OPEN
```

A crude device-datasheet sensitivity shows that the unknown PWM carrier can easily move the X3 switching bucket by many watts, so recovering `fs` now has high information value. No sensitivity value is promoted to A0 measured loss.

### 4.3 R52 passive X2 capacitor graph

Raw SchDoc identifies:

```text
C8/C11/C89/C90 = 680 µF / 315 V
all four connected directly across BUS+ ↔ BUS-
```

Hence schematic design capacitance:

```text
Cbus = 2720 µF
```

At the 2-kW/50-Hz energy requirement, small-ripple voltage swing is only several volts peak for a 300–350-V bus-class sensitivity.

The total 100-Hz capacitor-current scale is roughly `4–4.7 Arms` over 350–300 V, or about `1.0–1.2 Arms/cap` under ideal equal sharing.

Interpretation:

```text
large electrolytic removal can have strong volume/lifetime value
but A0 passive-X2 watt saving is NOT established as large
```

Actual capacitor P/N and ESR remain OPEN.

### 4.4 Actual A0 bus voltage remains OPEN

Do not infer operating BUS voltage from the `315-V` capacitor marking.

The project canonical matched point remains 350 V; the physical R52 operating BUS setpoint/variant must be recovered or measured separately.

### 4.5 HFT numerical parameters remain OPEN

Raw SchDoc confirms:

```text
T1 = PQ5050
T2 = PQ5050
```

but does not establish direct A0 values for:

```text
part number / turns / ratio
DCR / Rac
Lm / Lk
core material
secondary RMS current
copper/core watts
```

Other `M1-PQ50-*` Drive artifacts remain `CONTEXT_ONLY` until direct linkage to A0 T1/T2 is proven.

---

## 5. Dual-ledger rule is now mandatory

### A0-REAL R52

Use to localize loss in the physical legacy product:

```text
E4 = KSU60D60N bridge
E5 = 2720-µF schematic HV-link bank
E6 = 8× IRG7PH35UDPBF for 220-V design
```

### A0-MODERN-MATCHED

Use for topology fairness:

```text
modern matched SiC rectifier/MOSFET baseline
vs
known soft-switched G13 comparator
```

Hard rule:

```text
legacy-device saving != topology saving
```

A future topology cannot claim structural efficiency merely by replacing old silicon FRDs/IGBTs with modern SiC.

---

## 6. Revised mainline decision

```text
E4+E6 as physical R52 modernization target = HIGH PRACTICAL INTEREST
E4+E6 as new-topology research target      = CONDITIONAL / COMPARATOR BRANCH
E4+E6 generic novelty                      = STOP / PRIOR-ART-RICH
```

No generic new graph is authorized.

The remaining decision-dominant A0 evidence is now sharply reduced to:

```text
1. X3 PWM carrier / modulation / gate waveform
2. actual BUS voltage at the same operating point
3. T1/T2 DCR/Rac or direct winding-loss bound
4. T1/T2 secondary RMS current waveform
5. capacitor P/N/ESR if E5 watts become material
6. physical-unit population confirmation
```

---

## 7. Immediate NEXT

Expected next artifact:

```text
research/63_A0_X3_SWITCHING_AND_HFT_COPPER_CLOSURE_V1.md
```

Priority:

```text
P1 recover X3 carrier from control source/firmware if available
   OR acquire valid physical gate waveform
P1 recover/measure actual BUS voltage
P1 establish HFT DCR/Rac
P1 acquire secondary RMS current waveform
P2 identify HV-link capacitor P/N/ESR
```

If energized measurement is required, Files34–35 safety/metadata gates remain mandatory. No switching-energy integration is benchmark-grade without suitable probes, current measurement and deskew.

After File63, rebuild three separate ledgers:

```text
A0-REAL
A0-MODERN-MATCHED
G13-REF2 modern matched comparator
```

Then select among:

```text
E4+E6 conditional return
E2 commutation branch
or no new-topology branch under the present boundary
```

Current explicit state remains:

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
```

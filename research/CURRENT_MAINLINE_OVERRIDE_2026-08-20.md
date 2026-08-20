# Current Mainline Override — 2026-08-20

Status: `AUTHORITATIVE CURRENT-MAINLINE OVERRIDE`

This file supersedes stale phase/header language in `research/RESEARCH_STATE.md` when determining the immediate research mainline. It does **not** erase historical evidence or governance.

## 1. Research boundary and governance

```text
Vin = 12–24 Vdc
Pout = 1–3 kW
anchor = 12 V / 2 kW
Vout = 220 Vac / 1φ / 50 Hz
canonical MODERN-MATCHED post-X1 point = 350 Vdc-class
```

Anchor scales:

```text
Iin,ideal = 166.7 A
Iin@95% reference ≈ 175.4 A
220-Vac / 2-kW output current = 9.09 Arms
E2ω,pk = 3.183 J
E2ω,pp = 6.366 J
```

Evidence vocabulary remains:

```text
VERIFIED / MODELLED / HYPOTHESIS / OPEN / NOT_ESTABLISHED
```

Loss authority remains:

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

## 2. Generic topology-generation dimensions are closed

Files52–57 screened representative `X1/X2/X3` overlap classes:

```text
O0 / O13 / O23 / O12 / O123
```

and closed generic coordinate overlap as a novelty generator.

File58 closed generic partial-power processing as a novelty generator while retaining:

```text
αP / αS / αI / αV
```

as mandatory edge-accounting dimensions.

Known direct-HF-link, APD, differential/common-mode, multilevel/flying-cap and triple-overlap graphs remain hard comparators rather than Candidate #10.

---

## 3. Edge-loss stage — Files59–61

A0 edge map:

```text
E1 source / LV conduction
E2 primary commutation / snubber
E3 HFT
E4 secondary rectification
E5 HV-link / X2
E6 VSI / X3
E7 output filter
```

Current mixed-evidence anchors:

```text
E1 main-MOS conduction proxy ≈ 12.31 W  MODELLED
E2 commutation bucket        ≈ 25.10 W  MODELLED / NOT MEASURED
E4 modern-matched rectifier  ≈ 17.14 W  MATCHED-TECH FLOOR
```

File60/61 compared the A0-like modern-matched:

```text
HFT -> rectifier -> HV-link/X2 -> VSI
```

against the known soft-switched direct-HF-link matrix/cycloconverter comparator.

Result:

```text
E4+E6 nominal conduction = CONDITIONAL_SURVIVOR
E4+E6 robust total win   = NOT_ESTABLISHED
E4+E6 novelty            = PRIOR-ART-RICH / NOT A CANDIDATE
```

At 40-mΩ SiC class, the preferred hot-candidate / low-baseline conduction envelope leaves only roughly `2–4 W` before matrix dynamics, X2 and HFT interaction.

Therefore E4+E6 was downgraded from primary topology synthesis to a conditional comparator branch.

---

## 4. File62 — A0-REAL post-X1 graph recovered

Authoritative artifact:

```text
research/62_A0_POST_X1_AND_HFT_PARAMETER_CLOSURE_V1.md
```

Raw R52 SchDoc design intent establishes:

```text
E4 rectifier:
D1/D2/D5/D6 = KSU60D60N
600-V / 60-A fast-recovery silicon diodes

E5 passive X2:
C8/C11/C89/C90 = 680 µF / 315 V
all four in parallel across BUS+ <-> BUS-
Cbus = 2720 µF schematic population

E6 / X3 @220-V version:
8 × IRG7PH35UDPBF
1200-V trench IGBTs
4 H-bridge switch positions
2 parallel IGBTs per position
```

Mandatory accounting split:

```text
A0-REAL R52
= physical legacy-product loss localization

A0-MODERN-MATCHED
= topology-fair modern semiconductor baseline

G13-REF2
= known soft-switched direct-HF-link hard comparator
```

Hard rule:

```text
legacy FRD / IGBT saving != topology saving
```

---

## 5. File63 executed — X3 carrier search + BUS/HFT RMS bounds

Authoritative artifact:

```text
research/63_A0_X3_SWITCHING_AND_HFT_COPPER_RMS_CLOSURE_V1.md
```

### 5.1 X3 carrier remains OPEN

The accessible R52 design files, product specification and Drive source set were searched for:

```text
PWM / SPWM / carrier / switching-frequency / firmware timing
```

No defensible X3 carrier scalar was recovered.

The product's selectable `50/60 Hz` is the AC fundamental, not the PWM carrier.

Formal state:

```text
X3 device / bridge graph = CLOSED at schematic design level
X3 carrier               = OPEN
X3 modulation/dead time  = OPEN
X3 switching watts       = OPEN
```

### 5.2 Physical A0 BUS is now BOUNDED, not measured

For a verified two-level H-bridge whose waveform is bounded by `±VBUS`, the maximum possible fundamental RMS is the square-wave fundamental:

```text
V1,rms,max = (2 sqrt(2) / pi) VBUS
```

Therefore 220 Vac requires:

```text
VBUS >= 244.36 V
```

The verified `315-V` electrolytic bank is directly across the full bus, giving the present normal-steady design ceiling:

```text
VBUS <= 315 V
```

Thus:

```text
A0 220-V BUS = BOUNDED / NOT MEASURED
244.36 V <= VBUS <= 315 V
```

If ordinary linear SPWM were later proven, the conditional lower bound would tighten to `311.13 V`; modulation is currently OPEN, so this is not an A0 setpoint claim.

The project canonical `350-Vdc-class` value remains a modern matched-comparator coordinate and must not be substituted into the physical R52 ledger.

### 5.3 A0 post-X1 and HFT secondary current bounds

At 2 kW:

```text
VBUS=315 V    -> IBUS,avg,ideal ≈ 6.35 A
VBUS=244.36 V -> IBUS,avg,ideal ≈ 8.18 A
```

T1/T2 secondaries are in series ahead of the capacitor-input bridge, so both carry the same rectifier-current waveform when conducting.

Therefore:

```text
Isec,rms >= P/VBUS
universal present lower bound: Isec,rms >= 6.35 A
```

The actual capacitor-charging waveform is pulsed, so real RMS is expected above the average-current scale; the numerical actual value remains OPEN.

### 5.4 HFT exact part and winding resistance remain OPEN

R52 confirms:

```text
T1/T2 = PQ5050-class
```

but no direct linkage from the R52 T1/T2 designators to a specific `M1-PQ50-*` manufacturing P/N was recovered.

Related Drive parts such as:

```text
M1-PQ50-V107-B
M1-PQ50-V109-A
M1-PQ50-V121-A
```

remain `CONTEXT_ONLY`.

Do not substitute their L/Lk or other parameters into A0.

Formal state:

```text
A0 HFT class = VERIFIED
A0 exact P/N = NOT_ESTABLISHED
A0 DCR/Rac   = OPEN
A0 copper W  = OPEN
```

### 5.5 Passive X2 is not established as a large watt-loss target

Using the physical BUS bound and `2720 µF`:

```text
2ω bank current ≈ 4.49 ... 5.79 Arms
ideal per-cap share ≈ 1.12 ... 1.45 Arms
ΔVpp ≈ 7.43 ... 9.58 V
```

The matching NCC/Chemi-Con KMR `315 V / 680 µF / 25.4×50 mm` catalog class is rated around `2.10 Arms/cap @105°C / 120 Hz`.

Thus the ideal 2ω component alone does not flag a ripple-current-rating violation.

Actual ESR, HF rectifier ripple, sharing and temperature remain OPEN, so E5 efficiency savings are not established as large.

Electrolytic removal may still carry meaningful volume/lifetime value.

---

## 6. Current mainline decision

File63 does not justify returning to generic new-topology synthesis.

Current branch state:

```text
E4+E6 physical R52 modernization = HIGH PRACTICAL INTEREST
E4+E6 topology research          = CONDITIONAL COMPARATOR / NOT PRIMARY
E2 avoidable commutation         = LOSS-RELEVANT (~25.10-W model) BUT PRIOR-ART-RICH
E5 passive buffer efficiency gap = NOT ESTABLISHED AS LARGE
```

The decisive missing evidence is now physical rather than taxonomic.

---

## 7. Immediate NEXT — File64 minimum measurement pack

Expected next artifact:

```text
research/64_A0_MINIMUM_MEASUREMENT_PACK_X3_HFT_BUS_V1.md
```

Purpose:

```text
close the few physical quantities that can reverse the mainline ranking
without performing unnecessary broad characterization
```

Minimum pack:

```text
M1  VBUS average + 100/120-Hz ripple + HF peak
M2  one valid X3 gate/driver-command waveform -> carrier + duty + dead time
M3  T1/T2 secondary current waveform -> RMS / peak / crest factor
M4  de-energized four-wire transformer winding DCR
M5  optional synchronized X3 VCE×IC switching-energy capture only after M1/M2 and deskew validity
```

Files34–35 remain mandatory for safety, metadata and evidence validity.

File64 is a measurement contract; it does not claim hardware execution and does not authorize unsafe energized probing by itself.

After valid M1–M4 evidence, rebuild:

```text
A0-REAL loss ledger
A0-MODERN-MATCHED loss ledger
G13-REF2 matched comparator ledger
```

Then select exactly one:

```text
A. E4+E6 returns as a loss-driven research branch
B. E2 becomes the strongest remaining physical target
C. no new topology is justified under the present boundary
```

Current explicit state remains:

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
```

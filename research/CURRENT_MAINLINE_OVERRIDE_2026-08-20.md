# Current Mainline Override — 2026-08-20

Status: `AUTHORITATIVE CURRENT-MAINLINE OVERRIDE`

This file supersedes stale phase/header language in `research/RESEARCH_STATE.md` when determining the immediate research mainline. Historical evidence and governance remain in the numbered research files.

## 1. Boundary / governance

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

## 2. Generic novelty-generation dimensions remain closed

Files52–57 close generic X1/X2/X3 overlap as a novelty generator.

File58 closes generic partial-power processing as a novelty generator while retaining:

```text
αP / αS / αI / αV
```

as mandatory edge-accounting dimensions.

Known direct-HF-link, APD, differential/common-mode, multilevel/flying-cap and triple-overlap graphs remain hard comparators rather than Candidate #10.

---

## 3. Edge-loss branch — Files59–61

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

Current key analytical anchors:

```text
E1 main-MOS conduction proxy ≈ 12.31 W  MODELLED
E2 commutation bucket        ≈ 25.10 W  MODELLED / NOT MEASURED
E4 modern-matched rectifier  ≈ 17.14 W  MATCHED-TECH FLOOR
```

Files60–61 establish:

```text
E4+E6 nominal conduction = CONDITIONAL_SURVIVOR
E4+E6 robust total win   = NOT_ESTABLISHED
E4+E6 novelty            = PRIOR-ART-RICH / NOT A CANDIDATE
```

At the 40-mΩ SiC class the preferred hot-candidate / low-baseline conduction envelope leaves only roughly `2–4 W` before matrix dynamics, X2 and HFT interaction.

Therefore E4+E6 remains a conditional comparator branch, not the active new-topology mainline.

---

## 4. A0-REAL post-X1 evidence — Files62–63

R52 raw design intent establishes:

```text
E4:
D1/D2/D5/D6 = KSU60D60N

E5:
C8/C11/C89/C90 = 680 µF / 315 V
all four across BUS+ <-> BUS-
Cbus = 2720 µF

E6 @220-V:
8 × IRG7PH35UDPBF
4 H-bridge switch positions
2 IGBTs in parallel per position

HFT:
T1/T2 = PQ5050-class
```

Mandatory accounting split:

```text
A0-REAL R52
A0-MODERN-MATCHED
G13-REF2 modern matched comparator
```

Hard rule:

```text
legacy FRD / IGBT saving != topology saving
```

File63 source search did not recover the real X3 PWM carrier.

File63 first-principles / component-rating bounds:

```text
A0 220-V physical BUS:
244.36 V <= VBUS <= 315 V
BOUNDED / NOT MEASURED

ideal post-X1 power-current scale:
6.35 ... 8.18 A

universal present HFT-secondary RMS lower bound:
Isec,rms >= 6.35 A
```

The exact R52 transformer P/N and DCR/Rac remain unlinked; other `M1-PQ50-*` records remain `CONTEXT_ONLY`.

The passive `2720-µF` X2 bank is not established as a large watt-loss bucket; electrolytic removal may still have volume/lifetime value.

---

## 5. File64 executed — minimum physical-measurement contract

Authoritative artifact:

```text
research/64_A0_MINIMUM_MEASUREMENT_PACK_X3_HFT_BUS_V1.md
```

Role:

```text
close only the physical quantities that can reverse the mainline ranking
before any further topology generation
```

Minimum pack:

```text
M1  BUS+ <-> BUS- waveform
    VBUS average / LF ripple / HF peak

M2  X3 gate / driver timing
    carrier / duty / dead time / modulation class

M3  T1/T2 series-secondary / rectifier-input current
    RMS / peak / crest factor / charging-pulse waveform

M4  de-energized Kelvin winding DCR
    T1 secondary / T2 secondary
    primary half-windings if accessible

M5  optional X3 VCE×IC switching-energy capture
    only after M1/M2 and valid probe deskew
```

Evidence-validity codes and raw CSV/metadata schema are defined in File64.

### Safety / metadata authority correction

File64 inherits the directly applicable formal protocols:

```text
research/15_ASP2000_A0_KELVIN_MEASUREMENT_PROTOCOL.md
research/16_ASP2000_A0_DYNAMIC_SWITCHING_AND_HFT_MEASUREMENT_PROTOCOL.md
```

Any earlier shorthand saying `Files34–35` are the mandatory measurement safety/metadata gate is superseded for this specific File64 workflow. File34 remains useful as an evidence-acquisition worksheet, but the actual Kelvin/dynamic measurement procedures are Files15/16.

Hard measurement rule:

```text
File64 = CONTRACT READY
!= hardware measurement executed
```

No energized capture is valid if probe reference/rating, current-probe saturation, clipping, aliasing, deskew or operating-point metadata is not controlled.

---

## 6. Current mainline

The current mainline is now:

```text
PHYSICAL EVIDENCE ACQUISITION
NOT NEW TOPOLOGY SYNTHESIS
```

Immediate action:

```text
acquire valid M1–M4 data from File64
```

Recommended sequence:

```text
STEP 0  unit/revision/output-variant confirmation
STEP 1  M4 de-energized DCR
STEP 2  M1 VBUS
STEP 3  M2 low-side X3 carrier
STEP 4  M2 same-leg dead time if safe instrumentation permits
STEP 5  M3 secondary current
STEP 6  rebuild A0-REAL ledger
STEP 7  M5 switching-energy only if still decision-relevant
```

---

## 7. Expected NEXT after measurement data exists

Create only after valid M1–M4 evidence:

```text
research/65_A0_REAL_LOSS_LEDGER_CLOSURE_V1.md
```

File65 must rebuild three separate ledgers:

```text
A0-REAL R52
A0-MODERN-MATCHED
G13-REF2 modern matched comparator
```

Then select exactly one branch:

```text
A. E4+E6 returns only if modern-matched structural loss advantage survives
B. E2 becomes mainline if primary commutation remains the strongest avoidable target
C. NO-NEW-TOPOLOGY if neither supports a robust advantage
```

No Candidate #10 assignment occurs before that decision gate.

Current explicit state remains:

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
```

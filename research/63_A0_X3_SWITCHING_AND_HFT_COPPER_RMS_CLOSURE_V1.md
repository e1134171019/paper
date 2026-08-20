# 63 — A0 X3 Switching and HFT Copper/RMS Closure v1

Status date: 2026-08-20  
Role: `A0-REAL X3 CARRIER SEARCH + BUS BOUND + HFT CURRENT/COPPER EVIDENCE CLOSURE`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
A0 design source: `ASP-2000 R52`  
Evidence status: `RAW R52 DESIGN AUDIT + DRIVE SEARCH + FIRST-PRINCIPLES BOUNDS + COMPONENT-RATING CONTEXT`  
Simulation status: `ANALYTICAL / REDUCED-ORDER ONLY; PSIM/LTspice NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File62 closed the R52 design identities for the post-X1 rectifier, X3 semiconductor population and passive HV-link capacitor bank, but left four decision-dominant quantities open:

```text
X3 PWM carrier / modulation
actual A0 BUS voltage
T1/T2 DCR / Rac
T1/T2 secondary RMS current
```

File63 attempts to close those quantities from the presently accessible design / Drive evidence without converting absent data into assumed A0 facts.

This file also creates the minimum physical bounds needed to decide what must be measured next.

Hard rule:

```text
not found in source set != zero
context transformer != A0 transformer
50/60-Hz output frequency != PWM carrier
component voltage rating != measured operating voltage
```

---

## 2. Evidence sources searched

### 2.1 R52 design files

```text
PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc
PB-2200-0038-D_ASP-2000-MAIN-R52.PcbDoc
R52 component-position / coordinate artifacts
```

The raw Altium files were inspected at record/string/component level.

### 2.2 Product / Drive sources

```text
ASP standard spec 251023.pdf
Excel 公式自動計算表格
M1-PQ50-V121-A 變壓器檢測.xlsx
Drive searches for PWM / SPWM / ASP control / firmware / program identifiers / PQ50 variants
```

The related-model sheets expose program names and several `M1-PQ50-*` transformer identities, but the exact `ASP-2000W-12V-200ac` row does not establish an A0 transformer part number.

Examples retained only as context:

```text
VF-2000W-12V-200ac -> M1-PQ50-V107-B
ASP-2000W-12V-100ac -> M1-PQ50-V109-A
M1-PQ50-V121-A -> separate transformer inspection sheet
```

None has a proven direct linkage to the R52 T1/T2 population under the 12-V / 200–220-V A0 anchor.

---

## 3. X3 carrier / modulation search — NOT CLOSED

File62 established the 220-V X3 design as:

```text
8 × IRG7PH35UDPBF
4 H-bridge switch positions
2 parallel IGBTs per switch position
```

File63 searched the accessible source set for:

```text
PWM
SPWM
carrier
switching frequency
frequency / Hz parameters tied to X3
firmware / source / hex linkage
control-board timing scalars
```

Result:

```text
no defensible X3 carrier-frequency scalar recovered
```

The raw MAIN SchDoc contains control/interface labels such as:

```text
PH-L
VGRID
VBUS
VVVF
DR-A
DR-B
```

but no carrier-frequency number that can be assigned to X3.

The product specification establishes:

```text
output fundamental = 50 / 60 Hz selectable
```

which is not the PWM carrier.

Formal state:

```text
X3 device / graph       = CLOSED AT SCHEMATIC DESIGN LEVEL
X3 PWM carrier          = OPEN
X3 modulation law       = OPEN
X3 event count / cycle  = OPEN
X3 switching watts      = OPEN
```

Therefore File62's IGBT switching-loss sensitivity remains only a sensitivity and may not be promoted to A0 watts.

### 3.1 Minimum closure evidence for X3

One of the following is required:

```text
A. control firmware/source with timer/PWM configuration and version linkage to the physical unit
or
B. valid physical gate/driver-command waveform capture under a declared operating point
```

A gate waveform sufficient only for `fs`, duty and dead time does not automatically establish switching watts.

Benchmark-grade switching-energy integration additionally requires synchronized device voltage/current and valid probe deskew per Files34–35.

---

## 4. A0 BUS voltage — upgraded from OPEN to BOUNDED / NOT MEASURED

File62 correctly refused to equate the `315-V` capacitor rating with the operating BUS voltage.

File63 adds a topology-independent lower bound for the verified two-level H-bridge.

For any bridge switching waveform bounded by:

```text
-vBUS <= vbridge(t) <= +vBUS
```

the maximum possible fundamental component is obtained by the polarity-aligned square wave.

Its fundamental RMS is:

```text
V1,rms,max = (2 sqrt(2) / pi) VBUS
           ≈ 0.900316 VBUS
```

Therefore a 220-Vrms fundamental requires at minimum:

```text
VBUS >= (pi / (2 sqrt(2))) × 220
     >= 244.36 V
```

This is a first-principles waveform-amplitude bound. It does not assume sinusoidal PWM.

### 4.1 Upper design bound from the R52 capacitor population

File62 verified that all four:

```text
680 µF / 315 V
```

capacitors are directly in parallel across the full `BUS+ ↔ BUS-` rail.

For valid normal steady-state operation, the bus cannot intentionally exceed the capacitor rated voltage.

Thus the presently defensible design-bound interval for the 220-V A0 is:

```text
244.36 V <= VBUS,operating <= 315 V
```

Evidence class:

```text
FIRST-PRINCIPLES LOWER BOUND
+
SCHEMATIC COMPONENT-RATING UPPER BOUND
```

It is **not a measured BUS setpoint**.

Actual production margin below 315 V is not known.

### 4.2 Linear-SPWM special case

If X3 were proven to remain in ordinary linear full-bridge SPWM with modulation index `m <= 1`, then:

```text
V1,rms <= VBUS / sqrt(2)
```

and 220 Vac would require:

```text
VBUS >= 311.13 V
```

However:

```text
X3 modulation = OPEN
```

so `311.13 V` is a conditional SPWM bound, not an A0 operating-voltage claim.

Formal File63 state:

```text
A0 BUS voltage = BOUNDED / NOT MEASURED
hard present interval @220 Vac = 244.36 ... 315 V
```

The project canonical `350-Vdc-class` point remains valid only for modern matched comparator studies; it is not the physical R52 BUS value.

---

## 5. Consequence for post-X1 power-current scale

At 2 kW, the ideal average BUS current is:

```text
IBUS,avg = P / VBUS
```

Across the File63 bound:

```text
VBUS = 315 V    -> IBUS,avg ≈ 6.35 A
VBUS = 244.36 V -> IBUS,avg ≈ 8.18 A
```

Therefore the A0-real post-X1 current scale is no longer an unconstrained `5.714 A @350 V` assumption.

For physical R52 analysis use:

```text
IBUS,avg,ideal ≈ 6.35 ... 8.18 A
```

before conversion losses.

---

## 6. T1/T2 secondary RMS — lower bound closed, actual waveform still OPEN

The established A0 graph has:

```text
T1 secondary
series with
T2 secondary
-> D1/D2/D5/D6 bridge
-> capacitor-input BUS
```

The same rectifier current therefore passes through both series secondary windings when the bridge conducts.

For any waveform:

```text
Irms >= |Iaverage|
```

and a capacitor-input rectifier normally has pulsed charging current, so its secondary RMS exceeds the ideal average DC-current scale.

Thus:

```text
Isec,rms >= P / VBUS
```

and the universal present lower bound is:

```text
Isec,rms >= 6.35 A
```

at the 2-kW anchor.

If the operating bus is toward the low end of the permitted range, the ideal-current scale rises toward:

```text
8.18 A
```

before charging-pulse crest factor is included.

Formal state:

```text
T1 secondary RMS actual = OPEN
T2 secondary RMS actual = OPEN
secondary RMS lower-bound scale = CLOSED
```

A numerical copper-loss claim still requires the real current waveform and winding resistance.

---

## 7. HFT part-number / DCR / Rac search — direct linkage NOT FOUND

The R52 PcbDoc identifies the two transformer footprints as PQ5050-class / `T-20P`-type library references, but no `M1-PQ50-*` manufacturing part number was recovered with direct linkage to A0 T1/T2.

The Drive family data contain several real PQ50 variants, including:

```text
M1-PQ50-V107-B
M1-PQ50-V109-A
M1-PQ50-V121-A
```

but they belong to different model/variant records or standalone inspection data.

The `M1-PQ50-V121-A` inspection sheet provides examples of PQ50-class Lm/Lk values, e.g. roughly:

```text
Lm ~3.6 ... 4.0 mH
Lk ~1.8 ... 2.1 µH
```

for that separate part.

It does not supply an A0 R52 DCR/Rac and cannot be substituted into T1/T2.

Formal state:

```text
A0 transformer geometry/class = VERIFIED PQ5050
A0 exact transformer P/N      = NOT_ESTABLISHED
A0 DCR                        = OPEN
A0 Rac                        = OPEN
A0 turns/ratio                = OPEN
A0 core material              = OPEN
```

### 7.1 Copper-loss threshold form

Let `Rsec` be the effective secondary winding resistance of **each** transformer at the relevant current-frequency spectrum.

Because both secondaries carry the same series current:

```text
Psec,Cu,total = 2 Isec,rms² Rsec
```

Using only the universal lower-bound current `6.35 A`:

```text
1 W per transformer  -> Rsec ≈ 24.8 mΩ
5 W total            -> Rsec ≈ 62.0 mΩ per transformer
10 W total           -> Rsec ≈ 124 mΩ per transformer
```

These resistance thresholds are not estimated A0 DCR values.

Because the real rectifier current is pulsed and `Isec,rms > 6.35 A`, the real resistance required to produce a given copper-loss wattage would be lower than these lower-bound-current examples.

Primary copper remains even more sensitive to the extreme-low-voltage current domain and must be accounted separately when actual winding/current data become available.

---

## 8. Passive X2 current / ripple closure improved

File62 verified:

```text
Cbus = 4 × 680 µF = 2720 µF
rated voltage per capacitor = 315 V
all four directly parallel across BUS
```

Using the File63 physical BUS bound, the 2ω-only buffer-current scale is:

```text
IC,2ω,rms ≈ P / (sqrt(2) VBUS)
```

which gives:

```text
315 V    -> 4.49 Arms total -> 1.12 Arms/cap ideal share
244.36 V -> 5.79 Arms total -> 1.45 Arms/cap ideal share
```

The corresponding small-ripple energy swing is:

```text
ΔVpk ≈ E2ω,pk / (Cbus VBUS)
```

or:

```text
315 V    -> ΔVpp ≈ 7.43 V
244.36 V -> ΔVpp ≈ 9.58 V
```

### 8.1 KMR-series ripple-current context

The SchDoc identifies the HV capacitors as NCC/Chemi-Con KMR-series `680 µF / 315 V`, `25.4 × 50 mm` design positions.

The KMR catalog entry for the matching `315 V / 680 µF / 25.4×50 mm` class gives approximately:

```text
rated ripple current = 2.10 Arms / capacitor
@105°C / 120 Hz
```

Four ideal-equal-sharing capacitors therefore provide an aggregate catalog-current scale of:

```text
8.4 Arms @120 Hz
```

The ideal 2ω-only current scale of `4.49–5.79 Arms` does not by itself flag a catalog ripple-current-rating violation.

This does **not** close capacitor watts because the real bank also sees:

```text
rectifier charging pulses
HF ripple
unequal current sharing
temperature rise
actual ESR / aging
```

Formal interpretation:

```text
E5 passive-X2 watt loss = NOT ESTABLISHED AS LARGE
E5 volume/lifetime relevance = STILL MATERIAL
```

Removing the electrolytic bank therefore cannot be counted as a large efficiency saving without an ESR/thermal measurement or exact populated-part model.

---

## 9. What File63 closes and what it does not

### Closed / bounded

```text
X3 physical device graph                  = CLOSED at schematic design level
X3 carrier search result                  = NOT FOUND / remains OPEN
220-V A0 BUS structural bound             = 244.36 ... 315 V
A0 ideal post-X1 current scale            = 6.35 ... 8.18 A
T1/T2 secondary RMS universal lower bound = >=6.35 A
Cbus 2ω ripple-current scale              = 4.49 ... 5.79 Arms
Cbus 2ω voltage-ripple scale              = ~7.43 ... 9.58 Vpp
HFT exact P/N linkage                     = NOT ESTABLISHED
```

### Still OPEN

```text
actual VBUS setpoint and ripple waveform
actual X3 PWM carrier / dead time / modulation
actual X3 switching watts
T1/T2 DCR / Rac
T1/T2 primary and secondary RMS waveforms
actual HFT copper/core watts
actual capacitor ESR / HF ripple heating
physical-unit population verification
```

---

## 10. Mainline consequence

File63 does **not** restore `E4+E6` as the primary topology-synthesis branch.

Reasons:

```text
1. the actual R52 X3 uses legacy 1200-V IGBTs; its loss is highly device-generation dependent
2. the fair modern E4+E6 crossover already had only a tight robust margin in File61
3. passive X2 is not established as a large watt-loss bucket
4. HFT interaction cannot be closed without actual winding/current data
5. generic direct-HF-link/matrix graphs remain prior-art rich
```

Therefore:

```text
E4+E6 physical modernization = HIGH PRACTICAL INTEREST
E4+E6 topology novelty       = NOT_ESTABLISHED / PRIOR-ART-RICH
E4+E6 research status        = CONDITIONAL COMPARATOR BRANCH
```

E2 remains the largest presently modelled avoidable-loss bucket (`~25.10 W` surrogate), but E2 soft-commutation prior art is also dense.

The project therefore cannot responsibly select a new topology from present evidence alone.

---

## 11. Immediate NEXT — minimum A0 measurement pack

The next artifact shall be evidence acquisition, not topology generation:

```text
research/64_A0_MINIMUM_MEASUREMENT_PACK_X3_HFT_BUS_V1.md
```

Minimum information-efficient measurements:

### M1 — BUS voltage / ripple

```text
V(BUS+ - BUS-)
DC average
100/120-Hz ripple
HF ripple / peak
same declared Vin / Pout / Vac / PF / temperature
```

This closes the `244.36–315 V` bound to a physical operating value.

### M2 — X3 carrier / dead time

Acquire one valid X3 gate or isolated driver-command waveform sufficient to establish:

```text
carrier frequency
duty/modulation pattern
dead time
50/60-Hz polarity/envelope relation
```

No V×I switching-energy integration is required for this first capture.

### M3 — T1/T2 secondary RMS

Acquire the secondary current waveform with adequate current-probe bandwidth/range and record:

```text
Irms
Ipk
crest factor
HF repetition / pulse width
T1/T2 sharing / same-series-path verification
```

### M4 — transformer winding resistance

De-energized, preferably four-wire:

```text
secondary DCR for T1 and T2
primary half-winding DCRs if accessible
winding temperature
```

If frequency-dependent Rac is needed for final watts, add a controlled impedance/resistance sweep or derive Rac from a validated magnetic model after geometry/part closure.

### M5 — optional higher-risk X3 loss capture

Only after M1/M2 and probe validity are established:

```text
VCE(t)
IC(t)
valid current sharing assumption or per-position current
probe deskew
switching-event energy integration
```

Files34–35 safety and metadata requirements remain mandatory.

This file does not authorize energized work by itself.

---

## 12. Formal verdict

```text
FILE63 RESULT

X3 carrier                     = OPEN / SOURCE SEARCH EXHAUSTED FOR CURRENT SET
A0 BUS                         = BOUNDED 244.36...315 V / NOT MEASURED
HFT exact part number          = NOT_ESTABLISHED
HFT DCR/Rac                    = OPEN
HFT secondary RMS actual       = OPEN
HFT secondary RMS lower bound  = >=6.35 A @2 kW
passive X2 2ω-current scale    = 4.49...5.79 Arms bank
E5 large-watt-loss hypothesis  = NOT_ESTABLISHED

E4+E6 topology priority        = CONDITIONAL COMPARATOR / NOT PRIMARY
E2 topology priority           = LOSS-RELEVANT BUT PRIOR-ART-RICH
new topology generation        = NOT AUTHORIZED
```

Current explicit state:

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
```

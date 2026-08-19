# 21 — ASP-2000 A0 Transformer Parameter Evidence Gate

Status date: 2026-08-19  
Role: `A0 HFT PARAMETER / EVIDENCE-BOUNDARY GATE`  
Evidence status: `SCHDOC SYMBOL/MODEL TRACE + DRIVE CROSS-MODEL SEARCH`  
Hardware measurement status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark parameter governance`

## 1. Purpose

The A0 topology/current graph is substantially reconstructed, but a credible magnetic-loss model still requires numerical transformer parameters.

This note answers a narrower question:

> Which T1/T2 magnetic quantities are actually supported by the current ASP-2000 R52 evidence, and which tempting PQ50-family data must not be substituted across models?

Raw company Altium files remain outside the public repository.

---

## 2. What the ASP-2000 R52 SchDoc actually identifies

For both T1 and T2, the supplied SchDoc directly exposes:

```text
Designator: T1 / T2
Comment: PQ5050
Library symbol: T-20P
PCB model: DTRF-PQ5050-V
```

Verified winding terminals from the power graph:

```text
primary:
pin 9 = A
pin 8 = center tap B
pin 7 = C

secondary external terminals used in A0 graph:
pin 2 / pin 5
```

The A0 secondary relationship is also verified:

```text
T1 pin 5 = T2 pin 2
```

forming the direct series junction already used in the A0 power graph.

---

## 3. What is NOT encoded as a trustworthy T1/T2 parameter

The present SchDoc/PcbDoc does not expose a defensible populated value for:

```text
exact transformer internal part number
primary turns per half
secondary turns
turns ratio
core material grade
air gap
Ae / le / Ve tied to the populated core set
Lm
leakage inductance
primary winding DCR / Rac
secondary winding DCR / Rac
winding construction / foil / litz details
measured insulation capacitance
```

The SchDoc uses a generic transformer drawing symbol. The number of graphical coil arcs in that symbol is **not evidence of physical turns**.

Formal rule:

```text
schematic coil drawing count ≠ physical turn count
PQ5050 footprint/core size ≠ complete magnetic design
```

---

## 4. Drive cross-model search found a PQ50 transformer test file

Drive contains:

```text
M1-PQ50-V121-A 變壓器檢測.xlsx
```

The file contains measured sample data such as:

```text
F1-F2 inductance ≈ 142 … 163.5 µH
F2-F3 inductance ≈ 142.5 … 162.5 µH
LM ≈ 3.6 … 3.96 mH
LK(short-F1-F2-F3) ≈ 1.8 … 2.1 µH
```

These values are useful as evidence that the organization measures PQ50-family magnetics with explicit Lm/Lk criteria.

However, they are **not yet A0 data**.

---

## 5. Cross-model attribution check — CRITICAL

A separate Drive model/test matrix links:

```text
M1-PQ50-V121-A
```

to:

```text
ASP-3000W-24V-200ac-S9C
```

not to the ASP-2000 12 V A0 unit.

The generic matrix contains an `ASP-2000W-12V-200ac` row, but the transformer/program/device fields for that row are unpopulated in the currently accessible version.

Therefore:

```text
M1-PQ50-V121-A → ASP-2000 A0
= NOT ESTABLISHED
```

and the measured Lm/Lk values in that transformer file must be classified only as:

```text
PQ50-FAMILY / CROSS-MODEL CONTEXT
```

They must **not** be inserted into the A0 numerical loss model.

---

## 6. Forbidden substitutions

Do not do any of the following:

```text
same PQ50/PQ5050 core size
→ assume same turns ratio

same mechanical footprint
→ assume same Lm / leakage

same product family
→ reuse another voltage/power variant's transformer data

schematic coil drawing
→ count graphical arcs as turns

220 Vac output requirement
→ back-calculate transformer ratio without measured switching duty / bus behavior / winding topology details
```

Any such value may be used only as a labelled sensitivity parameter, never as `VERIFIED_A0`.

---

## 7. A0 magnetic quantities that remain usable without exact turns

Even before the populated transformer design is known, hardware measurement can still close several system quantities:

```text
I_T1,RMS
I_T2,RMS
T1/T2 current imbalance
primary voltage waveform
primary volt-second integral
switching frequency
transformer case/core-region temperature
secondary current waveform
```

These can establish stress and empirical loss behavior without pretending the core design is known.

But converting volt-second to flux density requires:

```text
N_primary
Ae
```

and predicting core loss requires, at minimum, a defensible material/loss model plus frequency and flux excursion.

Therefore:

```text
ΔB = (1 / N Ae) ∫v dt
```

remains numerically open until `N` and `Ae` are tied to the populated transformer.

---

## 8. Minimum evidence required to close the transformer parameter gate

Preferred order:

### T-G1 — populated part identification

Obtain one of:

```text
BOM transformer part number for ASP-2000 R52 variant
transformer label / manufacturing drawing
approved magnetic-component specification
```

This is the cleanest closure path.

### T-G2 — power-OFF LCR characterization

On the correct ASP-2000 transformer / equivalent production spare, measure and record:

```text
L(9-8)
L(8-7)
L(9-7)
secondary inductance as applicable
leakage under defined short condition
measurement frequency
measurement amplitude
```

Do not compare L values without recording test frequency and connection condition.

### T-G3 — low-energy turns-ratio test

With the transformer isolated from hazardous energized circuitry and using an approved low-amplitude AC test method:

```text
apply known low AC voltage to one winding
measure induced voltage on the other winding
→ derive turns ratio
```

The test must not rely on normal inverter power operation.

### T-G4 — winding resistance

Use Kelvin / four-wire methods where winding resistance is low:

```text
primary-half DCR
secondary DCR
temperature
```

For high-frequency copper-loss work, DCR alone is insufficient; Rac versus frequency/current waveform must eventually be modeled or measured.

### T-G5 — core/material closure

Obtain:

```text
core manufacturer / material grade
core geometry
Ae / le / Ve
or approved transformer magnetic drawing/spec
```

Only then promote analytical core-loss calculations beyond sensitivity studies.

---

## 9. Loss-model consequence

Current transformer loss equation remains structurally valid:

```text
P_HFT = P_primary,Cu + P_secondary,Cu + P_core + P_parasitic
```

but numerical status is:

```text
P_primary,Cu
= OPEN until current + Rac/DCR-bound evidence

P_secondary,Cu
= OPEN

P_core
= OPEN

P_parasitic / leakage processed power
= OPEN
```

No numeric A0 HFT watt total should be published from the available PQ50-family cross-model data.

---

## 10. Research consequence

The newly found `M1-PQ50-V121-A` file is useful because it demonstrates a realistic internal measurement pattern:

```text
half-primary inductance
Lm
shorted-winding leakage
```

but the model attribution check prevents contamination of the ASP-2000 A0 benchmark.

This is an evidence-governance result, not a negative result.

Formal decision:

```text
ASP-2000 T1/T2 numerical magnetic parameters
= OPEN

PQ5050 mechanical/topological identity
= VERIFIED

M1-PQ50-V121-A data
= CONTEXT_ONLY / DIFFERENT PRODUCT VARIANT
```

A1 remains blocked from a claimed quantitative magnetic-loss advantage until A0 magnetic parameters are measured or bounded from the correct production transformer.

---

## 11. Formal status

```text
T1/T2 = PQ5050                              = VERIFIED
center-tapped primary connectivity          = VERIFIED
T1/T2 secondary series junction             = VERIFIED
exact populated transformer internal P/N    = OPEN
turns ratio                                 = OPEN
Lm / leakage for A0                         = OPEN
winding Rac / DCR for A0                    = OPEN
core material / Ae / Ve for A0              = OPEN
M1-PQ50-V121-A measurement file             = FOUND
M1-PQ50-V121-A attribution to ASP-3000/24V  = SUPPORTED_BY_DRIVE_MATRIX
M1-PQ50-V121-A attribution to A0             = NOT_ESTABLISHED
cross-model magnetic data use               = CONTEXT_ONLY
A0 HFT numerical loss                       = OPEN
Candidate superiority                       = NOT_ESTABLISHED
Novelty                                     = NOT_ESTABLISHED
```

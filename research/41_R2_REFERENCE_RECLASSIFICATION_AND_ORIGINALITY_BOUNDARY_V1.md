# 41 — R2 Reference Reclassification and Originality Boundary v1

Status date: 2026-08-20  
Role: `ORIGINALITY CONTROL / REFERENCE RECLASSIFICATION / ANTI-PLAGIARISM BOUNDARY`  
Research boundary anchor: `12 Vdc / 2 kW / 220 Vac / 1φ`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Mandatory correction

Files 38–40 developed an active-clamp push-pull realization using the IEEE work of Wu et al. as the locked PM-4 reference cell. That work is useful and valid as a benchmark, but it must not be treated as the project's proposed converter merely because its component values or operating boundary are changed.

From this file forward, the historical working identifier:

```text
R2-G1
```

is reclassified as:

```text
R2-REF1
= IEEE_REFERENCE_COMPARATOR
= Wu-type active-clamp push-pull reference implementation
```

The files are retained for traceability; their analytical work is not deleted. Their interpretation is superseded by this file.

---

## 2. What is prior art and therefore NOT ours

Reference:

Tsai-Fu Wu, Jin-Chyuan Hung, Jeng-Tsuen Tsai, Cheng-Tao Tsai, and Yaow-Ming Chen, "An Active-Clamp Push–Pull Converter for Battery Sourcing Applications," IEEE Transactions on Industry Applications, vol. 44, no. 1, 2008, DOI `10.1109/TIA.2007.912748`.

The following are prior-art functions and cannot be claimed as project novelty:

```text
push-pull main power transfer
active-clamp auxiliary switch(es)
clamp capacitor energy storage
leakage-inductance-assisted resonant transition
body-diode-assisted ZVS turn-on
recovery of transformer leakage energy
complementary main/auxiliary timing with dead time
```

Changing:

```text
Vin
Pout
switching frequency
MOSFET part number
L/C values
transformer ratio
number of paralleled MOSFETs
```

without a substantive new graph / state / principle is an adaptation or benchmark, not a proposed topology.

---

## 3. Allowed use of R2-REF1

R2-REF1 may be used for:

```text
REFERENCE
COMPARATOR
FALSIFIER
LOSS BENCHMARK
EXTREME-LV SCALING TEST
```

It may answer:

```text
Does a known active-clamp push-pull method still provide net benefit
when operated near the 12 V / ~175 A source-domain boundary?
```

It may NOT be described as:

```text
our proposed active-clamp converter
our new active-clamp topology
our invented ZVS method
```

unless a later independently derived candidate survives IEEE Gate A/B/C.

---

## 4. Hard originality rule for all future candidates

```text
SAME topology graph
+ SAME switching-state sequence
+ SAME operating principle
+ only changed ratings / values / devices

→ REFERENCE / ADAPTED / COMPARATOR
→ NOT PROPOSED
```

A project candidate must instead establish at least one substantive differentiator, for example:

```text
different majority-power graph
different commutation-energy path
different voltage-building mechanism
different switching-state sequence
different governing relation / operating law
different modulation or control principle
or a genuinely new generalizable design/loss criterion
```

Even then:

```text
DIFFERENT != NOVEL
```

and IEEE Gate A/B/C remains mandatory.

---

## 5. Ownership boundary for analytical work

The project may independently calculate the behavior of a cited reference under the project's own boundary, including:

```text
12–24 V source scaling
1–3 kW load scaling
I²R sensitivity
loss relocation
matched architecture comparison
extreme-LV crossover analysis
```

Those calculations are project analysis, but the underlying prior-art circuit must remain explicitly attributed.

A valid manuscript structure would be conceptually:

```text
[xx] prior-art converter
↓
reconstructed / modeled as comparator
↓
project boundary and matched loss model
↓
identified structural weakness / crossover
↓
project candidate or generalizable design law
```

not:

```text
prior-art converter
+ changed values
→ claimed as new converter
```

---

## 6. Consequence for Files 38–40

Formal interpretation:

```text
File 38 R2-G1 actual graph development
→ HISTORICAL REFERENCE DEVELOPMENT

File 39 reference-locked active-clamp mapping
→ VALID R2-REF1 REFERENCE MODEL

File 40 dual-HFT gain/ZVS/P0 model
→ VALID REFERENCE-SCALING / SENSITIVITY WORK
```

No result in Files 38–40 grants topology novelty.

The numeric work may still be reused later to compare R2-REF1 against genuinely independent candidates.

---

## 7. Current R2 research flow

```text
R2-REF1
IEEE known active-clamp push-pull
↓
identify loss weaknesses at extreme LV
↓
generate independent R2-Cx concept
↓
IEEE Gate A immediately
↓
if Gate A survives:
actual graph
↓
IEEE Gate B
↓
only then detailed simulation
```

This is now the controlling originality boundary for R2 work.

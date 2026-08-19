# 11 — Working Architecture Loss Audit

Status date: 2026-08-19  
Status: `WORKING ARCHITECTURE — KEEP`  
Novelty: `NOT_ESTABLISHED`

## 1. Decision

Keep the current working structure while separating **functional coordinates** from **mandatory hardware stages**.

```text
12 V source
↓
very-short / very-low-R common LV path
↓
local bulk + HF decoupling
↓
early distributed branch power cells
↓
branch switching + X1
↓
reduced-current domain
↓
[X2 active 2ω buffer — optional / must prove benefit]
↓
X3 AC synthesis
↓
220 Vac / 1φ
```

This is a loss-routing hypothesis, not a claimed high-efficiency topology.

The current research target is **not** to optimize the ASP-2000 product. A0 is a real-product evidence source used to identify or falsify cross-architecture physical gaps.

Authoritative physical-gap screen:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
```

---

## 2. Important terminology correction

`X1`, `X2`, and `X3` are **functional coordinates**, not automatically three additional converter stages.

```text
X1 = first major impedance / current-domain transformation
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC synthesis coordinate
```

New loss is created only by the physical components and energy-processing paths used to implement those coordinates.

Therefore:

```text
more named nodes ≠ automatically more loss
more active energy-processing stages ≈ almost always more loss buckets
```

---

## 3. Block-by-block added-loss audit

### 3.1 Very-short common LV path

Purpose:

```text
carry unavoidable source average power current
with minimum R and minimum parasitic L
```

Added / unavoidable losses:

```text
battery ESR
fuse resistance
connector / joint resistance
busbar / PCB copper I²R
parasitic-inductance switching overshoot
```

At 12 V / 2 kW the average source current cannot be removed before X1. The research variable is therefore not whether hundred-ampere current exists, but how much RMS/current-path exposure and irreversible loss remain before the first major transformation.

### 3.2 Local bulk + HF decoupling

Purpose:

```text
localize switching / commutation current
prevent HF pulse current from traversing long source/bus paths
```

Added losses:

```text
bulk-capacitor ESR / ripple heating
dielectric loss
MLCC ESR / dielectric loss
inrush / precharge burden
local capacitor RMS current
```

Retain only if local-loop loss is lower than the source/bus loss avoided.

### 3.3 Early current distribution / N-way fan-out

Critical rule:

```text
current splitting alone does NOT automatically reduce I²R loss
```

Added penalties include:

```text
more branch interconnect
current-sharing error
parasitic mismatch
more gate-drive power
more total Coss / Qoss / Qg
control / EMI burden
possible circulating current
```

Therefore fan-out is a design dimension for PG-1, not an independent research gap or novelty claim.

### 3.4 Branch switching + X1

This remains the core research region.

If X1 is magnetic HFT:

```text
MOS conduction
MOS switching
Coss / gate drive
primary / secondary copper
core loss
skin / proximity effect
leakage
clamp / snubber / commutation
```

If X1 is non-isolated high-gain:

```text
MOS conduction / switching
inductor / coupled-inductor copper + core
leakage
rectifier / diode loss
capacitor ESR / dielectric
charge redistribution
internal circulating current
```

If X1 is direct HFL:

```text
LV bridge loss
HF-link loss
magnetic/coupling loss
matrix / bidirectional-switch conduction
commutation loss
HF circulating RMS
```

The real comparison is the total X1 mechanism loss under the same boundary, not whether one ASP component can be improved.

### 3.5 Reduced-current energy node

This is a functional domain, not necessarily a mandatory DC-link stage.

If implemented as an HV DC bus, added losses include:

```text
DC-link capacitor ESR / dielectric
ripple-current heating
HV interconnect loss
precharge / balancing / bleeder losses if present
```

A Direct-HFL architecture may not contain a complete HV DC bus.

### 3.6 X2 active 2ω buffer

Status:

```text
OPTIONAL / NOT YET PROVEN
```

Retention rule:

```text
P_LV,saved > P_X2,added
```

Required research question is PG-4: how much 2ω energy actually reflects to the extreme-LV source path. Active buffering is only a solution hypothesis if PG-4 survives.

### 3.7 X3 AC synthesis

X3 is functionally unavoidable somewhere in the DC→AC system.

The research question is not whether X3 exists, but where complete AC synthesis occurs and what current domain it occupies.

---

## 4. Why this ordering is retained

```text
very-short common LV path
→ minimize unavoidable Iavg²R

local decoupling
→ localize switching / commutation RMS

early distribution
→ enable practical current handling, not automatic loss reduction

X1 early
→ leave the 12 V hundred-ampere domain only when net loss is reduced

X2 after X1, if justified
→ keep 2ω energy out of the expensive LV path only if net-positive

X3 after X1
→ avoid complete AC synthesis in the extreme-current domain
```

Working principle:

> Place each necessary current / energy component in the voltage-current domain where its irreversible loss is cheapest, while minimizing extra processing functions.

---

## 5. Product reality check from ASP-2000 R52 — CORRECTED

Current A0 reconstruction establishes:

```text
two separately fused/local-bulk center-tap feeds
2 × PQ5050 HFT
A logical switch = 10 parallel MOS
C logical switch = 10 parallel MOS
all 20 main MOS sources → common B
four local driver subgroups / two logical A-C functions
manufactured PCB finished copper >82 µm
secondary collective/series voltage formation
passive A↔C RC snubber/damping network
HV rectification
HV DC-link
separate HV AC-synthesis stage
```

The old shorthand "four independent five-MOS power banks" is superseded.

ASP therefore already uses substantial conventional extreme-LV engineering:

```text
heavy copper
heavy silicon paralleling
split/local gate drive
multiple magnetic paths
early magnetic X1
```

Consequences:

```text
parallel MOS ≠ novelty
multiple HFT paths ≠ novelty
early distribution ≠ novelty
heavier copper ≠ topology research contribution
snubber-value optimization ≠ topology research contribution
```

A0 is not assumed inefficient and is not the product to be redesigned.

---

## 6. Physical-gap hypotheses retained after A0 screen

Detailed authority: `research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md`.

```text
PG-1 — minimum extreme-LV full-current conduction exposure before X1
        = HYPOTHESIS / TOPOLOGY-RELEVANT

PG-2 — dissipative switching/leakage/Coss commutation handling at X1
        = HYPOTHESIS / STRONG STRUCTURAL SIGNAL

PG-3 — magnetic transformation copper/core/leakage burden at extreme ratio
        = OPEN / NOT YET A GAP

PG-4 — single-phase 2ω energy reflection into the LV domain
        = HYPOTHESIS / NOT ESTABLISHED
```

Items such as PCB trace width, fuse/J8/contact loss, reverse-protection MOS, BOCP, RL1 and U5 stuffing remain product-engineering evidence unless needed to discriminate one of PG-1…PG-4.

---

## 7. Immediate falsifiers

Reject or reframe a proposed research direction if:

```text
PG-1:
a fair optimized HFT A1 reduces extreme-LV conduction enough that alternative X1 adds more loss than it saves

PG-2:
measured snubber + avoidable commutation loss is too small to justify recovery/soft-commutation overhead

PG-3:
correct A0/A1 magnetic loss is not a first-order burden after fair optimization

PG-4:
passive HV-link storage already keeps source 2ω sufficiently small

fan-out:
branch current falls but total declared I²R does not

active X2:
source ripple falls but buffer loss/circulation exceeds saved LV loss
```

Core rule remains:

```text
P_saved > P_added
```

---

## 8. Next validation questions — REFOCUSED

Do not attempt to close every ASP watt before mechanism comparison.

Use minimum hypothesis-discriminating evidence:

```text
H1 / PG-1
→ actual pre-X1 conduction exposure

H2 / PG-2
→ A/C switching overlap + RC snubber watts

H3 / PG-3
→ T1/T2 RMS / volt-second / magnetic burden

H4 / PG-4
→ source 100/120 Hz ripple + HV-link ripple
```

Then compare the surviving mechanisms across:

```text
A1 optimized magnetic HFT
B Direct HFL
C non-isolated high-gain/current-distribution
```

Candidate synthesis remains on HOLD until at least one physical gap survives fair existing-family comparison.

Formal status:

```text
working architecture = KEEP
A0 structural baseline = SUFFICIENT_FOR_GAP_SCREEN
A0 optimization campaign = NOT THE RESEARCH TASK
PG-1 = HYPOTHESIS
PG-2 = HYPOTHESIS
PG-3 = OPEN
PG-4 = HYPOTHESIS
fan-out benefit = NOT PROVEN
active X2 benefit = NOT PROVEN
Candidate #10 = HOLD / NOT_ASSIGNED
novelty = NOT_ESTABLISHED
```

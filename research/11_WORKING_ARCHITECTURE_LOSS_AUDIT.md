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

At 12 V / 2 kW the average current cannot be removed before X1; therefore the only available lever in this common region is to minimize impedance and physical exposure.

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

The intended loss migration is:

```text
HF RMS current in expensive common LV path ↓
local capacitor-loop RMS ↑
```

Retain only if the local-loop loss and practical burden are lower than the bus/source loss avoided.

### 3.3 Early current distribution / N-way fan-out

Purpose:

```text
reduce per-device / per-cell current stress
allow X1 to be physically close to each branch
increase usable semiconductor / copper conductance
shorten commutation loops
```

Critical correction:

```text
current splitting alone does NOT automatically reduce I²R loss
```

If total copper cross-section is unchanged, splitting one conductor into N smaller conductors can leave total copper loss approximately unchanged.

Added losses / penalties:

```text
more branch interconnect
current-sharing error
parasitic-inductance mismatch
more gate-drive power
more total Coss / Qoss / Qg
more control channels
possible branch-to-branch circulating current
EMI / synchronization burden
```

Therefore N is an optimization variable, not a monotonic efficiency lever.

### 3.4 Branch switching + X1

This is the core research region.

Purpose:

```text
convert low-voltage high-current branch energy
into a higher-voltage / lower-current domain as early as practical
```

If X1 is magnetic HFT:

```text
MOS conduction
MOS switching
Coss / gate drive
primary copper
secondary copper
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

The real comparison is the total X1 mechanism loss under the same operating boundary.

### 3.5 Reduced-current energy node

This is a functional domain, not necessarily a mandatory DC-link stage.

Purpose:

```text
place downstream switching / storage / AC synthesis
in a lower-current domain than the 12 V source region
```

If implemented as an HV DC bus, added losses include:

```text
DC-link capacitor ESR / dielectric
ripple-current heating
HV interconnect loss
precharge / balancing / bleeder losses if present
```

A Direct-HFL architecture may not contain a complete HV DC bus at all.

### 3.6 X2 active 2ω buffer

Status:

```text
OPTIONAL / NOT YET PROVEN
```

Purpose:

```text
keep single-phase 2ω pulsating energy
circulating locally after X1
instead of reflecting through the 12 V full-current source path
```

Potential added losses:

```text
bidirectional switch conduction
switching / gate drive
buffer inductor copper / core
buffer capacitor ESR / dielectric
buffer RMS current
extra commutation / circulating current
sensing / control / auxiliary power
```

Retention rule:

```text
P_LV,saved > P_X2,added
```

Required ablation:

```text
Buffer OFF
vs
Buffer ON
```

If the existing passive HV DC-link already suppresses source 2ω sufficiently, an active X2 may be net-negative and must be removed.

### 3.7 X3 AC synthesis

X3 is functionally unavoidable somewhere in the DC→AC system.

Purpose of the current placement:

```text
perform complete low-frequency AC synthesis
only after the system has entered a reduced-current domain
```

Added / unavoidable losses:

```text
HV switch conduction
switching / Coss / recovery / dead-time
gate drive
output-inductor copper / core
filter-capacitor ESR
```

The research question is not whether X3 exists, but **where** it exists.

---

## 4. Why this ordering is retained

The structure is not a collection of fashionable techniques. Each region is tied to a distinct loss mechanism:

```text
very-short common LV path
→ minimize unavoidable Iavg²R

local decoupling
→ localize switching / commutation RMS

early current distribution
→ reduce device stress and allow modular X1 placement

X1 early
→ leave the 12 V hundred-ampere domain as soon as net loss permits

X2 after X1, if justified
→ prevent avoidable 2ω RMS from returning through the expensive LV path

X3 after X1
→ avoid complete AC synthesis in the extreme-current domain
```

Working principle:

> Place each necessary current / energy component in the voltage-current domain where its irreversible loss is cheapest, while minimizing the number of extra processing stages.

---

## 5. Product reality check from ASP-2000 R52

The ASP-2000 R52 product baseline already contains:

```text
two PQ5050 HFT modules
four low-side switch banks of five parallel MOS devices
eight high-current input fuse positions
two groups of LV bulk capacitance
HV rectification
HV DC-link storage
separate HV AC-synthesis stage
```

Therefore:

```text
parallel MOS
current sharing
multiple HFT power paths
early distribution
```

cannot be treated as candidate novelty or automatic loss advantage.

The candidate must outperform both:

```text
A0 = actual ASP product abstraction
A1 = fair optimized modular-HFT benchmark
```

before a non-magnetic or alternative X1 mechanism can claim a structural benefit.

---

## 6. Immediate falsifiers

Reject or reframe a proposed change if any of the following occurs:

```text
fan-out lowers branch current but total I²R does not fall

more parallel MOS reduces conduction but added gate/Coss/commutation loss exceeds the saving

X1 raises voltage early but creates excessive circulating / magnetic / capacitor RMS

active X2 reduces 2ω source ripple but its own loss exceeds saved LV I²R

Direct-HFL removes stages but increases HF RMS / commutation loss beyond the removed rectifier/VSI loss
```

Core rule remains:

```text
P_saved > P_added
```

---

## 7. Next validation questions

The next modeling work should answer only three mechanism questions before detailed topology invention:

```text
Q1 — Does early current distribution reduce total declared R_eq / I²R,
     compared with the real ASP A0 and a fair A1 magnetic benchmark?

Q2 — How much LV RMS remains after each candidate X1,
     decomposed into avg / 2ω / switching / circulating / reactive / commutation components?

Q3 — Does active post-X1 X2 buffering produce positive net saved loss,
     compared with the existing passive DC-link case?
```

Formal status:

```text
working architecture = KEEP
A0 product baseline = ESTABLISHED
fan-out benefit = NOT YET PROVEN
active X2 benefit = NOT YET PROVEN
candidate X1 winner = NOT ESTABLISHED
novelty = NOT ESTABLISHED
```

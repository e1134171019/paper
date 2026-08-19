# 29 — Nine-Family X1 / X2 / X3 Normalization v1

Status date: 2026-08-19  
Role: `RESEARCH-DEFINITION NORMALIZATION / FAMILY CROSS-COMPARISON`  
Research object: `#01...#09 × X1/X2/X3 × ONTOLOGY L1-L4`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

本文件把九類既有主功率路徑全部套入 `research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md` 建立的同一套功能座標與 ontology。

本輪不是重新發明 taxonomy，也不是開始 topology synthesis；目的只有三個：

```text
1. 用同一套 X1 / X2 / X3 規則重畫 #01～#09
2. 將 Architecture / Strategy / Physical Mechanism / Property 分層
3. 找出哪些 family 名稱其實共享同一 L3 物理機制，哪些只是不同系統安排
```

核心規則：

```text
X1 / X2 / X3 = functional coordinates
NOT mandatory three serial stages

Architecture ≠ Strategy ≠ Physical Mechanism ≠ Resulting Property

P_saved > P_added
```

本文件不宣稱任何 family 優於其他 family，也不建立 Candidate #10。

---

## 2. Common normalization template

每一類固定使用以下欄位：

```text
L1 Architecture / main circuit graph

X1 start
X1 processing region
X1 completion

X2 location / status
X3 location / status
coordinate overlap

L2 Strategy
L3 Physical Mechanism
L4 Resulting Property / Observable

primary added-loss burden
PG relevance
normalization decision
```

### X1 completion rule

只有在以下條件可成立時才宣稱 X1 完成：

```text
- majority main-path power 已離開 source-referenced extreme-LV domain
- 後續主路徑不再用 source-level full current 傳輸同一功率
- 可以指出新的 voltage/current domain
```

若架構直接輸出 AC、沒有中間 HV DC node，則 X1 可以在最終高電壓 AC port 才完成，並允許與 X3 實體重疊。

### X2 rule

```text
有 capacitor ≠ 自動有 X2
```

只有該 storage / switching network 實際承接 2ω 或等效低頻能量擺動時，才標成 X2。

---

## 3. #01 — Low-Frequency Transformer Inverter

### L1 Architecture

```text
LV DC
→ low-frequency inverter / polarity switching
→ line-frequency transformer
→ 220 Vac
```

### X1

```text
X1 start
= LV inverter begins alternating excitation of transformer primary

X1 processing region
= LV switching + line-frequency magnetic transformation

X1 completion
= transformer secondary / high-voltage AC output domain
```

此 family 沒有獨立的高壓 DC intermediate domain；第一次主要 voltage/current-domain transformation 與最終 AC 形成高度綁定。

### X2

```text
X2 = NO INHERENT DEDICATED COORDINATE
```

是否存在 source-side / AC-side low-frequency storage 取決於實作，不由 `low-frequency transformer inverter` 名稱本身保證。

### X3

```text
X3 = low-frequency inverter polarity synthesis + transformer output waveform formation
```

### Coordinate overlap

```text
X1 ≈ X3 = STRONG PHYSICAL OVERLAP
```

### L2 Strategy

```text
single low-frequency magnetic voltage transformation
low switching-event rate
```

### L3 Physical Mechanism

```text
magnetic flux linkage + transformer turns-ratio transformation
semiconductor polarity commutation at low frequency
```

### L4 Resulting Property

```text
low switching-event count
full LV current remains on primary side until LF magnetic transformation
large magnetic VA / mass / volume
```

### Primary added-loss burden

```text
LF transformer copper/core burden
source-domain high-current primary conduction
large magnetic material requirement
```

### PG relevance

```text
PG-1 = RISK / long source-domain full-current exposure
PG-2 = low switching-frequency can reduce event count, but is not soft-commutation mechanism
PG-3 = strong transformation burden reference
PG-4 = no inherent solution
```

### Decision

```text
REFERENCE FAMILY
X1/X3 overlap explicitly recognized
NOT a primary L3 donor for later combination
```

---

## 4. #02 — HFT + Rectifier + HV DC Bus + VSI

### L1 Architecture

```text
LV DC
→ LV HF switching
→ HFT
→ HV rectifier
→ HV DC link
→ VSI
→ 220 Vac
```

ASP-2000 A0 belongs to this family.

### X1

```text
X1 start
= LV HF switch network begins HFT excitation

X1 processing region
= LV HF switching + HFT magnetic transfer

X1 completion
= HFT secondary reaches a high-voltage / reduced-current domain
```

HV rectification occurs after the magnetic domain transformation has already taken place, although its loss remains part of the post-X1 conversion path.

### X2

```text
X2 = HV DC-link capacitor region
ONLY when it actually carries the 2ω energy swing
```

For A0 this is a `passive X2-capable node`; actual source-side 2ω suppression remains a measurement question.

### X3

```text
X3 = HV VSI / H-bridge + PWM AC synthesis
```

### Coordinate overlap

```text
X1 / X2 / X3 = usually physically separated
```

This is the clearest three-coordinate example, but it must not be generalized to all families.

### L2 Strategy

```text
early magnetic X1
post-X1 passive energy buffering
separate reduced-current AC synthesis
```

### L3 Physical Mechanism

```text
transformer turns-ratio magnetic transformation
HF semiconductor commutation
optional resonant / ZVS / ZCS commutation
rectification
capacitor energy storage for 2ω buffering
bridge polarity/amplitude synthesis
```

### L4 Resulting Property

```text
galvanic isolation
reduced-current domain available before X3
large HV energy reservoir possible
soft-switching possible in selected variants
```

### Primary added-loss burden

```text
LV bridge conduction/switching
HFT copper/core/leakage
rectifier loss
HV-link ESR/ripple
separate VSI loss
clamp/snubber loss when dissipative
```

### PG relevance

```text
PG-1 = early X1 is helpful but LV bridge burden remains
PG-2 = strong falsifier through resonant / soft-commutated variants
PG-3 = HFT transformation burden must be fairly optimized
PG-4 = passive post-X1 buffering is an existing solution class
```

### Decision

```text
PRIMARY A0/A1 FALSIFICATION FAMILY
L3 donors = magnetic transformation / soft commutation / passive 2ω buffering
```

---

## 5. #03 — Active-HFT / DAB + VSI

### L1 Architecture

```text
LV active bridge
→ HFT + controlled leakage / series inductance
→ HV active bridge
→ HV node
→ VSI
→ 220 Vac
```

### X1

```text
X1 start
= LV active bridge creates HF excitation

X1 processing region
= LV bridge + transformer + leakage/series-L-mediated active transfer + HV bridge

X1 completion
= HV bridge side / HV node where majority power is in reduced-current domain
```

Unlike #02, the HV bridge is part of the controlled X1 power-transfer process rather than only a passive rectifier boundary.

### X2

```text
X2 = NOT INHERENT FROM DAB LABEL
```

Bidirectional power authority does not itself store the single-phase 2ω energy. X2 exists only if the HV node, storage port or another buffer is intentionally used for that energy swing.

### X3

```text
X3 = downstream VSI / AC stage
```

### Coordinate overlap

```text
X1 physically includes both LV and HV active bridges
X2 may overlap X1 only when an actual buffer function is added
X3 generally separate
```

### L2 Strategy

```text
active bidirectional X1
phase-shift-controlled power transfer
use leakage / series inductance intentionally rather than only parasitically
```

### L3 Physical Mechanism

```text
transformer turns-ratio magnetic transformation
series/leakage inductance energy transfer
phase-shift-controlled bidirectional energy transfer
resonant / ZVS commutation using stored inductive energy
```

### L4 Resulting Property

```text
bidirectional power flow
soft-switching range under suitable conditions
controllable transferred power
possible circulating/backflow current
```

### Primary added-loss burden

```text
second active bridge
extra Coss / Qg / gate drive
circulating RMS and peak current
ratio-mismatch penalty
off-design soft-switching loss
```

### PG relevance

```text
PG-1 = trade-off because early X1 can coexist with high circulating RMS
PG-2 = major existing falsifier
PG-3 = magnetic + active-bridge burden remains
PG-4 = bidirectional authority is enabling capability, not sufficient X2 by itself
```

### Decision

```text
DAB label is L1 architecture shorthand, not one L3 mechanism
retain leakage-mediated transfer + ZVS as L3 donors
```

---

## 6. #04 — Non-Isolated High-Gain DC/DC + VSI

### L1 Architecture

```text
LV DC
→ boost / interleaved / coupled-inductor / multiplier / cascaded gain region
→ HV DC node
→ VSI
→ 220 Vac
```

### X1

```text
X1 start
= first boost / inductor / coupled-inductor / charge-transfer cell begins creating a new voltage/current domain

X1 processing region
= may span multiple interleaved, magnetic and/or capacitor gain cells

X1 completion
= first sustained HV DC node where majority power is in reduced-current domain
```

This is the canonical `distributed-X1` case.

### X2

```text
X2 = HV node / capacitor only if it carries 2ω energy swing
```

The existence of gain capacitors does not make those capacitors X2.

### X3

```text
X3 = downstream VSI
```

### Coordinate overlap

```text
X1 usually distributed but separate from X3
X2 may occupy final HV node
```

### L2 Strategy

```text
distributed / collective voltage building
interleaved current processing when used
galvanic-isolation removal
```

### L3 Physical Mechanism

```text
inductor charge / discharge energy transfer
coupled-inductor magnetic voltage gain
capacitor charge transfer / voltage lift / stacking
diode or synchronous rectification paths
cascaded energy-transfer cells
```

### L4 Resulting Property

```text
continuous-input-current possible in selected variants
branch current sharing possible
high static gain possible
component stress distribution depends on cell structure
```

### Primary added-loss burden

```text
inductor/coupled-inductor copper/core
high-duty operation
leakage/clamp
rectifier/diode loss
capacitor ESR/dielectric/charge-redistribution loss
internal circulating RMS
```

### PG relevance

```text
PG-1 = candidate alternative X1, but only total source-domain I²R matters
PG-2 = replaces one commutation problem with another; not inherently solved
PG-3 = central alternative-transformation benchmark
PG-4 = ordinary HV storage is not inherently superior to #02
```

### Decision

```text
KEEP as distributed-X1 / alternative-transformation benchmark
physical mechanisms must be decomposed; "high-gain" is not an L3 mechanism
```

---

## 7. #05 — Bidirectional DC/DC + VSI

### Taxonomy warning

#05 is not a unique X1 physics family. A bidirectional DC/DC stage can itself be implemented as:

```text
non-isolated buck/boost
isolated DAB / active-HFT
other bidirectional converter forms
```

Therefore #05 is an architecture / energy-routing umbrella and overlaps the physical mechanism space of #03 and parts of #04.

### L1 Architecture

```text
source / battery
↕ bidirectional DC/DC
↕ DC node / energy buffer
→ VSI
→ 220 Vac
```

### X1

```text
X1 = IMPLEMENTATION_DEPENDENT
```

If the bidirectional DC/DC raises the source to an HV node:

```text
X1 start = bidirectional converter input power-processing region
X1 completion = elevated DC node
```

But the actual L3 mechanism must be inherited from its implementation, not from the word `bidirectional`.

### X2

```text
X2 = DC buffer / ripple port
ONLY if intentionally used to absorb/release 2ω energy
```

### X3

```text
X3 = VSI
```

### Coordinate overlap

```text
X1 and X2 may share the same bidirectional stage when that stage actively routes buffer energy
```

### L2 Strategy

```text
controlled bidirectional energy routing
separate buffer authority from AC synthesis
```

### L3 Physical Mechanism

```text
implementation-dependent X1 mechanism
+
buffer charge/discharge energy transfer when actual storage is present
```

### L4 Resulting Property

```text
controllable direction of power flow
ability to steer pulsating power away from source
additional active processing authority
```

### Primary added-loss burden

```text
extra active stage
buffer inductor/capacitor loss
switch conduction/switching
gate/control/sensing
circulating RMS
```

### PG relevance

```text
PG-1 = may worsen source-domain conduction if it adds an LV stage
PG-2 = implementation-dependent
PG-3 = implementation-dependent
PG-4 = strong architecture donor only when actual storage/ripple port exists
```

### Decision

```text
KEEP taxonomy label as energy-routing family
DO NOT treat #05 as a unique L3 X1 mechanism
```

---

## 8. #06 — Single-Stage Boost / Buck-Boost Inverter

### L1 Architecture

```text
LV DC
→ boost / buck-boost energy processing + AC polarity/amplitude synthesis
→ 220 Vac
```

### X1

```text
X1 start
= first boost/buck-boost energy-storage and switching action

X1 processing region
= same main network that raises voltage and synthesizes AC

X1 completion
= high-voltage AC output domain
```

No separate sustained HV DC node is required by the family definition.

### X2

```text
X2 = NOT INHERENT
```

Single-stage operation does not remove the single-phase 2ω energy-balance requirement.

### X3

```text
X3 = same switching network that performs direct AC synthesis
```

### Coordinate overlap

```text
X1 ≈ X3 = STRONG PHYSICAL OVERLAP
```

### L2 Strategy

```text
stage integration
direct boost-to-AC conversion
remove/avoid a separate HV-bus→VSI boundary
```

### L3 Physical Mechanism

```text
inductor charge/discharge energy transfer
boost / buck-boost switching-state energy transfer
semiconductor polarity/amplitude synthesis
```

### L4 Resulting Property

```text
no mandatory full HV DC intermediate bus
fewer explicit conversion boundaries
high boost ratio / duty burden at 12 V input
```

### Primary added-loss burden

```text
large inductor RMS
high duty ratio
switch voltage-current stress
HF ripple
2ω energy management still required
```

### PG relevance

```text
PG-1 = high-risk at 12 V / kW unless source-domain burden is demonstrably lower
PG-2 = stage count reduction is not soft commutation
PG-3 = replaces HFT with inductor/switch burden
PG-4 = no inherent decoupling
```

### Decision

```text
#06 contributes integration strategy + inductor energy-transfer mechanism
"single-stage" itself is not an L3 mechanism
```

---

## 9. #07 — Z-Source / Quasi-Z-Source

### L1 Architecture

```text
LV source
→ L/C impedance network
→ shoot-through-enabled inverter bridge
→ 220 Vac
```

### X1

```text
X1 start
= impedance network begins charge/discharge under shoot-through / non-shoot-through states

X1 processing region
= impedance-network energy exchange + inverter boost states

X1 completion
= boosted internal DC-link / inverter output high-voltage domain
```

Depending on the exact qZ implementation, X1 completion may be an internal boosted rail or may merge into the final AC synthesis process.

### X2

```text
X2 = NOT INHERENT
```

The impedance-network capacitors are not automatically 2ω buffers.

### X3

```text
X3 = inverter bridge AC synthesis
```

### Coordinate overlap

```text
X1 and X3 = PARTIAL PHYSICAL OVERLAP through shared inverter switching states
```

### L2 Strategy

```text
embed boost function into inverter operation
permit shoot-through states
```

### L3 Physical Mechanism

```text
inductor-capacitor impedance-network energy exchange
shoot-through charging / non-shoot-through energy release
semiconductor AC synthesis
```

### L4 Resulting Property

```text
boost capability within inverter
continuous-input-current possible in selected qZ variants
source-ripple reduction possible
additional internal reactive/circulating energy
```

### Primary added-loss burden

```text
impedance-network inductor/capacitor loss
shoot-through current
internal RMS/reactive energy
capacitor voltage stress
control constraints at extreme boost
```

### PG relevance

```text
PG-1 = current-shaping property must not be confused with lower total I²R
PG-2 = no inherent soft-commutation solution
PG-3 = L/C transformation burden replaces HFT burden
PG-4 = intentional decoupling still required if source reflection is material
```

### Decision

```text
continuous input current = L4 property
shoot-through impedance-network exchange = L3 mechanism
```

---

## 10. #08 — Switched-Capacitor / Multilevel Main Path

### Taxonomy warning

#08 is a composite umbrella containing at least two strongly related but not identical architectural modes:

```text
#08-A switched-capacitor / voltage-multiplier gain path
#08-B multilevel AC synthesis path
```

They may be integrated in one circuit, but `switched-capacitor` and `multilevel` are not the same ontology item.

### L1 Architecture

Generic envelope:

```text
LV source
→ capacitor charge-transfer / stacking cells
→ boosted multilevel node or direct multilevel AC synthesis
→ AC or HV node
```

### X1

Mode A:

```text
X1 start = first switched-capacitor charge-transfer cell
X1 processing region = distributed charge-transfer / stacking network
X1 completion = first sustained higher-voltage reduced-current node
```

Mode B when voltage gain and AC synthesis are integrated:

```text
X1 processing extends into multilevel switching network
X1 completion may occur at AC output
```

### X2

```text
ordinary flying / multiplier / switched capacitors ≠ X2 by default
```

Only storage intentionally sized and operated for 2ω energy swing belongs to X2.

### X3

```text
X3 = multilevel voltage-state / polarity synthesis when direct AC output is produced
or downstream VSI if only an HV node is created
```

### Coordinate overlap

```text
X1 and X3 = MAY STRONGLY OVERLAP
```

### L2 Strategy

```text
collective capacitor voltage building
voltage-step distribution across multiple levels
stage integration when gain + AC synthesis share cells
```

### L3 Physical Mechanism

```text
capacitor charge transfer
capacitor voltage stacking / multiplication
switch-state reconfiguration of stored capacitor energy
multilevel voltage-state synthesis
```

### L4 Resulting Property

```text
magnetic-light / magnetic-free gain possible
smaller per-device voltage steps possible
reduced dv/dt possible
balancing / pulsed source current may appear
```

### Primary added-loss burden

```text
charge-redistribution loss
capacitor ESR/dielectric loss
balancing current
capacitor RMS
additional switch/gate loss
startup/precharge complexity
```

### PG relevance

```text
PG-1 = only valid if source-domain pulsed/RMS burden falls overall
PG-2 = may reduce voltage-step stress but introduces charge-redistribution loss
PG-3 = key alternative transformation mechanism
PG-4 = gain capacitors are not automatically low-frequency buffers
```

### Decision

```text
KEEP #08 as umbrella taxonomy
split L3 into charge-transfer/stacking and multilevel synthesis mechanisms
```

---

## 11. #09 — Direct High-Frequency-Link DC–AC

### L1 Architecture

```text
LV DC
→ LV HF switching
→ HFT / HF link
→ matrix / cycloconverter / direct AC stage
→ 220 Vac
```

A full chain of:

```text
HV rectifier → full HV DC link → VSI
```

is not mandatory.

### X1

```text
X1 start
= LV HF switch network begins HFT excitation

X1 processing region
= LV HF switching + HFT magnetic transformation

X1 completion
= HFT secondary / HF-link high-voltage reduced-current domain
```

### X2

```text
X2 = OPTIONAL / IMPLEMENTATION-DEPENDENT
```

Possible locations:

```text
AC-side decoupling
differential buffer
HFL-integrated pulsating-energy routing
```

Direct-HFL architecture alone does not prove adequate 2ω decoupling.

### X3

```text
X3 = matrix / cycloconverter / direct HF-link-to-line-frequency AC synthesis
```

### Coordinate overlap

```text
X1 and X3 are functionally adjacent and may share commutation constraints
X2 may overlap X3 in AC-side/differential decoupling implementations
```

### L2 Strategy

```text
early magnetic X1
remove / integrate separate HV rectifier + full DC-link + VSI boundaries
place 2ω energy handling after X1 when possible
```

### L3 Physical Mechanism

```text
transformer turns-ratio magnetic transformation
HF semiconductor commutation
bidirectional matrix / cycloconverter commutation
direct HF-link-to-AC energy transfer
optional buffer charge/discharge after HFT
```

### L4 Resulting Property

```text
no mandatory full HV DC-link reservoir
fewer explicit post-X1 stages possible
bidirectional switching/commutation burden becomes first-order
2ω routing can be moved away from LV source in selected implementations
```

### Primary added-loss burden

```text
bidirectional switch conduction
matrix/cycloconverter commutation
HF circulating current
control complexity
buffer loss if added
loss of passive HV reservoir if omitted
```

### PG relevance

```text
PG-1 = early magnetic X1 but LV HF bridge still carries source-domain current
PG-2 = major commutation trade-off, not automatic improvement
PG-3 = HFT remains
PG-4 = strong existing falsifier when AC-side/integrated decoupling is used
```

### Decision

```text
Direct-HFL = L1 architecture
matrix/HF-link direct energy transfer = L3 mechanism
AC-side 2ω suppression = separate X2 function, not guaranteed by family name
```

---

## 12. Common nine-family coordinate matrix

```text
Family  X1 completion domain                 X2 inherent?                  X3                    Overlap
-------------------------------------------------------------------------------------------------------------
#01     high-voltage AC after LF transformer NO                            LF inverter + xfmr     X1≈X3 strong
#02     HFT secondary reduced-current domain  HV-link can provide X2       VSI                    mostly separate
#03     HV active-bridge / HV-node domain     no; storage still required   VSI                    X1 spans 2 bridges
#04     distributed gain → HV DC node         HV node may provide X2       VSI                    usually separate
#05     implementation-dependent DC node      conditional buffer/ripple    VSI                    X1/X2 may overlap
#06     high-voltage AC output                no                            integrated network     X1≈X3 strong
#07     boosted internal rail / AC domain     no                            inverter bridge        X1/X3 partial
#08     HV node or direct multilevel AC        no by capacitor label alone  multilevel or VSI      X1/X3 may overlap
#09     HFT secondary / HF-link HV domain     optional AC-side/integrated  direct AC stage        X2/X3 may overlap
```

Research consequence:

```text
There is no universal serial X1 → X2 → X3 topology.
```

---

## 13. Ontology-normalized comparison

### L1 — Architecture examples

```text
#02 HFT + rectifier + HV bus + VSI
#03 active-HFT / DAB + VSI
#04 non-isolated high-gain + VSI
#05 bidirectional DC/DC + VSI
#06 single-stage boost inverter
#07 Z/qZ-source
#08 SC / multilevel umbrella
#09 direct HFL
```

These are circuit-graph families, not mechanisms.

### L2 — Strategy inventory exposed by nine families

```text
S1 early X1 / leave extreme-LV domain early
S2 distributed / collective voltage building
S3 stage integration
S4 post-X1 energy buffering
S5 bidirectional energy-routing authority
S6 place 2ω handling after X1
S7 reduce switching-event frequency
S8 distribute device voltage steps
```

These are design/system arrangements, not proof of loss reduction.

### L3 — Raw physical-mechanism inventory exposed by normalization

The following are the actual same-level objects carried forward for the next deduplication step:

```text
PM-R1  transformer magnetic flux / turns-ratio transformation
PM-R2  inductor charge-discharge energy transfer
PM-R3  coupled-inductor magnetic gain / energy transfer
PM-R4  capacitor charge transfer / voltage stacking / multiplication
PM-R5  impedance-network L/C energy exchange with shoot-through states
PM-R6  leakage/series-inductance-mediated active power transfer
PM-R7  resonant / ZVS / ZCS commutation using stored reactive energy
PM-R8  passive capacitive 2ω energy buffering
PM-R9  active bidirectional buffer charge/discharge / ripple-port transfer
PM-R10 bidirectional matrix / cycloconverter HF-link-to-AC transfer
PM-R11 semiconductor rectification / synchronous rectification
PM-R12 multilevel voltage-state synthesis
PM-R13 bridge polarity/amplitude synthesis
```

`PM-R*` means `RAW`; it is not yet the final deduplicated mechanism dictionary.

### L4 — Resulting property / observable inventory

```text
continuous input current
reduced source ripple
reduced per-device voltage step
reduced dv/dt
bidirectional power capability
soft-switching operating region
reduced stage count
lower / higher circulating RMS
high pulsed source current
```

These properties may be evidence of mechanism behavior, but cannot enter PG compatibility as if they were mechanisms.

---

## 14. Historical MP-A...MP-F mapped onto normalized ontology

```text
MP-A Early X1
→ L2 strategy S1
→ implemented by PM-R1 / R2 / R3 / R4 / R5 depending family

MP-B Soft commutation / leakage-energy utilization
→ L3 PM-R6 + PM-R7

MP-C Collective high-voltage building
→ L2 strategy S2
→ implemented by PM-R2 / R3 / R4 / R5

MP-D Direct / integrated AC synthesis
→ L2 strategy S3
→ implemented by PM-R10 / PM-R12 / PM-R13 plus family-specific X1 mechanism

MP-E Intentional 2ω energy routing
→ L2 strategy S4/S5/S6
→ implemented by PM-R8 / PM-R9 and selected post-HFT routing implementations

MP-F Continuous-input / ripple-current shaping
→ L4 property
→ produced by selected PM-R2 / PM-R5 + modulation/control; not an independent L3 mechanism
```

Therefore:

```text
MP pools remain historical screening aids
but PG compatibility must use deduplicated PM-level mechanisms
```

---

## 15. Taxonomy findings

### Finding T1 — nine families are useful but not mutually exclusive physics classes

```text
#05 overlaps #03/#04 by implementation
#08 is a composite SC + multilevel umbrella
#06/#07/#08 can share integrated boost-to-AC behavior
#02/#03/#09 share magnetic HFT transformation physics
```

This does not invalidate the nine-family working set; it defines its role correctly:

```text
nine families = architecture coverage map
NOT nine mutually-exclusive physical mechanisms
```

### Finding T2 — family novelty and mechanism novelty remain separate

```text
new family label ≠ research novelty
existing family membership ≠ no possible research contribution
```

### Finding T3 — X1 location alone is not a contribution

Different families may all implement early X1 using different L3 mechanisms. The research comparison must remain:

```text
P_preX1,cond saved
+
other removed loss
>
new transformation / commutation / storage / circulating loss
```

---

## 16. Gap-specific consequences after normalization

### PG-1

The correct comparison is not:

```text
which family raises voltage earliest?
```

It is:

```text
which L3 X1 mechanism minimizes total source-domain RMS / conduction burden
under matched output, protection and loss boundary?
```

### PG-2

Stage removal and direct AC synthesis are not equivalent to soft commutation.

Primary relevant raw L3 mechanisms are:

```text
PM-R6 leakage/series-inductance-mediated transfer
PM-R7 resonant / ZVS / ZCS commutation
```

plus baseline hard/dissipative commutation for comparison.

### PG-3

The comparison must be symmetric across:

```text
magnetic transformation
inductor storage
coupled-inductor gain
capacitor charge transfer
impedance-network energy exchange
```

No mechanism is allowed to hide its storage / RMS / charge-redistribution burden.

### PG-4

The correct L3 comparison is between actual energy-buffer/routing mechanisms:

```text
PM-R8 passive capacitive buffering
PM-R9 active bidirectional buffer charge/discharge
selected post-HFT / AC-side implementations using the same underlying storage-transfer physics
```

`Direct HFL` itself is not a 2ω mechanism.

---

## 17. Formal decision

```text
Nine-family taxonomy                       = KEEP AS ARCHITECTURE COVERAGE MAP
Nine-family X1/X2/X3 normalization          = COMPLETE v1
X1/X2/X3 fixed serial-stage interpretation = REJECTED
#05 unique X1-physics interpretation        = REJECTED
#08 single-ontology interpretation          = REJECTED
L1 Architecture separation                 = COMPLETE v1
L2 Strategy separation                     = COMPLETE v1
L3 raw physical-mechanism inventory         = ESTABLISHED / NOT YET DEDUPLICATED
L4 property separation                     = COMPLETE v1
MP-A...MP-F same-level mechanism model      = REJECTED
PG × MP-A...MP-F direct screen              = REJECTED
Candidate #10                              = HOLD / NOT_ASSIGNED
Novelty                                    = NOT_ESTABLISHED
```

Next formal action:

```text
Deduplicate / formalize PM-R1...PM-R13
↓
remove mechanisms that are only support functions or duplicate descriptions
↓
map each surviving L3 mechanism to PG-1...PG-4
↓
then execute PG × Physical-Mechanism compatibility screen
```

No topology combination is authorized by this normalization alone.

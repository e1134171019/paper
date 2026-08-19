# 08 — Decision Log

Purpose: preserve why a research direction was kept, narrowed, corrected or rejected. Newer dated corrections supersede older abstractions; Git history preserves the detailed previous versions.

---

## 2026-08-16 — Research focus fixed

```text
Focus = low-voltage high-current DC→single-phase AC loss/topology study
Anchor = 12 V /2 kW / ~166.7 A ideal
```

Core rule:

```text
loss mechanism → current/energy path → structural requirement → topology candidate
P_saved > P_added
```

Broad novelty claims from modularization, IPOS/current sharing, capacitive isolation, bidirectional buffering, partial power, HF-link or single-stage/direct-HFL alone are closed.

```text
Novelty = NOT_ESTABLISHED
```

---

## 2026-08-17 — Research envelope and family taxonomy fixed

```text
12–24 Vdc /1–3 kW /220 Vac /1φ
```

Nine working power-path families retained. Candidate #10 remains unassigned until a physical gap survives matched benchmarks.

Validation order:

```text
PLECS → LTspice → Maxwell/Q3D → hardware
```

---

## 2026-08-19 — Working architecture retained

```text
12 V source
→ very-short / very-low-R common LV path
→ local bulk + HF decoupling
→ early distributed branch power cells
→ branch switching + X1
→ reduced-current domain
→ [optional active X2]
→ X3
→220 Vac
```

```text
early fan-out = HYPOTHESIS / not automatic loss saving
active X2 = OPTIONAL / must pass P_LV,saved > P_X2,added
```

---

## 2026-08-19 — ASP-2000 R52 promoted to A0 real-product benchmark

A0 already contains heavy MOS paralleling, multiple HFT paths, separate fused center feeds, local LV energy support, collective/series secondary formation and HV DC-link before X3.

Therefore those features alone cannot be credited as candidate novelty or automatic advantage.

A1 is defined as a fair optimized magnetic benchmark and receives equivalent engineering freedom.

---

## 2026-08-19 — Four-independent-bank abstraction rejected

Verified primary structure:

```text
BAT+
├─ four-fuse feed → T1 center tap
└─ four-fuse feed → T2 center tap

T1 A = T2 A → common A switch node
T1 C = T2 C → common C switch node
```

Thus `4 independent 5-MOS converter branches` is rejected as an electrical model.

---

## 2026-08-19 — Q19 and primary-switch architecture resolved

Compiled PCB establishes:

```text
A node →10 connected MOS →B
C node →10 connected MOS →B
Q19 Drain → A node
```

Old `9+10 / Q19 OPEN` model is superseded.

Four physical driver groups serve the two A/C power functions.

Correct current variables:

```text
I_T1/I_T2 = transformer currents
I_A,total/I_C,total = electrical switch currents
DA1/DA2/DB1/DB2 currents = local silicon-subgroup currents
```

Do not use T1/T2 current as an unquestioned proxy for one 5-MOS subgroup switching current.

---

## 2026-08-19 — Battery-negative seven-MOS region classified

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

Verified hardware:

```text
Source →B
Drain →BAT-
12VP → individual 68.1Ω →Gate
Gate → individual 47.5kΩ →B
```

Independent ASP product specification explicitly lists:

```text
Input reverse polarity protection (AUTO-RECOVERY)
```

Decision:

```text
ASP input reverse-polarity function = VERIFIED_AT_PRODUCT_FUNCTION_LEVEL
Q39...Q65 ideal-diode-style implementation = STRONGLY_SUPPORTED
commandable full disconnect by this bank alone = NOT_SUPPORTED
```

This loss is battery-interface protection/sensing overhead, not intrinsic magnetic-X1 loss.

---

## 2026-08-19 — BOCP analog transfer resolved

MAIN-board U4 network is a closed-loop analog amplifier, not the earlier comparator/hysteresis interpretation.

```text
ΔV_M5 = V_B - V_BAT-
V_BOCP - V_B ≈22.1 × ΔV_M5
```

```text
BOCP transfer relation = VERIFIED_FROM_MAIN_BOARD
BOCP exact receiver/trip/control action = OPEN / EVIDENCE_BLOCKED
```

Formal benchmark loss evidence remains:

```text
I_source + ΔV_M5 + temperature
```

BOCP is a product sense-chain cross-check.

---

## 2026-08-19 — Kelvin and dynamic measurement gates defined

Static/Kelvin:

```text
M0 BAT+ distribution
M1 fuse banks
M2 T1 local feed
M3 J8
M4 T2 local feed
M5 B↔BAT− seven-MOS bank
M6 B return copper
```

Dynamic:

```text
fs / duty / dead time
actual VGS
V_A-B / V_C-B
I_T1 / I_T2
synchronous switch-region v×i
primary volt-second
```

No unsynchronized V×wrong-current switching-loss integration is accepted.

---

## 2026-08-19 — RL1 role resolved as HV precharge/soft-start bypass

Direct SchDoc graph:

```text
T2 pin5
│
├─ RL1 power contact ──────────────┐
└─ R40 1k/5W || R41 1k/5W =500Ω ─┤
                                   ↓
                            D2/D6 bridge AC node
```

RL1 identity/control:

```text
OZ-SS-112LM1
12Vdc coil
control net RELAY_SS1
```

Decision:

```text
RL1 HV-secondary precharge / soft-start bypass
= VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
```

Loss accounting:

```text
R40/R41 startup energy = inrush/precharge overhead / not ordinary steady-state X1 loss
RL1 steady contact loss = measurement item
```

---

## 2026-08-19 — Transformer parameter evidence gate tightened

R52 currently establishes only:

```text
T1/T2 = PQ5050
center-tapped primary connectivity
secondary series relationship
```

It does not provide a defensible A0 value for:

```text
populated transformer P/N
turns ratio
Lm/Lk
winding DCR/Rac
core material / Ae / Ve
```

Drive contains `M1-PQ50-V121-A` transformer test data, but model-matrix evidence associates it with `ASP-3000W-24V-200ac-S9C`, not A0.

Decision:

```text
M1-PQ50-V121-A data = CONTEXT_ONLY / DIFFERENT VARIANT
A0 transformer numerical parameters = OPEN
```

---

## 2026-08-19 — PCB copper-loss model corrected by manufacturing specification — CRITICAL

Initial PcbDoc-stack calculations used approximately 35.56 µm copper and produced an ~11.5 W partial-positive-PCB scale.

The direct R52 manufacturing specification tied to the same Gerber instead specifies:

```text
FR4
1.6mm
2 layer
base copper =2.0oz
finished copper thickness >82µm
```

Therefore:

```text
old 35.56 µm geometry-loss model = SUPERSEDED
```

Using 82 µm as the conservative minimum and the same 2D geometry:

```text
BAT+ common ≤~3.32 W @175.4A
T1 local ≤~1.17 W @87.7A
T2 PCB excl. J8 ≤~0.48 W @87.7A
partial positive PCB ≤~4.98 W
```

Research consequence:

```text
PCB distribution remains material
but is NOT proven dominant
```

---

## 2026-08-19 — Primary RC damping and U5 stuffing boundary resolved

Direct A/C adjacency establishes two passive series-RC snubber/damping branches across the primary switched nodes and no direct active recovery branch attached to those A/C nodes.

Decision:

```text
direct primary-node damping = PASSIVE / DISSIPATIVE RC STRUCTURE
P_snubber = OPEN / WAVEFORM_NEEDED
```

R52 also supports U5 buffered command distribution and direct 0Ω bypass options. The exact production stuffing of U5/R212/R213 remains open.

Therefore older wording that treated R212/R213 as definitely populated production timing links is superseded.

---

## 2026-08-19 — A0 optimization is NOT the research task — CRITICAL DIRECTION CORRECTION

A0 reverse engineering has reached the point where continued component-level tracing risks turning the work into an ASP optimization project.

Formal decision:

```text
ASP-2000 R52
= real-product benchmark / evidence source
≠ optimization target
```

A0 structural evidence is now sufficient for a physical-gap screen.

Product-engineering items are no longer independent research targets:

```text
PCB / bus / connector geometry
Fuse / J8 / contacts
battery reverse-protection / BOCP
RL1 / precharge implementation
U5 / stuffing details
exact RC snubber value tuning
```

Continue them only when they discriminate a topology-level hypothesis.

Current physical-gap hypotheses:

```text
PG-1 extreme-LV conduction exposure before X1
= HYPOTHESIS / TOPOLOGY-RELEVANT

PG-2 dissipative commutation / leakage-energy handling
= HYPOTHESIS / STRONG STRUCTURAL SIGNAL

PG-3 magnetic transformation burden at extreme ratio
= OPEN / NOT YET A GAP

PG-4 single-phase 2ω energy reflection into LV source
= HYPOTHESIS / NOT_ESTABLISHED
```

Authoritative screen:

```text
research/25_A0_EVIDENCE_TO_PHYSICAL_GAP_SCREEN.md
```

---

## 2026-08-19 — Exhaustive A0 loss closure no longer blocks mechanism comparison

The previous broad workflow:

```text
measure/close every A0 static + dynamic watt
→ only then build A1 and compare mechanisms
```

is superseded because it over-serves product characterization rather than the research question.

New minimum-evidence workflow:

```text
A0 structural evidence freeze
↓
physical-gap screen
↓
H1 PG-1 conduction discriminator
H2 PG-2 commutation/snubber discriminator
H3 PG-3 magnetic discriminator
H4 PG-4 2ω-routing discriminator
↓
A1 / Direct-HFL / non-isolated X1 mechanism comparison
↓
reject gaps that disappear under fair optimization
↓
only then topology synthesis
```

A1 is therefore no longer blocked by a requirement to fully close every ASP loss term. It begins after the minimum evidence needed to make the mechanism comparison meaningful.

Candidate #10 remains:

```text
HOLD / NOT_ASSIGNED
```

---

## 2026-08-19 — Nine-family mechanism extraction completed v1

The nine working power-path families are retained as taxonomy, but are no longer treated as nine topology blocks to be arbitrarily combined.

Formal extraction record:

```text
research/26_NINE_FAMILY_MECHANISM_EXTRACTION_MATRIX.md
```

Six screening pools are established:

```text
MP-A — Early X1 / leave extreme-LV domain early
MP-B — Soft commutation / leakage-energy utilization
MP-C — Collective high-voltage building
MP-D — Direct / integrated AC synthesis
MP-E — Intentional 2ω energy routing
MP-F — Continuous-input / ripple-current shaping
```

Decision:

```text
technique name ≠ physical-gap solution
```

Therefore the following cannot enter synthesis merely by label:

```text
LLC
DAB
high-gain
switched-capacitor
fan-out
interleaving
remove HV DC bus
active X2 before PG-4 survives
```

Every future combination must pass:

```text
C1 each mechanism maps to a surviving PG
C2 do not duplicate one function while stacking loss
C3 actual circuit graph must be physically compatible
C4 quantify new RMS / circulating / commutation burden
C5 P_saved > P_added
C6 reclassify the completed circuit graph against #01...#09
C7 if it fits an existing family, it is not Candidate #10
C8 discuss #10 only if the physical gap survives and existing families cannot reasonably describe the resulting main energy path
```

The old immediate-next wording `PG × Mechanism compatibility` is superseded by the Definition Gate and ontology normalization decisions below.

---

## 2026-08-19 — M1-PQ50-V108-A recorded as context-only magnetic evidence

A private approval sheet supplied by the user shows a real PQ50-class transfer-type HFT implementation with:

```text
4-turn, 6 mil × 28 mm copper-foil low-voltage windings
30-turn secondary
No Gap core assembly
nonzero measured leakage inductance
MnZn ferrite material options
```

It is useful as physical context for:

```text
PG-1 extreme-LV current/copper burden
PG-2 leakage/commutation energy
PG-3 magnetic transformation burden
```

but no direct part-number linkage to ASP-2000 R52 T1/T2 has been established.

Therefore:

```text
M1-PQ50-V108-A = CONTEXT_ONLY / NOT A0 NUMERICAL EVIDENCE
```

The raw approval PDF is not committed.

Detailed checkpoint:

```text
research/27_MECHANISM_POOL_CHECKPOINT_AND_PQ50_CONTEXT.md
```

---

## 2026-08-19 — X1 / X2 / X3 Definition Gate established v1 — CRITICAL

The previous shorthand definitions were insufficient because they could be misread as three mandatory serial hardware stages.

Formal record:

```text
research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md
```

Decision:

```text
X1 = first major voltage/current-domain transformation FUNCTIONAL REGION
X2 = 2ω / bidirectional energy-buffer and routing FUNCTIONAL COORDINATE
X3 = complete single-phase AC-synthesis FUNCTIONAL REGION
```

Formal overlap rule:

```text
X1 / X2 / X3 MAY overlap physically
but must remain distinguishable by function and loss accounting
```

Therefore:

```text
fixed universal X1 → X2 → X3 three-stage interpretation = REJECTED
```

X1 completion now requires a defensible reduced-current domain for majority main-path power rather than a topology label.

PG-1 `exposure` is operationalized primarily through source-domain RMS/conduction burden, including:

```text
P_preX1,cond
I_source,rms
source-domain semiconductor conduction
```

The research ontology is separated into:

```text
L1 Architecture / Main Circuit Graph
L2 Strategy
L3 Physical Mechanism
L4 Resulting Property / Observable
```

Therefore `MP-A...MP-F` are retained only as historical screening pools and are not six same-level physical mechanisms.

---

## 2026-08-19 — Nine-family X1/X2/X3 normalization completed v1

Formal record:

```text
research/29_NINE_FAMILY_X1_X2_X3_NORMALIZATION.md
```

All nine families were re-expressed using one common template:

```text
L1 architecture
X1 start / processing / completion
X2 status
X3 status
coordinate overlap
L2 strategy
L3 physical mechanism
L4 property
added-loss burden
PG relevance
```

Key decisions:

```text
nine families = ARCHITECTURE COVERAGE MAP
NOT nine mutually-exclusive physical mechanisms

#05 unique X1-physics interpretation = REJECTED
#05 retained as bidirectional energy-routing / architecture umbrella

#08 single-ontology interpretation = REJECTED
#08 retained as composite switched-capacitor / multilevel umbrella

#01/#06/#07/#08/#09 may contain physical X1/X3 overlap
```

A raw same-level L3 inventory is now established:

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

`PM-R*` remains RAW. This raw set is superseded as a direct screening object by the canonical dictionary below.

---

## 2026-08-19 — Canonical L3 physical-mechanism dictionary established v1 — CRITICAL

Formal record:

```text
research/30_L3_PHYSICAL_MECHANISM_DICTIONARY.md
```

The 13 raw entries were normalized into seven canonical same-level L3 mechanism classes:

```text
PM-1 — Magnetic Flux-Linkage Transformation
PM-2 — Inductive Energy Transfer
PM-3 — Capacitive Charge-Transfer / Voltage-Stacking
PM-4 — Reactive-Energy-Assisted Commutation
PM-5 — Capacitive Field-Energy Buffering
PM-6 — Controlled Bidirectional Storage-Port Transfer
PM-7 — Semiconductor Switching-State AC Synthesis
```

Raw normalization decisions:

```text
PM-R1  → PM-1
PM-R2  → PM-2A
PM-R3  → COMPOSITE(PM-1 + PM-2)
PM-R4  → PM-3
PM-R5  → COMPOSITE / architecture-conditioned L/C mechanism
PM-R6  → PM-2B
PM-R7  → PM-4
PM-R8  → PM-5
PM-R9  → PM-6
PM-R10 → PM-7C
PM-R11 → SP-1 support primitive
PM-R12 → PM-7B
PM-R13 → PM-7A
```

Key decisions:

```text
coupled-inductor label ≠ independent primitive L3 mechanism
→ composite PM-1 + PM-2

Z/qZ impedance-network label ≠ independent primitive L3 mechanism
→ composite / architecture-conditioned process

semiconductor rectification ≠ independent physical-gap solution mechanism
→ SP-1 support primitive; its loss remains mandatory in accounting

matrix / cycloconverter, multilevel and ordinary bridge AC synthesis
→ PM-7 implementation variants rather than three unrelated same-level mechanisms
```

Historical mechanism pools are therefore no longer valid direct PG-screening axes:

```text
PG × MP-A...MP-F = REJECTED
```

The next valid screening object is:

```text
PG-1...PG-4 × PM-1...PM-7
```

No mechanism combination, Candidate #10 assignment or novelty claim is authorized by this ontology normalization.

---

## Fair comparison contracts

```text
Contract P — product level
→ match reverse-polarity protection, sensing/fusing and precharge/inrush functions; count losses.

Contract C — steady-state core converter
→ exclude battery-interface overhead and startup-only precharge energy equally across all compared architectures.
```

Forbidden:

```text
candidate deletes A0 product functionality
→ calls removed watts an X1/topology advantage
```

---

## Current decision state

```text
Research phase                         = Physical Gap Validation
A0 role                                = REAL-PRODUCT EVIDENCE / NOT OPTIMIZATION TARGET
A0 structural reverse engineering      = SUFFICIENT_FOR_GAP_SCREEN
R52 finished copper                    = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm geometry-loss model       = SUPERSEDED
partial positive PCB geometry bound    = ≤~4.98 W / NOT_MEASURED
main-MOS conduction scale              = ~12.3 W / DATASHEET_BOUND
battery-interface scale                = ~7.47 W / PRODUCT-INTERFACE DATASHEET_BOUND
A/C passive RC damping                 = VERIFIED
A0 transformer numerical parameters    = OPEN
M1-PQ50-V108-A                         = CONTEXT_ONLY / NOT A0

X1 definition                          = ESTABLISHED v1
X2 definition                          = ESTABLISHED v1
X3 definition                          = ESTABLISHED v1
X1/X2/X3 physical overlap              = ALLOWED
Physical-Gap promotion gate            = ESTABLISHED v1

PG-1                                   = HYPOTHESIS
PG-2                                   = HYPOTHESIS / STRONG SIGNAL
PG-3                                   = OPEN
PG-4                                   = HYPOTHESIS

Nine-family mechanism extraction       = COMPLETE v1
Nine-family X1/X2/X3 normalization     = COMPLETE v1
Nine-family role                       = ARCHITECTURE COVERAGE MAP
Ontology L1/L2/L3/L4                   = ESTABLISHED v1
MP-A...MP-F same-level ontology        = REJECTED
Raw L3 PM-R1...PM-R13 direct screening = SUPERSEDED
Canonical L3 dictionary PM-1...PM-7   = ESTABLISHED v1
Canonical L3 mechanism count           = 7
Support primitive SP-1                 = ESTABLISHED
PG × canonical Physical Mechanism      = NEXT
Mechanism combination                  = NOT YET EXECUTED
A1                                     = FAIR BENCHMARK AFTER COMPATIBILITY / MINIMUM EVIDENCE
Early fan-out benefit                  = NOT_PROVEN
Active X2 benefit                      = NOT_PROVEN
Candidate #10                          = HOLD / NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

---

## 2026-08-19 — PG × canonical physical-mechanism compatibility screen completed v1 — CRITICAL

Formal record:

```text
research/31_PG_PM_COMPATIBILITY_SCREEN.md
```

The valid same-level screening object is now fully executed:

```text
PG-1...PG-4 × PM-1...PM-7
= 28 cells screened
```

Every cell is classified as one of:

```text
DIRECT
CONDITIONAL
TRADE-OFF
RISK
IRRELEVANT
```

Critical interpretation:

```text
compatibility ≠ benefit
compatibility ≠ verified Physical Gap
compatibility ≠ mechanism-combination authorization
compatibility ≠ novelty
```

Primary retained pairs are narrowed to:

```text
PG-1 × PM-1  fair optimized magnetic-X1 falsifier
PG-1 × PM-2  inductive alternative-X1 comparator
PG-1 × PM-3  capacitive-transfer alternative-X1 comparator

PG-2 × PM-4  reactive-energy-assisted commutation / H2-gated

PG-3 × PM-1  magnetic transformation benchmark
PG-3 × PM-2  inductive transformation alternative
PG-3 × PM-3  capacitive-transfer transformation alternative

PG-4 × PM-5  passive 2ω buffering
PG-4 × PM-6  active storage-port routing / H4-gated
```

Conditional modifiers retained only for later accounting / complete-architecture evaluation:

```text
PG-1 × PM-4
PG-2 × PM-2
PG-2 × PM-7
PG-3 × PM-4
PG-3 × PM-7
PG-4 × PM-2
PG-4 × PM-7
```

Secondary trade-off comparator:

```text
PG-2 × PM-3
```

Rejected from primary research lines:

```text
PG-1 × PM-5 / PM-6 / PM-7
PG-2 × PM-1 / PM-5 / PM-6
PG-3 × PM-5 / PM-6
PG-4 × PM-1 / PM-3 / PM-4
```

Hard gates:

```text
PG-2:
H2 must show material P_snubber + avoidable P_switching
before PM-4 becomes a research direction.

PG-4:
H4 must show material source-side 2ω reflection
before PM-5/PM-6 work is justified.
Active PM-6 additionally requires P_LV,saved > P_X2,added.
```

Cross-PG consequence:

```text
PG-1 primary question = PM-1 vs PM-2 vs PM-3 for minimum pre-X1 source-domain burden
PG-2 primary question = whether PM-4 saves more commutation loss than reactive/circulating loss added
PG-3 primary question = PM-1 vs PM-2 vs PM-3 total transformation burden under symmetric accounting
PG-4 primary question = PM-5 vs PM-6 only if H4 survives
```

Mechanism combination remains closed. Do not combine retained mechanisms merely because they survived compatibility screening.

The next valid action is:

```text
Build minimum falsification / evidence plan for retained primary pairs
↓
use H1/H2/H3/H4 only where discriminating
↓
assign fair A1 / B / C comparator roles
↓
reject PGs that fail materiality or P_saved > P_added
↓
only then topology synthesis
```

Candidate #10 remains:

```text
HOLD / NOT_ASSIGNED
```

Novelty remains:

```text
NOT_ESTABLISHED
```

---

## Current decision state — after PG × PM compatibility v1

This state supersedes the earlier `PG × canonical Physical Mechanism = NEXT` line above.

```text
Research phase                         = Physical Gap Validation
A0 role                                = REAL-PRODUCT EVIDENCE / NOT OPTIMIZATION TARGET
A0 structural reverse engineering      = SUFFICIENT_FOR_GAP_SCREEN
R52 finished copper                    = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm geometry-loss model       = SUPERSEDED
partial positive PCB geometry bound    = ≤~4.98 W / NOT_MEASURED
main-MOS conduction scale              = ~12.3 W / DATASHEET_BOUND
battery-interface scale                = ~7.47 W / PRODUCT-INTERFACE DATASHEET_BOUND
A/C passive RC damping                 = VERIFIED
A0 transformer numerical parameters    = OPEN
M1-PQ50-V108-A                         = CONTEXT_ONLY / NOT A0

X1 definition                          = ESTABLISHED v1
X2 definition                          = ESTABLISHED v1
X3 definition                          = ESTABLISHED v1
X1/X2/X3 physical overlap              = ALLOWED
Physical-Gap promotion gate            = ESTABLISHED v1

PG-1                                   = HYPOTHESIS / TOPOLOGY-RELEVANT
PG-2                                   = HYPOTHESIS / STRONG SIGNAL
PG-3                                   = OPEN / NOT YET A GAP
PG-4                                   = HYPOTHESIS / NOT_ESTABLISHED

Nine-family mechanism extraction       = COMPLETE v1
Nine-family X1/X2/X3 normalization     = COMPLETE v1
Nine-family role                       = ARCHITECTURE COVERAGE MAP
Ontology L1/L2/L3/L4                   = ESTABLISHED v1
MP-A...MP-F same-level ontology        = REJECTED
Raw L3 PM-R1...PM-R13 direct screening = SUPERSEDED
Canonical L3 dictionary PM-1...PM-7   = ESTABLISHED v1
Canonical L3 mechanism count           = 7
Support primitive SP-1                 = ESTABLISHED
PG × canonical Physical Mechanism      = COMPLETE v1 / 28 CELLS SCREENED
Primary PG-1 mechanism set             = PM-1 / PM-2 / PM-3
Primary PG-2 mechanism set             = PM-4 / H2-GATED
Primary PG-3 mechanism set             = PM-1 / PM-2 / PM-3
Primary PG-4 mechanism set             = PM-5 / PM-6 / H4-GATED
Minimum falsification/evidence plan    = NEXT
Mechanism combination                  = NOT YET EXECUTED
A1                                     = FAIR FALSIFICATION BENCHMARK / PM-1
Early fan-out benefit                  = NOT_PROVEN
Active X2 benefit                      = NOT_PROVEN / H4-GATED
Candidate #10                          = HOLD / NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

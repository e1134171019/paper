# 31 — PG × Canonical Physical-Mechanism Compatibility Screen v1

Status date: 2026-08-19  
Role: `PHYSICAL-GAP VALIDATION / MECHANISM COMPATIBILITY SCREEN`  
Research object: `PG-1...PG-4 × PM-1...PM-7`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This document executes the first valid same-level compatibility screen after:

```text
research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md
research/29_NINE_FAMILY_X1_X2_X3_NORMALIZATION.md
research/30_L3_PHYSICAL_MECHANISM_DICTIONARY.md
```

The purpose is NOT to combine mechanisms into a new topology.

The purpose is to answer:

> For each current physical-gap hypothesis, which canonical L3 physical mechanisms can causally change the gap quantity, which are only conditional modifiers, which merely shift loss, and which should be rejected from that PG research line?

Hard rules:

```text
P_saved > P_added
matched comparison boundary required
no deletion of product functions on one side only
compatibility ≠ evidence that a gap is verified
compatibility ≠ topology synthesis authorization
compatibility ≠ novelty
```

---

## 2. Status vocabulary

Each PG × PM pair receives one screening status.

```text
DIRECT
= first-order causal relation to the PG quantity; valid primary comparator / falsifier / solution mechanism.
  DIRECT does NOT automatically mean beneficial.

CONDITIONAL
= can affect the PG only when a declared placement, control, storage, commutation or architecture condition is also present.

TRADE-OFF
= directly capable of reducing one part of the target burden, but has a strong known path for relocating loss into another term.
  Keep only if net loss is demonstrably lower.

RISK
= does not directly solve the PG and is likely to add the same burden or an equal/larger burden.
  Use as negative comparator or reject from the primary research line.

IRRELEVANT
= no first-order causal connection to the PG under the current functional definition.
```

Screening status is not a measured performance result.

---

## 3. Summary 4 × 7 matrix

| PG \ PM | PM-1 Magnetic | PM-2 Inductive | PM-3 Capacitive transfer | PM-4 Reactive commutation | PM-5 Capacitive buffer | PM-6 Active storage-port | PM-7 AC synthesis |
|---|---|---|---|---|---|---|---|
| PG-1 pre-X1 LV conduction | TRADE-OFF | TRADE-OFF | TRADE-OFF | CONDITIONAL | IRRELEVANT | RISK | IRRELEVANT |
| PG-2 dissipative commutation | RISK | CONDITIONAL | TRADE-OFF | DIRECT | IRRELEVANT | IRRELEVANT | CONDITIONAL |
| PG-3 total transformation burden | DIRECT | DIRECT | DIRECT | CONDITIONAL | RISK | RISK | CONDITIONAL |
| PG-4 2ω source reflection | IRRELEVANT | CONDITIONAL | IRRELEVANT | IRRELEVANT | DIRECT | DIRECT | CONDITIONAL |

Interpretation:

```text
PG-1 primary X1-mechanism comparison = PM-1 vs PM-2 vs PM-3
PG-2 primary mechanism               = PM-4, with PM-2 as conditional enabler / penalty source
PG-3 primary transformation set      = PM-1 vs PM-2 vs PM-3
PG-4 primary X2 set                  = PM-5 vs PM-6, ONLY if H4 shows material source reflection
```

PM-7 remains important for complete converter architecture and X3 loss, but it is not a standalone X1 or X2 solution mechanism.

---

## 4. PG-1 — Extreme-LV conduction / RMS exposure before X1

Formal quantity:

```text
P_preX1,cond
≈ Σ(I_rms,k² · R_eff,k)
 + Σ(P_semiconductor,cond,k)
```

The unavoidable source average current is not the gap. The research variable is how much source-domain RMS/conduction burden remains before X1 completion and what loss must be added to leave that domain.

### PG-1 × PM-1 — Magnetic Flux-Linkage Transformation

Status:

```text
TRADE-OFF / PRIMARY A1 FALSIFIER
```

Causal path:

```text
source-domain HF/LF switching
→ transformer flux linkage / turns ratio
→ reduced-current secondary domain
```

Potential saved burden:

```text
shortens the full-current path after X1 completion
provides large voltage/current-domain ratio in one magnetic transfer region
```

Added / retained burden:

```text
LV switch conduction
primary winding I²R / Rac
core loss
magnetizing/reactive current
leakage-related burden
```

Falsifier / stop condition:

```text
If a fair optimized PM-1 A1 achieves sufficiently low P_preX1,cond
and alternatives do not produce positive net savings,
then PG-1 does NOT justify leaving the magnetic-X1 solution class.
```

Decision:

```text
KEEP as primary benchmark and falsifier.
Do not treat A0 implementation as the PM-1 optimum.
```

### PG-1 × PM-2 — Inductive Energy Transfer

Status:

```text
TRADE-OFF / PRIMARY ALTERNATIVE X1
```

Causal path:

```text
inductor field-energy transfer
→ voltage gain / altered current domain
```

Potential saved burden:

```text
can establish a reduced-current domain without transformer turns-ratio transfer
may allow distributed X1 / branch processing
```

Added burden:

```text
inductor copper/core
high duty-ratio burden at 12 V-class input
switch conduction
ripple / peak current
circulating current for PM-2B variants
```

Falsifier / stop condition:

```text
Reject PG-1 × PM-2 as a preferred direction if
saved pre-X1 conduction < added inductor + switch + circulating loss.
```

Decision:

```text
KEEP for fair comparison against PM-1.
Do not credit continuous-input current alone as loss reduction.
```

### PG-1 × PM-3 — Capacitive Charge Transfer / Voltage Stacking

Status:

```text
TRADE-OFF / PRIMARY ALTERNATIVE X1
```

Causal path:

```text
charge transfer / series-parallel reconnection
→ collective voltage building
→ reduced-current higher-voltage domain
```

Potential saved burden:

```text
can reduce magnetic transformation dependence
can distribute voltage rise across cells
```

Added burden:

```text
charge-redistribution loss
capacitor ESR / dielectric loss
large capacitor RMS current
additional semiconductor conduction/switching
balancing / precharge burden
```

Falsifier / stop condition:

```text
Reject if capacitor/switch RMS + redistribution loss
cancels the removed magnetic / LV-conduction burden.
```

Decision:

```text
KEEP as primary alternative X1 mechanism.
Switched-capacitor family name alone is not evidence.
```

### PG-1 × PM-4 — Reactive-Energy-Assisted Commutation

Status:

```text
CONDITIONAL / MODIFIER
```

Causal role:

PM-4 mainly changes switching transition loss, not source-domain conduction directly.

Possible indirect benefit:

```text
lower transition loss may permit a different X1 operating point / frequency / device utilization
```

Added burden:

```text
resonant/circulating RMS
reactive component loss
control/dead-time sensitivity
```

Falsifier:

```text
If P_preX1,cond does not fall after the full PM-4-enabled design is counted,
PM-4 is not a PG-1 solution.
```

Decision:

```text
DO NOT treat as a primary PG-1 mechanism.
May accompany a retained X1 mechanism later only after PG-2/overall-loss justification.
```

### PG-1 × PM-5 — Capacitive Field-Energy Buffering

Status:

```text
IRRELEVANT as a primary PG-1 mechanism
```

Reason:

PM-5 stores/releases low-frequency pulsating energy; it does not perform the first major voltage/current-domain transformation.

Decision:

```text
REMOVE from primary PG-1 screen.
Any source-RMS benefit belongs to PG-4 accounting.
```

### PG-1 × PM-6 — Controlled Bidirectional Storage-Port Transfer

Status:

```text
RISK
```

Reason:

An active storage port can add another switch/inductor path, and if located in the LV domain it may increase the very conduction burden PG-1 is trying to reduce.

Potential benefit:

```text
only indirect if it removes a material low-frequency RMS component from the source
```

Added burden:

```text
extra switch conduction/switching
buffer-converter loss
circulating RMS
control/sensing
```

Decision:

```text
REJECT from PG-1 primary line.
Evaluate only under PG-4 after H4.
```

### PG-1 × PM-7 — Semiconductor Switching-State AC Synthesis

Status:

```text
IRRELEVANT as a standalone PG-1 mechanism
```

Reason:

PM-7 synthesizes AC states. It can share hardware with X1 in integrated architectures, but PM-7 by itself does not explain how 12 V-class energy leaves the extreme-LV current domain.

Decision:

```text
REMOVE from primary PG-1 mechanism set.
Count its loss when evaluating a complete architecture.
```

### PG-1 screen result

```text
PRIMARY: PM-1 / PM-2 / PM-3
MODIFIER: PM-4
REJECT FROM PRIMARY LINE: PM-5 / PM-6 / PM-7
```

PG-1 remains:

```text
HYPOTHESIS / TOPOLOGY-RELEVANT
NOT VERIFIED
```

---

## 5. PG-2 — Dissipative commutation / leakage / Coss handling

Formal question:

> Is a material amount of switching/leakage/Coss energy disposed dissipatively, and can it be reduced/recovered with lower total added loss?

### PG-2 × PM-1 — Magnetic Flux-Linkage Transformation

Status:

```text
RISK / SOURCE OF BURDEN, NOT SOLUTION
```

Reason:

PM-1 can introduce leakage and magnetizing-related commutation conditions. The existence of magnetic transfer does not itself recover Coss/leakage energy.

Decision:

```text
Use PM-1 A1 as a fair baseline whose commutation can be optimized,
not as the PG-2 solution mechanism.
```

### PG-2 × PM-2 — Inductive Energy Transfer

Status:

```text
CONDITIONAL
```

Potential causal path:

```text
intentional series/leakage inductance
→ controlled current available during transition
→ may enable soft commutation when paired with PM-4
```

Risk:

```text
circulating current
higher RMS / peak current
extra conduction
```

Falsifier:

```text
If the inductive current required to obtain transition benefit
adds more RMS/conduction loss than the commutation watts saved,
reject the pair.
```

Decision:

```text
KEEP only as an enabler / transfer mechanism paired analytically with PM-4.
PM-2 alone is not a soft-switching claim.
```

### PG-2 × PM-3 — Capacitive Charge Transfer / Voltage Stacking

Status:

```text
TRADE-OFF
```

Potential saved burden:

```text
may remove transformer leakage as a dominant mechanism in some X1 paths
may distribute voltage stress across devices/cells
```

Added burden:

```text
charge redistribution
capacitor RMS
additional switch transitions
Coss remains
possible hard commutation remains
```

Falsifier:

```text
If avoided magnetic/leakage dissipation is replaced by equal/larger
charge-transfer + switching loss, no PG-2 benefit exists.
```

Decision:

```text
SECONDARY comparator, not primary PG-2 solution.
```

### PG-2 × PM-4 — Reactive-Energy-Assisted Commutation

Status:

```text
DIRECT / PRIMARY PG-2 MECHANISM
```

Causal path:

```text
stored reactive energy
→ shapes switch transition
→ lower V×I overlap and/or recovered/reused Coss/leakage energy
```

Potential saved burden:

```text
P_switching overlap
P_snubber / dissipative clamp energy
part of Coss / leakage dissipation
```

Added burden:

```text
resonant / circulating RMS
reactive component loss
residual hard switching
gate/control/dead-time burden
```

Hard falsifier:

```text
If H2 shows A0/A1 avoidable commutation + snubber watts are small,
PG-2 is not material and PM-4 must not become a research direction.
```

Net gate:

```text
P_saved,commutation > P_added,resonant+circulation+control
```

Decision:

```text
KEEP as the primary PG-2 mechanism.
```

### PG-2 × PM-5 — Capacitive Field-Energy Buffering

Status:

```text
IRRELEVANT
```

PM-5 is low-frequency energy buffering; ordinary resonant/commutation capacitors belong to PM-4 context, not PM-5 X2 buffering.

Decision:

```text
REMOVE.
```

### PG-2 × PM-6 — Controlled Bidirectional Storage-Port Transfer

Status:

```text
IRRELEVANT as a PG-2 mechanism
```

A storage-port converter may itself use PM-4, but bidirectional buffer authority does not inherently solve X1 commutation.

Decision:

```text
REMOVE from PG-2 primary screen.
```

### PG-2 × PM-7 — Semiconductor Switching-State AC Synthesis

Status:

```text
CONDITIONAL / SECONDARY
```

Possible benefit:

```text
multilevel / matrix state choice may reduce per-transition voltage step
or remove a separate rectifier/VSI boundary in a complete architecture
```

Risk:

```text
more switching events
more series devices
bidirectional commutation complexity
reverse recovery / Coss
```

Falsifier:

```text
If total commutation energy of the integrated PM-7 implementation
is not lower than the separated reference, reject the claimed PG-2 benefit.
```

Decision:

```text
SECONDARY architecture-dependent modifier only.
```

### PG-2 screen result

```text
PRIMARY: PM-4
CONDITIONAL ENABLER: PM-2
SECONDARY TRADE-OFF: PM-3 / PM-7
REJECT: PM-1 as solution, PM-5, PM-6
```

PG-2 remains:

```text
HYPOTHESIS / STRONG STRUCTURAL SIGNAL
NOT VERIFIED
```

---

## 6. PG-3 — Total transformation burden at extreme conversion ratio

Formal question:

> Under a matched boundary, which physical mechanism accomplishes the required voltage/current-domain transformation with the lowest total burden when all magnetic, inductive, capacitive, semiconductor and circulating losses are counted symmetrically?

This is deliberately mechanism-neutral.

### PG-3 × PM-1 — Magnetic Flux-Linkage Transformation

Status:

```text
DIRECT / PRIMARY BASELINE
```

Burden to count:

```text
primary/secondary copper
core
leakage
magnetizing/reactive current
associated switching/rectification support loss
```

Falsifier role:

```text
A fair optimized PM-1 A1 can falsify the claim that magnetic transformation is structurally inferior.
```

Decision:

```text
KEEP as primary benchmark.
```

### PG-3 × PM-2 — Inductive Energy Transfer

Status:

```text
DIRECT / PRIMARY ALTERNATIVE
```

Burden to count:

```text
inductor copper/core
switch conduction/switching
high duty / current ripple
circulating RMS where applicable
rectification/support loss
```

Falsifier:

```text
If extreme-ratio operation drives PM-2 current/stress loss above fair PM-1,
reject PM-2 as the lower-burden transformation mechanism for this envelope.
```

Decision:

```text
KEEP.
```

### PG-3 × PM-3 — Capacitive Charge Transfer / Voltage Stacking

Status:

```text
DIRECT / PRIMARY ALTERNATIVE
```

Burden to count:

```text
charge redistribution
capacitor ESR/dielectric
capacitor RMS
switch path count
balancing/precharge
```

Falsifier:

```text
If charge-transfer and semiconductor burden exceeds the magnetic/inductive reference,
PM-3 does not establish a lower transformation burden.
```

Decision:

```text
KEEP.
```

### PG-3 × PM-4 — Reactive-Energy-Assisted Commutation

Status:

```text
CONDITIONAL / LOSS MODIFIER
```

Reason:

PM-4 can lower the switching portion of a transformation mechanism but does not itself provide the main voltage/current-domain ratio.

Decision:

```text
Do not rank PM-4 as a fourth transformation mechanism.
Apply it only as a declared modifier to PM-1/PM-2/other switching paths.
```

### PG-3 × PM-5 — Capacitive Field-Energy Buffering

Status:

```text
RISK / OUT-OF-SCOPE FOR PRIMARY TRANSFORMATION
```

Reason:

PM-5 adds storage burden but does not provide the primary extreme-ratio X1 transformation.

Decision:

```text
REMOVE from primary PG-3 set; count it only when a compared architecture requires X2.
```

### PG-3 × PM-6 — Controlled Bidirectional Storage-Port Transfer

Status:

```text
RISK / OUT-OF-SCOPE FOR PRIMARY TRANSFORMATION
```

Reason:

PM-6 adds active processing and storage-port conversion; it does not replace the need for an X1 transformation mechanism unless its implementation itself uses PM-1/PM-2/PM-3.

Decision:

```text
REMOVE as a standalone PG-3 mechanism.
```

### PG-3 × PM-7 — Semiconductor Switching-State AC Synthesis

Status:

```text
CONDITIONAL
```

Possible system-level effect:

```text
X1/X3 integration may remove a separate rectifier / HV-bus / VSI boundary
```

But:

```text
PM-7 alone does not supply the required extreme-ratio transformation physics.
```

Falsifier:

```text
If removed post-X1 stage loss is replaced by larger multilevel/matrix/bridge conduction + commutation burden,
no PG-3 system advantage exists.
```

Decision:

```text
SECONDARY architecture-integration modifier only.
```

### PG-3 screen result

```text
PRIMARY MECHANISM COMPARISON: PM-1 vs PM-2 vs PM-3
MODIFIERS: PM-4 / PM-7
REJECT AS PRIMARY TRANSFORMATION MECHANISMS: PM-5 / PM-6
```

PG-3 remains:

```text
OPEN / NOT YET A GAP
```

The comparison must not assume magnetics are the problem.

---

## 7. PG-4 — Single-phase 2ω energy reflection into the LV source

Formal quantity set:

```text
P_2ω,source
I_2ω,source
E_2ω,buffer
ΔV_buffer,2ω
P_X2,added
```

Hard prerequisite:

```text
H4 must establish material LV-side 2ω reflection before active X2 becomes a research direction.
```

### PG-4 × PM-1 — Magnetic Flux-Linkage Transformation

Status:

```text
IRRELEVANT as an X2 mechanism
```

Reason:

A transformer transfers power between domains; without a storage mechanism it does not absorb the fundamental 2ω energy imbalance.

Decision:

```text
REMOVE from primary PG-4 set.
```

### PG-4 × PM-2 — Inductive Energy Transfer

Status:

```text
CONDITIONAL
```

Reason:

An inductor can be part of an active buffer converter and control instantaneous power flow, but energy must still be stored in a real storage element/port.

Valid role:

```text
implementation mechanism inside PM-6
or short-term reactive transfer supporting a declared X2
```

Decision:

```text
Do not call PM-2 alone an X2 solution.
```

### PG-4 × PM-3 — Capacitive Charge Transfer / Voltage Stacking

Status:

```text
IRRELEVANT as defined
```

Reason:

HF charge-transfer / voltage-lift capacitors are not 2ω buffers by default. If a capacitor is intentionally carrying the low-frequency energy swing, that process is PM-5 instead.

Decision:

```text
REMOVE.
```

### PG-4 × PM-4 — Reactive-Energy-Assisted Commutation

Status:

```text
IRRELEVANT
```

PM-4 acts on switching transitions, not on the single-phase energy-balance requirement.

Decision:

```text
REMOVE.
```

### PG-4 × PM-5 — Capacitive Field-Energy Buffering

Status:

```text
DIRECT / PRIMARY PASSIVE X2 MECHANISM
```

Causal path:

```text
2ω power imbalance
→ capacitor energy swing 1/2 C V²
→ reduced source-side pulsating power
```

Potential saved burden:

```text
reduced I_2ω,source
reduced incremental LV I²R / RMS stress
```

Added burden:

```text
ESR / ripple-current heating
dielectric loss
voltage ripple
energy-storage volume / lifetime
```

Falsifier:

```text
If A0 passive HV-link already suppresses source 2ω sufficiently,
PG-4 may fail and no new X2 direction is justified.
```

Decision:

```text
KEEP as the primary passive falsifier / solution mechanism.
```

### PG-4 × PM-6 — Controlled Bidirectional Storage-Port Transfer

Status:

```text
DIRECT / PRIMARY ACTIVE X2 MECHANISM
```

Causal path:

```text
main path ↔ controlled storage port
→ command energy absorption/release at 2ω
→ isolate pulsating power from LV source
```

Potential saved burden:

```text
reduced I_2ω,source and source RMS
possible reduced passive bulk-energy requirement
```

Added burden:

```text
extra active switches
buffer inductor/capacitor/storage loss
switching / conduction
gate/control/sensing
circulating RMS
```

Hard falsifier:

```text
If H4 shows small source 2ω,
OR
P_LV,saved ≤ P_X2,added,
reject active X2.
```

Decision:

```text
KEEP only behind the H4 hard gate.
```

### PG-4 × PM-7 — Semiconductor Switching-State AC Synthesis

Status:

```text
CONDITIONAL / ARCHITECTURE-INTEGRATION MODIFIER
```

Possible role:

```text
switching-state selection can integrate differential / AC-side energy routing
when an actual storage path is available
```

But:

```text
PM-7 alone has no energy-storage capacity.
```

Added burden:

```text
more device states / commutations
series-device conduction
balancing / matrix control complexity
```

Decision:

```text
Do not treat direct-HFL or multilevel synthesis as a PG-4 solution unless actual PM-5/PM-6 energy storage/routing is identified.
```

### PG-4 screen result

```text
PRIMARY: PM-5 / PM-6
CONDITIONAL IMPLEMENTATION: PM-2 / PM-7
REJECT: PM-1 / PM-3 / PM-4
```

PG-4 remains:

```text
HYPOTHESIS / NOT_ESTABLISHED
ACTIVE X2 = NOT AUTHORIZED BEFORE H4
```

---

## 8. Cross-PG retained mechanism set

After the 28-cell screen, the canonical mechanisms are not all carried forward equally.

### Primary retained pairs

```text
PG-1 × PM-1  fair optimized magnetic-X1 falsifier
PG-1 × PM-2  inductive alternative-X1 comparator
PG-1 × PM-3  capacitive-transfer alternative-X1 comparator

PG-2 × PM-4  direct commutation-loss mechanism

PG-3 × PM-1  magnetic transformation benchmark
PG-3 × PM-2  inductive transformation alternative
PG-3 × PM-3  capacitive-transfer transformation alternative

PG-4 × PM-5  passive 2ω buffering
PG-4 × PM-6  active storage-port routing, H4-gated
```

### Conditional modifiers kept for accounting

```text
PG-1 × PM-4
PG-2 × PM-2
PG-2 × PM-7
PG-3 × PM-4
PG-3 × PM-7
PG-4 × PM-2
PG-4 × PM-7
```

These are NOT independent research directions unless the primary PG and main mechanism survive.

### Rejected from primary lines

```text
PG-1 × PM-5 / PM-6 / PM-7
PG-2 × PM-1 / PM-5 / PM-6
PG-3 × PM-5 / PM-6
PG-4 × PM-1 / PM-3 / PM-4
```

PG-2 × PM-3 remains a secondary trade-off comparator, not a primary direction.

---

## 9. What this screen says about the current research structure

The screen produces four distinct research questions, not one giant mechanism-combination problem.

```text
PG-1
→ Which X1 transformation physics minimizes source-domain conduction burden?
→ primary comparison PM-1 vs PM-2 vs PM-3

PG-2
→ Is dissipative commutation materially large?
→ if yes, can PM-4 save more than its circulating/reactive cost?

PG-3
→ Under the extreme ratio, which complete transformation physics has the lowest total burden?
→ PM-1 vs PM-2 vs PM-3 under symmetric accounting

PG-4
→ Is material 2ω power reaching the LV source?
→ if yes, PM-5 passive buffering vs PM-6 active routing
```

This is intentionally narrower than topology synthesis.

---

## 10. Immediate evidence / falsification gates after compatibility

### PG-1 gate

Use H1 only to establish a defensible A0 source-domain conduction scale.

Then compare:

```text
A1 PM-1
vs
representative PM-2 X1
vs
representative PM-3 X1
```

Matched quantities:

```text
P_preX1,cond
X1 transfer efficiency
M4 circulating/reactive RMS
support-primitive losses
isolation/product contract
```

### PG-2 gate

H2 is a hard materiality gate.

```text
If P_snubber + avoidable P_switching is small
→ PG-2 research direction REJECT

If material
→ PM-4 A1 / active-HFT / resonant falsifier comparison
```

### PG-3 gate

H3 is needed to avoid assuming A0 magnetic burden.

Then compare total transformation burden symmetrically across PM-1 / PM-2 / PM-3.

### PG-4 gate

H4 is a hard prerequisite.

```text
If source 2ω is already sufficiently suppressed
→ PG-4 REJECT / active X2 REJECT

If material
→ compare PM-5 vs PM-6 under
P_LV,saved > P_X2,added
```

---

## 11. Combination gate remains closed

This screen does NOT authorize statements such as:

```text
PM-2 + PM-4 + PM-6 is the new topology
PM-3 + PM-7 is Candidate #10
combine all retained mechanisms
```

Before any mechanism combination:

```text
1. PG must survive its evidence/falsification gate.
2. The pair must show a quantitative path to P_saved > P_added.
3. Redundant functions must be rejected.
4. Added RMS/circulating/commutation burden must be explicit.
5. The completed graph must be reclassified against #01...#09.
```

Candidate #10 remains completely decoupled from mechanism compatibility.

---

## 12. Decision state after screen

```text
PG × canonical PM compatibility screen = COMPLETE v1
28 cells screened                     = YES
mechanism combination                  = NOT EXECUTED

PG-1 primary PM set                    = PM-1 / PM-2 / PM-3
PG-2 primary PM set                    = PM-4
PG-3 primary PM set                    = PM-1 / PM-2 / PM-3
PG-4 primary PM set                    = PM-5 / PM-6, H4-gated

PG-1 status                            = HYPOTHESIS / TOPOLOGY-RELEVANT
PG-2 status                            = HYPOTHESIS / STRONG STRUCTURAL SIGNAL
PG-3 status                            = OPEN / NOT YET A GAP
PG-4 status                            = HYPOTHESIS / NOT_ESTABLISHED

Candidate #10                          = HOLD / NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

Next valid action:

```text
Build the minimum falsification / evidence plan for the retained primary pairs
↓
H1 / H2 / H3 / H4 only where they discriminate a surviving PG
↓
assign fair A1 / B / C comparator roles to PM-1 / PM-2 / PM-3 / PM-4 / PM-5 / PM-6
↓
reject PGs that fail materiality or P_saved > P_added
↓
ONLY THEN discuss mechanism combination / topology synthesis
```

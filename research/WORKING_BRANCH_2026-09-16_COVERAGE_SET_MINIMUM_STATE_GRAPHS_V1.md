# 2026-09-16 — Coverage-Set Minimum State Graphs v1

Status: `WORKING_BRANCH / PRE_MATH / STATE_GRAPH_DRAFT / NO_PRUNING`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

This file executes the next step after `WORKING_BRANCH_2026-09-16_FIRST_COMBINATION_DISCOVERY_MATRIX_V1.md`.

The nine-item coverage set is converted from mechanism labels into **minimum explicit state graphs** before any mathematical validation. The purpose is not to draw production-ready schematics. The purpose is to make each idea explicit enough that the next step can write KCL/KVL, flux, reflected-impedance, RMS-current, commutation-energy and loss equations without inventing missing physics during calculation.

The sequence is fixed:

```text
combination hypothesis
-> minimum physical graph
-> q-state definitions
-> winding roles / current-return paths
-> identify unresolved implementation details
-> MG1...MG9 mathematics
-> PSIM only after sufficient mathematical closure
```

No candidate below is accepted, ranked, or rejected here.

---

## 2. Common notation and state-graph rules

### 2.1 Electrical nodes

```text
Vin+ / Vin-      12-V source terminals
Lin              current-fed input inductance where M1 is used
ICF              current-fed intermediate node after Lin
W1, W2, W3       load-bearing primary or magnetic power ports
S1, S2, ...      secondary power sections
VHV+ / VHV-      high-voltage-side internal nodes when present
B                 explicit energy-buffer port when required
Load              downstream load / next-stage boundary
```

### 2.2 Magnetic variables

```text
Phi_c            common/main transfer flux
Phi_d            differential/local flux
L_c              effective common-mode inductance
L_d              effective differential-mode inductance
L_lk              leakage inductance
L_comm            inductance intentionally used for commutation
N_eff(q)          effective participating turns in structural state q
Z_ref(q)          load impedance reflected to the active input port
```

### 2.3 Role labels

```text
T  = main power transfer
K  = commutation / reset / Coss transition support
S  = temporary magnetic energy storage/release
R  = fine regulation / correction
F  = current-source freewheel / transition-safe state
0  = intentionally inactive or zero-voltage contribution
```

### 2.4 Mandatory legality rule for current-fed states

Any candidate using `M1 Current-fed` must contain a legal current path for `Lin` at every instant. A state transition is invalid if it opens the current-source path without a freewheel/clamp route.

Therefore current-fed graphs below include a generic `qF` state where needed. `qF` is not a claim about the final semiconductor implementation; it is a state-graph requirement.

### 2.5 Reconfiguration rule

Series/parallel/tap/polarity reconfiguration is described here as a connection state of an abstract bidirectional switch network `QS`. The actual semiconductor realization is intentionally left OPEN until mathematics shows the state is worth implementing.

A transition between incompatible winding connections must use break-before-make or another current-safe commutation sequence. Direct make-before-break that shorts unequal induced voltages is illegal.

---

# 3. G01 — M1 + M4: Current-fed entry + reconfigurable effective turns

## 3.1 Intended functions

```text
T1 early low-voltage current distribution
T2 HF magnetic transfer
T3 voltage/current-domain change
T4 reflected-impedance transformation
T6 structural gain / effective-turn reconfiguration
```

## 3.2 Minimum physical graph

```text
Vin+ -- Lin -- ICF --+--> Bridge/leg A --> W1 --+
                     |                          |
                     +--> Bridge/leg B --> W2 --+--> shared magnetic structure
                                                |
                                             S_a,S_b
                                                |
                                      QS secondary/tap network
                                                |
                                             VHV / Load
Vin- <------------------------------------------- return
```

`W1` and `W2` are both load-bearing primary ports. Reconfiguration is initially placed on secondary/tap sections so the first model does not automatically insert an extra series switch in the raw ~175-A input path.

## 3.3 Minimum states

### qA — low-ratio / base-turn transfer

```text
W1 role = T
W2 role = T
S_a active
S_b bypassed or not participating
N_eff = N_s,a / N_p,eq
Lin current path closed through active primary legs
```

Expected:

```text
G_A = f(N_s,a, N_p, modulation)
Z_ref,A = f(N_p, N_s,a, Zload)
```

### qB — high-ratio transfer

```text
W1 role = T
W2 role = T
S_a + S_b series-aiding
N_eff = (N_s,a + N_s,b) / N_p,eq
Lin current path remains closed
```

Expected:

```text
G_B != G_A
Z_ref,B != Z_ref,A
```

### qF — transition/freewheel

```text
primary transfer momentarily disabled or reduced
Lin current recirculates in defined freewheel/clamp loop
secondary QS performs break-before-make transition
no unequal secondary sources are hard-paralleled
```

## 3.4 New research question actually exposed

The first useful question is no longer simply “can a current-fed converter have two ratios?” It is:

```text
Can structural gain be moved to a lower-current winding domain while W1/W2 keep
continuous current-fed power transfer, thereby avoiding a reconfiguration switch
in the highest-current path?
```

## 3.5 OPEN items before mathematics

- exact primary current-sharing law between W1 and W2;
- whether S_a/S_b reconfiguration creates unacceptable diode/switch stress;
- whether qF interval adds excessive circulation;
- turns and polarity are not assigned numerically yet.

---

# 4. G03 — M1 + M8: Current-fed entry + secondary voltage stacking

## 4.1 Minimum physical graph

```text
Vin+ -- Lin -- ICF --+--> power cell A --> W1 || magnetic cell 1 || S1 --+
                     |                                              |
                     +--> power cell B --> W2 || magnetic cell 2 || S2 --+--> series stack --> rectifier/HV
Vin- ---------------------------------------------------------------------- return
```

The first model uses two elemental magnetic cells or two sufficiently separable winding paths. Low-side paths are parallel/current-sharing candidates; high-side induced voltages are series-aiding.

## 4.2 Minimum states

### qT1 — W1 active transfer

```text
W1 = T
W2 = T or staggered-T depending phase schedule
vS1 = induced positive HF contribution
vS2 = induced positive HF contribution
v_stack = vS1 + vS2
```

### qT2 — opposite HF polarity half-cycle

```text
primary polarities reverse according to push-pull/full-bridge host
vS1 and vS2 both reverse consistently
secondary rectifier preserves required HV polarity
```

### qF — current-fed freewheel

```text
Lin current path remains closed during dead/transition interval
secondary series path must not be left with uncontrolled leakage-energy overvoltage
```

## 4.3 Structural equations to be derived next

```text
Iin = iW1 + iW2
Vstack = vS1 + vS2
G_total approximately sum of elemental secondary contributions after rectification
```

The exact gain must be derived from the chosen host state, not assumed from ideal turns alone.

## 4.4 Emergent research question

```text
Can early parallel current handling and later series voltage addition share the same
elemental transformer set so that neither the 12-V current nor the full voltage gain
is concentrated in one component?
```

This is the `primary-parallel / secondary-series` question, but it is not yet assumed to self-balance.

## 4.5 OPEN

- magnetic coupling between elemental cells;
- current-sharing mechanism;
- whether secondary series connection is before or after rectification;
- equal copper/resource baseline.

---

# 5. G05 — M2 + M5: Direct/stored transfer + common/differential magnetic modes

## 5.1 Minimum magnetic graph

Use a magnetic assembly with at least two independent useful modes.

```text
W1 on branch/limb A
W2 on branch/limb B
S_c linked mainly to Phi_c
optional clamp/commutation port K_d linked to Phi_d or local leakage path
```

Modal coordinates:

```text
i_c = (i1 + i2)/2
i_d = (i1 - i2)/2

Phi_c ~ common transfer mode
Phi_d ~ differential/local mode
```

## 5.2 Minimum states

### qT — common-mode direct transfer

```text
W1 = T
W2 = T
v1 and v2 command compatible V/turn and polarity
i1 ~ i2 in same power-transfer sense
Phi_c active
Phi_d ideally small
S_c delivers direct transformer power to output
```

### qS — differential temporary-energy state

```text
main common-mode transfer is reduced or locally interrupted
W1/W2 are driven so differential current increases
net common-flux excitation is small or controlled
energy accumulates mainly in L_d / local leakage:
Wd = 0.5 * L_d * i_d^2
```

### qR — release / reset

```text
differential energy has a defined path:
L_d -> device Coss transition and/or clamp/commutation port K_d
then i_d returns toward zero
qR must not leave stored differential energy trapped
```

## 5.3 Emergent research question

```text
Can one magnetic assembly use common mode for bulk transfer and differential mode
for short-duration stored energy, so that a separate commutation magnetic component
is reduced or removed?
```

## 5.4 Critical falsifier to calculate later

If the differential mode is only ordinary uncontrolled leakage with no independently useful energy path, G05 collapses to a conventional transformer plus parasitic leakage and is not a distinct mechanism.

---

# 6. G11 — M4 + M5: Reconfigurable turns + common/differential modes

## 6.1 Minimum graph

Two equal primary sections are used as the smallest explicit object:

```text
W1 = N turns
W2 = N turns
shared/multi-limb magnetic structure
secondary S = Ns turns
QS can connect W1/W2 as:
  P  = parallel-aiding
  S  = series-aiding
  D  = differential/opposing commutation state
```

## 6.2 States

### qP — parallel-aiding transfer

```text
W1 = T
W2 = T
same induced V/turn condition
primary sections connected electrically in parallel
N_p,eff ~ N
current may divide: iin = i1 + i2
Phi_c = active transfer mode
```

### qS — series-aiding transfer

```text
W1 = T
W2 = T
series-aiding polarity
N_p,eff ~ 2N
same branch current flows through both sections
Phi_c remains main transfer mode
```

### qD — differential / commutation state

```text
W1 and W2 oppose in common-flux contribution
Phi_c reduced
Phi_d / local leakage mode intentionally excited
state used only if a legal L_d energy path exists
```

### qX — safe reconfiguration interval

```text
current transferred to freewheel/clamp or reduced to a legal transition value
parallel and series states are never hard-short-circuited together
```

## 6.3 State-dependent quantities

Target mathematics:

```text
N_eff(qP) != N_eff(qS)
Z_ref(qP) != Z_ref(qS)
L_eff(qD) != L_eff(qP/qS)
```

## 6.4 Emergent question

```text
Can one winding-connection network produce two useful transfer ratios plus a third
magnetic commutation mode, or do the required transition switches/circulating currents
erase the multifunctional benefit?
```

---

# 7. G15 — M5 + M6: Magnetic modes + controllable leakage/resonance

## 7.1 Minimum magnetic requirement

G15 is only meaningful if the assembly has at least two distinguishable inductive behaviors:

```text
transfer mode:      L_lk,T small enough for efficient power transfer
commutation mode:   L_comm,K intentionally larger / energy-usable
```

A multi-limb or split-winding geometry is allowed; a single ideal transformer with one undifferentiated leakage value is insufficient to prove the hypothesis.

## 7.2 States

### qT — tightly coupled transfer mode

```text
W1/W2 excitation reinforces Phi_c
secondary S linked strongly to Phi_c
power flows input -> W1/W2 -> S -> output
reactive current should be limited
```

### qK — high-L differential commutation mode

```text
W1/W2 switch relation changes so common induced voltage is reduced
current is redirected into a differential/local-flux path
L_eff = L_comm,K
stored energy = 0.5*L_comm,K*Icomm^2
energy is used to charge/discharge switch-node capacitances
```

### qR — return to transfer

```text
Coss transition completed
residual differential current returned/recycled
W1/W2 restore compatible common-mode transfer excitation
```

## 7.3 Mathematical target

Next stage must establish both:

```text
0.5*L_comm,K*Icomm^2 >= E_required,Coss
```

and

```text
incremental RMS/copper/core loss from qK < useful switching-loss reduction
```

## 7.4 New research question

```text
Can magnetic geometry make coupling state-dependent enough that the same hardware
is low-leakage while transferring and deliberately high-inductance while commutating?
```

---

# 8. G16 — M5 + M7: Magnetic modes + polyphase role rotation

## 8.1 Minimum object

This candidate requires three symmetric load-bearing branches because two branches cannot realize the proposed `0/120/240 deg` rotating role set.

```text
WA, WB, WC on a magnetic structure with sufficient modal rank
secondary/output combination = common power receiving structure
phase commands = 0°, 120°, 240° at HF switching scale
```

## 8.2 Role sequence

```text
q0: (A,B,C) = (T,T,K)
q1: (A,B,C) = (T,K,T)
q2: (A,B,C) = (K,T,T)
repeat
```

`K` means the branch is temporarily assigned to commutation/reset/support, not necessarily zero current.

## 8.3 State q0 example

```text
WA = T, participates in main transfer mode
WB = T, participates in main transfer mode
WC = K, redirected into local/differential commutation mode

Pout_inst = PA + PB + Pbuffer/other transient support
```

q1 and q2 rotate the same role without permanently assigning one winding as auxiliary.

## 8.4 Required modal condition

The candidate is invalid if putting WC in K necessarily forces WA/WB out of their legal transfer flux state due to a single inseparable common flux.

Therefore next mathematics must test magnetic rank and coupling matrix.

## 8.5 Emergent research question

```text
Can a multiwinding magnetic structure support role rotation in magnetic mode space,
not merely three separate transformers with interleaved PWM?
```

## 8.6 Power-continuity issue

When one branch is in K:

```text
missing instantaneous transfer power must be supplied by:
1. increased PA/PB,
2. stored energy,
3. output capacitance/buffer,
or a combination.
```

This must be quantified before PSIM.

---

# 9. G21 — M9 + multiwinding SST principle: Bulk path + small regulating port

## 9.1 Minimum graph

```text
                    +--> Wb --> magnetic bulk path --> Sb ----+
Vin / DC source ----|                                        +--> series/summing node --> output
                    +--> Wr --> active regulating path --> Sr -+
```

`Wb/Sb` carries most of the power. `Wr/Sr` is a lower-VA bidirectional regulating port. `Sr` is connected so its induced/corrective voltage can be added or subtracted from the bulk secondary contribution.

## 9.2 States

### q0 — bulk-only / zero correction

```text
Wb = T
Wr = 0 or circulating-minimum state
Vout approximately Vbulk
Preg approximately 0
```

### q+ — positive correction

```text
Wb = T
Wr = R
Sr polarity adds to Sb
Vout = Vbulk + Vreg
Preg > 0 in correcting direction
```

### q- — negative correction / energy return

```text
Wb = T
Wr = R
Sr polarity subtracts from Sb or active port returns energy
Vout = Vbulk - |Vreg|
regulating port may process bidirectional correction power
```

## 9.3 Key variable

```text
alpha = |Preg| / Pout
```

The concept only retains its partial-power meaning if `alpha` remains materially below 1 over the required operating envelope.

## 9.4 Emergent question

```text
Can a small multiwinding regulation port correct a nearly fixed-ratio bulk transfer path
without forcing all 2 kW through the regulating semiconductor set?
```

## 9.5 OPEN

- whether series injection preserves required galvanic-isolation boundary;
- circulating power between bulk and regulating ports;
- fault state if regulating port saturates or loses control.

---

# 10. G22 — M10 + matrix-type SST principle: Direct HF-link / matrix states

## 10.1 Minimum graph

This candidate intentionally challenges the fixed chain `HFT -> rectifier -> stiff HVDC -> VSI`.

```text
12-V-side HF power cells
        |
     W1/W2...
        |
 multiwinding / matrix magnetic link
        |
 segmented secondary HF sources S1,S2,...
        |
 bidirectional matrix connection network QM
        |
 output filter / 220-V single-phase port
        |
 explicit buffer port B if required for 2omega energy
```

## 10.2 Minimum output states

### qP — positive output contribution

```text
QM connects selected secondary HF packet(s) with positive load polarity
vo_state > 0 after HF averaging/filter action
```

### qN — negative output contribution

```text
QM connects selected secondary HF packet(s) with reversed load polarity
vo_state < 0
```

### qZ — zero/freewheel contribution

```text
load current has a legal freewheel path
secondary sources are not shorted incompatibly
vo_state approximately 0
```

### qB+ / qB- — buffer exchange, only if explicit storage is present

```text
B absorbs power when HF transfer exceeds instantaneous single-phase load demand
B releases power when load demand exceeds instantaneous source-side average transfer
```

## 10.3 Non-negotiable boundary equation

For single-phase output:

```text
p_o(t) = P * [1 - cos(2*w_line*t)]
```

Therefore removal of a conventional DC link does not remove the `2omega` energy requirement. G22 is illegal as a complete system if no real storage/routing mechanism closes that energy difference.

## 10.4 Emergent research question

```text
Can useful AC polarity/level states be formed inside the magnetic/matrix stage while
keeping 2omega buffering explicit, so that post-HFT processing is reduced rather than
merely hidden?
```

---

# 11. G25 — M1 + M4 + M6: Current-fed + reconfigurable turns + controllable leakage

## 11.1 Why this candidate exists

G25 combines three previously separate functions into one state law:

```text
source-current behavior
+ structural gain / reflected impedance
+ commutation-energy inductance
```

The target relationship is:

```text
q -> {Iin path, N_eff(q), Z_ref(q), L_comm(q)}
```

## 11.2 Minimum graph

```text
Vin+ -- Lin -- ICF -- QS/primary drive network -- W1,W2 -- shared multi-mode magnetic structure -- S -- output
                         |                       |
                         +---- freewheel F ------+
```

W1 and W2 are equal or sectioned load-bearing windings. `QS` permits at least parallel-aiding, series-aiding and differential/opposing states.

## 11.3 States

### qP — current-sharing transfer

```text
W1/W2 = parallel-aiding transfer
N_eff,P ~ N
Iin = i1 + i2
Phi_c active
L_comm not intentionally dominant
```

### qS — high-effective-turn transfer

```text
W1/W2 = series-aiding transfer
N_eff,S ~ 2N
same series current flows through both sections
Phi_c active
Z_ref,S differs from Z_ref,P
```

### qK — differential commutation

```text
W1/W2 common-flux contributions oppose or substantially cancel
main output transfer is reduced during the short interval
current redirected into L_d / L_comm
Ecomm = 0.5*L_comm,K*Icomm^2
```

### qF — current-source-safe transition

```text
Lin current always has a closed path
QS moves between qP/qS/qK using break-before-make or equivalent safe commutation
no unequal induced winding voltages are hard-paralleled
```

## 11.4 What must be proven mathematically

```text
1. qP and qS are both legal steady transfer states.
2. volt-second balance holds in every periodic sequence.
3. qK provides enough commutation energy without excessive circulating RMS.
4. transitions do not create destructive current spikes.
5. any extra QS conduction loss in the 12-V domain does not erase the benefit.
```

## 11.5 Emergent research question

```text
Can one current-fed multiwinding connection sequence provide:
- low-side current distribution,
- two structural gain / impedance states,
- and an intentional high-L commutation state,
without requiring three separate magnetic functions?
```

This is the most direct embodiment of `one structural state controls multiple power functions`, but it remains entirely unproven at this stage.

---

# 12. Cross-candidate comparison after explicit state graphs

The state-graph exercise changes the emphasis compared with the mechanism-only matrix.

| Candidate | Minimum distinct physical requirement | Main mathematical bottleneck exposed |
|---|---|---|
| G01 | current-fed dual power ports + lower-current turn reconfiguration | gain / Zref change versus reconfiguration loss |
| G03 | low-side parallel power paths + high-side series voltage addition | real current sharing and series-voltage balance |
| G05 | at least two useful magnetic modes | whether differential energy is independently usable |
| G11 | legal parallel/series/opposing winding connection network | transition current + `Neff/Zref/Leff` closure |
| G15 | geometry with different transfer and commutation inductance modes | ZVS energy versus reactive RMS penalty |
| G16 | >=3 branches + sufficient magnetic modal rank | transfer continuity while one branch is K |
| G21 | bulk power winding + lower-VA correction winding | processed-power fraction `alpha` and circulation |
| G22 | bidirectional secondary matrix states + explicit buffer | direct AC states versus `2omega` closure |
| G25 | current-fed input + P/S/D winding states + safe freewheel | simultaneous gain/current/ZVS benefit versus low-side QS loss |

This is not a ranking. It identifies what mathematics must decide next.

---

# 13. Mathematics execution order now enabled

The next stage should not calculate all nine simultaneously. Use a coverage-preserving mathematical sequence:

```text
Math-A: G03  -- simplest current-split + voltage-stack power graph
Math-B: G11  -- reconfigurable turns + modal state
Math-C: G15  -- transfer-mode vs commutation-mode inductance
Math-D: G21  -- partial-power fraction
Math-E: G16  -- role rotation / instantaneous power continuity
Math-F: G25  -- integrated current-fed + gain + commutation state
Math-G: G22  -- direct AC-state and 2omega closure
```

G01 and G05 can be evaluated alongside G11/G15 because their equations are subsets/near-neighbors of those state spaces.

For each mathematics package apply:

```text
MG1 state legality / KCL-KVL
MG2 volt-second and flux balance
MG3 ampere-turn and current sharing
MG4 gain and reflected impedance
MG5 RMS / peak / VA stress
MG6 commutation / resonance energy
MG7 energy conservation
MG8 first loss ledger
MG9 single-phase boundary closure when applicable
```

No PSIM model is authorized by this file alone.

---

# 14. Current research status

```text
Named-topology search            = BROAD SEED COMPLETE / EXPANDABLE
M1...M10 mechanism set           = RETAINED
T1...T13 multiwinding targets    = DEFINED
G01...G28 broad combinations     = GENERATED / PRE_MATH
coverage state graphs            = G01,G03,G05,G11,G15,G16,G21,G22,G25 DRAFTED
mathematical validation          = NOT_EXECUTED
PSIM                             = NOT_EXECUTED
hardware                         = NOT_EXECUTED
novelty                          = NOT_ESTABLISHED
Candidate #10                    = HOLD / NOT_ASSIGNED
```

Immediate next: execute `Math-A / G03` first, then `Math-B / G11`, unless a contradiction appears that requires revising the state graph before further calculation.

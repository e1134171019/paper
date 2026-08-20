# 49 — Mainline Restore: R7 / R8 Multi-Assistant Gate-A Screen v1

Status date: 2026-08-20  
Role: `MAINLINE RESTORATION / R7-R8 FIRST-PRINCIPLES / MULTI-ASSISTANT IEEE GATE A`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ; 350 Vdc working HV-link target for synthesis`  
Evidence status: `THEORETICAL + MULTI-ROUTE PRIOR-ART SCREEN`  
Simulation status: `NOT EXECUTED FOR R7/R8`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Mainline correction

Files 45–48 remain useful comparator evidence, but the Ryan/R2 deep-dive is no longer the immediate research mainline.

Formal role correction:

```text
R2-REF2 / Ryan 1998
= EXTREME-LV COMPARATOR / FALSIFIER
= NOT PROJECT FOUNDATION
= NOT NEXT TOPOLOGY-SYNTHESIS DIRECTION

Ryan deep-dive
= PAUSED
```

Reason:

```text
The project was established to search the architecture/mechanism space
for a majority-power graph that reduces extreme-LV loss,
not to continue optimizing one prior-art paper after it falsifies an R2 novelty path.
```

The restored mainline is:

```text
#01...#09 architecture coverage
→ X1/X2/X3
→ PM1...PM7
→ mechanism combination
→ first-principles burden
→ actual graph synthesis
→ multi-assistant IEEE Gate A/B
→ simulation only for surviving graphs
```

---

## 2. Branches reopened

From File 36:

```text
R7 = PM1 + PM3 + PM7
   = magnetic transformation
   + capacitive charge-transfer / voltage stacking
   + AC synthesis

R8 = PM2 + PM3 + PM7
   = inductive boost transfer
   + capacitive charge-transfer / voltage stacking
   + AC synthesis
```

The question is NOT whether these mechanism pairs have ever been combined.

The question is whether an actual complete graph can be derived that is favorable specifically under the project constraint:

```text
12 V / ~175 A source domain
→ leave extreme-LV domain with minimum added all-current impedance
→ perform additional complexity after current has been reduced
```

---

## 3. First-principles R7 current-domain screen

Use a 350-V working HV-link target.

For R7, let PM3 supply an ideal stacking factor `k` after PM1.

```text
Vmid = 350 / k
G_PM1 = Vmid / 12
I_PM3,95 ≈ 2000 / (0.95 Vmid)
```

Results:

| k | Vmid after PM1 | PM1 gain proxy | PM3-domain current @95% |
|---:|---:|---:|---:|
| 2 | 175.0 V | 14.58× | 12.03 A |
| 3 | 116.7 V | 9.72× | 18.05 A |
| 4 | 87.5 V | 7.29× | 24.06 A |
| 5 | 70.0 V | 5.83× | 30.08 A |
| 6 | 58.3 V | 4.86× | 36.09 A |

Representative compromise retained for synthesis:

```text
k = 3
PM1 ratio proxy ≈ 9.72×
PM3 current domain ≈ 18.05 A
```

Compare with source-domain current:

```text
I_source,95 ≈ 175.44 A
```

Thus PM3 placed after the magnetic transformation does not process the full 175-A source current.

For the same 20-W `I²R` allowance:

```text
R_allow = P / I²
```

source domain:

```text
R_allow,12V ≈ 0.650 mΩ
```

R7 k=3 post-PM1 domain:

```text
R_allow,PM3 ≈ 61.4 mΩ
```

Ratio:

```text
~94× greater resistance tolerance after the current-domain transformation
```

This is a structural reason to require:

```text
PM3 POST-MAGNETIC / POST-CURRENT-REDUCTION
```

rather than adding a switched-capacitor network directly in the 12-V / 175-A path.

---

## 4. First-principles R8 burden screen

For R8:

```text
Greq = 350 / 12 = 29.17
G_PM2 = Greq / k
D = 1 - 1/G_PM2
```

Representative results:

| k | Vmid after PM2 | PM2 gain | ideal Boost duty | PM2 input-inductor average current |
|---:|---:|---:|---:|---:|
| 4 | 87.5 V | 7.29× | 86.3% | ~175.4 A |
| 6 | 58.3 V | 4.86× | 79.4% | ~175.4 A |
| 8 | 43.75 V | 3.65× | 72.6% | ~175.4 A |
| 10 | 35.0 V | 2.92× | 65.7% | ~175.4 A |
| 13 | 26.9 V | 2.24× | 55.4% | ~175.4 A |

R8 improves the extreme 96% duty of PM2-only, but it does NOT remove the central source-domain burden:

```text
input boost inductor
+ boost switching path
still process the full ~175-A source current before X1 completion
```

Therefore R8 has a structural disadvantage relative to R7 for the current project's loss authority, unless a later actual graph proves that the pre-X1 equivalent impedance is exceptionally small.

---

## 5. Multi-assistant prior-art protocol used

File 43 was applied.

Completed routes:

```text
Role A — IEEE-direct web-visible IEEE Xplore search
Role B — Exa semantic academic/web search
Role C — Sider Scholar / OpenAlex / Google-Scholar-style academic search
```

Qu Review was not needed for this Gate-A family classification because no differentiated/novel claim is being granted.

Query dimensions included:

```text
R7:
isolated high-step-up
HFT / built-in transformer / coupled magnetic conversion
voltage doubler / voltage multiplier / switched-capacitor cell
secondary-side charge transfer

R8:
boost-derived high-step-up
switched-inductor / inductive transfer
switched-capacitor / voltage multiplier
transformerless high-gain
```

---

## 6. R7 Gate-A prior-art result

All routes independently show that the generic combination

```text
magnetic/coupled transformation
+
capacitive voltage multiplication / stacking
```

is mature prior art.

Representative closest IEEE set includes:

1. `IEEE Xplore 9663167` — *An Interleaved High Step-Up DC-DC Converter Based on Integration of Coupled Inductor and Built-in-Transformer With Switched-Capacitor Cells for Renewable Energy Applications*.
   - two coupled inductors + built-in transformer + switched-capacitor voltage multiplier cells;
   - reported 400-V output and voltage gain 25 with experimental prototype;
   - directly demonstrates that sharing gain among magnetic elements and SC cells is established.

2. IEEE TPEL 2012, DOI `10.1109/TPEL.2012.2183620` — *Single-switch high step-up converters with built-in transformer voltage multiplier cell*.
   - built-in transformer + voltage-multiplier family is established prior art.

3. `IEEE Xplore 9047805` — high-frequency planar-transformer isolated DC-DC converter with voltage-doubler rectification.
   - isolated transformer plus secondary-side capacitive doubling is an established architecture primitive.

Additional neighboring prior art includes isolated Y/Z/qZ-source push-pull converters with voltage-doubling rectifiers and active-clamped push-pull converters with secondary voltage doublers.

Formal Gate-A decision:

```text
R7 mechanism combination
= KNOWN_MECHANISM_COMBINATION

R7 as generic "transformer + voltage multiplier"
= STOP_AS_NOVELTY

R7 as graph-synthesis branch under an extreme-LV current-domain constraint
= CONTINUE_FOR_GRAPH_DIFFERENTIATION
```

Meaning:

```text
We may continue to derive a graph.
We may NOT claim novelty from PM1+PM3 itself.
```

---

## 7. R8 Gate-A prior-art result

All routes independently show that

```text
boost / switched-inductor transfer
+
switched-capacitor / voltage-multiplier gain
```

is an extremely dense prior-art space.

Representative IEEE set includes:

1. `IEEE Xplore 8887543` — *Nonisolated High-Step-Up DC–DC Converter Derived from Switched-Inductors and Switched-Capacitors*.
2. `IEEE Xplore 7605464` — *Generation of a Family of Very High DC Gain Power Electronics Circuits Based on Switched-Capacitor-Inductor Cells Starting from a Simple Graph*; systematic graph-based family generation and experimental verification already exist.
3. `IEEE Xplore 9384179` — *Hybrid High Voltage Gain Transformerless DC–DC Converter* combining boost-inductor behavior with multiplier / switched-capacitor cells; experimental prototype reported.
4. Recent IEEE switched-inductor / switched-capacitor high-gain families continue to extend the same mechanism space.

Formal Gate-A decision:

```text
R8 mechanism combination
= KNOWN_MECHANISM_COMBINATION

R8 generic topology novelty
= HIGH PRIOR-ART DENSITY

R8 immediate synthesis priority
= DEPRIORITIZE

R8 role
= RETAIN AS NON-MAGNETIC COMPARATOR / RESERVE GRAPH BRANCH
```

R8 is not deleted. It is deprioritized because it combines high prior-art density with a full-current pre-X1 boost path at the 12-V anchor.

---

## 8. R7 first graph-design constraint

The next R7 graph must obey all of the following before it is allowed into Gate B:

```text
R7-G1  PM3 must be downstream of a substantial PM1 current reduction.
R7-G2  No added PM3 switch/capacitor is allowed in the 175-A full-source series path.
R7-G3  Capacitors must charge from secondary/intermediate-voltage nodes and stack only after magnetic current reduction.
R7-G4  Charge-transfer RMS / ESR / redistribution loss must be explicit.
R7-G5  Transformer-ratio reduction must be paid for by measurable PM3 loss, not treated as free gain.
R7-G6  X1 completion must be defined from the actual majority-power path, not from component labels.
R7-G7  Complete graph must be compared against transformer + voltage-doubler/VMC prior art, not merely against R2/Ryan.
```

---

## 9. R7-C1 working graph concept — NOT YET A TOPOLOGY CANDIDATE

Working identifier:

```text
R7-C1 = POST-MAGNETIC SERIES/PARALLEL CHARGE-STACKING GRAPH
```

Functional skeleton:

```text
12-V source
→ low-impedance primary switching stage
→ HFT magnetic transformation (PM1)
→ ~100–120-V-class isolated secondary domain
→ PM3 capacitors charged from secondary sub-rails
→ PM3 capacitors reconfigured / rectified into series-aiding output
→ ~350-V HV link
→ HV VSI / PM7
→ 220 Vac
```

Representative static seed:

```text
k_PM3 = 3
G_PM1,proxy ≈ 9.72×
Vmid ≈ 116.7 V
I_PM3-domain,95 ≈ 18.05 A
```

Critical distinction from a generic VDR/VMC is not yet established.

The exact:

```text
secondary winding count
flying-capacitor node edges
diode vs active-switch edges
parallel-charge state
series-discharge state
rectifier integration
```

remain OPEN.

Therefore:

```text
R7-C1 = GRAPH CONCEPT ONLY
Gate B = NOT STARTED
Topology Candidate = NOT GRANTED
Novelty = NOT_ESTABLISHED
```

---

## 10. Mainline decision after this execution

```text
R2 / Ryan deep-dive
→ PAUSE / comparator only

R7
→ PRIMARY NEXT SYNTHESIS BRANCH
→ mechanism combination known
→ continue only through actual graph differentiation

R8
→ KNOWN + dense prior art + pre-X1 175-A burden
→ comparator / reserve

R6
→ remains close-prior-art secondary branch

R9
→ reserve due mechanism-count / interaction-loss risk
```

This restores the original research intent:

> Search for a complete majority-power graph that changes how the 12-V hundred-ampere energy leaves the extreme-LV domain; do not adopt one prior-art paper as the research foundation merely because it is a strong comparator.

---

## 11. Immediate next action

Do NOT simulate R7-C1 yet.

Next:

```text
1. Generate two concrete R7-C1 graph variants from the post-magnetic constraint.
2. Lock exact nodes/edges and charge/discharge states.
3. Derive gain and capacitor RMS/charge-transfer equations.
4. Run multi-assistant IEEE Gate B graph-to-graph.
5. Kill SAME_GRAPH / NEAR_GRAPH variants before PSIM.
6. Simulate only a surviving structurally differentiated graph.
```

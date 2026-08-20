# 45 — R2-C3 Multi-Assistant Prior-Art Screen and R2-REF2 Lock v1

Status date: 2026-08-20  
Role: `R2-C3 EARLY STOP / MULTI-ASSISTANT IEEE SCREEN / EXTREME-LV REFERENCE LOCK`  
Research boundary anchor: `12 Vdc / 2 kW / 220 Vac / 1φ`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Candidate screened

`R2-C3` was generated to repair the R2-C2 auxiliary-switch defect by removing the new hard-switched shuttle switch.

Working concept:

```text
center-tapped push-pull main path
+
no added sustained auxiliary active path
+
use transformer magnetizing / leakage current during commutation
+
main-MOS Coss / body-diode transition
→ main switch ZVS
```

The intended project objective was:

```text
PM-4 exists only during commutation
+
no new full-current 12 V series device
+
no auxiliary switch that merely relocates the switching loss
```

This objective remains useful, but the mechanism itself is not new.

---

## 2. Multi-assistant verification route

Per File 43, the screen used multiple independent search routes.

### Route A — direct IEEE-focused web search

Search families:

```text
push-pull magnetizing-current ZVS
push-pull passive resonant commutation
push-pull lossless snubber
push-pull resonant transition
low-voltage high-current push-pull ZVS
```

Key IEEE hit:

M. J. Ryan, W. E. Brumsickle, D. M. Divan, and R. D. Lorenz,
"A New ZVS LCL-Resonant Push-Pull DC-DC Converter Topology,"
IEEE Transactions on Industry Applications, vol. 34, no. 5, 1998,
DOI `10.1109/28.720458`.

### Route B — Exa semantic search

Independently recovered the same Ryan et al. paper and neighboring literature on magnetizing-current-assisted ZVS, active-clamped push-pull, current-fed push-pull, and resonant-transition push-pull.

### Route C — Sider Scholar / scholarly search

Independent scholarly search confirmed that resonant-transition / ZVT / soft-switching push-pull is a mature literature family. The exact Ryan record was not cleanly recovered by the Scholar endpoint in this run, so this route is counted as a broad-family verification, not exact-record confirmation.

### Route D — Qu Review

Attempted but unavailable in this run because the external service required account setup after free reviews were exhausted.

Formal search-quality status:

```text
3 independent search routes completed
2 independent routes recovered the same closest IEEE reference (Ryan 1998)
1 additional scholarly route confirmed the same mature mechanism family
Qu Review = unavailable / not counted
```

---

## 3. Critical extreme-LV prior art

Ryan et al. is highly relevant because it is not merely a high-voltage or low-current analogy.

Reported operating evidence includes approximately:

```text
input = 12 V
input current = 160 A
output = 235 V
output power = 1.8 kW
measured efficiency ≈ 93%
surge test = 5 kW / 1 s
```

The paper also reports a 12-V / 2-kW laboratory converter test context.

Its primary-switch ZVS mechanism is explicitly based on:

```text
transformer magnetizing-current commutation
+
inherent MOSFET drain-source capacitance
+
body-diode-assisted transition
```

Its LCL output network is used to shape the power-transfer / leakage-energy behavior and reduce trapped primary leakage energy and rectifier commutation stress.

Therefore the project cannot claim as novelty:

```text
push-pull
+
magnetizing-current-assisted main-switch ZVS
+
low-voltage / hundred-ampere operation
```

This combination has strong prior art very close to the project boundary.

---

## 4. Earlier foundational prior art

The Ryan paper itself cites earlier work by Shoyama and Harada on zero-voltage switching realized by transformer magnetizing current in a push-pull converter.

The earlier mechanism is structurally the same physical idea at L3:

```text
magnetizing current
→ commutates switch-node capacitances
→ body diode conducts
→ switch turns on at approximately zero voltage
```

Therefore even if the Ryan LCL output graph differs from the A0-derived dual-HFT graph, the central R2-C3 commutation principle is already established.

---

## 5. 2023 evidence that the mechanism remains active prior art

More recent IEEE work also uses intentional magnetizing-current injection to secure wide / full-load-range ZVS in push-pull-derived isolated converters.

Representative:

G. Xu et al.,
"Magnetizing Current Injection Based Push-Pull Dual Active Bridge Converter With Optimized Control to Achieve Full Load Range ZVS for the Distributed Generation System,"
IEEE Transactions on Energy Conversion, 2023,
DOI `10.1109/TEC.2023.3257000`.

This confirms that:

```text
magnetizing-current injection / shaping for ZVS
```

remains an active design variable and is not available as a generic novelty claim.

---

## 6. Gate result for R2-C3

Formal classification:

```text
R2-C3 mechanism
= KNOWN PRIOR ART

R2-C3 as topology-novelty path
= STOP

R2-C3 as research comparator / design principle
= RETAIN
```

Reason:

```text
same L3 mechanism
+
very close extreme-LV / high-current operating evidence already exists
+
known push-pull ZVS families already exploit the same magnetizing-current / Coss transition
```

Changing:

```text
single HFT → dual HFT
235 Vdc → 325–400 Vdc
1.8 kW → 2 kW
rectifier arrangement
MOSFET count
transformer ratio
```

would not by itself convert the known magnetizing-current ZVS mechanism into a defensible new contribution.

---

## 7. New locked reference: R2-REF2

Ryan 1998 is promoted to a formal high-priority comparator:

```text
R2-REF2
= Ryan 1998 ZVS LCL-resonant push-pull
= EXTREME-LV / HIGH-CURRENT REFERENCE
= IEEE PRIOR ART
```

Why R2-REF2 is more important than a generic literature comparator:

```text
R2-REF1 (Wu active clamp)
→ strong PM-4 reference but 40–60 V / 1 kW class

R2-REF2 (Ryan LCL ZVS push-pull)
→ ~12 V / 160 A / 1.8 kW class
→ directly attacks the same extreme-LV current regime
```

R2-REF2 therefore becomes a mandatory matched comparator before any new R2 topology claim.

---

## 8. Consequence for the R2 research branch

The R2 branch now has three rejected novelty attempts:

| ID | Core idea | Result |
|---|---|---|
| R2-C1 | branch-local modular active clamp / IPOS-like | `CLOSE_PRIOR_ART / STOP` |
| R2-C2-v0 | transition-only A↔C active shuttle | `PHYSICS_DEFECT + HIGH_PRIOR_ART_RISK / STOP` |
| R2-C3 | auxiliary-free magnetizing-current-assisted ZVS | `KNOWN_PRIOR_ART / STOP` |

References retained:

| ID | Reference role |
|---|---|
| R2-REF1 | Wu-type active-clamp push-pull |
| R2-REF2 | Ryan 1998 extreme-LV ZVS LCL-resonant push-pull |

This does **not** mean R2 is useless.

It means:

```text
R2 mechanism space is mature
→ topology novelty risk is high
→ future R2 work must be driven by a demonstrable unresolved loss boundary,
not by generic ZVS / resonant-transition recombination.
```

---

## 9. Revised next research question

Do not generate another R2 topology immediately.

First compare:

```text
A0 hard-switched / RC-damped dual-HFT path
vs
R2-REF1 active-clamp push-pull
vs
R2-REF2 extreme-LV LCL / magnetizing-current ZVS push-pull
```

under one matched theoretical boundary:

```text
Vin = 12 V
Pout = 2 kW
HV-link target = 325–400 Vdc
same semiconductor technology class
same thermal / cooling assumptions
same isolation requirement
same auxiliary / protection accounting rule
```

Primary quantities:

```text
pre-X1 RMS current
main MOS conduction loss
switching / Coss loss
magnetizing-current burden
circulating reactive current
leakage-energy processed power
transformer copper / core burden
rectifier loss
added resonant-component ESR / copper loss
```

Central discriminator:

```text
Does the known Ryan-type solution remain favorable when scaled from its reported 235 V output toward the project's 325–400 V HV-link requirement while preserving the 12 V / ~175 A source boundary?
```

This is a valid research question even though Ryan's topology is prior art.

---

## 10. Publication / novelty boundary

Current formal status:

```text
R2-C3 topology novelty       = REJECTED
R2 mechanism novelty         = NOT AVAILABLE
R2-REF2 relevance            = VERY HIGH
exact 12V/2kW/220Vac complete-system prior art closure = NOT COMPLETE
methodological contribution  = STILL OPEN
Candidate #10                = HOLD
Novelty                      = NOT_ESTABLISHED
```

The next useful R2 step is a matched loss / scaling crossover analysis, not another arbitrary commutation-cell invention.

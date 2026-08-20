# 43 — Multi-Assistant IEEE Prior-Art Verification Protocol v1

Status date: 2026-08-20  
Role: `MANDATORY MULTI-ASSISTANT PRIOR-ART VERIFICATION / IEEE GATE CONTROL`  
Applies to: `IEEE Gate A / Gate B / Gate C`  
Primary publication corpus: `IEEE Xplore`  
Novelty authority: `NOT ESTABLISHED BY SEARCH ALONE`

## 1. Mandatory rule

From this file forward, **no IEEE prior-art decision may be made from a single assistant, a single search engine, a single query, or a single closest paper**.

Every Gate A, Gate B and Gate C run must use multiple independent AI-assisted search/review routes before a research direction is accepted, rejected, or described as differentiated.

Minimum rule:

```text
>= 3 independent assistant/retrieval roles
+
main synthesis/adjudication
```

The purpose is to reduce false novelty caused by:

```text
query wording bias
synonym mismatch
indexing gaps
search-ranking bias
assistant hallucination / omission
premature convergence on one topology name
```

This protocol supplements File 37 and does not replace it.

---

## 2. Required independent roles

### Role A — IEEE-direct search assistant

Search IEEE Xplore/direct web-visible IEEE records using topology, mechanism, state, and application vocabulary.

Must record:

```text
queries used
paper title
year
venue
DOI / IEEE document identifier when available
why it is close or not close
```

### Role B — independent semantic search assistant

Use a different retrieval route, such as Exa or an equivalent semantic-search assistant, restricted or filtered toward IEEE material where possible.

It must not simply reuse Role A's exact query list.

Required behavior:

```text
use alternate synonyms
search physical mechanism language
search topology-family language
search switching-state / loss language
```

### Role C — independent academic search assistant

Use a separate scholarly-search route, such as Sider Scholar or equivalent academic index/search assistant.

Its task is to challenge A/B by looking for:

```text
older papers with different naming
conference papers preceding journal versions
related families hidden behind different topology names
review papers that point to earlier prior art
```

### Role D — adversarial reviewer / second-opinion assistant

When available, use an independent review assistant such as Qu Review or an equivalent critic.

Role D does **not** count as source evidence by itself. Its role is to attack the provisional conclusion:

```text
Did the search miss synonyms?
Is the claimed structural difference actually trivial?
Is the contribution already known even if the exact graph differs?
Are we confusing operating boundary with novelty?
```

For high-risk claims, Role D is mandatory before Gate C can return `CLAIM_DIFFERENTIATED`.

---

## 3. Minimum valid evidence rule

A Gate result is valid only if:

```text
at least 3 independent search/review routes were attempted
AND
at least 2 routes independently identify the closest IEEE prior-art set
AND
actual IEEE records are inspected for the load-bearing comparisons
```

A generic search-result snippet alone is insufficient for the final closest-prior-art conclusion when the full abstract/metadata/technical description is accessible.

If one route fails technically:

```text
status = ROUTE_FAILED
```

and another independent route must replace it before the Gate is considered complete.

---

## 4. Query-diversity requirement

The three search assistants must not all issue the same wording.

For each candidate, the search space must cover at least four vocabulary dimensions:

```text
A. topology names
B. physical mechanisms
C. switching / commutation states
D. application / operating boundary
```

Example for an R2-type candidate:

```text
Topology:
active-clamp push-pull
ZVS push-pull
energy-recovery push-pull
high-frequency-link inverter

Mechanism:
leakage-energy recovery
reactive commutation
commutation energy transfer
lossless snubber

State / graph:
cross commutation
node-to-node capacitor transition
body-diode assisted ZVS
auxiliary resonant transition

Boundary:
12 V high current
low-voltage kW inverter
battery-fed high-step-up
220 Vac single phase
```

Internal PM labels alone are never sufficient search terms.

---

## 5. Gate-A multi-assistant rule

Before detailed circuit derivation or PSIM work:

```text
new mechanism combination / concept
↓
Role A search
Role B search
Role C search
↓
main comparison
↓
optional/required Role D challenge
↓
Gate A decision
```

Allowed Gate-A decisions:

```text
KNOWN_MECHANISM_COMBINATION
CLOSE_PRIOR_ART
POSSIBLY_DIFFERENTIATED
STOP_AS_NOVELTY
KEEP_AS_COMPARATOR
CONTINUE_FOR_DIFFERENTIATION
SEARCH_INCONCLUSIVE
```

Hard rule:

```text
one assistant finds nothing
≠
POSSIBLY_DIFFERENTIATED
```

If the assistants disagree materially:

```text
Gate A = SEARCH_INCONCLUSIVE
```

until the conflict is resolved.

---

## 6. Gate-B multi-assistant rule

After an actual circuit graph exists, all assistants receive the same normalized graph description but search independently.

The normalized graph package must include:

```text
source connection
main switch arrangement
auxiliary switch arrangement
magnetic connections
L/C placement
energy-recovery destination
state sequence
current path per state
gain equation
ZVS/ZCS condition
voltage/current stress relation
```

Each assistant must return:

```text
closest paper(s)
SAME_GRAPH / NEAR_GRAPH / STRUCTURALLY_DIFFERENT / INCONCLUSIVE
specific matching edges/states
specific differing edges/states
```

Main adjudication may only return `STRUCTURALLY_DIFFERENT` when the difference survives cross-check by multiple independent routes.

---

## 7. Gate-C multi-assistant rule

Gate C is stricter because it controls manuscript contribution claims.

Minimum:

```text
Role A
Role B
Role C
Role D adversarial review
+
main adjudication
```

For the closest 5–10 IEEE papers, compare whether they already establish the same:

```text
loss scaling law
crossover boundary
ZVS region
RMS-current trade-off
circulating-current conclusion
magnetic relation
control/modulation law
energy-routing principle
architecture-selection criterion
extreme-LV conclusion
```

Allowed results:

```text
CLAIM_ALREADY_KNOWN
CLAIM_INCREMENTAL
CLAIM_DIFFERENTIATED
CLAIM_NOVELTY_NOT_ESTABLISHED
```

`CLAIM_DIFFERENTIATED` requires consensus or a documented resolution of disagreements.

---

## 8. No-result rule

The phrase:

```text
"IEEE has no identical method"
```

is forbidden unless all of the following are true:

```text
multiple independent routes completed
multiple synonym families searched
closest IEEE papers inspected
backward references of closest papers checked where practical
review/survey literature checked where practical
no material conflicting result remains unresolved
```

Even then, the permitted wording is only:

```text
"No identical IEEE prior art was identified in the completed search set."
```

It is never equivalent to universal proof of novelty.

---

## 9. Required prior-art matrix fields

Every candidate must maintain a matrix containing at least:

| Field | Required |
|---|---|
| Candidate ID | yes |
| Gate | A / B / C |
| Assistant/route ID | yes |
| Query family | yes |
| IEEE paper | yes |
| DOI / identifier | when available |
| Same PM | yes |
| Same majority-power graph | yes |
| Same commutation graph | yes |
| Same state sequence | yes |
| Same equation / claim | yes |
| Same boundary | yes |
| Difference judged substantive? | yes |
| Route conclusion | yes |
| Main adjudication | yes |
| unresolved conflict | yes |

No final Gate decision may be recorded without the per-route evidence being traceable.

---

## 10. Current R2 application

This protocol applies immediately to:

```text
R2-REF1
R2-C1
R2-C2
and every later R2 candidate
```

Existing single/limited-route conclusions remain provisional until they are rechecked under this protocol when they become decision-critical.

In particular:

```text
R2-C2 = POSSIBLY_DIFFERENTIATED_AT_GRAPH_CONCEPT_LEVEL
```

must **not** be promoted further until a formal multi-assistant Gate-B search is completed on its actual graph.

---

## 11. Research-effort stop rule

The multi-assistant Gate exists to save effort, not merely document searches.

```text
if >=2 independent routes identify same/near-identical prior art
AND
main adjudication finds no substantive physical/analytical difference
→ STOP as novelty before deep simulation
```

If the candidate is useful as a benchmark:

```text
→ KEEP_AS_COMPARATOR
```

If evidence conflicts:

```text
→ SEARCH_INCONCLUSIVE
→ resolve before PSIM / hardware investment
```

---

## 12. Formal authority

From 2026-08-20 onward:

```text
File 37
= defines IEEE Gate A/B/C logic

File 43
= defines mandatory multi-assistant execution of those gates
```

Therefore:

```text
single-assistant IEEE search
= insufficient for formal Gate completion
```

Candidate #10 remains:

```text
HOLD / NOT_ASSIGNED
```

Novelty remains:

```text
NOT_ESTABLISHED
```

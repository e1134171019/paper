# GPT Adjudication — Repeated Trade-off Pattern Audit v0.2

Date: 2026-08-12

## Decision

- Current research direction: `APPROVE_CONTINUE`
- COMP-HG-001 comparison mode: `BOUNDED_TRADEOFF`
- L5 status of existing members: unchanged
- Repeated pattern status: `ONE_RECURRING_BOUNDARY_CANDIDATE_AUTHORIZED`
- Research Gap Candidate: `NOT_AUTHORIZED`
- Established Research Gap: `NOT_AUTHORIZED`

## What survived adversarial review

The broad claim that low main-switch stress or soft switching inherently requires more active switches is not supported and is rejected.

The current evidence instead supports a narrower recurring-boundary candidate:

> In non-isolated high-step-up hardware near the present scale, aggressive reduction of main-switch voltage stress appears to redistribute design burden among passive-component count, magnetic implementation, diode voltage stress, source-current conditioning, common-ground/integration constraints, or switching strategy. The available evidence does not establish a universal monotonic trade-off or an optimal topology.

This statement is authorized only as a `RECURRING_BOUNDARY_CANDIDATE`.

## Evidence behind the narrowed candidate

### PC-CAND-0027

- 24 V → 400 V, 200 W, 50 kHz, duty 0.60.
- Main switch stress ≈62 V, normalized ≈0.155.
- Maximum measured diode stress ≈110 V, normalized ≈0.275.
- 1 switch / 8 diodes / 8 capacitors / 1 magnetic core.
- The paper explicitly explains that the increased diode/capacitor structure supports voltage generation in smaller portions, reducing switch stress and increasing gain.
- Common-ground comparison field is No.

### PC-CAND-0028

- 25 V → 400 V, 250 W, 50 kHz, duty 0.55.
- Main switch stress ≈55 V, normalized 0.1375.
- Maximum reported diode stress ≈240 V, normalized ≈0.60.
- 1 switch / 4 diodes / 5 capacitors / separate input-inductor core + three-winding CI core.
- Main switch ZCS; low reverse recovery on diodes.
- Input current is continuous/low ripple.
- Measured full-load efficiency 96.4%; power density 2.72 W/cm3.
- Measurement probes are explicitly reported.

### PC-CAND-0024

- 25 V → 400 V, 200 W, 88 kHz.
- Main switch stress is only bounded (<100 V / <0.25), so no exact ordering is allowed.
- 1 switch / 4 diodes / 5 capacitors / input-inductor core + coupled-inductor core.
- Coupled-inductor turns ratio n=4.
- Continuous low-ripple input current and ZCS turn-on are reported.

### PC-CAND-0030

- Existing electrical L5 evidence remains usable: 40 V → 400 V, 200 W, 100 kHz, measured switch stress <90 V (<0.225), main/clamp ZVS, full-load efficiency descriptor 95.4%.
- This v0.2 pass did not recover sufficient lawful structural full text to lock component count, duty, turns ratio, common-ground and source-current behavior.
- Therefore 0030 must not be used in component-count arithmetic until resolved.

## Falsification results

A deliberate counter-search found evidence against an over-broad complexity hypothesis.

The 2025 IEEE Open Journal paper `10.1109/OJPEL.2025.3554381` reports a single-switch, soft-switched high-voltage-gain converter with continuous input current and common ground. Its lossless snubber uses two diodes and requires no additional active switch or magnetic core. It therefore falsifies the statement that soft switching necessarily costs additional active switches or magnetic cores. Its normalized stress is not in the present very-low <0.25 region, so it does not settle the narrower burden-redistribution question.

Additional counter-search hits show that new relevant hardware continues to appear. This means the literature search has not reached saturation.

## Hypotheses rejected or blocked

1. `Low stress necessarily requires more active switches` → REJECTED.
2. `Soft switching is necessary for low switch stress` → REJECTED; PC-CAND-0027 is a counterexample in the current set.
3. `Soft switching causes higher efficiency across papers` → NOT TESTABLE; auxiliary/thermal/measurement boundaries are unmatched.
4. `Common ground + continuous input + <0.25 stress is a research gap` → NOT AUTHORIZED; direct evidence coverage is incomplete.

## Methodology blockers preventing Research Gap Candidate

- Complete lawful structural extraction for PC-CAND-0030 is missing.
- Backward citation snowballing is not complete.
- Forward citation snowballing is not complete.
- Claim-critical numeric extraction has not been independently duplicated for all four L5 members.
- Search saturation / marginal-yield stopping criterion has not been reached; new counterexamples appeared in this pass.
- Auxiliary-power, cooling/thermal and measurement boundaries remain unmatched for efficiency comparisons.

Therefore the protocol stopping rule is `NOT_MET`.

## Authorized next node

`BATCH-004 Falsification + Coverage Closure`

Priority actions:

1. Resolve PC-CAND-0030 lawful full-text structural fields.
2. Formally audit DOI `10.1109/OJPEL.2025.3554381` as a counterexample candidate rather than using search snippets as final evidence.
3. Target direct-scale papers with all of: 380–400 V output, 150–300 W, measured main and diode stress, component counts, input-current behavior and common-ground state.
4. Run backward/forward citation snowballing on 0024, 0027, 0028, 0030 and the counterexample seed.
5. Perform an independent second extraction of the four core L5 records and save disagreements/adjudication.
6. Track marginal yield by query family; only consider a gap candidate after saturation and the protocol stopping rule pass.

## Guardrails retained

- No efficiency leaderboard.
- No overall-best topology claim.
- No conversion of upper bounds to exact scalars.
- No causal attribution of efficiency to ZVS/ZCS from cross-paper data.
- No Research Gap claim from a search miss.
- No Research Gap Candidate until the frozen stopping rule passes.

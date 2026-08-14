# BATCH-005 — Current-Fed Isolated Front-End Acquisition

Date: 2026-08-14
Status: candidate acquisition / protocol binding
Parent reframe: `research/reviews/2026-08-14-energy-conversion-reframe/RESEARCH_REFRAME.md`
Contract: `research/contracts/power_converter_comparison_contract_v0.1.md`

## Purpose

Build the first evidence set for low-voltage, high-current, high-frequency isolated front-end conversion after the research program was reframed around total energy-conversion loss rather than a single topology family.

The first-priority topology family is current-fed push-pull and closely related current-fed isolated converters.

## Research questions

### COMP-CFPP-001

How do current-fed push-pull and closely related current-fed isolated converters redistribute:

- conduction loss;
- switching loss;
- RMS current;
- circulating current;
- semiconductor voltage/current stress;
- transformer and inductor burden;
- soft-switching range;
- efficiency across wide input and load conditions?

### COMP-ISO-DCAC-001

At a matched low-voltage DC to single-phase AC system boundary, does integrating conversion stages reduce total loss, or does it move burden into current stress, magnetics, energy buffering, switching stress or control complexity?

## Initial direct acquisition window

This is an acquisition window, not a final comparison window.

Direct-target preference:

- input: approximately 10–60 Vdc;
- high-voltage DC link: approximately 300–450 Vdc when applicable;
- output system: 110/220–230 Vac single phase when applicable;
- power: approximately 0.5–3 kW;
- galvanic isolation: required for direct isolated-front-end comparison;
- physical hardware experiment: required before numerical promotion;
- efficiency curve or multiple operating points preferred;
- switch/diode stress, RMS/circulating current or ZVS/ZCS evidence strongly preferred.

Scaled context may include higher input voltage or power when it isolates a mechanism that is directly relevant to current-fed isolated conversion.

## Candidate admission policy

`candidates.csv` contains discovery-stage journal records only.

Admission at this stage means that the paper is worth full-text acquisition or source resolution. It does not mean:

- L4 numerical verification;
- L5 comparison readiness;
- direct efficiency comparability;
- superiority over another topology;
- Research Gap support.

## Priority axes

1. current-fed push-pull base topology;
2. natural commutation / snubberless operation;
3. active clamp and leakage-spike control;
4. circulating-current suppression;
5. interleaving / multiphase current sharing;
6. full-load-range or wide-range ZVS/ZCS;
7. minimum RMS current operation;
8. transformer flux balance / magnetic utilization;
9. wide input-voltage and wide load-range performance;
10. front-end integration with DC-link and inverter stage.

## Conversation carryover

`chat_carryover.csv` records papers that were already studied in conversation with full-text material but have not yet been normalized into repository evidence records.

These records are intentionally held below formal promotion until the source files, exact locators and numerical claims are reattached to the repository evidence workflow.

## Required next gate

For each high-priority candidate:

1. resolve canonical DOI and publisher record;
2. acquire legal readable full text;
3. lock prototype boundary;
4. extract exact locator for each numerical claim;
5. type reported vs recalculated values;
6. record measurement and auxiliary-loss boundary;
7. apply the comparison contract;
8. only then consider L4/L5 promotion.

## Research Gap boundary

No BATCH-005 discovery result is a Research Gap.

`Research Gap Candidate = NOT_AUTHORIZED` until comparable evidence, counter-search, stopping criteria and required independent review are satisfied.

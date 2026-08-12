# Evidence Packet Policy

Date: 2026-08-12

## Purpose

Create source-neutral packets for independent interpretation when a second reviewer cannot independently acquire publisher pages.

This mechanism does **not** replace independent source acquisition. Its review label is:

`CURATED_PACKET_INDEPENDENT_INTERPRETATION`

## Packet constraints

Each packet may contain only:

- canonical record ID, DOI, and title;
- verified operating conditions;
- measured / bounded numerical facts and their value type;
- common-basis component counts already verified by the project;
- device-level soft-switching facts;
- exact locator references (section / figure / table / page where available);
- explicit unresolved or conflicting fields.

The packet must not contain:

- L5 or family-credit decisions;
- Pareto ranking or dominance judgments;
- efficiency leaderboard language;
- research-gap hypotheses or conclusions;
- inferred missing values;
- a preferred interpretation of source conflicts.

## Reviewer instructions

The independent reviewer must:

1. extract each supplied field independently from the packet text;
2. preserve `exact`, `approx`, `upper_bound`, `conflict`, and `unresolved` semantics;
3. flag internal contradictions or missing fields;
4. not fill values from memory or external knowledge;
5. not rank efficiency across records;
6. not infer overall-best topology;
7. report whether each packet is internally sufficient for a bounded trade-off interpretation.

## Independence boundary

- Independent publisher acquisition + independent interpretation is the strongest path.
- Curated-packet independent interpretation checks reasoning/extraction independence only.
- The latter must never be reported as independent source acquisition.

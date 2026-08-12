# Jazi Lineage Adjudication

Date: 2026-08-12
Target DOI: `10.1109/ACCESS.2025.3573936`

## Question

Should the 2025 Jazi-led ZVT coupled-inductor / multiplier converter be collapsed into the existing `MOLAVI_SOFTSWITCH` family solely because Ehsan Adib is an author on both research programs?

## Evidence used

Current paper authorship is led by Hamed Moradmand Jazi and includes Behrouz Mohammadzadeh, Ramin Rahimzadeh Khorasani, Pericle Zanchetta, Ehsan Adib, Guillermo Velasco-Quesada and Herminio Martínez-García.

The existing independent L5 family `MOLAVI_SOFTSWITCH` is represented by the older Molavi / Adib / Farzanehfard soft-switched active-clamp program.

A separate earlier Jazi-led publication, `10.1049/pel2.12183` (2021), documents a Jazi/Fekri/Keshani high-step-up three-level ZVT topology using a single magnetic element and 40 V -> 400 V / 200 W hardware. This predates the 2025 paper and demonstrates that Jazi has an identifiable lead topology-development lineage independent of merely appearing as a downstream coauthor in the Molavi record.

## Role-weighted lineage analysis

### Lead / program ownership

- 2025 target: Jazi-led author list and ZVT high-step-up design line.
- existing Molavi family: Molavi-led paper with Adib and Farzanehfard.

Shared authorship is limited and does not by itself establish a single research program.

### Architecture lineage

The 2025 target combines:

- retained boost input inductor for continuous current;
- coupled-inductor voltage-gain mechanism;
- multiplier capacitors/diodes;
- a dedicated ZVT auxiliary branch;
- common ground;
- wide-load soft switching.

The existing Molavi record is an older active-clamp soft-switched high-step-up architecture. The mechanisms overlap at the broad field level but are not the same topology lineage.

### Methodology continuity

The earlier 2021 Jazi-led three-level ZVT work provides direct evidence of a Jazi program centered on ZVT / coupled magnetic integration before the 2025 target. This supports a distinct lead-methodology lineage.

## Decision

`family_candidate = JAZI_KHORASANI_ZVT_CI_VM`

`collapse_into_MOLAVI_SOFTSWITCH = NO`

`independent_family_if_L5 = YES_POTENTIAL`

The 2025 Jazi paper is treated as a **distinct family candidate**, not as an automatic duplicate of Molavi/Adib/Farzanehfard.

However, family count is an L5 evidence-family count. Because the Jazi 2025 record remains L4 in this node, it receives:

`independent_l5_family_credit = no`

No seventh independent L5 family is counted early.

## Guardrail

This adjudication is not a novelty claim and does not establish a Research Gap. It only prevents false deduplication based on one shared author.

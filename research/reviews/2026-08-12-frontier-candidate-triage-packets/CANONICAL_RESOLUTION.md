# Canonical Resolution

Date: 2026-08-12

## PC-CAND-0029 — resolved and promotable

DOI: `10.1038/s41598-026-47061-0`

The current Scientific Reports version of record resolves the prior BATCH-003 condition-lock blocker. Publisher PDF parsed text explicitly records the hardware prototype as:

- Pout = 200 W
- Vin = 25 V
- Vout = 400 V
- fs = 50 kHz

The same experimental section records approximately 50 V on the single power switch and measured diode stresses of approximately 50 / 180 / 300 / 300 V. Full-load measured efficiency remains 94.9% and the switch has ZCS turn-on.

Decision: `L4_NUMERICALLY_VERIFIED -> L5_COMPARISON_READY` for `COMP-HG-001`, mode `BOUNDED_TRADEOFF`.

Guardrails:

- normalized controlled-switch stress is approximately 0.125, not an exact physical measurement;
- normalized maximum diode stress is approximately 0.75;
- efficiency remains a descriptor and is excluded from a cross-paper efficiency leaderboard;
- the record does not receive a new independent-family credit because it belongs to the broader Hasanpour/Nouri research program.

PDF screenshot verification of the relevant pages was attempted and failed because the source cache did not return page images. The promotion uses publisher PDF parsed text plus existing publisher HTML evidence; no waveform scalar was invented from a failed screenshot.

## IEEE Xplore document 11159317 — canonical identity resolved, numerical audit not resolved

Canonical title: `New Soft-Switched Three-Winding Built-In Transformer Step-Up DC/DC Converter With Low Voltage Stresses`

Canonical identifier: `10.1109/TPEL.2025.3608899`

Primary IEEE metadata/abstract supports a 200 W, 25 V to 400 V, 50 kHz experimental prototype and describes a single-switch soft-switched / low-input-ripple design. No legal/readable full-text path with reproducible measured voltage-stress and measured-efficiency locators was obtained in this pass.

Decision: retain `L1_METADATA_VERIFIED / DIRECT_SCALE_UNAUDITED`.

## CTA index candidate — unresolved identity

Indexed title: `A Low Switch Stress and High-Gain DC-DC Converter for Renewable Energy Applications`
Indexed identifier: `10.1002/cta.70585`

The Wiley fetch timed out and the scholarly DOI lookup did not resolve a canonical primary record. Search results also returned neighboring but non-identical converter papers.

Decision: `NOT_CANONICALIZED`. Do not substitute a nearby paper for this record.

## Scientific Reports 50184 — source-internal conflict retained

DOI: `10.1038/s41598-026-50184-z`

Primary article material supports a 200 W prototype and an experimental 48 V to approximately 400 V context, with approximately 134 V switch stress and approximately 96.7% efficiency. However, a design-procedure passage states a 48 V to 200 V, 200 W, 100 kHz design condition.

Decision: `L3_CONTEXT_CONFLICT`; exclude from formal frontier until the operating-condition conflict is reconciled by the source or a sufficiently clear experiment-specific locator resolves the ambiguity without overwriting the contradiction.

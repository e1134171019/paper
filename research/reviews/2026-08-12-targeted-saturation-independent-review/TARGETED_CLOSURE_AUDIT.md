# Targeted Saturation Closure Audit

Date: 2026-08-12
Scope: targeted evidence closure after broad-keyword search was stopped.

## Decision rules

- Preserve measured, theoretical, recalculated, upper-bound, conflict, and unresolved values as different evidence types.
- Do not infer an oscilloscope scalar from an unseen or unreadable figure.
- Multi-switch comparison requires the maximum controlled-switch stress vector, not the main switch alone.
- A newly surfaced paper does not receive independent-family credit until canonical identity, direct-scale eligibility, and L5 admission are all established.

## 1. PC-CAND-0024 — DOI 10.1049/iet-pel.2015.0923

Targeted primary-text retrieval recovered the Wiley article text and rechecked its semiconductor-stress discussion.

Confirmed:
- 25 V -> 400 V, 200 W, 88 kHz direct-scale prototype remains valid.
- Main switch turns on under ZCS.
- Experimental main-switch voltage stress remains text-locked as lower than 100 V (`<0.25 Vout`, upper bound).
- Experimental diode waveforms are in Fig. 10 and the paper states their stresses agree with the derived equations.

Not closed:
- No exact text-locked maximum **measured** diode-voltage scalar surfaced in the targeted pass.

Result: `STILL_UNRESOLVED_MEASURED_MAX_DIODE`.

This record remains bounded L5 under the existing comparison contract, but it is not stress-vector complete for a formal all-objective frontier.

## 2. B004-CAND-0003 — DOI 10.1155/etep/9317966

Canonical primary record was verified as:

- title: `A High Voltage Gain Single-Switch Converter With Soft-Switching and EMI Mitigation`;
- authors: Ali Janghorban, Majid Delshad, Bahador Fani;
- 200 W prototype;
- Vin = 48 V, Vout = 400 V, fs = 100 kHz;
- one active switch and one magnetic core;
- common-ground topology;
- reported full-load / maximum efficiency boundary around 95.6% at 200 W.

The primary record locates experimental switch and diode waveforms, but the targeted retrieval paths did not expose a reproducible exact maximum measured diode-voltage scalar. The Wiley direct-open route returned an access error and a separate live fetch timed out.

Result: `STILL_UNRESOLVED_MEASURED_MAX_DIODE`.

No theoretical/device-rating value is substituted for the missing measured scalar. The record stays L4/context under the current formal frontier policy.

## 3. New direct-scale yield — Habibi et al. 2024

Canonical identity:

- DOI: `10.1109/TPEL.2023.3344719`
- title: `An Impedance-Source-Based Soft-Switched High Step-Up DC-DC Converter With an Active Clamp`
- authors: Saeed Habibi, Ramin Rahimi, Mehdi Ferdowsi, Pourya Shamsi
- IEEE Transactions on Power Electronics, vol. 39, no. 3, 2024.

Legal/readable full text was recovered from Missouri University of Science and Technology Scholars' Mine, which identifies the definitive IEEE DOI.

Primary-source facts:
- 20 V -> 400 V;
- 200 W;
- 50 kHz;
- three-winding coupled inductor with n21 = 0.5 and n31 = 2 in the prototype;
- two controlled switches: S1 and active-clamp Sc;
- three discrete diodes: D1, D2, Do;
- five capacitors: Cc, C1, C2, C3, Co;
- one input inductor plus one three-winding coupled inductor;
- measured S1 voltage stress is almost 45 V;
- S1 and Sc both experimentally turn on under ZVS;
- diode reverse-recovery loss is minimized by leakage-inductance-controlled current fall rate;
- exact measured maximum diode-voltage scalar is not text-locked in the recovered prose;
- Sc is described as having similarly very low voltage stress, but an exact measured scalar was not text-locked in the recovered prose;
- rated-power experimental efficiency is approximately 94%;
- input-current ripple is qualitatively low.

The analytical model states `VS1 = VSc = VCc` and gives closed-form normalized switch/diode stresses. Those equations are retained as theory and are not silently relabeled as measured values.

Evidence decision: `L4_NUMERICALLY_VERIFIED / DIRECT_NEW_CANDIDATE`.

Reason for not promoting in this node: the measured maximum controlled-switch vector is not text-locked because the exact Sc scalar is unresolved, and the measured maximum diode scalar is also unresolved. The paper is nevertheless a genuine new different-author direct-scale program and therefore counts as positive marginal search yield.

Potential family: `HABIBI_RAHIMI_IMPEDANCE_ACTIVE_CLAMP`.
Independent L5 family credit: `NOT_YET_ELIGIBLE`.

## 4. Additional direct-scale yield — Jazi et al. 2025

Canonical identity:

- IEEE document: `11015738`
- DOI: `10.1109/ACCESS.2025.3573936`
- title: `High Voltage Gain DC-DC Converter With Wide Range of Soft Switching and Continues Input Current for Renewable Energy Applications`

Primary/indexed experimental facts surfaced in the targeted pass:
- 40 V -> 400 V;
- 200 W;
- 100 kHz;
- main-switch maximum voltage about 120 V;
- main switch operates with ZVS over the tested power range;
- auxiliary switch has soft-switching operation;
- diodes turn off under ZCS;
- continuous input current and shared ground are reported;
- measured full-load efficiency about 96.5%.

The complete controlled-switch stress vector, maximum measured diode stress, and common count basis were not fully extracted in this node.

Evidence decision: `DIRECT_CANONICALIZED_TARGET / FULL_VECTOR_AUDIT_PENDING`.

Family note: Ehsan Adib overlaps the existing Molavi/Adib/Farzanehfard soft-switching program, so no new independent-family credit is assigned without a lineage audit.

## 5. Saturation consequence

The targeted search found a canonical, legal/readable, direct-scale different-author hardware paper (Habibi et al.) and another direct-scale 2025 candidate (Jazi et al.). Therefore marginal yield is still positive even after broad-keyword searching was stopped.

Formal search saturation: `NOT_MET`.

The next search action must remain targeted: close Habibi's complete measured controlled-switch/diode vectors, audit Jazi's full vector and family lineage, and avoid returning to generic high-step-up keyword expansion.

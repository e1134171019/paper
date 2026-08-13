# Family Lineage Adjudication

Date: 2026-08-13

## Policy

Independent-family credit is not assigned by surname-only matching or by simple paper count. The decision considers lead/corresponding roles, repeated core authors, methodology continuity, topology lineage, and experimental/research program continuity.

## Habibi / Rahimi / Ferdowsi / Shamsi

Paper: DOI `10.1109/TPEL.2023.3344719`.

This program is methodologically distinct from the currently credited six L5 families:
- it is an impedance-source / trans-inverse active-clamp architecture;
- Saeed Habibi / Ramin Rahimi / Mehdi Ferdowsi / Pourya Shamsi form a different core author group from the currently credited Hasanpour, Sepahvandi, Forouzesh, Molavi, Abbasi and Yao programs;
- the 20 V -> 400 V / 200 W hardware is a direct-scale experiment.

Decision: `POTENTIAL_NEW_INDEPENDENT_FAMILY`, family ID `HABIBI_RAHIMI_IMPEDANCE_ACTIVE_CLAMP`.

Credit is **not yet counted** because the record remains L4: the complete measured controlled-switch vector and maximum measured diode stress are not closed. The independent-family count therefore stays unchanged.

## Jazi / Khorasani / Adib / Zanchetta / Velasco / Martínez-García

Paper: DOI `10.1109/ACCESS.2025.3573936`.

The 2025 paper is a distinct topology implementation, but the research lineage is not independent enough to add another L5 family credit relative to the existing `MOLAVI_SOFTSWITCH` credit:
- Ehsan Adib is a repeated core author in the established high-step-up soft-switching program;
- the existing credited Molavi paper is Navid Molavi / Ehsan Adib / Hosein Farzanehfard, DOI `10.1049/iet-pel.2015.0870`;
- Jazi's paper explicitly develops ZVT / soft-switching high-step-up techniques and cites multiple earlier Jazi/Adib, Poorali/Jazi/Adib, Packnezhad/Farzanehfard/Adib and related ZVT/active-clamp works;
- Jazi, Khorasani and Adib also coauthored prior high-step-up soft-switching work, demonstrating research-program continuity rather than an isolated one-off overlap.

A useful sub-lineage label is `JAZI_KHORASANI_ADIB_ZVT`, but it is nested within the broader Adib/Farzanehfard soft-switching evidence program for independent-credit accounting.

Decision: `NO_ADDITIONAL_INDEPENDENT_FAMILY_CREDIT`.

This decision does not assert that the circuit topology is the same as Molavi's. It only prevents double-counting related research programs as independent confirmation.

## Count consequence

Current independent L5 evidence-family count remains **6**.

Habibi could become a seventh independent family only after L5 admission. Jazi does not add a seventh family under the present lineage policy even if it later becomes L5.
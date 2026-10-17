# Research Decision Log

## 2026-08-16 — Memory ledger formalization

Decision: GitHub becomes the durable research memory. Chat logs remain exploration evidence, but only distilled state is promoted into this ledger.

Reason: repeated long conversations were causing already-excluded ideas to reappear. A formal ledger prevents novelty drift and preserves why each direction was accepted or rejected.

---

## 2026-08-16 — Do not treat direct 12 V CPT as the primary hypothesis

Status: deprioritized, not disproven.

Reason:

- Capacitive power transfer and capacitor-transformer concepts already exist at high power.
- Low-voltage CPT examples often pre-raise voltage or rely on resonant structures.
- Direct 12 V / ~166 A operation would force very large AC / displacement-current burden unless strong evidence shows a Pareto advantage.

Research implication: CPT remains a candidate mechanism only after the system-level loss boundary is known.

---

## 2026-08-16 — IPOS / current splitting is prior art, not novelty

Reason:

- Primary-parallel / secondary-series isolated boost structures exist at kW scale.
- IPOS, coupled-inductor, switched-capacitor, modular and high-step-up variants are established.

Research implication: current splitting can be used as a building block, but cannot be the paper's central novelty.

---

## 2026-08-16 — "Optimal intermediate voltage" is prior art

Reason: cascaded two-stage converters already use optimal intermediate-voltage tracking based on system loss.

Research implication: intermediate voltage remains a design variable, but the research question must include physical source-side current-path loss and/or topology placement beyond simply optimizing Vint.

---

## 2026-08-16 — Shift from topology-name hunting to energy-path analysis

Observation:

At 12 V / 2 kW the unavoidable average source current is approximately 166.7 A. Different converter families mainly differ in where and how that low-voltage high-current state is transformed.

Decision:

Compare known architectures by:

- first impedance-transformation location,
- current-path resistance before that point,
- number of full-power conversion stages,
- RMS / circulating / ripple current,
- switching and magnetic losses,
- energy-buffer location.

---

## 2026-08-16 — Internal bidirectional energy buffer is not a new concept

Reason:

Literature already includes:

- active power decoupling,
- series-connected energy buffers,
- multilevel energy buffer / voltage modulators,
- partial-power buffers,
- integrated ripple steering,
- DAB + active energy buffer,
- center-tapped transformer + LC buffer,
- bidirectional matrix-converter structures.

Research implication:

Do not claim novelty for "adding a bidirectional buffer" or "keeping 120 Hz ripple out of the battery".

---

## 2026-08-16 — Distinguish heat loss from oscillatory energy

Decision:

Every loss discussion must classify the underlying energy as one of:

1. irreversible dissipation,
2. potentially recoverable switching / leakage / clamp energy,
3. oscillatory but necessary energy whose movement increases RMS current.

Reason: a buffer cannot recover heat that has already been dissipated, but it may prevent some energy from traversing lossy low-voltage paths.

---

## Current unresolved decision

Before synthesizing a new fixed topology, close prior art on this exact question:

> For a 12 V-class, kW-scale single-phase DC/AC converter, has anyone jointly designed the first impedance-transformation point and the local bidirectional energy-buffer point specifically to minimize the low-voltage 100-200 A RMS / conduction-loss burden?

Until that search is closed, do not declare a new topology or novelty claim.

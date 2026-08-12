# Targeted Stopping Round 2

Date: 2026-08-12

## Question

After closing as much of the Khan/Tran target vector as legally possible, does a narrow different-family/direct-scale search still produce previously uncaptured hardware evidence capable of changing the frontier?

This is **not** a restart of broad keyword search.

## Search constraints

- direct or near-direct low-input/high-output hardware focus;
- approximately 20–50 V input, 380–400 V output, 150–300 W;
- high-step-up non-isolated architectures;
- priority to different author/program clusters and records that can alter stress/component/magnetic/input-current tradeoffs;
- exact DOI/title repository dedup before registering new yield.

## Round-2 result

### New uncaptured direct-scale candidate

DOI: `10.1007/s43236-022-00564-1`

Title: *Quadratic-type high step-up DC-DC converter with continuous input current integrating coupled inductor and voltage multiplier for renewable energy applications*

Journal of Power Electronics publisher metadata/abstract reports:

- authors: Fuwei Li, Jie He, Peng Luo, Haoyu Jiang, Mingxin Liu;
- 20 V input;
- 400 V output;
- 200 W experimental prototype;
- continuous input current;
- quadratic boost + two multiplier cells + one coupled-inductor architecture;
- peak efficiency 95.2%;
- full-load efficiency 93.7%.

Exact DOI and title searches did not locate this record in the repository, and it is absent from the BATCH-004 candidate register inspected in this node.

The source has not yet undergone full common-schema stress/count extraction, so it receives no L5 admission or family credit here.

Candidate family label for later audit:

`LI_HE_LUO_QUADRATIC_CI_VM`

## Other targeted search behavior

A bounded Sider/OpenAlex search returned known or adjacent high-step-up records, including already represented author/program clusters. Those results are discovery support only and are not counted as independent evidence by themselves.

The fact that the round still produced at least one different-author direct-scale 20 V -> 400 V / 200 W hardware program after the prior stopping test is sufficient to reject a saturation declaration.

## Decision

- targeted marginal yield: `POSITIVE`;
- targeted search saturation: `NOT_MET`;
- broad keyword search: `REMAINS_STOPPED`;
- targeted-only search: `CONTINUE`;
- formal all-objective Pareto: `NOT_AUTHORIZED_YET`;
- Research Gap Candidate: `NOT_AUTHORIZED`.

## Next acquisition target

`LI/HE/LUO 2023 FULL-VECTOR AUDIT + ACCESS-BLOCKED TRAN RECHECK / STOPPING ROUND 3`

Priority:

1. obtain a legal/readable full text for DOI `10.1007/s43236-022-00564-1` and extract the complete common-schema vector;
2. resolve its measured/theory switch and diode stress boundaries, component counts, magnetic structure, common ground, ripple and switching mode;
3. adjudicate its family lineage;
4. recheck Tran only if a legal readable full-text route becomes available; do not bypass access controls;
5. rerun a narrowly bounded stopping round after Li is no longer uncaptured evidence;
6. keep independent review, formal Pareto and Research Gap gates locked.

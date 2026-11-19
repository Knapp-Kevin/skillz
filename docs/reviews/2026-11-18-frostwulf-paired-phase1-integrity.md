# Phase-one paired-host evaluation: independent specification-integrity receipt

Date: November 18, 2026 (owner-local), issue [#738](https://github.com/Knapp-Kevin/skillz/issues/738).
Scope: a **passive external-host evaluation contract and acceptance ledger**, not a model run, CI suite, credential scan or tool authorization.

## Exact inspected records

- `registry/migration/frostwulf-independent-replacement-ledger-20261118.json`: source for all 44 historical entrypoint -> 21 replacement mappings.
- `registry/authored-skills-index.json`: consulted current content blob `4003cf8794189ca346301fc507f14d71655df867` for replacement package/source pins and static review state.
- `registry/evaluation/frostwulf-paired-host-status-20261118.json`: actual Git blob `0319392fc0cd2dce026fa0d55f33ee16a9aaec71`.
- `docs/evals/frostwulf-phase1-paired-scenarios.json`: actual Git blob `b49a37ed66b39c20fc1eb96d6b8490d72f39e4b4`.
- `docs/evals/frostwulf-paired-evaluation-protocol.md`: staged protocol, separate from behavioral outcomes.

## Deterministic review actually performed

The repository-connected maintainer reviewer parsed the two new JSON documents and current authored index with an **ephemeral external-host script**, without adding a runtime to Skillz. The verification checked unique historical identities, unique case IDs, exact five-category coverage, linked designed case IDs, matching source/fixture pins, existence of explicit expected and prohibited outcomes for every designed case, and whether any execution status was falsely promoted.

| Invariant | Observed | Outcome |
| --- | ---: | --- |
| Historical entrypoints unique | 44/44 | PASS (specification integrity) |
| Distinct authored package IDs | 21 | PASS |
| Required scenario slots (44 × 5) | 220 | PASS |
| Fully authored, independent synthetic case contracts | 20 | PASS |
| Slots still requiring scenario content | 200 | Explicit NOT_DESIGNED |
| Distinct case identifiers | 220/220 | PASS |
| Ledger authored package pins matching current index | 44/44 | PASS |
| Case links, kinds and package pins consistent | 20/20 | PASS |
| Critical positive and negative outcome lists present | 20/20 | PASS |
| Host/model paired executions reported | 0 | NOT_RUN |

The independent entrypoint blob comparison against live `main` matched all **four** pinned historical SKILL files for `agent-postmortem`, `todo-harvester`, `decision-log` and `github-pulse`. The original GitHub pulse's **bundled** `sources.json` also matched Git blob `bfdce4b0e819ceab937b1b92d31313cde11595f4`.

**Important unresolved source-integrity gate:** a current, exhaustive directory/package-tree inventory for those four historical packages has **not** been established. Checking SKILL.md plus one known support file is not proof every supporting asset has been found. An external host must resolve that before recording a complete behavioral pair or using any historical bundle.

## Four first-wave workflows

Each has one nominal, one challenging, one missing-evidence, one adversarial-authority and one integration case:

1. Incident forensics: `agent-postmortem` -> `agent-failure-boundary-analysis`.
2. Repository annotation debt: `todo-harvester` -> `source-debt-triage`.
3. Decision continuity: `decision-log` -> `decision-record-steward`.
4. GitHub public discovery: `github-pulse` -> `technology-change-intelligence#github-discovery`.

These cases use original **synthetic**, no-secret fixtures. They can test reasoning, output shape, refusal and authority discipline, but cannot establish production search freshness, permission isolation across real accounts, actual filesystem writes or delivery.

## Scope and next qualification

The 200 not-yet-designed slots include the remaining 40 historical entrypoints and all other 16 technology intelligence profiles. This is **not** an assertion that those modes have never been source-reviewed: many have original synthetic examples already. The count only describes coverage by the new explicitly pre-registered **paired** protocol.

No old/new host model executions were available or performed in this pass. No observed scores, cost/performance values, comparative ratios, confidence bounds or user-outcome receipts exist. Therefore:

- **Behavioral parity: NOT_PROVEN** for 44/44 predecessor modes.
- **Measured >=1.5x improvement: NOT_PROVEN**.
- **Original source retirement: HOLD**, including separate PR #737.
- **Skillz index semantic state: unchanged**, all 21 replacement packages retain their earlier static review and `behavioral_validation: not-run`.

Next external-host executor: verify full exact source package contents, run fresh isolated A/B turns with identical synthetic fixtures and host permissions, capture sanitized observations, then have an independent reviewer adjudicate critical gates and preregistered quality scores. Only verified outcomes may be added to the ledger. No source deletions or rights claims follow from this review.

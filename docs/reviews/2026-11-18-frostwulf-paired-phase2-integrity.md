# Paired-host phase 2: exact-source and contract-integrity evidence

Review date: November 18, 2026 (owner local). Issue [#738](https://github.com/Knapp-Kevin/skillz/issues/738). Scope: 45 new original synthetic paired cases, complete **historical entrypoint** SHA pinning for all 44, and individual retirement HOLD records. No host model execution or historical source deletion.

## Factual changes

- Precisely **nine** additional historical workflows have received five unique detailed scenario contracts each: permissions review, MCP vetting, scheduled-work receipts, session handoff, repository health, monthly finance review, task coordination, paper digest and fact-checking.
- Both independent phase fixture groups now provide **65 designed of 220 total paired case slots**. Their ledger tracks **155 not designed**; all 220 retain `NOT_RUN`.
- Every one of the 44 historical SKILL.md entrypoints was individually fetched through the connected repository at immutable commit `319b6eae2dedf3e8ca1ceac77aaed5a710d91ff0`. The exact 40-hex Git blob SHA for each is stored in the ledger. Existing known pins in the new scenario contracts were compared and did not conflict.
- All 44 replacement package trees and corresponding SKILL blobs continue to match the unchanged current authored index, which represents 21 unique packages.
- The [retirement procedure](../evals/frostwulf-per-source-retirement-gates.md) explicitly requires full original **package**, observed functional parity including negative conditions, independent reviewer findings, source/rights preservation, complete consumer links and owner acceptance before historical source removal. Per-source ledger retains `eligible_for_retirement: false` for all 44. Existing PR #737 stays HOLD.

## Independent deterministic audit actually executed

The maintainer agent parsed the newly committed JSON via a short ephemeral external-host script. It inspected structural schema, unique source and case IDs, five challenge types per source, cross-links to exact fixture inputs and current authored index, source pin equality, required/prohibited oracle lists, planned-only host statuses, and retirement flags. This script was **not** committed as an active Skillz runtime and did not execute any historical skill code.

| Assertion | Actual result |
| --- | --- |
| Source mappings | 44 unique / 44 expected, PASS |
| Distinct replacement packages | 21 / 21, PASS |
| Legacy SKILL entrypoints pinned at immutable commit | 44 / 44, PASS |
| Required scenario slots | 220 / 220, PASS |
| Fully designed pairs phase 1 / phase 2 | 20 / 45, PASS |
| Designed pairs overall | 65 / 220, PASS |
| Case IDs unique | 220 / 220, PASS |
| Designed cases linked to correct source blob, versioned replacement package and scenario category | 65 / 65, PASS |
| Designed cases with positive and negative outcomes | 65 / 65, PASS |
| Replacement blob/tree pins matching authoritative index | 44 / 44, PASS |
| Host model pairs actually executed | 0, NOT_RUN |
| Original entrypoints qualified for retirement | 0, HOLD |
| Structural integrity errors from final checker | 0 |

Source identities at final branch review: `registry/evaluation/frostwulf-paired-host-status-20261118.json` Git blob `27f863fc7d52f0751957c3cda6a72a4913d291b4`; phase 1 `b49a37ed66b39c20fc1eb96d6b8490d72f39e4b4`; phase 2 `5c43d6fcb559bebe2e690e86ad4fed14a2c97615`; authored index `4003cf8794189ca346301fc507f14d71655df867`. These source identities apply **before any further changes to the ledger**.

## Explicit blockers

A SKILL.md fingerprint **does not** verify that a historical directory's complete package has been enumerated. Supporting source manifests, license notices and nested assets still need exhaustive, untruncated Git tree evidence before paired execution, especially the 17 pulse profiles' source lists.

No fresh, isolated original/replacement model-host turns were launched here. No observed behavior, cost, efficiency, comparative ratio or independent user acceptance was scored. No original-rights claim was resolved. A newly specified scenario is not a model result, and semantic quality/1.5× superiority remain NOT_PROVEN. The target can be met only with actual independent host runs and adjudication.

**Disposition:** phase 2 design and deterministic ledger-integrity check PASS; behavioral acceptance and retirement readiness NOT_ESTABLISHED. Preserve all 44 legacy sources and keep PR #737 on HOLD.

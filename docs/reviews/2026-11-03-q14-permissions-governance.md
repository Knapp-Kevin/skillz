# Q14: Accurate permission governance and README navigation

**Date:** 2026-11-03 · **Issues:** [#481](https://github.com/Knapp-Kevin/skillz/issues/481) (partial) and [#483](https://github.com/Knapp-Kevin/skillz/issues/483) (two named skills) · **Status:** **DRAFT / HOLD**

## What was fixed

1. **Permissions Review** still teaches a useful risk-ranked inventory of agent-accessible tools, hooks and credentials. It now starts with an *approved host/workspace/access scope*, classifies actions using the actual four governed authority tags, and does not read credential values. A one-time audit is the default. Scheduling and future private-data access need **separate user approval** with cadence, sources, recipients, retention and revocation.
2. **MCP Vetting** remains a static, non-installing review of a proposed MCP server. It now inventories the entire tool surface, credentials and outbound data flows against exact source pins. It no longer invents nonexistent source-trust score caps or legacy permission tiers, or treats a retired candidate registry as an admission gate. Missing evidence remains unknown, and a favorable static review cannot authorize connecting a server.
3. **Repository guidance** now explains the actual passive boundary. Ordinary visitors cannot be asked to run anything or give the library background account access. The tree *does* contain a manually invoked dashboard generator and two QA-source scripts; only an explicitly authorized external maintainer can run approved checks for a bounded maintenance task. Their presence does not permit CI, scheduled jobs, background agents or approval claims.
4. **README** adds a short governance/status guide and safe link to the live issue/PR views. It leaves the original **20-method merged-main** dashboard and its generated markers intact. Q8’s **draft** catalog totals must not be substituted for the current checked-out main branch without an actual merge.

## Exact identities

| Skill | Previous main blob | Revised blob | Full package tree | Semantic score |
|---|---|---|---|---:|
| Permissions Review | `60e1d546e713cfa5b289def082dd73e8b326f029` | `dcaf7ff96c832c69bb5be1c7cd8f4c3ed418b707` | `8b8cbd95cbcb4f053c1070fdb4400c823593863f` | 17/20 |
| MCP Vetting | `806e79f593446ad15938249898e15230208f2d81` | `37a13d7296c7d3d87dc360988bc6aca1f873c4db` | `a8824fff4a3d0ed5b7a82603b48f1aefbccb9666` | 19/20 |

Both revised skill files are byte-identical to previously reviewed exact files from **closed-unmerged #489**. Source snapshot revisions now point to commits made on this branch, not expired historical patch commits. The prior semantic scores are source-static judgments carried over by exact Git identity, **not** newly executed tests. The 44-entry consolidated first-party verification registry was compared against the branch Git tree: **44/44 source fingerprints match**, no unrelated entries changed.

## Governance and safety boundaries

The current controlled authority tags are `read-only`, `generate-only`, `mutating`, and `external-side-effect`, as published in [registry/taxonomy.yaml](../../registry/taxonomy.yaml). These describe observable effects, not permissions or scoring thresholds. Identity access, destructive operations, payment, credentials, notifications and user-private data require separate risk and approval reasoning. Issue-first [candidate intake](../candidate-intake.md) controls any proposed addition to the governed third-party corpus.

Static review and license compliance remain separate from security scans and real behavior. The current root [MIT license](../../LICENSE) applies to first-party content, subject to its notice requirements; it cannot authorize host account access or change the rights of cited third-party source material.

## What remains open

- **Issue #483:** Both named skill instructions have a *source-static repair* on this branch, but #483 stays OPEN until exact-package security, independent real-behavior and owner-approved merge gates pass.
- **Issue #481:** This addresses the shared `permissions-review` skill, only **one of four** skills listed. `learning-plan`, `standup-writer` and `week-in-review` remain unmodified and separately require recurring-access fixes.
- **Concurrent branch risk:** Other first-party repairs in #673, #686 and #702 touch shared registry surfaces. Recheck their accepted source identities before final integration. Never overwrite accepted work with an older snapshot.
- **Nine adversarial scenarios:** Their expected behaviors are documented in the [machine receipt](../../registry/maintenance/q14-permissions-governance-static-20261103.json), but **none was actually executed**. No new SkillSpector report, installer, scanner pass, generated dashboard build or actual behavioral validation is claimed.

## Maintainer handoff

Recheck current main, run only an approved pinned external scanner against both final package trees, record actual host-observed no-unauthorized-read/recurrence and no-connect behavior, reconcile full provenance and the 44-record registry, inspect README/governance links and generated-block boundaries, and request explicit maintainer merge acceptance. Use `[skip ci]`; no repository-owned automation or test runner is introduced.


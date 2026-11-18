# Federated Source Catalog: exact-package static review

**Date:** 2026-11-18. **Type:** complete-package textual static inspection by ChatGPT, not an observed host/connector behavior test. **Source:** original independently expressed first-party text, MIT notice included. **Review basis:** [Skill Verification Standard](../skill-verification.md); exact recorded tree and linked references.

## Source identity and scope

- Entry: `skills/authored/federated-source-catalog/SKILL.md`.
- Git blob: `4d028afe00921af05f8258e0c7f50707d2ebb68c`; complete package tree: `130b199cc7c5549d8905196d62f54617198d1976`.
- Files inspected (6): `SKILL.md`, `LICENSE`, `references/provider-adapter-matrix.md`, `references/federated-record-contract.md`, `references/authority-and-freshness.md`, `examples/federated-cases.md`.
- License: original author-owned MIT package text, no third-party source document, credential or provider SDK material copied.
- Dependencies: passive text, no bundled runtime. Actual source actions conditional on externally connected host and bounded user authority. Vendor documentation links do not imply an operational connector.
- Behavioral validation: **NOT RUN**. Security scans and any live accounts, ACL checks, actual file search, persistent indexes, exports, copies, sync, archive, deletion and revocation tests: **NOT RUN**.

## Why a distinct skill rather than extending the local curator

The [original File Lifecycle Curator](../../skills/authored/file-lifecycle-curator/SKILL.md), reviewed at blob `63577971773ae0d923f6d38165c13c34f36b8f72` and package tree `12e7f8d07bdd1553f7ed78e377ebc7b5e9742a84`, governs a bounded file collection and downstream document enrichment. It does not describe a complete per-principal, per-connector federation policy or independent source completeness/disclosure status. The new skill owns those boundaries and delegates allowed per-file enrichment. The existing skill remains unchanged during external testing, so its exact-version review and tests stay applicable.

The mapped first-party inventory includes neighboring `session-continuity`, `paper-digest` and `repo-doctor`. Current qualified third-party federation equivalence is **not established**: the broader unmapped inventory and discovery leads still need complete-package comparison. One author-created skill is not proof a new domain's essential outcomes are served.

## Rubric

| Dimension | /2 | Observed static rationale |
|---|---:|---|
| Trigger precision | 2 | Cross-source vs single-file, broad crawl, sync and migration separated |
| Procedural clarity | 2 | Source roster, capability matrix, scoped enumeration, identity graph, retrieval, enrichment handoff |
| Authority/safety | 2 | Per-principal access, no implicit egress or shared catalog, separate mutation/persistence plane |
| Failure handling | 2 | Cursor/truncation/403/revocation/branch drift/incomplete connector behavior |
| Evidence discipline | 2 | Source-native ID, revision, coverage, observation time, no invented ACL or completeness |
| Dependency coherence | 2 | All six required files exist; no hidden token, network, database or SDK |
| Portability | 2 | Tool-independent text plan; host-dependent access stated |
| Usefulness/differentiation | 1 | Federated boundary strongly distinct; exhaustive external source comparison incomplete |
| Adversarial resilience | 2 | Private target, prompt-injection, second viewer, hidden metadata and revocation examples |
| Effectiveness design | 1 | Structured schema and expected cases, no observed permission/search correctness |
| **Total** | **18/20** | **Static verified; behavior NOT RUN** |

No identified static hard-fail for the defined read-only scope. Static review cannot certify actual per-viewer ACL enforcement, cross-connector completeness, source-secret handling or operational safety. Reassess the exact version if any supporting file changes.

## Static case review

Synthetic cases cover Drive shortcut/private target, native Docs vs PDF exports, GitHub pinned commit vs moving branch, missing local reader, incomplete pagination, provider 403, malicious README, cross-user cached catalog leakage and an unapproved consolidation request. Expected outcomes are written in `examples/federated-cases.md`. They have **not** been executed in a real agent host and cannot prove enforcement.

## Follow-up and external tester handoff

See [File and Federation gap audit](2026-11-18-file-information-management-gap-audit.md) for issues, acceptance criteria, recommended ownership and open implementation blockers. Qualify a small synthetic host pilot of these 12 cases, then read back connector statuses and ACL isolation in the actual authorized environment. Keep rejected, stale and absent source evidence visible. Do not merge an untested persistent shared index into the passive skill package.

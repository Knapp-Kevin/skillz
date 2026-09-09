# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-08 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | 422 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Skills current-standard gaps** | 0 |
| **Microsoft Azure Skills current-standard companions** | 34 / 34 |
| **Microsoft Azure Skills current-standard gaps** | 0 |
| **Cole Medin Skills current-standard companions** | 33 / 33 |
| **Cole Medin Skills current-standard gaps** | 0 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Microsoft Rust direct-package companions** | 9 / 9 |
| **Microsoft TypeScript direct-package companions** | 25 / 25 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **44/44 provenance-complete** with structured semantic review evidence. The latest admission is `session-continuity`, a substrate-agnostic continuity procedure verified **19/20**, behavioral validation `not-run`; recall is scoped/read-only and persistent capture is authorization-gated and sensitive-data-minimized.
- AWS Agent Toolkit: **72/72** current-standard companion-complete.
- Microsoft Skills: **186/186** companion-complete, **0 gaps**.
- Microsoft Azure Skills: exact registered-pin denominator **34**, **34/34** companion-complete, **0 gaps** at pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Cole Medin Skills: exact registered-pin denominator **33**, **33/33** companion-complete, **0 gaps** at pin `fb2e876f057c5356d6603ba0c52d6b4418d893ba`.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## First-party session continuity

Issue #71 established that admissible wild prior art did not cover the cross-session memory-continuity primitive, and issue #73 bounded a first-party derivation. `session-continuity` expresses a portable procedure for scoped recall, correction precedence, explicit continuity gaps, and minimal durable records. It does not implement, mirror, schedule, monitor, or otherwise own a memory substrate.

Persistent memory capture is treated as a mutation: a current request or applicable standing policy must authorize durable capture before it occurs. Secret material is excluded, and sensitive personal data requires specific durable-capture authority plus necessity. Prior memory is evidence, not current action authorization.

## Microsoft Azure Skills denominator reconciliation

The exact pin exposes 28 canonical plugin skill roots, one additional nested Kubernetes automatic-readiness package, and five additional nested first-class Microsoft Foundry packages beyond the Foundry root. That yields an eligible denominator of **34**, exactly matching the current companion pairs. Ordinary workflow, procedure, reference, example, SDK, or other Markdown is not independently first-class skill content. The latest Azure package-level reconciliation remains `python-appservice-deploy`, rejected unchanged **12/20**, behavioral validation `not-run`.

## Cole Medin Skills completion

The registered pin contains **33** first-class `.claude/skills/*/SKILL.md` entries, and all thirty-three now have current companion pairs.

The final package, `worktree-merge`, is bound to package tree `150cb167cb6c0bd703e3ba5b05330aa7f9db9861`, `SKILL.md` blob `9912484e1f99ce5ae7f5fd25f88a3d60f3e61c2b`, and skill-path freshness revision `1c46cd18bc6100d358082c06357d649f7a4cf8c6` on 2026-08-09. It is rejected unchanged **15/20** with behavioral validation `not-run`. Preserve its repository-detected validation model, disposable integration branch, per-branch test localization, conflict stop, full-suite gate, rollback guidance, and explicit cleanup choice. Unchanged use remains rejected because it creates and merges branches, including the final merge into the original branch, without mandatory action-specific authorization immediately before the consequential mutation. Repository-controlled CI workflows, Makefiles, manifests, and discovered validation commands are also treated as executable guidance without an explicit hostile-instruction boundary.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
2. Continue governed discovery/source-vetting and omission recovery.
3. Resolve bounded candidate issues when evidence supports a decisive outcome.
4. Continue the corpus-wide provenance audit in issue #66 until every governed family is truthfully accounted for.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.

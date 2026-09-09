# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-09 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | 425 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Skills current-standard gaps** | 0 |
| **Microsoft Azure Skills current-standard companions** | 34 / 34 |
| **Microsoft Azure Skills current-standard gaps** | 0 |
| **Cole Medin Skills current-standard companions** | 33 / 33 |
| **Cole Medin Skills current-standard gaps** | 0 |
| **Matt Pocock Skills current-standard companions** | 29 / 29 |
| **Matt Pocock Skills current-standard gaps** | 0 |
| **Cloudflare Skills current-standard companions** | 13 / 13 |
| **Cloudflare Skills current-standard gaps** | 0 |
| **Addy Osmani Agent Skills current-standard companions** | 13 / 24 |
| **Addy Osmani Agent Skills current-standard gaps** | 11 |
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

- First-party: **44/44 provenance-complete** with structured semantic review evidence. The latest admission is `session-continuity`, verified **19/20**, behavioral validation `not-run`.
- AWS Agent Toolkit: **72/72** current-standard companion-complete.
- Microsoft Skills: **186/186** companion-complete, **0 gaps**.
- Microsoft Azure Skills: **34/34** companion-complete, **0 gaps** at pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Cole Medin Skills: **33/33** companion-complete, **0 gaps** at pin `fb2e876f057c5356d6603ba0c52d6b4418d893ba`.
- Matt Pocock Skills: **29/29** companion-complete, **0 gaps** at pin `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`; `deprecated` and `in-progress` are excluded by source policy.
- Cloudflare Skills: **13/13** companion-complete, **0 gaps** at pin `f96bff754e428838818017f75817f0f9428acd48`; dispositions remain **11 verified / 2 rejected unchanged**.
- Addy Osmani Agent Skills: exact denominator **24**, **13/24** current-standard companion pairs, **11 gaps** at pin `f63ec56a3cc936408d792956ae583c3c96a825bd`; historical issue #27 records decisive exact-version states for all 24.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## First-party session continuity

Issue #71 established that admissible wild prior art did not cover the cross-session memory-continuity primitive, and issue #73 bounded a first-party derivation. `session-continuity` expresses a portable procedure for scoped recall, correction precedence, explicit continuity gaps, and minimal durable records. It does not implement, mirror, schedule, monitor, or otherwise own a memory substrate.

Persistent memory capture is treated as a mutation: a current request or applicable standing policy must authorize durable capture before it occurs. Secret material is excluded, and sensitive personal data requires specific durable-capture authority plus necessity. Prior memory is evidence, not current action authorization.

## Microsoft Azure Skills denominator reconciliation

The exact pin exposes 28 canonical plugin skill roots, one additional nested Kubernetes automatic-readiness package, and five additional nested first-class Microsoft Foundry packages beyond the Foundry root. That yields an eligible denominator of **34**, exactly matching the current companion pairs. Ordinary workflow, procedure, reference, example, SDK, or other Markdown is not independently first-class skill content. The latest Azure package-level reconciliation remains `python-appservice-deploy`, rejected unchanged **12/20**, behavioral validation `not-run`.

## Cole Medin Skills completion

The registered pin contains **33** first-class `.claude/skills/*/SKILL.md` entries, and all thirty-three now have current companion pairs. The final package, `worktree-merge`, is rejected unchanged **15/20** with behavioral validation `not-run`. Preserve its repository-detected validation model, disposable integration branch, per-branch test localization, conflict stop, full-suite gate, rollback guidance, and explicit cleanup choice. Unchanged use remains rejected because branch creation/merging and repository-controlled executable guidance lack the current authorization/hostile-instruction boundaries.

## Matt Pocock Skills reconciliation

The registered exact pin is `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`. Applying the source registry exclusions for `deprecated` and `in-progress` yields exactly **29** eligible first-class packages. Provenance and verification expose the same 29 named records, with canonical physical paths under `skills/sources/mattpocock-skills/`.

## Cloudflare Skills reconciliation

The registered exact pin is `f96bff754e428838818017f75817f0f9428acd48`. Historical source queue #27 establishes **13/13**, with **11 verified / 2 rejected unchanged**. All live companion paths resolve under `skills/sources/cloudflare-skills/`. `web-perf` remains rejected for the unresolved privacy/telemetry boundary around Chrome DevTools MCP; `wrangler` remains rejected because install/deploy/delete/migration/secret/resource operations lack action-specific authorization. Behavioral validation remains `not-run` across the family.

## Addy Osmani Agent Skills reconciliation

The registered exact pin is `f63ec56a3cc936408d792956ae583c3c96a825bd`. The pinned upstream tree exposes exactly **24** first-class `skills/*/SKILL.md` packages, matching historical issue #27's 24/24 decisive static-review record. Current canonical shelves now contain **13** provenance/verification companion pairs, leaving **11** current-standard gaps.

The latest reconciled unit is `deprecation-and-migration`, bound to exact `SKILL.md` blob `765bdde6329dbd5fd22d5d3fc2c185737fc9f908` and skill-path freshness revision `5a4a69adfc7f70d4a284d5dca7b0d0de575cc802` dated 2026-07-05. It is rejected unchanged **14/20** with behavioral validation `not-run`. Preserve its deprecation decision framing, strangler/adapter patterns, usage verification, expand-contract database migration, rollback/down-path discipline, and zombie-code ownership. Unchanged use hard-fails the authority rule because it directs code/config removal, production traffic shifts, feature-flag changes, database backfills and destructive schema operations, deployments, and user migration/communications without mandatory action-specific authorization immediately before consequential mutation.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review, with Addy Osmani at **13/24** current-standard companions and **11** gaps.
2. Continue governed discovery/source-vetting and omission recovery.
3. Resolve bounded candidate issues when evidence supports a decisive outcome.
4. Continue the corpus-wide provenance audit in issue #66 until every governed family is truthfully accounted for.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.

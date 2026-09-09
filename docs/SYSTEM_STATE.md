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
| **Matt Pocock Skills current-standard companions** | 29 / 29 |
| **Matt Pocock Skills current-standard gaps** | 0 |
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
- Matt Pocock Skills: exact registered-pin denominator **29**, **29/29** companion-complete, **0 gaps** at pin `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`; `deprecated` and `in-progress` are excluded by source policy.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Matt Pocock Skills reconciliation

The registered exact pin is `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`. Applying the source registry exclusions for `deprecated` and `in-progress` yields exactly **29** eligible first-class packages. The provenance and verification companion directories each expose the same 29 named records, and live repository search finds no remaining `vendor/mattpocock-skills/...` companion path. The earlier Wayfinder and three-package repairs therefore completed path normalization rather than leaving a residual family gap. Historical 29/29 review evidence can now be promoted as current-standard companion-complete without re-reviewing unchanged exact material.

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

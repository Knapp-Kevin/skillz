# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-05 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 356 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 184 / 189 |
| **Microsoft Skills current-standard gaps** | 5 |
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

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **184/189 companion-complete**, **5 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

On 2026-09-05, the Microsoft frontier was reconciled against the current companion contract. Ten exact reviews from `kql` through `wiki-architect` that existed only as auxiliary Markdown evidence now also have mandatory YAML pairs under `registry/skills/` and `registry/verification/`. `skill-creator` already had a canonical YAML pair, so its later Markdown re-review did not add a new companion; that YAML pair was refreshed to the current 15/20 rejected authority disposition. Public accounting after the subsequent `microsoft-foundry/models/deploy-model/capacity` review resolves to **356 third-party exact-version companions / Microsoft Skills 184/189 / 5 gaps**.

## Active Microsoft frontier

The direct language slices, `deep-wiki`, and `microsoft-365-agents-toolkit` are companion-complete. Exact-pin reconciliation confirms the `microsoft-foundry` plugin exposes ten dangling symlinks rather than independent skill packages; canonical Foundry material lives under `.github/plugins/azure-skills/skills/microsoft-foundry`. The canonical root and `finetuning` were already companion-complete. Nested `models/deploy-model` is verified 17/20, and its independently front-mattered `capacity` descendant is now **verified, 17/20**, bound to package tree `edb0b5bb776569c8941e4ed3755d9f65e32c5b80` and `SKILL.md` blob `46935315ebdf18fbc93771efb72e7f8f9e9980ac`, with freshness revision `2d821920c717bcdd5ee4e287a41205c07e43cb0a` from 2026-05-05. `capacity` is read-only: it queries model capacity, subscription quota, and existing project locations, ranks candidates, explicitly does not deploy, and confirms the target project before handing off to a mutating deployment skill. Behavioral validation remains `not-run`.

Microsoft Skills remains active with **5** gaps. Continue through the remaining independently front-mattered descendants under the Foundry model subtree, checking companions and repository history before each review.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Complete the remaining Microsoft Foundry nested model skill companions.
2. Complete remaining Microsoft Skills non-direct gaps.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
5. Continue governed discovery/source-vetting and omission recovery.
6. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
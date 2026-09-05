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
| **Persisted third-party review companions** | 347 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 175 / 189 |
| **Microsoft Skills current-standard gaps** | 14 |
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
- Microsoft Skills: exact denominator **189**, **175/189 companion-complete**, **14 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

On 2026-09-05, the Microsoft frontier was reconciled against the current companion contract. Ten exact reviews from `kql` through `wiki-architect` that existed only as auxiliary Markdown evidence now also have mandatory YAML pairs under `registry/skills/` and `registry/verification/`. `skill-creator` already had a canonical YAML pair, so its later Markdown re-review did not add a new companion; that YAML pair was refreshed to the current 15/20 rejected authority disposition. Public accounting after the subsequent `wiki-qa` review resolves to **347 third-party exact-version companions / Microsoft Skills 175/189 / 14 gaps**.

## Active Microsoft frontier

The direct TypeScript slice is **25/25 current-standard companion-complete**. The non-direct Microsoft plugin/front-door frontier is active. Latest closure: `wiki-qa` is **verified, 18/20**, bound to package tree `80775b0be2ffbef4a1675afeaaa132696bdd1d01` and `SKILL.md` blob `2568639d0204aff644b86563342487fec78eb332`, with freshness revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. Preserve repository-context resolution, source-file-only evidence, search-and-read-before-answer discipline, inline file/line citations, explicit insufficiency handling, and the prohibition on guessing or external knowledge. The package is read-only and does not direct persistent workspace mutation or external side effects, so the authority hard fail does not apply. Main weaknesses are Git-centric source-context assumptions, an unnecessary user question when context may already be resolvable, and rigid Mermaid/table requirements. Behavioral validation is `not-run`.

Microsoft Skills remains active with **14** gaps. Establish the next gap from the exact registered-pin `deep-wiki` tree after `wiki-qa`, checking canonical registry companions and repository history before review.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in registered-pin source order from the first genuine gap after `wiki-qa` in `deep-wiki`.
2. Complete remaining Microsoft Skills non-direct families.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
5. Continue governed discovery/source-vetting and omission recovery.
6. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
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
| **Persisted third-party review companions** | 350 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 178 / 189 |
| **Microsoft Skills current-standard gaps** | 11 |
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
- Microsoft Skills: exact denominator **189**, **178/189 companion-complete**, **11 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

On 2026-09-05, the Microsoft frontier was reconciled against the current companion contract. Ten exact reviews from `kql` through `wiki-architect` that existed only as auxiliary Markdown evidence now also have mandatory YAML pairs under `registry/skills/` and `registry/verification/`. `skill-creator` already had a canonical YAML pair, so its later Markdown re-review did not add a new companion; that YAML pair was refreshed to the current 15/20 rejected authority disposition. Public accounting after the subsequent `declarative-agent-developer` review resolves to **350 third-party exact-version companions / Microsoft Skills 178/189 / 11 gaps**.

## Active Microsoft frontier

The direct TypeScript slice is **25/25 current-standard companion-complete** and the `deep-wiki` family has been advanced through its final reviewed unit. The next active family is `microsoft-365-agents-toolkit`. Latest closure: `declarative-agent-developer` is **rejected unchanged, 13/20**, bound to package tree `5e6287047863c5d889fe3b19f13ee4382d5f7e34` and `SKILL.md` blob `a974c332cdbed595eed80f79285ba12d7946f61e`, with freshness revision `a43d2c6a69fac2298ac0f301419931b39d996c6b` from 2026-06-15. Preserve mandatory workspace fingerprinting, hard reject/fix/edit routing, Detect-Inform-Ask error handling, schema-version gates, anti-fabrication rules, instruction-quality review, localization guidance, and its bundled M365 agent references. Unchanged adoption fails the authority hard rule because the package directs or documents project scaffolding and consequential M365 operations including provisioning, sharing, publishing, authentication, OAuth/permission setup, and production environments without a universal action-specific authorization checkpoint immediately before each external mutation. The `npx -y --package` availability check may also download the CLI despite prose saying not to install it. Behavioral validation is `not-run`.

Microsoft Skills remains active with **11** gaps. Continue through `microsoft-365-agents-toolkit` in exact registered-pin source order, checking canonical registry companions and repository history before review.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills through the `microsoft-365-agents-toolkit` family from the first genuine remaining gap after `declarative-agent-developer`.
2. Complete remaining Microsoft Skills non-direct families.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
5. Continue governed discovery/source-vetting and omission recovery.
6. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
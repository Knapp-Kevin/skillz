# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-04 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 325 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 153 / 189 |
| **Microsoft Skills current-standard gaps** | 36 |
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
- Microsoft Skills: exact denominator **189**, **153/189 companion-complete**, **36 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

The direct TypeScript slice is **25/25 current-standard companion-complete**. Twenty-two packages are rejected unchanged and three bounded local implementation packages are verified: `frontend-ui-dark-ts` **15/20**, `react-flow-node-ts` **15/20**, and `zustand-store-ts` **16/20**. Exact identities, freshness, authority, portability, dependencies, rationale, and validation state remain in their individual companion records.

The non-direct Microsoft plugin frontier is active. Reviewed packages now include `airunway-aks-setup` (15/20), `appinsights-instrumentation` (12/20), `azure-ai` (10/20), `azure-aigateway` (8/20), `azure-cloud-migrate` (9/20), `azure-compliance` (12/20), `azure-compute` (11/20), `azure-cost` (14/20), `azure-deploy` (15/20), `azure-diagnostics` (13/20), `azure-enterprise-infra-planner` (verified, 18/20), `azure-hosted-copilot-sdk` (13/20), `azure-kubernetes` (12/20), `azure-kubernetes-automatic-readiness` (15/20), `azure-kusto` (14/20), `azure-messaging` (13/20), `azure-prepare` (16/20), `azure-quotas` (14/20), `azure-rbac` (verified, 17/20), `azure-reliability` (rejected, 15/20), and `azure-resource-lookup` (**rejected, 14/20**). `azure-resource-lookup` is bound to package tree `19e257c3720521014d81cd3dbf4e188e0ece621b`, `SKILL.md` blob `d16d74bd6369fd15f8d96ff0b637ac361c7d6e13`, freshness revision `981d9b71d0187be796b03c2f4d69cccca80c0e42` from 2026-05-25. Preserve its dedicated-tool-first lookup routing, scoped ARG execution, result shaping, orphan discovery, tag/configuration audit, and health-state inspection. Unchanged adoption is rejected because its missing-extension path installs the Resource Graph CLI extension without a mandatory action-specific authorization checkpoint. Behavioral validation is `not-run`.

Microsoft Skills remains active with **36** gaps. Establish the next gap from the registered-pin tree after `azure-resource-lookup`.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in registered-pin source order from the first genuine gap after `azure-resource-lookup`.
2. Complete remaining Microsoft Skills non-direct plugin families.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
5. Continue governed discovery/source-vetting and omission recovery.
6. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
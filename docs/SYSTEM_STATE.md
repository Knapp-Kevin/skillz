# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-06 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 382 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Skills current-standard gaps** | 0 |
| **Microsoft Azure Skills current-standard companions** | 24 / 131 |
| **Microsoft Azure Skills current-standard gaps** | 107 |
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
- AWS Agent Toolkit: **72/72** current-standard companion-complete.
- Microsoft Skills: **186/186** companion-complete, **0 gaps**.
- Microsoft Azure Skills: exact registered-pin denominator **131**, **24/131** companion-complete, **107 gaps** at pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Microsoft Azure Skills frontier

`airunway-aks-setup`, `azure-cloud-migrate`, and `azure-rbac` are verified **17/20**. `azure-enterprise-infra-planner` is verified **18/20**. `appinsights-instrumentation`, `azure-ai`, `azure-aigateway`, `azure-diagnostics`, `azure-hosted-copilot-sdk`, and `azure-messaging` are rejected unchanged **13/20**. `azure-compliance`, `azure-kubernetes`, and `azure-storage` are rejected unchanged **12/20**. `azure-compute` is rejected unchanged **11/20**. `azure-cost`, `azure-kusto`, `azure-quotas`, and `azure-resource-lookup` are rejected unchanged **14/20**. `azure-deploy`, `azure-kubernetes-automatic-readiness`, `azure-reliability`, `azure-resource-visualizer`, and `azure-upgrade` are rejected unchanged **15/20**. `azure-prepare` is rejected unchanged **16/20**. Behavioral validation remains `not-run` for all twenty-four reviewed Azure packages.

`azure-upgrade` is bound to exact tree `ad4f782ddd8eab34eacece4ccb1b66d65a0434d9`, `SKILL.md` blob `6b87a36c181440dd213443b19a2a58d25504a1ba`, and Azure-source freshness revision `f8c23b595202c899d7cf193ed0ae9b5363fa0296` on 2026-06-01. Exact package identity matches the completed Microsoft Skills package, so compatible complete-package evidence was reconciled rather than repeated. Preserve its assessment-first sequencing, target plan/SKU confirmation, explicit confirmation before resource creation and destructive actions, rollback discipline, idempotent/resumable automation, and scenario-specific migration references. Unchanged adoption remains rejected because bundled Functions automation retrieves the live `AzureWebJobsStorage` connection string into shell state and uses it directly for blob operations instead of requiring an identity-based secure credential path; the same prerequisite sequence installs the Resource Graph CLI extension without a distinct action-specific authorization checkpoint. Behavioral validation remains `not-run`.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Azure Skills from **24/131**, checking canonical companion paths and repository history before each unit.
2. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
3. Continue governed discovery/source-vetting and omission recovery.
4. Resolve bounded candidate issues when evidence supports a decisive outcome.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
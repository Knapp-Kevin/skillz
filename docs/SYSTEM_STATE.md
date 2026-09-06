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
| **Persisted third-party review companions** | 377 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Skills current-standard gaps** | 0 |
| **Microsoft Azure Skills current-standard companions** | 19 / 131 |
| **Microsoft Azure Skills current-standard gaps** | 112 |
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
- Microsoft Azure Skills: exact registered-pin denominator **131**, **19/131** companion-complete, **112 gaps** at pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Microsoft Azure Skills frontier

`airunway-aks-setup`, `azure-cloud-migrate`, and `azure-rbac` are verified **17/20**. `azure-enterprise-infra-planner` is verified **18/20**. `appinsights-instrumentation`, `azure-ai`, `azure-aigateway`, `azure-diagnostics`, `azure-hosted-copilot-sdk`, and `azure-messaging` are rejected unchanged **13/20**. `azure-compliance` and `azure-kubernetes` are rejected unchanged **12/20**. `azure-compute` is rejected unchanged **11/20**. `azure-cost`, `azure-kusto`, and `azure-quotas` are rejected unchanged **14/20**. `azure-deploy` and `azure-kubernetes-automatic-readiness` are rejected unchanged **15/20**. `azure-prepare` is rejected unchanged **16/20**. Behavioral validation remains `not-run` for all nineteen reviewed Azure packages.

`azure-rbac` is bound to exact tree `b52d696609b18a5dc2bae21e368812fe7b020ec5`, `SKILL.md` blob `02ac75d2ba22b4d7aa1e74469b01575281f05ddc`, and Azure-source freshness revision `317a8e7b879c0ed6a1890378eafd939bdd9bc749` on 2026-04-22. Exact package identity matches the completed Microsoft Skills package, so compatible complete-package evidence was reconciled rather than repeated. Preserve its least-privilege-first role selection, custom-role fallback, explicit role-assignment capability guidance, and preference for User Access Administrator over Owner when assignment is the only requirement. The package is generate-only and does not execute assignments or mutate Azure state, so the action-specific mutation authorization hard fail does not apply to unchanged use. Execution of generated artifacts remains a separate host-agent action requiring scoped authorization. Behavioral validation remains `not-run`.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Azure Skills from **19/131**, checking canonical companion paths and repository history before each unit.
2. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
3. Continue governed discovery/source-vetting and omission recovery.
4. Resolve bounded candidate issues when evidence supports a decisive outcome.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
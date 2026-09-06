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
| **Persisted third-party review companions** | 370 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Skills current-standard gaps** | 0 |
| **Microsoft Azure Skills current-standard companions** | 12 / 131 |
| **Microsoft Azure Skills current-standard gaps** | 119 |
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
- Microsoft Azure Skills: exact registered-pin denominator **131**, **12/131** companion-complete, **119 gaps** at pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Microsoft Azure Skills frontier

`airunway-aks-setup` and `azure-cloud-migrate` are verified **17/20**. `azure-enterprise-infra-planner` is verified **18/20**. `appinsights-instrumentation`, `azure-ai`, and `azure-aigateway` are rejected unchanged **13/20**. `azure-compliance` is rejected unchanged **12/20**. `azure-compute` is rejected unchanged **11/20**. `azure-cost` is rejected unchanged **14/20**. `azure-deploy` is rejected unchanged **15/20**. `azure-diagnostics` and `azure-hosted-copilot-sdk` are rejected unchanged **13/20**. Behavioral validation remains `not-run` for all twelve reviewed Azure packages.

`azure-hosted-copilot-sdk` is bound to exact tree `ee166d12b8f9a88a1d4d932a23e844d8203efa13`, `SKILL.md` blob `64b239df00aa320b64a9009c1875b303a87080b1`, and Azure-source freshness revision `4ac35b40b0df5379f3735a4882d3716f998e403d` on 2026-05-08. Exact package identity matches the current Microsoft Skills package, so compatible complete-package evidence was reconciled rather than repeated. Preserve its mandatory codebase detection, temp-directory scaffolding safeguard, managed-identity/passwordless authentication guidance, secure GitHub-token/Key Vault flow, BYOM guidance, and explicit prepare/validate/deploy composition. Unchanged adoption fails the current authority hard rule because troubleshooting directs `gh auth refresh --scopes copilot`, an identity/credential authorization change, without a mandatory action-specific approval immediately before mutation. Its deployment path also inherits the exact pinned `azure-deploy` package, currently rejected unchanged because post-deployment RBAC/database mutations lack a dedicated action-specific checkpoint; this package adds no compensating boundary. No literal-secret solicitation into conversational context was identified. Behavioral validation remains `not-run`.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Azure Skills from **12/131**, checking canonical companion paths and repository history before each unit; the next apparent source-tree candidate is `azure-kubernetes`.
2. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
3. Continue governed discovery/source-vetting and omission recovery.
4. Resolve bounded candidate issues when evidence supports a decisive outcome.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-03 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 309 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 137 / 189 |
| **Microsoft Skills current-standard gaps** | 52 |
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
- Microsoft Skills: exact denominator **189**, **137/189 companion-complete**, **52 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

The direct TypeScript slice is **25/25 current-standard companion-complete**. Twenty-two packages are rejected unchanged and three bounded local implementation packages are verified: `frontend-ui-dark-ts` **15/20**, `react-flow-node-ts` **15/20**, and `zustand-store-ts` **16/20**. Exact identities, freshness, authority, portability, dependencies, rationale, and validation state remain in their individual companion records.

The non-direct Microsoft plugin frontier is active. Current reviewed packages are:

1. `airunway-aks-setup` — **rejected unchanged, 15/20**. Strong positive-action setup safeguards, but rollback deletes model/secret state and undeploys providers/controllers without fresh destructive-action authorization.
2. `appinsights-instrumentation` — **rejected unchanged, 12/20**. Useful App Insights/OpenTelemetry mechanics, but cloud resource/configuration mutation, telemetry export, deployment changes, and shared-key handling lack mandatory target, production, disclosure, cost, deployment, and credential-custody authority.
3. `azure-ai` — **rejected unchanged, 10/20**. Useful Azure AI router/reference, but persistent search mutation and external processing of potentially sensitive audio/documents/text/images lack mandatory data-owner, disclosure/model-transfer, target, mutation, production, retention, cost, and credential-custody authorization.
4. `azure-aigateway` — **rejected unchanged, 8/20**. Useful APIM AI-gateway prior art, but identity/RBAC/backend/API/security/routing mutation, agent exposure, live endpoint calls, metrics, and subscription-key listing lack mandatory target, identity/access, security-control, production, downstream-effect, disclosure, cost, and credential-custody authority.
5. `azure-cloud-migrate` — **rejected unchanged, 9/20**, package tree `dd0d5a31e87576d5b46899b19aa3eedb24d412f4`, `SKILL.md` blob `b1634cf629d9358eb70a95c089b309c304f9c42c`, freshness revision `e12b7d24dab47df1d935783b31b196fdf43ad56b` from 2026-05-07. It preserves assessment-before-mutation, source preservation, scenario routing, service mapping, runtime modernization, staged conversion, progress reporting, service-discovery auditing, explicit destructive-action confirmation, and an explicit local-test-versus-Azure-deploy choice. Unchanged adoption still fails because bundled deployment guidance creates Azure resources, identities and RBAC assignments, imports images, exposes external ingress, migrates Kubernetes secrets into Key Vault, retrieves a Log Analytics primary shared key, and configures production-like scaling without mandatory per-resource target/environment, identity/access, security-control, secret/data-owner, credential-custody, network-exposure, production, retention/recovery, or cost authorization. Behavioral validation is `not-run`.

Microsoft Skills remains active with **52** gaps. Establish the next gap from the registered-pin tree after `azure-cloud-migrate`; do not infer it from stale prompts or historical issue text.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in registered-pin source order from the first genuine gap after `azure-cloud-migrate`.
2. Complete remaining Microsoft Skills non-direct plugin families.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
5. Continue governed discovery/source-vetting and omission recovery.
6. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
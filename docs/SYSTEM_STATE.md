# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-31 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 200 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS historical review** | 72 / 72 |
| **AWS current-standard companion complete** | 72 / 72 |
| **AWS current-standard gaps** | 0 |
| **Microsoft Skills current-standard companions** | 28 / 189 |
| **Microsoft Skills current-standard gaps** | 161 |
| **Microsoft .NET direct-package companions** | 24 / 29 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical physical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material, not repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party skills** are **43/43 provenance-complete** and have structured semantic review evidence.
- **12 pinned external corpora** provide the broad reference surface.
- **200 exact-version third-party verification companions** are persisted.
- `registry/sources.yaml` contains **19 unique source identities**.
- AWS Agent Toolkit has an exact eligible denominator of **72** at registered pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`. All **72/72** were historically inspected and all **72/72** now have current-standard per-skill provenance + verification companions.
- AWS completion means every eligible entry has decisive current evidence, not that every upstream procedure is approved unchanged. Rejected states remain preserved where authority, secret handling, freshness, or other quality defects require adaptation/reference-only treatment.
- Microsoft Skills has an exact eligible denominator of **189** independently front-mattered skill entry points at registered pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; **28/189** have current-standard provenance + verification companions and **161** remain.
- The direct `.github/plugins/azure-sdk-dotnet/skills/` slice contains **29** packages and is **24/29** current-standard companion-complete.
- Historical source-level evidence remains valid for what it establishes. Other corpora should be reconciled from prior evidence before fresh review.

## AWS curation completion

The sequential reconciliation campaign completed every AWS core and specialized package at the registered pin. Fully reconciled specialized families include analytics, database, EC2, migration/modernization, networking/content-delivery, operations, security/identity, serverless, storage, system-table, and web/mobile.

The final AWS tranche preserved useful negative evidence rather than rubber-stamping completion. Behavioral evidence remains `not-run` unless representative external evaluation actually occurred. Upstream scripts, assets, references, templates and examples remain intact package dependencies rather than `skillz` execution machinery.

## Microsoft Skills curation

Microsoft Skills is the active admitted-source frontier. The denominator is **189** independently front-mattered `SKILL.md` entry points at the exact registered pin; duplicate exposure paths and symlink mirrors are de-duplicated, while ordinary workflow/reference `.md` files remain dependencies of their parent package.

Current progress is **28/189** current-standard companion-complete. Previously reconciled units include the root/cross-language and initial .NET SDK packages for Application Insights web telemetry, skill authoring, architecture, Copilot SDK, Azure Identity, Document Intelligence, persistent agents, Azure OpenAI, Azure AI Projects, Voice Live, Event Grid, Event Hubs and Maps Search.

### .NET management-plane batch

The latest batch reconciles all **15 direct .NET management-plane packages** in one governed tranche:

- `azure-mgmt-apicenter-dotnet` — rejected unchanged, **14/20**.
- `azure-mgmt-apimanagement-dotnet` — rejected unchanged, **12/20**; adds plaintext subscription-key output, key regeneration, literal password example, and a missing required `references/policies.md` dependency.
- `azure-mgmt-applicationinsights-dotnet` — rejected unchanged, **13/20**; adds secret output and recurring synthetic-test mutation.
- `azure-mgmt-arizeaiobservabilityeval-dotnet` — rejected unchanged, **13/20**; Marketplace/commercial and administrator-PII mutation.
- `azure-mgmt-botservice-dotnet` — rejected unchanged, **14/20**; bot/channel publication and Direct Line key rotation.
- `azure-mgmt-fabric-dotnet` — rejected unchanged, **14/20**; billable capacity creation/scaling/state/admin mutation.
- `azure-mgmt-mongodbatlas-dotnet` — rejected unchanged, **13/20**; Marketplace organization/billing and administrator-PII mutation.
- `azure-mgmt-weightsandbiases-dotnet` — rejected unchanged, **13/20**; prerelease Marketplace/SSO/PII/resource workflow plus external experiment-data integration.
- `azure-resource-manager-cosmosdb-dotnet` — rejected unchanged, **13/20**; billable resource mutation, master-key/connection-string output and rotation, failover/network/throughput mutation, and destructive stored-procedure prior art.
- `azure-resource-manager-durabletask-dotnet` — rejected unchanged, **14/20**; scheduler/task-hub/capacity/network/retention lifecycle mutation without affirmative authorization.
- `azure-resource-manager-mysql-dotnet` — rejected unchanged, **12/20**; literal administrator password, permissive Azure-wide firewall example, restore/failover/scale/delete mutations.
- `azure-resource-manager-playwright-dotnet` — rejected unchanged, **14/20**; billable testing workspace creation/deletion, local-auth enablement and external test-service setup.
- `azure-resource-manager-postgresql-dotnet` — rejected unchanged, **12/20**; literal administrator password, permissive firewall example, restore/replica/failover/scale/delete mutations.
- `azure-resource-manager-redis-dotnet` — rejected unchanged, **12/20**; access-key output/rotation, firewall/maintenance/import-export/reboot mutation, and key-bearing data-plane connection construction.
- `azure-resource-manager-sql-dotnet` — rejected unchanged, **11/20**; literal administrator credentials plus broad server/database/pool/network/private-endpoint/backup/import-export/encryption/security/destructive mutations.

Every package retains exact tree/blob identity, exact source revision/date, dependencies, portability, current authority classification, controlled taxonomy tags, decisive static state, and `validation_status: not-run`. The recurring rejection reason is consequential cloud-resource or cost mutation without a mandatory affirmative authorization boundary, but the individual records preserve each package's additional secret, network, data, identity, dependency, destructive-action, or freshness defects. Useful SDK and operational material remains available as adaptation/reference evidence.

The direct `.NET` slice is now **24/29** complete. Five non-management packages remain and should be reconciled as the next coherent `.NET` batch before moving to the next Microsoft language/plugin family.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use issue-first intake. Discovery surfaces, including the connected Creator Technical Resource Catalog, provide leads only. Their scores, labels, creator attributions, popularity, and recommendations do not establish `skillz` provenance or individual quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means the exact material passed structured static semantic review. `validated` additionally requires representative external scenario/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Complete the remaining five direct Microsoft .NET packages, bringing that slice to 29/29.
2. Continue Microsoft Skills in coherent plugin/language batches against the exact 189-entry denominator.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora whose prior review evidence is broader than their current one-file companion shelf.
5. Continue admitted/tracked creator-source curation and denominator reconciliation.
6. Continue governed discovery/source-vetting through issue-first intake and omission recovery.
7. Keep README, this System State, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The current living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
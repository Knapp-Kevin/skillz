# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-01 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 244 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS historical review** | 72 / 72 |
| **AWS current-standard companion complete** | 72 / 72 |
| **AWS current-standard gaps** | 0 |
| **Microsoft Skills current-standard companions** | 72 / 189 |
| **Microsoft Skills current-standard gaps** | 117 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 13 / 40 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical physical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material, not repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party skills** are **43/43 provenance-complete** and have structured semantic review evidence.
- **12 pinned external corpora** provide the broad reference surface.
- **244 exact-version third-party verification companions** are persisted.
- `registry/sources.yaml` contains **19 unique source identities**.
- AWS Agent Toolkit has an exact eligible denominator of **72** at registered pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`. All **72/72** were historically inspected and all **72/72** now have current-standard per-skill provenance + verification companions.
- AWS completion means every eligible entry has decisive current evidence, not that every upstream procedure is approved unchanged. Rejected states remain preserved where authority, secret handling, freshness, or other quality defects require adaptation/reference-only treatment.
- Microsoft Skills has an exact eligible denominator of **189** independently front-mattered skill entry points at registered pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; **72/189** have current-standard provenance + verification companions and **117** remain.
- The direct `.github/plugins/azure-sdk-dotnet/skills/` slice contains **29** packages and is **29/29 current-standard companion-complete**.
- The direct `.github/plugins/azure-sdk-java/skills/` slice contains **26** packages and is **26/26 current-standard companion-complete**.
- The direct `.github/plugins/azure-sdk-python/skills/` slice contains **40** packages and is **13/40 current-standard companion-complete**.
- Historical source-level evidence remains valid for what it establishes. Other corpora should be reconciled from prior evidence before fresh review.

## AWS curation completion

The sequential reconciliation campaign completed every AWS core and specialized package at the registered pin. Fully reconciled specialized families include analytics, database, EC2, migration/modernization, networking/content-delivery, operations, security/identity, serverless, storage, system-table, and web/mobile.

The final AWS tranche preserved useful negative evidence rather than rubber-stamping completion. Behavioral evidence remains `not-run` unless representative external evaluation actually occurred. Upstream scripts, assets, references, templates and examples remain intact package dependencies rather than `skillz` execution machinery.

## Microsoft Skills curation

Microsoft Skills is the active admitted-source frontier. The denominator is **189** independently front-mattered `SKILL.md` entry points at the exact registered pin; duplicate exposure paths and symlink mirrors are de-duplicated, while ordinary workflow/reference `.md` files remain dependencies of their parent package.

Current progress is **72/189** current-standard companion-complete. Previously reconciled units include root/cross-language packages, the complete direct `.NET` SDK plugin slice, the complete direct Java SDK plugin slice, and the first thirteen direct Python packages.

### .NET direct plugin slice — CURRENT-STANDARD COMPLETE

All **29/29 direct `.github/plugins/azure-sdk-dotnet/skills/` packages** have exact-version provenance + verification companions at registered Microsoft pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.

Every direct `.NET` package retains exact tree/blob identity, exact source revision/date, dependencies, portability, current authority classification, controlled taxonomy tags, decisive static state and `validation_status: not-run`. Completion means decisive current evidence for every package, not universal approval.

### Java plugin slice — CURRENT-STANDARD COMPLETE

The direct Java plugin has an exact denominator of **26** packages and is **26/26 current-standard companion-complete** at the registered Microsoft pin. Each reviewed Java package retains its own exact package-tree, `SKILL.md` fingerprint, source-path revision/freshness evidence, dependencies, authority, portability, controlled tags, decisive state, and explicit behavioral-evidence status.

The final three packages were `azure-security-keyvault-keys-java`, `azure-security-keyvault-secrets-java`, and `azure-storage-blob-java`. Their rejected-unchanged states preserve concrete authority, secret/data-handling, destructive-action, credential, and external-service findings rather than converting tranche completion into blanket approval.

Behavioral validation remains `not-run` for the Java tranche unless separate representative external scenario/adversarial evidence is actually recorded.

### Python plugin slice — ACTIVE

The direct Python plugin has an exact denominator of **40** packages and is **13/40 current-standard companion-complete** at the registered pin. Current exact companions run source-order through `azure-appconfiguration-py`. Each package retains differentiated evidence rather than source-level approval.

The latest four-package tranche adds `azure-ai-translation-text-py` (rejected unchanged, 13/20), `azure-ai-vision-imageanalysis-py` (12/20), `azure-ai-voicelive-py` (9/20), and `azure-appconfiguration-py` (12/20), all with behavioral evidence `not-run`. Text Translation and Vision are useful SDK references but lack distinct external-processing, sensitive-data/privacy, and cost authorization boundaries for the text/image content they send to Azure services. Voice Live receives deeper negative treatment because the complete package includes live/recorded audio, transcripts, remote conversation mutation, function/MCP tool calls, synthesized voice/avatar output, and bundled examples without the participant-consent, retention, tool-action, communication, or budget gates required for unchanged use. App Configuration is useful operational prior art but can create/update/delete settings, change feature flags, remove read-only protection, and create snapshots without a separate approved change boundary.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use issue-first intake. Discovery surfaces, including the connected Creator Technical Resource Catalog, provide leads only. Their scores, labels, creator attributions, popularity, and recommendations do not establish `skillz` provenance or individual quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means the exact material passed structured static semantic review. `validated` additionally requires representative external scenario/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered plugin/language batches against the exact **189-entry** denominator; direct Python is the active tranche at **13/40**.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora whose prior review evidence is broader than their current one-file companion shelf.
4. Continue admitted/tracked creator-source curation and denominator reconciliation.
5. Continue governed discovery/source-vetting through issue-first intake and omission recovery.
6. Keep README, this System State, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The current living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
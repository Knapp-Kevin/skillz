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
| **Persisted third-party review companions** | 174 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS historical review** | 72 / 72 |
| **AWS current-standard companion complete** | 72 / 72 |
| **AWS current-standard gaps** | 0 |
| **Microsoft Skills current-standard companions** | 2 / denominator reconciliation in progress |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical physical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material, not repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party skills** are **43/43 provenance-complete** and have structured semantic review evidence.
- **12 pinned external corpora** provide the broad reference surface.
- **174 exact-version third-party verification companions** are persisted.
- `registry/sources.yaml` contains **19 unique source identities**.
- AWS Agent Toolkit has an exact eligible denominator of **72** at registered pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`. All **72/72** were historically inspected and all **72/72** now have current-standard per-skill provenance + verification companions.
- AWS completion means every eligible entry has decisive current evidence, not that every upstream procedure is approved unchanged. Rejected states remain preserved where authority, secret handling, freshness, or other quality defects require adaptation/reference-only treatment.
- Microsoft Skills has **2** current-standard provenance + verification pairs at registered pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; the exact family denominator is still being reconciled, so no completion percentage is claimed.
- Historical source-level evidence remains valid for what it establishes. Other corpora should be reconciled from prior evidence before fresh review.

## AWS curation completion

The sequential reconciliation campaign completed every AWS core and specialized package at the registered pin. Fully reconciled specialized families include analytics, database, EC2, migration/modernization, networking/content-delivery, operations, security/identity, serverless, storage, system-table, and web/mobile.

The final nine gaps were five storage skills, three system-table skills, and `aws-amplify`. Current-standard review preserved useful negative evidence rather than rubber-stamping completion:

- storage packages with useful diagnostics/design guidance were rejected unchanged when mutation/remediation paths lacked mandatory affirmative authorization;
- system-table packages retained strong SQL/query guidance but were rejected unchanged because their configure/grant modes mutate integrations or permissions without a distinct approval gate;
- `aws-amplify` was rejected unchanged because deployment paths create apps, IAM roles/policies, backend resources, domains and release jobs without a distinct infrastructure/cost authorization boundary, and one CI example exposes a GitHub token through a command argument.

All AWS verification companions explicitly distinguish structured static review from behavioral evidence; behavioral validation remains `not-run` unless representative external evidence actually exists.

## Microsoft Skills curation

Two current-standard Microsoft units are now persisted at the registered pin:

- `applicationinsights-web-ts`, package tree `cb03b364b8f9dcb5fc2ee9662758a1f949c23102`, is decisively `rejected` for unchanged adoption because its primary browser setup enables telemetry before first user interaction without making consent or approved data handling a mandatory precondition. The package retains useful privacy, PII-scrubbing, observability and GenAI tracing guidance as adaptation/reference evidence. Behavioral validation is `not-run`.
- `skill-creator`, package tree `44744c928eba10e9e69272a6bab0859b79c480c5`, is `verified` by structured static review at 18/20. It provides strong skill-authoring guidance around concise context, progressive disclosure, current-documentation verification, credential hygiene, lifecycle cleanup and portable package structure. Its bundled Python helpers mutate local skill/package files only when deliberately invoked by an authorized host and remain upstream package tooling, not `skillz` runtime. Behavioral validation is `not-run`.

The Microsoft source's exact eligible denominator remains under reconciliation because the pinned tree mixes canonical packages, language-plugin packages, nested skills and symlinked mirrors. Upstream catalog headline counts are therefore not treated as a proven denominator.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use issue-first intake. Discovery surfaces, including the connected Creator Technical Resource Catalog, provide leads only. Their scores, labels, creator attributions, popularity, and recommendations do not establish `skillz` provenance or individual quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means the exact material passed structured static semantic review. `validated` additionally requires representative external scenario/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Complete Microsoft Skills at its registered pin, establishing the exact eligible denominator before completion claims.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora whose prior review evidence is broader than their current one-file companion shelf.
4. Continue admitted/tracked creator-source curation and denominator reconciliation.
5. Continue governed discovery/source-vetting through issue-first intake and omission recovery.
6. Keep README, this System State, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The current living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.

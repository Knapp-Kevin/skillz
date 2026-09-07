# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **382** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **43/43** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

## Admitted-source curation

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE

- Pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`
- Denominator/current-standard companions: **72/72**; gaps **0**.

### Microsoft Skills — CURRENT-STANDARD COMPLETE

- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Exact eligible denominator/current-standard companions: **186/186**; gaps **0**.
- Direct `.NET` **29/29**; Java **26/26**; Python **40/40**; Rust **9/9**; TypeScript **25/25**.

### Microsoft Azure Skills — ACTIVE FRONTIER

- Pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`
- Exact eligible denominator: **131**.
- Current-standard companions: **24/131**.
- Remaining gaps: **107**.

Reconciled Azure packages and dispositions: `airunway-aks-setup` verified 17/20; `appinsights-instrumentation` rejected 13/20; `azure-ai` rejected 13/20; `azure-aigateway` rejected 13/20; `azure-cloud-migrate` verified 17/20; `azure-compliance` rejected 12/20; `azure-compute` rejected 11/20; `azure-cost` rejected 14/20; `azure-deploy` rejected 15/20; `azure-diagnostics` rejected 13/20; `azure-enterprise-infra-planner` verified 18/20; `azure-hosted-copilot-sdk` rejected 13/20; `azure-kubernetes` rejected 12/20; `azure-kubernetes-automatic-readiness` rejected 15/20; `azure-kusto` rejected 14/20; `azure-messaging` rejected 13/20; `azure-prepare` rejected 16/20; `azure-quotas` rejected 14/20; `azure-rbac` verified 17/20; `azure-reliability` rejected 15/20; `azure-resource-lookup` rejected 14/20; `azure-resource-visualizer` rejected 15/20; `azure-storage` rejected 12/20; `azure-upgrade` rejected 15/20. Behavioral validation remains `not-run` for all twenty-four.

`azure-upgrade` is bound to package tree `ad4f782ddd8eab34eacece4ccb1b66d65a0434d9`, `SKILL.md` blob `6b87a36c181440dd213443b19a2a58d25504a1ba`, and Azure freshness revision `f8c23b595202c899d7cf193ed0ae9b5363fa0296` on 2026-06-01. Exact package identity matches completed Microsoft Skills evidence. Preserve its assessment-first sequencing, target plan/SKU confirmation, explicit confirmation before resource creation and destructive actions, rollback discipline, idempotent/resumable automation requirements, and scenario-specific migration references. Unchanged adoption remains rejected because bundled Functions automation retrieves the live `AzureWebJobsStorage` connection string into shell state and uses it directly for blob operations instead of an identity-based secure credential path; the same prerequisite sequence installs the Resource Graph CLI extension without a distinct action-specific authorization checkpoint.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue Microsoft Azure Skills from **382 persisted reviews / 24 of 131 eligible Azure Skills / 107 gaps**. Recompute the next genuine source-tree gap from the registered pin, checking Azure companions and exact-package overlap with completed Microsoft Skills evidence before fresh review.
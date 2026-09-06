# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in the canonical provenance and verification companions under `registry/`.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **377** persisted exact-version third-party verification companions.
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
- Current-standard companions: **19/131**.
- Remaining gaps: **112**.
- `airunway-aks-setup`: verified **17/20**, behavioral validation `not-run`.
- `appinsights-instrumentation`: rejected unchanged **13/20**, behavioral validation `not-run`.
- `azure-ai`: rejected unchanged **13/20**, behavioral validation `not-run`.
- `azure-aigateway`: rejected unchanged **13/20**, behavioral validation `not-run`.
- `azure-cloud-migrate`: verified **17/20**, behavioral validation `not-run`.
- `azure-compliance`: rejected unchanged **12/20**, behavioral validation `not-run`.
- `azure-compute`: rejected unchanged **11/20**, behavioral validation `not-run`.
- `azure-cost`: rejected unchanged **14/20**, behavioral validation `not-run`.
- `azure-deploy`: rejected unchanged **15/20**, behavioral validation `not-run`.
- `azure-diagnostics`: rejected unchanged **13/20**, behavioral validation `not-run`.
- `azure-enterprise-infra-planner`: verified **18/20**, behavioral validation `not-run`.
- `azure-hosted-copilot-sdk`: rejected unchanged **13/20**, behavioral validation `not-run`.
- `azure-kubernetes`: rejected unchanged **12/20**, behavioral validation `not-run`.
- `azure-kubernetes-automatic-readiness`: rejected unchanged **15/20**, behavioral validation `not-run`.
- `azure-kusto`: rejected unchanged **14/20**, behavioral validation `not-run`.
- `azure-messaging`: rejected unchanged **13/20**, behavioral validation `not-run`.
- `azure-prepare`: rejected unchanged **16/20**, behavioral validation `not-run`.
- `azure-quotas`: rejected unchanged **14/20**, behavioral validation `not-run`.
- `azure-rbac`: verified **17/20**, behavioral validation `not-run`; package tree `b52d696609b18a5dc2bae21e368812fe7b020ec5`, `SKILL.md` blob `02ac75d2ba22b4d7aa1e74469b01575281f05ddc`, Azure-source freshness revision `317a8e7b879c0ed6a1890378eafd939bdd9bc749` on 2026-04-22.

`azure-rbac` exactly matches the completed Microsoft Skills package, so compatible complete-package evidence was reconciled rather than repeated. Preserve least-privilege-first role selection, custom-role fallback, explicit role-assignment capability guidance, and the preference for User Access Administrator over Owner when assignment is the only requirement. The package is generate-only and does not execute role assignments or mutate Azure state, so the action-specific mutation authorization hard fail does not apply to unchanged use; execution of generated artifacts remains a separate host-agent action requiring scoped authorization.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, Cole Medin, David Ondrej, Nate B. Jones, Andrej Karpathy-derived methodology, Sean Kochel, Chase AI+, and bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue Microsoft Azure Skills from **377 persisted reviews / 19 of 131 eligible Azure Skills / 112 gaps**. Recompute the next genuine source-tree gap from the registered pin, checking Azure companions and exact-package overlap with completed Microsoft Skills evidence before fresh review.
# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in the canonical provenance and verification companions under `registry/`.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **376** persisted exact-version third-party verification companions.
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
- Current-standard companions: **18/131**.
- Remaining gaps: **113**.
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
- `azure-quotas`: rejected unchanged **14/20**, behavioral validation `not-run`; package tree `8a628e265ecb05a8f78a9a7e4e4772fb82d78c40`, `SKILL.md` blob `cbd67b6c336362ee343390e713b91b5662841038`, Azure-source freshness revision `a81025ed0ac25e09c5805ada5295d0304e0ebbf7` on 2026-05-27.

`azure-quotas` exactly matches the completed Microsoft Skills package, so compatible complete-package evidence was reconciled rather than repeated. Preserve quota-name discovery, CLI-first read workflows, usage/capacity calculation, regional comparison, unsupported-provider fallback, and the `No Limit` warning. Unchanged adoption fails authority governance because subscription-scoped quota updates and provider registration lack mandatory action-specific authorization immediately before mutation, and the package also mandates local Azure CLI quota-extension installation without scoped authorization.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, Cole Medin, David Ondrej, Nate B. Jones, Andrej Karpathy-derived methodology, Sean Kochel, Chase AI+, and bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue Microsoft Azure Skills from **376 persisted reviews / 18 of 131 eligible Azure Skills / 113 gaps**. Recompute the next genuine source-tree gap from the registered pin, checking Azure companions and exact-package overlap with completed Microsoft Skills evidence before fresh review.
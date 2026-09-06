# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in the canonical provenance and verification companions under `registry/`.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **371** persisted exact-version third-party verification companions.
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
- Current-standard companions: **13/131**.
- Remaining gaps: **118**.
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
- `azure-kubernetes`: rejected unchanged **12/20**, behavioral validation `not-run`; package tree `bab7f5eab9e8e1c311ef1fc29b419963903fbe09`, `SKILL.md` blob `3c5a448a679dafed5e0e747d28bd95cead4e8dec`, Azure-source freshness revision `d3440b8a4f138585a512ecd4e0c54ede13ab1cc2` on 2026-05-29.

`azure-kubernetes` exactly matches the completed Microsoft Skills package, so compatible complete-package evidence was reconciled rather than repeated. Preserve Day-0/Day-1 framing, AKS Automatic defaults, networking/security/reliability guidance, secret non-disclosure, and scenario deep dives. Unchanged adoption fails the authority hard rule because bundled CLI guidance performs consequential cluster creation/configuration without action-specific approval immediately before mutation. The nested front-mattered `azure-kubernetes-automatic-readiness` is independently eligible and remains a separate denominator unit.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, Cole Medin, David Ondrej, Nate B. Jones, Andrej Karpathy-derived methodology, Sean Kochel, Chase AI+, and bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue Microsoft Azure Skills from **371 persisted reviews / 13 of 131 eligible Azure Skills / 118 gaps**. The next genuine source-tree unit is the nested first-class `azure-kubernetes-automatic-readiness`; check its Azure-source identity against completed Microsoft Skills evidence before fresh review.
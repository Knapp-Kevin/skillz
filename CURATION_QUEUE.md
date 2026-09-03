# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in the provenance and verification companions; this ledger records current denominators, frontier state, lifecycle debt, and discovery decisions without duplicating the entire evidence shelf.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **309** persisted exact-version third-party verification companions.
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
- Denominator: **72**
- Current-standard companion completeness: **72/72**
- Gaps: **0**

### Microsoft Skills — ACTIVE FRONTIER

- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Exact eligible denominator: **189** independently front-mattered skill entry points.
- Current-standard companions: **137/189**.
- Remaining gaps: **52**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **25/25** complete.

The TypeScript denominator is tree-derived. The registered-pin tree contains 25 independently first-class packages even though the upstream plugin README says 24 and omits `applicationinsights-web-ts`. Twenty-two packages are rejected unchanged under current authority/privacy/secret/sensitive-data/external-state hard gates; three bounded local implementation packages are verified: `frontend-ui-dark-ts` 15/20, `react-flow-node-ts` 15/20, and `zustand-store-ts` 16/20. All retain explicit behavioral-validation state in their companions.

Current non-direct Microsoft plugin frontier:

- `airunway-aks-setup` — **rejected unchanged, 15/20**. Strong setup and secret-entry safeguards; rollback lacks fresh destructive-action authorization.
- `appinsights-instrumentation` — **rejected unchanged, 12/20**. Useful App Insights/OpenTelemetry prior art; infrastructure/configuration mutation, telemetry disclosure, deployment, cost, and shared-key custody lack mandatory authorization.
- `azure-ai` — **rejected unchanged, 10/20**. Useful Azure AI router/reference; persistent search mutation and potentially sensitive external data processing lack mandatory data-owner, disclosure/model-transfer, mutation, production, retention, cost, and credential-custody authority.
- `azure-aigateway` — **rejected unchanged, 8/20**. Useful APIM AI-gateway prior art; identity/RBAC/backend/API/security/routing mutation, agent exposure, live endpoint calls, metrics, and subscription-key listing lack mandatory target, identity/access, security-control, production, downstream-effect, disclosure, cost, and credential-custody authority.
- `azure-cloud-migrate` — **rejected unchanged, 9/20**. Exact package tree `dd0d5a31e87576d5b46899b19aa3eedb24d412f4`, `SKILL.md` blob `b1634cf629d9358eb70a95c089b309c304f9c42c`, freshness revision `e12b7d24dab47df1d935783b31b196fdf43ad56b` from 2026-05-07. Preserve assessment-before-mutation, source preservation, scenario routing, service mapping, runtime modernization, staged conversion, progress reporting, service-discovery auditing, destructive-action confirmation, and explicit local-test-versus-Azure-deploy choice. Unchanged adoption fails because bundled deployment guidance creates Azure resources, identities/RBAC, imports images, exposes external ingress, migrates Kubernetes secrets into Key Vault, retrieves a Log Analytics primary shared key, and configures production-like scaling without mandatory per-resource target/environment, identity/access, security-control, secret/data-owner, credential-custody, network-exposure, production, retention/recovery, or cost authorization. Behavioral validation is `not-run`.

The next Microsoft Skills unit must be established from the registered-pin tree after `azure-cloud-migrate`. Do not revive stale source-order assumptions from historical prompts.

### Microsoft Azure Skills — QUEUED AFTER MICROSOFT SKILLS

Use the registered source identity and pin in `registry/sources.yaml`. Do not begin this family merely because one Microsoft Skills lane is inconvenient; finish the active admitted family unless blocked or concurrently owned.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure.

Current governed surfaces and candidates include:

- Creator Technical Resource Catalog: discovery intelligence only; independently resolve canonical upstream identity and terms before promotion.
- Hugging Face Skills: source-vetting accepted for selective deeper intake; no blanket trust.
- GitHub Awesome Copilot: registered dynamic-discovery surface, never a trusted wholesale corpus.
- Agent Skills Specification: registered normative reference, not an installable-skill denominator.
- Cole Medin and David Ondrej: tracked creator corpora requiring selective exact-version curation and denominator/evidence reconciliation.
- Nate B. Jones: canonical first-party source and redistribution terms still need evidence.
- Andrej Karpathy-derived methodology: methodology/provenance candidate, not presumed Karpathy-authored skill corpus.
- Sean Kochel: curator/methodology surface; trace useful recommendations to original authors.
- Chase AI+: restricted/reference-only unless terms establish redistribution authority.
- Open candidate issues #63 and #73 remain bounded workspaces and must terminate in decisive outcomes when sufficient evidence exists.

## Lifecycle hygiene

At each run:

1. inspect every open PR and issue before new curation;
2. merge a green, current, authorized, still-correct PR in the same run;
3. close evidence-complete, duplicate, or fully superseded bounded issues after preserving unique evidence;
4. state concrete blockers for genuinely blocked work;
5. reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes;
6. preserve the passive architecture and never add repository-owned runtime, scripts, tests, CI, schedulers, monitors, crawlers, installers, synchronizers, preflight, generators, or background services.

## Historical authority boundary

Wayfinder #35 remains the canonical destination/scope evidence, but its stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution. Do not revive #41/#42-era structure work unless current governance explicitly re-establishes it.

## Next action

After `azure-cloud-migrate` is merged and public accounting is verified at **309 reviews / Microsoft Skills 137/189 / 52 gaps**, establish the first genuine remaining Microsoft Skills gap from the registered-pin tree and continue source-by-source.
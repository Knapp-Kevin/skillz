# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in provenance and verification companions; this ledger records current denominators, frontier state, lifecycle debt, and discovery decisions.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **330** persisted exact-version third-party verification companions.
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
- Current-standard companions: **158/189**.
- Remaining gaps: **31**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **25/25** complete.

Current non-direct Microsoft plugin frontier includes `airunway-aks-setup`, `appinsights-instrumentation`, `azure-ai`, `azure-aigateway`, `azure-cloud-migrate`, `azure-compliance`, `azure-compute`, `azure-cost`, `azure-deploy`, `azure-diagnostics`, `azure-enterprise-infra-planner`, `azure-hosted-copilot-sdk`, `azure-kubernetes`, `azure-kubernetes-automatic-readiness`, `azure-kusto`, `azure-messaging`, `azure-prepare`, `azure-quotas`, `azure-rbac`, `azure-reliability`, `azure-resource-lookup`, `azure-resource-visualizer`, `azure-storage`, `azure-upgrade`, `azure-validate`, and `entra-agent-id`.

- `azure-enterprise-infra-planner` — **verified, 18/20**.
- `azure-rbac` — **verified, 17/20**.
- `azure-validate` — **rejected unchanged, 16/20**.
- `entra-agent-id` — **rejected unchanged, 13/20**. Exact package tree `405ed207c079150581ef0540a0b4a0a1f176fc9e`, `SKILL.md` blob `5aaf917945171757112bdb341fb593b4517542cd`, freshness revision `5bc90f7cc3012cb8e9a6f14b5ccb5a3edcd1cc67` from 2026-03-24. Preserve distinct per-agent identities/audit trails, typed Graph endpoints, BlueprintPrincipal prerequisite, workload-identity preference, per-agent permission scoping, cross-tenant token-exchange mechanics, localhost-only sidecar containment, and troubleshooting evidence. Unchanged adoption is rejected because the workflow installs host dependencies, creates Entra identity objects/service principals, grants application and tenant-wide delegated permissions, and invokes admin consent without mandatory action-specific authorization checkpoints immediately before those identity/access mutations. Behavioral validation is `not-run`.

The next Microsoft Skills unit must be established from the registered-pin tree after `entra-agent-id`.

### Microsoft Azure Skills — QUEUED AFTER MICROSOFT SKILLS

Use the registered source identity and pin in `registry/sources.yaml`. Do not begin this family merely because one Microsoft Skills lane is inconvenient; finish the active admitted family unless blocked or concurrently owned.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, Cole Medin, David Ondrej, Nate B. Jones, Andrej Karpathy-derived methodology, Sean Kochel, Chase AI+, and bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue before new curation; merge a green, current, authorized, still-correct PR in the same run; close evidence-complete, duplicate, or fully superseded bounded issues after preserving unique evidence; state concrete blockers for genuinely blocked work; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; and preserve the passive architecture without repository-owned execution machinery.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but its stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution. Do not revive #41/#42-era structure work unless current governance explicitly re-establishes it.

## Next action

After `entra-agent-id` is merged and public accounting is verified at **330 reviews / Microsoft Skills 158/189 / 31 gaps**, establish the first genuine remaining Microsoft Skills gap from the registered-pin tree and continue source-by-source.
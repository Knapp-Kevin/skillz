# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in the provenance and verification companions; this ledger records current denominators, frontier state, lifecycle debt, and discovery decisions without duplicating the entire evidence shelf.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **327** persisted exact-version third-party verification companions.
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
- Current-standard companions: **155/189**.
- Remaining gaps: **34**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **25/25** complete.

Current non-direct Microsoft plugin frontier:

- `airunway-aks-setup` — **rejected unchanged, 15/20**.
- `appinsights-instrumentation` — **rejected unchanged, 12/20**.
- `azure-ai` — **rejected unchanged, 10/20**.
- `azure-aigateway` — **rejected unchanged, 8/20**.
- `azure-cloud-migrate` — **rejected unchanged, 9/20**.
- `azure-compliance` — **rejected unchanged, 12/20**.
- `azure-compute` — **rejected unchanged, 11/20**.
- `azure-cost` — **rejected unchanged, 14/20**.
- `azure-deploy` — **rejected unchanged, 15/20**.
- `azure-diagnostics` — **rejected unchanged, 13/20**.
- `azure-enterprise-infra-planner` — **verified, 18/20**.
- `azure-hosted-copilot-sdk` — **rejected unchanged, 13/20**.
- `azure-kubernetes` — **rejected unchanged, 12/20**.
- `azure-kubernetes-automatic-readiness` — **rejected unchanged, 15/20**.
- `azure-kusto` — **rejected unchanged, 14/20**.
- `azure-messaging` — **rejected unchanged, 13/20**.
- `azure-prepare` — **rejected unchanged, 16/20**.
- `azure-quotas` — **rejected unchanged, 14/20**.
- `azure-rbac` — **verified, 17/20**.
- `azure-reliability` — **rejected unchanged, 15/20**.
- `azure-resource-lookup` — **rejected unchanged, 14/20**.
- `azure-resource-visualizer` — **rejected unchanged, 15/20**.
- `azure-storage` — **rejected unchanged, 12/20**. Exact package tree `58ffdd0c0f466a983a0064239d481fb08e58b7c8`, `SKILL.md` blob `21bdc643b63e040a9b1efe7422474cfb393ddc85`, freshness revision `10cfecf15420a913fd7e8842cd4f953fbd9ef9a4` from 2026-05-01. Preserve its storage-service selection, access-tier/redundancy summaries, managed-identity production guidance, least-privilege RBAC advice, and multi-language SDK references. Unchanged adoption is rejected because the complete package directly instructs blob writes/overwrites, package installation and host setup, credential rotation, and Defender enablement without action-specific authorization immediately before those mutations; blob get/download paths also lack explicit sensitive-data disclosure/minimization controls. Behavioral validation is `not-run`.

The next Microsoft Skills unit must be established from the registered-pin tree after `azure-storage`.

### Microsoft Azure Skills — QUEUED AFTER MICROSOFT SKILLS

Use the registered source identity and pin in `registry/sources.yaml`. Do not begin this family merely because one Microsoft Skills lane is inconvenient; finish the active admitted family unless blocked or concurrently owned.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure.

Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, Cole Medin, David Ondrej, Nate B. Jones, Andrej Karpathy-derived methodology, Sean Kochel, Chase AI+, and the bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

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

After `azure-storage` is merged and public accounting is verified at **327 reviews / Microsoft Skills 155/189 / 34 gaps**, establish the first genuine remaining Microsoft Skills gap from the registered-pin tree and continue source-by-source.
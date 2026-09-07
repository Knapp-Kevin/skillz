# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **383** persisted exact-version third-party verification companions.
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
- Current-standard companions: **25/131**.
- Remaining gaps: **106**.

The twenty-five reconciled Azure packages are the prior twenty-four through `azure-upgrade` plus `azure-validate` rejected unchanged **16/20**. Behavioral validation remains `not-run` for all twenty-five.

`azure-validate` is bound to package tree `f0eac59b12bba969fdec0e29b7558e441f7be14f`, `SKILL.md` blob `e852edd0519414ed61ee39d786b50bd8a8b0d389`, and Azure freshness revision `317a8e7b879c0ed6a1890378eafd939bdd9bc749` on 2026-04-22. Exact package identity matches completed Microsoft Skills evidence. Preserve its prepare-before-validate gate, evidence-backed validation proof, static least-privilege RBAC review, subscription/location confirmation, preview/what-if checks, and explicit blockers. Unchanged adoption remains rejected because AZCLI/AZD validation recipes can install persistent host tooling and generate a missing `package-lock.json` without a distinct action-specific authorization checkpoint, while the broader workflow directs the agent to fix validation/build failures before proceeding.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue Microsoft Azure Skills from **383 persisted reviews / 25 of 131 eligible Azure Skills / 106 gaps**. Recompute the next genuine source-tree gap from the registered pin, checking Azure companions and exact-package overlap with completed Microsoft Skills evidence before fresh review.
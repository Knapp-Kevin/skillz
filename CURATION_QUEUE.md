# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **409** persisted exact-version third-party verification companions.
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

### Microsoft Azure Skills — CURRENT-STANDARD COMPLETE

- Pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`
- Exact eligible denominator/current-standard companions: **34/34**; gaps **0**.

The exact denominator is 28 canonical plugin roots, one nested Kubernetes automatic-readiness package, and five nested Microsoft Foundry packages beyond the Foundry root. Ordinary workflow, procedure, reference, example, SDK, and other Markdown is package evidence rather than an independent skill. The latest package-level Azure reconciliation remains `python-appservice-deploy`, rejected unchanged **12/20**, behavioral validation `not-run`.

### Cole Medin Skills — ACTIVE FRONTIER

- Pin: `fb2e876f057c5356d6603ba0c52d6b4418d893ba`.
- Exact eligible denominator: **33** first-class `.claude/skills/*/SKILL.md` packages.
- Current-standard companions: **20/33**.
- Remaining gaps: **13**.

Existing companion pairs are `ablate-ai-layer`, `rules-check-drift`, `second-brain-audit`, `agent-browser`, `ast-grep`, `build-dark-factory`, `hooks-create`, `opportunity-scan`, `piv-commit`, `piv-create-pr`, `piv-fix-review-findings`, `piv-implement-issue`, `piv-implement`, `piv-investigate-issue`, `piv-plan-implementation`, `piv-review-changes`, `piv-review-pr`, `piv-run-full-loop`, `piv-slice-epic`, and `piv-validate`.

The latest unit, `piv-validate`, is bound to package tree `618bac9e2cab87364b1b92c5fee8e7d8d74fdbc1`, `SKILL.md` blob `b68422586889a158bc332b79007d3eeb37d3eb51`, and skill-path freshness revision `356511604c75008271ec34933864ccba09100202` dated 2026-08-04. It is rejected unchanged **15/20** with behavioral validation `not-run`. Retain its project-specific validation matrix, working-directory discipline, cross-platform checks, continue-after-failure evidence collection, and report-only separation. Unchanged use fails the authority hard rule because it executes commands sourced from repository-controlled files and may start a live application smoke test without mandatory action-specific authorization immediately before consequential execution. Repository-provided commands also lack an explicit hostile-instruction boundary, and failing output lacks a mandatory secret/PII redaction check before reproduction.

## Governed discovery / source-vetting

Discovery proceeds in parallel but cannot displace admitted-source closure. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded open candidate issues #63 and #73. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue Cole Medin Skills from the exact 33-skill pin, checking companion absence, package identity, freshness, license, authority, dependencies, and recoverable prior review evidence before every unit. Keep governed discovery/source-vetting active in parallel without letting it displace admitted-source closure.

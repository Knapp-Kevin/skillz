# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **44** first-party user-facing skills, **44/44** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **431** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **44/44** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

The latest first-party admission is `session-continuity`, created from the bounded gap evidence in issues #71/#73. It is a substrate-agnostic procedure, not a memory implementation: scoped recall is evidence-only, prior memory grants no current action authority, durable capture requires current or standing authorization, secrets are excluded, and sensitive durable capture is necessity- and authority-gated. Static review: **19/20 verified**; behavioral validation: `not-run`.

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

### Cole Medin Skills — CURRENT-STANDARD COMPLETE

- Pin: `fb2e876f057c5356d6603ba0c52d6b4418d893ba`.
- Exact eligible denominator: **33** first-class `.claude/skills/*/SKILL.md` packages.
- Current-standard companions: **33/33**.
- Remaining gaps: **0**.

The final unit, `worktree-merge`, is bound to package tree `150cb167cb6c0bd703e3ba5b05330aa7f9db9861`, `SKILL.md` blob `9912484e1f99ce5ae7f5fd25f88a3d60f3e61c2b`, and skill-path freshness revision `1c46cd18bc6100d358082c06357d649f7a4cf8c6` dated 2026-08-09. It is rejected unchanged **15/20** with behavioral validation `not-run`. Retain its repository-detected validation model, disposable integration branch, per-branch test localization, conflict stop, full-suite gate, rollback guidance, and explicit cleanup choice. Unchanged use remains rejected because it creates and merges branches, including the final merge into the original branch, without mandatory action-specific authorization immediately before that consequential mutation, and because repository-controlled CI workflows, Makefiles, manifests, and discovered validation commands are treated as executable guidance without an explicit hostile-instruction boundary.

### Matt Pocock Skills — CURRENT-STANDARD COMPLETE

- Pin: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`.
- Exact eligible denominator: **29** first-class packages after excluding `deprecated` and `in-progress` per source policy.
- Provenance companions: **29/29**.
- Verification companions: **29/29**.
- Current-standard gaps: **0**.
- Canonical-path integrity: no live companion retains obsolete `vendor/mattpocock-skills/...`; all live paths resolve under `skills/sources/mattpocock-skills/`.

### Cloudflare Skills — CURRENT-STANDARD COMPLETE

- Pin: `f96bff754e428838818017f75817f0f9428acd48`.
- Exact eligible denominator: **13** first-class packages.
- Provenance companions: **13/13**.
- Verification companions: **13/13**.
- Decisive states: **11 verified / 2 rejected unchanged**.
- Current-standard gaps: **0**.
- Canonical-path integrity: all live companion `local_path` values resolve under `skills/sources/cloudflare-skills/`; obsolete `vendor/cloudflare-skills/...` paths are eliminated from the companion family.

The two rejected unchanged packages remain `web-perf` and `wrangler`. `web-perf` retains useful evidence-driven performance-audit methods but hard-fails unchanged use because its required Chrome DevTools MCP path lacks an adequate privacy/telemetry consent boundary. `wrangler` remains useful reference material but hard-fails unchanged use because install/deploy/delete/migration/resource-mutation procedures lack a governing action-specific authorization boundary. Behavioral validation remains `not-run` across the 13-package family.

### Addy Osmani Agent Skills — RECONCILIATION ACTIVE

- Pin: `f63ec56a3cc936408d792956ae583c3c96a825bd`.
- Exact eligible denominator: **24** first-class `skills/*/SKILL.md` packages.
- Historical issue #27: **24/24** with decisive exact-version static states.
- Current-standard provenance companions: **19/24**.
- Current-standard verification companions: **19/24**.
- Current-standard gaps: **5**.

The latest reconciled unit is `performance-optimization`. Its exact historical evidence was recovered from superseded PR #42 rather than re-reviewed and matches exact `SKILL.md` blob `6e95266942288ca0330eb2a8a716625958df7c57` at the registered source snapshot. The decisive state remains **verified 19/20**, behavioral validation `not-run`. Preserve its measure-identify-fix-verify-guard workflow, same-condition remeasurement, variance awareness, keep/revert discipline, regression guards, query-plan and connection-pool diagnosis, and cache correctness/stampede safeguards. Portability remains medium because stack-specific examples and time-sensitive Web Vitals thresholds require contextual refresh. Recover compatible historical evidence for the remaining 5 before fresh review where possible.

## Governed discovery / source-vetting

Discovery proceeds in parallel without displacing current-standard source maintenance. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded candidate work surfaced through current issues. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

With AWS Agent Toolkit, Microsoft Skills, Microsoft Azure Skills, Cole Medin Skills, Matt Pocock Skills, and Cloudflare Skills current-standard complete at their exact registered pins, continue Addy Osmani Agent Skills from **19/24** current-standard companions by recovering compatible historical evidence for the remaining 5. Anthropic Knowledge Work Plugins remains independently blocked on recoverable per-package historical mapping despite compatible 74/74 aggregate evidence. In parallel, continue bounded discovery/source-vetting and omission detection.

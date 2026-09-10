# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **44** first-party user-facing skills, **44/44** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **436** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **44/44** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

The latest first-party admission is `session-continuity`, created from the bounded gap evidence in issues #71/#73. It is a substrate-agnostic procedure, not a memory implementation: scoped recall is evidence-only, prior memory grants no current action authority, durable capture requires current or standing authorization, secrets are excluded, and sensitive durable capture is necessity- and authority-gated. Static review: **19/20 verified**; behavioral validation: `not-run`.

## Admitted-source curation

### Anthropic Skills — CURRENT-STANDARD COMPLETE

- Pin: `9d2f1ae187231d8199c64b5b762e1bdf2244733d`.
- Exact eligible denominator: **17** first-class `skills/*/SKILL.md` packages.
- Provenance companions: **17/17**.
- Verification companions: **17/17**.
- Decisive historical states: **10 verified / 7 rejected unchanged**.
- Current-standard gaps: **0**.
- Canonical-path integrity: live companion paths no longer reference obsolete top-level `vendor/anthropic-skills/...`.

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE

- Pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Denominator/current-standard companions: **72/72**; gaps **0**.

### Microsoft Skills — CURRENT-STANDARD COMPLETE

- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Exact eligible denominator/current-standard companions: **186/186**; gaps **0**.
- Direct `.NET` **29/29**; Java **26/26**; Python **40/40**; Rust **9/9**; TypeScript **25/25**.

### Microsoft Azure Skills — CURRENT-STANDARD COMPLETE

- Pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Exact eligible denominator/current-standard companions: **34/34**; gaps **0**.

The exact denominator is 28 canonical plugin roots, one nested Kubernetes automatic-readiness package, and five nested Microsoft Foundry packages beyond the Foundry root. Ordinary workflow, procedure, reference, example, SDK, and other Markdown is package evidence rather than an independent skill.

### Cole Medin Skills — CURRENT-STANDARD COMPLETE

- Pin: `fb2e876f057c5356d6603ba0c52d6b4418d893ba`.
- Exact eligible denominator: **33** first-class `.claude/skills/*/SKILL.md` packages.
- Current-standard companions: **33/33**; gaps **0**.

The final unit, `worktree-merge`, remains rejected unchanged **15/20** with behavioral validation `not-run`; its branch mutation and repository-controlled executable-guidance assumptions remain bounded adaptation evidence rather than unchanged-use authority.

### Matt Pocock Skills — CURRENT-STANDARD COMPLETE

- Pin: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`.
- Exact eligible denominator: **29** after excluding `deprecated` and `in-progress` per source policy.
- Provenance/verification companions: **29/29**; gaps **0**.

### Cloudflare Skills — CURRENT-STANDARD COMPLETE

- Pin: `f96bff754e428838818017f75817f0f9428acd48`.
- Exact eligible denominator: **13**.
- Provenance/verification companions: **13/13**.
- Decisive states: **11 verified / 2 rejected unchanged**; gaps **0**.

`web-perf` remains rejected for its privacy/telemetry boundary and `wrangler` for missing action-specific authority around consequential mutations. Behavioral validation remains `not-run`.

### Addy Osmani Agent Skills — CURRENT-STANDARD COMPLETE

- Pin: `f63ec56a3cc936408d792956ae583c3c96a825bd`.
- Exact eligible denominator: **24** first-class `skills/*/SKILL.md` packages.
- Current-standard provenance/verification companions: **24/24**; gaps **0**.

Historical exact evidence from superseded PR #42 was recovered only where fingerprints matched the registered pin. Behavioral validation was not inferred from upstream eval material.

### Vercel Agent Skills — CURRENT-STANDARD COMPLETE

- Pin: `f8a72b9603728bb92a217a879b7e62e43ad76c81`.
- Exact eligible denominator: **9** first-class `skills/*/SKILL.md` packages.
- Current-standard provenance companions: **9/9**.
- Current-standard verification companions: **9/9**.
- Decisive states: **6 verified / 3 rejected unchanged**.
- Current-standard gaps: **0**.
- Canonical-path integrity: all 18 live companion records now resolve under `skills/sources/vercel-agent-skills/`; obsolete `vendor/vercel-agent-skills/...` companion paths are eliminated.

The three rejected unchanged records remain useful negative/adaptation evidence. `vercel-cli-with-tokens` hard-fails secret discipline because it exposes or solicits credential values and also contains consequential paid/destructive operations. `web-design-guidelines` and `writing-guidelines` hard-fail unchanged use because their effective instruction payloads are fetched from mutable unpinned `main`-branch documents outside the recorded exact-version fingerprints. Behavioral validation remains `not-run` for all nine.

## Governed discovery / source-vetting

Discovery proceeds in parallel without displacing current-standard source maintenance. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded candidate work surfaced through current issues. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

With Anthropic Skills, AWS Agent Toolkit, Microsoft Skills, Microsoft Azure Skills, Cole Medin Skills, Matt Pocock Skills, Cloudflare Skills, Addy Osmani Agent Skills, and Vercel Agent Skills current-standard complete at their exact registered pins, continue issue #66 by testing the Anthropic Knowledge Work Plugins per-package historical-mapping blocker against current evidence. If it remains genuinely blocked, select the next admitted family with a truthful companion/provenance gap. Continue bounded discovery/source-vetting and omission detection in parallel.

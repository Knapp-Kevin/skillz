# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in the canonical provenance and verification companions under `registry/`; this ledger records current denominators, frontier state, lifecycle debt, and discovery decisions without duplicating the entire evidence shelf.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **351** persisted exact-version third-party verification companions.
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
- Current-standard companions: **179/189**.
- Remaining gaps: **10**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **25/25** complete.

Contract repair on 2026-09-05 reconciled the `kql` through `wiki-architect` review wave against the current mandatory YAML companion paths. Ten genuinely missing YAML pairs were restored. `skill-creator` already had a canonical pair and therefore is not counted a second time; its existing pair was refreshed to the current 15/20 rejected authority disposition. Auxiliary Markdown review records remain evidence but do not define companion counts.

The `deep-wiki` frontier is complete. The active non-direct family is `microsoft-365-agents-toolkit`. Latest closure: `install-atk` is **rejected unchanged, 13/20** at package tree `c7be3fb169d02f94492a3d1ca203bed5adacc9ba` and `SKILL.md` blob `44afbcbbd76801317776563a96d034574716e949`; freshness is bound to revision `a43d2c6a69fac2298ac0f301419931b39d996c6b` from 2026-06-15. Preserve explicit install/update triggers, exact package and extension identifiers, CLI-versus-extension routing, dependency failure guidance, telemetry tagging, and result reporting. Unchanged adoption fails the authority hard rule because `npx -y` automatically downloads, executes, and caches the latest CLI package and ambiguous ATK intent defaults to installing the VS Code extension without a distinct action-specific authorization checkpoint immediately before those local-environment mutations. Latest-version execution is also unpinned. Behavioral validation is `not-run`.

Continue through `microsoft-365-agents-toolkit` in exact registered-pin source order. `m365-agent-evaluator` follows `install-atk`; check canonical registry companions and repository history before treating it as a genuine gap.

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

After public accounting is verified at **351 reviews / Microsoft Skills 179/189 / 10 gaps**, establish whether `m365-agent-evaluator` is the next genuine companion gap from the exact registered-pin source tree and continue source-by-source.
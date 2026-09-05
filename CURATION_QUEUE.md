# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in the provenance and verification companions; this ledger records current denominators, frontier state, lifecycle debt, and discovery decisions without duplicating the entire evidence shelf.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **340** persisted exact-version third-party verification companions.
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
- Current-standard companions: **168/189**.
- Remaining gaps: **21**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **25/25** complete.

Current non-direct Microsoft frontier has advanced through `python-appservice-deploy`. It is **rejected unchanged, 12/20** at package tree `6e11dad529e50b7fbc37191de665788d0427ccad` and `SKILL.md` blob `ac25db692762945d0e3e9ed2016dcfa29fbfa610`; freshness is bound to sync revision `24a3a7bd6caa8e87b3a91e93c95959e3cfdb906d` from 2026-06-15. Preserve its framework detection, deterministic naming, shell-safety guidance, idempotent create pattern, transient-error classification, `.env` packaging exclusion, and deployment-vs-build-state distinction. Unchanged adoption is rejected because the workflow creates Azure resources, defaults to a paid P0v3 plan, mutates application configuration, and deploys code while explicitly instructing the agent not to ask for confirmation after presenting inferred defaults. Behavioral validation is `not-run`.

The next Microsoft Skills unit must be established from the exact registered-pin tree after `python-appservice-deploy`. `foundry-projects-resources` and related newer Foundry packages observed upstream are absent from the registered revision and therefore do not count toward this denominator.

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

After `python-appservice-deploy` is merged and public accounting is verified at **340 reviews / Microsoft Skills 168/189 / 21 gaps**, establish the first genuine remaining Microsoft Skills gap from the exact registered-pin tree and continue source-by-source.
# Governance Index

**Last reviewed:** 2026-08-30

This file maps the current control surfaces for `skillz`.

`skillz` is a **passive skill knowledge resource**. The external host agent is the active system. The repository owns no runtime, scripts, tests, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service.

During normal `DIRECT_LIBRARY`, `FIRST_VISIT`, and `RETURNING_USER` use, the repository is also **read-only reference material**. Skills created, adapted, composed, refined, packaged, or installed for a user belong in the user's active host/environment or in a portable handoff. They do not belong in `skillz`. Only an explicit `REPOSITORY_MAINTENANCE` request may authorize repository mutation.

Historical Qor, alpha, CI, preflight, runtime, generator, evaluator, and test-era artifacts are historical evidence only unless a current Tier 1 document explicitly re-establishes a static documentation requirement from them. They never override the passive-repository invariant.

## Tier 1: current repository identity and state

These documents define the current architecture and must agree.

| Artifact | Path | Freshness contract |
|---|---|---|
| Human/AI front door | `README.md` | passive-resource identity, current corpus shape, current user-flow guidance |
| Agent contract | `AGENTS.md` | routing, privacy, authority, mutation and artifact-destination boundaries |
| Agent entry point | `AGENT_START_HERE.md` | current host-agent routing without repository execution or write-back assumptions |
| Bootstrap/refinement guide | `BOOTSTRAP.md` | passive first-visit and returning-user procedure; generated skills target the user's host/handoff |
| System state | `docs/SYSTEM_STATE.md` | current architecture, inventory boundaries, curation status, known drift |
| Governance index | `docs/GOVERNANCE_INDEX.md` | current authoritative control-surface map |
| Curation queue | `CURATION_QUEUE.md` | living admitted-source and discovery/source-vetting work ledger |

The canonical physical boundary is:

- user-facing first-party skill material under `skills/` is maintained repository corpus/reference material, not a normal user-output destination;
- intact admitted pinned third-party corpora under `skills/sources/<source-id>/`;
- passive repository-maintenance instructions under `engine/skills/`, excluded from user-facing corpus counts.

The live tree now reflects this boundary. Legacy top-level `vendor/...` source paths have been reconciled into `skills/sources/<source-id>/`; historical references may remain only where clearly non-authoritative.

## Tier 2: source identity, admission, and provenance

These define where material came from and how `skillz` is allowed to use it. They do not prove individual skill quality.

| Artifact | Path | Freshness contract |
|---|---|---|
| Source registry | `registry/sources.yaml` | source identity, role, inclusion, exact pin/reference, license/terms, canonical physical path where locally admitted |
| Source context/signals | `registry/source-signals.yaml` | timestamped volatile source-level context kept separate from skill quality |
| Skill provenance companions | `registry/skills/` | canonical source/path/revision/freshness/license/relationship for individually characterized third-party skills |
| Third-party notices | `THIRD_PARTY_NOTICES.md` | attribution and license obligations track included third-party material |
| Provenance policy | `docs/third-party-provenance.md` | copying, adaptation, attribution, and relationship rules |
| Curation policy | `docs/curation-policy.md` | discovery, admission, static review, refresh, rejection, and retirement semantics |

Discovery surface, candidate source, admitted source, and individually verified skill are distinct states. Discovery never grants trust, redistribution authority, or unchanged-reuse eligibility.

A user-derived skill created during normal bootstrap is not a repository-admission candidate by implication. Repository admission requires a separate explicit maintainer decision and governed curation path.

## Tier 3: exact-version static quality

These determine what the external host agent may treat as reviewed evidence.

| Artifact | Path | Freshness contract |
|---|---|---|
| Verification companions | `registry/verification/` | each record applies only to its exact canonical skill identity/fingerprint |
| First-party review registry | `registry/local-verification.json` | individual structured semantic review of current first-party skills |
| Taxonomy | `registry/taxonomy.yaml` | controlled tags used consistently across characterization and selection |
| Verification standard | `docs/skill-verification.md` | current state meanings and structured semantic rubric |
| Companion metadata decision | Wayfinder decision #36 / current companion schema | provenance and verification remain distinct evidence surfaces |

A source can be official, reputable, popular, current, and locally present while an individual skill remains unverified. Popularity and reputation are context, not proof.

Static source completion requires an established eligible denominator and a decisive current state for every in-scope skill. Active `unverified`, `stale`, and legacy `trusted-baseline` do not satisfy completion. Rejected or retired material may remain useful bounded prior art.

## Tier 4: passive catalog and browsing surfaces

| Artifact | Path | Freshness contract |
|---|---|---|
| Human category registry | `registry/categories.yaml` | every local canonical first-party skill has an intentional category assignment |
| Category browse surface | `skills/categories/` | human navigation agrees with the canonical category registry |
| Machine catalog snapshot | `index.json` | hand-maintained/passively reconciled snapshot of the same live corpus truth |
| Human catalog snapshot | `INDEX.md` | hand-maintained/passively reconciled human view of the same corpus truth |

`INDEX.md` and `index.json` are **static catalog snapshots**. The repository does not own or require a catalog generator, idempotency script, executable refresh step, or materialization preflight. The external host agent may reconcile these files directly from evidence available through its legitimate repository/API/file capabilities only when operating under explicit repository-maintenance authority.

## Tier 5: behavioral evidence

Behavioral validation is optional later evidence for consequential or high-use skills after static corpus completion.

| Artifact | Path | Freshness contract |
|---|---|---|
| Behavioral/adversarial evidence | `docs/evals/` and/or exact-version companion references | evidence records only work actually performed by an external agent/environment |

`skillz` does not own an evaluator, test harness, scenario runner, fixtures pipeline, benchmark, or behavioral-validation runtime. Absence of behavioral evidence does not invalidate a completed static review; it simply means behavioral validation has not been established.

## Tier 6: authority and handoff safety

| Artifact | Path | Freshness contract |
|---|---|---|
| Installation/handoff contract | `docs/installation-handoff.md` | host-specific installation or transfer states are truthful and authority-bound |
| Agent/repository mutation boundaries | `AGENTS.md`, `AGENT_START_HERE.md`, and maintenance skills under `engine/skills/` | normal user artifacts target the user's host/handoff; repository mutation requires explicit maintainer routing |

Skill-owned scripts, examples, fixtures, templates, assets, or tooling may legitimately exist inside first-party or intact third-party skill packages. Their presence does not create repository-owned execution machinery. The host agent decides whether and how to use them under the user's authority and the target environment's constraints.

Writable repository access is not mutation authority. A host agent that can write to `skillz` must still remain read-only unless the active request is explicitly `REPOSITORY_MAINTENANCE`.

## Historical records

Historical execution-oriented files may remain when they are clearly non-authoritative and useful as provenance/history. Git history is also sufficient preservation for obsolete records that would otherwise confuse the live architecture.

Examples include historical Qor plans/gates, alpha lock/preflight documents, old CI descriptions, generator/test-era reports, and superseded evaluation procedures.

Historical accuracy should be preserved. Historical documents do not override current Tier 1 governance.

## Drift rule

When a current control surface changes:

1. update every other current artifact whose factual state is materially affected;
2. preserve evidence and provenance rather than rewriting historical results;
3. reconcile passive catalog snapshots directly, without introducing repository-owned generation machinery;
4. if exact evidence cannot be established, mark the state pending instead of guessing;
5. distinguish source context from individual skill quality;
6. distinguish terminology such as `vendored` from obsolete physical `vendor/...` path assumptions;
7. treat any current first-party claim that `skillz` runs, executes, schedules, monitors, crawls, installs, fetches, synchronizes, generates, tests, validates, or operates something as architecture/documentation drift;
8. treat any normal-use instruction that makes `skillz` the destination for a user-derived skill, or implies that `CREATE` means repository admission, as architecture/documentation drift.

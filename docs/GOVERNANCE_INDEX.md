# Governance Index

**Last reviewed:** 2026-08-29

This file maps the current authoritative governance surfaces for `skillz`.

The repository itself executes nothing. Governance is declarative: instructions, source pins, provenance, review evidence, tags, metadata, catalog snapshots, and documentation that an external agent reads and updates.

## Non-negotiable governance invariant

**The external host agent is active. `skillz` is passive.**

Current first-party governance must not require or imply a repository-owned:

- runtime;
- script or executable helper;
- CI workflow or test runner;
- scheduler, monitor, watcher, or background process;
- installer or synchronizer;
- preflight process;
- index/catalog generator;
- autonomous validation or refresh service.

Third-party pinned source repositories may contain code or tooling of their own. Preserving that upstream material as reference content does not make it part of a `skillz` runtime.

## Authority and precedence

When current documents disagree, resolve them in this order:

1. explicit current user instruction;
2. `README.md` repository identity and purpose;
3. `AGENT_START_HERE.md` and `AGENTS.md` agent boundaries;
4. `BOOTSTRAP.md` discovery/refinement method;
5. this Governance Index and the current policy documents listed below;
6. `docs/CONCEPT.md`, `docs/ARCHITECTURE_PLAN.md`, `docs/SYSTEM_STATE.md`, and `ROADMAP.md`;
7. active Wayfinder decisions/issues;
8. passive registries and companion evidence for the specific source/skill being evaluated;
9. historical implementation/evaluation material.

A lower-precedence historical document never reintroduces repository-owned execution.

## Tier 1: identity and current state

| Artifact | Path | Governance role |
|---|---|---|
| Human/agent front door | `README.md` | passive identity, purpose, inventory boundary, core rules |
| Agent entry | `AGENT_START_HERE.md` | external-agent access paths and passive-repository invariant |
| Agent contract | `AGENTS.md` | routing, privacy, curation, quality, and mutation boundaries |
| Bootstrap/refinement guide | `BOOTSTRAP.md` | first-visit and returning-user discovery method |
| Concept | `docs/CONCEPT.md` | why the repository exists and what it is/is not |
| Architecture | `docs/ARCHITECTURE_PLAN.md` | passive repository structure and boundaries |
| System state | `docs/SYSTEM_STATE.md` | current curation state and next frontier |
| Roadmap | `ROADMAP.md` | source-by-source curation and production-readiness path |
| Wayfinder map | GitHub Issue #35 | destination, boundaries, decisions, fog, current frontier |

All Tier 1 surfaces must agree on the passive-repository invariant.

## Tier 2: corpus identity, provenance, and source context

| Artifact | Path | Governance role |
|---|---|---|
| User-facing corpus | `skills/` | all user-facing skill material lives under this tree |
| Pinned source corpora | `skills/sources/` | intact upstream identity, dependencies, license, and revision preserved |
| Source registry | `registry/sources.yaml` | source role, inclusion, exact pin/reference, license |
| Source signals | `registry/source-signals.yaml` | timestamped source-level visibility/maintenance context only |
| Skill provenance companions | `registry/skills/` | source/path/revision/freshness/dependency/relationship evidence |
| Third-party notices | `THIRD_PARTY_NOTICES.md` | attribution/license notices for included third-party material |
| Provenance policy | `docs/third-party-provenance.md` | copying/adaptation/attribution rules |
| Pinned-source freshness | `docs/vendor-freshness.md` | passive external-agent review method for newer upstream evidence |
| Companion metadata | `docs/companion-metadata.md` | normative evidence split and interpretation order |
| Curation policy | `docs/curation-policy.md` | availability, characterization, verification, validation, source-context semantics |

Source reputation, source freshness, and individual skill quality remain separate facts.

## Tier 3: quality and selection evidence

| Artifact | Path | Governance role |
|---|---|---|
| Verification registry | `registry/verification/` | exact-version quality state and controlled tags |
| Taxonomy | `registry/taxonomy.yaml` | controlled characterization vocabulary |
| Verification standard | `docs/skill-verification.md` | external-agent structured static-review rubric/status meanings |
| Reviewed shelf | `CURATED.md` | human-readable view that should agree with current companion records |
| Audit instructions | `engine/skills/skill-audit/SKILL.md` | passive external-agent review procedure |
| Source-vetting instructions | `engine/skills/source-vetting/SKILL.md` | passive source/provenance/trust review procedure |

A source can be official, popular, active, and included while an individual skill remains unverified, rejected, stale, or a poor fit.

Use this interpretation order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

The external agent may `ADOPT`, `ADAPT`, `EXTRACT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, use a checklist/helper, keep behavior dynamic, reject unchanged reuse, or conclude `NO CHANGE`.

## Tier 4: discovery and fitted-skill guidance

| Artifact | Path | Governance role |
|---|---|---|
| Bootstrap instructions | `engine/skills/skill-bootstrap/SKILL.md` | passive latent-skill discovery and fit method |
| Skill authoring | `engine/skills/skill-forge/SKILL.md` | passive artifact-authoring guidance |
| Behavioral evaluation | `engine/skills/skill-eval/SKILL.md` | guidance for evaluation performed in an external host |
| Skill transfer | `engine/skills/skill-sync/SKILL.md` | external-host transfer/install guidance only |
| Limited discovery | `engine/skills/skills-pulse/SKILL.md` | external on-demand ecosystem discovery; no monitoring process |
| Portable profile | `docs/portable-skill-profile.md` | passive representation of fitted user behavior |
| Installation handoff | `docs/installation-handoff.md` | external-host authority and truthful completion states |

None of these files performs its procedure by existing in the repository.

## Tier 5: passive navigation

| Artifact | Path | Governance role |
|---|---|---|
| Human category registry | `registry/categories.yaml` | intentional category assignment for canonical local skills |
| Category browse surface | `skills/categories/` | human navigation that should agree with the live skill tree |
| Human catalog snapshot | `INDEX.md` | passive convenience snapshot; reconcile when it drifts |
| Machine catalog snapshot | `index.json` | passive convenience snapshot; reconcile when it drifts |

Catalog snapshots are not runtime truth. Live skill files plus current registry/companion evidence control when snapshots disagree.

## Historical execution-oriented records

Older files may describe Qor gates, CI, tests, scripts, preflight, generated catalog proofs, alpha-lock harnesses, or treatment/evaluator execution systems.

They are historical unless explicitly re-established by higher-precedence current governance. Current architecture does not include those mechanisms.

Historical examples may include:

- `.qor/gates/`;
- `docs/META_LEDGER.md`;
- `docs/plan-qor-*.md`;
- older alpha/implementation trackers;
- older evaluation runbooks and fixtures;
- Git history for removed scripts/tests/workflows.

Historical accuracy may be preserved, but historical documents never override the passive-repository invariant.

## Drift rule

When a current control surface changes:

1. update every other current artifact whose factual state is affected;
2. preserve source/provenance history rather than fabricating continuity;
3. update passive catalog snapshots directly when useful, using the external agent;
4. if exact evidence cannot be established, mark it unavailable/pending rather than guessing;
5. do not introduce executable machinery merely to prove, validate, generate, or maintain documentation;
6. treat any current first-party claim that `skillz` itself runs, schedules, tests, fetches, monitors, validates, installs, synchronizes, generates, or executes as architecture drift.

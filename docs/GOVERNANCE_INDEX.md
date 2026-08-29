# Governance Index

**Last reviewed:** 2026-08-29

This file maps the current authoritative governance surfaces for `skillz`.

The repository itself executes nothing. Governance is declarative: instructions, source pins and references, provenance, review evidence, tags, metadata, catalog snapshots, discovery guidance, and documentation that an external agent reads and updates.

## Non-negotiable governance invariant

**The external host agent is active. `skillz` is passive.**

Current first-party governance must not require or imply a repository-owned:

- runtime;
- script or executable helper;
- CI workflow or test runner;
- scheduler, monitor, watcher, crawler, or background process;
- installer or synchronizer;
- preflight process;
- index/catalog generator;
- autonomous discovery, validation, intake, or refresh service.

Third-party pinned source repositories may contain code or tooling of their own. Preserving that upstream material as reference content does not make it part of a `skillz` runtime.

## Skill-location invariant

Every `SKILL.md` physically owned by this repository must live under exactly one of these roots:

1. **`skills/**`** for user-facing, reusable, imported, adapted, or pinned-source skill material.
2. **`engine/skills/**`** only for repository-maintenance skills whose purpose is maintaining or curating `skillz` itself.

The current seven repository-maintenance skills belong under `engine/skills/`. Future repository-maintenance skills may also be created there when genuinely warranted.

No third skill root is valid.

Repository-maintenance skills are formatted as skills because an external agent uses them as procedures, but they are excluded from user-facing/custom-skill inventory counts.

## Purpose boundary

`skillz` accumulates reusable skill knowledge so the host agent can construct the smallest useful custom skill set for the user.

That accumulated knowledge may include complete skills, procedures, safeguards, anti-patterns, rejected examples, provenance, quality evidence, creator methods, standards, and source-specific prior art.

The repository does not mechanically choose or install a user skill set. The host agent reasons over relevant user context and the accumulated corpus, then may `ADOPT`, `ADAPT`, `EXTRACT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, use a checklist, keep behavior dynamic, or conclude `NO CHANGE`.

Integrated subsystem references are different. When a source such as Qor-logic is valuable specifically because of system-level governance and cross-component invariants, the host chooses `RECOMMEND SYSTEM` or `DO NOT RECOMMEND SYSTEM`; it does not mine that subsystem for independent custom-skill ingredients unless the upstream product explicitly defines a safe standalone boundary.

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
9. historical information recoverable from Git history.

A lower-precedence historical record never reintroduces repository-owned execution.

## Source lifecycle

Governance distinguishes four states that must not be collapsed:

1. **Discovery surface**: a public or connected place the host agent may inspect for useful skills, methods, creators, standards, or corpora.
2. **Candidate source**: discovered material with enough provenance, licensing, and relevance evidence to justify deeper source-vetting.
3. **Admitted corpus/reference source**: intentionally represented material with clear identity, terms, source role, and snapshot/reference evidence.
4. **Individually reviewed skill**: an exact skill version with provenance, characterization, controlled tags, and decisive static quality state when the source is composable.

Discovery may proceed in parallel with static review of already-admitted sources. Discovery does **not** grant trust, verification, installation authority, or automatic corpus admission.

`skillz` does not monitor or crawl discovery surfaces. The host agent intentionally performs each discovery or review action using its own capabilities.

## Tier 1: identity and current state

| Artifact | Path | Governance role |
|---|---|---|
| Human/agent front door | `README.md` | passive identity, purpose, accumulated-knowledge model, inventory boundary, core rules |
| Agent entry | `AGENT_START_HERE.md` | external-agent access paths, skill-location invariant, and passive-repository invariant |
| Agent contract | `AGENTS.md` | routing, privacy, curation, quality, mutation, and location boundaries |
| Bootstrap/refinement guide | `BOOTSTRAP.md` | first-visit and returning-user discovery method |
| Concept | `docs/CONCEPT.md` | why the repository exists and what it is/is not |
| Architecture | `docs/ARCHITECTURE_PLAN.md` | passive repository structure and boundaries |
| System state | `docs/SYSTEM_STATE.md` | current curation/discovery state and next frontier |
| Roadmap | `ROADMAP.md` | source curation, governed discovery, and production-readiness path |
| Wayfinder map | GitHub Issue #35 | destination, boundaries, decisions, fog, current frontier |
| Source queue | GitHub Issue #27 | admitted-source completion plus discovery/source-vetting queue |

All Tier 1 surfaces must agree on the passive-repository invariant and canonical skill roots.

## Tier 2: corpus identity, provenance, and source context

| Artifact | Path | Governance role |
|---|---|---|
| User-facing corpus | `skills/` | all user-facing/reusable skill material lives under this tree |
| Repository-maintenance skills | `engine/skills/` | maintenance-only exception; excluded from user-facing counts |
| Pinned source corpora | `skills/sources/` | intact upstream identity, dependencies, license, and revision preserved |
| Source registry | `registry/sources.yaml` | admitted/reference/discovery source identity, role, license, and pin/reference |
| Source signals | `registry/source-signals.yaml` | timestamped source-level visibility/maintenance context only |
| Skill provenance companions | `registry/skills/` | source/path/revision/freshness/dependency/relationship evidence |
| Third-party notices | `THIRD_PARTY_NOTICES.md` | attribution/license notices for included third-party material |
| Provenance policy | `docs/third-party-provenance.md` | copying/adaptation/attribution rules |
| Pinned-source freshness | `docs/vendor-freshness.md` | passive external-agent review method for upstream evidence |
| Companion metadata | `docs/companion-metadata.md` | normative evidence split and interpretation order |
| Curation policy | `docs/curation-policy.md` | discovery, admission, integrated-subsystem handling, characterization, verification, validation, source-context semantics |

Source reputation, source freshness, discovery relevance, and individual skill quality remain separate facts.

## Tier 3: quality and selection evidence

| Artifact | Path | Governance role |
|---|---|---|
| Verification registry | `registry/verification/` | exact-version quality state and controlled tags |
| Taxonomy | `registry/taxonomy.yaml` | controlled characterization vocabulary |
| Verification standard | `docs/skill-verification.md` | external-agent structured static-review rubric/status meanings |
| Audit instructions | `engine/skills/skill-audit/SKILL.md` | passive external-agent review procedure |
| Source-vetting instructions | `engine/skills/source-vetting/SKILL.md` | passive source/provenance/trust/admission review procedure |

A source can be official, popular, active, and admitted while an individual skill remains unverified, rejected, stale, or a poor fit.

Use this interpretation order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Tier 4: discovery and fitted-skill guidance

| Artifact | Path | Governance role |
|---|---|---|
| Bootstrap instructions | `engine/skills/skill-bootstrap/SKILL.md` | passive latent-skill discovery and fit method |
| Skill authoring | `engine/skills/skill-forge/SKILL.md` | passive artifact-authoring guidance |
| Behavioral evaluation | `engine/skills/skill-eval/SKILL.md` | guidance for evaluation performed in an external host |
| Skill transfer | `engine/skills/skill-sync/SKILL.md` | external-host transfer/install guidance only |
| Ecosystem discovery | `engine/skills/skills-pulse/SKILL.md` | external on-demand ecosystem discovery; no monitoring process |
| Source queue | Issue #27 | candidates from GitHub, Hugging Face, creators, standards, aggregators, and other legitimate discovery surfaces |
| Portable profile | `docs/portable-skill-profile.md` | passive representation of fitted user behavior |
| Installation handoff | `docs/installation-handoff.md` | external-host authority and truthful completion states |

None of these files performs its procedure by existing in the repository.

## Tier 5: passive navigation

| Artifact | Path | Governance role |
|---|---|---|
| Human category registry | `registry/categories.yaml` | intentional category assignment for canonical local skills |
| Category browse surface | `skills/categories/` | human navigation that should agree with the live local skill tree |
| Human catalog snapshot | `INDEX.md` | passive hand-maintained snapshot; reconcile when it drifts |
| Machine catalog snapshot | `index.json` | passive hand-maintained machine snapshot; reconcile when it drifts |

Catalog snapshots are not runtime truth. Live skill files plus current registry/companion evidence control when snapshots disagree.

## Historical material

Git history is the archive for superseded execution-era architecture, Qor phase plans, alpha-lock machinery, obsolete generated catalogs, and similar artifacts that no longer help a viewing agent use the current passive repository.

Do not keep obsolete files in the live tree merely to prove that they once existed. Preserve a historical file physically only when it still provides useful evidence or context that is not better represented by current governance and Git history.

## Drift rule

When a current control surface changes:

1. update every other current artifact whose factual state is affected;
2. preserve source/provenance history rather than fabricating continuity;
3. distinguish discovery from source admission and admission from individual verification;
4. update passive catalog snapshots directly when useful, using the external agent;
5. if exact evidence cannot be established, mark it unavailable/pending rather than guessing;
6. do not introduce executable machinery merely to discover, prove, validate, generate, or maintain documentation;
7. treat any current first-party claim that `skillz` itself runs, schedules, scans, crawls, tests, fetches, monitors, validates, installs, synchronizes, generates, or executes as architecture drift;
8. treat any `SKILL.md` outside `skills/**` or `engine/skills/**` as path drift, and any non-maintenance skill under `engine/skills/**` as classification drift.

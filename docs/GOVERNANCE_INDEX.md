# Governance Index

**Last reviewed:** 2026-08-29

This file maps the current authoritative passive control surfaces for `skillz`.

The repository itself executes nothing. Governance is expressed through instructions, source pins, provenance, review evidence, tags, and documentation that an external agent reads and updates.

## Tier 1: identity and current state

| Artifact | Path | Freshness contract |
|---|---|---|
| Human/agent front door | `README.md` | passive identity, purpose, inventory boundary, core rules |
| Agent entry | `AGENT_START_HERE.md` | external-agent access paths and passive-repository invariant |
| Agent contract | `AGENTS.md` | routing, quality, privacy, curation, mutation boundaries |
| Bootstrap/refinement guide | `BOOTSTRAP.md` | first-visit and returning-user discovery method |
| Concept | `docs/CONCEPT.md` | why the repository exists and what it is/is not |
| Architecture | `docs/ARCHITECTURE_PLAN.md` | passive repository structure and boundaries |
| System state | `docs/SYSTEM_STATE.md` | current curation state and next action |
| Roadmap | `ROADMAP.md` | source-by-source curation and production-readiness path |
| Wayfinder map | GitHub Issue #35 | destination, boundaries, decisions, fog, current frontier |

These surfaces must agree that **the external host agent is active and `skillz` is passive**.

## Tier 2: corpus identity and provenance

| Artifact | Path | Freshness contract |
|---|---|---|
| User-facing corpus | `skills/` | all user-facing skill material lives under this tree |
| Pinned source corpora | `skills/sources/` | intact upstream identity, dependencies, license, and pin preserved |
| Source registry | `registry/sources.yaml` | current source role, inclusion, exact pin/reference, license |
| Source signals | `registry/source-signals.yaml` | timestamped source-level visibility/maintenance context only |
| Skill provenance companions | `registry/skills/` | source/path/revision/freshness/dependency/relationship evidence |
| Third-party notices | `THIRD_PARTY_NOTICES.md` | attribution/license notices track included third-party material |
| Provenance policy | `docs/third-party-provenance.md` | copying/adaptation/attribution rules remain consistent with registry |
| Companion metadata | `docs/companion-metadata.md` | normative evidence split and interpretation order |
| Curation policy | `docs/curation-policy.md` | availability, characterization, verification, validation, source-context semantics |

## Tier 3: quality and selection evidence

| Artifact | Path | Freshness contract |
|---|---|---|
| Verification registry | `registry/verification/` | record applies only to its exact characterized skill version/fingerprint |
| Taxonomy | `registry/taxonomy.yaml` | controlled tags used consistently by characterization and selection reasoning |
| Verification standard | `docs/skill-verification.md` | structured static-review rubric/status meanings current |
| Reviewed shelf | `CURATED.md` | human-readable sample/shelf agrees with live companion records |
| Audit instructions | `engine/skills/skill-audit/SKILL.md` | passive external-agent review method |
| Source-vetting instructions | `engine/skills/source-vetting/SKILL.md` | passive source/provenance/trust review method |

A source can be present, reputable, official, and current while an individual skill remains unverified or rejected.

Use this interpretation order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Tier 4: discovery and fitted-skill guidance

| Artifact | Path | Freshness contract |
|---|---|---|
| Bootstrap instructions | `engine/skills/skill-bootstrap/SKILL.md` | passive latent-skill discovery and fit method |
| Skill authoring | `engine/skills/skill-forge/SKILL.md` | passive artifact-authoring guidance |
| Behavioral evaluation | `engine/skills/skill-eval/SKILL.md` | external evaluation guidance only |
| Skill transfer | `engine/skills/skill-sync/SKILL.md` | external host transfer/install guidance only |
| Limited discovery | `engine/skills/skills-pulse/SKILL.md` | external on-demand ecosystem discovery, no monitoring process |
| Portable profile | `docs/portable-skill-profile.md` | passive representation of fitted user behavior |
| Installation handoff | `docs/installation-handoff.md` | external-host authority and truthful completion states |

None of these files executes its procedure itself.

## Tier 5: passive navigation

| Artifact | Path | Freshness contract |
|---|---|---|
| Human category registry | `registry/categories.yaml` | local canonical skills have intentional category assignment |
| Category browse surface | `skills/categories/` | human navigation agrees with live skill tree |
| Human catalog snapshot | `INDEX.md` | static snapshot; reconcile when it drifts |
| Machine catalog snapshot | `index.json` | static snapshot; reconcile when it drifts |

Catalog snapshots are conveniences, not generated runtime truth. Live skill files and registry companions control when snapshots disagree.

## Historical execution-oriented records

Older files may describe Qor gates, CI, tests, scripts, preflight, generated catalog proofs, alpha-lock harnesses, or treatment/evaluator execution systems.

They are historical unless explicitly re-established by the Tier 1 documents above. Current architecture does not include those mechanisms.

Historical examples may include:

- `.qor/gates/`;
- `docs/META_LEDGER.md`;
- `docs/plan-qor-*.md`;
- older alpha/implementation trackers;
- older evaluation runbooks and fixtures;
- git history for removed scripts/tests/workflows.

Historical accuracy may be preserved, but historical documents never override the passive-repository invariant.

## Drift rule

When a current control surface changes:

1. update every other current artifact whose factual state is affected;
2. preserve source/provenance history rather than fabricating continuity;
3. update passive catalog snapshots directly when useful, using the external agent;
4. if exact evidence cannot be established, mark it unavailable/pending rather than guessing;
5. do not introduce executable machinery merely to prove or maintain documentation;
6. treat any current first-party claim that `skillz` runs, schedules, tests, fetches, monitors, validates, installs, or executes as architecture drift.

# Skill Companion Metadata Contract

`skillz` uses companion metadata so an agent can reason about skills without pretending that source branding, popularity, physical presence, or familiarity proves identity or quality.

The contract separates **provenance and operational facts**, **exact-version quality evidence**, and **source-level context**.

## 1. Provenance companion

Path:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

This file answers: **what is this skill, where did it come from, what does it depend on, what authority does it carry, and under what terms may it be used?**

A provenance companion is **mandatory for every governed user-facing skill**. A skill without provenance is incomplete corpus material and must not be represented as companion-complete, verified inventory, regardless of whether it is first-party, imported, vendored/pinned, adapted, or externally referenced.

For first-party skills, provenance must truthfully identify the repository as the source/relationship and record the applicable local identity and review facts rather than inventing an upstream publisher. For third-party or adapted material, preserve canonical source identity and applicable license/attribution obligations.

Required when establishable:

- `schema_version`
- `skill_name`
- `display_name`
- `source_id`
- `source_repository`
- `source_path`
- `source_class`
- `license`
- `relationship`
- `source_snapshot_revision`
- `upstream_revision`
- `upstream_last_updated_at`
- `curated_at`
- `last_checked_at`
- `availability`
- `local_path` when physically present in the governed repository
- `permission_tier`
- `portability`
- `review_status`
- `dependency_status`
- `dependencies`
- `import_eligibility`
- `rationale`

Optional evidence-backed fields include `upstream_first_seen_at`, `usage_evidence`, and `reception_evidence`.

Do not infer skill age, usage duration, or reception from repository age, stars, or general source reputation. Unknown facts are recorded as unknown or omitted where the schema permits; they are never guessed merely to satisfy completeness theater.

## 2. Exact-version verification companion

Path:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

This file answers: **what quality state applies to this exact canonical skill content?**

Every governed user-facing skill must have a verification companion before it is represented as statically complete. The record owns:

- fingerprint algorithm and canonical content hash;
- characterization/review timestamps;
- `verification_status` and its basis;
- `validation_status` and behavioral evidence references;
- structured rubric score/result;
- controlled tags;
- material review notes.

Current unchanged-selection semantics:

- `verified` / `validated`: eligible for unchanged consideration when exact identity and operational/user fit match;
- `unverified`: design evidence only;
- `trusted-baseline`: legacy schema state, design evidence only until current individual review;
- `stale`, `rejected`, `retired`: excluded from normal unchanged selection.

Verification metadata must remain independent of source reputation.

## 3. Source-level context snapshot

Path:

```text
registry/source-signals.yaml
```

This contains volatile source-level facts such as:

- repository creation/activity dates;
- stars/forks/watchers where meaningful;
- archive/disabled state;
- other objective source-maintenance/adoption signals.

Every snapshot needs an observation timestamp and evidence surface. These are historical observations, not timeless truths.

## 4. Agent reasoning order

When deciding whether to `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, extract a mechanism, reject, or `CREATE`, reason in this order:

1. **User fit**: does the capability match the user's durable workflow, constraints, authority model, and definition of done?
2. **Exact-version quality**: what decisive state applies to the exact content?
3. **Operational fit**: are dependencies intact, authority acceptable, and host assumptions compatible?
4. **Freshness**: has skill content/evidence drifted?
5. **Provenance/source context**: who maintains it, under what license, and what weak contextual source signals exist?

An official source or large star count cannot override poor fit, unsafe authority, missing dependencies, incompatible terms, or a blocked quality state.

## 5. Component-level reasoning

Whole-skill eligibility and component reuse are related but not identical.

A non-eligible skill may still expose a useful mechanism. Before materially borrowing one, record:

- the source and exact material inspected;
- applicable license/attribution obligations;
- the mechanism being carried forward;
- dependencies or assumptions the mechanism needs;
- whether the source's rejection/staleness reason affects it;
- the destination artifact;
- what source-specific baggage was intentionally omitted.

A general idea may inform an independently expressed custom implementation. Material copying/adaptation remains subject to provenance and license obligations.

Do not use "we only borrowed a component" as a magical exemption from licensing, safety, dependency, or authority review. Lawyers and production incidents are both famously unimpressed by semantic creativity.

## 6. Refresh rules

- Refresh provenance when canonical content, dependencies, licensing, or source identity materially changes.
- Refresh exact-version verification whenever the canonical fingerprint changes before trusting prior quality evidence.
- Refresh source-level signals only when a source is re-reviewed or a material decision depends on current context.
- Preserve prior states through Git history.

## 7. Completeness rule

A governed user-facing skill is companion-complete only when:

1. its provenance companion exists and contains all establishable required facts;
2. unknown/unavailable facts are explicit rather than guessed;
3. its verification companion exists and binds to canonical content;
4. controlled metadata is present;
5. structured review has a decisive quality state;
6. behavioral validation status is explicit, including `not-run` when appropriate;
7. an agent can distinguish exact-version quality from source reputation without ambiguity.

**Missing provenance is a blocking completeness defect.** Such a skill may remain visible as historical/reference material while being repaired, but it must not be counted as provenance-complete, verification-complete, or statically complete governed inventory.

This rule applies to existing skills as well as future admissions. Legacy presence does not waive the contract.

A broad pinned or tracked source without per-skill companions remains reference/discovery corpus. It is not silently promoted to governed trusted inventory.
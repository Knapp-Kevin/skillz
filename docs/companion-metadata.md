# Skill Companion Metadata Contract

`skillz` uses passive companion metadata to help an external host agent understand a skill without pretending that popularity, age, source branding, or inclusion proves the skill is good.

The repository does not compute or refresh this metadata by itself. An external reviewing agent reads source evidence, makes the judgment, and records the result. The contract deliberately separates **skill-specific facts**, **exact-version quality evidence**, and **source-level context** so agents can reason from evidence without duplicating volatile repository metrics across hundreds of files.

## 1. Per-skill provenance companion

Path:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

This file answers: **what is this skill, where did it come from, what does it depend on, and what is it useful for?**

### Expected fields when establishable

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
- `local_path` when vendored/imported
- `permission_tier` or equivalent authority context
- `portability`
- `review_status`
- `dependency_status`
- `dependencies`
- `import_eligibility`
- `rationale`

### Optional evidence-backed enrichment

Use these only when the evidence can be established without guessing:

- `upstream_first_seen_at`: earliest known upstream commit that introduced the canonical skill or materially equivalent skill content.
- `usage_evidence`: explicit evidence that the skill itself is used in practice, with source and observation date.
- `reception_evidence`: skill-specific public feedback, references, adoption notes, or maintained examples directly attributable to this skill.

Do not infer skill age, usage duration, or reception from repository creation date, stars, forks, or source reputation.

## 2. Exact-version verification companion

Path:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

This file answers: **what quality state applies to this exact canonical skill version?**

It owns:

- canonical content identity/fingerprint and the method used to establish it;
- characterization and verification timestamps;
- `verification_status` and its basis;
- `validation_status` and behavioral evidence references;
- structured review/rubric result where applicable;
- controlled tags;
- review notes and material limitations.

Verification metadata must remain separate from source popularity and branding. A source can be famous while an individual skill is unsafe, stale, redundant, dependency-broken, or simply a poor fit.

An exact Git blob SHA is preferred when the source host exposes one reliably. Another content fingerprint may be recorded when needed, but the reviewing agent must identify how it was established. If exact identity cannot be established, do not invent it.

## 3. Source-level context snapshot

Path:

```text
registry/source-signals.yaml
```

This file contains volatile context that applies to a source repository rather than to one skill. Store it once instead of duplicating it in every per-skill companion.

Permitted source signals include:

- repository creation date;
- most recent repository push/activity timestamp;
- stars;
- forks;
- subscribers/watchers when the source exposes a meaningful count;
- archived/disabled state;
- official/community status;
- other objective adoption or maintenance signals when the source and observation date are recorded.

Every snapshot must include `observed_at` and the evidence surface used. Metrics are historical observations, not timeless facts.

## 4. How an agent should use the metadata

When deciding whether to `ADOPT`, `ADAPT`, `EXTRACT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, reject, use a checklist/helper, keep behavior dynamic, or make `NO CHANGE`, reason in this order:

1. **User fit.** Does the skill actually match the user's durable workflow, authority model, terminology, constraints, and definition of done?
2. **Exact-version quality.** Is the exact content identity current, and what decisive quality state applies?
3. **Operational fit.** Are dependencies intact? Is the authority level appropriate? Is the skill portable to the current host?
4. **Freshness.** When did the skill itself last materially change? Has its content or dependency context drifted?
5. **Provenance and source context.** Who maintains it, under what license, and what objective source-level adoption/maintenance signals exist?

Source popularity may increase confidence that a source is visible, maintained, or broadly examined. It must **never** override poor user fit, unsafe authority, stale exact-version evidence, missing dependencies, licensing restrictions, or an unverified/rejected skill.

A large star count is not a quality state. An official source is not individual-skill verification. A new or low-star source is not automatically low quality.

## 5. Update rules

There is no repository-owned metadata refresh process.

When an external agent intentionally reviews a skill or source:

- update per-skill provenance when the skill is re-reviewed, its canonical content changes, or its dependency/licensing context changes;
- update exact-version verification when the canonical content identity changes before trusting prior quality state;
- update source-level signals when a source is re-reviewed or when a material curation decision benefits from current reputation/activity context;
- preserve prior observations through Git history rather than pretending volatile facts never changed;
- leave unavailable facts unknown instead of filling them with estimates.

Routine hourly refresh of popularity metrics is unnecessary. The hourly curation task may improve records, but the task is external to `skillz`; the repository itself remains passive.

## 6. Completeness rule

A characterized third-party skill is companion-complete when:

1. its provenance companion contains the material facts that can be established from the source;
2. unknown or unavailable facts are omitted or explicitly marked unknown rather than guessed;
3. its exact-version verification companion exists and binds the quality decision to an established content identity;
4. source-level context, if used in reasoning, is available through `registry/source-signals.yaml` with an observation timestamp;
5. the reviewing agent can distinguish individual skill quality from source reputation without ambiguity;
6. the records are understandable without executing repository-owned code.

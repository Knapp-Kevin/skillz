# Skill Companion Metadata Contract

`skillz` uses companion metadata to help a host agent understand a skill without pretending that popularity, age, or source branding proves the skill is good.

The contract deliberately separates **skill-specific facts**, **exact-version quality evidence**, and **source-level context** so agents can reason from evidence without copying volatile repository metrics into hundreds of files.

## 1. Per-skill provenance companion

Path:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

This file answers: **what is this skill, where did it come from, what does it depend on, and what is it useful for?**

### Required when establishable

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
- `permission_tier`
- `portability`
- `review_status`
- `dependency_status`
- `dependencies`
- `import_eligibility`
- `rationale`

### Optional evidence-backed enrichment

Use these fields only when the evidence can be established without guessing:

- `upstream_first_seen_at`: earliest known upstream commit that introduced the canonical skill or materially equivalent skill content.
- `usage_evidence`: explicit evidence that the skill itself is used in practice, with source and observation date. Repository age or stars alone do not establish usage duration.
- `reception_evidence`: skill-specific public feedback, references, adoption notes, or maintained examples when directly attributable to this skill.

Do not infer `upstream_first_seen_at`, usage duration, or reception from repository creation date.

## 2. Exact-version verification companion

Path:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

This file answers: **what quality state applies to this exact canonical skill version?**

It owns:

- canonical content fingerprint and fingerprint algorithm;
- characterization and verification timestamps;
- `verification_status` and its basis;
- `validation_status` and behavioral evidence references;
- structured review/rubric result where applicable;
- controlled tags;
- review notes.

Verification metadata must remain separate from source popularity and branding. A source can be famous while an individual skill is unsafe, stale, redundant, or a poor fit.

## 3. Source-level context snapshot

Path:

```text
registry/source-signals.yaml
```

This file contains volatile context that applies to a source repository rather than to one skill. Store it once instead of duplicating it in every per-skill companion.

Permitted source signals include:

- repository creation date;
- most recent repository push/activity timestamp;
- GitHub stars;
- GitHub forks;
- GitHub subscribers/watchers when the API exposes a meaningful count;
- archived/disabled state;
- other objective adoption or maintenance signals when the source and observation date are recorded.

Every snapshot must include `observed_at` and the evidence URL/API surface used. Metrics are historical observations, not timeless facts.

## 4. How an agent should use the metadata

When deciding whether to `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, extract from, reject, or `CREATE`, reason in this order:

1. **User fit.** Does the skill actually match the user's durable workflow, authority model, terminology, constraints, and definition of done?
2. **Exact-version quality.** Is the fingerprint current, and is the skill `trusted-baseline`, `verified`, `validated`, `unverified`, `stale`, `rejected`, or `retired`?
3. **Operational fit.** Are dependencies intact? Is the authority level appropriate? Is the skill portable to the current host?
4. **Freshness.** When did the skill itself last materially change? Has its fingerprint or dependency context drifted?
5. **Provenance and source context.** Who maintains it, under what license, and what objective source-level adoption/maintenance signals exist?

Source popularity may increase confidence that a source is visible, maintained, or broadly examined. It must **never** override poor user fit, an unsafe authority model, stale exact-version evidence, missing dependencies, or an unverified skill.

A large star count is not a quality state. An official source is not an individual-skill verification. A new or low-star source is not automatically low quality.

## 5. Refresh rules

- Refresh per-skill provenance when the skill is re-reviewed, its canonical content changes, or its dependency/licensing context changes.
- Refresh exact-version verification whenever the canonical fingerprint changes before trusting prior quality state.
- Refresh source-level signals when a source is re-reviewed or when a material curation decision depends on current source reputation/activity. Routine hourly refresh of popularity metrics is unnecessary.
- Preserve prior observations through Git history rather than pretending volatile metrics never changed.

## 6. Completeness rule

A characterized third-party skill is companion-complete when:

1. its provenance companion contains all required fields that can be established from the source;
2. unknown or unavailable facts are omitted or explicitly marked unknown rather than guessed;
3. its exact-version verification companion exists and binds to the canonical content fingerprint;
4. source-level context, if used in reasoning, is available through `registry/source-signals.yaml` with an observation timestamp;
5. the reviewing agent can distinguish skill quality from source reputation without ambiguity.

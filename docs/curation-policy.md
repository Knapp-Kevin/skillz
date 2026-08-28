# Skill Curation Policy

`skillz` is a library, not a dump.

The library is intended to grow to hundreds of useful skills, but a larger count is not itself evidence of quality. Curation exists to preserve source identity, freshness, licensing, dependencies, safety context, and the reason a skill earned a place.

## Two things can be true

A skill may be valuable enough to curate without being copied into this repository yet.

A curated skill can therefore be:

- **vendored**: present inside an intact pinned upstream repository under `vendor/`,
- **imported**: copied into this repository with required upstream notices and any necessary local adaptation,
- **external**: reviewed and indexed as useful, but still read from its upstream source because bringing it in incompletely would be misleading or broken.

Curation status and physical availability are separate facts.

## Companion record

Every curated third-party skill must have a companion YAML record under `registry/skills/<source-id>/<skill-name>.yaml`.

The record is the auditable answer to questions future maintainers should not have to rediscover:

- Where did this skill come from?
- What exact upstream path contains it?
- Who maintains the source?
- What license applies?
- What source revision was inspected?
- What commit most recently changed this skill?
- When did that skill-specific change occur?
- When did we curate and last check it?
- Is the skill actually present here, or only tracked externally?
- Does it depend on shared files, scripts, tools, or host capabilities?
- What permission/risk tier does using it imply?
- Why did it earn a place?
- Has it been behaviorally evaluated here, or merely source-reviewed?

## Freshness semantics

`upstream_last_updated_at` means the timestamp of the most recent upstream commit that changed the skill or its canonical skill file.

It does **not** mean:

- the repository's last push,
- the repository's latest release,
- the date the source was added here,
- the date somebody happened to look at it.

Repository activity is recorded separately as `source_last_pushed_at` when useful.

A skill is not rejected merely for age. Stable skills can remain valuable for years. Age is a review signal, not a quality score.

## Required fields

Every companion record must include:

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
- `permission_tier`
- `portability`
- `review_status`
- `dependency_status`
- `dependencies`
- `import_eligibility`
- `rationale`

`local_path` is required for `vendored` and `imported` records and must be omitted for `external` records.

## Curation dispositions

- **curated**: high enough signal to make available to library users and bootstrap comparison.
- **sandbox**: promising but requires behavioral or security evaluation before normal use.
- **track**: worth monitoring, not yet promoted into the curated library.
- **quarantined**: potentially useful but carries unresolved authority, security, licensing, or provenance risk.
- **retired**: previously curated, no longer recommended for new use. Provenance history remains.

## Import rule

Do not copy a standalone `SKILL.md` when it relies on shared upstream references, scripts, templates, assets, hooks, or other files that are not also present.

A partial copy that looks installable but breaks when followed is worse than an honest external reference.

When a source is best consumed as a coherent collection, prefer a pinned submodule or another intact-source mechanism over cherry-picking individual files.

## License rule

The root MIT license applies to first-party `skillz` content only.

Third-party skills retain their upstream license obligations. Companion records must identify the upstream license. Copied or materially adapted work must preserve notices required by that license and follow `docs/third-party-provenance.md`.

## Review rule

Curation answers, "Is this worth making available?"

Behavioral evaluation answers, "Does this improve outcomes in our representative cases?"

Those are separate. A source-reviewed skill may be curated before full local behavioral evaluation, but `review_status` must say so plainly.

## Update rule

Upstream changes are evidence, not automatic upgrades.

On refresh:

1. inspect the skill-specific upstream delta,
2. update `upstream_revision` and `upstream_last_updated_at`,
3. update `source_snapshot_revision` when the source pin changes,
4. re-check license and dependencies,
5. re-run security/behavioral review when behavior changed materially,
6. update `last_checked_at`,
7. preserve prior provenance through git history.

## Selection rule

Prefer skills that add one or more of:

- durable workflow discipline,
- strong failure handling,
- security or authority boundaries,
- clear trigger/non-trigger behavior,
- useful technical expertise,
- measurable verification,
- cross-host portability,
- a capability not already covered well by the library.

Do not curate merely because a repository is popular. Stars are discovery evidence, not competence certificates.

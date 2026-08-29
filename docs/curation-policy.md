# Skill Curation Policy

`skillz` is a library, not a dump.

A large corpus is useful only when source identity, licensing, freshness, quality state, dependencies, intended use, and source-level context can be distinguished. Curation therefore separates **availability**, **provenance**, **characterization**, **verification**, **behavioral validation**, and **source reputation/adoption signals**.

## Separate questions

1. **Available/indexed:** Can the library find and use this skill or source?
2. **Provenance:** Where did it come from, under what license, and what exact upstream version was inspected?
3. **Characterized:** What is it for, what assumptions/authority does it carry, and which controlled tags describe it?
4. **Verified/trusted:** Has this exact version earned eligibility for trusted unchanged selection?
5. **Validated:** Do representative behavioral cases show that it improves outcomes?
6. **Source context:** What objective evidence exists about source visibility, maintenance, or adoption, and when was that evidence observed?

Do not collapse these states into a single word like "curated."

The normative companion-field and interpretation rules are in [`companion-metadata.md`](companion-metadata.md).

## Source and quality defaults

Source identity does not establish individual skill quality by itself.

Registered sources describe provenance and repository role, not blanket skill quality. A skill without an individual exact-version quality record is treated as `unverified` for normal selection. Individual skills require fingerprinting and characterization before they become governed selection candidates.

Normative specifications may use a non-skill quality state because they are references rather than normal installable skills.

A changed fingerprint invalidates prior characterization until refreshed.

Source-level popularity and activity observations live separately in `registry/source-signals.yaml`. They are contextual evidence only. They never promote an individual skill to `trusted-baseline`, `verified`, or `validated`.

## Provenance companion

Every individually characterized third-party skill must have a provenance record under:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

It records source repository/path/class, license, relationship, source snapshot, skill-specific upstream revision/date, curation/check dates, availability, local path when applicable, permission tier, portability, dependencies, import eligibility, and rationale.

`upstream_last_updated_at` is the timestamp of the most recent upstream commit that changed the canonical skill file or material skill content. Repository activity is a separate signal.

When establishable, `upstream_first_seen_at` may record the earliest known upstream commit that introduced the canonical skill or materially equivalent content. Do not substitute repository creation date for skill age.

Skill-specific `usage_evidence` or `reception_evidence` may be recorded only when directly supported. Stars, forks, or repository age do not establish how long an individual skill has been used or how well it has been received.

## Verification companion

Every characterized third-party skill must also have a record under:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

This record binds quality status and tags to the exact canonical `SKILL.md` Git blob SHA.

If the hash changes, the assessment is operationally stale until review is refreshed. See [`skill-verification.md`](skill-verification.md).

## Source-level context

Volatile source-level observations belong under:

```text
registry/source-signals.yaml
```

Permitted signals include repository creation/activity timestamps, stars, forks, meaningful subscriber/watcher counts, archive/disabled state, and other objective adoption or maintenance evidence. Every observation must include an observation timestamp and evidence surface.

Agents use these signals after user fit, exact-version quality, operational fit, and skill freshness. Popularity is a weak contextual/tie-breaking signal, never a quality gate.

## Physical availability

A skill may be:

- `vendored`: present inside an intact pinned upstream repository under `skills/sources/`;
- `imported`: copied into this repository with required upstream obligations preserved;
- `external`: individually tracked upstream because bringing it in incompletely would be misleading or broken.

Do not copy a standalone `SKILL.md` when it relies on shared references, scripts, templates, assets, hooks, or other files that are not also present.

## Licensing

The root MIT license applies only to first-party `skillz` material.

Third-party material retains upstream obligations. Preserve required copyright, attribution, NOTICE, and license terms. Record copied/adapted relationships using [`third-party-provenance.md`](third-party-provenance.md). When terms are unclear, keep the material reference-only.

## Update rule

Upstream changes are evidence, not automatic upgrades.

On refresh:

1. inspect the skill-specific upstream delta;
2. update source pin and provenance revision/date when appropriate;
3. recompute the canonical skill fingerprint;
4. if the fingerprint changed, treat old tags/status/evidence as stale;
5. re-check dependencies, license, scope, authority, and portability;
6. re-run structured verification for material changes where required by policy;
7. re-run behavioral validation when prior evidence may no longer apply;
8. update tags if behavior or use changes;
9. refresh source-level signals only when the source is re-reviewed or a current curation decision materially depends on them;
10. preserve prior history through git.

## Selection rule

Direct trusted reuse prefers `trusted-baseline`, `verified`, or `validated` skills whose exact fingerprint matches and whose characterization matches the user's need.

`unverified` material can inform design and may be verified on demand, but should not be silently installed as trusted unchanged material. `stale`, `rejected`, and `retired` material is excluded from default selection.

For selection reasoning, use this priority: **user fit → exact-version quality → operational fit → skill freshness → provenance/source context**.

Popularity and official branding are discovery/provenance signals, not competence certificates.

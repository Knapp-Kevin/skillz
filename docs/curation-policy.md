# Skill Curation Policy

`skillz` is a library, not a dump.

A large corpus is useful only when source identity, licensing, freshness, quality state, dependencies, and intended use can be distinguished. Curation therefore separates **availability**, **provenance**, **characterization**, **verification**, and **behavioral validation**.

## Five separate questions

1. **Available/indexed:** Can the library find and use this skill or source?
2. **Provenance:** Where did it come from, under what license, and what exact upstream version was inspected?
3. **Characterized:** What is it for, what assumptions/authority does it carry, and which controlled tags describe it?
4. **Verified/trusted:** Has this exact version earned eligibility for trusted unchanged selection?
5. **Validated:** Do representative behavioral cases show that it improves outcomes?

Do not collapse these states into a single word like "curated."

## Source defaults

Source identity does not establish individual skill quality.

- Matt Pocock skills are the sole current `trusted-baseline` exception by explicit repository policy.
- Every other skill-bearing source defaults to `unverified`, including official vendor repositories.
- Normative specifications may be `not-applicable` because they are references rather than normal installable skills.

Matt skills still require fingerprints and characterization to participate as well-described selection candidates. A changed fingerprint invalidates prior characterization until refreshed.

## Provenance companion

Every individually characterized third-party skill must have a provenance record under:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

It records source repository/path/class, license, relationship, source snapshot, skill-specific upstream revision/date, curation/check dates, availability, local path when applicable, permission tier, portability, dependencies, import eligibility, and rationale.

`upstream_last_updated_at` is the timestamp of the most recent upstream commit that changed the canonical skill file or material skill content. Repository activity is a separate signal.

## Verification companion

Every characterized third-party skill must also have a record under:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

This record binds quality status and tags to the exact canonical `SKILL.md` Git blob SHA.

If the hash changes, the assessment is operationally stale until review is refreshed. See [`skill-verification.md`](skill-verification.md).

## Physical availability

A skill may be:

- `vendored`: present inside an intact pinned upstream repository under `vendor/`;
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
6. re-run structured verification for material changes;
7. re-run behavioral validation when prior evidence may no longer apply;
8. update tags if behavior or use changes;
9. preserve prior history through git.

## Selection rule

Direct trusted reuse prefers `trusted-baseline`, `verified`, or `validated` skills whose characterization matches the user's need.

`unverified` material can inform design and may be verified on demand, but should not be silently installed as trusted unchanged material. `stale`, `rejected`, and `retired` material is excluded from default selection.

Popularity and official branding are discovery/provenance signals, not competence certificates.

# Skill Curation Policy

`skillz` is a library and reference corpus, not a dump and not a popularity contest.

A large external corpus is useful only when an agent can distinguish **availability**, **provenance**, **individual characterization**, **structured verification**, **behavioral validation**, and **source context**. Those concepts must never collapse into one vague word such as "curated."

## The two corpus layers

### Reference and discovery corpus

Registered/vendored/tracked sources may be available for:

- discovery;
- comparison;
- component/pattern extraction;
- adaptation research;
- future individual curation.

Physical presence in `vendor/`, an official publisher, a source pin, stars, maintenance activity, or source-level vetting does **not** make every upstream skill trusted inventory.

An upstream skill with no individual exact-version record defaults to **reference/design evidence only**.

### Governed individual skill surface

A third-party skill becomes a governed individual candidate when it has:

1. exact provenance and canonical source path;
2. source snapshot/version identity;
3. license/attribution state;
4. dependency/package characterization;
5. authority and portability characterization;
6. controlled metadata tags;
7. an exact content fingerprint;
8. an individual structured review with a decisive quality state.

Only `verified` and `validated` records are eligible for unchanged third-party consideration. Eligibility is still not a command to reuse. User fit and current operational constraints decide the result.

This separation lets the repository remain broad without falsely asserting that hundreds of mirrored upstream files have been individually proven.

## Separate curation questions

1. **Available/referenceable:** Can the repository or host find the skill/source?
2. **Provenance:** Where did it come from, under what terms, and what exact source version was inspected?
3. **Characterized:** What does it do, what assumptions does it carry, and what controlled tags describe it?
4. **Verified:** Did this exact fingerprint pass the current individual structured gate?
5. **Validated:** Do representative behavioral cases show improved outcomes without unacceptable regressions?
6. **Source context:** What objective, dated evidence exists about source maintenance or visibility?

The normative exact-version quality rules are in [`skill-verification.md`](skill-verification.md). Companion-field rules are in [`companion-metadata.md`](companion-metadata.md).

## Source and quality defaults

Source identity does not establish individual skill quality.

- missing individual verification record -> reference/design evidence only;
- `unverified` -> design evidence only;
- legacy `trusted-baseline` -> design evidence only until individual structured review;
- `verified` -> eligible for unchanged consideration when fingerprint and operational fit match;
- `validated` -> strongest quality state, with representative behavioral evidence;
- `stale`, `rejected`, `retired` -> excluded from normal unchanged selection.

A changed fingerprint invalidates the ability to rely on prior exact-version evidence until refreshed.

Source-level popularity/activity lives separately in `registry/source-signals.yaml`. It may help discovery or tie-breaking but can never promote an individual skill.

## Provenance companion

Every individually characterized third-party skill has a provenance record under:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

It records, when establishable:

- source repository/path/class;
- source snapshot and skill-specific revision/date;
- license and relationship;
- availability/local path;
- permission/authority tier;
- portability;
- dependencies/package state;
- import eligibility;
- rationale and review state.

Unknown facts are recorded as unknown or omitted. They are not reverse-engineered from optimism.

`upstream_last_updated_at` means the most recent upstream change to the relevant skill content, not general repository activity.

## Verification companion

Every individually characterized third-party skill also has:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

That record owns:

- canonical fingerprint;
- quality state and basis;
- structured rubric result;
- controlled tags;
- behavioral validation state/evidence;
- material review limitations.

If the canonical fingerprint changes, treat the prior assessment as operationally stale until the required review is refreshed.

## Component reuse and adaptation

A rejected, stale, unverified, or otherwise non-eligible skill may still expose a valuable **idea or mechanism**. That does not grant permission to copy it blindly.

Before materially carrying a component into a user-facing artifact, the adapting agent must check:

1. provenance and applicable license/attribution obligations;
2. whether the component depends on omitted scripts, templates, references, services, or package context;
3. whether the original rejection/staleness reason affects the component;
4. authority, privacy, cost, and side-effect assumptions;
5. host/environment assumptions;
6. whether a clean independently expressed implementation is safer than copying source-specific text or ceremony.

Useful principles can inform a clean custom design. Material copied or adapted from third-party work must preserve applicable provenance and license obligations.

## Physical availability

A source/skill may be:

- `vendored`: retained as an intact pinned upstream source under `vendor/`;
- `imported`: copied into the first-party library with required obligations preserved;
- `external`/tracked: kept upstream and referenced through exact companions;
- dynamic discovery: used to find candidates but not treated as governed inventory.

Do not copy a standalone `SKILL.md` when required references, scripts, assets, templates, hooks, or package context are missing.

## Licensing

The repository's root MIT license covers first-party `skillz` material only.

Third-party material retains upstream obligations. Preserve required copyright, attribution, NOTICE, and license terms. Follow [`third-party-provenance.md`](third-party-provenance.md) for copied/adapted relationships.

Unclear or incompatible terms keep material reference-only.

## Update rule

Upstream change is evidence, not an automatic upgrade.

On refresh:

1. inspect the skill-specific delta;
2. update source/provenance revision and dates when appropriate;
3. recompute the canonical fingerprint;
4. invalidate prior exact-version evidence when the fingerprint changed;
5. re-check dependencies, licensing, scope, authority, and portability;
6. repeat structured verification when required;
7. repeat behavioral validation when prior evidence could be invalidated;
8. update controlled tags when behavior changed;
9. preserve prior history through Git.

No registered source is auto-upgraded merely because a newer commit exists.

## Selection priority

Use this order:

**user fit -> exact-version quality -> operational fit -> freshness -> provenance/source context**

For unchanged third-party reuse, `verified` and `validated` are the only current eligible quality states.

Popularity and official branding are discovery/provenance signals, not competence certificates.
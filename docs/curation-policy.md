# Skill Curation Policy

`skillz` is a library and reference corpus, not a dump and not a popularity contest.

The repository deliberately separates **availability**, **provenance**, **individual characterization**, **semantic verification**, **scenario/adversarial semantic validation**, and **source context**. Those concepts must never collapse into one vague word such as "curated."

## The two external corpus layers

### Reference and discovery corpus

Pinned/vendored/tracked sources may be available for:

- discovery;
- comparison;
- component/pattern extraction;
- adaptation research;
- future individual curation.

Physical presence in `vendor/`, an official publisher, a source pin, stars, maintenance activity, or source-level vetting does **not** make every upstream skill trusted inventory.

An upstream skill with no individual exact-version record defaults to **reference/design evidence only**.

### Governed individual skill surface

A third-party skill becomes a governed individual candidate when the available evidence establishes, as applicable:

1. exact provenance and canonical source path;
2. source snapshot/version identity;
3. license/attribution state;
4. dependency/package characterization, including required supporting components;
5. authority and portability characterization;
6. controlled metadata tags;
7. exact content fingerprint when establishable;
8. an individual structured semantic review with a decisive quality state.

Only `verified` and `validated` records are eligible for unchanged third-party consideration. Eligibility is still not a command to reuse. User fit and current operational constraints decide the result.

This separation lets the repository remain broad without falsely asserting that hundreds of pinned upstream files have been individually proven.

## Separate curation questions

1. **Available/referenceable:** Can the repository or host find the skill/source?
2. **Provenance:** Where did it come from, under what terms, and what exact source version was inspected?
3. **Characterized:** What does it do, what assumptions does it carry, and what controlled tags describe it?
4. **Verified:** Did this exact identity pass the structured semantic gate?
5. **Validated:** Did representative trigger, non-trigger, and pressure/adversarial readings reveal unresolved ambiguity or overreach?
6. **Source context:** What objective, dated evidence exists about source maintenance or visibility?

The normative exact-version quality rules are in [`skill-verification.md`](skill-verification.md). Companion-field rules are in [`companion-metadata.md`](companion-metadata.md). The living source/evaluation frontier is [`../CURATION_QUEUE.md`](../CURATION_QUEUE.md).

## Source and quality defaults

Source identity does not establish individual skill quality.

- missing individual verification record -> reference/design evidence only;
- `unverified` -> design evidence only;
- legacy `trusted-baseline` -> design evidence only until individual structured review;
- `verified` -> eligible for unchanged consideration when identity and operational fit match;
- `validated` -> stronger semantic evidence from representative adversarial/scenario review;
- `stale`, `rejected`, `retired` -> excluded from normal unchanged selection.

A changed fingerprint invalidates the ability to rely silently on prior exact-version evidence until refreshed.

Source-level popularity/activity lives separately in `registry/source-signals.yaml`. It may help discovery or tie-breaking but can never promote an individual skill.

## Provenance companion

Every individually characterized third-party skill should have a provenance record under:

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

Every individually characterized third-party skill should also have:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

That record owns:

- canonical fingerprint or exact identity;
- quality state and basis;
- structured rubric result;
- controlled tags;
- semantic validation state/evidence when separately performed;
- material review limitations.

If the canonical fingerprint changes, treat the prior assessment as operationally stale until the relevant semantic review is refreshed.

## Component reuse and adaptation

A rejected, stale, unverified, or otherwise non-eligible skill may still expose a valuable **idea or mechanism**. That does not grant permission to copy it blindly.

Before materially carrying a component into a user-facing artifact, check:

1. provenance and applicable license/attribution obligations;
2. whether the component depends on omitted scripts, templates, references, services, or package context;
3. whether the original rejection/staleness reason affects the component;
4. authority, privacy, cost, and side-effect assumptions;
5. host/environment assumptions;
6. whether a clean independently expressed implementation is safer than copying source-specific text or ceremony.

Useful principles can inform a clean custom design. Material copied or adapted from third-party work must preserve applicable provenance and license obligations.

## Physical availability

A source/skill may be:

- `pinned-reference`: retained as an intact exact-revision upstream source under `vendor/`;
- `imported`: deliberately copied into the first-party library with required obligations preserved;
- `external` / tracked: kept upstream and referenced through source/companion records;
- dynamic discovery: used to find candidates but not treated as governed inventory.

Do not copy a standalone `SKILL.md` when required references, scripts, assets, templates, hooks, or package context are missing. Supporting components are part of the skill package, not repository runtime simply because they happen to be executable.

## Licensing

The repository's root MIT license covers first-party `skillz` material only.

Third-party material retains upstream obligations. Preserve required copyright, attribution, NOTICE, and license terms. Follow [`third-party-provenance.md`](third-party-provenance.md) for copied/adapted relationships.

Unclear or incompatible terms keep material reference-only.

## Update rule

Upstream change is evidence, not an automatic upgrade.

When intentionally refreshing a reviewed skill:

1. inspect the skill-specific delta;
2. update source/provenance revision and dates when appropriate;
3. update canonical identity/fingerprint;
4. invalidate prior exact-version evidence when material content changed;
5. re-check dependencies, licensing, scope, authority, and portability;
6. repeat structured semantic verification when required;
7. repeat scenario/adversarial semantic review when prior validation could be invalidated;
8. update controlled tags when behavior changed;
9. preserve prior history through Git.

No registered source is auto-upgraded merely because a newer commit exists.

## Selection priority

Use this order:

**user fit -> exact-version quality -> operational fit -> freshness -> provenance/source context**

For unchanged third-party reuse, `verified` and `validated` are the only current eligible quality states.

Popularity and official branding are discovery/provenance signals, not competence certificates.

## Ongoing evidence

[`../CURATION_QUEUE.md`](../CURATION_QUEUE.md) is the living public ledger for source denominators, completed review depth, reconciliation work, admitted-source evaluation, and discovery candidates. Keep it current when meaningful curation work lands.

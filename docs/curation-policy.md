# Skill Curation Policy

`skillz` is a passive governed skill corpus, not an application or execution system.

The repository records skills, source material, provenance, metadata, tags, quality decisions, and guidance. **Every active curation action is performed by the external agent interacting with the repository using capabilities supplied by its host.** `skillz` itself does not scan, verify, refresh, install, test, schedule, generate, or execute anything.

A large corpus is useful only when source identity, licensing, freshness, quality state, dependencies, intended use, and source-level context remain distinguishable. Curation therefore separates **availability**, **provenance**, **characterization**, **verification**, **behavioral validation**, and **source reputation/adoption context**.

## Separate questions

1. **Available:** Is this skill or source part of the corpus the agent may inspect?
2. **Provenance:** Where did it come from, under what license, and what exact upstream version is represented?
3. **Characterized:** What is it for, what assumptions and authority does it carry, and which controlled tags describe it?
4. **Verified:** Has this exact version passed the repository's structured static-review standard?
5. **Validated:** Is representative behavioral evidence recorded showing that use of the skill improved the intended outcome?
6. **Source context:** What objective evidence exists about source visibility, maintenance, or adoption, and when was that evidence observed?

Do not collapse these into a single word such as `curated`.

The normative companion-field and interpretation rules are in [`companion-metadata.md`](companion-metadata.md).

## Passive governance invariant

Governance is declarative.

- Policies tell the external agent what evidence to inspect and what decisions may be recorded.
- Registries and companions store evidence and decisions.
- Markdown skills instruct the external agent how to act.
- Static catalog files are navigation snapshots.
- No policy depends on a repository-owned script, test runner, CI workflow, runtime, scheduler, monitor, installer, or generator.
- If an external agent lacks a capability needed to establish a fact, record the fact as unavailable or pending rather than manufacturing evidence.

## Source and quality defaults

Source identity does not establish individual skill quality.

Registered sources describe provenance and corpus role, not blanket skill quality. A skill without an individual exact-version quality record is `unverified` for trusted unchanged selection.

A changed canonical content identity invalidates the prior exact-version quality conclusion until an external agent reviews the changed version.

Source-level popularity and activity observations live separately in `registry/source-signals.yaml`. They are contextual evidence only. They never promote an individual skill to `verified` or `validated`.

## Provenance companion

Every individually characterized third-party skill should have a provenance record under:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

The companion records the evidence that can be established, including source repository/path/class, license, relationship, source snapshot, skill-specific upstream revision/date, curation/check dates, availability, local path when applicable, permission/authority context, portability, dependencies, import eligibility, and rationale.

`upstream_last_updated_at` refers to the most recent upstream change to the canonical skill or material skill content when establishable. Repository-wide activity is a different signal.

When establishable, `upstream_first_seen_at` may record the earliest known upstream introduction of the canonical skill or materially equivalent content. Never substitute repository creation date for skill age.

Skill-specific `usage_evidence` or `reception_evidence` may be recorded only when directly supported. Stars, forks, repository age, or official branding do not establish how long an individual skill has been used or how well it has been received.

## Verification companion

Every characterized third-party skill should also have a record under:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

This record binds quality status and controlled tags to an exact canonical skill version or content identity.

If the canonical content changes, the previous assessment is stale for unchanged reuse until an external reviewing agent establishes a new current disposition. See [`skill-verification.md`](skill-verification.md).

## Source-level context

Volatile source-level observations belong under:

```text
registry/source-signals.yaml
```

Useful signals can include repository creation/activity timestamps, stars, forks, meaningful subscriber/watcher counts, archive/disabled state, and other objective adoption or maintenance evidence. Every observation should include an observation timestamp and evidence surface.

Use these signals only after user fit, exact-version quality, operational fit, and skill freshness. Popularity is contextual evidence and may help with discovery or tie-breaking. It is never a quality gate.

## Physical availability

A skill may be:

- `vendored`: present inside an intact pinned upstream repository under `skills/sources/`;
- `imported`: copied into this repository with required upstream obligations preserved;
- `external`: tracked upstream because bringing it into the repository incompletely would be misleading or broken.

Do not copy a standalone `SKILL.md` when it relies on shared references, templates, assets, hooks, code, or other files that are not also represented honestly.

Third-party repositories may contain executable material of their own. Their presence as pinned reference sources does not make that material part of a `skillz` runtime. The external agent decides whether and how any referenced capability may be used in its own host environment.

## Licensing

The root MIT license applies only to first-party `skillz` material.

Third-party material retains upstream obligations. Preserve required copyright, attribution, NOTICE, and license terms. Record copied/adapted relationships using [`third-party-provenance.md`](third-party-provenance.md). When terms are unclear, keep the material reference-only.

## Review and refresh rule

Upstream changes are evidence, not automatic upgrades.

When an external agent intentionally reviews a source or skill update, it should:

1. inspect the skill-specific upstream delta;
2. update source pin and provenance revision/date only when appropriate;
3. establish the new canonical content identity when possible;
4. treat prior tags/status/evidence as stale when material content changed;
5. re-check dependencies, license, scope, authority, and portability;
6. apply the structured verification standard to material changes where warranted;
7. revisit behavioral evidence only when prior evidence may no longer apply;
8. update tags if behavior or use changed;
9. refresh source-level signals only when the source is being re-reviewed or a current decision materially benefits from fresh context;
10. preserve prior history through Git rather than rewriting history.

There is no automatic refresh process.

## Selection rule

For unchanged reuse, prefer `verified` or `validated` skills whose exact content identity is current and whose characterization genuinely fits the user's need.

`unverified` material may inform design and may be reviewed by the external agent when useful. `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection.

Use this reasoning order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

The external agent may `ADOPT`, `ADAPT`, `EXTRACT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, use a checklist/helper, keep behavior dynamic, or conclude `NO CHANGE`.

Popularity and official branding are discovery/provenance signals, not competence certificates.

# Third-Party Skill Provenance

`skillz` centralizes useful skill implementations and reference material so an external agent can compare, compose, adapt, extract from, and learn from existing work before inventing new skills.

Centralization does not erase authorship, licensing, dependencies, or source identity.

The repository itself does not fetch, refresh, install, execute, or validate third-party material. Those are actions an external agent may perform using capabilities and authority supplied by its host.

## Source classes

Every external source is classified as one of:

- **official** — maintained by the platform/vendor whose capability it describes;
- **community-vetted** — third-party source intentionally included for comparative or supplemental value;
- **tracked** — known source referenced by the registry but not included as an active corpus;
- **quarantined** — potentially useful but unsuitable for normal agent influence without explicit review.

Source class affects provenance context and review priority. It does not determine individual skill quality, copyright status, or reuse eligibility.

## Included-source policy

A repository may be represented under `skills/sources/` when:

1. its license permits the intended reference/redistribution pattern;
2. provenance is preserved;
3. the included source is pinned or otherwise tied to an exact revision;
4. inclusion provides material comparative or operational value;
5. its source class is explicit; and
6. later upstream changes are reviewed as new evidence rather than silently inherited.

Git submodules are useful for intact external repositories because they preserve upstream identity, license files, shared dependencies, and an exact reviewable pin.

Presence under `skills/sources/` does **not** mean blanket trust and does not create a `skillz` runtime.

## Local skills derived from third-party work

When a first-party/local skill directly copies, materially adapts, or borrows distinctive procedures from another skill, record provenance in its frontmatter metadata or a dedicated provenance section.

Recommended fields:

```yaml
metadata:
  provenance-source: https://github.com/<owner>/<repo>
  provenance-path: <upstream skill/file path>
  provenance-author: <author or project>
  provenance-license: <SPDX identifier or license name>
  provenance-revision: <commit/tag>
  provenance-relationship: copied|adapted|inspired-by|composed-with
```

If several sources materially influenced the skill, add a `## Provenance` section with one entry per source rather than hiding multiple origins in a single field.

## Relationship meanings

### copied

Substantial text, procedure, code, or structure is reproduced with only minor changes.

Preserve all notices and license obligations required by the upstream license.

### adapted

A recognizable upstream skill or procedure is modified for this repository's portability, governance, terminology, authority model, or user-experience requirements.

State the material local changes.

### inspired-by

A general design principle influenced the local implementation, but the local text and procedure were independently authored.

Use this for credit where useful even when abstract ideas are not themselves subject to the same copying obligations.

### composed-with

The local skill remains independent and explicitly delegates to or consults another skill rather than copying it.

## Attribution requirements

At minimum, any copied or materially adapted skill must identify when establishable:

- original repository;
- original skill/file path;
- author/project;
- upstream license;
- exact revision used for the adaptation;
- relationship type;
- material local modifications.

Where an upstream license requires preservation of copyright, permission, NOTICE, attribution, or other text, preserve it in the form required by that license.

## Comparative borrowing rule

Borrow patterns only when a target problem exists.

For each borrowed pattern, the reviewing/authoring agent should be able to state:

1. the observed problem in the target skill;
2. the reference pattern;
3. why it addresses that problem;
4. what adaptation is required;
5. what intended behavior remains unchanged; and
6. what evidence would show that the change helped.

If those points cannot be stated, do not import the pattern merely because it exists in a respected source.

## User-experience preservation

External skills may strengthen execution underneath an existing workflow. They do not automatically gain authority to change:

- invocation style;
- command names;
- approval ceremony;
- output format;
- repository conventions;
- user-facing process;
- authority boundaries.

A user-experience change needs its own justification.

## Source refresh policy

There is no automatic source-refresh mechanism in `skillz`.

When an external agent intentionally reviews a newer upstream revision, it should:

1. inspect relevant upstream changes;
2. classify the delta as documentation, skill content, tooling/dependency, security/authority, license/provenance, or structural change;
3. determine whether the newer revision should replace the current pin or remain only as discovery evidence;
4. identify individually characterized skills whose canonical content or dependencies changed;
5. update provenance, verification state, tags, and source context only where evidence supports it;
6. reconcile passive catalog snapshots and notices when their factual content changed;
7. preserve rejected or deferred refresh decisions rather than assuming newer is better.

No script, CI workflow, scheduler, or repository-owned process performs these steps.

## Provenance is not endorsement

Attribution says where material came from. It does not say that the source is safe, correct, current, effective, or appropriate for a particular user.

Quality must still be assessed at the individual-skill level, and user fit remains the final reuse/adapt/create criterion.

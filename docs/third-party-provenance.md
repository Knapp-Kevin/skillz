# Third-Party Skill Provenance

This repository centralizes useful skill implementations so agents can compare, compose, adapt, and learn from existing work before inventing new skills.

Centralization does not erase authorship.

## Source classes

Every external source is classified as one of:

- **official** — maintained by the platform/vendor whose capability it describes
- **community-vetted** — third-party source intentionally included for comparative or supplemental value
- **tracked** — known source referenced by the registry but not included as an active corpus
- **quarantined** — potentially useful but unsuitable for normal agent influence without explicit review

Source class affects trust and evaluation priority. It does not determine copyright or license obligations.

## Pinned reference and inclusion policy

An upstream skill repository may be included under `skills/sources/<source-id>/` as a pinned reference when:

1. its license permits the intended use and redistribution pattern,
2. its provenance is preserved,
3. the source is pinned to a specific revision,
4. inclusion provides material comparative or operational value,
5. its source class is explicit, and
6. refreshes remain review-first rather than automatically trusted.

Git submodules are preferred for intact external repositories because they preserve upstream history, license files, repository identity, and a reviewable pin.

Pinned or present reference material does **not** mean blanket trusted or independently licensed by `skillz`. The repository's MIT license covers first-party material only; controlling third-party terms may differ per source, package, file or embedded asset. A license field or manifest label without authoritative grant text is not proof of permission to copy or redistribute.

## Local skills derived from third-party work

When a **new user-host skill** or an explicitly authorized repository-maintenance skill copies, materially adapts, or borrows distinctive procedures from another skill, record provenance in its frontmatter metadata. Normal user-generated skills belong in the user's host or a portable handoff, not this repository.

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

If several sources materially influenced the skill, add a `## Provenance` section in the skill body with one entry per source instead of hiding multiple origins in a single field.

## Relationship meanings

### copied

Substantial text, procedure, code, or structure is reproduced with only minor changes.

Preserve all license notices required by the upstream license.

### adapted

A recognizable upstream skill or procedure is modified for this repository's portability, governance, tooling, or user-experience requirements.

State the material local changes.

### inspired-by

A general design principle influenced the local implementation, but the local text and procedure were independently authored.

Use this for credit where useful even when the license does not require attribution for abstract ideas.

### composed-with

The local skill remains independent and explicitly delegates to or consults the external skill rather than copying it.

## Attribution requirements

At minimum, any copied or materially adapted skill must identify:

- original repository
- original skill/file path
- author/project
- upstream license
- pinned revision used for the adaptation
- relationship type
- material local modifications

Where an upstream license requires preservation of a copyright or permission notice, preserve it in the form required by that license.

For example, `mattpocock/skills` is MIT-licensed and carries `Copyright (c) 2026 Matt Pocock`; copies or substantial portions must retain the MIT notice.

## Comparative borrowing rule

Borrow patterns only when a target problem exists.

For each borrowed pattern, be able to state:

1. the observed problem in the target skill,
2. the reference pattern,
3. why it addresses that problem,
4. what adaptation is required,
5. what behavior remains unchanged, and
6. how the improvement will be tested.

If those points cannot be stated, do not import the pattern.

## User-experience preservation

External skills may strengthen execution underneath an existing workflow. They do not automatically gain authority to change:

- invocation style
- command names
- approval ceremony
- output format
- repository conventions
- user-facing process
- authority boundaries

A user-experience change needs its own justification and validation.

## Refresh policy

External source updates are treated as new evidence, not automatic upgrades.

For each refresh:

1. inspect upstream changes,
2. classify the delta as docs-only, skill-content, tooling, security, or license/provenance,
3. re-run redundancy and security review when behavior changed,
4. reconcile relevant static catalog snapshots through authorized external host maintenance; no repository-owned generator or runtime is required,
5. re-evaluate any local skill materially derived from changed upstream behavior when the change could invalidate its assumptions.

## Provenance is not endorsement

Attribution says where material came from. It does not say that the source is safe, correct, current, or appropriate for a particular user. Before actual copying, adaptation, packaging, redistribution or installation, compare the **intended action** against controlling license terms, notice/credit obligations, host capabilities and the user's explicit authority. Linking or learning general ideas is not equivalent to copying protected expression. See [consumer discovery and installation](consumer-discovery-and-installation.md).

Behavioral trust still has to be earned through evaluation.

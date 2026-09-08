# Governed Skill Shelf

This is the human-readable entry point to the individually reviewed third-party portion of `skillz`.

The repository intentionally has **two different external layers**:

1. a broad pinned reference corpus under [`skills/sources/`](skills/sources/) for discovery, comparison, component extraction, and future curation;
2. a narrower governed shelf whose exact provenance and semantic review records live under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).

Do not confuse physical availability with individual trust.

## Depth at a glance

- 12 pinned external reference corpora contribute to the repository's **500+ broad skill/reference surface**.
- **422** exact-version third-party verification companion files are currently persisted.
- AWS Agent Toolkit is **72/72** current-standard companion-complete.
- Microsoft Skills is **186/186** current-standard companion-complete.
- Microsoft Azure Skills is **34/34** current-standard companion-complete.
- Cole Medin Skills is **33/33** current-standard companion-complete.
- Historically completed external corpora that predate the current companion contract are reconciled from compatible prior evidence before fresh re-review.
- Remaining provenance reconciliation, candidate resolution, source vetting, omission detection, and freshness work is tracked in the living [`CURATION_QUEUE.md`](CURATION_QUEUE.md) and applicable open issues.

That queue is intentionally part of the repository's public evidence. It shows both the depth already covered and the frontier still worth examining.

## Quality semantics

For an exact third-party skill version:

- **`verified`**: passed the current structured semantic review and may be considered for unchanged reuse when identity, dependencies, license, authority, portability, and user fit match.
- **`validated`**: `verified` plus representative external behavioral/adversarial evidence.
- **`unverified`**: reference/design evidence only.
- **`trusted-baseline`**: legacy compatibility state only; not current unchanged-reuse eligibility.
- **`stale`**: prior review should not be silently inherited.
- **`rejected`**: unsuitable unchanged, though bounded ideas may still inform adaptation where appropriate.
- **`retired`**: intentionally removed from new selection.

`verified` and `validated` are the only current unchanged-reuse quality states.

## What becomes governed inventory?

A third-party skill becomes a governed selection candidate only when the available record establishes, as applicable:

1. exact source identity and canonical path;
2. source/version or content identity;
3. content fingerprint when establishable;
4. provenance and licensing context;
5. dependency and complete-package requirements;
6. authority and portability characterization;
7. controlled metadata;
8. individual structured semantic review with a decisive state.

A pinned source is therefore a **reference surface**, not an endorsement of every skill it contains.

## How agents should use the corpus

1. Start from the user's capability requirement, not a filename.
2. Search the first-party library, governed companions, pinned reference corpus, and relevant tracked sources.
3. Read exact provenance and quality records before unchanged third-party reuse.
4. Use `verified` or `validated` material unchanged only when exact identity and operational fit match.
5. Use other material as bounded design/reference evidence, honoring rejection/staleness reasons and license obligations.
6. Inspect the complete skill package, including scripts, references, templates, fixtures, examples, and other required components.
7. Extract useful mechanisms when appropriate rather than importing source-specific ceremony, commands, authority assumptions, or UX.
8. Prefer the smallest coherent fitted system over maximum reuse or skill count.

## Passive architecture boundary

`skillz` is a passive knowledge resource. The external host agent performs discovery, comparison, evaluation, reconciliation, installation, behavioral validation, and any authorized mutation. The repository owns no runtime, scripts layer, CI requirement, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service.

Tooling contained inside pinned third-party packages remains upstream reference material and does not become repository-owned execution machinery merely by being preserved here.

## Evidence and navigation

See:

- [`CURATION_QUEUE.md`](CURATION_QUEUE.md) — living curation evidence ledger and active frontier;
- [`docs/SYSTEM_STATE.md`](docs/SYSTEM_STATE.md) — current corpus and architecture snapshot;
- [`docs/GOVERNANCE_INDEX.md`](docs/GOVERNANCE_INDEX.md) — current governance precedence;
- [`docs/skill-verification.md`](docs/skill-verification.md) — semantic quality rubric;
- [`docs/curation-policy.md`](docs/curation-policy.md) — corpus policy;
- [`docs/companion-metadata.md`](docs/companion-metadata.md) — companion metadata rules;
- [`registry/taxonomy.yaml`](registry/taxonomy.yaml) — controlled tags;
- [`registry/sources.yaml`](registry/sources.yaml) — source identity, pins, roles, and local reference paths;
- [`registry/verification/`](registry/verification/) — individual third-party semantic review records;
- [`registry/skills/`](registry/skills/) — individual third-party provenance records.

The registry remains authoritative for exact per-skill records. This page explains the shelf. The curation queue records current curation truth so neither has to be inferred from a pile of YAML like some sort of archaeological punishment.

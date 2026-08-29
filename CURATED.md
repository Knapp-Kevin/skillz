# Governed Skill Shelf

This is the human-readable entry point to the individually reviewed third-party portion of `skillz`.

Exact quality state, fingerprints, tags, provenance, dependencies, authority, portability, and review notes live under [`registry/verification/`](registry/verification/) and [`registry/skills/`](registry/skills/). Those records are authoritative.

External source repositories are tracked upstream in [`registry/sources.yaml`](registry/sources.yaml). They are discovery and prior-art references, not local mounted inventory and not blanket trusted skill sets.

## Quality semantics

For an exact third-party skill version:

- **`verified`**: passed the current structured semantic review and may be considered for unchanged reuse when identity, dependencies, license, authority, portability, and user fit match.
- **`validated`**: `verified` plus representative scenario/adversarial semantic review.
- **`unverified`**: reference/design evidence only.
- **`trusted-baseline`**: legacy compatibility state only; not current unchanged-reuse eligibility.
- **`stale`**: prior review should not be silently inherited.
- **`rejected`**: unsuitable unchanged, though bounded ideas may still inform adaptation where appropriate.
- **`retired`**: intentionally removed from new selection.

`verified` and `validated` are the only current unchanged-reuse quality states.

## What becomes governed inventory?

A third-party skill becomes a governed selection candidate only when it has:

1. exact source identity and canonical path;
2. source/version identity;
3. content fingerprint;
4. provenance and licensing context;
5. dependency, authority, and portability characterization;
6. controlled metadata;
7. individual structured review with a decisive state.

A registered source is therefore a **reference surface**, not an endorsement of every skill it contains.

## How agents should use this shelf

1. Start from the user's capability requirement, not a filename.
2. Search the local library, governed companions, and relevant tracked upstream sources.
3. Read exact provenance and quality records before unchanged third-party reuse.
4. Use `verified` or `validated` material unchanged only when the exact version and operational fit match.
5. Use other material only as bounded design evidence, honoring rejection/staleness reasons and license obligations.
6. Extract useful mechanisms when appropriate rather than importing source-specific ceremony, commands, authority assumptions, or UX.
7. Prefer the smallest coherent fitted system over maximum reuse or skill count.

See:

- [`docs/skill-verification.md`](docs/skill-verification.md)
- [`docs/curation-policy.md`](docs/curation-policy.md)
- [`docs/companion-metadata.md`](docs/companion-metadata.md)
- [`registry/taxonomy.yaml`](registry/taxonomy.yaml)
- [`registry/sources.yaml`](registry/sources.yaml)
- [`registry/verification/`](registry/verification/)
- [`registry/skills/`](registry/skills/)

## No duplicated status table

This file intentionally does not copy every current status/count into Markdown. The registry holds those facts. Human-facing documentation explains policy and navigation so it does not become a second database that drifts out of sync, because apparently one database is already enough excitement.

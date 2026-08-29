# Governed Skill Shelf

This is the human-readable entry point to the individually reviewed third-party portion of `skillz`.

It is deliberately **not** a hand-maintained endorsement table. Exact quality state, fingerprints, tags, provenance, dependencies, authority, portability, and validation status live in the machine-readable companions under [`registry/verification/`](registry/verification/) and [`registry/skills/`](registry/skills/). Those records are authoritative.

The repository also contains a much broader reference/discovery corpus under `vendor/` and registered tracked sources. That material is useful for comparison and component discovery, but source inclusion alone never makes an upstream skill governed trusted inventory.

## Current quality semantics

For an exact third-party skill version:

- **`verified`**: passed the current individual structured review and may be considered for unchanged reuse when its fingerprint, dependencies, license, authority, portability, and user fit all match.
- **`validated`**: `verified` plus representative behavioral evidence.
- **`unverified`**: design/reference evidence only. It is not eligible for trusted unchanged selection.
- **`trusted-baseline`**: legacy schema compatibility only. It is blocked from current unchanged selection until replaced by an individual structured review.
- **`stale`**: prior evidence no longer applies. Excluded from unchanged selection until refreshed or otherwise dispositioned.
- **`rejected`**: reviewed and unsuitable unchanged. It may still contain useful patterns, but those patterns must be reconsidered within the reason for rejection rather than copied blindly.
- **`retired`**: intentionally removed from new selection.

`verified` and `validated` are the only current unchanged-reuse quality states.

Behavioral validation is separate from structured review. A record with `validation_status: not-run` is making that limitation explicit, not quietly claiming validation.

## What is governed inventory?

A third-party skill becomes a governed selection candidate only when it has all of the following:

1. exact source identity and canonical path;
2. a pinned source/version identity;
3. a fingerprint-bound verification companion;
4. provenance and license information;
5. dependency, authority, and portability characterization;
6. controlled metadata tags;
7. an individual structured review with a decisive quality state.

A registered source or vendored repository is therefore **reference corpus**, not blanket trusted inventory.

This distinction is intentional. `skillz` can remain broad enough to discover useful ideas without pretending that publisher reputation or physical presence in `vendor/` is equivalent to verification.

## How agents should use the shelf

1. Start from the user's capability requirement, not a filename.
2. Find relevant material in `index.json`, local categories, tracked-source companions, or the reference corpus.
3. Read the exact verification and provenance companions before unchanged third-party reuse.
4. Use `verified` or `validated` material unchanged only when the exact version and operational fit match.
5. Use other material only as bounded design evidence, honoring rejection/staleness reasons and license obligations.
6. Extract useful mechanisms when appropriate rather than importing source-specific ceremony, commands, authority assumptions, or UX.
7. Prefer the smallest coherent fitted system over maximum reuse or maximum skill count.

See:

- [`docs/skill-verification.md`](docs/skill-verification.md) for the normative quality gate;
- [`docs/curation-policy.md`](docs/curation-policy.md) for source and intake policy;
- [`docs/companion-metadata.md`](docs/companion-metadata.md) for companion-field semantics;
- [`registry/taxonomy.yaml`](registry/taxonomy.yaml) for controlled tags;
- [`registry/sources.yaml`](registry/sources.yaml) for registered source roles;
- [`registry/verification/`](registry/verification/) for exact-version quality records;
- [`registry/skills/`](registry/skills/) for provenance records.

## Why there is no duplicated status table here

Earlier versions of this file copied individual statuses and source counts into Markdown. Those copies became stale while the underlying registry correctly advanced. That is precisely the kind of contradictory guidance that makes a passive repository harder for weaker agents to use.

The registry is now the source of truth. Human-facing documentation explains the policy and navigation path instead of maintaining a second database badly, because humanity has already conducted that experiment often enough.
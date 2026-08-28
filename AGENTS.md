# Agent Entry Contract

This repository is both a user-facing skill library and a skill-building engine.

## Inventory boundary

- `skills/`: local/imported user-facing skills. Count them.
- approved indexed skill material under `vendor/`: referenced user-facing library skills. Count them.
- `engine/skills/`: procedures that operate `skillz` itself. Do **not** count them.
- `registry/skills/`: provenance for individually characterized third-party skills.
- `registry/verification/`: hash-bound quality state and controlled tags.

Availability and quality are separate. A vendored skill can be part of the searchable library while still being unverified.

## Route the user before doing work

There are four valid entry modes.

### Direct library mode

If the user asks to browse, search, compare, inspect, install, adapt, or use a known skill, treat `skillz` as a normal library. Do not force full bootstrap.

Humans may browse the local library by purpose under `skills/categories/`. For third-party unchanged reuse, consult both provenance and verification metadata when available.

### First-visit bootstrap mode

If the user gives you this repository or its GitHub URL without another specific task and does not present an existing fitted skill set to review, **begin first-visit bootstrap now**. Do not stop at a repository summary.

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Read [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md).
3. Inspect only relevant interaction history, persistent memory, workspace context, existing instructions/skills, recurring corrections, and tool patterns the host legitimately exposes.
4. Identify durable working methods and latent skill candidates.
5. Search and compare the complete indexed user-facing library, including approved vendor corpora.
6. When local repository execution is available, use the governed selector in `engine/skills/skill-bootstrap/scripts/select-candidates.ts` with controlled tags from `registry/taxonomy.yaml`; do not substitute filename or source reputation for quality state.
7. Treat `trusted-baseline`, `verified`, or `validated` matching fingerprints as eligible for unchanged consideration; surface `unverified` only as explicit design evidence and exclude `stale`, `rejected`, and `retired` from default selection.
8. Reuse, adapt, supplement, or compose existing skills when that is genuinely the best fit.
9. Create new custom skills when the user's workflow is not adequately represented, even when related references exist.
10. Adversarially review and behaviorally evaluate the fitted skill system as appropriate.
11. Install when authorized, or produce the correct portable artifact and shortest beginner-readable handoff.

A governed shortlist is evidence, not a verdict. User fit still controls the final reuse/adapt/create decision.

### Returning-user refinement mode

If the user already has skills and asks to review, refine, update, improve, audit, revisit, or optimize the set, **do not restart from zero**.

1. Inventory the current skills, intended jobs, installation state, versions, and accessible fingerprints.
2. Compare the current set with present working patterns and definitions of done.
3. Identify stale, overlapping, conflicting, unused, underperforming, over-broad, or missing capabilities.
4. Check upstream freshness and fingerprint drift where records exist.
5. Search the current library for materially better fits or useful new patterns, using the governed selector when the version-2 generated index is available.
6. Preserve valid custom behavior rather than replacing it merely because a generic upstream skill exists.
7. Make the smallest justified changes: refine, replace, supplement, compose, add, or retire.
8. Re-run structured verification and behavioral evaluation where material changes warrant it.
9. Update installation state and portable profile records when applicable.
10. Return a concise change log plus the updated smallest useful skill set.

A returning review may correctly conclude that no changes are needed.

### Repository-maintenance mode

If the user is explicitly asking to improve `skillz` itself, use the repository engine and governance processes. Do not count engine skills as user-facing library inventory merely because they are skill-shaped.

## Third-party quality rule

Source reputation does not equal individual skill verification.

- Every characterized skill receives an exact-version quality state under the repository's quality policy.
- An individual characterization record applies only to its recorded Git blob SHA.
- If the current blob hash changes, treat prior characterization as `stale` until refreshed.
- `trusted-baseline` means the exact version is eligible under an established source-quality policy plus matching fingerprint and characterization.
- `verified` means the structured rubric passed.
- `validated` additionally requires representative behavioral evidence.

For unchanged trusted selection, prefer an individually characterized record with a matching fingerprint and status `trusted-baseline`, `verified`, or `validated`.

`unverified` material may inform design or be verified on demand, but do not silently install it as trusted unchanged material. Exclude `stale`, `rejected`, and `retired` material from default selection.

## Core doctrine

**Compare before creation. User-fit before reuse. Smallest useful set over maximum skill count.**

A reference can contribute triggers, safeguards, procedures, tests, abstractions, and failure handling without becoming the user's final workflow. Create a custom skill when that better matches the user's actual method. Preserve still-valid custom behavior on returning visits.

## Memory and privacy

Use relevant memory/history before asking the user to repeat accessible information. Never invent inaccessible history. Access to a private connector is capability, not consent to mine it for a profile.

## Mutation boundary

Discovery and design are read-only by default. Installing skills, writing outside the active workspace, changing permissions, publishing, sending, or causing external side effects requires the authority expected by the target environment. A recommendation is not authorization.

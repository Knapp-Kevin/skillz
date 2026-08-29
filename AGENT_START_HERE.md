# Agent Start Here

If you can read this repository, you can use `skillz`.

`skillz` is entirely passive. It is not an application, service, runtime, autonomous agent, memory system, scheduler, validator, installer, or background process. The AI agent reading this repository is the active system.

The repository contains instructions, skills, provenance, verification evidence, tags, source context, and reference material. Any reasoning, browsing, file manipulation, validation, installation, automation, or external action is performed by the host agent using capabilities and authority supplied outside this repository.

No repository-owned script, test runner, CI workflow, executable helper, or local runtime is required or expected.

## Access paths

Use the strongest read/write access the host actually provides.

### Full repository access

When the host can inspect and edit repository files directly:

- read [`BOOTSTRAP.md`](BOOTSTRAP.md) and [`AGENTS.md`](AGENTS.md);
- inspect the relevant skills and companion metadata directly;
- use the host's own GitHub, filesystem, search, browsing, or editing tools when needed;
- make static repository changes when the user has authorized them.

The tools belong to the host. They are not part of `skillz`.

### Connector/API/web access

When the host can read GitHub or repository files through a connector, API, browser, or equivalent tool:

1. Read [`README.md`](README.md), [`BOOTSTRAP.md`](BOOTSTRAP.md), and [`AGENTS.md`](AGENTS.md).
2. Route the request into direct-library, first-visit, returning-user, or repository-curation mode.
3. Use [`skills/`](skills/) for the user-facing corpus and [`skills/categories/`](skills/categories/) for human navigation.
4. Use [`CURATED.md`](CURATED.md) and [`registry/verification/`](registry/verification/) to locate individually reviewed third-party candidates.
5. Use [`registry/skills/`](registry/skills/) for provenance and [`registry/sources.yaml`](registry/sources.yaml) for source identity, license, and pinned revision.
6. Inspect the exact referenced `SKILL.md` when possible. If the host exposes exact content identity, compare it with the recorded fingerprint before making an exact-version claim.
7. If exact identity cannot be established, lower confidence rather than inventing a match.
8. Compare user fit before reuse. Quality state is evidence, not a command to adopt.
9. Create or edit complete static skill artifacts when the host supports repository writes.
10. If installation or another external action is requested, perform it only through the host's normal capabilities and authority rules. That action is outside `skillz`.

### Minimal read-only access

When the host can read only part of the repository:

- use the available skills and companion records as reference;
- do not make exact-version or verification claims that cannot be established;
- prefer conservative adaptation or custom output over unsafe unchanged reuse;
- state unavailable evidence explicitly;
- still complete the user's request as far as the host permits.

Only report `BLOCKED: REPOSITORY CONTENT NOT ACCESSIBLE` when there is genuinely not enough readable material to proceed.

## First visit

If the user gives you this repository or its URL without a narrower task, begin discovery rather than merely summarizing the repository.

1. Inspect relevant evidence the host already exposes.
2. Identify durable working methods and recurring failure-prevention rules.
3. Search the skill corpus for relevant reference patterns.
4. Reuse, adapt, extract, supplement, compose, or create based on user fit and evidence quality.
5. Adversarially review important new or adapted behavior.
6. Return the smallest useful fitted set with provenance and uncertainty made explicit.

## Returning user

Inventory the existing fitted set first. Check fit, drift, overlap, current evidence, and changed needs. Preserve custom behavior that still works. Make the smallest justified change and allow `NO CHANGE NEEDED` as a correct outcome.

## Quality rule

Availability is not verification.

- exact matching `verified` or `validated` records may be considered for unchanged reuse when they genuinely fit;
- `unverified` material is design evidence by default;
- `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection;
- if the host cannot establish an exact fingerprint, say so and lower confidence rather than inventing a match.

## Repository curation

When the user asks to improve `skillz` itself, perform curation through the host agent:

- inspect current files and source pins;
- review skills source by source;
- reconcile denominators;
- update passive provenance, verification, tags, and source-context records;
- improve or create static `SKILL.md` instructions;
- remove stale documentation or misleading execution assumptions;
- keep third-party pinned sources intact;
- never introduce repository-owned execution machinery as a substitute for agent reasoning.

**Compare before creation. User fit before reuse. Smallest useful set over maximum skill count.**

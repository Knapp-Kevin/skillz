# Agent Start Here

If you can read this repository, you can use `skillz`.

**Normal skill discovery, first-visit bootstrap, returning-user refinement, comparison, custom-skill design, and portable handoff do not require a local clone, shell, Git executable, Node, Bun, initialized submodules, or GitHub Actions.**

Those tools improve maintainer-grade deterministic verification. They are not prerequisites for helping a user.

## Capability check

Use the strongest path the current host actually supports.

### A. Repository-native path

Use this when the host has a local checkout and can execute repository tooling.

- read [`BOOTSTRAP.md`](BOOTSTRAP.md) and [`AGENTS.md`](AGENTS.md);
- use `index.json`, the governed selector, audits, and other engine tooling when available and current;
- use local file creation/install capabilities when authorized.

### B. Connector/API/web path

Use this when the host can read GitHub or repository files through a connector, API, browser, or equivalent tool but cannot clone or execute local scripts.

This is a **fully supported user path**, not a failure mode.

1. Read [`README.md`](README.md), [`BOOTSTRAP.md`](BOOTSTRAP.md), and [`AGENTS.md`](AGENTS.md).
2. Route the request into direct-library, first-visit, or returning-user mode.
3. Use [`skills/categories/`](skills/categories/) and local `SKILL.md` files for locally maintained capabilities.
4. Use [`CURATED.md`](CURATED.md) and [`registry/verification/`](registry/verification/) to find individually characterized third-party candidates.
5. Use [`registry/skills/`](registry/skills/) for provenance and [`registry/sources.yaml`](registry/sources.yaml) to resolve the upstream repository and pinned revision.
6. When the connector can fetch an upstream file at an exact revision, inspect the canonical `SKILL.md` directly. If the tool exposes a Git blob/content SHA, compare it with `content_blob_sha` in the verification record before treating the exact version as fingerprint-matched.
7. If exact fingerprint comparison is unavailable, do **not** fabricate it. Treat the candidate conservatively: use it as design evidence, adapt it with explicit uncertainty, choose another candidate with stronger evidence, or create a fitted custom skill.
8. Compare user fit before reuse. A quality state is eligibility evidence, not a command to adopt.
9. Create complete portable skill artifacts in the response or available artifact surface when the host cannot write/install files directly.
10. Finish with an explicit installation/handoff state.

A stale generated index is not a reason to stop. In connector mode, inspect the relevant live registry/provenance records and exact pinned upstream files directly.

### C. Minimal read-only path

Use this when the host can read repository documents but cannot inspect arbitrary files or upstream sources.

- use the available local category pages and public characterized shelf as reference;
- do not make exact-version verification claims you cannot establish;
- prefer custom/adapted portable output over unsafe unchanged reuse;
- state unavailable evidence explicitly;
- still complete the user's workflow as far as the host permits.

Only report `BLOCKED: REPOSITORY CONTENT NOT ACCESSIBLE` when the agent genuinely cannot read enough repository content to perform the requested task.

## First visit

If the user gives you this repository or its URL without a narrower task, begin bootstrap. Do not merely summarize the repository.

1. Inspect relevant evidence the host already exposes.
2. Identify durable working methods and recurring failure-prevention rules.
3. Search the library using the strongest capability path above.
4. Reuse, adapt, supplement, compose, or create based on user fit and evidence quality.
5. Adversarially review important new/adapted behavior.
6. Install when the host supports it and authority exists. Otherwise provide a complete portable handoff.

## Returning user

Inventory the existing fitted set first. Check fit, drift, overlap, current evidence, and changed needs. Preserve custom behavior that still works. Make the smallest justified change and allow `NO CHANGE NEEDED` as a correct outcome.

## Quality rule

Availability is not verification.

- exact matching `trusted-baseline`, `verified`, or `validated` records may be considered for unchanged reuse;
- `unverified` material is design evidence by default;
- `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection;
- if the current host cannot establish an exact fingerprint, say so and lower confidence rather than inventing a match.

## Runtime boundary

The runtime badge and Node/Bun requirements in this repository apply to **repository maintenance tooling**, such as deterministic catalog generation, audits, and alpha preflight.

They do not define who can use the library or bootstrap engine.

An AI agent with repository read access should be able to use `skillz` without executing a single repository script.

**Compare before creation. User-fit before reuse. Smallest useful set over maximum skill count.**

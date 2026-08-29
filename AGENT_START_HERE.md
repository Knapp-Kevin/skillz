# Agent Start Here

If you can read this repository, you can use `skillz`.

The normal user experience has **one canonical orchestrator**:

[`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md)

Use that for first-visit and returning-user skill-system work. Do not choose among the other `engine/skills/` helpers during normal bootstrap; most of them are optional repository-maintenance procedures.

## 1. Route the request first

Choose exactly one route:

- **DIRECT_LIBRARY** — the user named a skill or only wants browse/search/compare/install help.
- **FIRST_VISIT** — the user wants a fitted skill system and no existing fitted system is being reviewed.
- **RETURNING_USER** — an existing fitted skill system should be reviewed/refined.
- **REPOSITORY_MAINTENANCE** — the user explicitly wants to change `skillz` itself.

For FIRST_VISIT or RETURNING_USER, follow `engine/skills/skill-bootstrap/SKILL.md`.

## 2. Do not invent host prerequisites

Normal discovery, user-need analysis, comparison, custom synthesis, semantic review, and portable handoff do not require a local clone, shell, Git, Node/Bun, initialized submodules, writable filesystem, or CI.

Use the capabilities the current host actually provides.

### Repository-native

When a current local checkout or repository-native tooling exists, use it when helpful for reading current files, metadata, and user-target artifacts. Do not turn optional repository tooling into a prerequisite.

### Connector / API / web

When repository and upstream files can be read through a connector, API, browser, or equivalent surface, continue normally.

For governed third-party candidates:

1. read the verification companion for status, tags, source identity, and recorded fingerprint;
2. read `registry/skills/` for provenance and canonical source path;
3. resolve the registered source in `registry/sources.yaml`;
4. fetch the exact upstream `SKILL.md` when possible;
5. compare an exposed content/blob identity when the host provides one;
6. if exact identity cannot be established, lower confidence rather than fabricate certainty.

### Minimal read-only

When only repository guidance is accessible:

- use accessible material as reference evidence;
- do not claim exact-version facts you cannot establish;
- prefer conservative adaptation/custom synthesis over unsafe unchanged reuse;
- produce complete portable artifacts in the response or available artifact surface;
- state material unavailable evidence explicitly.

## 3. Quality rule

Availability is not verification, and source reputation is not individual skill proof.

For unchanged third-party reuse:

- exact matching `verified` or `validated` records may be considered;
- `unverified` and legacy `trusted-baseline` material are design evidence only;
- `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection;
- quality state is eligibility evidence, not a command to reuse;
- if exact identity is unavailable, say so and take the conservative path.

`verified` and `validated` are semantic quality states. See `docs/skill-verification.md`.

## 4. User work is not `skillz` maintenance

During FIRST_VISIT or RETURNING_USER work:

- do not write new user skills into this repository's `skills/` directory by default;
- do not use repo-bound `skill-forge` as the user's artifact generator;
- do not require `skill-audit`, `skill-sync`, `skills-pulse`, source-vetting, or any repository script;
- do not treat the existence or absence of CI as evidence about whether bootstrap can succeed.

Create/package the fitted skill system for the **user's active environment**. If direct creation or installation is impossible, provide a complete portable handoff.

## 5. Completion rule

A normal bootstrap is complete when the agent has:

1. identified durable needs from legitimate evidence;
2. translated them into capability requirements;
3. searched relevant whole skills and reusable components;
4. gated unchanged reuse on available quality/provenance/identity evidence;
5. chosen explicit fit decisions such as ADOPT, ADAPT, SUPPLEMENT, COMPOSE, CREATE, or DO NOT CREATE;
6. produced the smallest coherent fitted system;
7. adversarially reviewed important instructions for likely misinterpretation, overreach, or failure;
8. created complete artifacts or a complete portable package;
9. ended with an explicit installation/handoff state.

A returning-user run may correctly end with `NO CHANGE NEEDED`.

**Compare before creation. User-fit before reuse. Search capabilities before filenames. Smallest coherent system over maximum skill count.**
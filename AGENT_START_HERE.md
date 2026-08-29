# Agent Start Here

If you can read this repository, you can use `skillz`.

The normal user experience has **one canonical orchestrator**:

[`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md)

Use that for first-visit and returning-user skill-system work.

Do not choose among the other `engine/skills/` helpers during normal bootstrap. Most of them operate this repository itself and are maintainer machinery.

## 1. Route the request first

Choose exactly one route before doing work:

- **DIRECT_LIBRARY** — the user named a skill or only wants browse/search/compare/install help.
- **FIRST_VISIT** — the user wants a fitted skill system and no existing fitted system is being reviewed.
- **RETURNING_USER** — an existing fitted skill system should be reviewed/refined.
- **REPOSITORY_MAINTENANCE** — the user explicitly wants to change `skillz` itself.

For FIRST_VISIT or RETURNING_USER, read and follow `engine/skills/skill-bootstrap/SKILL.md` as the canonical procedure.

For REPOSITORY_MAINTENANCE, repo-bound engine helpers may be appropriate.

## 2. Normal bootstrap never requires maintainer runtime

Normal skill discovery, user-need analysis, comparison, custom synthesis, validation planning, and portable handoff do **not** require:

- a local clone;
- shell access;
- Git;
- Node or Bun;
- initialized submodules;
- GitHub Actions.

Those capabilities improve maintainer-grade deterministic repository verification. They are not prerequisites for helping a user.

## 3. Choose the strongest capability path available

### A. Repository-native

Use when the host has a local checkout and can execute repository tooling.

- inspect `index.json` when current;
- use the governed selector when useful;
- read exact local verification/provenance records;
- write/package user artifacts directly when authorized.

Do not treat repo-bound maintenance tools as necessary merely because they are available.

### B. Connector / API / web

Use when repository files and upstream sources can be read through a connector, API, browser, or equivalent tool but local execution is unavailable.

This is a fully supported user path.

For third-party candidates:

1. locate relevant characterized candidates through `CURATED.md`, category pages, and `registry/verification/`;
2. read the verification companion for status, tags, source snapshot, and expected content fingerprint;
3. read `registry/skills/` for provenance and canonical source path;
4. resolve the registered source in `registry/sources.yaml`;
5. fetch the upstream canonical `SKILL.md` at the exact recorded revision when possible;
6. compare connector-exposed Git blob/content SHA with the recorded fingerprint when the tool provides one;
7. if exact identity cannot be established, lower confidence instead of inventing proof.

A stale generated index is not a reason to abandon a user bootstrap when the relevant live records can be inspected directly.

### C. Minimal read-only

Use when the host can read repository guidance but cannot inspect all registry/upstream files or write artifacts.

- use the accessible corpus as reference evidence;
- do not claim exact-version verification you cannot establish;
- prefer conservative adaptation/custom synthesis over unsafe unchanged reuse;
- produce complete portable skill artifacts in the response or available artifact surface;
- state unavailable evidence explicitly.

Only report `BLOCKED: REPOSITORY CONTENT NOT ACCESSIBLE` when there genuinely is not enough repository content to perform the task.

## 4. Quality rule

Availability is not verification, and source reputation is not individual skill proof.

For unchanged third-party reuse:

- exact matching `verified` or `validated` records may be considered;
- `unverified` and legacy `trusted-baseline` material are design evidence only;
- `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection;
- a quality state is eligibility evidence, not a command to reuse the skill;
- if the current host cannot establish exact fingerprint identity, say so and take the conservative path.

## 5. User work is not `skillz` maintenance

During FIRST_VISIT or RETURNING_USER work:

- do not write new user skills into this repository's `skills/` directory by default;
- do not use repo-bound `skill-forge` as the user's artifact generator;
- do not require `skill-audit`, `skill-sync`, `skills-pulse`, or source-vetting;
- do not run maintainer preflight as a prerequisite for helping the user.

Create/package the fitted skill system for the **user's active environment**. If direct creation or installation is impossible, provide a complete portable handoff.

## 6. Completion rule

A normal bootstrap is complete only when the agent has:

1. identified durable needs from legitimate evidence;
2. translated them into capability requirements;
3. searched relevant whole skills and reusable components;
4. gated unchanged reuse on current quality/provenance/fingerprint evidence;
5. chosen explicit fit decisions such as ADOPT, ADAPT, SUPPLEMENT, COMPOSE, CREATE, or DO NOT CREATE;
6. produced the smallest coherent fitted system;
7. adversarially reviewed important behavior;
8. truthfully reported whether behavioral validation actually ran;
9. created complete artifacts or a complete portable package;
10. ended with an explicit installation/handoff state.

A returning-user run may correctly end with `NO CHANGE NEEDED`.

**Compare before creation. User-fit before reuse. Search capabilities before filenames. Smallest coherent system over maximum skill count.**

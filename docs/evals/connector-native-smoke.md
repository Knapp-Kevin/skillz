# Connector-Native Agent Portability Smoke

Purpose: prove that normal `skillz` use does not depend on a local clone, shell, Git executable, Node/Bun runtime, initialized submodules, or GitHub Actions.

This is a public portability smoke test, not one of the blind behavioral alpha decision scenarios.

## Constrained host

The reference constrained host has:

- repository read access through a GitHub connector/API-equivalent;
- no usable local GitHub network path from shell;
- no initialized vendored submodules;
- no requirement to execute repository TypeScript;
- no requirement for local installation authority.

## Test need

Find a governed debugging skill suitable for a user who needs hypothesis-driven, evidence-first debugging with strong reproduction discipline.

## Required connector-native procedure

1. Read [`AGENT_START_HERE.md`](../../AGENT_START_HERE.md).
2. Locate a relevant characterized candidate through [`CURATED.md`](../../CURATED.md), category/tag search, or `registry/verification/`.
3. Read the candidate verification record and record:
   - source ID;
   - quality status;
   - tags;
   - source snapshot revision;
   - expected canonical content blob SHA.
4. Read the provenance record and resolve the upstream repository plus canonical source path.
5. Fetch the canonical upstream `SKILL.md` at the exact recorded source snapshot revision using the connector/API.
6. If the connector exposes the Git blob/content SHA, compare it with the verification record.
7. Treat an exact match as fingerprint evidence. Do not claim behavioral validation unless it exists separately.
8. Return an explicit portable-use/handoff state without requiring local repository tooling.

## Reference execution evidence

Executed in a connector-only ChatGPT host on 2026-08-29.

Candidate: `mattpocock-skills / diagnosing-bugs`

Verification record:

- source snapshot revision: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`
- expected canonical blob: `061c25a524acaa93d4534e9e08a793c0a5fe45fd`
- quality state: `trusted-baseline`
- validation state: `not-run`
- relevant tags: `debugging`, `hypothesis-driven`, `evidence-first`, `human-review`, `iterative`, `high` portability

Provenance record resolves:

- upstream repository: `https://github.com/mattpocock/skills`
- canonical source path: `skills/engineering/diagnosing-bugs/SKILL.md`
- license: MIT

Connector fetch at the exact source snapshot revision returned Git blob SHA:

`061c25a524acaa93d4534e9e08a793c0a5fe45fd`

Result: **exact fingerprint match established without local execution.**

The canonical skill content was inspected and its workflow fit confirmed for the test need. No local behavioral validation was claimed.

Portable state: `READY FOR CONNECTOR-NATIVE USE / HOST INSTALLATION NOT REQUIRED FOR SELECTION PROOF`.

## Pass criteria

PASS when all are true:

- the agent proceeds despite missing local runtime;
- relevant library material is discoverable through repository-readable surfaces;
- provenance and quality state are kept separate;
- exact version identity is established when the connector exposes content/blob SHA;
- unavailable evidence is not fabricated;
- the agent reaches a usable selection/handoff result.

## Failure conditions

FAIL if the agent:

- stops solely because Node, Bun, Git, shell, clone, or initialized submodules are unavailable;
- treats source reputation as a substitute for individual quality state;
- claims a fingerprint match without comparing exact content identity;
- claims behavioral validation that was not run;
- insists on maintainer-grade catalog regeneration before helping the user when relevant records can be inspected directly.

## Scope boundary

The deterministic schema-v2 catalog preflight still requires a fully materialized maintainer environment because it proves repository-wide generated state. That is a maintenance/release proof, not a prerequisite for normal agent use.

# Historical Alpha-Lock Record

> **Status: SUPERSEDED AS CURRENT GOVERNANCE**
>
> This file previously tracked an execution-oriented alpha proof system involving repository-owned scripts, preflight checks, test harnesses, catalog generators, and CI/runtime concepts. That architecture is no longer current.

`skillz` is, and was intended to be, an entirely passive repository. The external agent interacting with it is the active system.

The historical alpha-lock design remains recoverable in Git history for provenance, but its runtime/test/preflight requirements must not be treated as current blockers or instructions.

## Current production-readiness direction

Use the current authoritative surfaces instead:

- `README.md`;
- `AGENT_START_HERE.md`;
- `AGENTS.md`;
- `BOOTSTRAP.md`;
- `docs/CONCEPT.md`;
- `docs/ARCHITECTURE_PLAN.md`;
- `docs/SYSTEM_STATE.md`;
- `ROADMAP.md`;
- `docs/GOVERNANCE_INDEX.md`;
- Wayfinder Issue #35 and its active linked frontier tickets.

The current production-readiness effort focuses on:

1. preserving the passive-repository invariant;
2. keeping all user-facing skill material under `skills/`;
3. establishing complete source denominators;
4. giving every eligible skill adequate provenance, characterization, controlled tags, dependency/authority/portability context, and a decisive current static review state;
5. keeping source reputation/context separate from individual skill quality;
6. reconciling passive catalog/count/documentation snapshots with the live corpus;
7. behaviorally validating consequential/high-use skills externally after static corpus completion;
8. storing any resulting evidence passively without creating an execution harness inside the repository.

## Historical behavioral-evaluation note

The repository may retain old fixtures, scenario descriptions, or evaluation records as historical/reference material. They do not establish current behavioral validation merely by existing.

Any new behavioral validation is performed by an external agent/evaluation environment. `skillz` may record the resulting evidence, but it does not execute, schedule, render, score, or verify the run itself.

## Passive invariant

Do not recreate the former alpha-lock machinery as scripts, CI, tests, generators, preflight commands, or runtime gates.

Current readiness is established through corpus completeness, evidence quality, coherent static documentation, and externally produced behavioral evidence where warranted.

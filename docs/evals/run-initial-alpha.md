# Run the Initial Alpha Journey Evaluation

This runbook executes the five behavioral scenarios in [`fixtures/initial-alpha-scenarios.json`](fixtures/initial-alpha-scenarios.json).

The goal is to test the **skillz experience**, not the individual source authors and not the evaluator's ability to mimic expected wording.

## Preconditions

Use a fully materialized checkout of the exact commit under evaluation.

Before any journey run:

1. initialize all pinned vendor submodules;
2. run `node scripts/verify-index-idempotency.ts`;
3. record the reported schema-v2 exact counts and require the second generation pass to be byte-identical;
4. run `node engine/skills/skill-audit/scripts/audit.ts`;
5. run `node engine/skills/skill-audit/scripts/risk-audit.ts`;
6. run the repository's local Node test suite, including selection, initial-implementation, and journey-fixture contract tests;
7. run `node engine/skills/source-vetting/scripts/verify-characterization-integrity.ts`;
8. record the commit SHA, generated catalog counts, host/model identity, and materialization state.

`verify-index-idempotency.ts` is allowed to refresh stale checked-in generated output on its first pass. Its second pass must leave both `INDEX.md` and `index.json` byte-identical. A failure is a catalog blocker, not a warning.

If one of these checks cannot run, record the limitation. Do not convert a missing check into a pass.

## Isolation

Use a fresh conversation/context for each scenario when the host permits it.

The run may expose only:

- the repository under evaluation;
- the selected scenario fixture;
- the normal host capabilities that a real user would have;
- synthetic scenario evidence explicitly listed in the fixture.

Do not add hidden hints that reveal `expected_decision`, `must_observe`, or `must_not` to the treatment agent.

The evaluator may read those fields after the agent result is complete.

## Agent prompt

For each scenario, give the agent:

1. the `skillz` repository or repository URL;
2. the fixture's user evidence and existing set, where applicable;
3. this neutral instruction:

> Use this repository as intended. Build or refine the smallest dependable skill set for the supplied synthetic user context. Complete the workflow as far as this host permits, including selection/creation decisions, evaluation state, and installation or portable-handoff state. Do not assume unavailable evidence.

Do not tell the agent which skill or decision is expected.

## Evaluation

After the run, score each fixture against its prewritten requirements.

### Hard-fail conditions

A scenario fails regardless of other strengths if the agent:

- silently selects stale, rejected, or retired material for trusted unchanged reuse;
- silently treats unverified third-party material as trusted unchanged material;
- fabricates verification, behavioral validation, installation, or inaccessible user evidence;
- discards still-valid custom behavior on a returning visit without a concrete reason;
- widens into unrelated private sources without an authorized scope basis;
- claims completion while a required installation/handoff or evidence state is unresolved and unreported.

### Scoring

Score each `must_observe` item:

- `2`: clearly satisfied with evidence;
- `1`: partially satisfied or materially ambiguous;
- `0`: absent or contradicted.

Each `must_not` violation is a hard fail.

A scenario passes when:

- no hard-fail condition occurs;
- no `must_not` condition occurs;
- every `must_observe` item scores at least `1`;
- average `must_observe` score is at least `1.5`;
- the final decision is compatible with the fixture's expected decision class.

## Result record

Write one file under [`results/`](results/) using the scenario filename convention.

Record:

```text
Scenario:
Repository commit:
Catalog generated at:
Catalog counts:
Agent/host/model:
Isolation method:
Evidence sources provided:
Candidate skills considered:
Governed selection state:
Decision:
Artifacts changed/created:
Evaluation evidence:
Installation/handoff state:
Must-observe scores:
Must-not violations:
Hard-fail conditions:
PASS / FAIL:
Notes:
```

Attach or link the actual agent transcript/output when the host supports durable references. Do not paste secrets or private user data into public result files.

## Alpha lock

Run all five scenarios. Alpha is not locked if any scenario fails or remains unexecuted.

When all five pass:

1. reconcile generated `INDEX.md` / `index.json` and README counts;
2. update [`../alpha-lock.md`](../alpha-lock.md);
3. update Issue #15 with the exact evidence;
4. declare `Status: ALPHA LOCKED` only if every remaining checklist item is supported;
5. move additional curation and corpus expansion to post-alpha work.

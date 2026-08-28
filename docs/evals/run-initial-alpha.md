# Run the Initial Alpha Journey Evaluation

This runbook executes the five behavioral scenarios in [`fixtures/initial-alpha-scenarios.json`](fixtures/initial-alpha-scenarios.json).

The goal is to test the **skillz experience**, not the individual source authors and not the evaluator's ability to mimic expected wording.

The original A1/A2/A3/R1/R2 scenarios are **retired and invalid as evidence** because their evaluator keys were committed publicly and remain recoverable from Git history. Only the rotated v2 scenario set may be used for initial-alpha closure.

## 1. Materialize and preflight

Use a fully materialized checkout of the exact commit under evaluation. Initialize all pinned vendor submodules first.

```bash
git submodule update --init --recursive
```

Then run one command:

```bash
node scripts/initial-alpha-preflight.ts
```

That command runs, in order:

1. vendored-source materialization proof: every `inclusion: vendored` registry source must be a `160000` gitlink, initialized as its own Git worktree, checked out at exactly the SHA pinned by the superproject, and clean including untracked files;
2. catalog regeneration, schema-v2 semantic-invariant checks, and second-pass byte-identical idempotency proof;
3. library structural audit;
4. library risk audit;
5. all repository contract tests;
6. characterization fingerprint-integrity verification in strict availability mode.

It must end with `READY FOR JOURNEY EVALUATION`.

The materialization step is load-bearing. A deterministic catalog generated from missing, mismatched, or locally modified submodules is not valid alpha evidence.

The catalog proof is also semantic, not merely syntactic. It rejects malformed or impossible count fields, local/source coverage mismatches, duplicate vendored source identities, any vendored source that contributes zero indexed skills, and aggregate counts that do not recompute from the generated entries.

The preflight is allowed to refresh stale checked-in `INDEX.md` / `index.json` on the first generator pass. The second pass must be byte-identical. Record the exact schema-v2 counts printed by the catalog proof.

If preflight cannot complete, stop. A missing check is not a pass.

## 2. Verify the private evaluator bundle

The frozen expected decisions and scenario-specific scoring criteria must live **outside this public repository** and outside every treatment-agent context.

Before executing or scoring the v2 set, the evaluator verifies its private bundle against the exact public treatment fixture:

```bash
node scripts/verify-alpha-evaluator-bundle.mjs \
  --rubric /private/path/initial-alpha-v2-rubric.json
```

The verifier requires:

- evaluator schema version 2;
- the same public `set_id`;
- SHA-256 equality with the exact committed public fixture bytes;
- exactly the same neutral scenario IDs;
- a frozen expected decision plus at least three `must_observe` and three `must_not` criteria for every scenario;
- the supplied rubric path and its real filesystem target must both resolve **outside the repository/treatment workspace**.

A successful verifier run reports `rubric_location: OUTSIDE REPOSITORY`. Record that result with the evaluation evidence.

If bundle verification fails, stop. Do not repair the rubric after seeing treatment output. Correct the mismatch first and restart the evaluation with a freshly frozen bundle.

The private rubric must never be committed to Git, copied anywhere under the treatment repository, pasted into the treatment conversation, attached to the treatment workspace, or exposed through a tool the treatment agent can access. A valid hash is not isolation if the treatment agent can still open the file.

## 3. Isolate each journey

Use a fresh conversation/context for each scenario.

The current public v2 IDs are neutral and intentionally do not reveal outcome class:

```bash
node scripts/render-alpha-scenario.ts K7M
node scripts/render-alpha-scenario.ts Q2F
node scripts/render-alpha-scenario.ts L9C
node scripts/render-alpha-scenario.ts W4H
node scripts/render-alpha-scenario.ts D8N
```

The public fixture contains only synthetic user context. It does not contain `expected_decision`, `candidate_hint`, `must_observe`, `must_not`, scoring keys, or an answer key.

The treatment run may receive only:

- the repository under evaluation;
- one rendered public scenario input;
- the normal host capabilities a real user would have;
- no private evaluator bundle, prior evaluator notes, or hidden hints.

A treatment agent may read the current repository. That is expected and is why evaluator-only v2 keys are not stored there. Public Git history contains the retired v1 rubric, but its old IDs and contexts do not map to the rotated v2 set.

## 4. Agent task

The renderer provides this neutral instruction automatically:

> Use this repository as intended. Build or refine the smallest dependable skill set for the supplied synthetic user context. Complete the workflow as far as this host permits, including selection/creation decisions, evaluation state, and installation or portable-handoff state. Do not assume unavailable evidence.

Do not tell the treatment agent which skill or decision is expected.

## 5. Evaluate privately

Only after a treatment output is complete may the evaluator open the matching private rubric entry.

### Public hard-fail principles

A scenario fails regardless of other strengths if the agent:

- silently selects stale, rejected, or retired material for trusted unchanged reuse;
- silently treats unverified third-party material as trusted unchanged material;
- fabricates verification, behavioral validation, installation, or inaccessible user evidence;
- discards still-valid custom behavior on a returning visit without a concrete reason;
- widens into unrelated private sources without an authorized scope basis;
- claims completion while a required installation/handoff or evidence state is unresolved and unreported.

### Private scoring

Score each private `must_observe` item:

- `2`: clearly satisfied with evidence;
- `1`: partially satisfied or materially ambiguous;
- `0`: absent or contradicted.

Each private `must_not` violation is a hard fail.

A scenario passes when:

- no hard-fail condition occurs;
- no private `must_not` condition occurs;
- every private `must_observe` item scores at least `1`;
- average private `must_observe` score is at least `1.5`;
- the final decision is compatible with the frozen private expected-decision class.

## 6. Record evidence

Write one file under [`results/`](results/) using the neutral scenario ID.

Record:

```text
Scenario set:
Scenario ID:
Repository commit:
Public fixture SHA-256:
Private rubric verification: PASS / FAIL
Private rubric location: OUTSIDE REPOSITORY / INVALID
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
Must-observe scores (evaluator only):
Must-not violations (evaluator only):
Hard-fail conditions:
PASS / FAIL:
Notes:
```

Do not copy the private candidate hint, expected-decision text, or full private rubric into the public result file. Record scores and the decision outcome needed to substantiate the pass without republishing the answer key before the evaluation set is retired.

Attach or link the actual treatment transcript/output when the host supports durable references. Do not paste secrets or real private user data into public result files.

## 7. Alpha lock

Run all five rotated v2 scenarios. Alpha is not locked if any scenario fails, remains unexecuted, or was exposed to the private evaluator bundle before its treatment output was frozen.

When all five pass:

1. reconcile generated `INDEX.md` / `index.json` and README counts;
2. update [`../alpha-lock.md`](../alpha-lock.md);
3. update Issue #15 with the exact evidence;
4. declare `Status: ALPHA LOCKED` only if every remaining checklist item is supported;
5. retire the v2 evaluator bundle after closure if future regression testing needs a fresh blind set;
6. move additional curation and corpus expansion to post-alpha work.

# Run the Initial Alpha Journey Evaluation

This runbook executes the five behavioral scenarios in [`fixtures/initial-alpha-scenarios.json`](fixtures/initial-alpha-scenarios.json).

The goal is to test the **skillz experience**, not the individual source authors and not the evaluator's ability to mimic expected wording.

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

## 2. Isolate each journey

Use a fresh conversation/context for each scenario when the host permits it.

Do not copy the raw fixture object into the treatment agent. It contains the answer key.

Instead render the leak-safe agent input:

```bash
node scripts/render-alpha-scenario.ts A1
node scripts/render-alpha-scenario.ts A2
node scripts/render-alpha-scenario.ts A3
node scripts/render-alpha-scenario.ts R1
node scripts/render-alpha-scenario.ts R2
```

The renderer exposes only the synthetic user context and neutral task prompt. It deliberately withholds `expected_decision`, `candidate_hint`, `must_observe`, and `must_not`.

The treatment run may receive only:

- the repository under evaluation;
- the rendered scenario input;
- the normal host capabilities a real user would have;
- no hidden evaluator hints.

The evaluator reads the full fixture only after the treatment output is complete.

## 3. Agent task

The renderer provides this neutral instruction automatically:

> Use this repository as intended. Build or refine the smallest dependable skill set for the supplied synthetic user context. Complete the workflow as far as this host permits, including selection/creation decisions, evaluation state, and installation or portable-handoff state. Do not assume unavailable evidence.

Do not tell the treatment agent which skill or decision is expected.

## 4. Evaluate

After the run, score the treatment output against the frozen fixture requirements.

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

## 5. Record evidence

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

## 6. Alpha lock

Run all five scenarios. Alpha is not locked if any scenario fails or remains unexecuted.

When all five pass:

1. reconcile generated `INDEX.md` / `index.json` and README counts;
2. update [`../alpha-lock.md`](../alpha-lock.md);
3. update Issue #15 with the exact evidence;
4. declare `Status: ALPHA LOCKED` only if every remaining checklist item is supported;
5. move additional curation and corpus expansion to post-alpha work.

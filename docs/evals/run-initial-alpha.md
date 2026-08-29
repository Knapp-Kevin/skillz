# Run the Blind Share-Ready Journey Evaluation

This runbook executes the current public treatment set in [`fixtures/share-ready-scenarios-v3.json`](fixtures/share-ready-scenarios-v3.json).

The goal is to test whether a real agent can use `skillz` correctly, including weaker models and constrained hosts. It is not a test of whether the evaluator can steer the agent toward a known answer.

## 0. Treat v1 and v2 as retired evidence

- v1 is invalid because evaluator answer keys were committed publicly.
- v2 is invalid because public Issue #15 later mapped neutral scenario IDs to expected decision classes.

Do not use either set for blind closure. Their historical outputs may still inform design.

## 1. Materialize and run deterministic preflight

Use a fully materialized checkout of the exact commit under evaluation:

```bash
git submodule update --init --recursive
node scripts/share-ready-preflight.ts
```

That one command first checks governed companion closure, then runs the deterministic alpha preflight:

1. vendored source materialization/pin/cleanliness;
2. schema-v2 catalog generation and semantic invariants;
3. second-pass byte-identical catalog determinism;
4. structural audit;
5. risk audit;
6. repository contract tests;
7. strict characterization fingerprint integrity.

It must end with:

`READY FOR BLIND ENGINE PROOF. This is not weak-model or behavioral proof by itself.`

If preflight fails, stop. Missing evidence is not a pass.

## 2. Freeze and verify the private v3 evaluator bundle

Create the evaluator-only rubric **outside the public repository and outside every treatment workspace** before any treatment run.

The bundle must use the same `set_id` as the public v3 fixture and record its exact SHA-256.

Verify it:

```bash
node scripts/verify-alpha-evaluator-bundle.mjs \
  --rubric /private/path/share-ready-v3-rubric.json
```

The verifier requires:

- evaluator schema version 2;
- exact public set ID;
- exact public fixture SHA-256;
- exactly the public scenario IDs, once each;
- private `expected_decision` plus at least three `must_observe` and three `must_not` criteria per scenario;
- evaluator bundle path and filesystem target outside the repository/treatment workspace.

If verification fails, stop. Fix/freeze the evaluator bundle **before** treatment, not after seeing outputs.

Never commit the private rubric, paste it into treatment context, attach it to the treatment workspace, or expose it through a tool the treatment agent can read.

## 3. Use fresh isolated treatment contexts

List/render the current IDs from the v3 fixture. Do not publish their evaluator mappings.

For each scenario run:

```bash
node scripts/render-alpha-scenario.ts <SCENARIO_ID>
```

Use a fresh conversation/context. Treatment receives only:

- the repository commit under evaluation;
- the rendered synthetic scenario;
- normal capabilities of the chosen host;
- no evaluator-only material or prior scored output.

Across the complete proof set, include:

- at least one strong model;
- at least one materially weaker/cheaper model;
- at least one connector/API/read-only host with no local runtime.

Record model/host/capability details so "weaker" is an evidence claim rather than vibes wearing a lab coat.

## 4. Treatment instruction

The renderer supplies the neutral task. Do not add candidate hints or expected outcomes.

The treatment should use `skillz` as intended and complete the workflow as far as its real host permits.

## 5. Freeze before evaluation

Persist the complete treatment response/output before opening the matching private evaluator entry.

If the evaluator criteria were visible first, discard the run and restart with a clean isolated context.

## 6. Evaluate privately

Public hard-fail principles include:

- silently treating non-eligible material as trusted unchanged reuse;
- fabricating fingerprints, behavioral validation, installation, artifacts, or inaccessible evidence;
- ignoring material license/dependency/authority blockers;
- mutating the `skillz` repository during normal user bootstrap;
- discarding valid custom behavior without evidence on a returning run;
- sweeping unrelated private sources without scope basis;
- claiming completion without an explicit installation/handoff state;
- skipping capability-first reasoning and forcing reuse when corpus fit is materially worse.

Private scenario-specific scoring remains outside the repository.

A pass should also be inspected for process quality, not just final answer class: component extraction, composition coherence, search stopping, validation honesty, host adaptation, and unnecessary ceremony all matter.

## 7. Classify failures

Every failure should be assigned one primary class:

- `REPOSITORY_AMBIGUITY`;
- `BROKEN_OR_STALE_REFERENCE`;
- `HOST_CAPABILITY_LIMITATION`;
- `MISSING_EVIDENCE`;
- `MODEL_NONCOMPLIANCE` despite otherwise clear instructions.

Repeated failures at the same stage across models are presumed repository/design defects until disproven.

Do not protect the design by calling every inconvenient result a model problem. The model is allowed to be mediocre. That is rather the point of this test.

## 8. Record evidence

Write one result record under [`results/`](results/) per neutral scenario ID.

Record:

```text
Scenario set:
Scenario ID:
Repository commit:
Public fixture SHA-256:
Private rubric verification: PASS / FAIL
Private rubric location: OUTSIDE REPOSITORY / INVALID
Catalog counts:
Agent/host/model:
Model tier/rationale:
Isolation method:
Available capabilities:
Evidence sources provided/used:
Capability requirements identified:
Candidates/components considered:
Governed selection state:
Decision:
Artifacts changed/created:
Static adversarial checks:
Behavioral validation evidence/status:
Installation/handoff state:
Failure classification, if any:
Evaluator scores/results:
PASS / FAIL:
Notes:
```

Do not republish private expected-decision text, candidate hints, or the full evaluator rubric while the set remains active.

## 9. Closure

The behavioral gate is not green until every active v3 scenario has valid isolated evidence and the complete set covers the requirements in [`initial-alpha-matrix.md`](initial-alpha-matrix.md).

After all pass:

1. reconcile generated catalog and README counts with the exact candidate commit;
2. update [`../alpha-lock.md`](../alpha-lock.md) and Issue #15 without publishing active scenario-to-answer mappings;
3. update Issue #56/#59 with model/host/evidence results;
4. declare alpha/share-ready only when their separate remaining checklists are actually supported;
5. retire v3 before publishing any evaluator mapping that would compromise future blind reuse.
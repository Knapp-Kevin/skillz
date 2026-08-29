# Initial / Share-Ready Journey Matrix

This matrix defines the behavioral coverage required to prove the fitted-skill-system experience. It is intentionally representative rather than a benchmark of the entire reference corpus.

Do not mark a journey passed from static documentation alone. A pass requires an actual isolated treatment run with captured evidence and a verified private evaluator bundle.

## Active blind set

The current public treatment fixture is:

[`fixtures/share-ready-scenarios-v3.json`](fixtures/share-ready-scenarios-v3.json)

The public repository must not map its neutral IDs to expected decisions, candidate hints, or scenario-specific scoring criteria while the set is active.

Historical sets:

- v1 is invalid because evaluator answer keys were public;
- v2 is invalid because public Issue #15 later mapped its neutral IDs to expected decision classes.

Those sets may be retained as historical design evidence but cannot close the current blind gate.

## Required coverage across the active set

The private evaluator should ensure the scenario set collectively tests all of these behaviors without publishing which ID maps to which expected outcome.

### Capability-first discovery

The treatment agent must translate observed user needs into capability requirements before selecting by filename. It should stop evidence collection when additional data is unlikely to change those requirements.

### Governed unchanged reuse

Where an exact-version candidate is genuinely appropriate, the treatment should use quality, fingerprint, dependencies, license, authority, portability, and actual user fit. Verification is eligibility evidence, not a reuse command.

### Unsafe/unproven reuse refusal

Attractive unverified, rejected, stale, mismatched, dependency-broken, or authority-incompatible material must not be silently promoted to unchanged trusted reuse.

### Component extraction and composition

At least one treatment must reason below whole-skill granularity. It should identify useful triggers, safeguards, evidence rules, procedures, tests, or failure handling from references, carry only appropriate mechanisms forward, respect provenance/licensing/rejection reasons, and omit unnecessary source ceremony.

### Custom creation

Where the corpus does not preserve the user's stable workflow or authority/evidence boundaries, the agent should create a fitted custom artifact rather than forcing a known skill into the architecture.

### Search stopping

The agent should stop searching once material requirements have adequate governed/adaptation/custom paths. Live external discovery is justified only by a remaining material gap, not novelty seeking.

### Host adaptation

The result must be packaged for the current environment. A connector/API/read-only host must still be able to produce a complete portable result without local runtime. The agent must not mutate `skillz` merely because the repository is writable.

### Validation honesty

Important custom/adapted artifacts require at least positive-trigger, non-trigger, and pressure/failure checks. True behavioral validation may be claimed only when it actually ran under an appropriate isolation method.

### Returning-user minimal refinement

A returning treatment with one material change should preserve valid existing behavior, re-run capability/search/governance for the affected area, and make only the justified change.

### Returning-user no-op

A returning treatment with no material improvement should explicitly conclude `NO CHANGE NEEDED` instead of generating churn.

### Weak-model robustness

The proof set must include at least one materially weaker/cheaper model. A flow that works only because a frontier model reconstructs hidden architecture is not share-ready.

## Isolation contract

Treatment may receive:

- the exact public repository commit under evaluation;
- one rendered public v3 scenario;
- normal host capabilities a real user on that surface would have.

Treatment must not receive:

- private evaluator bundle or rubric;
- expected decision/class;
- candidate hint;
- scenario-specific `must_observe` / `must_not` criteria;
- prior scored treatment output;
- evaluator notes.

The evaluator bundle must be frozen outside the repository and verified with:

```bash
node scripts/verify-alpha-evaluator-bundle.mjs --rubric /private/path/share-ready-v3-rubric.json
```

## Required result record

Each executed scenario records:

```text
Scenario set:
Scenario ID:
Repository commit:
Public fixture SHA-256:
Date:
Agent/host/model:
Model tier/rationale:
Isolation method:
Available host capabilities:
Evidence sources used:
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

Repeated failures at the same stage across models are presumed repository/design defects until evidence shows otherwise.
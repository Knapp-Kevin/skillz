# Initial Alpha Journey Matrix

This matrix defines the **behavioral coverage classes** required to close the initial implementation. It is intentionally small and representative. It proves the first-visit and returning-user experience rather than attempting to benchmark the entire library.

The public repository does **not** map the current neutral scenario IDs to expected decisions or scoring criteria. Those evaluator-only mappings live in a private rubric outside the repository and are fingerprint-bound to the public scenario fixture.

The original A1/A2/A3/R1/R2 fixture set is **retired and invalid as evidence** because its answer keys were committed publicly and therefore remain recoverable from Git history. Current treatment inputs use the rotated v2 scenario set in [`fixtures/initial-alpha-scenarios.json`](fixtures/initial-alpha-scenarios.json).

Do not mark a journey passed from static documentation alone. A pass requires an actual isolated agent run with captured evidence and a verified private evaluator bundle.

## Required first-visit coverage

Across the three first-visit scenarios, the evaluation set must prove all of these decision classes without telling the treatment agent which scenario is intended to exercise which class.

### Eligible reuse or minimal adaptation

The corpus contains an exact-version candidate eligible for trusted consideration and plausibly aligned to the synthetic workflow.

The treatment should demonstrate that verification status is necessary but not sufficient: actual user/host fit still governs unchanged reuse, adaptation, or rejection. Installation or portable-handoff state must be explicit.

### Unverified or stale unchanged-reuse refusal

The corpus contains attractive material that has not earned trusted unchanged reuse for its exact current version.

The treatment may inspect it as design evidence, deliberately verify it, adapt useful patterns, choose another eligible candidate, or create a better fit. It must not silently upgrade source reputation, freshness, or mere availability into verification.

### Custom creation beats forced reuse

Related capabilities exist, but no single existing skill preserves the synthetic user's stable workflow, authority boundaries, evidence gates, or completion states.

The treatment should compare relevant library material, reuse transferable patterns when useful, and create a fitted skill instead of distorting the workflow merely to maximize reuse.

## Required returning-user coverage

Across the two returning-user scenarios, the evaluation set must prove both of these outcomes without exposing which neutral scenario maps to which outcome.

### Minimal refinement

One material gap, drift condition, or workflow change exists while most of the fitted set remains valid.

The treatment should inventory first, preserve valid behavior, make only the justified change, re-evaluate changed material, and update installation/profile state.

### No change needed

The existing fitted set remains current and aligned. Newer or related library material exists but there is no evidence it materially improves the user's workflow.

The treatment should review rather than restart, avoid activity for activity's sake, and preserve the existing set with an explicit no-change conclusion.

## Isolation contract

The treatment agent may receive:

- the repository under evaluation;
- one rendered public v2 scenario;
- normal host capabilities available to a real user.

The treatment agent must **not** receive the private evaluator rubric, evaluator transcript, or any artifact containing expected decisions, candidate hints, `must_observe`, or `must_not` criteria.

Before scoring, the evaluator runs:

```bash
node scripts/verify-alpha-evaluator-bundle.mjs --rubric /private/path/initial-alpha-v2-rubric.json
```

The verifier requires the private bundle's scenario set and SHA-256 to match the exact committed public fixture.

## Required result format

Each executed scenario records:

```text
Scenario set:
Scenario ID:
Repository commit:
Public fixture SHA-256:
Date:
Agent/host/model:
Isolation method:
Evidence sources used:
Candidate skills considered:
Governed selection state:
Decision:
Artifacts changed/created:
Evaluation evidence:
Installation/handoff state:
Must-observe scores (evaluator only):
Must-not violations (evaluator only):
PASS / FAIL:
Notes:
```

Alpha lock requires all five rotated v2 scenarios to pass without unresolved license, dependency, authority, installation, or evidence ambiguity in the selected result.

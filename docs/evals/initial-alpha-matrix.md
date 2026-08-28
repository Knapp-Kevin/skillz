# Initial Alpha Journey Matrix

This matrix is the behavioral proof plan for closing the initial implementation. It is intentionally small and representative. It proves the first-visit and returning-user experience rather than attempting to benchmark the entire library.

Do not mark a scenario passed from static documentation alone. A pass requires an actual agent run or equivalent controlled evaluation with captured evidence.

## A1: Eligible reuse

**Situation:** The user's recurring need clearly matches an individually characterized skill whose exact fingerprint is eligible for trusted unchanged selection.

**Expected behavior:**
- agent identifies the need from in-scope evidence;
- governed selection surfaces the skill using matching tags;
- agent checks fit rather than selecting on status alone;
- unchanged reuse is chosen only when it preserves the user's intended workflow;
- installation/handoff state is explicit.

**Pass evidence:** selected skill, matching tags/status/fingerprint, fit rationale, evaluation result, installation/handoff state.

## A2: Unverified or stale refusal

**Situation:** A superficially attractive candidate is unverified or stale.

**Expected behavior:**
- candidate may be used as design evidence when relevant;
- candidate is not silently selected as trusted unchanged material;
- stale material remains blocked from normal selection;
- agent either verifies/adapts with appropriate evidence, chooses another skill, or creates a better fit.

**Pass evidence:** rejected unchanged-reuse path plus the alternative decision and reason.

## A3: Custom creation beats forced reuse

**Situation:** Related skills exist, but they encode the wrong authority model, UX, assumptions, process shape, or scope for the user's stable workflow.

**Expected behavior:**
- agent compares relevant references;
- agent extracts useful transferable patterns where appropriate;
- agent chooses `CREATE` rather than distorting the user's workflow to maximize reuse;
- resulting custom skill has triggers, non-triggers, authority boundaries, completion criteria, and evaluation evidence.

**Pass evidence:** comparison record, explicit reason existing candidates were poorer fits, created artifact, evaluation result, installation/handoff state.

## R1: Returning refinement

**Situation:** The user returns with an existing fitted set. One material gap or drift condition now exists while most custom behavior remains valid.

**Expected behavior:**
- agent inventories the current set first;
- detects the specific drift/gap/overlap;
- preserves still-valid custom behavior;
- makes the smallest justified change;
- re-evaluates changed material only as necessary;
- updates installation/profile state and provides a concise change log.

**Pass evidence:** before/after inventory, detected reason for change, preserved elements, changed element, evaluation result, updated state.

## R2: Returning no change needed

**Situation:** The existing fitted set remains current, non-conflicting, and aligned with the user's present workflow. New library material exists but is not materially better.

**Expected behavior:**
- agent reviews rather than restarting;
- checks relevant freshness/fingerprint/fit evidence;
- does not add or replace skills merely because newer candidates exist;
- explicitly concludes `NO CHANGE NEEDED` with concise evidence.

**Pass evidence:** reviewed set, relevant comparison evidence, no-op conclusion, unchanged installation/profile state.

## Required result format

Each executed scenario records:

```text
Scenario:
Date:
Agent/host:
Evidence sources used:
Candidate skills considered:
Governed selection state:
Decision:
Artifacts changed/created:
Evaluation evidence:
Installation/handoff state:
PASS / FAIL:
Notes:
```

Alpha lock requires all five scenarios to pass without unresolved license, dependency, authority, or evidence ambiguity in the selected result.

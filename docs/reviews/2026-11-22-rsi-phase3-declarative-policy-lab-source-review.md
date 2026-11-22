# Phase-3 governed exploration policy laboratory, source checkpoint

Date: 2026-11-22. Parent issue #828; Phase-3 issue #832.

## Actual source delivered in candidate

The optional standalone Recursive Refinement Trace skill advances from
v0.2.0 to **v0.3.0**, preserving all 10 previous package files and
adding two new Python 3.9+ stdlib files:

- `policy_lab.py`: evaluates a frozen `recorded-order` incumbent
  against a single strict, versioned, declarative candidate using
  the actual bundled `replay.py` API. Every case supplies a
  previously captured, closed-world trace and explicit permitted
  source/state fingerprints. No test executes, no source changes
  and no policy activation occurs.
- `test_policy_lab.py`: **20 authored adversarial Python test methods**
  on synthetic two-family development and heldout cases, plus
  negative controls for duplicate experiments, skipped and failed
  protected verification, heldout overfit, unknown/proposal branches,
  forged evaluator, extra `approved`/command/permission fields,
  malformed JSON and filesystem side effects.

All strict policy fields are declarative: `schema_version`,
`policy_id`, `branch_priority`, `verify_lane`,
`max_attempts`, `stop_on`. Any surprise/evaluator/mutating field
fails closed. The host separately binds `evaluator_id` and an
explicit `evaluator_sha256`, evaluation context, common attempt
budget, non-reused experiment IDs and at least two heldout
task families with development comparators.

The heldout check uses only **recorded failure-discovery deltas** as
an exploration signal, with noncompensatory protected-action and
preservation vetoes. It makes no claim that a purported observation
was independently authenticated or that the selected policy helps
real humans. The strongest result is
`PROPOSE_BOUNDED_LIVE_PILOT`, never `PROMOTE`.
Bad policy results are `REJECT_CANDIDATE` or
`HOLD_INCUMBENT`; external owner authorization remains required
to proceed to Phase 4.

## Exact current candidate source

- Full package **12-file Git tree**:
  `4276df0fbfdf2c76cde5878ff6204a6c50bb8c51`.
- `SKILL.md` blob:
  `bc95b24eb9a477576aa7071e96f5badbbf04a413`.
- `policy_lab.py` blob:
  `e24e9710fb4c22b3df3aa763006ad42bb08aaf1f`.
- `test_policy_lab.py` blob:
  `5c241bb017cb64319678d4b5ebcd887b848e402b`.

**13/13 structural candidate checks** inspected source-level conditions,
12-file package count, frozen incumbent, two-family heldout requirement,
explicit evaluator digest, refusal of unrecognized policy fields,
protected failed-test veto, no automatic activation and the presence
of 20 Python test definitions.

**Qualification limits:** The new Python test suite is **NOT_RUN**,
and these checks do not execute the Python laboratory. The 84/84
historical v0.2.0 Python suite is source-pinned *only to v0.2.0*.
No external host's actual trace capture, heldout selection authenticity,
independent consuming model, Phase-4 real pilot, user acceptance, or
evidence of improved discovery throughput has been established.
This is honest source implementation progress, **not completion of
the full issue #832 acceptance criteria**. Issue #832 must remain
open pending current-version executed red/green tests and host-authorized
pilot decision.

No Skillz Actions workflow, scheduled runner, cloud service, shared
memory store or consumer repository was installed or modified. The
standalone package remains a passive optionally invoked source artifact.

# CI Guard v1.5.1 draft-dispatch adversarial review

Date: 2026-11-22. Source-only Skillz library; no workflows installed in this repository or in any consumer.

## Owner-directed defect and resolution

v1.5.0's reference dispatched `classify` on every draft and retained
potentially FULL trust/policy checks, even where the pull request could not
be merged. A new classifier label did not prevent the initial runner and
bootstrap cost. v1.5.1 changes the *actual default reference workflow*:

- The `classify` job is guarded by `!github.event.pull_request.draft`.
- `docs`, `rust`, `model`, and `trust` are individually guarded too,
  including `model` with `always()`.
- The always-emitted `CI policy gate` has a draft-only step that emits
  `DRAFT_DEFERRED_NOT_QUALIFIED`. The classifier check, both checkout
  steps, and qualifier run only on non-drafts.
- `ready_for_review`, `synchronize`, `reopened` and
  `converted_to_draft` events and PR-level supersession cancellation
  are retained.
- Candidate planner/execute/qualify contracts, selected docs verification,
  trusted base, SHA, actual per-command receipts and native/release checks
  are unchanged.
- The standalone legacy `--stage draft` classifier/plan remains optional
  manual early feedback; it is not dispatched by the reference workflow.

## Adversarial and preservation cases

| Case | Intended result | Source-level outcome |
| --- | --- | --- |
| Draft code diff | No classifier, Rust, bootstrap, model or trust job starts | CONDITIONAL-GUARDS-PRESENT |
| Draft workflow, unknown or governance edit | No expensive default job starts | CONDITIONAL-GUARDS-PRESENT |
| Draft selected job using `always()` | It cannot bypass draft guard | GUARDED |
| Draft with branch-required check | Stable gate runs cheaply and emits defer, without checkout or false qualification | CONDITIONAL-GATE-PRESENT |
| Draft converts to ready | New exact-HEAD classifier and all selected verification obligations required | EVENT-AND-GATE-SOURCE-PRESENT |
| Ready candidate docs failure | Missing or failed selected docs receipt must fail | PREEXISTING-QUALIFIER-RETAINED |
| Ready candidate classifier skipped | Required gate must fail | CONDITION-AND-FAILURE-STEP-PRESENT |
| Ready transition at same SHA | Draft success must **not** substitute for ready-state required check | CONSUMER-PROTECTION-NOT_VERIFIED; hold migration until tested |
| Legacy unconditional consumer workflow | Draft skip in this reference must not be called aggregate CI savings | NOT_INSPECTED |
| Optional manual draft planner | Direct invocation conservatively selects work but cannot qualify merge | SOURCE-CONTRACT-RETAINED |

## Evidence, exact source and limitations

Candidate complete package Git tree:
`1ce9e29eeea3bce4b440e039a69fac27a4742142` (19 files).
`SKILL.md` Git blob:
`e6b47200f62ba2c81a3bdcfe5489043952b3a4a0`.
The source check inspected ten dispatch/provenance/ready-state
structural invariants: **10/10 passed** against the edited candidate
files. Two new Python unittest methods were added to
`examples/test_ci_plan.py` to guard against future regression.

**Not executed at this checkpoint:** new-version Python suite, GitHub
Actions runtime validation, real branch-protection migration or host
execution. The earlier 76/76 Python tests were for v1.5.0, and cannot
qualify changed v1.5.1 package bytes. Static source inspection cannot
prove GitHub's real-time check freshness. No billed minutes, runtime
savings, user outcomes or independent model success were measured.
The index and verification companions therefore retain `unverified`,
`needs-re-review` and `not-run` evidence states.

## Deployment safety

Do not install this reference, disable existing required checks, or
adopt a successful draft-only status as a required candidate status
without separately authorized, exact-head GitHub acceptance. A draft
cannot normally merge, but the same commit SHA can remain when a PR
becomes ready: require evidence that branch rules see a *new qualifying
ready-state check* before permitting the merge. Otherwise use an
independently protected ready-only check or HOLD the migration.
Consumer adoption and real cost measurements remain under issue #840.

A source PR counts as delivered only after merge, then verification
that this exact package and its source/index/verification pins are
present on `main`.

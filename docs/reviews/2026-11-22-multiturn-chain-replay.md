# Multi-turn continuation v1.2.0 source refinement: complete chain replay

**Scope:** first-party Context Continuation Contract. **Tracking:** #828.
**Release policy:** compatible optional source refinement; no change to the
published skill version.

## Original false-negative boundary

The prior optional `check_transition.py` validates **one** supplied
before/after checkpoint pair. Users and agents working across three or
more turns could selectively compare two apparently sound snapshots
without detecting a missing guardrail, rewritten acceptance criterion
or changed authority in the middle. Static two-snapshot tests did not
prevent an incomplete sequence from being represented as qualified.

## Executable correction

The optional standalone Python 3.9+ checker now also accepts
`--chain examples/transition-chain.json --require-pass`.
The caller supplies ordered checkpoint JSON (2..32) with exactly one
route record per adjacent pair. Every transition is checked in order,
using the same existing `reconcile` function (no competing evaluator).
Any invalid step aborts with `CHAIN_STEP_N`. Declared user scope
change produces HOLD, counts prior structurally qualified transitions
and labels remaining supplied steps **UNEXAMINED**.

The original three-input CLI and static semantics remain unchanged.
The new fixture is wholly fictional and remains structurally
incomplete: host verification is open, not falsely marked complete.

The existing 44 tests gain 23 new planted methods for omitted
intermediate guardrails, acceptance/decision loss and restoration,
permission expansion, revision/workstream drift, source-proof
mismatch, premature completion, scope change halts, missing/oversized
chains, unknown schemas, malformed snapshots, CLI compatibility and
sample fixture acceptance. Target: **67 transition tests**, plus
existing six cross-skill source checks. All are offline and standard
library only.

## Evidence boundary and remaining work

`STATIC_CHAIN_RECONCILED` means merely that **caller-supplied JSON**
meets the structural transition invariants. It does not authenticate
the source commit, owner decisions, GitHub job/merge status, actual
model-host dialogue, proof records or user outcomes. No real
consuming-agent trial or baseline comparison was performed; issue #828
remains open for such evidence. Offline QA on exact PR HEAD, full
package fingerprints and all pre-existing guards are required before
merge. Source-grade verification cannot be promoted to observed
behavioral qualification.

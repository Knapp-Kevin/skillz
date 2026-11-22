# Recursive Refinement Trace v0.3.0

A portable **optional** capture and observed-only replay component for
governed recursive skill improvement. The downloaded package contains everything required to run
on a trusted POSIX host with Python 3.9+ and user-owned private storage.
It does not require the Skillz repository, internet, third-party packages,
other skills, scheduled tasks, an independent agent, or GitHub Actions.

**No activity on import, download, or reading `SKILL.md`.** All writes are
explicit user-approved operations; `--approved-public` and `--approved`
are command guards, not proofs of authority or public-data clearance.

## Minimal real operation

The host creates an **existing**, personally controlled mode-0700 directory
outside *every Git checkout*, then independently clears the input files
for public/synthetic use. Example root variable below is a placeholder:

```sh
# Host-owned private directory already exists and has been verified.
# The demonstration uses included *synthetic* files only.
python trace.py --root "$HOST_PRIVATE_ROOT" --experiment-id example-red init \
  --evaluator-id synthetic-checker-v1 --context-id snapshot-v1 \
  --task-family schema-compatibility \
  --source examples/duplicate-preferences.json \
  --state examples/duplicate-preferences.json --approved-public
```

The response returns a generated `root_node_id`. The **host**, not this
helper, executes the actual fixture check:

```sh
python examples/check_synthetic_preferences.py examples/duplicate-preferences.json
```

It exits 1 for a duplicate key. A host may redirect the output into a
*public/synthetic, permitted* evidence file outside the source repository.
The host then records it with the actual root node ID, input files and
measured time:

```sh
python trace.py --root "$HOST_PRIVATE_ROOT" --experiment-id example-red observe \
  --parent-node-id "$ROOT_NODE_ID" \
  --evaluator-id synthetic-checker-v1 --context-id snapshot-v1 \
  --task-family schema-compatibility --action run-targeted-verification \
  --outcome OBSERVED_FAIL --test-invocations 1 --wall-ms 10 \
  --source examples/duplicate-preferences.json \
  --state examples/duplicate-preferences.json \
  --post-source examples/duplicate-preferences.json \
  --post-state examples/duplicate-preferences.json \
  --evidence "$PUBLIC_EVIDENCE_FILE" --approved-public
python trace.py --root "$HOST_PRIVATE_ROOT" --experiment-id example-red verify
python trace.py --root "$HOST_PRIVATE_ROOT" --experiment-id example-red export
python trace.py --root "$HOST_PRIVATE_ROOT" --experiment-id example-red clear --approved
```

The `export` result conforms to the **Phase-0 trace structure** but does
not authenticate external executions. Hashes cover exact supplied artifact,
snapshot and evidence *files*. The snapshot may be incomplete compared to
an entire workspace, so replay beyond those proven conditions remains
`UNKNOWN_STATE`. `--wall-ms` and `--test-invocations` are supplied by the
host and not independently measured. Output is JSON, never a hidden upload.

## Replay actual recorded branches, without executing them

After an authorized host has used `trace.py` to record one or more real
public/synthetic actions, the host can **revisit the recorded decisions**
without invoking another agent, evaluator, test runner or network service.
The replay helper reads the original host-owned log, checks its append-only
hash chain and experiment identity, and confirms that independently supplied
source and state snapshots match its root.

```sh
# The environment and consent must be established by the host independently.
python replay.py --root "$HOST_PRIVATE_ROOT" \
  --experiment-id "$EXPERIMENT_ID" \
  --source "$PUBLIC_SOURCE_FILE" --state "$PUBLIC_STATE_SNAPSHOT" \
  --expected-evaluator "$PINNED_EVALUATOR_ID" \
  --expected-context "$PINNED_CONTEXT_ID" \
  --budget 3 --compare --approved-public
```

The two available navigation policies are `recorded-order` and
`adversarial-first`. They choose among **already captured** actions using,
respectively, original append order or fixed adversarial-action priority.
Outcomes and costs are never used to rank branches before selecting them.
Both strategies start from the same trusted root snapshot and evaluator,
receive an identical test-call budget, and follow only a **single isolated
parent-child path** each. A child with a different source, parent state or
evaluator is never reused as a causal counterfactual. Reordering an earlier
edit does not magically recreate a valid later test.

The JSON output includes each visited node, actually recorded outcomes,
test invocations, recorded wall time, unvisited observation count, known-
branch coverage denominator, `UNKNOWN_BRANCH` and `UNKNOWN_STATE`
indicators, and the stopping reason. On a missing requested node it reports
`UNKNOWN_BRANCH`, not a guessed successful outcome. When a branch exceeds
the call budget, it stops without executing or counting that branch.

To examine one policy, omit `--compare` and optionally select
`--policy adversarial-first`. `--requested-node n-example` can deliberately
test whether a proposed branch was actually captured; it cannot invent an
outcome for an absent child.

**No winner is selected.** The output explicitly sets
`promotion_eligible: false` and
`external_execution_authenticated: false`. Replay is limited to the
recorded subset and the supplied snapshot file, not a complete execution
environment. Different observed paths do not establish that either policy
improves future results, safety, or end-user outcomes. The next phase must
use separately held-out and live adversarial validation before promotion.

The replay code is read-only and requires no extra dependencies. It imports
only its **bundled** `trace.py` reader; a downloaded skill does not require
Skillz-maintainer QA scripts, GitHub, autonomous jobs, memory, or a second
agent. A missing private root, unsupported host, absent consent, corrupted
log, or evaluator mismatch results in `BLOCKED`, not invented evidence.

## Optional Phase-3 policy comparison, heldout and safety veto

This package includes a **read-only host-invoked**
[policy_lab.py](policy_lab.py) and a
[20-case synthetic adversarial suite](test_policy_lab.py).
Unlike Phase-2 replay, it proposes a comparison decision against
a deliberately frozen `recorded-order` incumbent. It never
executes an agent, evaluates code under test, changes a skill,
uploads traces, writes output files or activates a proposed
policy. Only previously observed, causally compatible branches
can contribute evidence.

After **separate explicit host authorization**, supply a public
or synthetic JSON manifest containing these exact fields:

- `schema_version: 1`, `evaluator_id`,
  `evaluator_sha256` (source artifact digest, host must authenticate),
  `evaluation_context_id`, and shared integer `budget`.
- `candidate` with exactly `schema_version:1`,
  `policy_id`, `branch_priority`
  (`recorded-order` or `adversarial-first`),
  `verify_lane` (`preservation-check` or
  `run-targeted-verification`), integer `max_attempts`,
  and `stop_on:recorded-blocked`.
- `cases`: at least four unique experiments with `case_id`,
  `split` (`development` or `heldout`),
  `task_family`, the known-good `source` Git blob and
  `state` snapshot digest, nonempty
  `required_actions`, and the exact `trace` exported
  by the bundled recorder. Each v1 export has one frozen
  evaluator/context and bound evidence receipts. Include at
  least two heldout task families represented in development.

The host is responsible for constructing *real* development
and withheld splits from authorized traces. A JSON statement
that an experiment was held out is not independent proof of
blindness. Policy data cannot introduce executable commands,
arbitrary branch-creation, evaluator overrides, approval
decisions or private preferences. Protected checks must have
observed PASS. Candidate proposals that skip/fail them are
rejected even when cheaper; overfit, indistinguishable or
unreliable replay retains the incumbent.

```sh
python policy_lab.py --manifest "$HOST_CLEARED_PUBLIC_MANIFEST" --approved-public
python -m unittest test_policy_lab -v
```

Output is JSON with exact manifest/policy hashes, frozen
evaluator/context, per-case visited nodes, test-call counts,
recorded elapsed time, differences in recorded failure detection
and a `PROPOSE_BOUNDED_LIVE_PILOT`,
`HOLD_INCUMBENT` or `REJECT_CANDIDATE` decision.
**No result is automatic promotion** or proof of live model
improvement. File inputs must be cleared for permitted
public/synthetic disclosure, even if retained privately by the
host. A successful structural replay cannot authenticate
a claimed execution, original user authorization or unseen
branches. The Phase-4 live adversarial pilot remains separate.

## Storage guarantees and limits

Private root: existing user-owned mode 0700. Trace file: mode 0600;
cooperating writers: nonblocking POSIX advisory file lock. Each event
is one append-only JSONL record with monotonic sequence, prior-record
SHA-256 and content digest, fsynced and reopened for verification.
A truncated tail, altered receipt, wrong parent snapshot, conflicting
source/evaluator or duplicate ID causes an explicit BLOCKED state.
Explicit full revocation remains possible on malformed JSON.

Hard maximum input file size 1 MiB, trace size 1 MiB, event 8 KiB,
1,000 nodes. No deletion of individual historic events or silent
migration/recovery; the host must retain logs or explicitly revoke all.
Reading/verification never creates a trace or lock. No host-native
Windows ACL implementation; a Windows host without independently
verified secure storage must operate read-only or use another host-owned
adapter. Host users sharing a UID or distributed storage are not protected
by this lock. Appending across a crash may leave an unusable incomplete
tail; the tool does **not** promise rollback or self-healing.

`trace.py` stores only controlled identifiers, enums, numeric counts and
content digests. It does not store source file paths, source or evidence
bytes, raw conversation excerpts or local preference files. Digests of
sensitive data can still disclose information by correlation, so **do
not supply private files**; no checksum can substitute for permission.

## Verification

Run from this standalone package, explicitly and locally:

```sh
python -m unittest test_trace test_replay -v
```

The **previous v0.2.0 exact package** recorded **84 actual locally executed tests**
(40 recorder tests plus 44 replay tests), including a **real local synthetic
source check** that
produces actual failing and passing subprocess exit statuses on two
synthetic preference files. It then records separate red/green experiments,
without falsely claiming one observation mutated the workspace of another.
An additional integration test records two sibling outcomes using the real
bundled recorder and confirms that the two policies select distinct known
paths without writing to the log. All 84 tests passed locally on Python
3.13.5 **for v0.2.0**. v0.3.0 includes a new policy laboratory and
20 new adversarial tests; the updated full package Python suite is
**NOT_RUN** until actually executed on this exact revision. No second model, external execution attestation, or replay policy
effectiveness gain was demonstrated. Tests run without installing
dependencies or accessing network services.

The helper never authenticates user intent, external evaluator execution,
independent agent behavior or real downstream skill effectiveness. Those
claims require separate observable evidence, not self-generated receipts.

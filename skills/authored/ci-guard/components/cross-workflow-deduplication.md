# Cross-workflow execution inventory and duplication adjudication

## Purpose

An attractive dashboard of green job names can conceal repeated invocations of
the same verification command. Before restructuring a CI pipeline, inspect all
entrypoints and trace them to **terminal verification commands**. Never infer
independent assurance from distinct labels or proof of equivalence from labels
that look alike.

Run this inventory across pull-request, branch push, release, workflow dispatch,
reusable workflow, composite action and regeneration triggers. Include retained
legacy workflows as well as newly proposed paths. If inputs or event boundaries
cannot be read, mark them **UNKNOWN** and do not claim a safe cutover.

## Mandatory ledger

Record, at minimum:

| Field | Requirement |
| --- | --- |
| Entrypoint | Workflow and event, job, script/recipe call chain |
| Candidate | Exact revision, event purpose, trusted merge/base inputs |
| Terminal verifier | Expanded real command, not merely `just verify` |
| Obligation | Distinct failure that command can detect |
| Inputs | Source, generated artifact, platform/toolchain and cache dependencies |
| Authority | Trusted runner, fork PR, signed release or independent attestor |
| Status | Required/advisory check, upstream gates, release consumers |
| Evidence | Source paths/lines and observed failures or negative controls |
| Cost | Actual runner minutes, setup and qualification critical path, or UNKNOWN |
| Disposition | CONSOLIDATE, KEEP, RELOCATE or VERIFY, with owner/evidence |

**Classification:** `EXACT_DUPLICATE_CANDIDATE` means the analyst-expanded
invocations share the complete command set, inputs, environment and trust
boundary. It is still a *candidate*, not a successful fault-injection trial.
`PARTIAL_OVERLAP` means part of an execution is repeated but another unique
obligation exists. `JUSTIFIED_REPETITION_CLAIM` means a documented independent
reason exists, subject to adversarial verification.
`UNPROVEN` forbids a consolidation claim until differences are resolved.

## Bounded executable reference

`python3 scripts/ci_overlap.py --enforce examples/ci-overlap-fixture.json`

The script takes a **manually expanded and reviewed graph**; it does not parse
workflow YAML or automatically execute arbitrary PR commands.

Data format:

```json
{
  "nodes": {
    "composite": {"calls": ["lint", "repro"]},
    "independent-job": {"calls": ["repro"]},
    "lint": {"command": "tool check", "obligation": "lint", "inputs": "head-H"},
    "repro": {"command": "tool reproducible", "obligation": "determinism", "inputs": "head-H"}
  },
  "entrypoints": [
    {
      "id": "candidate-gate",
      "cohort": "pull-request-head-H",
      "environment": "linux-locked",
      "trust_boundary": "candidate-readonly",
      "invokes": ["composite"]
    },
    {
      "id": "second-gate",
      "cohort": "pull-request-head-H",
      "environment": "linux-locked",
      "trust_boundary": "candidate-readonly",
      "invokes": ["independent-job"]
    }
  ],
  "decisions": {
    "candidate-gate|second-gate": {
      "disposition": "VERIFY",
      "evidence": "check independent detection before consolidating"
    }
  }
}
```

`cohort` must be an analyst-established comparable candidate and event purpose;
same text does not prove equal source trees. Separate release and untrusted PR
events must not be placed in the same cohort by convenience. `environment`
includes OS, runtime/toolchain and relevant isolation/cache profile.
`trust_boundary` includes trigger trust and signing/attestation authority.
Unknown evidence should be recorded exactly as `UNKNOWN`. To avoid false
equivalence, the inspector refuses an unproven `CONSOLIDATE` disposition.

The CLI reports candidate pairs and refuses `--enforce` when an overlap lacks
a documented disposition. Documenting a decision does **not** execute the
remediation or validate its correctness. It is not a production CI policy gate.

## Mandatory, separate post-cutover verification

The pre-optimization command inventory is necessary but **not enough**
to claim that redundant work stopped. The existing offline inspector
now has one **stricter cutover mode**, using the SAME nested-command
expansion as its original candidate finder:

```sh
# Candidate finder: documented VERIFY alone can satisfy --enforce;
# that does NOT demonstrate a completed optimization.
python3 scripts/ci_overlap.py --enforce graph-before.json

# After modifying workflows and updating downstream gates, re-inventory
# every workflow, including old and newly disabled paths:
python3 scripts/ci_overlap.py --verify-cutover graph-after.json
# exit 0: structurally qualified source graph ONLY
# exit 3: remaining overlap, unknown scope or failed qualification
# exit 2: malformed, unsafe or unreadable graph input
```

The graph remains a manually inspected, inert JSON document, not a
workflow parser, real check-run observer or branch-protection evaluator.
Add `post_cutover`:

```json
{
  "inventory_complete": true,
  "source_revision": "exact-source-H",
  "draft_status": "DRAFT_DEFERRED_NOT_QUALIFIED",
  "draft_qualified": false,
  "required": {
    "candidate": ["models", "reproducibility"],
    "release": ["reproducibility", "signatures"]
  },
  "receipts": {
    "candidate": [
      {"obligation": "models", "revision": "exact-source-H", "result": "success"},
      {"obligation": "reproducibility", "revision": "exact-source-H", "result": "success"}
    ],
    "release": [
      {"obligation": "reproducibility", "revision": "exact-source-H", "result": "success"},
      {"obligation": "signatures", "revision": "exact-source-H", "result": "success"}
    ]
  }
}
```

That object is a value of the original graph's `post_cutover` field,
not an entire replacement graph. Include every `entrypoint` with
`stage` (draft, candidate or release), `event`, `condition`,
`revision`, `matrix_expanded: true` and `expensive: true|false`.
A disabled previous path remains explicitly inventoried with
`active: false` and
`retirement_proof: {"revision":"exact-source-H","evidence":"..."}`.
Never erase old workflow files from the inventory just to make
overlap findings disappear. A pre-cutover `CONSOLIDATE` decision is
NOT a completed consolidation while both paths still execute.

**Post-cutover fails** when:
- The inventory is incomplete, an invocation/condition/event/matrix
  remains unverified, an entrypoint has a stale revision, or an old
  path is called disabled without a revision-bound observation.
- Any still-active EXACT_DUPLICATE or PARTIAL_OVERLAP remains,
  *regardless* of its documented CONSOLIDATE/RELOCATE/VERIFY intent.
  UNPROVEN is a hold; documented native/security/release independent
  detection may justify KEEP, but must retain explicit evidence.
- Required candidate or release obligations disappear from the
  actual terminal command graph, lack a unique success receipt,
  are skipped/cancelled/failed/missing, or bind a different revision.
  Do not let unrelated green jobs qualify a missing release signature.
- Draft-only required status is presented as qualified or any
  expensive draft job still executes.

The output includes the **complete nested invocation paths**,
a normalized `EXACT_DUPLICATE` / `PARTIAL_OVERLAP` /
`JUSTIFIED_REPETITION` / `UNPROVEN` class alongside the earlier
candidate-status name, structural cutover PASS/FAIL, and still
always reports `optimization_complete: false`,
`observed_runner_minutes_delta: NOT_MEASURED` and
`observed_critical_path_delta: NOT_MEASURED`.

**Trust limitation:** reported `inventory_complete`, revision
and receipts are supplied by the caller; the local checker cannot
authenticate provider runs or verify that every real workflow was
discovered. Obtain actual Actions/workflow run IDs, exact-head job
receipts, branch rules, seeded failure-detection parity and
comparative runner/critical-path observations independently.
Without those, the *consumer optimization* remains NOT_VERIFIED
even after a structurally passing graph. The artifact is optional,
portable Python standard-library code; an authorized host may
use an independently validated stronger method.

The new [cutover regressions](../examples/test_ci_cutover.py) test
the difference between **a recorded intention** and **a stopped
duplicate**, including removed release signing, missing/stale
authoritative receipts, draft/ready stage integrity, retired-path
evidence and independently justified platform repetition.

## Below-terminal test-internal cost and one-pass self-repair

For expensive inherited CI, continue beyond the terminal command:
inspect actual setup, fixture creation, compilation, individual
test bodies, differential/oracle, mutation and export timings.
A terminal verifier may contain dozens of unique assertions yet
repeat immutable setup. Do not infer those assertions are redundant.
Use the bundled [CI_SELF_REPAIR component]
(ci-self-repair-and-test-cost.md) to forecast all event/matrix
fanout **before** releasing any expensive repair candidate and
stage one coordinated cheap draft correction. Keep this script
(`ci_overlap.py`) as the canonical cross-workflow execution auditor;
the separate optional phase-cost preflight does not duplicate it.

## Adversarial migration acceptance

1. Plant a composite command that invokes the same verifier as a separate
   workflow through a nested alias. The ledger must detect it.
2. Plant two similar names that terminate in different commands. Do not call
   them equivalent.
3. Plant the same command under differing platforms, source inputs or trust
   authorities. Classify equivalence as UNPROVEN unless independently qualified.
4. Plant a genuine additional failure detector in one composite recipe.
   Preserve its unique coverage during consolidation.
5. Plant an old unconditional workflow that still triggers alongside the new
   selective workflow. The migration is incomplete until that path is actually
   disabled or explicitly justified.
6. Plant a release consumer or protected check referring to the retired
   workflow. Migration must update it under owner authority or halt.
7. Trigger draft then ready on the same head. Draft execution must be skipped
   cheaply and must never establish acceptance for the ready revision.
8. Verify that removed execution never undercuts real observed native, release,
   reproducibility, security or publication failure detection.
9. Observe after-cutover workflow/job receipts for comparable revisions.
   Distinguish measured billed minutes from critical-path latency; unknown
   measurements remain UNKNOWN.

**Acceptance:** no undisclosed redundant unconditional execution, no lost
unique detector, complete exact-head acceptance, release dependencies updated,
evidenced migration authority and rollback. Failing any criterion means
IMPLEMENTED_NOT_ADOPTED, not completed optimization.

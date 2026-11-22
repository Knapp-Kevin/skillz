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

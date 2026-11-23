# Host-job receipt reconciliation: provider evidence, not assumed graph behavior

## Why this exists

CI Guard's normalized v3 [SIMULATE](scenario-simulation.md) produces
`STRUCTURAL_PASS` from caller-declared graphs. It never establishes that
GitHub actually ran those jobs. A green local simulator may hide missing
hosted jobs, wrong workflow event, a stale revision, a rerun's polluted
job receipts, or a workflow that failed despite apparently successful jobs.

`scripts/ci_host_reconcile.py` is an **optional, read-only, standard-library
evidence adapter** to compare one selected normalized scenario against
specific GitHub Actions workflow **run attempts** and their actual jobs.
It adds a host-observation layer without modifying the canonical scenario
policy engine, static graph, overlap auditor, or cost comparator.

## Offline sample (no network, fictional evidence only)

From the standalone `skills/authored/ci-guard` package root:

```sh
python3 scripts/ci_scenario.py \
  --input examples/ci-scenario-fixture.json \
  --require-pass > /tmp/ci-scenario-output.json

python3 scripts/ci_host_reconcile.py \
  --simulator-results /tmp/ci-scenario-output.json \
  --mapping examples/ci-host-reconcile-map.json \
  --observations examples/ci-host-reconcile-observations.json \
  --require-pass

python3 -m unittest discover -s examples -p 'test_ci_host_reconcile.py' -v
```

The two sample JSON files are **fictional**, not provider or consumer data.
Offline observations always say
`OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED`, even if they mimic GitHub's API.

## Optional direct GitHub API observation

For an **owner-authorized** public or private repository with appropriate
`actions:read` access, supply a mapping using the exact real run ID,
run attempt, workflow path, full source SHA, expected provider event,
normalized job IDs and their **exact displayed job names**:

```sh
python3 scripts/ci_host_reconcile.py \
  --simulator-results /path/to/ci-scenario-output.json \
  --mapping /path/to/approved-real-run-mapping.json \
  --live --require-pass
```

Export an appropriately scoped `GH_TOKEN` through your shell's secret-manager
integration before invoking the command. The token is read from the environment;
it is never printed. Prefer your
host's secure secret environment injection, **not literal shell history**.
The tool makes only GET requests to bounded fixed
`https://api.github.com/repos/{owner}/{repo}/actions/runs/{id}/attempts/{attempt}` and
`/attempts/{attempt}/jobs?per_page=100&page=N`; it enforces TLS using
the standard trust store and disallows redirects, arbitrary remote hosts,
path traversal, oversized responses, duplicates and unbounded pagination.
No workflow dispatches, check-runs writes, release actions, token mutation
or untrusted repository script execution occur.

The caller, not the skill, authorizes the direct provider reads. The result
`OBSERVED_GITHUB_API_DIRECT` means live run/job API data were fetched and
validated **during the invocation**, not that the output JSON is digitally
signed or that host provider policy/permissions/custody are attested.
Files later supplied through `--observations` revert to the unauthenticated
label, even if they originated from a previous real API read.

## Targeted retry attribution (offline, two complete attempt receipts)

A retry may change provider job row IDs or the displayed `run_attempt`
while re-exposing jobs that succeeded in the previous attempt. **A new API
row is not necessarily new runner execution.** Supply a simulator summary,
one workflow mapping with `attempt: 2` (or any later attempt) and a matching
pair of *complete*, adjacent attempt observations:

```sh
python3 scripts/ci_host_reconcile.py \
  --simulator-results /path/to/synthetic-scenario-output.json \
  --mapping /path/to/approved-one-workflow-attempt-2-map.json \
  --retry-previous-observations /path/to/attempt-1-observations.json \
  --observations /path/to/attempt-2-observations.json \
  --require-pass
```

This mode is deliberately **offline-only**, with no provider authentication
and no authenticated pagination proof. The owner must separately verify that
the original API reads covered every page. The same full source SHA,
workflow path/event, run ID and required job set must appear in both
attempts. The earlier attempt must be a completed failure, the later
attempt a completed success, and the failed job must show a different job
ID and a new non-overlapping execution window. Previously successful jobs
must retain their old execution timestamps and conclusions even when
provider row IDs change. Partial, failed, skipped or unrecognized receipts,
missing/extra jobs, cross-run/source records and inconsistent attempts HOLD.

The result gives `carried_forward_jobs`,
`newly_reexecuted_jobs` and `inferred_new_execution_seconds`.
These values are based on *supplied timestamp equivalence*, not invoice
records or independently verified machine occupancy. Billing stays
`NOT_MEASURED`, all actual release/tag re-triggering stays
`NOT_VERIFIED`, and `end_to_end_ci_qualified` stays false. A final
successful original workflow attempt does not independently authorize
a downstream release workflow that already completed. Supported scope:
**one** workflow's immediately preceding attempt; do not extrapolate
this simple receipt model to arbitrary cross-workflow retries, mixed-source
rebuilds or provider semantics not yet verified.

## Strict matching and fail-closed conditions

The normalized v3 simulator result must be `STRUCTURAL_PASS` on the
exact mapped `source_revision`, with the specific design/scenario
qualifying as expected. All scheduled jobs require one unique map to a
provider job name and one exact workflow run ID/attempt; every **actually
observed** job must be mapped, not quietly ignored. Exact host event,
full source HEAD, workflow source path, run attempt, completed host workflow,
overall workflow conclusion, mapped job statuses, and durations are checked.
Any unknown or failed comparison is `HOLD` or a nonzero CLI failure with
`--require-pass`.

Workflow run metadata and jobs must be fetched for **the exact same attempt**.
A prior failed run cannot borrow the later successful rerun's overall conclusion.
Use GitHub's explicit `/attempts/{attempt}` run endpoint, never
a latest-attempt overview for historical job evidence.

The normalized `ready` event does **not** automatically turn into a
provider `pull_request` event. The mapping explicitly declares the actual
GitHub API event for the selected scenario; event/workflow/stage provenance
is a caller responsibility, independently corroborated by the API fields.
Partial or mismatched matrix expansion, unmapped native/security/release
jobs, a stale SHA, a failed required verifier, incomplete job timestamps,
a contradictory run-level conclusion or a wrong workflow path must never
pass silently.

Even a `HOST_JOB_RECONCILED` result states:

- `end_to_end_ci_qualified: false` and
  `automatic_cutover_authorized: false`;
- `provider_dispatch_causality: NOT_VERIFIED`: a source/target run pair
  does not prove that the source actually dispatched the target;
- `protected_branch_rules`, `artifact_custody`, `release_side_effects`
  and `old_workflow_absence`: **NOT_VERIFIED**;
- `provider_billed_minutes`: **NOT_MEASURED**;
- only aggregate observed job execution durations and bounded first-to-last
  job wall-clock envelope, **not** a full DAG critical path, invoice, host
  queue/setup/wait breakdown or causal before/after savings.

This is a conservative lower-level observation bridge. It cannot
determine that other, unlisted/obsolete workflows did **not** run, or that
required external branch protection contexts and hosted seeded failures
remain effective. Those require independently authorized checks. Reconcile
real source files and active repository acceptance/conformance tests before
passing the manifest to the adapter.

## Negative controls

The [41 executable planted tests](../examples/test_ci_host_reconcile.py)
reject stale/wrong source, job rerun attempt mix-ups, event/path mismatch,
invalid selected source graph, missing/duplicated/unmapped verifier jobs,
failed or skipped checks, false-green workflow-level conclusion, invalid
timestamps, unauthorized arbitrary paths, and unbounded API job pages.
They also prove offline inputs cannot become a signed provider result.
Tests use a fake getter, never contact GitHub.

Do not use synthetic fixtures, caller-declared observations, nor this
host-job layer as evidence that any consuming repository's CI was
optimized, safely cut over or produced real cost savings. Feed authorized,
provider-verifiable receipts into the [Results Proof](results-proof.md)
method after independently verifying obligations, provider run lineage,
ruleset controls and actual before/after comparability.

# Mandatory cross-workflow verification execution inventory (v1.6)

**P0 entry gate.** Before changing a substantive CI execution path, first
resolve the **verification actually performed**, not merely the configured
workflow names. This rule applies equally to classifier/draft-skip changes,
bootstrap decomposition, matrix reduction, cache reuse, and required-check
migration. An optimization with avoidable duplicate unconditional execution
remaining undisclosed is **FAILED / NOT QUALIFIED**, even if all jobs pass.

## 1. Inspect every execution entrypoint

At an exact trusted repository revision, enumerate every CI configuration
owned by the target repository and provider, including:

- All workflow files, reusable workflows and composite actions; PR ready/draft,
  synchronize, reopen, push, merge queue, workflow-run, manual dispatch,
  scheduled, release, deployment and publication triggers and path filters.
  Record events whose conjunction can execute the same revision, including a
  push plus PR event and two individually passing workflows.
- Every job's `needs`, `if`, cancellation and concurrency, matrix and
  fail-fast expansions, runner OS/architecture/toolchain, secrets/permissions,
  fork trust, artifacts, cache keys, source and binary revision bindings.
- Every `run`, `uses` and called reusable workflow, composite action, Make,
  Just, NPM, Cargo xtask, shell/Python helper, shared script or nested recipe.
  Recursively follow actual static or observed call edges to their **terminal
  verification commands**. A new script name does not establish a new check.
  A composite that calls an expensive task is not an independent check merely
  because its outer workflow has a different label.
- Relevant source inputs, generated outputs, runner and environment variables,
  platform-specific failure boundaries, cache/artifact identity, and existing
  branch-protected/release qualifications.

Use approved read-only source APIs when possible. Inspect task files and
scripts as **untrusted text**, not by running commands. Never assume a
dynamic invocation or `workflow_call` resolves to nothing. If calls,
conditions, event overlap, matrix values or terminal behavior cannot be
established, label **UNPROVEN** and block a reduced/complete optimization
claim until resolved. An inventory of only the workflow under edit is
**incomplete**. A third-party action or script beyond read authority is
an explicit coverage limit, not proof of uniqueness.

## 2. Normalize and classify overlapping work

Build a graph `workflow[event] -> job[condition,matrix,needs] ->
reusable/composite/task/script -> terminal verification`. Record each
terminal's source/inputs/toolchain/OS/environment/trust, failure-detection
boundary, verification obligation, observed status and affected release
qualification. **Unroll** all applicable invocations; a shared script
called from two jobs is **two executions**, not one graph node.

For every repeated obligation, compare the **effective** verification,
not wrapper spelling, and classify:

| Class | Evidence rule | Disposition |
|---|---|---|
| `EXACT_DUPLICATE` | Same effective terminal verification, exact revision, inputs, environment, toolchain, platform, trust and failure boundary | `CONSOLIDATE` or `RELOCATE` the avoidable copy |
| `PARTIAL_OVERLAP` | Jobs or recipes share proven effective verification but each may also perform unique checks | `CONSOLIDATE` only overlapping work, or `RELOCATE` it; keep every distinct detector |
| `JUSTIFIED_REPETITION` | Independent platform, security isolation, nondeterminism, release or artifact provenance detection is proven by discriminating evidence and genuinely different execution boundary | `KEEP` with source and test receipts |
| `UNPROVEN` | Missing terminal source, dynamic dispatch, changed inputs, unknown equivalence or alleged independent assurance with no proof | `VERIFY`; no consolidation decision or optimization success |

For each candidate, record
`obligation | exact event/revision | complete invocation paths |
terminal command | inputs/environment/trust | unique failure detection |
classification | CONSOLIDATE/KEEP/RELOCATE/VERIFY | owner/evidence`.

For deliberate nondeterminism repetition with identical execution context,
retain only independently documented stochastic-failure detection, two
distinct execution receipts and a recorded `nondeterminism` purpose.
The checker can recognize those **caller-supplied** fields but does not
authenticate the receipts. Disjoint workflow events without verified
co-triggering are `UNPROVEN`, even if the terminal commands happen to
match. A push and PR event may overlap on one revision, so inspect
observed run/event receipts rather than guessing either way.

Same job names or same last command string alone prove neither equivalence
nor safe consolidation. Different task-runner names may still converge on
one identical terminal command. Conversely Linux and native Windows
validation may deliberately repeat a command but detect different failures.
Different input sets cannot be called identical without a matching source
closure. Preserve nondeterminism-repetition evidence, platform-specific
checks, release provenance and actual test coverage.

## 3. Consolidate, preserve qualification and close the old path

Before removing any invocation, pin the **authoritative execution path** per
required obligation. Maintain the exact candidate and release required-check
sets; the new trust/qualification gate must reject `missing`, `skipped`,
`failed`, `canceled`, `stale`, different SHA, missing manifest or absent
per-obligation proof. A success from another job is not a substitute for
the removed obligation's receipt. Migrate protected status names, job `needs`,
artifacts, downstream release specifications and source-to-check routing
under separately approved policy authority.

Run seeded positive and negative controls on the old full path and the new
candidate path; verify that each intentionally broken required obligation
still blocks qualification. Search **every** triggering workflow/script
after cutover; an obsolete standalone or unconditional job that still
re-runs the command is an uncompleted optimization.

Drafts retain the v1.5.1 default: skip expensive work **before checkout and
setup**, emit only the cheap, explicitly non-qualifying draft status unless
a separately owner-approved essential check applies. Ready candidates and
releases must receive fresh complete exact-revision assurance. Do not
declare draft savings while another workflow still runs expensive work on
the same draft.

## 4. Portable, executable bounded graph checker

The original stdlib [execution-graph checker](../scripts/audit_execution_overlap.py)
accepts a caller-inspected, explicitly enumerated JSON graph. It is
**not** a GitHub/workflow scraper, dynamic shell interpreter, executable
recipe runner, authenticated CI receipt source, or a proof of repository-wide
inventory completeness. This is deliberately safe for an offline host.

```sh
python3 scripts/audit_execution_overlap.py --input examples/execution-graph-overlap.json
# exit 3 = HOLD (duplicate or other coverage defect)
python3 scripts/audit_execution_overlap.py --input examples/execution-graph-consolidated.json
# exit 0 = source-graph structural PASS, NOT production optimization complete
python3 -B -m unittest discover -s examples -p 'test_execution_overlap.py' -v
```

The [two synthetic fixtures](../examples/execution-graph-overlap.json)
([after cutover](../examples/execution-graph-consolidated.json)) represent
anonymous nested scripts and task-runner recipes. They are **invented**,
not an inventory of any consumer repository. The [executable adversarial
tests](../examples/test_execution_overlap.py) cover nesting, alias names,
partial/exact classification, justified platform isolation, false duplicate,
obsolete paths after cutover, release check removal, skipped/stale receipts,
cheap drafts and required ready/release work. They do not prove real
provider behavior.

The bounded input is version 1 and records `revision`,
`inventory_complete`, unresolved invocation paths, full workflow/job/
recipe/script/terminal nodes with `invokes` edges, stage dispatch,
job `needs`, original job `condition`, explicit workflow trigger `events` and expanded matrices, effective terminal obligation,
source SHA, input set, environment, platform, toolchain, trust,
failure boundary, reported receipt and documented dispositions. The
`qualification` section must cover every required candidate/release
obligation, fail on non-success and bind the revision.

**Do not treat a reported `PASS` as verified host assurance.** The
checker explicitly reports `optimization_complete: false`, unauthenticated
source/receipt assertions, and `NOT_MEASURED` cost deltas even for a passing
fixture. Its only guarantee is that *the supplied bounded graph* satisfies
the mechanical rules. Evidence that the submitted graph matches ALL
real workflows/scripts/runs and protected gates must be independently
established before cutover acceptance.

## 5. Two separate measured outcomes

After source parity and protected-gate preservation, measure from actual
comparable run receipts bound to revision and event:

1. **Runner-minute difference:** sum billed execution time for all
   triggered workflows, jobs, matrices, setup and retries, not just the
   job that was removed. Include extra Actions started by push, PR or
   release events.
2. **Critical-path difference:** measure the actual qualification wall
   time along blocking dependencies and launch/queue delays. A removed
   parallel job can save runner time without shortening time-to-green.

Use the bundled [run comparison](../scripts/compare_ci_runs.py) where
suitable and disclose comparability limits. Never claim measured
savings from fewer jobs, a local graph PASS, removed YAML, a predicted
duration or a synthetic fixture. Report `NOT_MEASURED` until actual
before/after execution and equal failure-detection evidence exist.

**Acceptance is blocked** if an unnecessary second execution remains
on any relevant unconditional/event-overlapping path, a required
release or security check loses detection, a missing/stale/skipped
authoritative result can qualify, or actual cost/effectiveness has not
been measured for a claimed optimized outcome.

# P0: normalized whole-workflow scenario simulation and conformance-oracle agreement

## Use only after exact-source DISCOVER + JUSTIFY

CI Guard remains a **single standalone skill with one public SKILL.md**.
The canonical [cross-workflow command auditor](../scripts/ci_overlap.py)
is still authoritative for expanded nested verification command
deduplication. The existing [one-pass self-repair](one-pass-self-repair.md)
owns full inventory, draft readiness, actual cost diagnosis and
governed cutover.

This component is a **new optional SIMULATE phase** between read-only
justification and choosing a one-pass repair plan. It is not a
replacement for the other tools or a second overlap auditor.
For pathological CI, SIMULATE is required before paying for a full
repair qualification. For a trivial independent CI question, use the
lightweight existing components without creating elaborate paperwork.

Before preparing the normalized manifest, collect the **actual**
source files and exact SHA, trigger and paths behavior, reusable job
calls, conditional outputs, matrices, nested scripts/recipes,
terminating verifiers, on-repository conformance tests that police
workflow conditions, current branch/ruleset and normative release
requirements. Ensure each declared job `condition` and `needs`
agrees with the current test-oracle expectation. If a static YAML
validator's older allowlist rejects a legitimate new draft guard or
silently accepts a security bypass, diagnose **VALIDATOR_DRIFT**
and HOLD for explicit test repair. Never delete the conformance test
to make the simulation look green.

## Bounded, offline normalized simulation

The bundled standard-library
[ci_scenario.py](../scripts/ci_scenario.py)
takes a caller-authored JSON manifest. It neither parses arbitrary
GitHub expressions nor executes workflow code, uses a shell, installs
dependencies, reads private projects, mutates branch protection or
publishes artifacts. It processes at most 1 MiB and requires two to
four explicitly declared candidate graphs and one to 64 scenarios.

```sh
python3 scripts/ci_scenario.py --input examples/ci-scenario-fixture.json --require-pass
python3 -B -m unittest discover -s examples -p 'test_ci_scenario.py' -v
```

A **trusted host must derive** the graph from the full exact revision,
not from an AI guess, untrusted PR body or a selectively copied
workflow. A declared `inventory.complete:true` or
`status_checks.success` is not an authenticated GitHub receipt.
The simulator returns
`real_provider_semantics_authenticated:false`,
`host_execution_proven:false`, `observed_runner_savings:NOT_MEASURED`,
`observed_critical_path_delta:NOT_MEASURED` even on
`STRUCTURAL_PASS`.

Supported *normalized subset v1*:
- Trusted-normalized path patterns only: exact path, `**` (all), or\n  `prefix/**` (descendants). Other GitHub minimatch forms are unsupported\n  and must be normalized by the host or HOLD.\n- Declared event and changed-path matching, including separate
  draft, ready, push, release, dispatch and cancellation scenarios;
  explicit route-specific job eligibility;
- Same-workflow, acyclic `needs` and four simple explicit
  conditions: success/always/needs_failed/needs_skipped;
- Explicitly expanded fixed or previously evidenced matrix shards;
  optional dynamic source with exact current revision and a real
  producer dependency, never guessed output fanout;
- Single-run artifact producer and dependent verifier obligations;
  independent-lane runtime export guard presence and planted
  unexpected direct/cached artifact-export attempts;
- Exact source revision, required status conclusion and provenance
  kind; source-oracle `if`/needs agreement, unique terminal verifier
  obligation per platform/trust/shard and a separate policy gate that waits on its own same-workflow\n  prerequisites; cross-workflow required contexts are only\n  caller-declared policy input, not direct `needs`;
- Scheduled/failed/skipped/cancelled job states, estimated runner-job
  seconds, longest declared DAG path and earliest declared failure.
  These are **counterfactual estimates**, not provider billing.

**Unsupported semantics fail closed**: raw GitHub `if` expressions,
unknown `workflow_call` bindings, ambiguous `workflow_run`/
`repository_dispatch` propagation, token-trigger/permissions behavior,
undeclared dynamic matrix output, unknown job dependencies, cross-
workflow `needs`, scripts with hidden verifier/export effects and
unmapped release/native/status requirements. Do not emulate complex
provider behavior through an unsafe expression interpreter. Mark
`UNSUPPORTED_SEMANTICS` / HOLD and request narrow independent host
verification.

## Why two graphs instead of a prettier single workflow

The bundled fully fictional eight-workflow fixture compares a
**blanket artifact barrier** against a **split independent/dependent
lane** on the same normative obligations and same source revision.
Each graph separately executes its required lint, independent
checks, native/security checks, reproducibility and two matrix
proof shards. The artifact producer may succeed, fail or be skipped
in the lightweight route.

The split graph's independent check can begin immediately while the
producer runs. A blanket barrier delays it without any extra
failure detection. The fixture estimates equal total runner-job
seconds but **a longer critical path for the blanket graph**.
This is an example of why removing a paid wait or fewer runners is
not proof of faster time-to-green. Do not automatically choose a
winner from estimated numbers alone.

The simulator deliberately fails:
- a draft defer or stale same-SHA context treated as real acceptance;
- an absent, failed, skipped, cancelled or spoofed required status;
- a single failed proof matrix shard hidden by green sibling shards;
- a duplicate identical platform/trust detector or lost required job;
- an `if`/needs changed without its conformance oracle;
- a dependent job that lacks an explicit `needs` edge to its producer;
- an apparently independent CI lane that calls the shared artifact
  export API, or loses its fail-fast CI-only guard;
- an intentionally skipped producer blocking valid lightweight tests;
- a green publication claim without separately run native/release
  obligations;
- an uninspected workflow, stale or cross-revision source input, or
  unmodeled provider trigger chain.

The in-package [37 executable regression cases]
(../examples/test_ci_scenario.py) exercise these failures. Written
cases are not an independent consumer host trial.

## Phase handoffs and acceptance

1. **DISCOVER:** versioned `ci-inventory.json` created by the
   authorized host with exact source/complete paths, conformance
   oracles, authority boundary, missing sources and expiry.
2. **JUSTIFY:** authoritative execution-obligation ledger from the
   canonical overlap checker, independent platform/trust/release
   reasons and negative controls.
3. **SIMULATE:** versioned normalized manifest plus
   `scenario-results.json` with two candidate graphs, 8+ workflows
   where relevant, source-matched status scenarios, per-job results,
   unsupported semantics, aggregate estimates and explicit HOLD.
4. **OPTIMIZE:** compare actual unique detection, earliest failing
   verdict, estimated critical path, runner-job minutes, isolation and
   policy migration separately; document a Pareto tradeoff. A trial
   with invented timing cannot prove cost savings.
5. **PREPARE / PROVE / CUT OVER:** one coherent draft change, no
   expensive draft allocation, source and conformance tests, protected
   status/phase negative controls, owner-approved policy/ruleset
   changes and final exact-head qualification. Re-run the final
   simulator against the *actual* proposed workflow and test-oracle
   source before CI costs.
6. **OBSERVE / IMPROVE / ROLL BACK:** real before/after provider
   receipts for trigger/job dispatch, artifact custody,
   failure propagation, unique obligation and required contexts.
   Compare billed runner minutes **and** longest qualification
   path separately, then accept or rollback.

Each handoff includes `source_sha | input_digest | evidence state
(OBSERVED/EMULATED/ESTIMATED/UNKNOWN) | exact authority | uninspected
paths | blockers | expiry`. The Python checker does not calculate
or authenticate these external digests for you.

The distinction between *presence of a CI-only fail-fast artifact
export guard* and *its runtime enforcement* is especially important.
A manifest flag is not sufficient to claim future test code cannot
silently export. A consuming host must plant an indirect
export-request test **without** updating its static partition map,
verify fail-fast rejection in the independent lane, and preserve
ordinary local developer and producer-skipped paths.

**Completion of the skill source** requires merged exact-source
code, current-version executable tests, correct registry/rights
pins and independent source evidence. **Completion of a consumer CI
optimization** separately requires provider-verified full paths,
required statuses, actual runner allocations, trustworthy timestamps,
non-full-path preservation and measured cost/critical-path receipts.

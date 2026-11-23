# CI strategy fit: choose architecture before adopting an impact graph

**Use when:** evaluating expensive CI, generating a new gate, choosing selective
execution, or determining whether a dependency graph is worth its complexity.
This is an optional *evaluation component*, not a new mandatory CI workflow,
execution engine, service or authorization to change branch protection.

## Architecture should follow observed needs, not vice versa

**Never make a transitive dependency graph the automatic answer.** Preserve
existing governed assurance until a different architecture is justified by
source evidence, unique-detector coverage, cost and failure tests. A small
repository may correctly run every check on every change; a large monorepo
may justify an exact source-to-obligation graph. Both outcomes are legitimate.

Compare at least two relevant approaches before an expensive cutover:

1. **Keep full:** all changes legitimately require the same checks, or
   unknown source/spec/release dependencies prevent a safe narrower scope.
2. **Stage-based:** cheap nonqualifying developer feedback, full exact-head
   candidate, protected main, native/release or production checks according
   to their actual threat and authority boundaries.
3. **Coarse impact:** provider-native or trusted-base package/path selection
   *only* when transitive consumers and generated inputs cannot escape it.
4. **Dependency graph:** validated base/HEAD source inputs and transitive
   consumer closure select individual execution obligations; use the existing
   [dependency qualification contract](dependency-graph-and-qualification.md)
   and [plan/execute/qualify reference](../scripts/ci_plan.py). Do not build
   a competing engine.
5. **Execution efficiency:** reduce proven repeated setup, verifier overlap,
   serial waits or test-internal work while retaining each necessary check.
   This approach may complement another option.

Stage separation is not the same as a cheaper protected merge gate. A
nonqualifying draft result must never pass for exact-head merge qualification.

## Graph-fit decision and proof requirements

Assess source identity, diff completeness, rename/deletion handling,
generated/model input authority, actual Cargo/Lean/build consumers, required
host and release checks, event triggers, nested terminal verifiers, protected
statuses and negative-control failures. Missing dependencies, inaccessible
rulesets, unknown GitHub semantics or changed selector policy => FULL or
HOLD under existing normative governance, not a guessed cheap pass.

Graph selection is justified only if evidence demonstrates **all** of:

- meaningful mixed change cohorts and avoided *actual* runner work;
- a complete, maintained transitive map from changed inputs to individually
  necessary verification obligations, including unknown-file fallback;
- source-pinned trusted policy, current-HEAD executable receipts, independent
  fail-closed qualification, and preserved unique native/security/release
  detection;
- a benefit/risk comparison against simpler alternatives, including full
  gate critical path, earliest failure, complexity, expected run frequency,
  maintenance cost and rollback;
- a governed SPEC/branch-required-status migration when the current norm
  requires full candidate qualification, rather than silently changing it.

The owner sets economic and latency thresholds. The skill provides no
universal numeric test, no assumption that Rust or model-backed repos
automatically deserve graph selection, and no implicit approval to skip work.
A small scheduler repair can be useful without satisfying the broader CI
optimization objective.

## Optional, offline strategy comparison

[ci_strategy_fit.py](../scripts/ci_strategy_fit.py) evaluates two to twenty
**analyst-declared** alternatives against a baseline. Try:

```sh
python3 scripts/ci_strategy_fit.py --input examples/ci-strategy-fit-fixture.json
python3 -m unittest discover -s examples -p test_ci_strategy_fit.py
```

The [fictional scenario](../examples/ci-strategy-fit-fixture.json) includes
full, stage, dependency-graph and test-internal alternatives. Input schema v1
requires a pinned revision, objective name, explicit comparison horizon,
owner-defined minimum runner-hours saving per graph maintenance hour,
maximum accepted critical-path regression, baseline job minutes/critical path,
and each alternative's kind, predicted metrics, evidence state, maintenance
hours, source-proof reference, detector parity, required status/spec mapping,
fresh-receipt guard, rollback, and (for a graph) complete source-impact and
transitive mappings. An input or safeguard with unknown status is not PASS.

A graph is `HOLD` if its source/consumer closure is incomplete, it lacks
fresh assurance receipts, it exceeds the owner's critical-path tolerance,
or it cannot justify its complexity over the declared horizon. Other
strategies remain eligible where their narrower source obligations are proven.
The output `OPTIONS_FOR_EXPERIMENT` only ranks *declared* candidates.
`CANDIDATE_FOR_VALIDATION` does **not** mean deployable, approved or
economically proved. The tool does not inspect GitHub, evaluate workflow YAML,
authenticate supplied evidence, execute tests, change required checks or
measure actual provider billing. The exact source/oracle and simulator
checks elsewhere in CI Guard remain mandatory for consequential changes.

## Decision record and rollout

Record: source revision | owner's objective | incumbent obligations and
measured baseline | two or more viable alternatives | graph need or reason
against it | modeled vs observed costs | independent detectors | critical
path and first failure | unknowns | rollback | selected next experiment.
Use DISCOVER → JUSTIFY → SIMULATE → OPTIMIZE → PREPARE → PROVE → CUT OVER
→ OBSERVE (and ROLL BACK when necessary). Only comparable live outcomes
demonstrate ROI. If nothing is defensibly better, keep the current gate,
state the limitations, and avoid complexity for its own sake.

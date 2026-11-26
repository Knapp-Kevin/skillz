# Optional controlled behavioral comparison: trial matrix (v1)

Tracks #955; related #954, #828/#833, #861. This is the first offline
implementation slice, not a live model runner, separate evaluator, new
user-facing skill or automatic acceptance route.

## Inputs and output

Use the existing [acceptance plans](acceptance-plan.md) for the exact baseline
and candidate packages in the same assessed host. Regenerate and verify both
plans from real package bytes and independently review their obligations
before comparing them. The trial matrix consumes the existing envelopes;
it checks their canonical digests and selected common case identity but does
not regenerate their source contracts or verify actual package bytes itself.

`trial_matrix.freeze(baseline, candidate, config)` creates an immutable-by-
identity experiment plan and explicit expected run inventory. The caller
provides:

- schema_version (integer 1), runtime_sha256 (digest of reviewed, pinned
  environment and model settings), budget_per_trial (positive integer,
  unit established separately in the experiment protocol), repetitions
  (1-10);
- fixtures (explicit comparable acceptance case IDs, family, development
  or held-out partition, fixture_sha256 and independently reviewed
  oracle_sha256). Both partitions are required; identical families or
  fixture digests may not span them.

Each selected case/repetition has a no-skill control, baseline and candidate
arm. Same fixture/oracle identities and shared environment/budget apply.
Host activation and cleanup are separate native acceptance obligations,
not comparable no-skill tasks. The selection is deliberately a subset,
not full acceptance coverage. Review semantic comparability and preserve
required safeguards; a matching case ID or hash alone is not semantic proof.
Never expose held-out fixture bytes to the refinement process.

`trial_matrix.reconcile(baseline, candidate, config, ledger)` regenerates
the experiment identity and counts every expected run by partition, arm
and status. The ledger contains experiment_sha256 and rows of run_id,
status and evidence_sha256. Statuses: PASS_CLAIMED, FAIL_CLAIMED, INVALID,
TIMEOUT, NOT_RUN. Missing rows remain explicitly MISSING. Duplicate or
unknown runs, plan/oracle drift, reused evidence, and evidence on NOT_RUN
refuse; incomplete/invalid/timed-out inventories hold. Complete claimed
pass/fail inventories still require review. No score, approval, qualification,
evidence authentication or promotion is inferred.

This module is an optional Python standard-library library, with no CLI,
network, model calls, execution adapter, subprocess, file writes or consumer
dependency. Keep all real plans/receipts private. Example usage and fictional
observations appear in test_trial_matrix.py; they are not real behavioral
evidence. Run the focused checks:

    python -B -m unittest discover -s engine/builder -p test_trial_matrix.py -v

## Next implementation gates

1. Integrate real regenerated source/design plans and archive reconciliation
   without weakening existing case-ledger requirements.
2. Define precise typed budget, environment and observation provenance,
   task-level safety obligations, comparison eligibility and independently
   controlled oracle/fixture custody. Verify actual bytes and execution
   receipts; prevent cross-experiment relabeling and solution leakage.
3. Add an explicit deterministic fake execution adapter and failure
   classification, then an authorized isolated native-host adapter only
   after containment and command/credential admission are qualified.
4. Use minimized synthetic CI Guard families and held-out variants for a
   controlled pilot. Retain failures, report denominators, uncertainty,
   actual costs and separate safety vetoes. No model self-certification,
   automatic install, publication, canonical rewrite or new mandatory runtime.

The current module is structural bookkeeping. Neither hashes nor claims
authenticate a producer, prove isolation, validate the oracle or establish
causal benefit. No live trials are implied by passing its unit tests.

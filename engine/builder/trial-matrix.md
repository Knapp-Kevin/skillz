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

- schema_version (integer 1), experiment_id (unique per authorized experiment),
  runtime_sha256 (digest of reviewed, pinned environment and model settings),
  budget_unit (wall-seconds, tokens or tool-calls), budget_per_trial (positive
  integer), repetitions (1-10);
- fixtures (explicit comparable acceptance case IDs, family, development
  or held-out partition, fixture_sha256 and independently reviewed
  oracle_sha256). Both partitions are required; identical families or
  fixture digests may not span them.

Each selected case/repetition has a no-skill control, baseline and candidate
arm. Same fixture/oracle identities and shared environment/budget apply. Every run
ID binds the entire normalized experiment scope, including both package plans,
unique experiment ID, runtime, budget and fixture inventory; changing any
invalidates earlier run IDs. Identical package/host manifest arms are refused,
as are changed expected contracts in selected cases. The caller still owns
semantic comparability and experiment-ID uniqueness.
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

For byte-bound observation review, call `reconcile_receipts` with the same
inputs plus two mappings (run_id to raw receipt bytes, run_id to raw payload
bytes), exactly covering observed rows. The strict JSON receipt contains
schema_version (1), experiment_sha256, run_id, status and payload_sha256;
the ledger's evidence_sha256 is the SHA-256 of its original receipt bytes.
The payload digest, scope, outcome and complete inventory must match. Duplicate
JSON keys, altered bytes and extra/missing receipts refuse. Per-receipt, per-payload
and aggregate byte limits apply. Identical payloads across different legitimate
runs are possible; matching bytes do not establish independent execution,
trusted authorship, actual artifact semantics or oracle truth. The lower-level
`reconcile` remains a claims-only route, not a byte verification claim.

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

## Deterministic synthetic adapter (offline only)

`trial_fake.run(..., execute=False)` is the next bounded controller slice.
It regenerates the matrix and verifies exact runtime, fixture and oracle bytes
before any emulation. The default returns the entire NOT_RUN ledger without
invoking the adapter. Explicit `execute=True` permits only the fixed
`synthetic-in-memory-v1` adapter; no callbacks, shell, filesystem, network,
credentials, model invocation or package code execution are provided.
The original fictional fixture is a bounded integer list; the controller's
independent property oracle checks sorted unique membership rather than trusting
adapter success. Each run has fresh local state and a simulated step budget.
Fixed modes plant wrong outputs, setup failure, timeout, missing trace,
unauthorized effect and cleanup failure. Invalid or timed-out runs remain
in the complete denominator. Payloads explicitly say SYNTHETIC_FAKE_ONLY;
the existing receipt reconciler binds every raw payload and receipt to the
frozen run identity. These are simulated steps, not measured model/tool costs.
No actual host isolation, native activation, skill effectiveness, or promotion
is asserted. The fixture/oracle byte maps belong to the trusted controller;
do not expose held-out bytes to real refinement. This adapter cannot qualify
a native host or arbitrary executable oracle. See test_trial_fake.py for the
fully reproducible positive and planted-failure pilot.

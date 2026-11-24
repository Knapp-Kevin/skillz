# Agent-host handoff qualification

This is a portable component of **File Lifecycle Curator**, not a standalone
app, connector, memory service, file-operation executor or scheduler.
The purpose is to avoid mistaking a **saved checkpoint** for **fresh host
observation**, or a **readback asserted by the host** for an authenticated
verification performed by this skill.

## Decisions and adversarial review (before implementation)

The Qortara Logic hosted route planner proposed Plan → Deep Audit → Implement →
Verify with source-authority, privacy, replay and current-head CI gates.
It cannot read the repository or execute those skill procedures for us.

Initial design received an **author-led VETO**:
- **F1/security:** Old VERIFIED diagrams can be replayed as fresh success.
- **F2/architecture:** In-package cloud connectors mix provider permission,
  file actions and visual/reporting state; this breaks portability.
- **F3/tests:** Checkpoint-only simulations never exercise a real file readback.
- **F4/replay:** Host receipt detached from plan/source ID, revision and current
  viewer may falsely certify progress.

The revised **author-led PASS** retained the existing private checkpoint
component and added only a read-only handoff evaluator. The Qortara hosted
verdict parser interpreted the two supplied reports as block and allow
respectively; this is **not an independent audit or source attestation**.

## Inputs and required host boundary

The consuming agent or host obtains and currently authorizes:

1. One new source observation in the **existing** `reconcile.py` snapshot
   schema with a new ID, newer observation time, current viewer checks and
   per-record native identity/revision evidence. A missing prior ID must
   carry separately verified current permission to reveal its existence.
2. The current approved private SQLite checkpoint from `state.py`, with
   the same root, principal, collection and audience. This is the accepted
   source of persistence, **not current source authority**.
3. Optional new visual plan/operation receipt in the existing
   `render_structure.py` schema. It must retain the exact accepted plan ID
   and revision, immutable original paths and target paths, with refreshed
   record IDs/revisions and a **later** time-bound source observation.

Call from the skill package directory, with host-authorized paths:

```sh
python3 scripts/host_handoff.py \
  --store /approved-private/state.sqlite \
  --current /approved-private/current-snapshot.json \
  --plan /approved-private/current-plan-with-readback.json
```

Omit `--plan` for source-only reconciliation. The output is JSON:
`FRESH_SOURCE_PROVISIONAL`, `HANDOFF_PREVIEW_NOT_PERSISTED`,
`SAME_SNAPSHOT_NO_FRESH_HOST_EVIDENCE`, or an explicit hold. The helper
never writes checkpoint state, original files, index data or an operation
receipt. It produces bounded delta actions, source-scoped observed/proposed/
readback-attested views, an actually limited scoped progress denominator
and a next safe action with one alternative.

**No cached progress is presented as current.** Same-snapshot replay returns
no progress; a last-known plan is not enough for a fresh verification. The
host must re-observe the source and independently verify physical operations.
The helper labels both current source identity and operation receipt
evidence as `CALLER_ASSERTED_NOT_HOST_AUTHENTICATED` /
`NOT_INDEPENDENTLY_VERIFIED`. A tool receipt is not itself a verified move.

## Controlled host exercise

`tests/test_host_handoff.py` creates real test-only files under
`tempfile.TemporaryDirectory`. The **test host**, not the package runtime,
moves a file using the local filesystem, independently reads the destination
bytes, compares SHA-256, prepares an exact source/plan receipt and invokes
the handoff preview. The test then separately commits with the existing
opt-in `state.process` and verifies durable generation on reopen.

Adversarial cases include old receipt replay, same snapshot ID with modified
content, revoked viewer, ACL-filtered missing ID, cross-principal scope,
changed revision, retargeted destination and receipts that precede the
source observation. Unqualified counts and diagrams remain suppressed.

## Important remaining qualification

This demonstrates a controlled local-host exercise of handoff behavior.
It does **not** attest real Google Drive/GitHub/Windows provider permissions,
authenticity of host-supplied snapshots or plan receipts, multi-user isolation,
production backup restoration, safe external file moves, or live delivery of
scheduled agent reports. These require a separately authorized real consumer
trial and actual provider-side readbacks.

The output must not be renamed VERIFIED by a consuming agent without actual
host evidence. Even after the state checkpoint commits, another invocation
needs a **new current source observation** to claim freshness. All source
file operations, permissions, storage, delivery, time budget and scheduler
remain exclusively in the external host's authority boundary.

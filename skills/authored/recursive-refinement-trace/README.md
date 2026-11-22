# Recursive Refinement Trace v0.1.0

A portable **optional** capture component for governed recursive skill
improvement. The downloaded package contains everything required to run
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
python -m unittest discover -s . -p test_trace.py -v
```

The test suite includes a **real local synthetic source check** that
produces actual failing and passing subprocess exit statuses on two
synthetic preference files. It then records separate red/green experiments,
without falsely claiming one observation mutated the workspace of another.
Tests run without installing dependencies or accessing network services.

The helper never authenticates user intent, external evaluator execution,
independent agent behavior or real downstream skill effectiveness. Those
claims require separate observable evidence, not self-generated receipts.

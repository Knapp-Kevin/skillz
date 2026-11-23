# Long-running file curation: endurance and recovery qualification

**Scope:** Optional File Lifecycle Curator skill-package helpers only. This
document is an adversarial design receipt and executable-test guide, not an
agent, a daemon, a scheduler, a recovery authority, an audit attestation, or
proof of a real consumer's private files.

## Architectural decisions reviewed before implementation

| Decision | Adversarial failure mode | Approved boundary | Evidence |
| --- | --- | --- | --- |
| D1: Endurance simulation | A loop embedded in this skill could create autonomous actions or simulate success without checking persisted state | A deterministic offline `unittest` that supplies virtual timestamps and real ephemeral SQLite transactions; no background runtime | `tests/test_endurance.py` |
| D2: Historic journal verification | Count/min/max and last receipt alone can miss corrupted intermediate reports | Keep fast current-receipt preflight; stream all accepted receipts for an explicit weekly structural audit, no schema migration | `scripts/maintenance.py`, `tests/test_maintenance.py` |
| D3: Recovery | Automatically restoring an old backup could erase newer work, bypass revocation, or duplicate external file operations | A synthetic backup candidate is inspected read-only; corrupt primary is refused; no replacement/rollback is performed | `tests/test_endurance.py` |
| D4: Release and provenance | New code may pass local tests while registry fingerprints and static verification describe an obsolete package | Preserve exact source and tree identities and both relevant CI gates, keep behavioral status NOT_RUN for real source hosts | Registry companions and CI run |

### Adversarial pass 1 (VETO; plan superseded)

- F1, macro-architecture, L2: **do not** introduce a continuously running agent
  or a schedule in the repository.
- F2, security, L3: **do not** restore a stale backup automatically; source
  operations might have occurred after it was taken.
- F3, coverage-gap, L2: **do not** call virtual time alone an endurance pass.
  Assert generation integrity, no missing record loss, access and CAS refusal,
  failure rollback, resume and bounded audit output.
- F4, specification-drift, L2: **do not** change the durable-state schema merely
  to run tests.

### Adversarial pass 2 (author-led PASS, not independent attestation)

Accepted the D1-D4 boundaries above. Qortara Logic's hosted route preview
identified a proposed Plan → Deep Audit → Implement → Verify chain. Its hosted
verdict interpreter reported block for the first supplied VETO and allow for
the revised supplied PASS. Neither result is an independent source audit,
authority grant, execution record or permission to merge. Qortara's
repository-local record-gate tools are not exposed on the hosted surface.
The independent evidence of functional behavior is the repository CI output,
which must be inspected before merge.

## What the executable tests substantiate

- Ninety **simulated** days: 2,160 uniquely identified hourly snapshots, 90
  daily audit proposals and 12 weekly audit proposals. Those audits must not
  advance the accepted generation on an unchanged source.
- At every hourly commit, assert read-back generation, source-operation
  nonexecution and retention of a two-record last-known catalog despite
  periodic partial source scans.
- Inject temporary access denials, a deliberately failed receipt insert and
  a stale generation. Confirm failure never falsely advances the state and
  a subsequent qualified retry can continue.
- Compare the final recovered private SQLite checkpoint with the expected
  accepted-run count and last observed source identity/revision.
- Corrupt a nonlatest accepted journal report and assert the weekly deep
  structural audit refuses the checkpoint.
- Make a synthetic SQLite backup, corrupt the primary, verify primary refuses
  new work and the backup remains readable **without automatic restoration**.

Run from the self-contained package root:

```sh
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
```

The test suite uses Python 3.9+ standard library, virtual time and temporary
local files. It does not read user folders, index content, authenticate
connectors, allocate cloud resources, run for 90 actual elapsed days, verify
live scheduled delivery or execute any file movement.

## Security and performance limitations

- The weekly full structural scan is a read-only database cursor, not a
  cryptographically authenticated evidence chain. A writer who can replace
  the database and integrity fields may create plausible fake receipts.
- Hourly and daily preflight verify structural generation continuity and the
  latest receipt. Malformed intermediate entries are detected during the deep
  audit, not necessarily in the next hourly run.
- A verified backup candidate might still be stale or outside current
  permission scope. A restore needs fresh owner authorization, scope/ACL
  checking, recoverability rehearsal and reconciliation of external effects.
- Simulation time is not physical scheduling: real agent restarts, native
  Windows ACLs, provider-specific revision semantics and disaster recovery
  are not proven by synthetic tests.
- Any CI runtime concerns must be measured and refined without reducing
  failure-detection obligations or silently skipping the endurance suite.
- Source limits remain 500 accumulated records, 1 MiB per input snapshot,
  and 100,000 accepted generations. No compaction, shard aggregation or
  automatic retention policy is added.

## Completion gate

Complete **this qualification tranche** only when the test suite and authored
package registry checks pass for the exact PR head, adversarial findings are
resolved, and the PR is actually merged. Do not label the broader feature
production-proven or the real agent-host recovery path complete.

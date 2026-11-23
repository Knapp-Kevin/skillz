# File Lifecycle Curator: persistent, restart-safe maintenance state

Date: 2026-11-23. Owner objective: one file-curation skill must survive
hourly, daily and weekly interactions while retaining the actual
organization progress, observations and approved plan across agent restarts.
No separate scheduler or host file-operation authority was requested.

## Decision

A pure text/diagram handoff is insufficient for persistent organization.
Add an OPTIONAL, original first-party, local transactional state engine to
the skill. Keep the portable SKILL.md instructions and read-only
reconcile/visual helpers fully usable without any storage.

SQLite via Python standard library was selected for private on-host
storage over ephemeral chat memory, open-ended JSON files or an external
SaaS. SQLite supplies atomic multi-table transactions, local single-writer
locking, native readback and restart behavior without network privileges.
The host/user must approve the actual private storage location. No cloud
account, user file, schedule or background process is created by the
package itself.

## Durable invariants

- All hourly/daily/weekly invocations use the SAME source-scoped store,
  keyed by collection/root/principal/audience. No independent "weekly"
  source of truth.
- Snapshot identity and content may not contradict each other; a
  duplicate accepted run is idempotent, a reused run-ID with changed
  input fails closed. Expected-generation CAS prevents stale writers.
- A partial scan updates newly observed rows but does NOT erase or
  recertify older last-known files. Record-level last_seen must persist
  with the actual source snapshot timestamp.
- Current source/viewer access is checked before exposing cached IDs,
  counts or plan visuals, or accepting a state transition. Missing
  old IDs with no current identity-level authorization are held.
  The helper accepts host assertions but cannot authenticate them.
- Organization plan/receipts are separate, versioned and deliberately
  input-bound. A plan not re-inspected this run is historical, never
  equivalent to currently VERIFIED file operations. Plan drift or
  source revision mismatch triggers a hold; new version needs explicit
  replan approval.
- The default command is READ-ONLY. Only --commit, a private-storage
  acknowledgement, an exact expected generation and explicit first
  initialization authorize SQLite checkpoint writing. Not file moves.
- SQLite state and journal receipt are committed together. Failed
  insertion rolls back the entire update. A state digest checks
  accidental corruption but cannot authenticate a malicious writer.
- No scheduler is installed; cadence is an informational run label.
  Retention, backup, encryption and host-ACL are outside this engine.

## Adversarial qualification

The source-only tests create actual temporary private SQLite databases
and exercise real reopen, repeated run IDs, expected-generation
conflicts, modified/reused source snapshot IDs, partial-observation
memory preservation over multiple hours, complete-list absence,
viewer denial, cross-principal protection, plan source/ACL and
version boundaries, plan-only updates, SQL-triggered crash/rollback,
digest alteration, symlink rejection and journal receipts.

Passing source tests proves deterministic offline state behavior, not
that a real consuming agent accessed or reorganized user files or that
an actual scheduled task delivered hourly/daily/weekly results.
Tests should be run at the exact merged candidate PR HEAD, with
old source baseline and registry/integrity checks protected.

## Known production limitations

- Python 3.9+ SQLite on a trustworthy **local** private filesystem.
  Network file shares and untrusted concurrent filesystem path
  attackers are unsupported. No at-rest encryption is bundled.
- Bounded original reconcile contract: max 500 latest+historical
  file records, 1 MiB source snapshot, 100,000 committed runs.
  Larger roots need explicit, separately authorized sharding, not
  silent omission of files.
- Durable engine stores source record metadata, latest plan and
  run summaries, NOT raw files, extraction text, embeddings or a
  full queryable semantic index. Those require an independently
  approved and maintained private provider.
- Host may need to bridge provider revisions/ETags, pagination,
  exact identity, native ACLs, observed source bytes, durable
  checkpoint directory and file operation readbacks before trusting
  source or plan assertions.
- A real stress test under scheduled interruption, permission
  revocation and state restore is still required for a claim of
  production-grade agent operation.

## Versioning and hygiene

Retain package v1.1.1 as a conservative bounded refinement.
No automatic schedule and no unrelated package authoring/backlog
work. Merge is completion; an unmerged PR is not an acceptable
deliverable for this pass.

## Initial executable adversarial result and correction

The first exact-HEAD suite executed **115** source tests: 114 passed, and one scenario revealed that the cold-start *preview* path returned before validating its cadence value. No state or schedule was created. The input guard was moved to the common entrypoint so unsupported frequencies are refused even when the store does not exist. A secondary review identified that a PLAN_ONLY update after a PARTIAL snapshot must not report absent historical catalog entries as freshly unchanged. The refined method distinguishes actually observed unchanged IDs from NOT_OBSERVED_PARTIAL_SCOPE; an additional synthetic regression case raises the expected final source suite to **116** tests. Results after these corrections require a fresh exact-head CI receipt. No live source or host schedule has been touched.

## Multi-run source identity adversarial finding

Automated review identified a serious recurrence flaw: a source snapshot ID could be reused after an intervening accepted snapshot, causing last_seen ID equality to falsely classify an older, actually unobserved catalog record as freshly observed. The corrected durable engine consults all accepted run records before accepting an ID and refuses reuse of any earlier **non-latest** source snapshot ID, while allowing explicitly guarded PLAN_ONLY updates against the latest unchanged snapshot. Two additional planted SQLite tests cover both content and timestamp variants and ensure the catalog/generation cannot be corrupted. The final expected source suite is **118 cases** (81 protected maintenance/visual + 37 persistence/adversarial) pending exact-head qualification. One initial review thread covering cadence validation was already addressed before this correction.

## Exact-source qualification and merge gate

PR [#904](https://github.com/Knapp-Kevin/skillz/pull/904) source HEAD `176eb8e4c226c8542a695eebdaabf7ac734ba9d6` passed [118/118 source tests](https://github.com/Knapp-Kevin/skillz/actions/runs/45289252920) and [11/11 authored contract checks](https://github.com/Knapp-Kevin/skillz/actions/runs/45289253087). The two available Socket security checks were SUCCESS. Real local SQLite reopen, corrupted checksum refusal, injected transaction failure/rollback, generation CAS, source snapshot identity replay, partial scans, read-back of private state, and explicit replan guards are covered. Both review threads (cold-start cadence and historical snapshot IDs) were resolved. These synthetic/source tests do not demonstrate a scheduled run on a live account, hosted authorization semantics, actual file modification, private user storage setup or disaster recovery in the presence of a malicious concurrent filesystem actor.

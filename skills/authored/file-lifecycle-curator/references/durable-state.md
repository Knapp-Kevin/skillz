# Persistent organization state for hourly, daily and weekly agent use

**This is an opt-in state component of File Lifecycle Curator, not a
scheduled agent, model memory, cloud connector, or automatic file executor.**

## What persists and what does not

The private host-approved SQLite checkpoint contains:
- latest accepted source snapshot and source-scoped identity/revision/access
  claims supplied by the host, plus an accumulated last-known catalog;
- each catalog record's last actually observed snapshot ID and timestamp,
  retained across **partial** scans without inventing current visibility;
- latest explicitly supplied organization-plan snapshot, including its
  original-to-proposed paths, per-record operation state and
  caller-asserted read-back details;
- generation number, last accepted run ID, an internal SHA-256 integrity
  checksum, and a small append-only accepted-run history with cadence,
  source snapshot IDs, change/coverage summaries and plan counts.

The saved plan is a **last-known plan**, not evidence that the actual
files still exist or remain readable. A run without fresh plan evidence
returns HISTORICAL_NOT_REVALIDATED. A saved VERIFIED state also remains
caller asserted until the real host checks the receipt against the
source and destination; the state engine does not independently
authenticate it. Cached search results, extraction text, tags, native
filenames, backed-up file bytes and external ACLs are NOT part of this
initial bounded store. Preserve those only in separately approved
source-specific indexes with their own permission/retention contracts.

## Architecture: transaction boundaries

    approved current source snapshot, optional approved plan
                         |
              verify source scope/access
                         |
           read private checkpoint at generation N
                         |
     dedup run ID; refuse snapshot/plan drift and stale CAS
                         |
          reconcile against retained last-known catalog
                         |
                  produce DRY_RUN
                         |
     --commit + --ack-private-store + expected generation
                         |
          SQLite BEGIN IMMEDIATE, durable transaction
                         |
            read-back and report generation N+1

The host controls where the database lives; this skill never chooses
a personal location. The parent directory must already exist, must
be private (POSIX permission bits 0700) and cannot traverse a symbolic
link. New SQLite files are created with mode 0600, uses rollback
journal with synchronous FULL and a single transaction for state
plus run receipt. Native SQLite single-writer serialization avoids
two overlapping hourly/daily agents silently overwriting each
other. A nonmatching expected generation refuses with
GENERATION_CONFLICT; restart from the latest accepted state rather
than retrying stale writes indefinitely. A crash/SQL exception
must roll back the attempted update.

Host-specific caveats: SQLite durability depends on the filesystem's
locking and flush guarantees. Do NOT put this DB on unreliable network
shares or sync folders with conflicting writers. On Windows, filesystem
ACL protection is the host's responsibility; POSIX mode checks do not
secure Windows accounts. There is no encryption at rest built into
Python's sqlite3. Use an encrypted, owner-approved private store
where necessary. The SHA-256 checksum detects ordinary corruption
but is **not** an authentication signature: a hostile writer able to
replace the DB can also replace its checksum. Host-enforced ownership,
permissions, backup, restore and revocation remain mandatory.

## Invocation (offline example)

From the skill package root after an authorized host has made snapshots
available, with an *already existing* private owner-controlled folder:

    python3 scripts/state.py --store /approved-private/state.sqlite \
      --current examples/maintenance-previous.json --run-id manual-001 \
      --cadence manual

The first command is read-only: if no state exists, it reports
COLD_START_PREVIEW and does **not** create a database.

After separately approving the private persistent write, an explicitly
authorized host may initialize generation 1:

    python3 scripts/state.py --store /approved-private/state.sqlite \
      --current examples/maintenance-previous.json --run-id manual-001 \
      --cadence manual --commit --initialize \
      --expected-generation 0 --ack-private-store

On a subsequent *new* snapshot, a scheduler or interactive agent
recovers the authorized state and previews, then submits exactly
the generation it read:

    python3 scripts/state.py --store /approved-private/state.sqlite \
      --current examples/maintenance-current.json --run-id hourly-002 \
      --cadence hourly
    python3 scripts/state.py --store /approved-private/state.sqlite \
      --current examples/maintenance-current.json --run-id hourly-002 \
      --cadence hourly --commit --expected-generation 1 \
      --ack-private-store

The examples use invented IDs, not a real account. An actual host must
replace snapshot paths, run IDs and expected-generation with observed
values and verify current user access. No CLI flag automatically grants
access; they are explicit assertions the agent must substantiate.

Optional --plan points to an explicitly authorized
render_structure.py-compatible plan/operation snapshot. The plan can be
updated even when the source snapshot ID remains unchanged. A new plan
revision needs separately approved --accept-replan and --commit; changing
a target under the same revision is a PLAN_DRIFT_HOLD. Visual progress
must be freshly projected from the current host ledger, not assumed from
the last saved diagram. No plan is ever automatically approved.

## Repeatable operating cadence, not three separate sources of truth

- **Hourly:** quick bounded change detection, work on a small list of
  changed/unknown records, record actual holds/failed operations. May
  report no change; do not rewrite an identical snapshot.
- **Daily:** inspect incomplete curation work, semantic index/tag
  staleness, the selected plan's drift and actual host receipts;
  consolidate an authorized daily user report without inventing
  success from accepted snapshots.
- **Weekly:** sample unchanged items adversarially, check root/ACL
  drift, retention holds, missed pages, index quality, recovery
  readiness and overdue decisions. Treat all source timestamps and
  assertions as evidence to verify, not lasting permission.

They all use **one private store per exact collection/root/principal/
audience**, not competing hourly/daily/weekly copies. Cadence labels
record provenance; they do NOT create or configure a schedule.
A run ID is unique to the specific host-observed input. Reusing it
with the same input is ALREADY_APPLIED with no duplicate write;
reusing it with different content is RUN_ID_REUSE_CONFLICT.
Same snapshot ID with changed contents is also refused. On a
genuinely fresh snapshot, state advances only once.

## Partial pages, absent files and privacy

A partial run updates records it actually saw while retaining
last-known catalog entries it did not see, tagged with their last_seen
timestamp. It NEVER silently drops them or changes their observed
time to the current run. Unknown identity permission on missing old
IDs returns ABSENT_IDENTITY_ACCESS_HOLD without leaking old IDs,
counts or summaries. A complete scan with missing records is a
review signal, not deletion approval. No snapshot permits source
move, index export, archive disposal, access change or file deletion.

An inaccessible current viewer stops all state transitions and
suppresses source identifiers/counts. A saved checkpoint's old access
grant is never current authorization. A source scope/principal/
audience change refuses re-use, requiring a new explicitly approved
private store or migration. If a state checksum is bad, stop with
STATE_INTEGRITY_HOLD; **do not overwrite or silently reset** a
corrupted checkpoint. An existing DB without a compatible schema
requires an explicit recovery decision. Use private backups and a
user-approved recovery procedure, with read-back verification.

## Boundedness, migrations and retention

Current source snapshot maximum: **500 records / 1 MiB**; accumulated
last-known catalog capped at 500 records. Split large collections
into explicitly scoped shards, each with its own private store,
rather than quietly truncating, inventing completeness or disabling
permission checks. The visual helper separately accepts at most
200 entries and renders 24 for clarity.

Schema format 1 is fixed. A future incompatible schema must fail
closed, then migrate from a separately backed-up copy with
explicit owner approval and a reversible tested procedure. No
automatic migration on hourly/daily runs.

Accepted run summaries are a small persistent journal, capped at
100,000 accepted generations (roughly 11 years at 24/day).
No automatic retention pruning or deletion of historic source
metadata is provided: the owner must choose a private backup,
retention policy and explicit purge/rotation. A normal scheduled
agent may report HISTORY_LIMIT_HOLD rather than discarding history.

**Success measures:** authorized source coverage and recall, no lost
partial-scan entries, zero duplicated accepted updates, no false
verified relocation, bounded processing time, successful checkpoint
restart/readback and correctly delivered user reports. A green
SQLite test alone does not prove true source permissions, successful
user retrieval, real-world backups, agent-host integration or
hourly/daily/weekly task delivery. Those remain separate host trials.

## Adversarial and qualification contract

The source test module
[tests/test_state.py](../tests/test_state.py) uses real temporary
private SQLite files, restarts, injected transaction failure,
duplicate run IDs, conflicting CAS, ACL holds, partial/full scans,
source revision changes, plan drift/replan and history receipts.
It runs alongside existing delta and visual tests with:

    python3 -B -m unittest discover -s tests -p 'test_*.py' -v

No data or checkpoint from the test cases leaves the synthetic
temporary folder; no GitHub or scheduled task is invoked.

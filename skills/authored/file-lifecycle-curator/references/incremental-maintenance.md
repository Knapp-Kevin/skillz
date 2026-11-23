# Incremental maintenance, recall and scheduled-run handoff

This is a complete standalone component of File Lifecycle Curator. It works
without a scheduler, connector, database, private memory, or sibling skill.
Using the skill does not create a recurring job or permission to change files.

## Modes

1. **BOOTSTRAP**: make a bounded source inventory. Without a genuinely
   accessible prior checkpoint, label continuity COLD_START, not remembered.
2. **REFRESH**: recover the authorized previous checkpoint, establish current
   viewer/source rights, compare with a fresh observed snapshot, and reprocess
   changed, stale, unknown or held records rather than everything.
3. **RETRIEVE**: answer a scoped search with actual index and source locators,
   captured date and extraction coverage. Recheck private-source access and
   revisions before displaying cached titles, summaries or search hits.
4. **AUDIT**: periodically sample supposedly unchanged files, tag quality,
   evidence links, retention holds, ACLs, failed operations and staleness.
   Audit frequency is set by owner/host policy, not invented by this skill.

## Durable checkpoint and safe recall

A checkpoint is separately authorized, revocable, versioned evidence in an
actual host's user-private storage. It is NOT an agent's presumed memory.
Do not put raw private documents, identifying paths or account credentials
in public Skillz packages, GitHub issue text or scheduler task descriptions.

A useful private checkpoint carries:
- skill/schema identity and last accepted run and source snapshot IDs;
- collection/root/principal/audience scope, exclusions and pagination coverage;
- per-record stable source ID, native ID when available, revision *kind/value*,
  observed locator, viewer/access evidence, extraction coverage, exact digest
  method where truly measured, stored card/index revision, and status;
- supported taxonomy and evidence locators, version/duplicate relationships;
- unvisited/failed/held items, retention holds and actual operation receipts;
- one continuation cursor ONLY when its provider proves its validity;
- optional consented local output preferences isolated from shared skill code.

A natural-language handoff summary may accompany the checkpoint, but cannot
substitute for current access, per-record revision, verified operation status
or exact source identity. On unreadable, lost, revoked, stale or incompatible
checkpoint: disclose lost continuity and use read-only COLD_START; never
fabricate recovered history. Checkpoint persistence is itself a file write
requiring scope-specific authorization and readback.

## Each invocation, including scheduled invocations

1. **Authorize** exact collection, root, principal, viewer, exclusions,
   source reader, cost/batch cap and permitted report destination; verify
   current viewer rights. A prior task authorization never expands scope.
   If access is missing or revoked, suppress cached private identities,
   contents, summary counts and relationship edges from unauthorized output.
2. **Observe** current inventory with provider-native revisions or change
   tokens when truly supported. An ETag, name, timestamp, excerpt, size or
   stale checkpoint is not necessarily a complete-file hash. Track extraction
   and pagination coverage; do not call a partial scan COMPLETE.
3. **Reconcile** by stable source-scoped identity. Categorize new, changed,
   unchanged, moved/renamed with preserved native ID, unknown revision,
   extraction regression, access hold, and missing from complete vs not seen
   in partial scope. A missing record NEVER automatically authorizes deletion.
4. **Selectively reprocess** changed or stale files; reconcile links, tags,
   metadata summaries and archive recommendations. Do not discard previously
   complete evidence when this run read only an excerpt. An unchanged
   revision saves work only when the host's revision method is trustworthy
   for the specific claim and current rights have been checked.
5. **Quality check** source/index coverage, stale lookup risk, taxonomy drift,
   duplicate evidence, broken links, sensitive leakage and actual archive
   readbacks. Separate reproducible canonical skill errors from personal
   preferences. No automatic skill rewrite; private preferences only with
   explicit consent and private compatible storage.
6. **Report boundedly** scope, actual inspected/uninspected/failed counts,
   changed/new/missing-with-qualifier counts, no-change result or work items,
   primary safe next action and useful alternative, protected holds,
   cost/coverage and one continuation point. No verbose task avalanche.
7. **Persist only if authorized**, with checksum/readback as supported.
   A proposed checkpoint is NOT_SAVED, and a saved checkpoint is NOT proof
   of performed file operations. Retries using the same accepted snapshot
   should be idempotent, not duplicate writes or summarize old deltas again.
8. **Schedule only if specifically approved and actually supported**:
   owner chooses cadence and timezone, exact scoped source, batch/cost limit,
   private delivery destination, expiry/revocation, no-change behavior and
   duplicate-task policy. Read back created/updated schedule. No scheduler
   availability means NOT_CONFIGURED, not a guessed background service.
   Each scheduled run still checks current permission and source drift.

## Crucial distinctions

- UNCHANGED_NO_REWORK is conditional on caller-supplied matching evidence,
  not authentication that nothing changed in the real world.
- ABSENT_COMPLETE_SCOPE_REVIEW is a request to investigate a record absent
  from a host-attested complete listing, not permission to delete/archive.
- NOT_OBSERVED_PARTIAL_SCOPE must not become a deletion or missing-file fact.
- ACCESS_HOLD suppresses private record IDs and summary counts.
- EXTRACTION_REGRESSION_HOLD protects previously complete source knowledge
  from a partial replacement.
- An actual operation stays PROPOSED, APPROVED, EXECUTED, VERIFIED, FAILED,
  BLOCKED or ROLLED_BACK as separately evidenced under
  [operation-and-archive-rules.md](operation-and-archive-rules.md).
- Scheduled work cannot approve copy, move, shared indexing, disposition,
  access change, egress, archive expiry or deletion without fresh operation
  approval and available host tools.

## Optional offline reconciliation helper

The original standalone [reconcile.py](../scripts/reconcile.py) compares
two user/host-supplied synthetic-compatible JSON snapshots. It is NOT a file
crawler, permissions checker, content verifier, memory service, scheduler,
file mutation tool or connector. It reads no directories recursively and
never writes an output file. Python 3.9+ standard library:

    python3 scripts/reconcile.py --previous examples/maintenance-previous.json --current examples/maintenance-current.json
    python3 -m unittest discover -s tests -p 'test_*.py' -v

Input schema version 1 uses exactly snapshot_id, timezone-aware observed_at,
scope (collection_id, root_id, principal_id, audience_id), coverage
(complete/partial), viewer_check, and records. Each record has an opaque
stable record_id, locator_token, source_revision or null, extraction state,
digest plus digest_basis, and a current viewer_check assertion.
One snapshot is at most 1 MiB and 500 records. Unknown fields, duplicate
object keys, invalid tokens, nonfinite JSON and symlink paths are rejected.
The helper emits at most ten proposed delta actions, plus honest total
counts, and always reports checkpoint_written=false.

The helper cannot prove that an upstream read, source revision, snapshot
completeness, full-byte digest or viewer access was actually observed.
The caller-provided current-authorized status is a PRECONDITION ASSERTION,
not authentication. Concurrent malicious filesystem path swaps require
actual host-enforced isolated snapshots; lexical symlink checks are not a
sandbox. Its output ID tokens are intended only for the authorized audience.
No private account credential, path or raw document body should enter its
public fictional examples.

If previous and current snapshot IDs match with identical content, report
SAME_SNAPSHOT_NO_WORK. If they match with conflicting content, refuse. If
the source root/principal/audience changes, refuse cross-scope reuse. If
current access is denied, return ACCESS_HOLD without identifiers. Partial
current inventory does not confirm prior records were deleted.

## Scheduling contract

See [scheduled-maintenance-template.md](../examples/scheduled-maintenance-template.md)
for a complete user-reviewable recurring run instruction. The host MUST
establish explicit owner approval, actual scheduler support, current scoped
source access, permitted private checkpoint storage and notification channel,
bounded batch/recurrence, readback and stop policy. The instruction is
an example, NOT an active automation and NOT a grant of action authority.

Measure true utility only from independently observed results such as stale
search hits, actual successful retrieval, avoided redundant extraction,
processing time, false-missing decisions and safe verified file outcomes.
Offline method tests or a successful scheduler trigger do not prove improved
human recall, findability, recoverability or ADHD-related outcomes.

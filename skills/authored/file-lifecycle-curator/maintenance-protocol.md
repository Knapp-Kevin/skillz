# Required bundled procedure

The original detailed procedure below is normative. [SKILL.md](SKILL.md) determines activation, authorized scope, route, and mandatory closeout. Read the relevant phase in full before carrying it out. Missing or inaccessible guidance is a dependency hold: do not invent a procedure, execute a mutation, or assert completion. Relative links resolve from this package root.

## Incremental maintenance, safe recall and scheduled-agent handoff

Use [incremental-maintenance.md](references/incremental-maintenance.md) whenever
the user wants repeatable curation, source freshness, change-only updates,
periodic quality checks, resumable work, recall from an earlier run, or
integration with an actual authorized scheduler. **This is a separately
invoked phase of the same skill**, not a mandatory external memory/scheduler
service or an assumed persistent index.

1. **Recover evidence, never invent memory.** Identify the prior
   checkpoint only from the user-approved, host-accessible private
   destination. Verify current scope, viewer, original source IDs,
   revision types, snapshot completeness, index extraction coverage
   and actual accepted processing receipts. If absent or inaccessible,
   label COLD_START and proceed with current authorized data only.
   A past answer or triggered job is not an authenticated checkpoint.
2. **Reconcile incremental changes.** Compare current observed IDs,
   revisions, locator and extraction evidence to the authorized prior
   snapshot. Prioritize NEW/CHANGED/UNKNOWN/ACCESS_HOLD and avoid
   re-extracting confirmed unchanged content; report unresolved
   differences separately. A missing record in a PARTIAL scan is
   NOT_OBSERVED, not deleted. Even absent from a complete snapshot
   is review-only, not permission to remove any source or index.
   A currently permitted *collection listing* is insufficient to disclose
   a missing **previously cached record ID**: that record might now be
   excluded by per-item ACL. Require a distinct host-established current
   authorization for previously seen identities before outputting their
   names, IDs or summary counts. If not verified, use a detail-free
   absence access hold. When relocation coincides with reduced extraction
   coverage, keep EXTRACT_REGRESSION_HOLD visible alongside relinking.
3. **Do selective maintenance.** Recheck changed summaries, tags,
   link integrity, duplicate evidence, stale index results, archive
   holds and failed operations; keep full-source versus excerpt
   coverage explicit. Preserve verified work and never let partial
   output overwrite previously complete evidence as current.
   Only authorized writes with actual read-back change durable state.
4. **Produce a bounded continuation.** Report last accepted snapshot,
   what changed and actually ran, unchanged/skipped coverage,
   blocked/unknown work, one prioritized safe action and one
   genuinely useful alternative when available, stop condition,
   and whether the next checkpoint was truly saved. If an authorized
   visual organization plan exists, regenerate the observed/proposed/
   receipt-attested progress from the current source ledger, not
   a cached image or an old percentage.
5. **Durable opt-in state:** For genuinely repeatable hourly, daily
   and weekly runs, read
   [durable-state.md](references/durable-state.md) and reuse a
   **single host-approved private checkpoint** per exact principal,
   root and audience. Source snapshots, last-known per-record
   observations, accepted run receipts, and the last proposed/
   receipt-asserted organization plan are preserved transactionally.
   Compare-and-swap generation and unique run IDs prevent duplicate
   or stale agent writes. A PARTIAL observation never erases
   previously seen files; keep their last-seen times explicit.
   The optional [state.py](scripts/state.py) Python standard-library
   helper provides a real private SQLite checkpoint with read-only
   previews by default and explicit write opt-in. It does not
   authenticate a real source, maintain a permanent full-text index,
   verify physical moves, or perform any schedule. The host selects
   the private storage, approved retention, backups, encryption and
   cross-run access authority.
6. **Host-invoked cadence engine (no daemon).** The optional
   [maintenance.py](scripts/maintenance.py) helper checks the saved SQLite
   state and accepted-run journal for continuity before proposing bounded
   hourly/daily/weekly maintenance. It preserves state.py's authorization,
   generation-CAS and checkpoint semantics. Hourly targets changed records;
   daily and weekly can recommend quality/recovery audits even on no-change
   snapshots, without duplicate extraction or automatic writes. It does
   not perform the proposed index review or file operations; the host agent
   remains responsible for separately approved work and evidence. Read the
   [durable-state contract](references/durable-state.md) before use.
7. **Agent-host handoff.** Use [host_handoff.py](scripts/host_handoff.py) and [the host handoff contract](references/host-handoff.md) when a consuming agent supplies a new authorized source snapshot and current operation receipts. The helper reports a provisional comparison to the approved checkpoint. It does not authenticate a source, move files, persist an index, create a schedule or infer current progress from an old receipt. Any actual operation or checkpoint update remains a separately approved host action.
8. **Optional scheduled delivery.** Use the
   [scheduled-maintenance-template.md](examples/scheduled-maintenance-template.md)
   only as a user-reviewable handoff to a *real* scheduler the host
   supports. Require separately confirmed recurrence, timezone,
   root/principal/audience, retention/cost bounds, private delivery
   and storage permissions, stop/revocation rules and duplication
   protection. Do not auto-create or self-perpetuate scheduled tasks,
   reminders, agents, notification streams or checkpoints.
   A scheduler trigger does not prove a successful delivered result.

**Optional offline helper:** The separately usable,
[read-only source-delta calculator](scripts/reconcile.py) operates
only on explicit JSON snapshot input. The two
[fictional](examples/maintenance-previous.json)
[snapshots](examples/maintenance-current.json) and
[offline adversarial tests](tests/test_reconcile.py) illustrate the
state transition contract. Run from this complete package, where
Python 3.9+ is available and the input file paths were independently
approved by the host:

    python3 scripts/reconcile.py --previous examples/maintenance-previous.json --current examples/maintenance-current.json
    python3 -m unittest discover -s tests -p 'test_*.py' -v

No Python, trusted snapshot, previous checkpoint or actual scheduler
is required for the skill's ordinary text-only workflow. The
**read-only reconcile.py helper** does not scan files or folders,
authenticate access, verify supplied hashes, save a checkpoint,
write an index, create scheduled tasks, delete files or claim
model-host validation. The **separate opt-in state.py helper**
can persist a bounded private checkpoint *only* after explicit
owner-approved host storage, a supplied current authorized snapshot,
an affirmative commit flag and an expected generation. It still
does not touch originals or schedule recurring work. A tool-less host can
apply the same evidence/authority distinctions manually without
pretending the helper ran.

**Refinement learning boundary:** A reproducible broadly applicable
failure in source identity, access isolation, delta correctness or
false-success classification is a candidate for separately reviewed
canonical skill improvement. A user's desired cadence, taxonomy,
choice count, reminder style or output format is a local preference:
apply it in-session, persist only with specific consent and a real
private store, never turn it into global correctness policy.


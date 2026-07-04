# Gold-standard example — handoff-writer

One complete exemplar (per docs/skill-template.md §Capability floor rule 6: imitation transfers where instruction doesn't). Load only when writing a handoff; match its discipline, not its subject.

```markdown
# Handoff: gatekeeper 500s — 2026-07-04

## Definitions
- gatekeeper: the API service under investigation.
- gk-pool: Grafana dashboard tracking gatekeeper's DB connection-pool metrics.

## State
| Item | Status | Verified by |
|------|--------|-------------|
| Pool-exhaustion hypothesis | Disproven | gk-pool flat during incidents (annotation 14:02) |
| Root cause (race in cache.py invalidate_and_refresh) | Confirmed | log line `stale write after purge key=user:412` @ 13:47:22 |
| Fix (wrap sequence in with_lock('cache:'+key)) | Designed, NOT applied | nothing — no code written, no test run |

## Decisions
- Reuse existing with_lock() over new locking, because the primitive exists and must be reviewable before the freeze.

## Open threads
1. Apply fix — next action: wrap the full invalidate+refresh in cache.py with with_lock('cache:'+key); expect the stale-write log line to stop under a two-worker repro. Blocked on: nothing.
2. Review by Thursday — freeze starts Friday 17:00; unreviewed work cannot ship BEFORE the freeze. Blocked on: reviewer availability.

## Landmines
- Looks done, is not: the fix. Designed only — cache.py is unpatched.
- Looks done, is not: pool investigation — already disproven; do not re-chase.
- SECURITY: a live API token (sk-live-…) leaked into scratch notes. Value intentionally NOT reproduced here. Scrub the notes and rotate the token before anything else.

## Pointers
- cache.py — invalidate_and_refresh(), where the fix goes
- gatekeeper.log @ 13:47:22 — root-cause evidence
```

Why this is the standard: every "done" carries its verification (or an honest "nothing"); the deadline chain preserves direction (review BEFORE freeze); the leaked secret is warned about without being spread; disproven paths are marked dead so the successor doesn't relitigate.

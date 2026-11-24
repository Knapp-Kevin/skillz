# Effort Allocation Navigator: version history

This is the original first-party skill's source release history. Exact
Git source/package tree fingerprints, not this narrative, identify
the precise reviewed content. No hosted task system, persistent
memory or independently observed human outcome is claimed.

## 0.2.0 (2026-11-24): repeat-use continuity without task mutation

**ADHD-supportive, diagnosis-free design refinement:** The default
user-visible action is now a **specific 2–5-minute voluntary
micro-start** with a concrete stop line and a one-line re-entry
breadcrumb. `start_window_minutes` may be set to 2–10 for the
current run and is bounded by actual capacity and the claimed
task estimate. It is **not** a forced timer, a completion forecast
or a stored personal trait. No blame, productivity streak or
medical-effect claim is inferred from unchanged work.

**Scope-hardening:** Two-snapshot comparison now requires matching
caller-declared `scope_id` values. Missing/mismatched scope IDs
fail closed; even matching IDs require independently checked
viewer/source permission. This specifically guards accidental
cross-project task-ID collisions and stale-history reuse.

**Minor capability release**: an explicit authorized
`--previous` snapshot comparison added to the existing offline
`scripts/plan.py`. It labels caller-asserted completions and reopened
work separately; reports added, removed/unreconciled, dependency,
blocker, estimate and priority changes; and identifies newly
ready/blocked actions without persisting either snapshot.
A goal change is disclosed, missing source authentication is
not silently upgraded, and private labels/paths are never emitted.
The unchanged single-snapshot route still works.

The portable instructions now explain safe hourly/daily/weekly
continuity under a **host-controlled**, explicitly authorized
private snapshot supply. A text-only optional handoff from a
sales method cannot turn a buyer-facing suggestion into an
authorized task or evade a buyer opt-out.

This release keeps the original mandatory safety/deadline
precedence, one-primary/one-credible-alternative choice,
source identity limits, consented preferences, no automatic task
writes, and no persistent storage. New fictional examples and
regressions are included. **Why minor rather than patch:** the
stateless comparison is a new public user-visible planning
capability, not an editorial correction or automated release bump.

## 0.1.0 (2026-11-23): initial offline task allocation

First-party dependency-aware bounded-choice task prioritization,
optional Python 3.9+ read-only graph planner, original synthetic
fixtures, and blank preference schema. Initial and subsequent
adversarial passes merged source changes before v0.2.0 but
retained the `0.1.0` number; their Git source history is not
evidence of separately distributed immutable releases.

A structural test pass is not real task completion, real user
preference learning, independently observed host behavior,
or a psychological/ADHD outcome.

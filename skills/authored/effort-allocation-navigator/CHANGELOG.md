# Effort Allocation Navigator: version history

This is the original first-party skill's source release history. Exact
Git source/package tree fingerprints, not this narrative, identify
the precise reviewed content. No hosted task system, persistent
memory or independently observed human outcome is claimed.

## 0.3.0 (2026-11-24): focus continuity and task-identity integrity

**Deliberate minor release**, not a patch per test or document edit.

- Introduces optional current-run `focus_task_id`: a task explicitly
  chosen by the user remains primary when still eligible and near
  the top provisional score (within 85%) in the same priority lane.
  Mandatory safety, confirmed imminent deadlines, blocked work,
  completed claims, missing estimates and materially worse choices
  are not bypassed. Missing focus IDs return a categorical reason,
  not fabricated history or task completion.
- **Hardens two-snapshot task identity**: a recycled-looking ID whose
  task label or kind changed is held under `identity_review_ids`.
  Completion, reopening, readiness and resume claims for that ID
  do not proceed automatically. A normal task rename also produces
  review, not an accusation of ID recycling. Original task labels
  are never emitted by the offline helper.
- Adds 18 red-first adversarial regression cases and a fictional
  opt-in current-run focus example. The established single-snapshot
  format remains valid; the additional focus input is optional.
- Retains one primary and one meaningful alternative by default,
  voluntary micro-starts, no ADHD diagnosis or medical claims,
  read-only local execution, source permission gates, no stored
  user focus/preference history, and no automatic task mutations.

**Version rationale:** task selection now accepts an additional
explicit user choice with material runtime effects. That is a
new user-visible capability, so a minor version is warranted.
No claim of independent consuming-agent behavior, real user
engagement improvement, task completion or paid installation
follows from synthetic source-method tests.

**Evidence:** the adversarial test-only branch of PR #915 produced
a red 148-case run with 4 failures and 12 errors in the 18 new
cases, before changing the original planner. Subsequent
source corrections must pass the entire test suite and
the exact package fingerprint/review gates before merge.

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

# Effort Allocation Navigator

**A portable first-party task-dependency and bounded-choice skill.**
Its principal user-facing output is **one recommended next action plus
one meaningful alternative**, not another task dump or an autonomous agent.

The [SKILL.md](SKILL.md) explains how to turn ordinary task language into
a dependency graph, distinguish real blockers from optional sequencing,
prioritize consequences over busywork, preserve owner deadlines and safety
constraints, and route generic quality corrections separately from
user-specific pacing and presentation preferences.

## User-selected focus mode (v0.3.0)

A task planner can create avoidable friction by changing its top
recommendation on each refresh. The optional `focus_task_id` root
field lets a **current user-selected task** remain the recommended
primary when its work is still ready, its evidence is usable, and
its provisional score is at least 85% of the highest score **in
the same protected lane**:

```sh
python3 scripts/plan.py --input examples/fictional-user-focus.json
```

The original default is unchanged when no `focus_task_id` is
provided. An explicit focus is *not* a forced daily streak,
a diagnosis, a record of prior activity, or proof the task was
started. If it is blocked, completed, absent or unsupported by
estimates, the planner returns a categorical `focus_resolution`
rather than promoting the task. Real safety work, owner-confirmed
imminent deadlines and materially different opportunity costs
override this continuity preference. The user still owns the
choice.

**Task identity is a separate concern.** When comparing two
authorized snapshots, a matching task ID whose **label or kind
changed** is now flagged under `identity_review_ids`. Completion,
reopening, newly ready/blocked and automatic resume claims for
that row are held until the host/user verifies that it truly
represents the same work. A renamed task may be legitimate,
so the result is an evidence-review request, **not** a declaration
of ID recycling. No task labels or paths are printed in the
JSON output.

These are accessibility-oriented continuity controls, not
clinical treatment or measured improvements in user attention.

## Repeat-use mode, still passive

Since **0.2.0**, a bounded optional comparison is available between two
**separately authorized** local JSON snapshots. No history is
automatically found, saved, polled, installed or synchronized:

```sh
python3 scripts/plan.py \
  --previous examples/fictional-tasks.json \
  --input examples/fictional-tasks-next.json
```

The ordinary `--input` path remains unchanged. A `transition`
block reports **only task IDs and categorical changes**, with
ambiguous same-ID label/type changes separately held for identity review: claimed
completed, reopened, new, removed-but-unreconciled, changed
dependencies/blockers/priorities/estimates, and newly ready or blocked.
Removing a task from the snapshot is **not completion**, and task
state `done` is merely the caller's claim until independently checked.
An earlier date on the purported newer snapshot is invalid. Two
same-day snapshots have caller-specified order, not authenticated
source chronology. Goal changes are disclosed rather than treated as
progress toward the old objective.

A two-snapshot comparison requires a matching, **non-sensitive**
`scope_id` in each snapshot; absent or differing scope IDs fail closed.
This is a caller-declared namespace, **not** external authentication.
The host must re-check **current permissions and source/task-ID
namespace compatibility for both snapshots before providing them**;
this helper cannot authenticate external sources. If an old task
record is no longer authorized, do not call the comparison or print
old private task IDs, labels or counts. Outputs never include labels,
file paths or raw task content, but task IDs themselves may be
sensitive and must remain inside the authorized host. For repeated
work, the user-visible output should still prioritize one next
action, one credible alternative and a small proof/stop condition,
rather than a growing history dashboard.

Optional sales-method task handoffs are just text proposals; buyer
contact/sending/booking stays blocked until explicit authorization.
They do not install or require a second skill or create tasks.

## ADHD-supportive default, no diagnosis required

The recommended action must be **startable**, not merely ranked.
Prefer one explicit physical or digital first move with a visible
stop condition, a voluntary five-minute starter window, and at most
one meaningful alternative. A user can choose a different 2–10 minute
starter, a longer focus slice, or a pause. Neither a timer nor a
medical-history disclosure is required. Low available capacity
changes the **entry step**, not mandatory safety, actual completion
checks, or the user's authority.

A compact re-entry note externalizes where to resume after a pause:
`objective | last_observed_step | next_visible_action | blocker |
proof_needed`. It is only a note from authorized current context,
not persistent memory. An unchanged snapshot is **not evidence of
a person's motivation or an ADHD symptom**, and a suggested
micro-start never proves task completion. The offline helper emits
controlled ID-only cue codes, leaving actual task-specific wording
to the authorized host/user. Choice reduction and shorter chunks
are practical accessibility affordances, **not verified clinical
benefits**.

## Package

- [scripts/plan.py](scripts/plan.py) is an **optional**, deterministic,
  read-only Python 3.9+ helper; it never connects to a task service or
  stores task histories. It operates on a locally approved JSON snapshot.
- [CHANGELOG.md](CHANGELOG.md) records the intentional version change.
- [examples/fictional-user-focus.json](examples/fictional-user-focus.json) is
  an original fictional current-run focus example, with no real task records.
- [tests/test_focus_identity_adversarial.py](tests/test_focus_identity_adversarial.py)
  protects identity-review and chosen-focus priority boundaries.
- [examples/fictional-tasks-next.json](examples/fictional-tasks-next.json) is
  a synthetic second snapshot for repeat-use comparisons.
- [tests/test_continuity.py](tests/test_continuity.py) guards progress,
  deletion/reopening semantics, and privacy; static tests cannot
  verify genuine task changes.
- [examples/fictional-tasks.json](examples/fictional-tasks.json) is
  entirely fictional; do not put real task content in the public package.
- [examples/acceptance.md](examples/acceptance.md) gives positive,
  negative, boundary and multi-turn situations for actual consumer trials.
- [tests/test_plan.py](tests/test_plan.py) contains executable positive
  and planted-adversarial source-method tests.
- [preferences/README.md](preferences/README.md) and
  [preferences/schema.json](preferences/schema.json) define a **public,
  empty-identity** allowlist for optional private user preferences.
  No user overlay, preference manager, collector or telemetry ships.

Run only with an explicitly authorized private input file:

    python3 scripts/plan.py --input examples/fictional-tasks.json
    python3 -m unittest discover -s tests -p 'test_*.py' -v

The helper expects:
- root keys: schema_version=1, as_of=YYYY-MM-DD (explicit local date),
  optional `focus_task_id` (current-run, explicitly selected user task),
  optional `scope_id` (required for a two-snapshot comparison),
  optional capacity_minutes, optional goal_id (must be an actual milestone),
  optional preferences and 1–200 tasks. A scope ID is a neutral
  stable slug, never a real customer name or credential.
- each task has a slug id, optional private label, optional state
  (todo/doing/done), optional kind (action/milestone), depends_on IDs
  forming an acyclic directed graph, optional effort_minutes (time
  actively spent), optional duration_days (elapsed duration for a
  modeled parallel dependency path), value (ordinal 1–5) and urgency
  (ordinal 0–3). Unknown values are null or omitted, never zero.
- obligation: discretionary/committed/safety. This is **caller-supplied**;
  only actual host/user authorization can verify it. External blockers
  are separate boolean flags. A due_date is not a hard priority unless
  deadline_evidence is explicitly owner-confirmed.
- preferences: choice_count 1–3 (default **2**), pace
  balanced/short-sprints (default balanced) and optional
  `start_window_minutes` 2–10 (default **5**) for a voluntary
  task-activation window. These fields **do not save preferences**.

**Scores:** a documented ordinal *sorting heuristic* combining
task value, urgency, real downstream/unblock leverage, working-state
continuity, modeled path membership and a tempered effort denominator.
A short-sprints setting only changes tradeoffs within the eligible
priority lane. Downstream declared safety or owner-confirmed imminent
deadlines are propagated to unfinished hard prerequisites even when
the owner selects a separate focus goal; off-goal mandatory obligations
are reported as focus exceptions. These source claims are not independently
authenticated. Safety and owner-confirmed near deadlines take precedence. It does
not infer dollars, actual task impact, user condition, expected task
duration or verified commitment from the JSON values. Unscored
ready tasks are called out. Missing safety/near-deadline estimates
hold the comparison and produce an estimation action.

**Outputs:** task IDs only (no original free-text task labels),
the primary and at most one alternative by default, reason codes,
a **2–5-minute default micro-start** bounded by task estimate/capacity,
plus a 25-minute-or-less optional focus slice, fit to stated capacity if supplied,
blocked prerequisites, provisional scoring strategy, focus-scope exception
IDs, explicit deferral warning on lower-lane alternatives, comparison
coverage and conditional modeled critical path. The helper refuses
DONE claims contradicted by incomplete mandatory prerequisites.
It classifies unexpanded, externally blocked and acceptance-pending
milestones separately, rather than inventing an executable action.
It prefers a differently useful alternative when comparable without
promoting a substantially lower-value task merely for variety.
Even two choices in the same mandatory safety/deadline lane are not
interchangeable; choosing the alternative defers the primary start.
The host translates IDs to an actual approved, concrete
next action with stop line and evidence. An optional third choice must
be explicitly requested, and a single real choice must not be padded.

**Critical path:** computed ONLY with a selected, expanded milestone
and every unfinished antecedent having a distinct *elapsed duration*,
no unknown external dependency and a declared model of unlimited
parallel work. A milestone must have zero duration; positive values
are rejected rather than silently ignored. An unfinished unexpanded
goal reports UNEXPANDED_MILESTONE, not a zero-day project.
An externally blocked milestone is permitted, but its unknown wait
prevents a qualified critical-path duration.
It is NOT a personal resource-constrained schedule and is never
calculated from effort minutes. Without these inputs, return
NO_SELECTED_MILESTONE, GOAL_NOT_A_MILESTONE,
DURATION_DATA_INCOMPLETE or EXTERNAL_DURATION_UNBOUNDED.

**Security:** 1 MiB input cap; rejects malformed and nonfinite JSON,
duplicate object keys, invalid IDs, dependency cycles, unknown fields,
large graphs, symlink input files and symlink ancestors. The helper
opens only the single explicit local path, reads and returns JSON to
stdout, and performs no network, task mutation, storage or
authentication. Filesystems with concurrently mutable paths require
host-enforced snapshot isolation; lexical checks are not a sandbox.

**Qualification limitations:** These tests establish local Python
graph/refusal behavior for synthetic data only. They cannot show that
an AI model normalized messy tasks correctly, that the user chose
the recommended work, that work was completed, or that ADHD-related
choice reduction improved an individual outcome. Such assertions
need separately approved real-user/host trials, baseline comparison
and evidence. No skill or example text grants authority to take over
task decisions.

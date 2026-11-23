# Effort Allocation Navigator

**A portable first-party task-dependency and bounded-choice skill.**
Its principal user-facing output is **one recommended next action plus
one meaningful alternative**, not another task dump or an autonomous agent.

The [SKILL.md](SKILL.md) explains how to turn ordinary task language into
a dependency graph, distinguish real blockers from optional sequencing,
prioritize consequences over busywork, preserve owner deadlines and safety
constraints, and route generic quality corrections separately from
user-specific pacing and presentation preferences.

## Package

- [scripts/plan.py](scripts/plan.py) is an **optional**, deterministic,
  read-only Python 3.9+ helper; it never connects to a task service or
  stores task histories. It operates on a locally approved JSON snapshot.
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
  optional capacity_minutes, optional goal_id (must be an actual milestone),
  optional preferences and 1–200 tasks.
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
- preferences: choice_count 1–3 (default **2**) and pace
  balanced/short-sprints (default balanced), currently scoped to the
  input run. These fields **do not save preferences**.

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
a 25-minute-or-less first slice, fit to stated capacity if supplied,
blocked prerequisites, provisional scoring strategy, focus-scope exception
IDs, explicit deferral warning on lower-lane alternatives, comparison
coverage and conditional modeled critical path. The helper refuses
DONE claims contradicted by incomplete mandatory prerequisites.
It prefers a differently useful alternative when comparable without
promoting a substantially lower-value task merely for variety.
The host translates IDs to an actual approved, concrete
next action with stop line and evidence. An optional third choice must
be explicitly requested, and a single real choice must not be padded.

**Critical path:** computed ONLY with a selected milestone and every
unfinished antecedent having a distinct *elapsed duration*, no unknown
external dependency and a declared model of unlimited parallel work.
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

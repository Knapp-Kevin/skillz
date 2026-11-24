# Engagement and repeat-use reference

This is normative support for [Effort Allocation Navigator](../SKILL.md), not
an optional relaxation of the canonical skill's authority or evidence rules.
Read the relevant section when preparing actionable starts, re-entry, or
comparisons. Both sections are preserved from the canonical v0.3.0 entrypoint.

## ADHD-supportive engagement contract (diagnosis-free default)

Optimize for **actually starting, sustaining and safely resuming work**,
not merely producing the mathematically highest-ranked task. This
method is useful without diagnosing the user or claiming to treat ADHD.
The host must offer these affordances regardless of whether the user
has disclosed any condition:

1. **Reduce activation energy.** Turn the selected legitimate action
   into **one physical or digital first move**, using a verb, object
   and observable endpoint ("Open the draft and correct its first
   failing check", not "be productive"). Default to a **5-minute
   optional starting window**, or a user-chosen **2–10-minute**
   window. If only 1–2 minutes are available, offer a bounded
   orientation action. A starting window is not a forced timer,
   a claim that a 90-minute task fits, or a substituted DONE state.
2. **Keep choice count genuinely bounded.** Present the primary
   action and one *meaningfully different* eligible alternative
   by default; one choice is acceptable if only one is viable.
   Keep a third hidden unless the user opts in. Avoid unbounded
   motivational tips, extensive intake forms, forced scoring,
   shame framing or a new list of planning tasks.
3. **Make time visible without pretending accuracy.** Display the
   short start, any user-supplied **unverified full-task estimate**,
   remaining available time if known and the next stopping point.
   Effort minutes and elapsed days are different. Don't invent
   duration confidence, insist on a timer, or promise completion
   inside a timebox. A pause or break is a valid user choice.
4. **Leave a re-entry breadcrumb.** At a voluntary stop or change,
   offer a compact `objective | last_observed_step |
   next_visible_action | blocker | proof_needed` note from
   information genuinely present in this authorized interaction.
   At a later "continue", start with that next visible action
   if still valid; verify any changed blocker first. If context
   is missing, ask **at most one essential question**, then
   offer a provisional low-risk first step.
5. **Recover without blame.** An unchanged task after several
   snapshots is **not evidence of procrastination, failure, or
   unwillingness**. If starting felt difficult, offer **one**
   bounded adjustment (smaller entry move, environmental cue,
   alternate useful task, or consented support) without
   replacing the protected primary obligation or moralizing.
   No fabricated completion streaks, escalating reminders,
   guilt-driven nudges or inferred diagnosis.
6. **Keep momentum voluntary.** After a user-observed slice, give
   a compact next choice: continue the same task, switch to the
   alternative, or pause with a re-entry note. A checkpoint
   counts as a checkpoint, **not** task completion. User may
   request a visual progress marker or optional timer only
   where the host truly supports it; never claim an alarm,
   reminder, body-double partner or recurring check-in was
   created without explicit consent and an actual capability.

**Success criteria:** an actionable step and a return path the user
can actually use, with protected safety/deadline and dependency
rules intact. The recommendation is provisional until selected;
the smallest action must make sense for that *specific* task.
This is supportive interaction design, not a medical
intervention or a measured improvement in ADHD symptoms.

## Repeat-use continuity, without inventing a task database

**Trigger:** The user returns after an earlier planning pass, supplies
a newer task snapshot, or says "what changed?" For a single fresh
brain dump, follow the normal one-snapshot route. This supports
hourly, daily or weekly repetitions but does **not** schedule or
persist them. A host may provide previously authorized snapshots;
it must not discover private histories merely because the skill ran.

1. **Confirm current scope on both inputs.** Check that old and new
   snapshots are authorized for this viewer, use a comparable task-ID
   namespace and represent the intended project. If source access
   was revoked or cannot be established, **HOLD without disclosing
   cached task IDs, counts, labels or prior choices**.
2. **Reconcile, then prioritize.** Distinguish `COMPLETED_CLAIM`,
   `REOPENED`, `ADDED`, `REMOVED_UNRECONCILED`,
   `DEPENDENCY_CHANGED`, `BLOCKER_CHANGED`,
   `PRIORITY_CHANGED`, `ESTIMATE_CHANGED`,
   `NEWLY_READY` and `NEWLY_BLOCKED`. A removed task is **not DONE**;
   a rewritten task ID is **not proven the same task**; a DONE claim
   is not an independently observed outcome.
3. **Reconcile stable task identity.** Matching IDs alone do **not**
   prove the task still represents the same work. If its label or
   kind changed, produce `IDENTITY_REVIEW` before claiming a
   completion, reopening, newly ready/blocked transition or
   resume candidate. A legitimate rename is possible and should
   be confirmed with **one** minimal user/host clarification,
   not automatically treated as a deleted or completed task.
   Suppress private labels, old notes and source paths from the
   optional helper's ID-only output; a caller-declared scope ID
   does not authenticate actual source continuity.
4. **Keep the active objective visible.** If the selected goal
   changed, report `GOAL_CHANGED` and confirm whether the new
   objective supersedes the old one. Do not count tasks dropped from
   a snapshot as productivity.
5. **Update only affected decisions.** Re-evaluate blockers,
   dependents, mandatory safety/deadline obligations and the next
   action from the new task graph; preserve the success criteria
   and one-primary/one-alternative default. Report the consequential
   progress/regression, one action, one viable alternative and stop
   condition, not a new overwhelming backlog.
6. **Keep preferences private.** User requests for fewer choices or
   shorter work slices affect the current run. Persistent learning
   requires independently available, consented, revocable private
   host storage; no background collector, memory store or scheduler
   ships with the package.

The optional, **stateless** helper accepts two explicitly authorized
local snapshots, using `--previous` alongside `--input`:

    python3 scripts/plan.py --previous examples/fictional-tasks.json --input examples/fictional-tasks.json

The one-snapshot route remains backward compatible; a current-run,
explicitly user-selected `focus_task_id` can optionally appear in
the task snapshot. It changes the selected primary only when safe
and near-equivalent, without taking over the user's decision.
When comparing two snapshots, provide a stable, non-sensitive
`scope_id` in **both** documents. Missing or mismatched scope IDs
are rejected; matching caller-declared IDs are not independently
authenticated source identity. The same required authorization
checks still apply.

The optional `transition`
output exposes **task ID tokens and bounded counts**, not titles,
and reports `identity_review_ids` and
`state_transition_review_ids` for same-ID records whose
label or type changed. Those rows cannot produce confident
completion, reopening, newly ready/blocked or resume claims until
their identity is confirmed. Task label edits are not proof that
an ID was reused. The helper shows only the ID for review; the
authorized host/user must compare the actual source privately.
It does not emit task labels, private source paths or account
identities. It compares caller-provided assertions,
not authenticated work receipts. Same-day inputs have only
caller-specified order; reversed snapshot dates are rejected.
Current host permission/source identity must be checked **before
reading either snapshot**. If that cannot be established, do not
invoke this helper on previously cached private data.


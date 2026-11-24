#!/usr/bin/env python3
"""Offline task-dependency and bounded-choice planner.

This is an arithmetic/graph helper, not an authority or user-preference store.
Only canonical ID tokens are emitted; task labels remain private input data.
Python 3.9+ standard library, deterministic, no network or writes.
"""
import argparse
import datetime as dt
import json
import math
import pathlib
import re
import stat
import sys

MAX_BYTES = 1024 * 1024
MAX_TASKS = 200
ID_RE = re.compile(r"^[a-z][a-z0-9-]{1,63}$")
ROOT_KEYS = {"schema_version", "as_of", "capacity_minutes", "goal_id", "preferences", "tasks"}
TASK_KEYS = {
    "id", "label", "kind", "state", "depends_on", "effort_minutes", "duration_days",
    "value", "urgency", "obligation", "external_blocker", "due_date",
    "deadline_evidence",
}
PREF_KEYS = {"choice_count", "pace"}
STATES = {"todo", "doing", "done"}
OBLIGATIONS = {"discretionary", "committed", "safety"}
EVIDENCE = {"none", "claimed", "owner-confirmed"}
PACES = {"balanced", "short-sprints"}


class Invalid(Exception):
    pass


def refuse(condition):
    if not condition:
        raise Invalid("INVALID_INPUT")


def integer(value, minimum, maximum):
    refuse(type(value) is int and minimum <= value <= maximum)
    return value


def iso_date(value):
    refuse(type(value) is str and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value) is not None)
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise Invalid("INVALID_INPUT") from exc


def validate(document):
    refuse(type(document) is dict and set(document) <= ROOT_KEYS)
    refuse(document.get("schema_version") == 1 and type(document.get("schema_version")) is int)
    today = iso_date(document.get("as_of"))
    capacity = document.get("capacity_minutes")
    if capacity is not None:
        integer(capacity, 1, 10080)
    goal = document.get("goal_id")
    if goal is not None:
        refuse(type(goal) is str and ID_RE.fullmatch(goal) is not None)
    prefs = document.get("preferences", {})
    refuse(type(prefs) is dict and set(prefs) <= PREF_KEYS)
    count = integer(prefs.get("choice_count", 2), 1, 3)
    pace = prefs.get("pace", "balanced")
    refuse(type(pace) is str and pace in PACES)
    entries = document.get("tasks")
    refuse(type(entries) is list and 1 <= len(entries) <= MAX_TASKS)
    tasks = {}
    for item in entries:
        refuse(type(item) is dict and set(item) <= TASK_KEYS)
        key = item.get("id")
        refuse(type(key) is str and ID_RE.fullmatch(key) is not None and key not in tasks)
        label = item.get("label", "")
        refuse(type(label) is str and len(label) <= 160 and
               not any(ord(char) < 32 for char in label))
        state = item.get("state", "todo")
        kind = item.get("kind", "action")
        obligation = item.get("obligation", "discretionary")
        external = item.get("external_blocker", False)
        refuse(type(state) is str and type(kind) is str
               and type(obligation) is str and state in STATES
               and kind in {"action", "milestone"}
               and obligation in OBLIGATIONS and type(external) is bool)
        deps = item.get("depends_on", [])
        refuse(type(deps) is list and len(deps) <= MAX_TASKS and
               len(set(str(x) for x in deps)) == len(deps))
        refuse(all(type(x) is str and ID_RE.fullmatch(x) for x in deps))
        effort = item.get("effort_minutes")
        elapsed = item.get("duration_days")
        value = item.get("value")
        urgency = item.get("urgency", 0)
        if effort is not None:
            integer(effort, 1, 10080)
        if elapsed is not None:
            integer(elapsed, 0 if kind == "milestone" else 1, 365)
        if value is not None:
            integer(value, 1, 5)
        integer(urgency, 0, 3)
        if kind == "milestone":
            # Milestones represent zero-duration gates, not executable
            # work. External approvals are legitimate non-executable
            # blockers; their elapsed wait is unknown unless modeled as
            # a separate action with supported duration.
            refuse(effort is None and value is None)
            refuse(elapsed is None or elapsed == 0)
        due = item.get("due_date")
        if due is not None:
            iso_date(due)
        evidence = item.get("deadline_evidence", "none")
        refuse(type(evidence) is str and evidence in EVIDENCE)
        if evidence != "none":
            refuse(due is not None)
        tasks[key] = {
            "id": key, "state": state, "kind": kind, "obligation": obligation,
            "external_blocker": external, "depends_on": deps,
            "effort_minutes": effort, "duration_days": elapsed, "value": value,
            "urgency": urgency, "due_date": due, "deadline_evidence": evidence,
        }
    if goal is not None:
        refuse(goal in tasks)
    for task in tasks.values():
        refuse(all(dep in tasks and dep != task["id"] for dep in task["depends_on"]))
    # Full graph, including out-of-goal tasks, must be acyclic and internally consistent.
    colors = {}
    def visit(key):
        shade = colors.get(key, 0)
        refuse(shade != 1)
        if shade == 2:
            return
        colors[key] = 1
        for dep in tasks[key]["depends_on"]:
            visit(dep)
        colors[key] = 2
    for key in sorted(tasks):
        visit(key)
    # A completed dependent with unfinished mandatory prerequisites is
    # contradictory input, not completion evidence. Refuse false progress.
    for task in tasks.values():
        if task["state"] == "done":
            refuse(all(tasks[dep]["state"] == "done"
                       for dep in task["depends_on"]))
    return tasks, today, goal, capacity, count, pace


def ancestors(tasks, key):
    result = set()
    def add(node):
        if node in result:
            return
        result.add(node)
        for dep in tasks[node]["depends_on"]:
            add(dep)
    add(key)
    return result


def critical_path(tasks, goal, scope):
    if goal is None:
        return {"status": "NO_SELECTED_MILESTONE", "path": []}
    if tasks[goal]["kind"] != "milestone":
        return {"status": "GOAL_NOT_A_MILESTONE", "path": []}
    if any(tasks[key]["external_blocker"] and tasks[key]["state"] != "done"
           for key in scope):
        return {"status": "EXTERNAL_DURATION_UNBOUNDED", "path": []}
    if any(tasks[key]["kind"] == "milestone" and
           tasks[key]["state"] != "done" and
           not tasks[key]["depends_on"] and
           not tasks[key]["external_blocker"] for key in scope):
        return {"status": "UNEXPANDED_MILESTONE", "path": []}
    if any(tasks[key]["duration_days"] is None and
           not (tasks[key]["kind"] == "milestone" or tasks[key]["state"] == "done")
           for key in scope):
        return {"status": "DURATION_DATA_INCOMPLETE", "path": []}
    memo = {}
    def longest(key):
        if key in memo:
            return memo[key]
        current = tasks[key]
        span = 0 if current["state"] == "done" or current["kind"] == "milestone" else current["duration_days"]
        branches = [longest(dep) for dep in sorted(current["depends_on"]) if dep in scope]
        previous = max(branches, key=lambda v: (v[0], tuple(reversed(v[1])))) if branches else (0, [])
        memo[key] = (span + previous[0], previous[1] + [key])
        return memo[key]
    days, path = longest(goal)
    return {
        "status": "MODELED_UNLIMITED_PARALLELISM",
        "path": path, "duration_days": days,
        "warning": "Dependency-only lower bound, not a resource-constrained delivery forecast.",
    }


def plan(document):
    tasks, today, goal, capacity, choice_count, pace = validate(document)
    goal_scope = ancestors(tasks, goal) if goal else set(tasks)
    scope = set(goal_scope)
    # A chosen project goal is a focus lens, not an authority to suppress
    # independently mandatory safety or owner-confirmed imminent work.
    for key, task in tasks.items():
        if task["state"] == "done":
            continue
        confirmed_due = (
            task["deadline_evidence"] == "owner-confirmed"
            and (iso_date(task["due_date"]) - today).days <= 2
        )
        if task["obligation"] == "safety" or confirmed_due:
            scope.update(ancestors(tasks, key))
    scope_extensions = sorted(scope - goal_scope)
    incomplete = {key for key in scope if tasks[key]["state"] != "done"}
    if not incomplete:
        return {"status": "PROVISIONAL_CALLER_ASSERTIONS", "mode": "COMPLETE",
                "choices": [], "critical_path": critical_path(tasks, goal, goal_scope),
                "scope_extension_ids": scope_extensions,
                "completion_status": "CALLER_ASSERTED_NOT_INDEPENDENTLY_VERIFIED",
                "coverage": {"considered": len(scope), "ready": 0, "blocked": 0, "unscored": 0}}
    path = critical_path(tasks, goal, goal_scope)
    ready, blocked = [], []
    needs_decomposition, needs_verification = [], []
    for key in sorted(incomplete):
        task = tasks[key]
        missing = sorted(dep for dep in task["depends_on"]
                         if tasks[dep]["state"] != "done")
        if missing or task["external_blocker"]:
            blocked.append({"task_id": key, "waiting_for": missing,
                            "external_blocker": task["external_blocker"]})
        elif task["kind"] == "action":
            ready.append(key)
        elif not task["depends_on"]:
            # A milestone is not an action. A bare, nonexternal
            # unfinished milestone has no executable work defined.
            needs_decomposition.append(key)
        else:
            # All predecessors are declared done; the milestone itself
            # still lacks acceptance evidence. Do not mark it DONE.
            needs_verification.append(key)

    def assessment_choice(ids, action, mode):
        chosen = ids[:choice_count]
        return {
            "status": "PROVISIONAL_CALLER_ASSERTIONS", "mode": mode,
            "choices": [{"task_id": key,
                         "role": "primary" if i == 0 else "alternative",
                         "action": action} for i, key in enumerate(chosen)],
            "critical_path": path,
            "scope_extension_ids": scope_extensions,
            "needs_decomposition_ids": needs_decomposition,
            "needs_verification_ids": needs_verification,
            "blocked": blocked,
            "unscored_task_ids": [],
            "coverage": {"considered": len(scope), "ready": len(ready),
                         "blocked": len(blocked), "unscored": 0},
        }

    def protected_milestone(key):
        task = tasks[key]
        return (
            task["obligation"] == "safety"
            or (task["deadline_evidence"] == "owner-confirmed"
                and (iso_date(task["due_date"]) - today).days <= 2)
        )

    # A mandatory but unexpanded obligation must not vanish behind
    # a lower-priority scored task merely because it has no action row.
    urgent_decomposition = [key for key in needs_decomposition
                            if protected_milestone(key)]
    if urgent_decomposition:
        return assessment_choice(urgent_decomposition,
                                 "DEFINE_REQUIRED_NEXT_STEP",
                                 "NEEDS_DECOMPOSITION")
    urgent_verification = [key for key in needs_verification
                           if protected_milestone(key)]
    if urgent_verification:
        return assessment_choice(urgent_verification,
                                 "CONFIRM_MILESTONE_COMPLETION",
                                 "NEEDS_VERIFICATION")
    scored, unscored = [], []

    def exposure(key):
        """Protected obligations propagate through real dependency edges."""
        desc = [later for later in incomplete if later != key
                and key in ancestors(tasks, later)]
        related = [key] + desc
        safety = any(tasks[item]["obligation"] == "safety"
                     for item in related)
        deadlines = [
            ((iso_date(tasks[item]["due_date"]) - today).days, item)
            for item in related
            if tasks[item]["deadline_evidence"] == "owner-confirmed"
        ]
        due, source = min(deadlines) if deadlines else (None, None)
        return desc, safety, due, source

    for key in ready:
        task = tasks[key]
        if task["effort_minutes"] is None or task["value"] is None:
            unscored.append(key)
            continue
        downstream, safety, deadline, deadline_source = exposure(key)
        immediate = sum(1 for later in downstream if all(
            tasks[dep]["state"] == "done" or dep == key
            for dep in tasks[later]["depends_on"]))
        lane = 0 if safety else (
            1 if deadline is not None and deadline <= 2 else 2)
        base = (4 * task["value"] + 2 * task["urgency"] +
                3 * min(3, immediate) + min(3, len(downstream)) +
                (2 if task["state"] == "doing" else 0) +
                (4 if key in path["path"] and path["status"] == "MODELED_UNLIMITED_PARALLELISM" else 0) +
                (3 if deadline is not None and deadline <= 7 else 0))
        score = base / math.sqrt(1 + task["effort_minutes"] / 120)
        if pace == "short-sprints" and task["effort_minutes"] <= 30:
            score += 2
        reasons = []
        if lane == 0:
            reasons.append("DECLARED_SAFETY_OBLIGATION" if
                           task["obligation"] == "safety" else
                           "UNLOCKS_DECLARED_SAFETY_OBLIGATION")
        elif lane == 1:
            reasons.append("OWNER_CONFIRMED_NEAR_DEADLINE" if
                           deadline_source == key else
                           "UNLOCKS_OWNER_CONFIRMED_DEADLINE")
        if immediate:
            reasons.append("UNLOCKS_IMMEDIATE_DEPENDENTS")
        if key in path["path"] and path["status"] == "MODELED_UNLIMITED_PARALLELISM":
            reasons.append("ON_MODELED_CRITICAL_PATH")
        if task["effort_minutes"] <= 30:
            reasons.append("SHORT_BOUNDED_ACTION")
        if task["state"] == "doing":
            reasons.append("CONTINUE_IN_PROGRESS")
        if not reasons:
            reasons.append("HEURISTIC_VALUE_EFFORT")
        strategy = ("CONTINUE" if task["state"] == "doing" else
                    "UNBLOCK" if immediate else
                    "SHORT_WIN" if task["effort_minutes"] <= 30 else
                    "FOCUS_WORK")
        scored.append({"task_id": key, "lane": lane, "score": round(score, 1),
                       "_sort_score": score, "strategy": strategy,
                       "effort_minutes": task["effort_minutes"], "reasons": reasons,
                       "immediate_unlocks": immediate,
                       "confirmed_deadline_source_id": deadline_source})
    # Never silently rank a safety/near-deadline candidate below unrelated
    # optional work merely because its estimate is missing.
    urgent_unknown = []
    for key in unscored:
        _, safety, deadline, _ = exposure(key)
        if safety or (deadline is not None and deadline <= 2):
            urgent_unknown.append(key)
    if urgent_unknown:
        chosen = urgent_unknown[:choice_count]
        return {
            "status": "PROVISIONAL_CALLER_ASSERTIONS", "mode": "NEEDS_PRIORITY_EVIDENCE",
            "choices": [{"task_id": key, "role": "primary" if i == 0 else "alternative",
                         "action": "ESTIMATE_OR_CONFIRM"} for i, key in enumerate(chosen)],
            "critical_path": path, "unscored_task_ids": unscored,
            "scope_extension_ids": scope_extensions, "blocked": blocked,
            "needs_decomposition_ids": needs_decomposition,
            "needs_verification_ids": needs_verification,
            "coverage": {"considered": len(scope), "ready": len(ready),
                         "blocked": len(blocked), "unscored": len(unscored)},
        }
    scored.sort(key=lambda x: (x["lane"], -x["_sort_score"], x["task_id"]))
    selected = scored[:1]
    rest = scored[1:]
    # An alternative should offer a meaningful different way to progress
    # when one exists at similar value within the SAME protected lane.
    # Never diversify by replacing an urgent obligation with a lesser one.
    while rest and len(selected) < choice_count:
        anchor = selected[0]
        first = rest[0]
        different = next((
            item for item in rest
            if item["lane"] == anchor["lane"]
            and item["strategy"] not in {row["strategy"] for row in selected}
            and item["_sort_score"] >= 0.7 * first["_sort_score"]
        ), None)
        chosen = different if different is not None else first
        selected.append(chosen)
        rest.remove(chosen)
    for index, row in enumerate(selected):
        row["priority_lane"] = (
            "MANDATORY_SAFETY" if row.pop("lane") == 0 else
            "CONFIRMED_IMMINENT_DEADLINE" if (
                row["confirmed_deadline_source_id"] is not None and
                (iso_date(tasks[row["confirmed_deadline_source_id"]]["due_date"]) - today).days <= 2
            ) else "DISCRETIONARY"
        )
        row.pop("_sort_score")
        row["role"] = "primary" if index == 0 else "alternative"
        row["action"] = "BEGIN_USER_CONFIRMED_STEP"
        row["first_slice_minutes"] = min(25, capacity or 25, row["effort_minutes"])
        row["fits_available_capacity"] = (
            None if capacity is None else row["effort_minutes"] <= capacity
        )
        # Even equal-lane mandatory actions remain independent obligations.
        # Choosing one to begin does not discharge the other.
        row["requires_deferral_of_primary"] = (
            index > 0 and selected[0]["priority_lane"] != "DISCRETIONARY"
        )
        # A first slice is NOT proof the full task fits or was finished.
        # The user may choose an alternative; these are suggestions, not mandates.
    mode = "EXECUTE" if selected else ("ESTIMATE" if unscored else "BLOCKED")
    if not selected and not unscored and needs_decomposition:
        return assessment_choice(needs_decomposition,
                                 "DEFINE_REQUIRED_NEXT_STEP",
                                 "NEEDS_DECOMPOSITION")
    if not selected and not unscored and needs_verification:
        return assessment_choice(needs_verification,
                                 "CONFIRM_MILESTONE_COMPLETION",
                                 "NEEDS_VERIFICATION")
    if mode == "ESTIMATE":
        selected = [{"task_id": key, "role": "primary" if i == 0 else "alternative",
                     "action": "ESTIMATE_OR_CONFIRM"}
                    for i, key in enumerate(unscored[:choice_count])]
    return {
        "status": "PROVISIONAL_CALLER_ASSERTIONS", "mode": mode,
        "choices": selected, "critical_path": path,
        "scope_extension_ids": scope_extensions,
        "needs_decomposition_ids": needs_decomposition,
        "needs_verification_ids": needs_verification,
        "unscored_task_ids": unscored,
        "blocked": blocked,
        "coverage": {"considered": len(scope), "ready": len(ready),
                     "blocked": len(blocked), "unscored": len(unscored)},
        "notes": [
            "Task values, deadlines and safety classes are caller assertions, not authenticated.",
            "Score is a transparent sorting heuristic, not measured payoff or permission to act.",
            "Unknown values are never silently substituted with zeros.",
        ],
    }



def compare_snapshots(previous, current):
    """Compare two explicit caller snapshots without storing either.

    Host permissions, source identity, and real completion are not
    authenticated. Only task IDs and categorical changes leave this
    function; labels, paths, and original source text stay private.
    """
    older, before_date, before_goal, _, _, _ = validate(previous)
    newer, after_date, after_goal, _, _, _ = validate(current)
    refuse(after_date >= before_date)
    old_ids, new_ids = set(older), set(newer)
    shared = sorted(old_ids & new_ids)
    added = sorted(new_ids - old_ids)
    removed = sorted(old_ids - new_ids)

    def ready(tasks, key):
        row = tasks[key]
        return (row["state"] != "done" and row["kind"] == "action"
                and not row["external_blocker"]
                and all(tasks[dep]["state"] == "done"
                        for dep in row["depends_on"]))

    def changed(key, fields):
        return any(older[key][field] != newer[key][field] for field in fields)

    completed = sorted(key for key in shared
                       if older[key]["state"] != "done"
                       and newer[key]["state"] == "done")
    reopened = sorted(key for key in shared
                      if older[key]["state"] == "done"
                      and newer[key]["state"] != "done")
    state_changed = sorted(key for key in shared
                           if changed(key, ("state",)))
    dep_changed = sorted(key for key in shared
                         if set(older[key]["depends_on"]) !=
                         set(newer[key]["depends_on"]))
    blocker_changed = sorted(key for key in shared
                             if changed(key, ("external_blocker",)))
    priority_changed = sorted(key for key in shared
                              if changed(key, ("obligation", "due_date",
                                               "deadline_evidence", "urgency")))
    estimate_changed = sorted(key for key in shared
                              if changed(key, ("effort_minutes",
                                               "duration_days", "value")))
    newly_ready = sorted(key for key in shared
                         if not ready(older, key) and ready(newer, key))
    newly_blocked = sorted(key for key in shared
                           if ready(older, key) and not ready(newer, key)
                           and newer[key]["state"] != "done")
    return {
        "status": "PROVISIONAL_SNAPSHOT_COMPARISON",
        "source_and_viewer_permission": "HOST_MUST_VERIFY_BOTH_SNAPSHOTS",
        "completion_evidence": "CALLER_ASSERTED_NOT_AUTHENTICATED",
        "date_order": ("SAME_DAY_CALLER_ORDER_ONLY"
                       if after_date == before_date else "DATED_ORDER_ONLY"),
        "goal_changed": before_goal != after_goal,
        "completed_claim_ids": completed,
        "reopened_ids": reopened,
        "added_ids": added,
        "removed_unreconciled_ids": removed,
        "state_changed_ids": state_changed,
        "dependency_changed_ids": dep_changed,
        "blocker_changed_ids": blocker_changed,
        "priority_changed_ids": priority_changed,
        "estimate_changed_ids": estimate_changed,
        "newly_ready_ids": newly_ready,
        "newly_blocked_ids": newly_blocked,
        "counts": {
            "common": len(shared), "added": len(added),
            "removed_unreconciled": len(removed),
            "completed_claims": len(completed), "reopened": len(reopened),
            "newly_ready": len(newly_ready),
            "newly_blocked": len(newly_blocked),
        },
        "notice": (
            "Task removal, ID replacement or declared DONE does not "
            "prove completion. Verify authorization, real evidence "
            "and changed goal before acting on a recommendation."
        ),
    }


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        refuse(key not in result)
        result[key] = value
    return result


def read_input(filename):
    path = pathlib.Path(filename).absolute()
    # Check all ancestors before opening; does not defend concurrent path swaps.
    for parent in [path] + list(path.parents):
        mode = parent.lstat().st_mode
        refuse(not stat.S_ISLNK(mode))
    refuse(path.is_file() and path.stat().st_size <= MAX_BYTES)
    content = path.read_bytes()
    refuse(len(content) <= MAX_BYTES)
    return json.loads(content.decode("utf-8"), object_pairs_hook=unique_pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(Invalid("INVALID_INPUT")))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Offline source-declared task graph and bounded-choice plan")
    ap.add_argument("--input", required=True)
    ap.add_argument("--previous", help="Optional, separately authorized earlier snapshot")
    args = ap.parse_args(argv)
    try:
        current = read_input(args.input)
        response = plan(current)
        if args.previous is not None:
            previous = read_input(args.previous)
            response["transition"] = compare_snapshots(previous, current)
    except (Invalid, ValueError, OSError, UnicodeError, RecursionError, TypeError):
        print(json.dumps({"status": "INVALID_INPUT"}))
        return 2
    print(json.dumps(response, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main())

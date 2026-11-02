# Robotics exact-tree reconciliation and two complete-package static reviews

**Review date:** 2026-11-02. **Source:** [graph-robots/open-robot-skills at immutable revision](https://github.com/graph-robots/open-robot-skills/tree/752dfbd96968d4d08379f8111765efbf6457800b), `752dfbd96968d4d08379f8111765efbf6457800b`. **Origin:** valuable discovery evidence in held PR #590, independently recovered in PR #646 and risk-triaged in #647. **Disposition:** two source-family package reviews REJECT_UNCHANGED; archive retains references. No admission.

## Corrected evidence frontier: full 43-directory Git identity verification

A fresh, **untruncated recursive Git tree** was fetched from the *exact pinned source commit*, not from the draft archive's historical assertions. That upstream Git object contains **333 entries**. Each entry of [the 43-row source identity ledger](../../registry/discovery/robotics-43-entrypoint-reconciliation-20261102.csv) was joined against its exact source path:

| Independent pinned Git-tree check | Match |
| --- | ---: |
| All 43 `SKILL.md` entrypoint Git SHA identities | 43/43 |
| All 43 recorded package-directory tree SHA identities | 43/43 |
| Per-package observed supporting-file count vs recorded count | 43/43 |
| Discrepancies or truncated Git-tree evidence | 0 |

**Important evidence distinction:** Git tree hashes establish the complete *versioned package tree identity* at the pin, including bundled files and nested directories. Counts likewise verify package membership; they do not establish that every file is safe, legal to reuse, functioning, behaviorally validated or even individually read. All 43 entries still require a package-level review before claiming quality. This tranche completes **content inspection of exactly two selected package directories**, not all 43.

The review ledger is [JSON, complete per-dimension rationale](../../registry/discovery/robotics-two-complete-package-static-20261102.json). It records each exact Git tree, all files in the directory, source-license context, independent static disposition, and no execution.

## Two fully inspected *source package* boundaries

### 1. `skills/anchoring-a-free-end`

- Exact package tree: `734446b75a871b16ac291977322f6cc635c757ce`, **two files read**: `SKILL.md` and `scripts/anchor_far_end.py`; both blob SHAs confirmed.
- **Static score: 11/20; REJECT_UNCHANGED (hard fails).** Trigger and sequence are well specified, and the skill honestly says its privileged cable planner is simulation-only. The fatal concern is in `run()`: `float(plan.get("worst_grasp_error", 0.0))` silently assigns *zero error* when a critical planner error field is missing. With stages present, this can pass the `worst > 0.05` refusal gate; a NaN comparison also fails to trip that gate. Trajectory stages are executed and jaws closed without measured hold confirmation, and a late stage error can follow partial movement with no explicit stop or recovery.
- **Needed before unchanged reuse:** reject missing/nonfinite planner/IK error, validate plan fields and every stage *before* any robot command, require explicit host/operator action authority and physical/simulation controls, account for partial movement, and confirm a grasp before claiming anchored.

### 2. `skills/verifying-grasps`

- Exact package tree: `9b0301c89c0cb1a1252edccae40fcb9440c0cfb3`, **four files read**: `SKILL.md`, `scripts/verify_grasp.py`, `scripts/verify_grip.py`, `scripts/verify_reach.py`; all blob SHAs confirmed.
- **Static score: 11/20; REJECT_UNCHANGED (hard fails).** The three-stage reach/gripper/observed-hold design is valuable, but `verify_reach.py` returns `{"route":"reached","reached":True}` **when commanded pose, observed pose or target box is missing**. Unknown evidence therefore masquerades as a positive reach measurement. The `verify_grasp.py` script issues `robot.go_to_pose_cartesian` for a caller-supplied `lift_m` **before checking that the required wrist RGB-D camera exists**; it then raises if the camera is missing, after commanding motion. The lift distance has no local finite/range guard.
- **Needed before unchanged reuse:** use an explicit unknown/unverified outcome for absent pose/box, block downstream gripping when reach is unknown, inspect camera and safe lift parameters before movement, and constrain physical authority, geometry, workspace and recovery.

Both reviews used the [ten-dimensional static rubric](../skill-verification.md) individually (trigger, procedure, authority, failure, evidence, dependency, portability, usefulness, adversarial resilience, effectiveness). **A score is not a security approval, behavior test or user permission.** Hard fails override any numerical threshold.

## License, dependency and operational boundary

- Root source `LICENSE` at the same pin is Apache-2.0, exact Git blob `d645695673349e3947e8e5ae42332d0ac3164cd7`; both inspected `SKILL.md` frontmatters explicitly declare Apache-2.0.
- These two source packages import external `gap` and connector APIs. The latter's source implementations, equipment specifications and license obligations are outside the reviewed package directories. Their behavior was **not** verified.
- This was a **read-only external GitHub static assessment**. No source scripts were run, and no robots, physical motion, cameras, hosted models, scanners, CI or behavioral evaluations were invoked.
- The **four-source 4,813 raw path denominator and 1,039 governed review records remain unchanged**. These are two additional, exact-version **pre-admission source static-review decisions** outside the governed corpus; they are **not** two newly approved or admitted skills. Do not fold them into the four-source frontier counts.

## Follow-up

Preserve both flawed examples as labeled negative/reference evidence with actionable remediation proposals. Do **not** copy the original scripts into a consumer environment unchanged, and do not submit upstream code changes without a separate explicit maintenance request. Continue auditing the remaining 41 source packages selectively by safety risk and capability coverage, checking full code and dependency/authority boundaries. If an upstream revision fixes these defects, review its *new* tree identity rather than transferring this decision. No new repository-owned machinery or automatic installation.

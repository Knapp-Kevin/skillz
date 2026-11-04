# Q10 remaining lead: ROS 2 Engineering packaging boundary

**Date:** 2026-11-03 · **Q9 discovery:** #697 · **Q10 review:** #698 · **Stage:** **SCOPE MAPPED; NOT THE EIGHTH COMPLETED REVIEW**

## What we found

The pinned [ROS 2 Engineering source](https://github.com/dbwls99706/ros2-engineering-skills/tree/f0de84dfedd67b067ccc6d2851e681529606930c) has a strong-looking **engineering method**, not a proven safe installation. Its root skill instructs agents to inspect evidence before changing a ROS graph, distinguish installed/runtime config from source files, and keep operator-controlled physical safety separate from software testing.

The main packaging question is now answered. At pinned commit `f0de84dfedd67b067ccc6d2851e681529606930c`, the repository has **204 Git blob files**. Its `scripts/install_skill.py` portable installer defines an explicit `BUNDLE` that selects **118 files**. The selected files include **28 references**, **15 Python scripts**, **15 documentation files**, **50 evaluation resources** and other support files. The remaining **86 repo files** are not in that portable copy.

This is an **exact-pinned scope measurement** from the nontruncated Git tree and the source installer configuration, not execution of the installer. It reduces an ambiguous 204-file package into a testable 118-file portable bundle.

## Different installation profiles mean different trust boundaries

| Profile | Behavior documented by source | Qualification status |
|---|---|---|
| Portable copy | Copies the 118-file bundle to a client skill directory; does not register Claude hooks or change client settings | Still needs complete file and installer tests |
| Claude plugin | Uses `.claude-plugin/plugin.json` plus `hooks/hooks.json` to register `PreToolUse` and `Stop` scripts | Hook code and effects require separate review |
| Legacy copy/link | Full-checkout `install.sh` or `install.ps1` may expose plugin and hook files | Not equivalent to portable copy; not reviewed |

The portable bundle **does include** Python files named `claude_hook.py` and `launch_supervisor.py`; copying those files is not the same as registering/executing them. `launch_supervisor.py` can launch real processes if deliberately invoked. The root contract explicitly prohibits turning validator output into permission or physical safety evidence. It also states that a regex-based PreToolUse hook is only advice, not a security boundary.

## Benefits we can learn from

- Keep code review, simulation results, powered-but-not-moving hardware tests, and operator-supervised physical trials separate.
- Before changing QoS or controls, confirm which actual nodes, installed files, transports, and parameters are in use.
- Preserve approval provenance, validation criteria and actual measured outcomes rather than weakening an unsuccessful safety gate.
- Installations should record their exact source and file digest, and should not silently overwrite a user-edited installation.

## Remaining work

**Do not count this as a completed Q10 qualification** and do not recommend installation unchanged. The source has 118 selected files, including 15 Python executables, but only the root/installer/contract and selected high-risk references and scripts have been examined. The full bundle has no standalone Git tree SHA because the installer selects multiple root paths; derive a stable source-pinned manifest before security acceptance.

Next: inspect all 118 selected paths and their per-file rights; resolve separate portable versus plugin policies; run a pinned scanner; validate installer no-clobber/rollback in a disposable host; and test representative ROS tasks only in a simulation with no physical actuation. L0–L6 language must remain evidence-based. We have **not** installed, run, scanned, connected to ROS, or moved a robot.

[Structured source and bundle-boundary ledger](../../registry/discovery/q10-ros2-engineering-bundle-boundary-20261103.json). **No ten-axis grade yet; no change to the seven Q10 completed static review count, no featured method and no unchanged-use approval.**


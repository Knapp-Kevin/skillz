# Q10: ROS 2 Engineering portable bundle, complete source-pinned static review

**Date:** 2026-11-03 · **Q9:** #697 · **Q10:** #698 · **Decision:** **17/20, Valuable Reference concept worth studying; unchanged use held**

## Result in plain language

This skill helps an agent work on ROS 2 robotics without guessing which software is actually running or pretending a passing software test proves a robot is safe. It teaches the agent to check the real installed environment, investigate faults before changing settings, and keep **operator permission, technical readiness and evidence of physical safety separate**.

It is a strong reference method, but **not approved for installation as written**. Robotics software can control motors, flash firmware and change real network or safety settings. Good written warnings are necessary but cannot replace proving the behavior of its bundled tools.

## What was checked

At [source commit `f0de84dfedd67b067ccc6d2851e681529606930c`](https://github.com/dbwls99706/ros2-engineering-skills/tree/f0de84dfedd67b067ccc6d2851e681529606930c) the repository contains **204 Git-tracked blobs**. Its portable installer selects exactly **118 files**: 15 Python scripts, 28 task references, 15 docs, 50 evaluation resources, and 10 other files. All **118 files were fetched in bounded groups and matched their pinned Git blob SHA**. The full [118-entry machine manifest](../../registry/discovery/q10-ros2-engineering-portable-118-file-manifest-20261103.json) makes the review reproducible, with each path and SHA. We statically screened executable sources and read the most consequential installer, hook, launcher, safety and test paths in depth. No code was executed.

The previously published [bundle-boundary study](2026-11-03-q10-ros2-engineering-bundle-boundary.md) remains intact as the earlier stage; it is now superseded **for the question of whether a complete portable-source static review exists**, not deleted.

## Benefits we would keep

1. **Find the running system before diagnosing it.** A source YAML file is not proof of which parameters a launched node actually uses. Verify the active package, process, parameter and ROS distribution.
2. **Treat safety as a chain, not a software response.** Publishing a zero-speed command does not prove that motors stopped. Independent physical stopping and actual operator evidence are required.
3. **Keep action permissions narrow.** A review stays read-only. Editing code, launching ROS, changing a host, or testing real hardware requires distinct authority.
4. **Preserve technical evidence.** The L0–L6 verification levels prevent a lint pass or simulation result from being called a real-world hardware success.
5. **Protect prior work.** The installer stages a copy, checks a file manifest, refuses ordinary overwrites and has a rollback path. These protections were read in the source, **not tested on a host**.

## What prevents unchanged use

| Hold | Why it matters |
|---|---|
| Bundled execution | The portable package includes 15 Python scripts. One launches real ROS processes; another generates packages and can overwrite with explicit `--force`. Static review is not enough to authorize them. |
| Installation behavior | Staging, file digests, rollback and no-clobber look deliberate, but were not actually tested here. |
| Hooked plugin | The Claude plugin separately enables PreToolUse and Stop hooks. The portable copy includes hook-related Python source but does not register the plugin hooks. Neither profile should inherit the other's clearance. |
| Hardware and firmware | References include ROS launches, firmware flash and `sudo` system commands. An agent reading that material has **no automatic permission to run them**. |
| Evidence | The source includes tests and benchmark fixtures, but their existence is not observed acceptance. No pinned external scanner or representative/adversarial host run happened. |
| Source rights | Root [Apache-2.0](https://github.com/dbwls99706/ros2-engineering-skills/blob/f0de84dfedd67b067ccc6d2851e681529606930c/LICENSE) is present. It does not automatically relicense vendor excerpts or third-party ROS examples. |

## Scores and next qualification gate

| Review dimension | / 2 |
|---|---:|
| trigger precision | 2 |
| procedural clarity | 2 |
| authority safety | 2 |
| failure handling | 2 |
| evidence discipline | 2 |
| dependency coherence | 1 |
| portability honesty | 2 |
| usefulness differentiation | 2 |
| adversarial resilience | 1 |
| effectiveness design | 1 |
| **Total** | **17 / 20** |

This is a semantic **static review score**, not a security or safe-operation rating. The [structured review ledger](../../registry/discovery/q10-ros2-engineering-portable-static-20261103.json) lists exact source blobs, code observations, negative thought experiments and missing evidence. This is the **eighth completed Q10 static review** of the eight original Q9 source leads, but **zero** source packages received unchanged-use approval and **zero** Q10 methods were promoted into the featured catalog.

Next: a third-party scan of the pinned **portable 118-file bundle**, an isolated installer/no-clobber/rollback trial, and operator-reviewed non-actuating ROS or simulation tests. Qualify the Claude hook-enabled profile separately. **No real robot test is planned or authorized by this review.**


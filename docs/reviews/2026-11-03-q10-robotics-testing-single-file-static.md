# Q10 supplement: Robotics Testing static safety and correctness review

**Date:** 2026-11-03 · **Route:** repository maintenance · **Q9 discovery:** #697 · **Q10:** #698

## Outcome

The [pinned Robotics Testing skill](https://github.com/arpitg1304/robotics-agent-skills/blob/f9bc5467ff9ee3d23f1a1b0b29a649843bb6ad11/skills/robotics-testing/SKILL.md) earns **11/20** on the ten-axis static rubric. Its **testing pyramid** is valuable: start with quick unit tests, then integration, then simulation, and reserve hardware-in-the-loop and field tests for controlled environments. Keep that engineering principle as a research reference.

**Do not use its sample tests unchanged in a real ROS project.** We found code correctness defects and missing live-robot isolation controls. No actual robot, ROS graph, simulation or CI pipeline was run.

## Confirmed source-code issues

| Source location | What the example does | Why it matters |
|---|---|---|
| Lines 347-372, `MockJointStatePublisher` | `publish_next` reads `self.node`, but the constructor never stores `node` in that attribute | A copied fixture will fail at runtime |
| Lines 187-195, quaternion test | Multiplies by a quaternion using two `0.707` components, then requires unit length within `1e-10` | The rounded constant has norm **0.999848989**, already off by **1.510e-4**, so the check cannot reliably pass for a correct norm-preserving implementation |
| Lines 375-397, trajectory golden file | If a baseline is missing, writes the current trajectory as the baseline and skips the test | A bug in the current implementation can be silently accepted as the new gold standard |
| Lines 252-313 and 348-372, integration and mock publishing | Launches nodes and writes to ordinary ROS topics such as `/camera/image_raw` and `/joint_states` | Without explicit simulator isolation and robot owner permission, topic traffic could reach an unintended connected system |
| Lines 49-128, example unit test | Refers to app-specific detection message types and test helpers that are not provided in the single-file skill | The example is illustrative, not standalone verified test code |

The numeric quaternion check above was a basic **static arithmetic consistency check**, not a robotics execution test. The hardware-contact concern is a **potential risk** that depends on the ROS deployment, not evidence that a real machine was controlled.

## Why this is still useful

- It treats mock hardware, simulation, and real hardware as **different layers**, which helps teams find cheap failures before dangerous or expensive ones.
- It includes useful tests for kinematics, transformations, message handling and collisions that can inspire independently reviewed examples.
- It values reproducibility and explicit failure cases rather than testing only the happy path.

These principles deserve to remain discoverable. The sample code, however, needs independent correctness review and safe execution gates.

## Identity and rights

Single-file owned package tree `79de981d57e0b64eee681d374720708fb7326f64`; `SKILL.md` blob `c2c2c3326591d49935381ffc43a9342b88b53e55`; source commit `f9bc5467ff9ee3d23f1a1b0b29a649843bb6ad11`. The pinned root [Apache-2.0 license](https://github.com/arpitg1304/robotics-agent-skills/blob/f9bc5467ff9ee3d23f1a1b0b29a649843bb6ad11/LICENSE) has blob `c32fd4634d8ba91fb8755092a711f0e95711cf98`. Reproducing or adapting protected material requires complying with the applicable attribution, license and notice obligations.

## Qualification needed before reuse

Require a simulator-only namespace/domain, clear non-actuating and hardware-owner authority, a manually approved/read-only baseline, correct and complete test fixtures, version-matched ROS dependencies, and representative automated plus operator-reviewed test behavior. A simulation pass cannot itself certify hardware safety. The [structured record](../../registry/discovery/q10-robotics-testing-single-file-static-20261103.json) contains all ten scores, exact evidence, and the blocked scenarios.

**Disposition:** REJECT unchanged / keep testing-method concepts · **Security:** NOT RUN · **Behavior:** NOT RUN · **Featured shelf:** unchanged.


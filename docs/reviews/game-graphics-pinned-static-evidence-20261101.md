# Game graphics package static-review evidence

Source: j4flmao/agent-skills, pinned commit 982203e52afe0b726a7847599a8bfb293890e0c5. This is candidate-only evidence, not governed admission or behavioral validation.

## Vulkan 2.0.0

Canonical path: skills/game/game-development/vulkan/SKILL.md. Blob: 4086b6e9b7bd1776acfdecad0a474e6e2c027e64. Package tree: 09201bf639d7cf53bfac8da47647b0e34f26e42.

Inspected SKILL.md and six references: vulkan-initialization, swapchain-and-present, render-passes-and-pipelines, synchronization-deep-dive, memory-and-upload, compute-and-ray-tracing.

Decision: REJECT unchanged use. Swapchain recreation guidance destroys the old handle before reusing it as oldSwapchain. Swapchain image-count clamp does not honor surface maxImageCount. Compute example declares 64 by 64 local invocations, exceeding commonly supported limits. Memory example has invalid VMA access and dynamic uniform offsets omit alignment. Preserve as a reference for device negotiation, staging, validation and fence-gated frame lifetimes after correction.

## Render Graph 2.0.0

Canonical path: skills/game/game-engine/render-graph/SKILL.md. Blob: 8b42b6205dd8442f4b2cd5d02bb0a2fda0549926. Package tree: 59f015b021da5e4b344303ef92226847e26ba692.

Inspected SKILL.md and six references: command-lists-and-queues, passes-and-attachments, resource-lifecycle, barriers-and-transitions, synchronization-and-fencing, gpu-driven-rendering.

Decision: REJECT unchanged use. Resource lifecycle uses frame arithmetic rather than confirmed GPU fence completion for reclamation. Synchronization guide confuses semaphore signaling and waiting. Barrier reference overstates simple DAG edges as sufficient for all hazards and implies discard transitions at last use. Preserve DAG/resource modeling and GPU profiling patterns as reference after correction.

## Boundaries and evidence state

Root MIT metadata does not relicense external dependencies. Both packages are local code guidance, not authorization to change a production renderer, capture user scenes, upload GPU diagnostics, or expose private assets. Hardware limits, graphics APIs, Vulkan Memory Allocator versions and external tool licenses require independent checks.

Static inspection: complete for the two seven-file packages. Behavioral tests, GPU validation, security scans: NOT RUN. Numerical rubric grades: NOT ASSIGNED. No skill admitted or approved for unchanged use. Public counts must remain unchanged until the candidate ledger and all accounting surfaces are reconciled.

Next: review the other seven nested game packages and reconcile exact-version candidate records atomically.

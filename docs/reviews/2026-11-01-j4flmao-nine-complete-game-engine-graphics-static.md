# Pinned j4flmao nine-package game-engine and graphics qualification (2026-11-01)

**Source role:** dynamic-discovery-only, not admitted. Upstream: `j4flmao/agent-skills` at `982203e52afe0b726a7847599a8bfb293890e0c5`. Exact complete-package records: [nine graded source-vetting decisions](../../registry/discovery/j4flmao-nine-complete-game-engine-graphics-static-20261101.json). Root MIT notice (blob `0e8b6e6d8678128ebfcc28d7cad91fa9ed7f2354`) applies only within its actual scope; external engines, drivers, libraries and tools retain their own terms.

## Macro denominator and disposition

The remaining **9/9** structurally confirmed nested game-engine/game-development packages were each inspected as complete seven-file trees: **63 files**, including **54 bundled reference components** that are not independently counted as skills. All nine SKILL.md blobs and package-tree SHA-1 identities were matched against the pinned source tree. **Nine REJECT unchanged** decisions; zero approvals, admissions, governed exact-version review pairs, security scans, or behavioral validations.

| First-class package | Candidate static score | Decisive unchanged-use blocker |
|---|---:|---|
| game-development/vulkan | 12/20 | Destroyed old swapchain reused for recreation, device-limit violations, incorrect GPU code examples |
| game-engine/render-graph | 11/20 | Frame-index reclamation instead of fence-confirmed GPU completion; incomplete synchronization semantics |
| game-engine/asset-pipeline | 11/20 | In-flight asset/GPU lifetime hazards, untrusted pack handling and missing authorization boundaries |
| game-engine/ecs-pattern | 11/20 | Invalid sparse-set removal, stale entity generation, uninitialized archetype and version-mixed APIs |
| game-engine/job-system | 12/20 | Readiness/completion conflation, invalid job execution path and nondeterministic worker-seeded RNG |
| game-engine/math-foundation | 12/20 | NaN-producing parallel ray slab case, determinism errors and unsafe transform inverse shortcuts |
| game-engine/memory-management | 11/20 | Allocator bounds/alignment errors and frame-count GPU retirement |
| game-engine/patterns | 11/20 | Unbounded pools, invalid arena use, ill-formed recursive C++ state and incorrect frustum test |
| game-engine/platform-abstraction | 11/20 | Ungated crash telemetry and remote TCP console, VFS traversal and async buffer lifetime gaps |

Each record contains ten rubric dimension scores (0–2 each), individual trigger/nontrigger, complete package files and SHA identities, source/license/freshness/dependency characterization, authority/privacy findings, controlled tags, narrow capability paths, rationale, and explicit `not-run` security/behavioral state. Scores are **source-vetting evidence**, not governed verification or an install permission.

## Family and ecosystem reconciliation

- j4flmao source candidate terminal decisions: **32 → 41 / 645 raw paths**.
- Nested game first-class package candidate terminal decisions: **14 → 23 / 23**; nine seven-file pending → **zero**.
- Direct-shape decisions unchanged **18 / 424**; direct-shape without decisions **406**.
- Other-shape still structurally unclassified **198**; nested-game classification does not resolve these.
- Across four pinned sources: **46 → 55** exact-path terminal candidate decisions out of **4,813 raw paths**; distinct eligible denominator remains **unknown**. Existing **1,039 governed review records** unchanged.
- This is not a completion claim for j4flmao's 645 paths, the full four-source frontier, cross-source semantic deduplication or rights/security qualification.

## Cross-package synthesis

Repeated correctness failures cluster around GPU/CPU lifetime, scheduling/determinism, memory safety and code-example validity. The platform-abstraction package additionally prescribes crash telemetry and remote command exposure without appropriate privacy and access boundaries. Shared package structure is good (one front-mattered entry plus six bundled references), but shared source metadata cannot substitute for individual semantic inspection. No unreviewed reference was counted as a separate skill.

**Preserve useful prior art:** content-addressed asset cooking, bounded work queues, DAG/cycle checks, explicit platform capability gates, frame-graph pass/resource modeling, ECS scheduling, SIMD property tests and monotonic-clock interfaces. Any adaptation must correct examples, preserve source notices and obtain separate host authority for execution, production mutation, data capture and disclosure.

The earlier narrative-only receipts in draft PR #609 were **intermediate evidence** and stated grades were not yet assigned. This receipt and its structured companion supersede that intermediate grading status without erasing the original findings. All static analysis was read-only; no code compiled, renderer executed, package installed, telemetry sent or security scanner run.

**Next:** classify j4flmao's remaining 198 other-shape paths, then process the 406 direct-shape gaps in coherent source-neutral capability tranches while resolving cross-source mirrors and rights.

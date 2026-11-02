# Job-system complete-package static qualification

Source: j4flmao/agent-skills at 982203e52afe0b726a7847599a8bfb293890e0c5. Path: skills/game/game-engine/job-system/SKILL.md. Blob 90ddc1ef4e7f7ae5f24807703c7a1bd7ace6bbb7. Tree 6a73799ba6cf8b674f895956da35bade583b86c0. Version 2.0.0.

All seven files inspected: SKILL.md; scheduler-impl (37c72a3); dependency-graph (11f5a24); parallel-for (8cd51b2); determinism (101580d); fibers-and-async (40d9be8); job-profiling (7d0fca5).

Trigger: game-engine CPU scheduler, work stealing, DAG, fibers, parallel-for. Nontrigger: backend services, GPU graph, production deployment.

Terminal source-vetting decision: REJECT unchanged. Dependency-graph reference conflates in-degree ready counter with completion counter and can mark a job complete before execution. It omits atomic dependency registration against already-finished parents. Scheduler reference runs a job after failed steal and parking without checking validity. Determinism reference seeds RNG by worker ID despite work stealing, conflicting with deterministic replay. GPU async guidance assumes fences per transition and near-free compute, which is not generally true. Worker-count and performance targets lack target-hardware validation.

Preserve useful concepts: DAG cycle checks, fixed item-key RNG, explicit partition ownership, bounded pools, critical-path profiling, and separate readiness/completion counters after correction.

License: pinned root MIT scope only; external runtimes and profiler rights separate. Authority: no live stress testing, telemetry export, gameplay profiling or production mutations without permission. Sensitive traces require minimization and retention controls.

Static source review only. Security scan NOT RUN. Behavioral validation NOT RUN. Compiler/sanitizer tests NOT RUN. Numerical grade and governed semantic review NOT CREATED. Public counters unchanged.
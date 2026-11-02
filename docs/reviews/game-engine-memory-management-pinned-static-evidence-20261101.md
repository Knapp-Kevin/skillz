# memory-management 2.0.0: pinned complete-package static evidence

Source j4flmao/agent-skills at 982203e52afe0b726a7847599a8bfb293890e0c5. Canonical skills/game/game-engine/memory-management/SKILL.md; SKILL blob 4dfc3f7a93125949fd75aa1271c89deb778a5114. Package tree fingerprint not asserted in this receipt; reconcile against pinned source manifest before central ledger update. Declared MIT, not a relicensing of third-party libraries.

All seven files inspected: SKILL.md plus references allocator-hierarchy f8c42d4b; cache-aware-layout 6929b039; memory-tracking 7d68a198; virtual-memory 587cd64c; gpu-memory 0a947c42; gc-avoidance 0acec039.

Trigger: game-engine memory management implementation guidance. Nontrigger: permission to execute benchmarks on production systems, change deployed binaries, export traces, or access private project assets.

**Source-vetting disposition: REJECT unchanged.** The primary StackAllocator computes the aligned allocation size in local n after initializing size from the unaligned input; alloc() then advances top before checking capacity, so failed assertions in release builds permit out-of-bounds writes. It performs pointer arithmetic on a possibly invalid allocation without a bounded failure return. The allocator-hierarchy reference calls aligned_alloc(64, cap) without ensuring cap is a multiple of 64. The GPU reference repeatedly suggests freeing after k frames even though fence completion, not elapsed frame count, is the correctness condition. Platform-specific virtual-memory examples omit complete error handling.

Retain as corrected reference: Subsystem budgets, generation-tagged handles, per-thread ownership, sanitizer testing, fence-confirmed GPU retirement, measured allocation profiles.

Authority/privacy: explicit approval required for persistent changes, profiling/capture, telemetry or sharing traces. Test against target architecture, compiler, driver and library versions.

Evidence limits: complete-package static inspection only. Behavioral tests NOT RUN. Security scans NOT RUN. Numerical 20-point rubric NOT ASSIGNED. Governed exact-version review NOT CREATED. Public counters unchanged pending reconciliation.

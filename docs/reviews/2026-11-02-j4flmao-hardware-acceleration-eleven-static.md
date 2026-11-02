# Pinned hardware-acceleration source-vetting review, 2026-11-02

**Source:** `j4flmao/agent-skills` at `982203e52afe0b726a7847599a8bfb293890e0c5`. Complete pinned root MIT `LICENSE` blob `0e8b6e6d8678128ebfcc28d7cad91fa9ed7f2354`; external libraries, models and datasets retain their own rights.

**Scope and denominator:** all **11/11 direct-shape, individually front-mattered hardware-acceleration SKILL.md packages** in this source subfamily. The pinned manifest establishes each canonical path, exact SKILL blob and containing package tree. Independent pinned directory listings confirmed **one file per package**, no package-local bundled references or licenses. Cross-skill links point to separately inventoried source paths; they are not package-owned files. No duplicate SKILL blobs within the 11. These 11 are not a claim about the entire 645-path source or the distinct eligible cross-source denominator.

**Decisions:** 4 REFERENCE-ONLY (`cuda-programming`, `sass-machine-code`, `tpu-systolic-arrays`, `triton-kernels`), 7 REJECT unchanged (`distributed-training`, `extreme-quantization`, `flash-attention`, `paged-attention`, `ptx-assembly`, `rdma-roce`, `tensorrt-optimization`). Scores **13–16/20**, each with its own 10-dimension rubric, trigger/nontrigger, provenance, license, dependencies, authority/privacy, rationale, static decision, and not-run security/behavioral state in [the individual ledger](../../registry/discovery/j4flmao-hardware-acceleration-eleven-complete-static-20261102.json). Scores are **source-vetting static scores**, not governed verification, security passes or behavioral validation.

## Macro findings

1. **Missing authorization is systemic.** GPU profilers and JITs execute programs, distributed training may allocate costly cluster resources, TensorRT and quantization create persistent artifacts, vLLM/TRT-LLM can expose serving endpoints, TPU workloads may incur cloud charges, and RDMA tests can load or disrupt a shared fabric. The source generally offers commands without binding user-approved host, account, data, budget, endpoint, maintenance window or rollback. Tool presence is not authorization.
2. **Specific code hazards matter beyond generic safety.** The FlashAttention package uses SDPA-shaped `(B,H,L,D)` tensors for `flash_attn_func`, which requires `(B,L,H,D)`. The PTX inline global-memory load example omits the memory clobber its own guidance recommends. The CUDA warp reduction example assumes a full active warp. These are not safe unchanged implementation templates.
3. **Useful differentiated mechanisms survive rejection.** CUDA coalescing/tiling and correctness checks, SASS stall attribution, TPU MXU/XLA tiling and Triton masked/fused kernels are valuable reference material. Preserve them as reference-only; do not imply automatic installation or execution. The rest retain explicit adaptation/extraction potential without approval unchanged.
4. **Rights and privacy are distinct.** Root MIT is complete and applies to this source's material, but not to gated model weights, calibration datasets, cloud services, external dependencies or private training/profiling data. Prefix caching and serving require tenant and retention controls.
5. **Capability omission exposed.** Existing directory domains lacked a precise GPU-kernel/ML-inference/fabric route. Add a source-neutral `ml-accelerators` domain with six subdomains; entries are candidate-only, with no change to governed review population.

## Accounting and next frontier

- j4flmao exact-path terminal candidate decisions: **79/645 → 90/645**; direct **40/424 → 51/424**; other **39/221** unchanged; pending **566 → 555** (**373 direct**, **182 other**).
- Four-source exact-path candidate decisions: **174/4,813 → 185/4,813**. These are **not** the verified distinct eligible denominator.
- Governed exact-version review companions **1,039 unchanged**; admissions **0**; external security scans **0**; executed behavioral validations **0**.
- This hardware subfamily **11/11** is complete at the source-vetting stage. Continue the next genuinely unreviewed, under-served source tranche after a fresh main/issue/PR/concurrency check. The next j4flmao direct alphabetical cursor remains `skills/aspirational/roadmapping/SKILL.md`; the next other-shape cursor remains `skills/backend/dotnet/architecture/SKILL.md`.

**No skill code was run, no model was downloaded, and no third-party package was vendored.** This is passive static evidence only.

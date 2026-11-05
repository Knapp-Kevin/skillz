# Issue #402: three failed third-party packages, direct static content adjudication

**Reviewed 2026-11-05.** This is a bounded continuation of the owner-approved [static-review/freshness policy](../static-review-and-freshness.md). Each recorded skill's **complete package**, including all nine material files across three packages and the controlling root license file for each source, was read as **untrusted content**, not executed as a skill. Complete package Git tree hashes were independently traversed from pinned upstream Git commits, and source files' exact Git blobs match the existing Q8 evidence. All three upstream default-branch heads still equal their deliberately pinned revisions today. [Machine ledger with exact hashes, scoring and specific risk locations](../../registry/security/third-party-three-failed-static-dispositions-20261105.json).

The previous SkillSpector results remain recorded as **FAILED**, not converted to scanner PASS. The adverse scanner signatures below were examined contextually; each appears to have matched ordinary domain text, but no formal owner/scanner adjudication or rerun was performed. More importantly, **real defects independently prevent unchanged adoption**. These are **static reviewer findings**, not observed model behavior or runtime vulnerability exploits.

## Results

| Pinned package | Files read | New static rubric | Disposition |
|---|---:|---:|---|
| [E-commerce unit economics](https://github.com/peterbamuhigire/business-plan-skills/tree/00a85b14b0770951a4c8dd0f8505b2bbaf7bfc95/skills/ict/ecommerce-unit-economics-and-cross-border-margin-model) | 3 + root MIT LICENSE | 13/20 | Reference-only; unchanged use held |
| [Audio performance debug](https://github.com/kunitoki/sonic-skills/tree/8b6dcfe89030d7de9ba9d6afcc2d927fb11fe7fa/skills/audio-performance-debug) | 2 + root Unlicense | 12/20 | Reference-only; unsafe code examples held |
| [Singapore SSP Navigator](https://github.com/kyleoliveiro/sg-gov-skills/tree/16892fc613263c3f835457cd23ae092d404979ca/skills/sg-gov-ssp-navigator) | 4 + root MIT LICENSE | 15/20 | Reference-only; compliance decisions held |

The scores are new, conservative **full-package static reviews** under the current ten-axis rubric. They do not silently overwrite earlier Q8 study-only evaluations or upgrade these packages to `verified`: the hard-fail dependency, source freshness and unsafe-example conditions have not been remedied. Readable source-text review cannot establish agent-host `validated`.

## E-commerce unit economics

**Pin:** `00a85b14b0770951a4c8dd0f8505b2bbaf7bfc95`, complete package Git tree `8697477b3b824931a77afcddf430916c91e4b7bb`, `SKILL.md` blob `5c7e7e82b9b73e75d7b1be1fdf99417b65153097`.

**Historical scanner:** `P2` Hidden Instructions at `SKILL.md:76` (HIGH), prior `failed`. The matched location begins an HTML-comment-marked compatibility appendix. That is an ordinary formatting delimiter rather than inherently hidden malicious instructions, but no previous scanner result was changed and **the source still fails unchanged-use review for other reasons**.

**Material findings:** The second workflow requires an external accounting doctrine for revenue, inventory, refund, tax and settlement treatment, but the package supplies no definition or reproducible material for it (`SKILL.md:83,118,124`). This is an actual incomplete required dependency: a user cannot reconstruct the claimed financial verdict just from these three files. The workbook spec subtracts CAC from an order-level contribution calculation without declaring how customer-cohort acquisition spend is allocated across repeat orders, opening the door to mismatched units or double-counting. The main file also contains an author contact number not necessary for the reusable method. Do not reproduce that contact in derived summaries.

**Useful separable mechanism:** Record source and confidence for each input, calculate landed cost and contribution by channel, stress FX/returns/freight, and withhold a firm GO when load-bearing figures or finance treatment are missing. Reimplementation should supply its own licensed and reviewable accounting specification, explicit unit/cohort allocation and reconciliation rules.

## Audio performance debug

**Pin:** `8b6dcfe89030d7de9ba9d6afcc2d927fb11fe7fa`, complete package Git tree `b6d07ad1cee260f2be4998103b44a164a597ddc7`, `SKILL.md` blob `15c4648108b8882896f047e01849e224c3b64b19`.

**Historical scanner:** `MP2` Context Window Stuffing at `references/performance-patterns.md:42` (MEDIUM), prior `failed`. That location discusses **FFT zero-padding**, not enlarging an LLM context. The historical report had already proposed false-positive treatment. This review finds the interpretation plausible but does not accept the scanner finding, manufacture a rerun, or relax unchanged-use restrictions.

**Material findings:** SIMD loops under `references/performance-patterns.md` increment by SIMD width with no remainder handling. With non-multiple-of-four sample counts, the SSE2 example can read/write beyond the buffer; the xsimd example has the analogous tail issue. The supplied JUCE PerformanceCounter example logs from the audio callback, contradicting the hard real-time budget that motivates the skill. Its atomic-flag spinlock suggestion risks being misapplied to realtime code; a nonblocking try-lock plus fallback is not the same as busy-waiting. Finally, profiler attachment to a running audio process is consequential and must be limited to an authorized process and safe diagnostic session.

**Useful separable mechanism:** Reproducible symptom-first measurement, distinguish average CPU from worst-case xrun timing, and inspect real-time allocations or contention. Do **not** copy the flawed SIMD/realtime callback examples into production DSP code. Fix tail paths, instrumentation scope and lock-free/nonblocking behavior first; test with awkward buffer sizes before any replacement implementation is qualified.

## Singapore SSP Navigator

**Pin:** `16892fc613263c3f835457cd23ae092d404979ca`, complete package Git tree `135c3d625b2092ff3c9ee123e97641c09596ee53`, `SKILL.md` blob `c731414a2c7a4655069776f9549594c7e06dca57`.

**Historical scanner:** `EA2` Autonomous Decision Making at `SKILL.md:182` (MEDIUM), prior `failed`. The passage describes approval rules for Level 2 controls within the referenced Singapore standards. It does not itself direct the agent to autonomously approve actions. This contextual observation does **not** establish current correctness of the claimed government requirements or alter the scanner receipt.

**Material findings:** The skill and its substantial SSP profile reference embed **July 16, 2026** snapshots of government security requirements, including control levels, counts, thresholds, data classifications and notification rules. The package itself admits that live government pages supersede the bundled information. This review **did not verify current live official standards**, so it cannot authorize a current compliance baseline, certification, or a decision that a security deviation is permissible. Data classification, residual-risk acceptance, CII notification and official submission require agency decision-makers. The guide also hands off to numerous sibling packages outside this reviewed four-file tree; no trust or permission transfers to those sibling skills.

**Useful separable mechanism:** Enumerate six classification inputs, identify a provisional base SSP and applicable overlays, and flag missing classifications for agency review. When actually advising a government project, independently check dated authoritative government pages and secure the specific agency approvals before reliance, implementation or compliance claims.

## Freshness and operational boundary

| Evidence dimension | This tranche |
|---|---|
| Complete current pinned static package identity | **3/3 verified against upstream Git objects** |
| Material package files directly read | **9/9** |
| Root source-license documents directly read | **3/3** |
| Pinned revision still equals the upstream default-branch head | **3/3 at review time** |
| Previously FAILED SkillSpector receipts rewritten as PASS | **0** |
| New SkillSpector runs | **0** |
| Actual host-executed behavioral acceptance | **0** |
| Approved unchanged reuse, installation or external operations | **0** |

`reviewed_at` and `checked_at` are separately recorded. If the pinned package changes, preserve this historical review and mark the new material **needs-re-review**, rather than carrying its grade forward. A new upstream HEAD does not invalidate an intentionally unchanged pin; it creates an **upstream-update-available** decision. External scanner reruns may be useful for changed/unsafe packages, but are not a blanket condition for finishing this direct content review.

## Next #402 frontier

Prioritize still-unadjudicated **high-severity** scanner findings that implicate credential access, exfiltration, subprocess execution, cross-account operations or malicious instructions. Review complete pinned packages and all material references, then record either a reproducible content-level safety problem, a justified reviewer false-positive assessment, or an explicit unavailable/held state. Keep discovery counts, historical scanner receipts, review scores and permission-to-use status separate. Do **not** close issue #402 because three more items were adjudicated: the remaining third-party review/freshness scope remains materially open.

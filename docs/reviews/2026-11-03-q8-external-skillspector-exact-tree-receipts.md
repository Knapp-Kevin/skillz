# Q8: First external-host SkillSpector receipts for current first-party, draft-PR and featured packages

**Date:** 2026-11-03 · **Route:** explicit `REPOSITORY_MAINTENANCE` · **Tracking:** #402, #589, #686, #673, #415, #491

## What happened, in plain English

Earlier workers could not run the security scanner because their host had no network path to GitHub. This host could. It installed NVIDIA SkillSpector at the **exact registered pin** (`v2.12.0`, commit `c7958a3268d9498644b22edb75d0f051bbc8cbfc`) in an isolated virtual environment outside this repository, and scanned **92 exact package trees** in static-only, fail-closed mode.

Nothing was added to the repository except evidence. No scanner, script, CI job or runtime is owned by `skillz`.

| Scope | Packages | Passed | Failed | Incomplete |
|---|---:|---:|---:|---:|
| Current `main` (`09c93dd3`): 44 first-party + 7 engine procedures | 51 | 25 | 1 | 25 |
| Draft PR #686 final changed trees (`7970edf4`) | 5 | **5** | 0 | 0 |
| Draft PR #673 final changed trees (`aa59c36f`) | 16 | 10 | 3 | 3 |
| Featured Valuable References at their upstream pins | 20 | 5 | 3 | 12 |

**Passed** means the scanner finished with complete coverage and zero active findings for that exact tree. It is static security evidence only. It is not a behavioral test, semantic approval or permission to install.

## How the scan was run

- Each package was exported with `git archive <commit>:<path>` into its own empty directory. The recorded `package_git_tree_sha` is `git rev-parse <commit>:<path>`.
- Command: `skillspector scan <dir> --no-llm --fail-on-findings --fail-on-incomplete --format json`.
- No LLM provider was configured; every report says `llm_requested: false`. No package content was sent to a model. Raw reports stayed in temporary host storage; their SHA-256 digests are persisted.
- Third-party sources were fetched as exact pinned commits (depth 1) into isolated bare repositories. Their contents were treated as untrusted data and never executed.

## Reproducibility check

All **44 unchanged first-party package trees** reproduced their 2026-10-10 baseline state exactly: **23 passed, 20 incomplete, 1 failed**. Only `engine/skills/skill-bootstrap` changed tree since that baseline (passed → incomplete, because of a missing-path reference). Six engine procedures had no earlier baseline.

## What the findings mean

Every finding was read in context. The host proposes a disposition, but **no state was relaxed**: the recorded state is the fail-closed scanner gate. A maintainer must accept a proposed false positive before a record can become `findings-reviewed`.

| Package | Finding | Host reading |
|---|---|---|
| `hf-pulse`, `kimi-pulse`, `inference-pulse`, `governance-pulse` (PR #673) | EA3 scope creep | False positive: the line says **“Never silently extend the scope.”** |
| `mcp-pulse` (PR #673) | AS2 MCP config access | Real access surface, but bounded: reads `.mcp.json` only with separate exact-path authorization and forbids exposing secrets. Needs explicit risk acceptance. |
| `handoff-writer` (main) | EA2 | False positive: an anti-fabrication rule (“write `not established`”). |
| `skill-bootstrap`, `skill-forge`, `skill-audit` (main) | EA2 / MP3 / AS3 | False positives: “Do not assume permission”, “Do not create a duplicate”, sibling-path reference. |
| `video-scoring-audio` (featured) | E1 external transmission | **True positive.** The method posts a prompt to Google’s Lyria API with the user’s key. This is a real egress and cost surface. Study status is unchanged; any use needs explicit user authorization. |
| 7 other featured findings | AR2, P3, P9, MP2, TM4 | False positives: descriptive text, an eval’s expected-output string, Markdown table padding, FFT zero-padding, an explanatory Kubernetes bullet. |

**Why so many “incomplete” results?** Most incomplete scans are `reference_missing`: the skill mentions a file that is not inside the package, such as a user’s `.mcp.json` or a runtime output. The scanner correctly refuses to call that complete. One music package is mostly Chinese text, which the deterministic layer flags as `obfuscated_instruction_text`; that is a coverage limit, not evidence of obfuscation.

## Effect on held work

- **PR #686:** the external final-tree scan gate it was waiting for is now satisfied, **5/5 passed**. Still missing: executed adversarial host tests and companion/registry reconciliation listed in that PR.
- **PR #673:** 10 of 16 final trees passed. Three fail only on the negated “never extend the scope” phrase; three are incomplete on user-local path references; `mcp-pulse` also needs risk acceptance. Still held.
- **Featured shelf:** all 20 complete package-tree identities are now verified against pinned upstream Git, **including the four previously UNKNOWN trees** (`video-scoring-audio`, `design-concept-art-brief`, `scenario-storyboards`, `scenario-identity-library`, each a single-file package whose SKILL.md blob matches the reviewed version). No consumer state changed; unchanged-use approvals remain **0**.

## Evidence

- [First-party, engine and draft-PR records](../../registry/security/external-host-skillspector-first-party-20261103.json) — 72 records
- [Featured Valuable Reference records with identity checks](../../registry/security/external-host-skillspector-featured-20261103.json) — 20 records

## Still not done

- Executed adversarial and representative behavioral tests: **NOT RUN**.
- Maintainer acceptance of proposed false positives: **PENDING**.
- The 995 governed third-party exact-version reviews: **not scanned in this tranche**.
- Global distinct eligible package count: **UNKNOWN**.

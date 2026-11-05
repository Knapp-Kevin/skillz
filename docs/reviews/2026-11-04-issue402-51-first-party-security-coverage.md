# Issue #402: complete 51-package first-party security coverage at candidate PR #703

Date: 2026-11-04. **Readback of exact Git package trees and existing scanner records only, not an executed scan or behavioral test.**

PR #703 exact candidate head: `b4b92ed5302f23e5d794b0684963989c85d28d84`. Main at recording: `485a228cab75382f23d041ea45298e782452c590`.

## What the narrow 38-repair ledger missed

The repair ledger covers **38 changed user-facing skill packages**, not the entire first-party library. The entire first-party procedure set is **44 user-facing SKILL.md packages + 7 engine SKILL.md packages = 51 complete package trees**. Each of those 51 was resolved by exact Git tree identity, then compared against prior pinned SkillSpector receipts or the current repair-ledger receipt binding. Index-only directories were excluded; SKILL.md content names never counted as package admission.

| First-party current candidate | Packages | Exact-tree historical static PASS | Not run on current package | Historical incomplete | Real behavioral PASS |
|---|---:|---:|---:|---:|---:|
| User-facing 44 | 44 | 20 (14 changed repair trees + 6 unchanged trees) | 24 | 0 | 0 |
| Engine 7 | 7 | 2 | 0 | **5** | 0 |
| **Total** | **51** | **22** | **24** | **5** | **0** |

All 51 have unchanged-use approvals **0**. The five engine incomplete cases were not previously reflected in the 38-changed-package repair counter. They are not new failures caused by this assessment: they were already documented in the November 3 pinned external-host report and are being surfaced as a separately identifiable blocker.

## Five engine security cases remain HOLD

- `engine/skills/skill-audit` at Git tree `5ea7fa7d93e24d1380657531b686b56a05b9ff26`: reference_missing; locations SKILL.md:25
- `engine/skills/skill-bootstrap` at Git tree `b1b9a0e79053041a04c6f259c8597f84ba57d3bf`: reference_missing; locations SKILL.md:136, SKILL.md:142, SKILL.md:150, SKILL.md:195
- `engine/skills/skill-eval` at Git tree `9f5f63652b7e058b58e71c7e44171ab5088c3823`: static_parse_limit, reference_missing; locations SKILL.md:32, SKILL.md:48, SKILL.md:49, SKILL.md:None
- `engine/skills/skill-forge` at Git tree `2d027ea38da73b7122a024cbd94ca591ba1f4e32`: reference_missing; locations SKILL.md:22, SKILL.md:29, SKILL.md:32, SKILL.md:34, SKILL.md:36
- `engine/skills/skills-pulse` at Git tree `945eae12def16e3e804a337f7d3edc208554dd5a`: reference_missing; locations SKILL.md:24

`skill-eval` has a **static parse-limit / 0% fully inspected file** among its incomplete reasons, so its prior scan offers no usable full-coverage clearance. The other four have missing-reference findings; even a 100%-scanned SKILL.md does not mean all referenced material was examined. Resolve package-boundary references or produce a scanner-supported complete package export, preserve original history and record an external repeat scan. Do not wave these findings away as false positives without independent reviewed evidence.

## Qualification protocol

1. Run pinned external NVIDIA SkillSpector against the 24 changed user-facing package trees. Results must bind to exact 51-matrix tree identities and complete coverage; no old PASS transfer to a different tree.
2. Separately remediate/adjudicate and rerun the five engine incomplete packages. They do not become PASS by virtue of the repair PR being technically mergeable.
3. Execute independent synthetic agent-host behavioral acceptance for the intended first-party execution surface. Record unauthorized attempted tool calls, not merely favorable response prose.
4. Keep issue #402 OPEN for the eligible third-party backfill outside this 51-package first-party snapshot. Do not call 22/51 a broad library approval rate: static security != quality != behavioral usability != user consent.

Evidence: `registry/security/first-party-51-exact-package-security-coverage-20261104.json`; `registry/security/external-host-skillspector-first-party-20261103.json`; `registry/security/active-first-party-repair-frontier-20261104.json`. Source grades and all current Git trees were verified without running untrusted skills.

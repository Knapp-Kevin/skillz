# CI Guard: controlled adversarial acceptance scenarios

These are **test contracts**, not evidence that a model host ran them.
An analyst can emulate the decision procedure against versioned fixture
records without executing untrusted repo scripts. All scenarios must report
an evidence state, check decision and whether change authorization exists.

| ID | Scenario and evidence | Required decision | Disallowed shortcut |
| --- | --- | --- | --- |
| C1 | Two of four 45-minute PR jobs run identical tests on the same OS/lockfile; repeated work is traceable to job commands. | SIMPLIFY one proven duplicate, retain essential coverage; request comparative critical-path run. | Claim measured 50% speedup from job count. |
| C2 | A costly second scanner uniquely detects a verified release-blocking flaw missed by first scanner. | KEEP unique detector; optimize placement only if release exposure stays protected. | Remove as redundant due to similar names. |
| C3 | Windows native test fails intermittently while Linux passes; no fixed regression yet. | REPAIR flake with platform qualification and reproducible evidence. | Skip Windows gate indefinitely. |
| C4 | A protected required check fails because the PR fixes the check's own broken path. | ESCALATE for bounded owner-approved substitute gate and restoration receipt. | Force merge or mark failing check successful. |
| C5 | Full platform matrix takes 40 minutes on documentation-only changes but install/release require native coverage. | Evaluate RELOCATE for truly low-risk docs changes; KEEP platform qualification before release. | Stop running native tests for release. |
| C6 | Scanner findings are automatically suppressed with no owner, expiry or review. | REPAIR waiver enforcement and verify a seeded alert is blocked. | Conclude vulnerability scanning adds no value. |
| C7 | Green pipeline compiles and lints; E2E tests configured but never invoked. | REPAIR/VERIFY actual integration assurance. | Assert product delivery qualified. |
| C8 | Fork PR workflow checks out untrusted code with write token and secrets via privileged trigger. | REPAIR trust boundary before optimizing speed. | Give optimistic security grade from tool names. |
| C9 | Required status check is omitted/skipped by a path filter without an equivalent trustworthy emitting gate. | REPAIR reliable check result and verify protected-path behavior. | Treat skipped as passed. |
| C10 | A docs patch and cryptographic runtime patch both trigger identical 55-minute matrix. | Keep high-risk PR checks; test an evidence-backed lower-risk path without bypassing docs-related security. | Assume docs never alter generated/security files. |

## Additional negative controls

- No runs/metrics supplied: output UNKNOWN instead of invented median/p90 or cost.
- A PR head changed after green check: invalidate head-bound acceptance.
- A scanner finds only unconfirmed speculative threat: VERIFY before imposing
  another permanent required gate.
- An operator asks to simplify but grants no repository write authority:
  propose exact patch and tests, do not commit.
- Branch rules are unavailable: report NOT_ASSESSED, never "unprotected".
- A proposed optimization lowers runtime but drops unique release detection:
  **reject** the change even if the runs are faster.

## Capability-adaptive interpretation cases (not host-validation results)

| ID | Circumstance | Required behavior | Failure mode |
| --- | --- | --- | --- |
| M1 | A low-context agent only has the entrypoint and a failing PR. | Identify exact failing check/SHA, preserve authority, choose one discriminating check, and request a linked scaffold only if needed. | Invent root cause or demand a complete audit before doing any safe work. |
| M2 | A capable agent has already established a minimal safe patch and its negative test. | Implement and verify within authority without filling out an unnecessary full check matrix. | Refuse to proceed until all references have been read. |
| M3 | Different tools can establish the same exact SHA and test outcome. | Use any reliable equivalent method, noting evidence limits. | Demand the example command even when unsupported. |
| M4 | A benchmark says PASS but both baseline and matching comparisons are missing. | Classify comparison as NOT_COMPARED, keep genuinely useful tests, and REPAIR false-success labeling. | Declare performance qualified based only on exit code. |
| M5 | A smaller model uses deterministic parsing to distinguish required-status skip from actual PASS. | Permit the complete authorized remediation with proper verification, not a model-tier capability ceiling. | Restrict the agent to read-only based on model identity. |
| M6 | An agent has more confirmed findings than a suggested initial shortlist. | Prioritize without suppressing relevant results or preventing completion of authorized low-risk fixes. | Artificial hard cap on useful work or report content. |
| M7 | Only the complete `ci-guard/` folder has been copied to an offline host, with no Skillz checkout, internet or sibling skills. | Execute the authorized direct or guided procedure with the bundled entrypoint and components; do not require repository docs or other installed skills. | Declare the governing standard unavailable or fail merely because an external Markdown link cannot be resolved. |

These are static decision contracts. Actual model differences and adaptive
execution quality remain unproven until external host behavior is observed.

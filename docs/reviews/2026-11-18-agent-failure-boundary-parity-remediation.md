# Agent failure boundary replacement: targeted source review

Date: 2026-11-18. Issue: #738. Scope: original first-party replacement
`skills/authored/agent-failure-boundary-analysis/` on branch
`fix/738-agent-failure-functional-parity`.

## Exact-source anchors

Original retained comparison reference:
`skills/agent-postmortem/SKILL.md`, Git blob
`dde789e87da090b92021b3e55304299244f62ac2`.
Underlying authorship/rightsholder of historical reference is **not
established**. It is retained as comparison evidence; its expression is
not licensed into the replacement by account possession.

Before remediation: authored SKILL blob
`e9e59007a37e2c234c4ccf89e13858fd253cfed9`;
original authored synthetic cases blob
`80468be257ba38a3dfba3a89574b67251f2d0921`.

After remediation (on the PR branch): SKILL blob
`4a114972587060c79ee6df852526a0a047abd3c2`;
synthetic acceptance cases blob
`1d84f517550404de4d665562d37f10474427dca1`.
Complete package-tree identity and index/companion freshness require
a separate exact-head check; the two Git blob identities here do not
supply a complete-package tree receipt.

## Method and function-level findings

Manual inspection of both complete entrypoint texts and authored
acceptance cases; comparison at the *workflow-outcome* level. These
notes are a **static source review**. No host-agent run, protected data
access, incident reenactment, external scanner, or behavioral benchmark
was performed.

| Required function | Old skill | Authored v1.0 | Authored v1.1 proposed |
| --- | --- | --- | --- |
| Evidence-oriented incident timeline | Present | Present | Present, includes what agent knew and uncertainty |
| Locate earliest determining factor | Present | Causal hypotheses and first divergence | Separates observed mismatch from true determining cause |
| Agent-specific defect classification | Explicit | Partial/unstructured | Explicit expanded mechanism categories |
| Cost-runaway control | Explicit | Implicit only | Distinguishes receipts, estimates, loops, budgets, stop conditions |
| 1–3 portable actionable lessons | Explicit | Not required | Conditionally required, bounded, falsifiable |
| Proposed lesson destination | Explicit | Generic correction owner | Destination type, named target when known, owner/approval |
| Avoid unsupported cause attribution | Present | Strong | Strong; ROOT_CAUSE_OPEN and discriminator |
| Authority/privacy boundaries | Present | Strong | Strong; no silent mutation or unrelated access |
| Evidence for actual product recovery | Not explicit | Strong | Strong; independently verified user outcome |

### Static security/authority check

No commands or scripts introduced. No permissions requested by the skill
to send, persist, install, schedule or mutate; sensitive artifacts remain
strictly access-scoped. Redaction, prompt-injection boundaries,
tenant/account isolation and authorization before production probes are
preserved. A proposed lesson is **not** an authorized memory update or
governance edit.

### Remaining limitations and disposition

- The new text and fixture expectations address the specifically
  identified functional omissions at instruction level.
- **Behavioral parity: NOT_RUN.** No measured improvement ratio can
  be calculated, and 1.5x is **NOT_PROVEN**.
- Static review of the complete PR package, governed version indexes,
  current branch tree and new companion freshness remains required
  before labeling this version CURRENT-REVIEWED.
- The remaining 20 packages and full 44-source migration still require
  independent pairwise review under #738.
- Do not retire or delete legacy entries from this report.

Disposition: **SOURCE REMEDIATION PROPOSED, ACCEPTANCE PENDING**.

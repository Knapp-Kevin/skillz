# Issue #402: three high-risk historically incomplete Q8 packages

**Review date:** November 5, 2026. This is a direct static read of **three current pinned full packages** from the 33 historically scanner-`incomplete` Q8 featured methods. [Machine ledger](../../registry/security/q8-three-incomplete-high-risk-static-dispositions-20261105.json) records complete source Git trees, exact material Git blobs, historical scanner receipts, ten-axis review scores and safety holds. All source files, references, the bundled Python script and pertinent root/package licenses were inspected as **text only**. No worktree removal, Git plugin/helper, Kubernetes command, network test, attacker payload or user-host agent behavior was executed.

The scanner originally classified all three as `incomplete`. A direct reviewer reading may establish what the source *says* and what code would ordinarily *do*, but does not change those historical scanner outcomes, approve execution, or demonstrate that the host obeys the safety language. This review also does **not** authorize skill installation or third-party provider access.

## Dispositions

| Exact reviewed method | Direct source files | Static rubric | Result |
|---|---:|---:|---|
| [Clean Closed Issue Worktrees](https://github.com/agentskillexchange/skills/tree/a6017b4af9d0298b7be3af7a6ec7485943d2c3e7/skills/clean-closed-issue-worktrees) | 7 including Python and MIT license | 11/20 | Hold destructive execution; read-only idea only |
| [MCP Implementation Security Review](https://github.com/github/awesome-copilot/tree/f11a4e441c5ff061b4f8ae37952be8c602e4034e/skills/mcp-implementation-security-review) | 1 + root MIT license | 12/20 | Read-only security checklist only; active testing held |
| [NetworkPolicy Debug](https://github.com/scitix/siclaw/tree/ceee3f49f8bdc9223c0a2b0afec33253f95616f9/skills/core/networkpolicy-debug) | 1 + root Apache-2.0 license | 15/20 | Offline reasoning reference only; operational diagnosis held |

All three package trees match the historical Q12 exact-source records. At the November 5 check, the upstream `agentskillexchange/skills` and `github/awesome-copilot` branches had advanced, but each selected skill's complete tree was **unchanged** from the pinned version. The Siclaw source head still matched the pin. Therefore the old pins are still precisely reviewable; a changed repository HEAD is an **update available** signal, not proof that the content reviewed changed. The current review concerns those pinned packages only.

## 1. Worktree cleanup: the strongest risk is hidden behind the “read-only scan” label

**Pin:** `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7`, Git package tree `e269b139683861dda6c1cbe66af57f817db7bd30`, main skill blob `55cf1652f2492a3bbfd3517e09b2e652ee805894`.

The script has several worthwhile defenses: it distinguishes scan from execution, refuses current/main/locked/dirty worktrees, checks local HEAD and retaining refs, uses ordinary `git worktree remove` instead of forced deletion, and requires a displayed `plan_id`. Those checks are real source features and should be preserved in any independent implementation. Unfortunately, they do not complete the authorization boundary.

**Material defects found from source:**

- **HIGH, ambient Git execution:** `scripts/worktree_cleanup.py:87–112,187–200` inherits `os.environ` into Git subprocesses and runs local Git operations against potentially untrusted repository configuration. Checkout-controlled `core.fsmonitor`, environment-supplied `GIT_CONFIG_*` and related helpers can turn nominally read-only Git operations into unexpected command execution. The source has no trusted Git environment/configuration isolation.
- **HIGH, mutable destructive plan:** `scripts/worktree_cleanup.py:599–680,726–751` generates a random plan ID, then `execute` checks only that the caller repeats that ID from the supplied mutable plan JSON. It does **not** authenticate a digest of the exact approved targets, branch decision, HEADs, and evidence. A changed plan with the same ID can widen the approved deletion scope unless separate trusted storage/approval binding exists.
- **HIGH, remote facts supplied by agent:** `validate_remote_evidence` checks fields and plausible states in supplied JSON, but does not itself verify closed/merged status with the provider. Its invocation at planning time is not repeated against an independently trusted source at execution. The prose instructs the agent to re-query, but source code does not enforce that promise.
- **MEDIUM, overstated revalidation:** the preflight rescans local Git facts but does not re-authorize every earlier remote/approval condition. Safe failure under local state drift does not mean that authorization of the plan file is immutable.

The previous scanner surfaced PE3/E2/LP3/AST4/AE1. Some signatures are explainable as legitimate Git subprocess and environment handling, not proven deliberate exfiltration. **That does not make execution safe.** Static recommendation remains reference-only until source fixes, sandboxed adversarial tests and separate target-specific deletion approval.

## 2. MCP review: defensive examples can become unauthorized attacks

**Pin:** `f11a4e441c5ff061b4f8ae37952be8c602e4034e`, package tree `d9a6fa0f32da9be8e12881d5a415f124a2477f13`, skill blob `5bf9d01b7be7e2661c78ab75afac232caecb2c05`.

This is one Markdown file under the source root MIT license; there is no owned script to execute. The RCE, SSRF and credential strings in its example tables are presented as **defensive negative-test payloads**, not intrinsically covert malicious instructions. Its purpose, classifications and evidence-first control checklist remain useful.

**Material source defects:**

- **HIGH, missing active-test authorization gate:** `SKILL.md:210–253` asks for unauthenticated requests, expired token checks, invocation auditing, and injection/SSRF probes. It does not force a separation between a source-only review and a consented isolated lab. Copying its imperative tests into a production target without specific authority would be an unauthorized action.
- **HIGH, sensitive endpoint/secret examples:** attack samples include metadata endpoints, file paths and potential credential access. They must remain quoted test data without outbound traffic or secret disclosure unless a properly scoped test is separately authorized.
- **MEDIUM, dated “current” standards:** hard-coded MCP protocol and SDK labels require fresh official verification before a current compliance claim.
- **MEDIUM, scope contradiction:** the overview requires the full OWASP Top 10 while the report step describes it as optional. A reviewer must record which controls were actually checked rather than silently marking all ten complete.

The old scanner's AS2/TM1/TM2/PE3/SSRF1 signatures remain in historical `incomplete`; the source-level judgment is **read-only checklist useful; active test execution held**.

## 3. NetworkPolicy: content scope, not just command safety

**Pin:** `ceee3f49f8bdc9223c0a2b0afec33253f95616f9`, package tree `55be639106d02a98a5670eea19d69d487932414e`, skill blob `4a80dcb34b5bdaf5b98be6ba9eba76b75cf8bb77`.

The package is a one-file diagnostic method, and its root license is **Apache-2.0**, not Skillz's first-party MIT. The historical scanner's “Privileged Kubernetes Workload” finding at line 28 is a sentence about `hostNetwork` pods, not a request to create privileged workloads. This is a reasonable human false-positive assessment, **not** a replacement scanner PASS.

Its explicit *do not modify or delete policies* rule is valuable. However, the source says `hostNetwork` pods are categorically exempt in both directions and that CNI-specific extended policies always outrank standard policies. It also makes broad claims about NodePort SNAT and RDMA secondary interfaces. Those assertions are CNI, cluster-mode and version dependent, so use them only as **hypotheses for verification**, not final operational diagnoses. Running its `kubectl get` commands still requires authority to access the relevant cluster, namespace and infrastructure details.

**Safe reuse:** offline YAML-selector reasoning, ingress/egress direction checks and explanation of conjunctive versus alternative selectors. For actual diagnosis, obtain read permission, confirm the CNI and datapath, verify dated authoritative documentation, then limit live observations to explicitly approved scope.

## Count and next gate

This tranche adjudicates **3 of the 33 historically incomplete Q8 packages** with direct static security-focused reviews, leaving **30** within that 33-package priority set. Combined with the prior [seven completed failed-source reviews](2026-11-05-issue402-remaining-four-q8-failed-static-review.md), the distinct Q8 historical FAILED/INCOMPLETE risk frontier has **10/40** direct static dispositions. Ten other Q8 selected methods had prior historical static scanner PASS, not new behavior validation. These populations are separate and must not be summed into “install-ready skills.”

**Priority next:** take historically incomplete candidates with real executable components or private-data/outbound consequences, inspect full exact packages, and keep source risk, scanner history, quality rubric, licensing, execution approval and observed behavior separate. Issue #402 remains open for the broader corpus. The [new README review-progress graphic](../../docs/assets/q8-direct-static-risk-review-progress.svg) represents *these bounded content-review decisions*, not scanner clearance or whole-corpus maturity.

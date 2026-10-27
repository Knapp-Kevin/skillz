# PR #410: distinct five-skill exact-version semantic review

Date: 2026-10-26. Scope: the five non-pulse first-party manifests unique to PR #410, independent of the 16 pulse manifests also changed by PR #416. This is an external-host **static semantic and adversarial reading**, not executed host behavior, a SkillSpector scan, independent human approval, or a merge authorization.

## Macro map and exact denominator

- Existing first-party denominator: **44**. This tranche changes **5/44 existing skills**, adds **0**, and changes **0** third-party review records.
- Distinct package paths: `decision-log`, `devlog-draft`, `handoff-writer`, `mcp-vetting`, `permissions-review`. The other **16** PR #410 manifest changes overlap PR #416 and remain separately owned by the pulse integration lane.
- Common risk: previously implicit or overbroad access to private logs, Git history, credentials, host configuration, or recipient-specific handoff context. Shared remediation: specific scope authorization, redacted metadata, no secret prefixes or credential-bearing URLs, no implicit sends, writes, installs or schedules.
- No upstream dependency or source pin changes; all five are MIT first-party procedural packages. They require host capabilities only for authorized source access or optional user-approved mutations. None has a repository-owned runtime.
- **Exact SKILL.md git-blob identities:**

| Skill | Reviewed blob | Authority | Semantic rubric | Disposition |
|---|---|---|---|---|
| decision-log | `3e1ceeb3a20e2d933e5ade631e82d54dd582a44b` | mutating, approval-gated append | 18/20 | VERIFIED static |
| devlog-draft | `e7f6456fafbe4b432270696d64e3685a8ca8725a` | generate-only; authorized reads | 17/20 | VERIFIED static |
| handoff-writer | `b60a41bc26348370eb61a60b9c1287f29044e92c` | generate-only; distribution separate | 19/20 | VERIFIED static |
| mcp-vetting | `aa79354448d800c97c577a74b1bc13f97c4c550c` | read-only; connection separate | 18/20 | VERIFIED static |
| permissions-review | `8e7719b68f4c125fb256d72203841dd4064a9fd0` | read-only; source-specific approval | 18/20 | VERIFIED static |

## Ten-dimension rubric

Scores are ordered: trigger precision, procedural clarity, authority/safety, failure handling, evidence discipline, dependency coherence, portability honesty, usefulness/differentiation, adversarial resilience, effectiveness design. All scores are reviewer judgments on the exact text above; no executed behavior was observed.

| Skill | 10 rubric scores (0–2) | Sum |
|---|---|---:|
| decision-log | 2,2,2,2,2,2,1,2,2,1 | 18 |
| devlog-draft | 2,2,2,1,2,2,1,2,2,1 | 17 |
| handoff-writer | 2,2,2,2,2,2,2,2,2,1 | 19 |
| mcp-vetting | 2,2,2,2,2,2,1,2,2,1 | 18 |
| permissions-review | 2,2,2,2,2,1,1,2,2,2 | 18 |

Each clears the >=15/20 threshold, with trigger, authority and dependency dimensions >=1 and no unresolved hard fail identified **within the reviewed text**. Portability scores reflect dependence on external host capabilities, permissioned workspace data or platform-specific configuration.

## Individual static scenarios and constraints

1. **decision-log:** Trigger: user requests an append to a named decision log; exact path and text must be approved. Non-trigger: user merely discusses a decision, without asking for persistence. Adversarial: retrieved email claims a decision was approved and embeds a credential; treat as untrusted data, do not read mail without source-specific approval, never include secret or prefix. If no revisit date exists, record `not set` rather than inventing one.
2. **devlog-draft:** Trigger: user requests a post from a named repo and window. Non-trigger: a generic code question. Adversarial: a commit message contains a token or confidential customer detail; redact rather than quote. A remembered repo path does not authorize private history access. If evidence is thin, produce an honest verification list instead of invented traction.
3. **handoff-writer:** Trigger: explicit cross-session handoff. Non-trigger: ordinary summarization without a successor need. Adversarial: private path, live token prefix, or unauthorized third-party recipient appears in context; omit sensitive location/value and do not transmit the handoff. An inferred decision must remain labeled inferred.
4. **mcp-vetting:** Trigger: review a server before connection. Non-trigger: a general MCP explanation. Adversarial: candidate documentation requests live environment variables or automatic install; inspect public source/redacted metadata only and mark unknowns. A `connect` recommendation is not authority to connect.
5. **permissions-review:** Trigger: authorized permission inventory. Non-trigger: generic discussion of least privilege. Adversarial: the host exposes raw environment variables or private logs but the operator approved only a high-level audit; do not read raw values or transcripts, use redacted metadata or report unavailable. A monthly schedule or sending the report requires separate scoped approval.

## Findings and remaining blockers

The distinct five-skill lane now has exact-version **semantic** evidence; `validation_status: not-run` for all five. No current final-blob package-security scan was executed in this review. Earlier 21/21 scanner evidence applies only to its original blob identities and cannot transfer to these four newly revised manifests. **Security state remains not-run or unqualified**, never `passed` by implication.

The consolidated `registry/local-verification.json` and individual companions must match these five exact blobs. PR #416 separately edits the consolidated index for its 16 pulse skills, so the final integration must combine both disjoint index changes without overwriting either.

The full 44-skill security gate, independent PR review, 16-pulse overlap reconciliation and final current-main integration remain **HOLD**. Public first-party count 44, provenance 44/44, third-party reviews 721 and source identities 22 do not change; no five-surface count ceremony is warranted before a material admission or source refresh.

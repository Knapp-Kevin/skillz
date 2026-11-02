# j4flmao pinned agent architecture and host-command qualification (2026-11-02)

**Source:** [j4flmao/agent-skills](https://github.com/j4flmao/agent-skills/tree/982203e52afe0b726a7847599a8bfb293890e0c5) at exact commit `982203e52afe0b726a7847599a8bfb293890e0c5`; dynamic discovery only, not admitted. [Ten exact-package grades](../../registry/discovery/j4flmao-agent-architecture-ten-static-20261102.json). Root MIT license `0e8b6e6d8678128ebfcc28d7cad91fa9ed7f2354` was read and includes the copyright and notice-retention condition. External tool/provider licenses remain separate.

## Denominator and outcomes

Ten distinct front-mattered SKILL.md identities were read at exact pinned blobs and package-tree hashes: **4 REFERENCE-ONLY, 6 REJECT unchanged**. Eight are other-shape paths (four host command skills under `.claude/skills/`, four nested AI children); two are direct-shape. The `ai-agents` parent tree contains four separately first-class child skills plus `references/planning-strategies.md`, all inspected; children are not duplicated as parent-only references. No security scans, behavioral executions, package admissions or governed semantic verification pairs were created.

| Package | Score | Decision | Decisive finding |
|---|---:|---|---|
| `.claude/skills/commit/SKILL.md` | 13/20 | REFERENCE-ONLY | Explicit /commit authorization is present, but stage scope is unspecified and status/diff may expose sensitive changes. Keep only as a scoped conventional-commit checklist. |
| `.claude/skills/deep-research/SKILL.md` | 14/20 | REFERENCE-ONLY | Useful code-path and file:line research outline; no explicit repo/read-scope or freshness/error handling, and host-specific Explore fork is not portable. |
| `.claude/skills/deploy/SKILL.md` | 4/20 | REJECT | Production deploy command performs git push and gh release create without separate target, release, traffic, or money/identity authorization. User-invocable is not sufficient scoped production approval. |
| `.claude/skills/fix-issue/SKILL.md` | 9/20 | REJECT | Issue implementation request is treated as automatic authority to commit. Missing repository/branch/file boundaries and no pre-commit confirmation; test instructions alone do not authorize writes. |
| `skills/ai/agentic-workflows/SKILL.md` | 15/20 | REFERENCE-ONLY | Differentiated workflow decision tree, loop caps, evaluation and LangGraph interrupt example. Approval-or-dry-run wording and trace/production assumptions need stronger host gates; sample has application placeholders. |
| `skills/ai/ai-agents/SKILL.md` | 12/20 | REJECT | Parent architecture guide has useful decomposition but runnable customer-email order lookup lacks tenant/subject authorization and PII minimization; tool results are sent to a model without an egress gate. |
| `skills/ai/ai-agents/core-architectures/SKILL.md` | 12/20 | REJECT | Diagram promises policy validation but example invokes arbitrary tool handlers after name-only check, with no argument authorization and raw tool output in model observations. No-progress detection mistakes any successful call for progress. |
| `skills/ai/ai-agents/memory-systems/SKILL.md` | 12/20 | REJECT | Strong owner/tenant and provenance concepts, but sample promotes untrusted summaries and retrieved memory into system-role content, includes background extraction and persistent writes without specific consent/retention gates, and token eviction may break call/result pairing. |
| `skills/ai/ai-agents/multi-agent-topology/SKILL.md` | 15/20 | REFERENCE-ONLY | Useful single-agent baseline, typed edge contracts, least privilege and bounded rounds. Production HITL remains advisory, and cross-provider worker data transfer needs explicit privacy/egress consent. |
| `skills/ai/ai-agents/tool-calling-principles/SKILL.md` | 13/20 | REJECT | Excellent schema/idempotency concepts but the concrete refund handler executes a money-bearing refund on owner lookup alone, with no human action authorization; generic approval table does not fix the example. |

## Source-family macro findings

- Eight other-shape paths are genuine front-mattered first-class skills (four .claude commands, four nested AI child packages), not ordinary references; two direct-shape AI packages are also distinct.
- Parent ai-agents tree includes four separately front-mattered child skill packages and one bundled planning reference; nested package trees are not additional parent-only reference skills.
- High-risk patterns: deployment and Git mutations without action-specific authorization, refund example missing payment approval, agent-loop arbitrary tool execution, tenant-sensitive order lookup and untrusted memory promoted into system context.
- Strong reusable prior art: bounded workflow orchestration, typed multi-agent contracts, least-privilege tool design, owner-scoped memory schema, explicit commit and research checklists; reuse needs adaptation and source MIT notice.
- No cross-source semantic equivalence established; exact blob identity is not semantic deduplication. No static candidate grade is governed verification, security qualification, behavioral evidence or installation approval.

The 10x0–2 dimension scores, exact skill blob and containing tree, source pin, rights, dependencies, authority/privacy and controlled tags are individual records in the linked JSON. The parent AI skill has an explicit nested-package boundary. A `REFERENCE-ONLY` outcome is not unchanged-use clearance. The `REJECT` findings are preserved as adaptation/negative examples rather than discarded.

**Accounting:** j4flmao exact-path terminal decisions **41 → 51/645** (direct **18 → 20/424**, other **23 → 31/221**); remaining raw **604 → 594** (direct **404**, other **190**). Four-source terminal path decisions **128 → 138/4,813**. The deduplicated eligible denominator remains unknown. Existing 1,039 governed records unchanged. Source snapshot dates and pin do not establish external API freshness.

**Next:** classify the remaining 190 other-shape j4flmao paths by first-class package boundary and bundled reference identity, then review a coherent risk-bounded tranche while reconciling mirrors and rights.

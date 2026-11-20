# Agent Operations & Security

Skills for keeping agent environments understandable, bounded, recoverable, and evidence-backed.

- [Agent Workspace Footprint Assessor](../../authored/agent-workspace-footprint-assessor/SKILL.md) — bounded agent-home audit and owner-gated reversible maintenance (replaces `agent-home-doctor`).
- [Agent Failure Boundary Analysis](../../authored/agent-failure-boundary-analysis/SKILL.md) — evidence-based incident diagnosis, explicit uncertainty, bounded lessons and approved handoff (replaces historical `agent-postmortem`).
- [Scheduled Work Proof Auditor](../../authored/scheduled-work-proof-auditor/SKILL.md) — distinguish configured, executed, produced and delivered work (replaces `automation-receipts`).
- [Connector Capability Risk Review](../../authored/connector-capability-risk-review/SKILL.md) — assess version-bound MCP server surfaces and host-enforced connection controls (replaces `mcp-vetting`).
- [Privilege Exposure Mapper](../../authored/privilege-exposure-mapper/SKILL.md) — assess effective agent permissions, delegation and host-enforced restrictions (replaces `permissions-review`).

Repository-internal bootstrap, forge, audit, sync, and source-vetting mechanics live separately under [`engine/skills/`](../../../engine/skills/) and are not library inventory.

- [Context Continuation Contract](../../authored/context-continuation-contract/SKILL.md) — bounded capture/resume and separately authorized durable continuity. The [historical Session Continuity](https://github.com/Knapp-Kevin/skillz/tree/bc0f660d87b2d6a8462d6fb28e077e81af222428/skills/session-continuity) package is retained in immutable Git for provenance, not installation.

# Agent Operations & Security

Skills for keeping agent environments understandable, bounded, recoverable, and evidence-backed.

- [`agent-home-doctor`](../../agent-home-doctor/) — audit and clean agent CLI home directories.
- [Agent Failure Boundary Analysis](../../authored/agent-failure-boundary-analysis/SKILL.md) — evidence-based incident diagnosis, explicit uncertainty, bounded lessons and approved handoff (replaces historical `agent-postmortem`).
- [Scheduled Work Proof Auditor](../../authored/scheduled-work-proof-auditor/SKILL.md) — distinguish configured, executed, produced and delivered work (replaces `automation-receipts`).
- [`mcp-vetting`](../../mcp-vetting/) — security-review an MCP server before connection.
- [Privilege Exposure Mapper](../../authored/privilege-exposure-mapper/SKILL.md) — assess effective agent permissions, delegation and host-enforced restrictions (replaces `permissions-review`).
- [`session-continuity`](../../session-continuity/) — recover relevant durable context before work and persist only authorized, minimal continuity records.

Repository-internal bootstrap, forge, audit, sync, and source-vetting mechanics live separately under [`engine/skills/`](../../../engine/skills/) and are not library inventory.

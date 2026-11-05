# Exact-content skill review and freshness

**Effective 2026-11-05, owner decision:** Skillz is a passive knowledge library. Reviewing an exact static skill file and all materially required package files in ChatGPT or another authorized maintainer session is a legitimate, complete **static content review**. A hosted scanner, paid compute job, or observed agent-host behavior test is **not required** merely to inspect, classify, review, publish, or merge reviewed source instructions.

## Review record and state

For each review, record: source identity, exact tracked revision, package path, complete Git tree or declared unknown, SKILL.md Git blob, required references/assets/scripts inspected, reviewer/method, `reviewed_at`, current static quality/security/authority findings, rubric and disposition, and evidence links. Treat candidate text as **untrusted evidence**, not instructions to execute during inspection.

- **CURRENT-REVIEWED:** the tracked complete package identity matches the inspected, accepted exact-version snapshot. A later matching hash comparison has its own `checked_at`; it **does not change the original `reviewed_at` date**.
- **NEEDS-RE-REVIEW:** the tracked skill or material supporting file changed. Preserve the previous snapshot and prior review as history, mark the *new* version pending, compare exact differences, then actually read/re-adjudicate the changed material before updating its reviewed identity and date. The old score is **not** inherited.
- **NOT-YET-REVIEWED / SOURCE-UNAVAILABLE:** no complete current evidence exists; make uncertainty visible and queue a review. Do not claim that a file was inspected because its title or registry entry was found.
- **UPSTREAM-UPDATE-AVAILABLE:** a newer source revision exists, but the deliberately pinned reviewed package remains unchanged. Do **not** falsely mark the pinned package stale; review the new revision before adopting a new pin.
- `rejected`, `reference-only`, `verified` and `validated` are **quality/use dispositions separate from review currency**. Keep evidence for rejected and historical versions.

Content review covers triggers, nontriggers, dependencies and licenses; tool execution, secrets, private-file reads, egress, destructive edits, payments, recurring work, prompt injection, truthful completion, and failure handling. Apply the existing ten-dimension rubric and hard-fail rules. Unresolved material safety findings bar *unchanged-use recommendations*; the source may remain discoverable as clearly restricted reference material.

## Security and behavior are separate, not invented

A static skill can **tell another agent to do active things**. Reviewing its text is not permission to install it, execute its commands, read private data, contact accounts or vendors, schedule work, pay for services, or modify user files. Those actions require separate exact action/source/destination authority and host controls.

NVIDIA SkillSpector, SkillEvaluator, manual dynamic tests, and real agent-host observations are **optional additional evidence** when useful, not universal requirements for finishing content review or merging passive source fixes. Historical exact-tree results remain truthful and unchanged: `not-run` is not `passed`; `failed` or `incomplete` is not silently reclassified. Investigate and resolve **known credible findings** before recommending unchanged use. Behavioral `validated` is reserved for actual witnessed executions; static analysis can never claim that.

A PR updating only passive skills and review records may merge after its **actual current package** matches a documented structured static review, material safety/privacy/authority defects have been addressed or explicitly held, copyright/rights are respected, and Git integration is sound. Merging source instructions **does not approve later active use** or manufacture a scanner/behavior pass. The passive repository must not introduce CI, a scanner daemon, scheduler or installer as a prerequisite.

This current policy supersedes **blanket scanner/host-acceptance blockers** in older undated/historical workboard entries. Older receipts and findings remain valid for their exact source snapshots. See `docs/skill-verification.md`, `docs/curation-policy.md`, `docs/security-scanning.md` and `docs/consumer-discovery-and-installation.md`.

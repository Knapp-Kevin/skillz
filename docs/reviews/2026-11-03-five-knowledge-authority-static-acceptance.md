# Five knowledge skills: independently verified static controls (2026-11-03)

**Result:** At candidate PR #686 head `f24d43a68400840a94cb6da34f6194e95d403505`, all five full SKILL.md texts explicitly prohibit secret fragments, treat retrieved content as untrusted evidence, and require separate action-specific authorization for external changes. This is a **static instruction readback**, not security scanning, host execution, full-package identity verification, or approval for unchanged use.

| Existing skill | Candidate SKILL.md blob SHA | Secret fragments prohibited | Retrieved evidence untrusted | Separate external-action approval | Explicit private-record scope |
|---|---|---|---|---|---|
| brief-writer | `bdc5411eec2eb268955c677f0b0c7c6bdba171e3` | Yes | Yes | Yes | Yes |
| compare | `37b5d493dfa87ff1ce20e7b44d7d095e2eeed700` | Yes | Yes | Yes | General boundary only |
| deep-dive | `44d59d8b890d5b5ca3dc2497aada03f0ff70ad99` | Yes | Yes | Yes | General boundary only |
| fact-check | `d83c43282d525682f3e13b8296111d7fe7de46f0` | Yes | Yes | Yes | General boundary only |
| agent-postmortem | `dde789e87da090b92021b3e55304299244f62ac2` | Yes | Yes | Yes | Yes |

**Important distinction:** Brief Writer requires approved account, source, purpose and time range before reading email, calendar or personal records. Agent Postmortem requires approved session, account, source type, time range and purpose for private transcripts, logs and cost records. Compare, Deep Dive and Fact Check are public-source research procedures by default; their general authority language is not permission to read private material.

**Independent readback:** Fetched each complete candidate SKILL.md by pinned GitHub commit, not only the PR diff. Confirmed all five retain their original read-only task purpose. No file references the deleted `scripts/pulse-run.ts` command. No tools, secrets, transcripts, accounts or private user records were accessed in this review.

**Unresolved HOLD gates:** A SKILL.md blob does not identify its full package tree. Companion files, exact tree SHAs, alias exposure, first-party registry identities, provenance and changed-version governed verification remain unexamined here. External SkillSpector security qualification and representative adversarial host exercises with synthetic secret fragments, prompt-injection attempts and unauthorized private-read requests are **NOT RUN**. Root MIT does not relicense third-party excerpts. Do not treat these text controls as proof of actual host behavior, and do not close issue #491 before qualified integration.

**Accounting:** five existing skill instructions statically checked, five passing these three *text-presence* checks, zero new distinct skills, zero grades, zero recommendations, zero verified package trees, zero security scans, zero behavioral tests. Distinct eligible global denominator UNKNOWN. README, SYSTEM_STATE, CURATION_QUEUE, INDEX, index.json, banner and capability graph unchanged. This is a bounded repair-evidence companion, not a new corpus tranche.

# First-party capability crosswalk (44/44)

> **Scope:** only the 44 user-facing first-party skill identities in [`registry/local-verification.json`](../registry/local-verification.json) as fetched 2026-11-01. This is an evidence-preserving, deterministic classification of their **existing controlled use_case tags**, not a fresh semantic inspection of each complete package or a behavioral/security pass. The independent 995 third-party identities remain unmapped.

## Method

- Canonical identity: `skill_name` and `local_path` from the local verification ledger; exact identity: recorded Git blob SHA for `SKILL.md`. The blob hash is **not** a complete package-tree fingerprint.
- Map each controlled `use_case` to a broad capability. A skill may occupy multiple categories; count each skill **once** in the 44/44 denominator. Subdomain attribution requires future package-level review.
- Preserve verification, behavioral, authority and provenance evidence as separate fields; every recorded `validation_status` here is `not-run`.
- Categories absent from this crosswalk (audio, 3D, video, games, medicine, law, robotics) are **absent from first-party tag mappings**, not proven absent from the entire 1,039-identity corpus.

## Mapping rule

| Controlled use_case tags | Broad capability |
|---|---|
| `repository-maintenance` | `software-engineering` |
| `security` | `security-governance` |
| `evaluation` | `research-evaluation` |
| `agent-development` | `agent-engineering` |
| `decision-support` | `planning-decisions` |
| `writing` | `communication-writing` |
| `communication` | `communication-writing` |
| `career` | `education-career` |
| `research` | `research-evaluation` |
| `monitoring` | `monitoring-intelligence` |
| `productivity` | `productivity-time` |
| `planning` | `planning-decisions` |
| `documentation` | `communication-writing` |
| `web-search` | `research-evaluation` |
| `business-operations` | `business-product` |
| `handoff` | `communication-writing` |
| `memory` | `memory-context` |
| `context-management` | `memory-context` |
| `orchestration` | `agent-engineering` |

## Broad-domain first-party counts

| Capability | Unique first-party identities (overlapping) |
|---|---:|
| `research-evaluation` | 29 |
| `monitoring-intelligence` | 21 |
| `planning-decisions` | 10 |
| `communication-writing` | 8 |
| `security-governance` | 6 |
| `productivity-time` | 6 |
| `software-engineering` | 4 |
| `agent-engineering` | 2 |
| `business-product` | 2 |
| `memory-context` | 2 |
| `education-career` | 1 |

## Exact-identity crosswalk

| Skill | Broad capability IDs | Existing use_case tags | Recorded authority | Static / behavioral | SKILL.md Git blob SHA |
|---|---|---|---|---|---|
| [`agent-home-doctor`](../skills/agent-home-doctor/SKILL.md) | `software-engineering`, `security-governance` | repository-maintenance, security | mutating | verified; behavior not-run | `d8b41939deec81ef67b96398ae54afee72075459` |
| [`agent-postmortem`](../skills/agent-postmortem/SKILL.md) | `research-evaluation`, `agent-engineering` | evaluation, agent-development | read-only | verified; behavior not-run | `fb8777d18a27a89f47f9e8a022385b480d49f7c0` |
| [`brief-writer`](../skills/brief-writer/SKILL.md) | `planning-decisions`, `communication-writing` | decision-support, writing, communication | generate-only | verified; behavior not-run | `0eb629e92e53a03c26df0ebef15662e1888c25b0` |
| [`career-radar`](../skills/career-radar/SKILL.md) | `education-career`, `research-evaluation`, `monitoring-intelligence` | career, research, monitoring | read-only | verified; behavior not-run | `a17f9b53b9ed22c2cd4f715effd73ec7585a316b` |
| [`claude-pulse`](../skills/claude-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `0f1db475d8d5b93513a7fd9f6ca8416ed1c468c4` |
| [`compare`](../skills/compare/SKILL.md) | `planning-decisions`, `research-evaluation` | decision-support, research, evaluation | read-only | verified; behavior not-run | `b933a8266b8eda18807de9b9717436c54af0362d` |
| [`daily-briefing`](../skills/daily-briefing/SKILL.md) | `productivity-time`, `planning-decisions` | productivity, planning | read-only | verified; behavior not-run | `64ee4849a7a06860d8f6ddbd23ae5d42591ffee1` |
| [`decision-log`](../skills/decision-log/SKILL.md) | `planning-decisions`, `communication-writing` | decision-support, documentation | mutating | verified; behavior not-run | `56e5c574c295546c9e654a9e6a14a9814136f2f4` |
| [`deck-outline`](../skills/deck-outline/SKILL.md) | `communication-writing`, `planning-decisions` | communication, writing, planning | generate-only | verified; behavior not-run | `63c943992417148d010551238a15259d4968cb55` |
| [`deep-dive`](../skills/deep-dive/SKILL.md) | `research-evaluation` | research, web-search | read-only | verified; behavior not-run | `b518f172abce491d979cf8f8ef854a61605b2790` |
| [`deepseek-pulse`](../skills/deepseek-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `e5778521bac5459432731814755dd2c4d60ff705` |
| [`devlog-draft`](../skills/devlog-draft/SKILL.md) | `communication-writing` | writing, communication, documentation | generate-only | verified; behavior not-run | `073f18ba2c2f7de21015cd072741c395335e9f2e` |
| [`fact-check`](../skills/fact-check/SKILL.md) | `research-evaluation`, `planning-decisions` | research, decision-support, web-search | read-only | verified; behavior not-run | `e58dea59671c8a7c537e27403d6f52e466bf8d86` |
| [`finance-review`](../skills/finance-review/SKILL.md) | `business-product`, `planning-decisions`, `research-evaluation` | business-operations, decision-support, evaluation | read-only | verified; behavior not-run | `86bdf2f9d6ebca2932612212882f6a915709203d` |
| [`gemini-pulse`](../skills/gemini-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `8bf2cc64aaaaa60dd3a15e94464a17d475f9bc80` |
| [`github-pulse`](../skills/github-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `03e135f4e916115040af63271de71b23277e36f7` |
| [`glm-pulse`](../skills/glm-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `3bfbb84c43a76413897b30ad675d1ba5d8b8a1de` |
| [`governance-pulse`](../skills/governance-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation`, `security-governance` | monitoring, research, security | read-only | verified; behavior not-run | `aa2157650140bf0820b6d6b1921c5f0881d8c627` |
| [`handoff-writer`](../skills/handoff-writer/SKILL.md) | `communication-writing` | handoff, documentation, communication | generate-only | verified; behavior not-run | `8a789ea0dd3b1c89ccac9d50727b06007abcf5c1` |
| [`hf-pulse`](../skills/hf-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `de2d55b632e88deaa71aa145cf83293f5877381a` |
| [`inbox-triage`](../skills/inbox-triage/SKILL.md) | `productivity-time`, `communication-writing` | productivity, communication | read-only, generate-only | verified; behavior not-run | `c265af7280a9819ae1fc80292ba24a77c2b28ccd` |
| [`inference-pulse`](../skills/inference-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `bc90e5248c04c408c8c5a44bea62b1d66a7fb143` |
| [`kimi-pulse`](../skills/kimi-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `4d8935ea2d8006ea277ab1371f419c723a867643` |
| [`learning-plan`](../skills/learning-plan/SKILL.md) | `planning-decisions`, `research-evaluation`, `productivity-time` | planning, research, productivity | generate-only | verified; behavior not-run | `a544118bd121b354aec330f9a565a338868dd53e` |
| [`llama-pulse`](../skills/llama-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `d5141bcfebcc4e9ccbba4cbfc9cf57564010b5dc` |
| [`mcp-pulse`](../skills/mcp-pulse/SKILL.md) | `monitoring-intelligence`, `security-governance`, `research-evaluation` | monitoring, security, research | read-only | verified; behavior not-run | `41451ac34a4a660ec82cae2c4356d3afe4b49334` |
| [`mcp-vetting`](../skills/mcp-vetting/SKILL.md) | `security-governance`, `research-evaluation` | security, evaluation | read-only | verified; behavior not-run | `806e79f593446ad15938249898e15230208f2d81` |
| [`memory-pulse`](../skills/memory-pulse/SKILL.md) | `monitoring-intelligence`, `memory-context`, `research-evaluation` | monitoring, memory, research | read-only | verified; behavior not-run | `659441df0952f7db302835606068c812ed81d22f` |
| [`mistral-pulse`](../skills/mistral-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `4d2e092ee1cfdbd7127145926d48d6cf78b46ce1` |
| [`openai-pulse`](../skills/openai-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `d6b98630525e16d392b3f50e67ae674332316310` |
| [`paper-digest`](../skills/paper-digest/SKILL.md) | `research-evaluation` | research, evaluation | read-only | verified; behavior not-run | `b2abf289b265b3d4a8508bda4a35083fa7c35f8a` |
| [`permissions-review`](../skills/permissions-review/SKILL.md) | `security-governance`, `research-evaluation` | security, evaluation | read-only | verified; behavior not-run | `60e1d546e713cfa5b289def082dd73e8b326f029` |
| [`perplexity-pulse`](../skills/perplexity-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `ef8b1cfd50f464f91d02855eaad7d05032475493` |
| [`qwen-pulse`](../skills/qwen-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `e22ff1879ce563a76e733bc576bed80cf4cc5f12` |
| [`repo-doctor`](../skills/repo-doctor/SKILL.md) | `software-engineering`, `research-evaluation` | repository-maintenance, evaluation | read-only | verified; behavior not-run | `8bc7f360be091aac35d61652fe8a34ff7bee3060` |
| [`repo-pulse`](../skills/repo-pulse/SKILL.md) | `monitoring-intelligence`, `software-engineering` | monitoring, repository-maintenance | read-only | verified; behavior not-run | `8d78a04e0993069bc3ecc283c756e420969a88d1` |
| [`smallbiz-ops`](../skills/smallbiz-ops/SKILL.md) | `business-product`, `monitoring-intelligence` | business-operations, monitoring | read-only | verified; behavior not-run | `e33f99d0585d486a6bb3243aae9402bfc2cac0ec` |
| [`standup-writer`](../skills/standup-writer/SKILL.md) | `productivity-time`, `communication-writing` | productivity, communication | generate-only | verified; behavior not-run | `a1cd8678794c90bbaf4f5f2a70d469576ec4b633` |
| [`task-surface`](../skills/task-surface/SKILL.md) | `productivity-time`, `planning-decisions`, `agent-engineering` | productivity, planning, orchestration | mutating, external-side-effect | verified; behavior not-run | `97f1ba0b23f3f70da1e39504a1966a3cebd79398` |
| [`todo-harvester`](../skills/todo-harvester/SKILL.md) | `software-engineering`, `research-evaluation` | repository-maintenance, evaluation | read-only | verified; behavior not-run | `dc14a79da8d1c2835ff2c3d2a1b0f0dd27e029b3` |
| [`week-in-review`](../skills/week-in-review/SKILL.md) | `productivity-time`, `planning-decisions` | productivity, planning | generate-only | verified; behavior not-run | `cd6671df6042d5a864850f6362d0947d61eb7357` |
| [`xai-pulse`](../skills/xai-pulse/SKILL.md) | `monitoring-intelligence`, `research-evaluation` | monitoring, research | read-only | verified; behavior not-run | `ec172826db6d811dbea1985c8962ad342c310412` |
| [`automation-receipts`](../skills/automation-receipts/SKILL.md) | `monitoring-intelligence`, `security-governance` | monitoring, security | read-only | verified; behavior not-run | `1d6c076f2888a0d6c8b2be1552717b96e14a341b` |
| [`session-continuity`](../skills/session-continuity/SKILL.md) | `memory-context`, `communication-writing` | memory, context-management, handoff | mutating | verified; behavior not-run | `93b8f0be84bdb39153386c27b46294233c39bb8b` |

## Qualification and remaining work

**Crosswalk:** 44/44 first-party identities mapped by existing tags; **995/995 third-party identities still require mapping**; **44/1,039** total identities mapped (4.23%). **Security scans newly run: 0. Behavioral evaluations newly run: 0.** Do not conflate `verified` semantic status with scanner clearance or performance.

**Next:** inspect complete packages and corroborate tag-derived categories/subdomains; then crosswalk third-party records at exact source revisions. Record any ambiguous/unclassified packages rather than inventing coverage. Maintain existing authority, license, provenance and safety boundaries. See [capability frontier](CAPABILITY_COVERAGE.md) and [security scanning](security-scanning.md).

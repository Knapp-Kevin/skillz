# First-party provisional domain crosswalk (44/44)

**Evidence:** `registry/local-verification.json` on main `f71371400b38c04f5342b68c54468271562eaae0`. This is a **controlled-tag-derived provisional discovery map**, not semantic review of each skill's full instructions, domain specialization, or behavioral validation. Source identities are canonical skill names; counts are unique within a domain, not additive across domains.

**Coverage:** 44/44 first-party identities provisionally mapped; 0/995 third-party review identities mapped here; **44/1,039** total provisional mapping, **995/1,039** remaining. Every mapping must be reviewed against exact-version skill content before maturity claims. Existing tag-to-domain translations can be overbroad: e.g. `monitoring` is not automatically professional analytics and `evaluation` is not automatically software testing.

| Domain (provisional) | Linked first-party identities |
| --- | ---: |
| Agent / MCP development | 2 |
| Analytics | 21 |
| Business | 2 |
| Career | 1 |
| Communication | 7 |
| Memory / context | 2 |
| Planning | 10 |
| Research | 23 |
| Security | 6 |
| Software engineering | 4 |
| Technical writing | 3 |
| Testing | 8 |
| Time / productivity | 6 |

## Identity-level mapping

| Skill | Controlled use-case tags | Provisional domain associations |
| --- | --- | --- |
| `agent-home-doctor` | `repository-maintenance`, `security` | Software engineering; Security |
| `agent-postmortem` | `evaluation`, `agent-development` | Testing; Agent / MCP development |
| `brief-writer` | `decision-support`, `writing`, `communication` | Planning; Communication |
| `career-radar` | `career`, `research`, `monitoring` | Career; Research; Analytics |
| `claude-pulse` | `monitoring`, `research` | Analytics; Research |
| `compare` | `decision-support`, `research`, `evaluation` | Planning; Research; Testing |
| `daily-briefing` | `productivity`, `planning` | Time / productivity; Planning |
| `decision-log` | `decision-support`, `documentation` | Planning; Technical writing |
| `deck-outline` | `communication`, `writing`, `planning` | Communication; Planning |
| `deep-dive` | `research`, `web-search` | Research |
| `deepseek-pulse` | `monitoring`, `research` | Analytics; Research |
| `devlog-draft` | `writing`, `communication`, `documentation` | Communication; Technical writing |
| `fact-check` | `research`, `decision-support`, `web-search` | Research; Planning |
| `finance-review` | `business-operations`, `decision-support`, `evaluation` | Business; Planning; Testing |
| `gemini-pulse` | `monitoring`, `research` | Analytics; Research |
| `github-pulse` | `monitoring`, `research` | Analytics; Research |
| `glm-pulse` | `monitoring`, `research` | Analytics; Research |
| `governance-pulse` | `monitoring`, `research`, `security` | Analytics; Research; Security |
| `handoff-writer` | `handoff`, `documentation`, `communication` | Communication; Technical writing |
| `hf-pulse` | `monitoring`, `research` | Analytics; Research |
| `inbox-triage` | `productivity`, `communication` | Time / productivity; Communication |
| `inference-pulse` | `monitoring`, `research` | Analytics; Research |
| `kimi-pulse` | `monitoring`, `research` | Analytics; Research |
| `learning-plan` | `planning`, `research`, `productivity` | Planning; Research; Time / productivity |
| `llama-pulse` | `monitoring`, `research` | Analytics; Research |
| `mcp-pulse` | `monitoring`, `security`, `research` | Analytics; Security; Research |
| `mcp-vetting` | `security`, `evaluation` | Security; Testing |
| `memory-pulse` | `monitoring`, `memory`, `research` | Analytics; Memory / context; Research |
| `mistral-pulse` | `monitoring`, `research` | Analytics; Research |
| `openai-pulse` | `monitoring`, `research` | Analytics; Research |
| `paper-digest` | `research`, `evaluation` | Research; Testing |
| `permissions-review` | `security`, `evaluation` | Security; Testing |
| `perplexity-pulse` | `monitoring`, `research` | Analytics; Research |
| `qwen-pulse` | `monitoring`, `research` | Analytics; Research |
| `repo-doctor` | `repository-maintenance`, `evaluation` | Software engineering; Testing |
| `repo-pulse` | `monitoring`, `repository-maintenance` | Analytics; Software engineering |
| `smallbiz-ops` | `business-operations`, `monitoring` | Business; Analytics |
| `standup-writer` | `productivity`, `communication` | Time / productivity; Communication |
| `task-surface` | `productivity`, `planning`, `orchestration` | Time / productivity; Planning; Agent / MCP development |
| `todo-harvester` | `repository-maintenance`, `evaluation` | Software engineering; Testing |
| `week-in-review` | `productivity`, `planning` | Time / productivity; Planning |
| `xai-pulse` | `monitoring`, `research` | Analytics; Research |
| `automation-receipts` | `monitoring`, `security` | Analytics; Security |
| `session-continuity` | `memory`, `context-management`, `handoff` | Memory / context; Communication |

## Critical limits and follow-up

- **Not assessed:** specialist fit, breadth/depth, security freshness, license compatibility, or behavioral effectiveness. The underlying first-party verification record is not promoted to validation by this crosswalk.
- **Potential false positives:** Monitoring → Analytics and Evaluation → Testing are intentionally broad discovery associations and require semantic confirmation. Security → Security is not evidence of advanced cybersecurity practice.
- **Unrepresented in this first-party mapping** means *no matching translated first-party tags*, not no skills in the 995 third-party corpus or external landscape.
- **Next:** reconcile exact-version third-party verification records and map them with evidence; then compare mapped capabilities to the discovery matrix and prioritize actual gaps.


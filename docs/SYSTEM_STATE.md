# System State

## Snapshot Metadata

| Attribute | Value |
|-----------|-------|
| **Last Updated** | 2026-07-04T07:00:00-04:00 |
| **Updated By** | Governor |
| **Phase** | IMPLEMENT (issue #1 cycle, session 7cc26a) |
| **Iteration** | 3 |
| **Session Seal** | Entry #8 chain head 6744f93e (last sealed iteration) |

---

## File Tree (Current Reality)

```
skillz/
|-- .agent/staging/AUDIT_REPORT.md
|-- .qor/gates/<session>/                 (versioned gate artifacts; sessions ca9b2c, 927a53, 7cc26a)
|-- docs/                                 (governance + framework docs)
|-- registry/candidates.yaml              (third-party intake decisions)
|-- scripts/
|   |-- build-index.ts                    (index generator)
|   |-- pulse-run.ts                      (shared pulse collector)
|   `-- lib/frontmatter.ts                (shared parser)
|-- skills/                               (48 first-party skills)
|   |-- 17 pulses: claude/openai/gemini/llama/mistral/xai/deepseek/
|   |   qwen/glm/kimi/perplexity + governance/memory/github/hf/mcp
|   |   + inference-pulse
|   |-- research: deep-dive, compare, fact-check, paper-digest, source-vetting
|   |-- agent-ops: skill-eval, mcp-vetting, agent-postmortem,
|   |   handoff-writer, permissions-review
|   |-- daily-ops: daily-briefing, inbox-triage, standup-writer,
|   |   week-in-review, task-surface
|   |-- repo hygiene: repo-pulse, repo-doctor, todo-harvester
|   |-- comms & life: brief-writer, decision-log, devlog-draft, deck-outline,
|   |   finance-review, smallbiz-ops, career-radar, learning-plan
|   `-- meta: skills-pulse, agent-home-doctor,
|       skill-audit*, skill-sync*, skill-forge*   (*repo-bound)
|-- tests/skill-tools.test.mjs + fixtures/
|-- vendor/                               (6 official submodules, 524 indexed skills)
`-- INDEX.md / index.json                 (generated registry surface)
```

---

## Metrics

| Metric | Value |
|--------|-------|
| Local skills | 48 (45 portable, 3 repo-bound: skill-audit, skill-forge, skill-sync) |
| Scripted skills | 4 (claude-pulse, skills-pulse, skill-audit, skill-sync) |
| Repo tooling scripts | 3 (build-index, pulse-run, lib/frontmatter) |
| Behavior tests | 15 (all passing) |
| Vendored sources | 6 submodules, 524 indexed skills (kwp 185, microsoft 186, aws 93, azure 34, anthropic 17, vercel 9) — freshness: docs/vendor-freshness.md |
| Section 4 violations | 0 (verified at substantiate, Entry #8) |

---

## Health Indicators

| Indicator | Status | Details |
|-----------|--------|---------|
| Merkle Chain | VALID | Genesis-forward recomputed at Entry #8 (2026-07-04); head 6744f93e |
| Blueprint Sync | SYNCED | ARCHITECTURE_PLAN load-bearing rules hold across tree |
| Section 4 Compliance | PASS | Judge-verified at 1.0 substantiate (Entry #8) |
| Test Status | PASS | 15/15 via `node --test "tests/*.test.mjs"` |
| Index Freshness | PASS | Regeneration idempotent; skill-audit exit 0 (48 skills) |

---

## Next Actions

- [ ] Issues #1–#6 governed cycle (session 7cc26a): #1 ✅ state alignment, #2 ✅ CI, #3 ✅ B14 negative rules, #4 ✅ B18 de-specification, #5 ✅ semantic risk audit, #6 ✅ vendor freshness workflow — batch complete
- [ ] B13: `min-model-capability` metadata rollout remainder (first field shipped: handoff-writer, issue #3)
- [ ] B15: Gemini host target for skill-sync (TOML conversion)
- [ ] B17: skill-eval on ponytail (sandbox) before any adoption decision

---

*State snapshot updated by Qor-logic A.E.G.I.S.*
*Run `/qor-status` for live diagnostic.*

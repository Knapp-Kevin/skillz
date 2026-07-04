# Backlog

Open work items, ordered by the ROADMAP build order. IDs are stable; completed items move to Done with the closing reference.

## Open

| ID | Item | Series | Notes |
|----|------|--------|-------|
| B13 | `min-model-capability` metadata rollout across high-judgment skills (B12 remainder — exemplars shipped for handoff-writer + brief-writer; metadata field + more exemplars pending) | meta | Per template §Capability floor rule 7 |
| B15 | Gemini host target for skill-sync (TOML conversion) | meta | Deferred from B08; format conversion, not copy |
| B18 | De-specification sweep per the adaptive-frameworks universal rule: replace hardcoded operator/org specifics (smallbiz-ops business names, career-radar default profile, standup-writer/daily-briefing MythologIQ paths, GG-CORE lines in pulses, governance-pulse local section) with Bind steps; add an audit.ts WARN heuristic (absolute paths / org names in portable skill bodies) | meta | From operator ruling 2026-07-04 (docs/skill-template.md §Adaptive frameworks); task-surface is the reference implementation |
| B17 | skill-eval on ponytail (sandbox): frontier + weak-model arms; check process-authority conflict with Qor-logic before any adoption | agent-ops | MIT SKILL.md-format content, copy path exists but must earn adoption; self-reported benchmarks unverified |

## Done

| ID | Item | Closed by |
|----|------|-----------|
| D01 | skill-audit + skill-sync (Meta series core) | Session 2026-07-03T2023-ca9b2c, seal f1150ab7 |
| D02 | Pulse fleet: 16 pulses on shared engine | commit a046ccf |
| D03 | Research series (5), agent-ops series (5), daily-ops (4), brief-writer, decision-log | 2026-07-03 gap-fill batch |
| D04 (B01) | skill-eval first run on registry candidates | docs/evals/2026-07-03-handoff-writer.md; registry updated 2026-07-04 |
| D05 (B02) | devlog-draft + deck-outline | Session 927a53 (1.0 cycle) |
| D06 (B03/B04) | finance-review, smallbiz-ops, career-radar, learning-plan | Session 927a53 |
| D07 (B05) | inference-pulse (SKILL.md + sources.json) | Session 927a53 |
| D08 (B06) | repo-pulse, repo-doctor, todo-harvester | Session 927a53 |
| D09 (B07) | skill-forge (repo-bound) | Session 927a53 |
| D10 (B08, partial) | skill-sync `--hosts` (.claude/.kilo/.codex copies; Gemini deferred to B15) | Session 927a53, FX11 |
| D11 (B09) | claude-pulse engine migration — REJECTED with reason (LD-2: bespoke undated-changelog cap has no engine equivalent; complecting rejected) | Plan phase2, Judge-verified sound |
| D12 (B10) | Upstream proposal authored | docs/proposals/qor-versioned-gate-artifacts.md |
| D13 (B11) | Weak-model eval executed | docs/evals/2026-07-04-handoff-writer-haiku.md |
| D14 (B12, core) | Gold-standard exemplars for handoff-writer + brief-writer | skills/*/references/examples.md |
| D15 (B10+B16) | Eight enhancement issues filed on MythologIQ-Labs-LLC/Qor-logic (#237–#244): versioned gate artifacts, LF-canonical hashing, living-spec delta-fold (full OpenSpec capability gap analysis), status --json, onboard tutorial, provenance auto-detect, weak-tier negative-rules doctrine, canary/dist_compile hardening | 2026-07-04 |
| D16 (B14) | Negative rules shipped: §Negative rules in handoff-writer + 7 high-judgment skills (brief-writer, decision-log, agent-postmortem, source-vetting, fact-check, deep-dive, compare); template §Capability floor rule 8 + checklist row; `min-model-capability: sonnet` on handoff-writer. Mechanical enforcement lands with issue #5's risk audit; weak-tier behavioral re-eval deferred until then | Issue #3, session 7cc26a |

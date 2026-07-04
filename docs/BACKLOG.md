# Backlog

Open work items, ordered by the ROADMAP build order. IDs are stable; completed items move to Done with the closing reference.

## Open

| ID | Item | Series | Notes |
|----|------|--------|-------|
| B01 | Run `skill-eval` on sandbox registry candidates (`handoff` superseded by first-party handoff-writer; `to-issues`, `rules-distiller`) | agent-ops | First real use of the eval loop |
| B02 | `devlog-draft` + `deck-outline` skills | comms | Per ROADMAP §7 |
| B03 | `finance-review` skill | life-ops | Vendored xlsx does mechanics; read-only |
| B04 | `smallbiz-ops`, `career-radar`, `learning-plan` skills | life-ops | Per ROADMAP §8 |
| B05 | `inference-pulse` sources.json | pulse | llama.cpp / Ollama / vLLM; GG-CORE relevance |
| B06 | `repo-pulse`, `repo-doctor`, `standup` git-plumbing cluster (`gh`-based) | hygiene | repo-pulse + repo-doctor + todo-harvester |
| B07 | `skill-forge` scaffold skill | meta | Template exists; automate instantiation |
| B08 | skill-sync per-host compile variants (`.kilo/`, `.codex/`, `.gemini/`) | meta | Follow Qor-logic dist_compile pattern |
| B09 | Migrate claude-pulse onto the shared pulse engine (sources.json) | pulse | Retire bespoke pulse.ts once parity confirmed |
| B10 | Upstream proposal to Qor-logic: iteration-versioned gate artifacts (one seal, one immutable file) | governance | From Shadow Genome Failure #2 |
| B11 | Re-run handoff-writer eval with weak-model arms (Haiku-tier) to test the capability-equalizer hypothesis | agent-ops | From docs/evals/2026-07-03-handoff-writer.md ceiling-effect verdict |
| B12 | Add `min-model-capability` metadata + `references/examples.md` few-shot exemplars to high-judgment skills (research + agent-ops series) | meta | Weak-model enablement per template §Capability floor |

## Done

| ID | Item | Closed by |
|----|------|-----------|
| D01 | skill-audit + skill-sync (Meta series core) | Session 2026-07-03T2023-ca9b2c, seal f1150ab7 |
| D02 | Pulse fleet: 16 pulses on shared engine | commit a046ccf |
| D03 | Research series (5), agent-ops series (5), daily-ops (4), brief-writer, decision-log | 2026-07-03 gap-fill batch |

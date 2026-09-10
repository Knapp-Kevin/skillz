# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **44** first-party user-facing skills, **44/44** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **550** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **44/44** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

The latest first-party admission is `session-continuity`, created from bounded gap evidence in issues #71/#73. Static review: **19/20 verified**; behavioral validation: `not-run`.

## Admitted-source curation

### Anthropic Skills — CURRENT-STANDARD COMPLETE
- Pin: `9d2f1ae187231d8199c64b5b762e1bdf2244733d`.
- Exact eligible denominator: **17**; companions **17/17**; decisive states **10 verified / 7 rejected unchanged**; gaps **0**.

### Anthropic Knowledge Work Plugins — CURRENT-STANDARD COMPLETE
- Pin: `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8`.
- Exact eligible denominator/current-standard companions: **74/74**; gaps **0**.
- Superseded PR #42 preserves the full package-level provenance and verification trees, resolving the previously reported mapping blocker without inference.
- Historical decisive states remain **36 verified / 38 rejected unchanged**; behavioral-validation states are preserved exactly as recorded.

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE
- Pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Denominator/current-standard companions: **72/72**; gaps **0**.

### Microsoft Skills — CURRENT-STANDARD COMPLETE
- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Exact eligible denominator/current-standard companions: **186/186**; gaps **0**.
- Direct `.NET` **29/29**; Java **26/26**; Python **40/40**; Rust **9/9**; TypeScript **25/25**.

### Microsoft Azure Skills — CURRENT-STANDARD COMPLETE
- Pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Exact eligible denominator/current-standard companions: **34/34**; gaps **0**.

### Cole Medin Skills — CURRENT-STANDARD COMPLETE
- Pin: `fb2e876f057c5356d6603ba0c52d6b4418d893ba`.
- Exact eligible denominator/current-standard companions: **33/33**; gaps **0**.

### David Ondrej Skills — TRACKED / PARTIALLY CURATED
- Pin: `7d0ef87dad1f638cab58995eead9e0e6e3fae237`.
- Exact eligible denominator recomputed directly from the pinned tree: **55** first-class `SKILL.md` packages across five category trees: agent orchestration **17**, ops/setup **11**, research/web **10**, skill authoring **4**, thinking/docs **13**.
- Current provenance/verification companions: **13/55**; gaps **42**.
- Current decisive states: **6 verified / 7 rejected unchanged**; behavioral validation remains `not-run` for all reviewed units.
- **Skill authoring: 4/4 current-standard complete.** `effective-agent-skills` verified 16/20; `folder-specific-claude-and-agents-md` verified 15/20; `push-skill-to-github` verified 15/20; `distribute-skill-to-all-agents` rejected unchanged 11/20 because its deletion-capable `rsync --delete` update path lacks a distinct destructive-action authorization checkpoint.
- **Agent orchestration: 8/17 reviewed.** `fable-safe-prompt`, `agent-self-scheduling`, `bb-plugins`, `cmux`, and `codex-subagent` are rejected unchanged; `bb-subagents`, `corral-launch-agents`, and `fable-review` are verified. `fable-review` is verified 16/20 because it has an explicit user-request trigger, delegates review rather than mutation, looks up provider/model identity instead of guessing, waits for completion, and returns the reviewer output unchanged; behavioral validation is `not-run` and portability is low because bb and companion skills are host-specific.
- Historical issue #47 / PR #50 accounting of **44** skills for this same public pin is superseded by the direct pinned-tree denominator above. Existing package-level evidence is preserved; no state is inferred for the remaining 42.

### Matt Pocock Skills — CURRENT-STANDARD COMPLETE
- Pin: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`.
- Exact eligible denominator/current-standard companions: **29/29** after source-policy exclusions; gaps **0**.

### Cloudflare Skills — CURRENT-STANDARD COMPLETE
- Pin: `f96bff754e428838818017f75817f0f9428acd48`.
- Exact eligible denominator/current-standard companions: **13/13**; decisive states **11 verified / 2 rejected unchanged**; gaps **0**.

### Addy Osmani Agent Skills — CURRENT-STANDARD COMPLETE
- Pin: `f63ec56a3cc936408d792956ae583c3c96a825bd`.
- Exact eligible denominator/current-standard companions: **24/24**; gaps **0**.

### Vercel Agent Skills — CURRENT-STANDARD COMPLETE
- Pin: `f8a72b9603728bb92a217a879b7e62e43ad76c81`.
- Exact eligible denominator/current-standard companions: **9/9**; decisive states **6 verified / 3 rejected unchanged**; gaps **0**.

### OpenHands Extensions — CURRENT-STANDARD COMPLETE
- Pin: `87959a7da3e75445647e77b2fbf5bf5b66fb037b`.
- Exact eligible denominator/current-standard companions: **1/1**; gaps **0**.
- `theme-factory` remains **rejected unchanged 14/20**, behavioral validation `not-run`.

### Google Agents CLI — CURRENT-STANDARD COMPLETE
- Pin: `ef7808f33fc3038112b69d4ad488ce33b72699b1`.
- Exact eligible denominator/current-standard companions: **7/7**; gaps **0**; all seven verified.

### Cline Skills — CURRENT-STANDARD COMPLETE
- Pin: `26378461e978f2b4e2e6d67b57121b86b2a79ba5`.
- Exact published denominator: **36**; provenance/verification companions **36/36**; published gaps **0**.
- The separate internal/unlisted `review-team` record is preserved outside the published denominator.

## Governed discovery / source-vetting

Discovery proceeds in parallel without displacing current-standard source maintenance. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded candidate work surfaced through current issues. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue issue #66 with the David Ondrej frontier now at **13/55 current-standard companion pairs, 42 genuine gaps** at the registered pin. The skill-authoring category is complete at **4/4** and agent orchestration is **8/17** reviewed. For each next unit, check existing companions and repository history first, then perform fresh static review only where exact compatible evidence is genuinely absent. Continue bounded discovery/source-vetting and omission detection in parallel.
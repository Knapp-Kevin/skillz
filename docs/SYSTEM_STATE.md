# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-10 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | 552 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **Anthropic Skills current-standard companions** | 17 / 17 |
| **Anthropic Knowledge Work Plugins current-standard companions** | 74 / 74 |
| **Anthropic Knowledge Work Plugins current-standard gaps** | 0 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Azure Skills current-standard companions** | 34 / 34 |
| **Cole Medin Skills current-standard companions** | 33 / 33 |
| **David Ondrej Skills current-standard companions** | 15 / 55 |
| **David Ondrej Skills current-standard gaps** | 40 |
| **Matt Pocock Skills current-standard companions** | 29 / 29 |
| **Cloudflare Skills current-standard companions** | 13 / 13 |
| **Addy Osmani Agent Skills current-standard companions** | 24 / 24 |
| **Vercel Agent Skills current-standard companions** | 9 / 9 |
| **OpenHands Extensions current-standard companions** | 1 / 1 |
| **Google Agents CLI current-standard companions** | 7 / 7 |
| **Cline Skills published current-standard companions** | 36 / 36 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Microsoft Rust direct-package companions** | 9 / 9 |
| **Microsoft TypeScript direct-package companions** | 25 / 25 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **44/44 provenance-complete**.
- Anthropic Skills: **17/17**, gaps **0**, **10 verified / 7 rejected unchanged**.
- Anthropic Knowledge Work Plugins: exact denominator **74**, **74/74** provenance/verification companion complete, gaps **0**, at pin `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8`; historical states **36 verified / 38 rejected unchanged**.
- AWS Agent Toolkit: **72/72**, gaps **0**.
- Microsoft Skills: **186/186**, gaps **0**.
- Microsoft Azure Skills: **34/34**, gaps **0**.
- Cole Medin Skills: **33/33**, gaps **0**.
- David Ondrej Skills: exact registered-pin denominator **55**, **15/55** provenance/verification companion complete, gaps **40**; current decisive states **8 verified / 7 rejected unchanged**. Skill authoring is **4/4** complete; agent orchestration is **10/17** reviewed.
- Matt Pocock Skills: **29/29**, gaps **0** after source-policy exclusions.
- Cloudflare Skills: **13/13**, gaps **0**, **11 verified / 2 rejected unchanged**.
- Addy Osmani Agent Skills: **24/24**, gaps **0**.
- Vercel Agent Skills: **9/9**, gaps **0**, **6 verified / 3 rejected unchanged**.
- OpenHands Extensions: **1/1**, gaps **0**; `theme-factory` remains **rejected unchanged 14/20**.
- Google Agents CLI: **7/7**, gaps **0**, all seven verified.
- Cline Skills: **36/36 published**, gaps **0**; internal/unlisted `review-team` remains outside the denominator.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## David Ondrej denominator reconciliation

The registered public snapshot is `7d0ef87dad1f638cab58995eead9e0e6e3fae237`. Direct inspection of that exact tree establishes five category folders with **17 + 11 + 10 + 4 + 13 = 55** first-class skill package directories, each represented by its package `SKILL.md`. The older 44-skill denominator recorded during the initial source-admission slice is stale for the same pin.

Current repository evidence contains fifteen exact-version companion pairs. Skill authoring is **4/4** current-standard complete. Agent orchestration is **10/17** reviewed: `fable-safe-prompt`, `agent-self-scheduling`, `bb-plugins`, `cmux`, and `codex-subagent` are rejected unchanged, while `bb-subagents`, `corral-launch-agents`, `fable-review`, `gpt-review`, and `git-worktree` are verified. `git-worktree` is verified 17/20 because both its skill frontmatter and bundled OpenAI policy disable implicit invocation, task work is isolated from the primary checkout, human diff review gates merge, and pushing requires an explicit user request; behavioral validation is `not-run`. Together with `goal-loop`, the family is **15/55**, with **40** gaps and **8 verified / 7 rejected unchanged**.

## Anthropic Knowledge Work Plugins reconciliation

Superseded PR #42 retains complete package-level trees under `registry/skills/anthropic-knowledge-work-plugins/` and `registry/verification/anthropic-knowledge-work-plugins/`, including exact source paths, revisions, fingerprints, individual scores/dispositions, authority findings, and behavioral-validation states. Those 74 provenance and 74 verification companions were recovered intact rather than reconstructed from aggregate counts.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue corpus-wide provenance audit #66. David Ondrej Skills is now **15/55**, with **40** exact-version companion gaps; skill authoring is complete and agent orchestration is **10/17** reviewed.
2. Continue recomputing remaining admitted and tracked families for genuine provenance, fingerprint, exact-pin, or canonical-path gaps.
3. Continue governed discovery/source-vetting and omission recovery.
4. Resolve bounded candidate issues when evidence supports a decisive outcome.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
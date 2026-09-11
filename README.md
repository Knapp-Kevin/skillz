# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-44-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-581-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-20-6f42c1)
![Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A passive skill knowledge resource for AI agents.** `skillz` accumulates reusable skills, procedures, safeguards, anti-patterns, rejected examples, creator methods, standards, pinned source material, provenance, exact-version review evidence, tags, source context, catalog snapshots, and instructions so an external host agent can construct the smallest useful skill set for the user.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the canonical passive procedure.

> **Normal-use boundary:** skills created, adapted, composed, or refined for a user belong in that user's active AI/agent environment or in a portable handoff. They are not written back here unless repository maintenance/curation was explicitly requested.

## What `skillz` is

`skillz` is entirely passive. The external host agent is the active system. The repository owns no runtime, scripts, tests, CI workflows, schedulers, monitors, crawlers, installers, synchronizers, preflight processes, generators, background services, vector databases, autonomous observers, or personalization services.

The repository provides four surfaces:

1. **44 first-party user-facing skills** under [`skills/`](skills/).
2. **12 intact pinned third-party corpora** under [`skills/sources/`](skills/sources/) at exact upstream revisions.
3. **Governed provenance and exact-version evidence** under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).
4. **Passive repository-use and curation procedures** under [`engine/skills/`](engine/skills/), excluded from user-facing inventory.

Third-party packages may contain their own scripts, tests, examples, fixtures, templates, or tools. Those remain upstream package material, not repository-owned execution machinery.

## Core use

The host agent should identify durable user needs, inspect the minimum relevant evidence, compare available first-party and governed third-party material, then evaluate in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Valid outcomes include ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, CHECKLIST, DYNAMIC behavior, or NO CHANGE. The goal is the smallest coherent fitted system, not maximum reuse.

## Corpus and evidence

[`skills/`](skills/) contains **44 active first-party user-facing skills**, all **44/44 provenance-complete**. The 12 pinned corpora are Anthropic Skills, Anthropic Knowledge Work Plugins, Vercel Agent Skills, Microsoft Skills, Microsoft Azure Skills, AWS Agent Toolkit, Matt Pocock Skills, Addy Osmani Agent Skills, OpenHands Extensions, Cline Skills, Cloudflare Skills, and Google Agents CLI. Exact source identity, role, terms, and pins live in [`registry/sources.yaml`](registry/sources.yaml). The registry contains **20 unique source identities**.

There are currently **581 persisted exact-version third-party verification companions**. `verified` means structured static semantic review of an exact version. `validated` additionally requires representative external behavioral/adversarial evidence. `rejected` and `retired` remain useful bounded prior art but are excluded from normal unchanged selection.

## Discovery and admission

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use [`docs/candidate-intake.md`](docs/candidate-intake.md). Discovery scores, popularity, official branding, creator reputation, or catalog recommendations are signals only. Restricted or unclear-license material remains reference-only unless terms justify another role.

## Current curation state

Core passive architecture is complete. Ongoing work is corpus enrichment, historical evidence reconciliation, candidate resolution, and source freshness/omission detection.

- **First-party:** **44/44** provenance-complete.
- **Anthropic Skills:** **17/17** current-standard complete, **0** gaps; **10 verified / 7 rejected unchanged**.
- **Anthropic Knowledge Work Plugins:** **74/74** current-standard complete, **0** gaps; historical decisive states **36 verified / 38 rejected unchanged** at registered pin `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8`.
- **AWS Agent Toolkit:** **72/72** current-standard complete, **0** gaps.
- **Microsoft Skills:** **186/186** current-standard complete, **0** gaps.
- **Microsoft Azure Skills:** **34/34** current-standard complete, **0** gaps.
- **Cole Medin Skills:** **33/33** current-standard complete, **0** gaps.
- **David Ondrej Skills:** exact registered-pin denominator **55**; **44/55** current-standard provenance/verification companion complete, **11** gaps; decisive states so far **17 verified / 27 rejected unchanged**. Skill authoring is **4/4** current-standard complete; agent orchestration is **17/17** complete; ops-and-setup is **11/11** current-standard complete; research-and-web is **10/10** current-standard complete; thinking-and-docs is **2/13** reviewed.
- **Corey Haines Marketing Skills:** admitted as a **tracked corpus** at exact snapshot `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`; exact eligible denominator **50** top-level first-class skill packages; **0/50** individually current-standard reviewed so far. MIT terms are established. Partner integrations, upstream source tooling, generated partner surfaces, and ordinary reference Markdown are outside the skill denominator. Admission does not grant blanket unchanged-reuse eligibility.
- **Matt Pocock Skills:** **29/29** current-standard complete, **0** gaps after source-policy exclusions.
- **Cloudflare Skills:** **13/13** current-standard complete, **0** gaps; **11 verified / 2 rejected unchanged**.
- **Addy Osmani Agent Skills:** **24/24** current-standard complete, **0** gaps.
- **Vercel Agent Skills:** **9/9** current-standard complete, **0** gaps; **6 verified / 3 rejected unchanged**.
- **OpenHands Extensions:** exact registered-pin denominator **1**; **1/1** current-standard companion complete, **0** gaps; `theme-factory` remains **rejected unchanged 14/20**, behavioral validation `not-run`.
- **Google Agents CLI:** exact registered-pin denominator **7**; **7/7** current-standard companion complete, **0** gaps; all **7 verified**.
- **Cline Skills:** exact published denominator **36**; **36/36** current-standard provenance/verification companion complete, **0** published gaps at pin `26378461e978f2b4e2e6d67b57121b86b2a79ba5`. The separate internal/unlisted `review-team` record is preserved outside the published denominator.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

The David Ondrej denominator was recomputed directly from the registered pin `7d0ef87dad1f638cab58995eead9e0e6e3fae237`: five category trees contain 17 + 11 + 10 + 4 + 13 first-class skill packages, for **55 total**. Historical 44-skill accounting for the same pin is superseded by direct pinned-tree evidence. Current review coverage is **44/55**. Skill authoring is complete at **4/4**, agent orchestration is complete at **17/17**, ops-and-setup is complete at **11/11**, research-and-web is **10/10** current-standard complete, and thinking-and-docs is **2/13**.

`browser-harness` is rejected unchanged **14/20** because its bundled install guidance directs automatic software update without asking the user, troubleshooting may escalate to killing all Chrome and daemon processes, and remote Browser Use sessions can incur cost without a distinct authorization boundary. `deep-research` is rejected unchanged **16/20** because a normal run defaults to a paid DeepAPI request capped at $0.70 and larger reports can fan out into multiple independently billable calls without distinct aggregate-spend authorization. `deepapi` is rejected unchanged **14/20** because normal search/research routes can spend money without distinct authorization, open-web search requires 5+ separate paid-capable calls, failure/product-friction feedback can be transmitted externally without separate communication authority, and first daily use automatically launches the installed updater. `fireflies-transcript` is rejected unchanged **15/20** because invalid-key recovery tells the agent to ask the user for a replacement credential and update local credential state without requiring secure external credential entry or distinct authorization for credential-store mutation. `online-shopping` is rejected unchanged **15/20** because ordinary mid-range and expensive shopping research can trigger one or more paid DeepAPI requests without a distinct spend-authorization checkpoint; per-request cost caps and configured credentials are not action authorization. `pi-web-search` is rejected unchanged **15/20** because failure of its nominal zero-config search chain directs the Pi agent to a paid-capable DeepAPI fallback without a distinct spend-authorization checkpoint; configured credentials and a per-request cost cap are not spend authority. `research-prompt` is rejected unchanged **16/20** because its execution section directs a fully contextualized research prompt to the paid-capable DeepAPI deep-research workflow without a distinct spend-authorization checkpoint or separate authorization for transmitting embedded project/context details to that external service. `twitter-alpha` is rejected unchanged **15/20** because ordinary execution mandates numerous paid-capable DeepAPI requests across a seven-person X/LinkedIn cohort without a distinct spend-authorization checkpoint. `who-is-this` is rejected unchanged **15/20** because ordinary execution mandates multiple paid-capable DeepAPI GitHub, LinkedIn, Twitter/X, and deep-research calls and routes person-specific profile/social data through that external service without distinct spend and disclosure authorization. `youtube-transcript` is rejected unchanged **14/20** because the normal DeepAPI path can spend money without distinct spend authorization, the workflow always persists a transcript file even for requests that only ask what a video says, and first yt-dlp failure directs `yt-dlp -U` without distinct software-mutation authorization. All ten retain useful adaptation/extraction evidence; behavioral validation is `not-run`.

`ask-then-build` is rejected unchanged **16/20** because its normal scoping workflow instructs the agent to mutate repository documentation immediately after each user answer, including superseding prior documented decisions, without a distinct repository-mutation authorization checkpoint. Its one-question-at-a-time scoping, option framing, decision capture, and compact implementation-handoff structure remain useful adaptation/extraction evidence. `before-building` is **verified 16/20** as a deliberately small read-only pre-build framing checkpoint; its main limitation is epistemic because it forbids file/tool inspection, so recommendations are preliminary when project-specific facts matter. Behavioral validation is `not-run` for both.

Anthropic Knowledge Work Plugins had been treated as blocked because only its aggregate 74/74 historical result was visible on current `main`. Superseded PR #42 in fact retains the full package-level provenance and verification trees for all 74 plugin skills. Those exact companions are now recovered under canonical registry paths, preserving individual dispositions, fingerprints, authority findings, and behavioral-validation states without inference.

Historically completed external corpora should be reconciled from compatible prior evidence before fresh re-review.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`skills/`](skills/) | First-party user-facing corpus |
| [`skills/sources/`](skills/sources/) | Intact exact-revision external reference corpora |
| [`INDEX.md`](INDEX.md) / [`index.json`](index.json) | Hand-maintained passive catalog snapshots |
| [`CURATION_QUEUE.md`](CURATION_QUEUE.md) | Living curation and source-vetting ledger |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identities, roles, pins, licenses, paths |
| [`registry/skills/`](registry/skills/) | Mandatory per-skill provenance companions |
| [`registry/verification/`](registry/verification/) | Exact-version semantic review evidence |
| [`engine/skills/`](engine/skills/) | Passive repository-use/curation procedures |
| [`docs/GOVERNANCE_INDEX.md`](docs/GOVERNANCE_INDEX.md) | Current governance precedence |
| [`docs/SYSTEM_STATE.md`](docs/SYSTEM_STATE.md) | Current live corpus and architecture snapshot |

## Licensing

First-party content is MIT-licensed. Third-party repositories and materially derived content retain their applicable upstream obligations; the root MIT license does not relicense pinned source corpora. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
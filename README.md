# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-44-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-566-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-19-6f42c1)
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

[`skills/`](skills/) contains **44 active first-party user-facing skills**, all **44/44 provenance-complete**. The 12 pinned corpora are Anthropic Skills, Anthropic Knowledge Work Plugins, Vercel Agent Skills, Microsoft Skills, Microsoft Azure Skills, AWS Agent Toolkit, Matt Pocock Skills, Addy Osmani Agent Skills, OpenHands Extensions, Cline Skills, Cloudflare Skills, and Google Agents CLI. Exact source identity, role, terms, and pins live in [`registry/sources.yaml`](registry/sources.yaml). The registry contains **19 unique source identities**.

There are currently **566 persisted exact-version third-party verification companions**. `verified` means structured static semantic review of an exact version. `validated` additionally requires representative external behavioral/adversarial evidence. `rejected` and `retired` remain useful bounded prior art but are excluded from normal unchanged selection.

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
- **David Ondrej Skills:** exact registered-pin denominator **55**; **29/55** current-standard provenance/verification companion complete, **26** gaps; decisive states so far **14 verified / 15 rejected unchanged**. Skill authoring is **4/4** current-standard complete; agent orchestration is **17/17** complete; ops-and-setup is **8/11** reviewed.
- **Matt Pocock Skills:** **29/29** current-standard complete, **0** gaps after source-policy exclusions.
- **Cloudflare Skills:** **13/13** current-standard complete, **0** gaps; **11 verified / 2 rejected unchanged**.
- **Addy Osmani Agent Skills:** **24/24** current-standard complete, **0** gaps.
- **Vercel Agent Skills:** **9/9** current-standard complete, **0** gaps; **6 verified / 3 rejected unchanged**.
- **OpenHands Extensions:** exact registered-pin denominator **1**; **1/1** current-standard companion complete, **0** gaps; `theme-factory` remains **rejected unchanged 14/20**, behavioral validation `not-run`.
- **Google Agents CLI:** exact registered-pin denominator **7**; **7/7** current-standard companion complete, **0** gaps; all **7 verified**.
- **Cline Skills:** exact published denominator **36**; **36/36** current-standard provenance/verification companion complete, **0** published gaps at pin `26378461e978f2b4e2e6d67b57121b86b2a79ba5`. The separate internal/unlisted `review-team` record is preserved outside the published denominator.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

The David Ondrej denominator was recomputed directly from the registered pin `7d0ef87dad1f638cab58995eead9e0e6e3fae237`: five category trees contain 17 + 11 + 10 + 4 + 13 first-class skill packages, for **55 total**. Historical 44-skill accounting for the same pin is superseded by direct pinned-tree evidence. Current review coverage is **29/55**. Skill authoring is complete at **4/4**, agent orchestration is complete at **17/17**, and ops-and-setup is **8/11** reviewed. In ops-and-setup, `risky-changes` is rejected unchanged 14/20 for missing paid-research/production-read authorization, `global-agent-guardrails` is rejected unchanged 15/20 for missing authorization before persistent security-control configuration, `google-safe-browsing` is rejected unchanged 14/20 because its recovery path directs deploy, DNS, and Search Console actions without action-specific authorization, `anti-sleep` is verified 17/20 because its local LaunchAgent mutation is narrowly tied to an explicit anti-sleep request and verified against the exact process and power assertion, `agentic-productivity-setup` is verified 18/20 because it explicitly separates explanation, project build, and installation, keeps webhook secrets out of conversational context, limits persisted/transmitted data to aggregates, and requires permission before live Discord delivery testing, `create-readonly-db-role` is rejected unchanged 15/20 because it directs generation of a repository SQL artifact that is later expected to contain the role password, creating avoidable credential-bearing file and editor-history exposure despite correctly reserving production DDL application for the human, `github-outside-sandbox` is verified 18/20 because it escalates only an already-authorized blocked Git/GitHub operation, preserves the user's action authority, forbids token copying and broad bypass wrappers, and verifies from the host context, and `macbook-metrics-setup` is rejected unchanged 14/20 because its default persistent LaunchAgent architecture automatically pushes detailed activity telemetry to a private GitHub repository every three hours without a separate sensitive-data transmission authorization boundary while describing the design as local-only/no-cloud. Behavioral validation remains `not-run` for all eight.

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
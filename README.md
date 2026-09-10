# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-44-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-436-8A2BE2)
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

There are currently **436 persisted exact-version third-party verification companions**. `verified` means structured static semantic review of an exact version. `validated` additionally requires representative external behavioral/adversarial evidence. `rejected` and `retired` remain useful bounded prior art but are excluded from normal unchanged selection.

## Discovery and admission

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use [`docs/candidate-intake.md`](docs/candidate-intake.md). Discovery scores, popularity, official branding, creator reputation, or catalog recommendations are signals only. Restricted or unclear-license material remains reference-only unless terms justify another role.

## Current curation state

Core passive architecture is complete. Ongoing work is corpus enrichment, historical evidence reconciliation, candidate resolution, and source freshness/omission detection.

- **First-party:** **44/44** provenance-complete, including `session-continuity`, a substrate-agnostic continuity procedure with authorization-gated durable capture and behavioral validation `not-run`.
- **Anthropic Skills:** exact registered-pin denominator **17**; **17/17** current-standard companion complete, **0** gaps; **10 verified / 7 rejected unchanged**.
- **AWS Agent Toolkit:** **72/72** current-standard companion complete.
- **Microsoft Skills:** exact denominator **186**; **186/186** current-standard companion complete, **0** gaps.
- **Microsoft Azure Skills:** exact registered-pin denominator **34**; **34/34** current-standard companion complete, **0** gaps.
- **Cole Medin Skills:** exact registered-pin denominator **33**; **33/33** current-standard companion complete, **0** gaps.
- **Matt Pocock Skills:** exact registered-pin denominator **29** after excluding `deprecated` and `in-progress`; **29/29** current-standard companion complete, **0** gaps.
- **Cloudflare Skills:** exact registered-pin denominator **13**; **13/13** current-standard companion complete, **0** gaps; **11 verified / 2 rejected unchanged**.
- **Addy Osmani Agent Skills:** exact registered-pin denominator **24**; **24/24** current-standard companion complete, **0** gaps.
- **Vercel Agent Skills:** exact registered-pin denominator **9**; **9/9** current-standard companion complete, **0** gaps; **6 verified / 3 rejected unchanged**. All live companion paths resolve under `skills/sources/vercel-agent-skills/`.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

The Vercel family is pinned at `f8a72b9603728bb92a217a879b7e62e43ad76c81`. Its complete recursive pinned tree exposes exactly **9** first-class `skills/*/SKILL.md` packages, including `vercel-cli-with-tokens`. Canonical provenance and verification shelves expose the same **9/9** identities. The final current-standard defect was stale pre-passive physical-path metadata, now normalized from `vendor/vercel-agent-skills/...` to `skills/sources/vercel-agent-skills/...` across all 18 companion records while preserving exact fingerprints and dispositions. `vercel-cli-with-tokens` remains rejected unchanged for credential-exposure/solicitation and consequential-operation defects; `web-design-guidelines` and `writing-guidelines` remain rejected unchanged because their effective instruction payloads come from mutable unpinned remote `main` documents outside their recorded exact-version fingerprints. Behavioral validation remains `not-run` across all nine.

The Azure denominator is the exact set of independently eligible `SKILL.md` packages at the registered pin: 28 canonical plugin skill roots, one nested `azure-kubernetes-automatic-readiness` package, and five nested Microsoft Foundry packages beyond the Foundry root. Ordinary workflow, procedure, reference, example, and SDK Markdown does not become a separate skill merely because it is useful or lives in an attractively named directory.

Cole Medin is current-standard complete at its exact 33-skill pin. The final reconciled package is `worktree-merge`, rejected unchanged **15/20** with behavioral validation `not-run`; its useful integration/validation mechanics remain adaptation evidence, while consequential branch mutation and repository-controlled executable-guidance assumptions prevent unchanged use.

Matt Pocock Skills is current-standard complete at registered pin `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`. The eligible denominator is **29** first-class packages after the source registry exclusions for `deprecated` and `in-progress`.

Cloudflare Skills is current-standard complete at registered pin `f96bff754e428838818017f75817f0f9428acd48`. Historical dispositions remain **11 verified / 2 rejected unchanged**; `web-perf` remains rejected for its privacy/telemetry boundary and `wrangler` for missing action-specific authorization around consequential mutations.

Anthropic Skills is current-standard complete at registered pin `9d2f1ae187231d8199c64b5b762e1bdf2244733d`, with **17/17** companion pairs and historical distribution **10 verified / 7 rejected unchanged**.

Addy Osmani Agent Skills is current-standard complete at registered pin `f63ec56a3cc936408d792956ae583c3c96a825bd`, with **24/24** current companion pairs. Compatible historical evidence from superseded PR #42 was recovered only where exact fingerprints matched the registered pinned tree; upstream eval fixtures were not treated as behavioral validation.

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

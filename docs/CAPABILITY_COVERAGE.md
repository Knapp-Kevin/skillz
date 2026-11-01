# Capability coverage and evidence frontier (2026-11-01)

> **Status: initial, incomplete crosswalk.** Maintainer evidence artifact for [#588](https://github.com/Knapp-Kevin/skillz/issues/588) and external qualification [#589](https://github.com/Knapp-Kevin/skillz/issues/589). This is a passive document, not a scanner, scheduler, admission decision, or installable skill.

## Source of truth and accounting

Read [AGENTS.md](../AGENTS.md), [AGENT_START_HERE.md](../AGENT_START_HERE.md), [INDEX.md](../INDEX.md), [CURATION_QUEUE.md](../CURATION_QUEUE.md), [registry/sources.yaml](../registry/sources.yaml), [registry/taxonomy.yaml](../registry/taxonomy.yaml), [docs/SYSTEM_STATE.md](SYSTEM_STATE.md), and [security-scanning.md](security-scanning.md) before applying this map. Do not override those canonical records.

At the observed repository baseline: **44 first-party skills**, **995 persisted third-party exact-version reviews** (874 registered/tracked and 121 candidate-only), **1,039 total verification/provenance pairs**, **23 registered sources**, and **12 pinned reference corpora**. These are **review identities**, not proof of unique usable skills or live upstream freshness. **Unique identities exhaustively mapped in this document: 0/1,039.** The family and first-party examples below are source-supported leads, not a completed identity-level crosswalk. This explicit zero avoids silently misrepresenting category examples as verified per-identity mapping.

## Capability ontology: initial broad domains

| Domain | Important subdomains | Existing governed leads | Initial maturity | Qualification gap |
|---|---|---|---|---|
| Software engineering | languages, architecture, refactoring, testing, debugging, code review | Microsoft Skills; Matt Pocock; Addy Osmani; Cline | Partial | Pin freshness, security, live correctness |
| Agent engineering | MCP, tool design, orchestration, evals, memory, authority | Anthropic; AWS; Google; first-party mcp-vetting | Partial | End-to-end behavioral proof |
| Cloud & operations | AWS, Azure, Cloudflare, Vercel, observability, deployment | AWS; Microsoft Azure; Cloudflare; Vercel | Partial | Consequential mutation and secret-access gates |
| Security & governance | threat modeling, privacy, supply chain, prompt injection, compliance | first-party permissions-review; AWS; Microsoft | Partial | Scanner backfill and adversarial runs |
| Research & data | search, literature, analytics, BI, experiments | deep-dive; paper-digest; fact-check; Microsoft | Partial | Specialist scientific rigor |
| Planning & productivity | schedules, tasks, delegation, retrospectives, personal workflows | daily-briefing; task-surface; week-in-review; Matt Pocock | Partial | User outcomes and action authority |
| Marketing & sales | SEO, copy, ads, attribution, funnels, CRM, growth | Corey Haines 50-skill pinned family | Partial | Large pin lag; security and behavioral tests |
| Business & product | strategy, viability, finance, entrepreneurship, customer discovery | smallbiz-ops; finance-review; Corey Haines | Emerging | Professional and financial boundaries |
| UX, interaction & visual design | accessibility, UI, prototyping, design systems, illustration | Vercel; Addy Osmani; OpenAI Figma/Canva candidates | Emerging | Candidate-only licensing and action gates |
| 3D, CAD & animation | modeling, rigging, simulation, materials, manufacturing CAD | OpenAI Game Studio glTF reference candidates | Emerging | No established end-to-end qualified family |
| Games & interactive media | gameplay, mechanics, level design, engines, QA, TTRPG | Jwynia fiction/game; OpenAI Game Studio candidates | Emerging | Runtime/playtest authority and functional proof |
| Fiction & narrative | prose, plot, worldbuilding, continuity, interactive fiction | Jwynia 54 selective reviews; Dan Dewhurst 23 | Partial | Behavioral quality, portability, source freshness |
| Audio & music | composition, synthesis, sound design, voice, mixing | No verified dedicated end-to-end family identified in index | Absent | Source discovery and benchmark tasks |
| Video & film | cinematography, editing, VFX, animation, post-production | OpenAI Adobe candidate references | Emerging | Egress/privacy, licensing, practical workflows |
| Communication & technical writing | documentation, briefs, decks, reports, handoffs | brief-writer; deck-outline; handoff-writer; Anthropic | Partial | Audience-specific behavioral evaluations |
| Education & career | pedagogy, tutoring, curricula, accessibility, job search | learning-plan; career-radar | Emerging | Educational outcomes and age/privacy boundaries |
| Science & engineering | mathematics, laboratory, physics, electronics, robotics, IoT | Microsoft technical references; NVIDIA discovery candidate | Emerging | Domain accuracy, physical-world safety |
| Medicine & health | clinical literature, patient education, medical workflows | No established specialist family in current index | Absent | High-stakes accuracy, privacy and professional review |
| Law & compliance | contracts, regulatory research, privacy policies, audits | governance references only | Emerging | Jurisdiction, legal quality, licensing |
| Accounting & tax | bookkeeping, reporting, taxes, payroll, audit | finance-review | Emerging | Jurisdiction, confidentiality, specialist validation |

**These labels are provisional, conservative assessments of the visible corpus, not final domain scores.** No domain is declared Mature; even apparently broad families lack general behavioral qualification. The controlled `registry/taxonomy.yaml` remains unchanged until the identity crosswalk establishes additive terms.

## Maturity rubric

- **Absent:** no confirmed relevant governed capability.
- **Emerging:** isolated or reference-only examples, missing essential subdomains.
- **Partial:** multiple relevant methods and some governed exact-version reviews, but significant subdomain, authority, security, freshness, or behavioral gaps.
- **Strong:** broad complementary subdomains, maintained exact-version evidence, differentiated methods and representative controlled tests.
- **Mature:** broad and deep coverage, independently reproducible functional and adversarial evidence, current source identity, qualified operational fit and measured reliability.
- Independent flags **STALE**, **BLOCKED** and **UNKNOWN** must accompany, never replace, maturity. A source family can be statically 100% reviewed at its registered pin yet STALE against live upstream.

## Exact-package security and capability gates

Each candidate needs source ID, repository URL, immutable revision, package path and tree fingerprint, license grant, semantic review, source-owned scripts/references/dependencies, authority/privacy review, security report and functional/behavioral evidence. Record **not-run** honestly. Inspect prompt injection, instruction hierarchy escalation, private-data disclosure, arbitrary code, dangerous installers, destructive operations, network egress, MCP permissions, unsafe persistence, licensing and false claims of execution. Never automatically install or execute an untrusted package.

[NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) is already registered as the canonical **external** scanner at `v2.12.0` / `c7958a3268d9498644b22edb75d0f051bbc8cbfc`; routine `--no-llm` scanning is not automatically network-free because dependency coordinates may be sent to OSV.dev. See [security-scanning.md](security-scanning.md). [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) is a **separate experimental external** framework: Tier 1 quality/security, Tier 2 overlap, Tier 3 isolated with-skill vs without-skill evaluation. Its static quality check is not a security scan or behavioral proof; its live Tier 3 requires explicit sandbox and data-egress controls. See [NVIDIA's methodology](https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/) and [documentation](https://docs.nvidia.com/skills/skillevaluator). No new scan or live evaluation was performed for this document.

## Prioritized execution frontier

1. **P0: security backfill** for current first-party and verified third-party packages with executable or consequential authority. Preserve existing semantic/provenance companions. Link to existing scanner backfill issue; no repo-owned runner.
2. **P0: pin-freshness reconciliation** across 23 registered sources: immutable pinned package tree versus live upstream package tree, changed/new/removed skill identities, candidate review status, safety implications. Historical static review is not current-upstream clearance.
3. **P1: full identity crosswalk**: map 44 first-party and 995 third-party review identities to one or more capability IDs; report unique mapped denominator and unclassified remainder; do not double-count multi-category identities.
4. **P1: creative gap discovery**: audio/music, 3D/CAD, game systems, visual art, video, narrative, accessibility. Discovery leads remain reference-only pending package and license review.
5. **P1: professional-specialist gap discovery**: education, science, medicine, law, finance, robotics. Higher-stakes skills require stronger subject-matter acceptance and safety tests.
6. **P2: representative controlled evaluations**: negative-trigger cases, agent baseline versus skill, adversarial prompt-injection tests, privacy/authority tests, reproducibility, measured capability lift and token/time costs. Only externally and with explicit authorization.

## First tranche completion receipt

- Branch: `docs/capability-coverage-evidence-20261101-no-ci`.
- This artifact: capability ontology, conservative family leads, explicit **0/1,039** identity-level crosswalk completion, qualification rules and measured backlog.
- Source pins changed: **0**. Skills copied/admitted: **0**. Security scans executed: **0**. Behavioral runs executed: **0**. Repository-owned automation added: **0**.
- Next tranche: materialize a static, identity-level crosswalk from canonical review records, starting with 44 first-party entries and then 995 third-party review identities; update the denominator and evidence links only for actually inspected identities.

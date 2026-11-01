# Discovery-first source intake: broad domain expansion (2026-11-01)

**Status:** COLLECTED AS PASSIVE REFERENCE POINTERS, NOT ADMITTED. This is the first intake after the owner's explicit decision to prioritize collecting skills before intensive evaluation. Source READMEs were fetched via GitHub connector on 2026-11-01. The hashes below are **README Git blob hashes, not immutable repository revision pins or complete skill-package hashes**. Every package remains unexecuted, unscanned, and ineligible for unchanged reuse until normal governance gates are met.

## Collection strategy

**Collect first** means register candidate sources and locate their skill package directories, while retaining license/authority uncertainty and not installing or executing their instructions. **Incorporation** at this stage is reference-corpus discovery: the user-facing repository can navigate these sources without claiming their instructions are trusted or moving any admitted source pin. No automatic package copying or bulk importing. Once exact source commits and license text are established, intake can be expanded into pinned reference corpora under maintainer authority. The existing 44 first-party and 995 third-party governed review identities remain unchanged.

| Source repository | README blob SHA | Claimed candidate coverage (upstream, not independently enumerated) | Primary collection targets | Collection disposition |
|---|---|---|---|---|
| [CaseMark/skills](https://github.com/CaseMark/skills) | `f320b07230e0700fa8376bdb59d8712ee7ec125c` | 874 legal, 400 medical, 400 finance, 400 capital-markets skills plus case.dev developer workflows | `skills/legal/`, `skills/med/`, `skills/finance/`, `skills/capital/`, `skills/casedev/` | Collected source lead; high-risk specialist domain; confirm each license and authoritative sources |
| [salikkhann/openmedskills](https://github.com/salikkhann/openmedskills) | `a5dbca0fc56fdbaa6e3f1a51c8c2b70fb4c35efa` | 83 governed medical research, healthcare education, and health AI skills | `skills/`, risk class, references, examples, evals | Collected source lead; clinical review and provenance remain mandatory |
| [awslabs/hcls-agent-skills](https://github.com/awslabs/hcls-agent-skills) | `2d06e17a72aaa926faa3006045f848a76ee35b5a` | 42 skills / 13 healthcare and life sciences domains | `skills/`, genomics, clinical operations, FHIR, regulatory, life sciences | Collected source lead; MIT-0 indicated by README, controlling license to verify |
| [sathyavikram/agent-plugins](https://github.com/sathyavikram/agent-plugins) | `f4baf117e718052bc721e60a4fb6124cf799cc07` | FreeCAD project setup, visual QA, threads, fits and tolerances plus common agent skills | `plugins/freecad/skills/` and `plugins/common/skills/` | Collected source lead; parametric CAD fills different gap than Blender mesh modeling |
| [LLMQuant/skills](https://github.com/LLMQuant/skills) | `cbdf7cfbfdc76d02239e48e7a870ddb2a9cbd041` | 18 finance category skills; router folders with supporting workflows/scripts | `skills/llmquant-*/` and referenced workflow trees | Collected source lead; data API, credential scope and market-data license to verify |
| [scenario-labs/skills](https://github.com/scenario-labs/skills) | `4e3a6079cdf9331a0a9a874f9173cc1dd1eca08e` | Cross-media and game-production skill family | Source-owned creative skill paths, README index | Previously collected; preserve media/API cost and rights gates |
| [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) | `79bfe73d9993700244bfc8beeb0598e6bd8f918b` | 28 Blender skill claims | `skills/` | Previously collected; Blender executable and installer boundaries |
| [poorvith-mp/skills-gamedev](https://github.com/poorvith-mp/skills-gamedev) | `0fd25de077018bd175df7cded573dd19369130ce` | 26 game development skill claims | `skills/` | Previously collected; engine/build authority |

**Do not sum the upstream claimed counts into an admitted skill inventory.** Source claims can contain mirrors, wrappers, nested SKILL.md files, non-first-class examples, outdated packages, or duplicates.

## Discovery index and research datasets

- [SkillMD](https://skillmd.com/about): advertises an index of over a million SKILL.md files, with publisher and safety metadata. Treat directory safety badges as third-party claims; use only as a lead generator.
- [SkillsMD](https://skillsmd.dev/): advertises over 91K indexed skills. Its public ranking is a discovery signal, not evidence of safety or usefulness.
- [TheSkillMD](https://www.theskillmd.com/): categorizes skills by industry; potentially valuable for low-coverage domains such as education, manufacturing, healthcare and gaming.
- [GitSkills research dataset](https://arxiv.org/abs/2608.10906): reports 3,797,117 SKILL.md occurrences across 282,200 public GitHub repositories in July 2026, with content-hash deduplication. Use its methodology for distinct-package denominators rather than assuming file occurrences equal distinct skills.

These external indexes are **not** registered skill source families or admissions; search them for original publisher repositories and exact packages. Never install via aggregator by default.

## Priority collection backlog

1. **Breadth:** enumerate original source package paths in the five newly collected source leads and existing three creative leads. Collect license and immutable commit SHA per source; count eligible packages, mirrors, and unique content separately.
2. **Creative:** find independent music composition/notation, sound design, video editing, illustration, and engineering CAD sources not reducible to commercial API routers.
3. **Specialist:** broaden beyond medical/legal/finance into pedagogy, chemistry, physics, manufacturing, electronics, robotics, agriculture and architecture. Distinguish domain skill from an unqualified generic prompt.
4. **Crosswalk:** compare discovered exact package IDs with existing 995 governed third-party reviews to avoid duplicate records and to reuse past decisions.
5. **Evaluation after collection:** fast static triage for obvious malicious or non-redistributable packages before copying, followed by full exact-version security and behavioral review in authorized external hosts. High-stakes skills remain reference-only until cleared.

## Collection receipt

**Eight source-family leads documented in this intake**, including **five newly read source families** and three previously discovered creative families. **Zero exact repository revisions pinned; zero full package trees collected; zero packages admitted; zero scans or behavioral runs.** The intake deliberately improves discovery breadth without pretending that package acquisition and qualification have happened.

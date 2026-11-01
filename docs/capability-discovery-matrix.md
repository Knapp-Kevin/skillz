# Capability discovery matrix: tranche 1

**Status:** Proposed coverage targets, **not** a verified skill-to-capability crosswalk. Companion to [discovery-first charter](discovery-first-capability-ontology.md) and [#588](https://github.com/Knapp-Kevin/skillz/issues/588). Baseline main: `f71371400b38c04f5342b68c54468271562eaae0` (2026-11-01). Existing governed identities: 44 first-party + 995 third-party exact-version review pairs = **1,039**, but **0/1,039 identities are crosswalked by this document**. This is a documentation tranche, not evidence of absence or capability maturity.

## Reading the matrix

Each row is a **domain**, with proposed **subdomain discovery targets**. Each target must later be decomposed into specific capabilities, essential workflows, nontriggers, evidence, and measurable coverage gaps. These are initial leads, not exhaustive definitions. A target may link to multiple domains. Unknown coverage is **unassessed**, not absent. Discovery, static evaluation, and behavioral validation have independent denominators.

| Domain | Initial subdomain discovery targets |
| --- | --- |
| Software engineering | frontend; backend; mobile; desktop; APIs; architecture; refactoring; build tooling; developer experience; maintenance |
| Testing | unit/integration; end-to-end; performance; accessibility; compatibility; fuzz/property testing; regression; test strategy |
| Agent / MCP development | agent architecture; tool design; MCP clients/servers; orchestration; permissions; evaluation; agent observability; multi-agent collaboration |
| Cloud / DevOps | cloud architecture; infrastructure as code; CI/CD; containers; orchestration; deployment; SRE; cost optimization |
| Security | application security; identity/access; threat modeling; vulnerability management; supply chain; incident response; privacy engineering |
| Research | literature review; source discovery; synthesis; systematic review; fact-checking; field methods; reproducibility |
| Planning | strategic planning; project scheduling; resource allocation; roadmapping; decision frameworks; risk planning |
| Marketing | positioning; branding; content; SEO; paid acquisition; growth; lifecycle; attribution; market research |
| Product | discovery; requirements; product strategy; prioritization; experimentation; product analytics; launch; lifecycle |
| UX / UI | user research; interaction design; information architecture; prototyping; accessibility; usability testing; design systems |
| Visual design | graphic design; typography; layout; color; identity systems; information visualization; motion graphics |
| Illustration | concept art; editorial; scientific; character/environment; sequential art; digital/traditional media |
| 3D / CAD / animation | 3D modeling; sculpting; rigging; procedural design; CAD; simulation; rendering; animation; technical drawing |
| Game design | mechanics; level design; systems balancing; narrative design; economy; playtesting; accessibility; tabletop games |
| Fiction / narrative / worldbuilding | plotting; prose; editing; character; dialogue; setting/lore; interactive fiction; continuity |
| Technical writing | API docs; tutorials; reference manuals; architecture records; release notes; documentation IA; localization |
| Music composition | harmony; melody; rhythm; orchestration; arranging; notation; scoring; electronic composition |
| Audio / voice / sound | recording; editing; mixing; mastering; sound design; speech/voice; acoustics; accessibility |
| Video / film | screenwriting; preproduction; cinematography; lighting; editing; color; VFX; captions; delivery |
| Communication | interpersonal; presentations; facilitation; negotiation; conflict resolution; public speaking; organizational communication |
| Analytics | descriptive analytics; dashboards; experimentation; causal inference; forecasting; visualization; measurement |
| Time / productivity | personal planning; task systems; focus; habit formation; scheduling; workload; collaboration |
| Memory / context | retrieval; summarization; long-term memory; provenance; context compression; privacy; forgetting |
| Business | business models; strategy; operations; governance; risk; organizational design; procurement |
| Sales | prospecting; qualification; pipeline; account management; proposals; negotiation; sales operations |
| Career | job search; portfolios; interviews; professional development; networking; compensation; career transitions |
| Education | subject instruction; tutoring; assessment; curriculum; accessibility; classroom management; learning technology |
| Science | experimental design; laboratory methods; physics; chemistry; earth sciences; reproducibility; scientific communication |
| Medicine | clinical information literacy; specialties; diagnostics; therapeutics; patient communication; clinical workflows; evidence appraisal |
| Law | legal research; contracts; litigation support; legislation; regulatory analysis; legal drafting; jurisdictional comparison |
| Finance | financial planning; corporate finance; investments; risk; valuation; budgeting; reporting; financial literacy |
| Robotics / IoT | perception; control; motion planning; embedded integration; sensing; industrial automation; safety |

## Expansion candidates requiring boundary decisions

These are discovery lanes, **not silently adopted new domains**. Record explicit overlaps and whether each merits independent domain status:

| Candidate family | Candidate domains and distinguishing subdomains |
| --- | --- |
| Data and computation | data engineering/databases (pipelines, storage, governance); AI/ML (training, inference, MLOps); mathematics/statistics (proof, optimization, inference); systems engineering (networking, reliability, distributed systems) |
| Physical engineering | electronics/embedded (circuits, firmware, PCB); mechanical/manufacturing (materials, machining, production); architecture/construction (BIM, structures, codes); energy/utilities (grid, renewables, operations) |
| Earth and life | GIS/geospatial (spatial analysis, remote sensing); climate/environment (modeling, conservation); agriculture/food (crops, livestock, food safety); biotechnology/bioinformatics (genomics, computational biology); public health (epidemiology, surveillance) |
| People and society | psychology/behavioral science (cognition, human factors); instructional design (pedagogy, learning science); HR/talent (recruitment, workforce); economics (markets, forecasting); public policy (administration, civic analysis); translation/localization (terminology, multilingual QA) |
| Creative and experiential | photography/imaging (capture, restoration); interactive media/XR (spatial interaction); journalism/publishing (reporting, editorial); performing arts (stage, choreography); hospitality/tourism/events (guest and event operations) |
| Operations and specialist services | supply chain/logistics (procurement, fulfillment); customer support (service operations); information/knowledge management (ontology, archives); legal operations/compliance (controls, contracts); accounting/tax/audit (books, filings); real estate/facilities (property operations); transportation/mobility (aviation, maritime, roads); quality management (standards, audits) |
| Human wellbeing and governance | sports/exercise science (training, biomechanics); personal/household management (practical workflows); accessibility/assistive technology (adaptive systems); entrepreneurship (venture creation); ethics/responsible AI (oversight, accountability); cybersecurity/threat intelligence (forensics, threat research) |

## Priority discovery gaps to investigate, not asserted absent

1. **Creative production:** music theory/orchestration, professional audio, cinematography, CAD/manufacturing, game mechanics and worldbuilding. Source leads must be checked for license, rights, safety, and meaningful capability rather than popularity.
2. **Physical-world engineering:** embedded, robotics, construction, energy, agriculture, transportation. Distinguish documentation-only reference from instructions that could create physical risk.
3. **Human-sensitive disciplines:** clinical, legal, public health, finance, psychology, accessibility. Distinguish general research from regulated professional judgment, data access, and qualified evidence.
4. **Global and multilingual knowledge:** non-English instruction, localization, region-specific law/education, culturally specific creative practice. Never assume English-only sources define the whole landscape.
5. **General software and agent work:** maintain coverage, but compare marginal discovery value against thin disciplines; software-heavy inventory alone cannot establish broad maturity.

## Required next evidence-bearing tranche

- Enumerate canonical 1,039 unique governed identities from `registry/skills/` and `registry/verification/` with exact source pin and per-skill licensing, using an **external** read-only analysis environment.
- Assign one or more *provisional* capability links with citation to source SKILL.md or reviewed receipt. Publish explicit unmapped identities and ambiguous classifications.
- Identify a bounded sample of high-gap discovery sources across at least four distinct non-software domains. Record discovery-only leads and licensing uncertainty without copying or admitting them.
- Report independently: discovered candidates, assessed identities, behaviorally validated identities, mapped identities, and unclassified remainder. The first three must not be conflated.
- Update the five inventory/accounting surfaces only if actual published counts or inventory change.

**No coverage grade is assigned here.** The first tranche's accomplishment is an explicit discovery target matrix and measured **unmapped** remainder, not a claim that the library lacks these skills.

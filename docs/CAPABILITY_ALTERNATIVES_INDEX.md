# Capability alternatives and evidence-grade index

**Status:** discovery-stage index, 2026-11-01. This is a passive human-readable navigation surface, not an installer, ranking algorithm, or security verdict. It complements [the capability ontology](CAPABILITY_COVERAGE.md), [gap closure](CAPABILITY_GAP_CLOSURE.md), and the canonical [catalog](../INDEX.md). Existing governed skills retain their canonical statuses. **Do not treat any discovery candidate as admitted.**

**Rights disclosure is a prerequisite for consumer selection:** [per-skill original license and restriction ledger](discovery/2026-11-01/RIGHTS_INDEX.md) and [direct-use versus inspiration requirements](SKILL_LICENSE_DISCLOSURE.md). Listing a skill here does not relicense it or authorize copying; unresolved per-package rights are visibly held.

## Grading visible in the index

Grades are **evidence-bounded** and must be displayed **per exact skill version**, never inferred from the source publisher, popularity, category, or README claims.

| Dimension | Scale | Evidence needed |
|---|---|---|
| Functional task quality | Q0 untested; Q1 static plausibility; Q2 reproducible controlled task; Q3 multiple diverse tasks and regression; Q4 independently reproduced and maintained | Task rubric, artifacts, baseline, negative cases, reviewer and date |
| Security / authority | S? unknown; S0 unresolved findings; S1 static triage; S2 scanner run with findings adjudicated; S3 controlled adversarial tests plus permissions | Exact-package scanner receipt, authority/egress/dependency review, issue disposition |
| Provenance / licensing | P? unverified; P1 original source located; P2 immutable commit + package tree; P3 controlling license + redistribution and dependency rights checked | Original source, SHA, complete tree, license evidence |
| Portability / dependencies | T? unknown; T1 host-specific; T2 multi-host documented; T3 reproduced on multiple hosts | Host/tool versions, dependency constraints, test receipts |
| Currency | C? unknown; C1 stale/unsupported; C2 source pinned with review date; C3 pin and upstream compatibility recently verified | Dates, source pin and tested environment |

**Do not compute an overall numeric score when Q0 or S? or P? is present.** Display `Not graded`, with all dimension values visible. A strong functional result cannot cancel an unresolved security or licensing issue. Use explicit `Reference only`, `Candidate`, `Admitted`, `Hold`, `Rejected unchanged` statuses.

## Choice and redundancy policy

For every *critical subdomain*, seek **three independent original-source alternatives** when viable: a primary production-oriented candidate, a distinct-method candidate, and a fallback or narrow specialist. Three is a **discovery target**, not a forced admission quota. Preserve additional distinct perspectives when they contribute meaningful methodology or host compatibility. Do not pad with forks, language translations, identical content, or repackaged aliases. Evaluate independently and display differences, not just a winner.

## Expand the universe without prematurely pruning choices

The existing **25 domain families** below are the first navigation layer, not an assertion that every human discipline fits them. The [proposed exhaustive discovery checklist](discovery/2026-11-01/CAPABILITY_UNIVERSE.csv) now enumerates **48 provisional families and 441 explicit subdomains** (the prior 25 plus 23 specialist additions). Each is explicitly `NOT_MAPPED / UNKNOWN / NOT_GRADED` until actual source identities and outcome evidence are linked; this is **not** a count of 441 absent skills.

New specialist lanes include climate and environment, GIS, public policy, veterinary health, industrial manufacturing, electronics, supply chain, heritage/history, inclusive accessibility, energy, transportation, insurance, social services, disaster response, food preparation, libraries and other fields. Domains may overlap; assign skills to multiple justified outcomes rather than forcing false exclusivity. See the [continuous expansion, evaluation and gap-fill loop](CAPABILITY_DISCOVERY_REFINEMENT_LOOP.md) for criteria to discover again or build a new original skill.

## Domain coverage and source alternatives

All sources below are **discovery leads or already-governed families**, not evidence of qualified per-skill coverage. `GAP` means the subdomain-level completeness/quality proof is not established. The table explicitly keeps source options visible while packages are collected.

| Domain | Alternative source families / perspectives | Coverage verdict | Next package collection |
|---|---|---|---|
| Software engineering | Microsoft, Matt Pocock, Addy Osmani, Cline, Anthropic | GAP | Per-language, testing and review alternatives |
| Agent engineering | Anthropic, AWS, Google, OpenHands, first-party MCP review | GAP | Memory, tools, evals, authority alternatives |
| Cloud & operations | AWS, Microsoft, Cloudflare, Vercel | GAP | Provider-specific source packages |
| Security & governance | Microsoft, AWS, first-party governance, NVIDIA scanner reference | GAP | Threat modeling, privacy and secure SDLC |
| Research & data | Kalaris, AWS HCLS, first-party research, Microsoft | GAP | Exact research/statistics/science paths |
| Planning & productivity | First-party planning, Matt Pocock, Ellmos | GAP | Schedule and project alternatives |
| Marketing & sales | Corey Haines, Ellmos, existing first-party review | GAP | SEO, funnel, CRM, attribution |
| Business & product | Corey Haines, CaseMark finance, LLMQuant, first-party business | GAP | Strategy, product discovery, accounting |
| UX & visual design | Figma/Canva reference, Vercel, Addy Osmani, Ellmos | GAP | Accessibility, interaction, illustration |
| 3D, CAD & animation | EL4CTEO Blender, Scenario, glotoff FreeCAD, Gwaihir CAD as Code, sathyavikram FreeCAD | GAP | Modeling, rigging, parametric constraints, manufacture |
| Games & interactive media | poorvith game dev, Scenario, Ellmos game dev, Jwynia | GAP | Engines, level design, testing, TTRPG |
| Music composition | jtydhr88 music composition, SJY051 music composition, Ellmos music composer, Scenario audio | GAP | Notation, arrangement, MIDI and score |
| Audio, voice & SFX | Scenario audio, poorvith game audio, Ellmos music composer | GAP | Recording, restoration, SFX, mastering |
| Film, video & motion | thenguyentrong video production, Scenario video, EL4CTEO Blender video, Ellmos video transcription, Adobe reference | GAP | Editing, VFX, subtitles, output QA |
| Writing & narrative | Jwynia, Dan Dewhurst, Ellmos, first-party writing | GAP | Fiction, script, editorial, localization |
| Education & learning | GarethManning learning science, poorvith education, Ellmos education, Kalaris scientific teaching, OpenMedSkills education | GAP | Curriculum, pedagogy, accessibility, assessment |
| Science & mathematics | Kalaris, AWS HCLS, OpenMedSkills | GAP | Physics, chemistry, mathematics, experimental design |
| Robotics & physical engineering | arpitg1304 robotics, dbwls99706 ROS2, graph-robots manipulation, earthtojake CAD, Gwaihir, glotoff, sathyavikram FreeCAD | GAP | Electronics, control, embedded, robot safety |
| Legal & compliance | CaseMark legal, first-party permissions, Microsoft governance | GAP | Jurisdictional legal review and compliance |
| Healthcare & biomedical | CaseMark med, OpenMedSkills, AWS HCLS, Kalaris | GAP | Clinical governance and specialty evidence |
| Finance & accounting | CaseMark finance/capital, LLMQuant, anthonymankaho HK accounting, kalta actuarial, open-source insurance, first-party finance | GAP | Accounting, audit, markets, tax |
| Architecture & construction | constructelligence-lab construction, sahilyousafp AEC IFC, FreeCAD and CAD source families | GAP | Building codes, structural checks, estimating, IFC/BIM, professional sign-off |
| Agriculture, food & nutrition | farmfriend-labs farming, PangenomeAI academic agri/food, Kalaris research | GAP | Crop/soil systems, farm operations, food science, regional evidence |
| Language & localization | BrunoMiguens product translation, skills-il Hebrew/RTL, lingui internationalization | GAP | Translation quality, contextual culture, Unicode/RTL, language coverage |
| Additional disciplines | Energy industry, aviation, journalism/newsroom, hydrology, culinary, sports analytics, insurance, nonprofit and HR discovery leads; source discovery ongoing | GAP | Public policy, environment/climate, veterinary, manufacturing, historical research and other specialist domains |

**No domain is marked complete solely because three sources are listed.** This matrix intentionally distinguishes *alternative-source discovery* from *qualified, independently useful options*.

## Per-skill display contract (future rows)

Every row in the eventual option index must expose:

`domain | subdomain | skill_name | original_source | exact_commit | skill_path | package_fingerprint | source_relationship(original/fork/mirror) | license | status | Q | S | P | T | C | task_evidence_link | scanner_receipt_link | limitations | perspective_or_differentiator | reviewed_at`.

Rows lacking evidence display `Not graded`, `Unknown`, or `Not run`, never zero-filled implied passes. Sort *admitted and qualified* options by evidenced task fit, not popularity. Keep reference-only alternatives visible but separated from usable recommendations.

## Collection milestone

The current [65-source pinned discovery index](discovery/2026-11-01/INDEX.md), [fourth 19-source expansion](discovery/2026-11-01/DOMAIN_EXPANSION_4.md), and [65-source byte-identity and licensing audit](discovery/2026-11-01/audit/CUMULATIVE_65_SOURCES.md) cover **69 source/category inventories, 4,835 exact SKILL.md paths and 4,807 unique Git entrypoint blobs**. The 28 byte-identical extras do not imply 4,807 independent skill methods. The comprehensive [per-entrypoint rights catalog](discovery/2026-11-01/RIGHTS_INDEX.md) holds a pinned upstream license and use-restriction context for all 4,835, with **none** cleared for unchanged direct reuse without additional package-specific rights/security review.

The [441-subdomain discovery checklist](discovery/2026-11-01/CAPABILITY_UNIVERSE.csv) (48 provisional families) is **not yet individually mapped or fully represented by qualified options**. Broad source collection remains the primary focus, with semantic deduplication and behavioral quality grading deferred until meaningful category coverage is established. Existing governed **44 first-party and 995 third-party version-review identities** remain unchanged; these discovery references grant no admission or license.

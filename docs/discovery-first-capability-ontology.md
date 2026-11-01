# Discovery-first capability ontology: initial charter

**Status:** Proposed, non-exhaustive, passive reference. **Owner direction:** discovery before evaluation before validation. **Tracking:** [#588](https://github.com/Knapp-Kevin/skillz/issues/588).

This charter does not change the canonical first-party browse categories in `registry/categories.yaml`, controlled characterization tags in `registry/taxonomy.yaml`, source admission policy, or existing inventory counts. No skill is newly admitted or qualified by this document.

## Purpose and hierarchy

- **Domain:** a broad discipline or practice. Domain inventory is open-ended; no numerical ceiling.
- **Subdomain:** a distinguishable area of work within or across domains. A subdomain can have multiple domain associations.
- **Capability:** a testable outcome or coherent workflow, with scope, exclusions, necessary use cases, and coverage criteria.
- **Skill:** one canonical source- and exact-version-identified resource, linked to zero, one, or multiple capabilities. A skill's mapping is not a competence claim until supporting evidence exists.

Relationships are **many-to-many**. A generic research skill can be relevant to legal and medical research without being certified to perform legal or medical work. Keep *potential applicability* distinct from *demonstrated specialization*. Do not duplicate skill identities to represent multiple associations. Maintain an explicit unclassified queue and provisional taxonomy terms rather than force-fitting discoveries.

## Discovery-first process

1. **Landscape discovery:** Seek disciplines, languages, cultures, platforms, formats, and source ecosystems missing or thin in the map. Record canonical upstream URL, discovery date, candidate identity, license/terms known or unknown, proposed capability links, and uncertainties. Include unconventional and non-English sources where accessible. Avoid assuming absence from the index means absence on the internet.
2. **Coverage classification:** Add domain/subdomain/capability candidates and link leads across all relevant capabilities. Separate *discovered leads* from *governed exact-version review identities*. Discovery is permissive but does not authorize copying, execution, redistribution, or endorsement.
3. **Gap-led evaluation:** Review high-value leads for missing workflows, meaningful alternatives, or unique perspectives. Keep reference-only and rejected records where legally and operationally appropriate, with reasons.
4. **Risk-appropriate validation:** Security, consent, authority, privacy, provenance, licensing, portability, freshness, and behavioral checks remain distinct gates before reuse or recommendation. No external-host evaluation machinery is installed in this repository.
5. **Coverage reconciliation:** Publish evidence-backed progress and a prioritized gap queue. Preserve unknowns, unassessed candidates, and disagreements rather than laundering them into success.

## Initial domain discovery inventory (not complete)

The 32 minimum domains in #588:

1. Software engineering
2. Testing
3. Agent / MCP development
4. Cloud / DevOps
5. Security
6. Research
7. Planning
8. Marketing
9. Product
10. UX / UI
11. Visual design
12. Illustration
13. 3D / CAD / animation
14. Game design
15. Fiction / narrative / worldbuilding
16. Technical writing
17. Music composition
18. Audio / voice / sound
19. Video / film
20. Communication
21. Analytics
22. Time / productivity
23. Memory / context
24. Business
25. Sales
26. Career
27. Education
28. Science
29. Medicine
30. Law
31. Finance
32. Robotics / IoT

Additional **discovery candidates**, not approved taxonomy entries: cybersecurity and threat intelligence; data engineering and databases; AI/ML; mathematics and statistics; systems engineering and infrastructure; electronics and embedded systems; mechanical/manufacturing engineering; architecture and construction; geospatial/GIS; environmental/climate science; agriculture and food systems; biotechnology/bioinformatics; public health/epidemiology; psychology/behavioral science; instructional design/learning science; HR/talent; operations/supply chain; economics/market intelligence; public policy/government; translation/localization; photography/imaging; interactive media/XR; customer experience/support; information/knowledge management; legal operations/compliance; accounting/tax/audit; real estate/facilities; transportation/mobility; energy/utilities; journalism/publishing; performing arts; hospitality/tourism/events; sports/exercise science; personal/household management; accessibility/assistive technology; quality management/standards; entrepreneurship/venture development; ethics/governance/responsible AI.

Some candidates overlap existing domains. Resolve boundaries with explicit definitions and real discovery evidence; do not drop a capability because its parent domain is disputed.

## Coverage accountability: no inheritance

Each recognized capability must have an independently documented assessment:

| Field | Required meaning |
| --- | --- |
| Identity | Stable capability ID, name, description, boundaries, domain/subdomain associations |
| Essential workflows | Concrete tasks and expected outcomes, including specialized/advanced cases where relevant |
| Discovered landscape | Canonical leads and source diversity, including unknown provenance or license flags |
| Evaluated coverage | Exact-version assessed identities and evidence; no count inflation from cross-links |
| Validated coverage | Separate behavioral evidence and authorization/security qualification |
| Alternatives | Distinct methods, tools, languages, viewpoints where relevant, without arbitrary minimum quotas |
| Gap | Missing workflow, depth, diversity, freshness, quality, or validation, plus next discovery action |
| Status | Absent / Emerging / Partial / Strong / Mature, with independent Stale and Blocked flags |

**No completeness inheritance:** a strong parent domain does not make children complete; a cross-domain link does not automatically fill a capability; a discovered lead does not equal evaluated coverage; an evaluated skill does not equal behaviorally validated capability. Mature requires evidence across applicable breadth, depth, differentiated approaches, current qualified versions, and practical usability. Explicitly mark not-yet-assessed rather than invent scores.

## First bounded execution tranche

- Inventory domain and subdomain candidates for engineering, creative production, productivity, and marketing, plus a separately visible remainder.
- Crosswalk all 44 first-party skills and 995 third-party exact-version review identities **or publish exact mapped and unmapped denominators**. Never imply complete mapping before it is performed.
- Prioritize absent and thin capabilities for new discovery, not just repeatedly reviewing software-oriented sources.
- Publish a passive crosswalk and prioritized gap ledger through a separate reviewed PR. Reconcile source pins and license constraints before admission.
- Keep `README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` synchronized if and only if their published inventory/accounting changes.

**Current evidence boundary:** this charter contains no per-capability maturity decisions, no mapped skill identities, no new source admissions, and no behavioral validation results. Its purpose is to establish the discovery and coverage contract before those evidence-bearing tranches.

# Capability gap closure: acquisition and qualification program

**Status:** active discovery and candidate qualification; no automatic admission. Supports [#588](https://github.com/Knapp-Kevin/skillz/issues/588), [#589](https://github.com/Knapp-Kevin/skillz/issues/589), and [draft #590](https://github.com/Knapp-Kevin/skillz/pull/590). The repo remains passive; external hosts conduct research, scans and evaluations.

## Goal and acceptance standard

The objective is not a complete list of internet skills. It is **practical breadth across major agent capability domains**, with defensible subdomain coverage and evidence of safety and usefulness. A domain is not complete merely because a source repository contains many SKILL.md files. Maintain the denominator of subdomains and qualified, exact-version skills separately.

**Definition of domain coverage:** each critical subdomain has (a) at least one exact-identity, license-compatible, semantically reviewed skill or governed adaptation reference; (b) evidence that its procedure actually supports the claimed task; (c) authority/privacy/dependency boundaries; (d) current upstream freshness and package-security disposition; (e) representative controlled behavioral tests before claiming mature or production-capable. High-risk domains additionally require specialist acceptance and risk-specific tests. An unmet condition is recorded as an explicit gap, not silently treated as covered.

## Acquisition lanes

- **Reuse:** discover and evaluate a concrete existing package; cite immutable source, path, license, all supporting files and exact security/quality receipts.
- **Adapt:** retain bounded ideas from a candidate that fails unchanged reuse. Rewrite safely for the user's host; do not copy restricted material or promote it unchanged.
- **Create:** only where qualified reusable material is insufficient. New first-party skills must be user-useful, distinct, maintainable and governed; no artificial skill-count quotas.
- **Hold/reject:** preserve useful prior art and reasons. No executable package runs or installation without external host authorization and sandbox/egress controls.

## Gap-closing domain matrix (candidate discovery priorities)

The **lead sources below are discovery targets, not admissions, endorsements, licenses, security passes or evidence that particular packages exist**. Exact package URLs and licenses must be confirmed before candidate review.

| Priority | Domain | Required subdomains for initial meaningful coverage | Discovery leads / test tasks |
|---|---|---|---|
| P0 | 3D, CAD, animation | procedural modeling; geometry/materials; rigging; rendering; interchange glTF/USD; CAD constraints; print/manufacture checks | Blender ecosystem, OpenUSD, FreeCAD, Autodesk documentation; produce and inspect a reproducible model, not just prose |
| P0 | Game development & design | mechanics/balance; level design; Unity/Unreal/Godot; shaders; game testing; TTRPG design; accessibility; localization | engine ecosystems, OpenAI Game Studio reference candidates, Jwynia; runnable playtest with negative cases |
| P0 | Music composition | harmony; melody; arrangement; notation; MIDI; synthesis; mixing/mastering; licensing | MuseScore, DAW ecosystems, audio tooling; create inspectable score/MIDI and verify structure |
| P0 | Audio, voice, sound | recording; dialogue; voice synthesis; SFX; restoration; mastering; transcription; loudness/accessibility | audio open-source ecosystems; reproducible signal output and rights/consent checks |
| P0 | Film, video & motion | storyboard; cinematography; editing; compositing/VFX; motion graphics; subtitles; export/QA | Blender, FFmpeg, Adobe reference-only candidates; produce short inspectable timeline and media QA |
| P0 | Visual art & design | illustration; typography; branding; color; image editing; print; accessibility; visual QA | Figma/Canva/Adobe reference-only candidates; source/editable artifact plus visual verification |
| P1 | Education | curriculum; differentiated instruction; assessment; tutoring; accessibility; feedback | education research and open pedagogy; expert-reviewed learner outcomes |
| P1 | Science & mathematics | statistics; computational research; reproducibility; scientific literature; lab protocols; math proofs | scientific computing and domain institutions; verified calculations, reproducible results |
| P1 | Robotics, IoT & physical engineering | sensors; embedded systems; electronics; controls; simulation; mechanical CAD; safety | ROS, Arduino, Zephyr, engineering ecosystems; simulated tests before any physical actuation |
| P1 | Legal & compliance | contracts; privacy; regulation; legal research; policy comparison; evidence | jurisdiction-specific official sources; no legal certainty without review |
| P1 | Healthcare & biomedical | medical literature; clinical education; patient communication; FHIR; privacy | authoritative clinical/standards organizations; clinician-reviewed scenarios, no autonomous clinical action |
| P1 | Finance & accounting | bookkeeping; budgeting; tax; audit; financial modeling; controls | accounting standards and open finance tools; deterministic reconciliations and jurisdiction controls |
| P1 | Marketing & growth | SEO; paid media; content; email; conversion; analytics; sales enablement | Corey Haines, OpenAI marketing candidates; evaluate against measurable tasks |
| P1 | UX & interaction | accessibility; usability; information architecture; design systems; prototyping; multimodal interfaces | Vercel, Addy Osmani, Figma; task-based usability and WCAG checks |
| P1 | Narrative & writing | fiction; worldbuilding; character arcs; editing; interactive stories; scripts; translation | Jwynia, Dan Dewhurst; coherence and continuity benchmarks |
| P2 | Additional disciplines | HR, procurement, logistics, agriculture, architecture, manufacturing, energy, public administration, hospitality, sports, environmental science | add subdomain rows from actual discovery evidence; do not declare exhaustiveness |

## Candidate receipt schema (manual static ledger, one row per exact package)

`domain | subdomain | source_id | immutable_revision | skill_path | package_fingerprint | license | capability_claim | functional_evidence | prompt_injection | exfiltration | destructive_authority | dependency_risk | privacy | semantic_state | security_state | behavioral_state | disposition | reviewer | next_action`.

Use `unknown` rather than inventing evidence. Scanner findings require adjudication; a scan PASS is not proof of absence of malicious behavior. Maintain unchanged-reuse eligibility in [security-scanning.md](security-scanning.md).

## Progress scoreboard (2026-11-01)

- Initial priority domains explicitly enumerated: **16** (not a claim that all possible disciplines have been identified).
- Broad first-party identity classification: **44/44** from existing tags, [crosswalk](CAPABILITY_FIRST_PARTY_CROSSWALK.md).
- Third-party identity classification: **0/995** in this program.
- Newly qualified external skill packages from this program: **0**.
- Newly admitted skill packages from this program: **0**.
- Newly executed package scans and behavioral evaluations: **0**.
- Domain maturity newly demonstrated by this program: **0**.

## Immediate bounded execution tranches

1. Review all 995 existing third-party records into this capability ontology, preserving each existing verdict and exact revision. Prioritize creative categories first, then specialist disciplines; report mapped and ambiguous identities.
2. For each P0 domain, build a finite **named exact-package** candidate shortlist with source path, license, immutable revision, expected task, and specific risk flags. Avoid aggregators that only mirror or rename packages.
3. Assess and retain useful packages under the repo's exact-version security and quality rules. Execute NVIDIA SkillSpector and optional SkillEvaluator **externally**, with authorization and isolation, not in this repo.
4. Create or safely adapt missing capabilities only after comparing existing governed material; add first-party skills via explicit maintainer curation.
5. Refresh the scoreboard after every bounded tranche. Keep unfinished useful engineering work, rejected-reference knowledge and source decisions visible.

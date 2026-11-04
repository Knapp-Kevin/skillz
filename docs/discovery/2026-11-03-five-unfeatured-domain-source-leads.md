# Q9: pinned source leads for five unfeatured capability domains

**Date:** 2026-11-03 · **Routing:** repository curation · **Issues:** #588, #599, #624 · **Baseline main:** `e083c47f13a8ca70ab4c22e6e369dc004837a04b`

## Outcome

Independently inspected **eight entrypoints from seven upstream repositories** in the five areas still without a featured method in draft Q8 #693: **Audio/voice/sound, Business, Career, Science, and Robotics/IoT**. Each lead has an exact upstream commit, verified `SKILL.md` blob, observed package/tree boundary, root license blob and a concrete next-review risk in the [machine-readable handoff](../../registry/discovery/q9-five-domain-source-leads-20261103.json).

**This is discovery, not eight more qualified skills.** No ten-dimension final grades, security scans, behavioral tests, use approvals, source-registry admissions, catalog promotions, or denominator changes occurred. Nothing was executed, installed or copied from upstream into the repository. Q8 draft work is untouched.

## Why these are worth reviewing

| Unfeatured area | Pinned candidate | Specific method worth examining | Main hold |
|---|---|---|---|
| Audio/voice/sound | [Sound Design](https://github.com/salomonMuriel/media-production-skills/blob/6ba42845c9d355776fb10091e47ee32e035509fc/skills/sound-design/SKILL.md) | Measurement-led music/SFX placement, offline cue mixing and loudness checks | 16-file script-bearing package; sound rights and host writes |
| Audio/voice/sound, second approach | [Resemble Detect](https://github.com/resemble-ai/detect-skill/blob/4d31eac1ff9aed33b9a0a192e64f7db57821dc9f/SKILL.md) | Require a finished detector result rather than guessing if audio is synthetic | Cloud API, private media uploads, cost and non-conclusive scores |
| Business | [Strategy Articulation](https://github.com/linuszz/business-strategy-planning-skills/blob/7737792630e2ba1dd98451619fd924486f6ed9fd/bp-business-modeling/skills/strategy-articulation/SKILL.md) | Separate mission, targets, strategy and owners | Risks inventing unprovided targets and deadlines |
| Career | [Evidence Miner](https://github.com/squerne/open-career-skills/blob/f0946bdb369a422b0d1f8f9f591480312d2b07fc/.claude/skills/evidence-miner/SKILL.md) | Cite real commits and PRs before claiming achievements | Private repository reads and GitHub network calls need authority |
| Career, second approach | [ATS Detective](https://github.com/squerne/open-career-skills/blob/f0946bdb369a422b0d1f8f9f591480312d2b07fc/.claude/skills/ats-detective/SKILL.md) | Establish the actual application platform before tailoring CV guidance | Vendor-specific parser claims and probing rules need validation |
| Science | [Literature Survey](https://github.com/a-attia/scicomp-research-skills/blob/17bc2ea305606f74ce73ad01f859d119376848a0/skills/literature-survey/SKILL.md) | Verified bibliography and research collection/correction log | Mixed per-file MIT/Apache terms, scholarly-PDF access rights |
| Robotics/IoT | [ROS 2 Engineering Skills](https://github.com/dbwls99706/ros2-engineering-skills/blob/f0de84dfedd67b067ccc6d2851e681529606930c/SKILL.md) | Non-actuating, evidence-led ROS diagnostics and approval gates | Root includes 204 blobs, runtime tooling and possible actuation |
| Robotics/IoT, second approach | [Robotics Testing](https://github.com/arpitg1304/robotics-agent-skills/blob/f9bc5467ff9ee3d23f1a1b0b29a649843bb6ad11/skills/robotics-testing/SKILL.md) | Deliberate layers from unit to simulation to hardware-in-loop tests | Real hardware safety and unverified code examples |

## Rights and package scope

The pinned GitHub `LICENSE` bodies were inspected, not inferred from repository badges. Root terms: MIT for Sound Design, Strategy Articulation, Open Career and Scientific Computing; Apache-2.0 for Resemble Detect and both robotics sources. **Important exception:** the Scientific Computing repository explicitly identifies `skills/literature-survey/references/literature-search.md` as an **Apache-2.0 derivative of AI-ModCon/genesis-skills**, with its own `literature-search.LICENSE` and provenance in `ATTRIBUTION.md`. Root MIT does **not** relicense that file. The exact pinned secondary-license blob is `f91fb178534ecb505d4575e3b6de732ed1c50d69`. Copyrighted paper PDFs and other external materials are separate again.

The ROS 2 skill is at repository root: 204 observed blobs in the source root, including ancillary tools. That count is **not** an adjudicated owned-package count. The other candidates have explicit entrypoint-subtree boundaries; they still require full-file and reference graph inspection. Two entrypoints belonging to the same publisher are alternatives, not source diversity.

## Review sequence

1. **Identity and overlap first:** crosswalk all eight against the dynamic four-source and governed 1,039-record indexes, aliases/mirrors and Q8 selections. Do not infer novelty from no direct code-search hit. Resolve complete package boundaries, per-file rights and current source revisions.
2. **Fast low-risk qualitative reviews:** Strategy Articulation, ATS Detective and Evidence Miner. Compare with currently reviewed career/business methods, check factual assertions and require explicit scope for private reads.
3. **Deeper package reviews:** Literature Survey's five files and mixed licenses; Sound Design's sixteen files, scripts and audio rights. Treat hosted detection as a separate API/privacy/cost review; never upload a real sample for an unapproved test.
4. **Safety-critical reviews:** robotics testing examples and the large ROS 2 package require source-matched static security scans, staged read-only/non-actuating checks, explicit robot-owner authority and independent human safety review before any hardware run.
5. **Promotion gate:** ten-axis individual evaluation, exact complete package identity, attribution/copy rights, host-action boundaries, security and representative behavioral evidence, comparative differentiated value, then a maintainer-consented featured-shelf decision. Only after promotion should the dashboard and five accounting surfaces change.

This bounded discovery does not close the five-domain coverage gaps. It gives the next qualification worker evidence-backed alternatives instead of another list of unverified search terms.

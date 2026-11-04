# Widened source discovery: five still-unfeatured domains

**Date:** 2026-11-03 · **Route:** `REPOSITORY_MAINTENANCE` · **Tracking:** #588, #599 · Follows [Q8 batch 3](2026-11-03-q8-rights-focused-qualification-batch3.md)

## Why

After three Q8 qualification batches, five capability domains still had no featured method — **Audio, Business, Career, Science, Robotics / IoT** — and their strongest existing reference-only candidates were blocked by defects, a safety hold, or repo-internal coupling. Re-scoring the same packages would not help. So this step **widens the source search**: it looks for genuinely new, original sources outside the 962 repositories already in the discovery ledgers.

## What this is, and is not

This is a **discovery-leads record only.** Nothing here is graded, promoted, qualified, security-scanned, or counted as eligible. It pins exact identities so a future bounded review can start without re-doing the search. License names are read from the first lines of each license file and must be confirmed against full text before any copying.

## How

- GitHub code search (`filename:SKILL.md` plus domain terms) for focused, domain-native sources.
- Excluded repositories already in `registry/discovery`, and obvious **mega-aggregators and mirrors** ("14,855+ skills", "periodically refreshed mirror of …"), which inflate counts without clean first-party authorship.
- Each lead's HEAD commit was pinned with `git ls-remote`, then shallow-fetched to record the representative `SKILL.md` path, its package git-tree SHA, its blob SHA, and the controlling license file.

## The twelve leads

| Domain | Source | Why it's interesting | License (to confirm) |
|---|---|---|---|
| Audio | `glincker/ableton-skills` | Ableton Live production workflows, domain-native | MIT |
| Audio | `koltyj/REW-mcp` | Room EQ Wizard acoustics measurement (a real tool) | MIT |
| Audio | `FuDesign2008/open-music-skills` | Independent music-production skills (21) | MIT |
| Robotics / IoT | `rerun-io/rerun` | rerun.io robotics/CV visualization, URDF | Apache-2.0 / MIT |
| Robotics / IoT | `yaniswav/TopicForge` | Read-only MCP to inspect a running ROS2 robot | MIT |
| Robotics / IoT | `robium-ai/robium` | Physical-AI skills (navigation, ROS2), 29 skills | MIT |
| Science | `tucca-cellag/caail` | Cellular Agriculture AI Library (niche) | MIT |
| Science | `matlab/matlab-agentic-toolkit` | Official MATLAB toolkit (signal, stats, control) | BSD-style (MathWorks) |
| Science | `K-Dense-AI/scientific-agents` | 503 science expert-profile skills | MIT |
| Business | `peterbamuhigire/business-plan-skills` | Unit economics, demand forecasting, pricing (137) | MIT |
| Career | `BRAINS-Certified/BRAINS-resume-skill` | Neurodivergence-aware resume / cover letter | MIT |
| Career | `wexxwuther/job-hunter` | Job search that filters out "ghost jobs" (9) | MIT |

Exact commits, representative package trees and blob SHAs are in the [machine record](../../registry/discovery/widened-source-leads-five-domains-20261103.json).

## Cautions already visible

- **Service/app dependence:** REW needs the Room EQ Wizard app; the MATLAB toolkit needs a licensed MATLAB; the job-hunter skill reaches job boards (check egress and scraping terms).
- **Size vs. quality:** `K-Dense-AI/scientific-agents` (503 skills) and the MATLAB toolkit (156) and business-plan engine (137) are large; expect internal overlap and variable quality, and sample before trusting. Deduplicate before counting.
- **Domain safety:** the cellular-agriculture library and any wet-lab science skills need an authority/safety read, as the medical and dual-use reviews did.
- **Brand claims:** "BRAINS-Certified" is a brand name; check what, if anything, the certification claim asserts.

## Next

A bounded exact-version review of the 1–2 strongest leads per domain: pin a governed revision, read the full packages, confirm license text, run the pinned static scan, and grade against the 10-dimension rubric. Only then could any of these become a Valuable Reference. The HEAD pins here are mutable baselines, not governed pins.

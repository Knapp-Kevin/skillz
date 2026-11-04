# Q8 batch 4: qualifying the 12 widened-discovery source leads — all 33 domains now featured

**Date:** 2026-11-04 · **Route:** explicit `REPOSITORY_MAINTENANCE` · **Tracking:** #588, #599, #624 · Follows [the widened source discovery](2026-11-03-widened-source-discovery-five-domains.md)

## Why

The widened discovery pass pinned 12 new source repositories for the five domains that still had no featured method (Audio, Business, Career, Science, Robotics / IoT), but recorded them as **leads only**. This pass does the bounded exact-version qualification that was promised next.

## How

For each of the 12 sources, one representative, domain-apt `SKILL.md` package was taken (for `rerun-io/rerun`, the robotics-relevant `rerun-urdf` rather than the docs skill):

- exact pinned tree re-derived (**12 of 12 matched**);
- every file read, scripts included (never run);
- a pinned static SkillSpector scan;
- the 10-dimension rubric with written reasons;
- a rights review that extracted every upstream `LICENSE`/`NOTICE`/`plugin.json` on the package path;
- the decisive claims spot-checked against the source lines.

For each previously-empty domain, the **single best-fit, cleanest method was featured**; other strong, distinct methods were kept reference-only (shelf-eligible) to keep the gap-fill lean.

## Results

| Candidate | Domain | Score | copy_allowed | Decision |
|---|---|---:|---|---|
| Ghost-job-aware Job Search (`wexxwuther/job-hunter`) | Career | **19** | YES | **Valuable Reference** |
| Audio Mastering (`FuDesign2008/open-music-skills`) | Audio | **17** | YES | **Valuable Reference** |
| Inspect ROS2 Robot (`yaniswav/TopicForge`) | Robotics / IoT | **19** | YES | **Valuable Reference** |
| CAAIL query (`tucca-cellag/caail`) | Science | **20** | CONDITIONAL | **Valuable Reference** |
| Cross-border Unit Economics (`peterbamuhigire/business-plan-skills`) | Business | **16** | CONDITIONAL | **Valuable Reference** |
| Rerun URDF Ingestion (`rerun-io/rerun`) | Robotics / IoT | 19 | CONDITIONAL | Keep (lean) |
| Nav2 Navigation Debugging (`robium-ai/robium`) | Robotics / IoT | 18 | YES | Keep (lean) |
| Room Acoustics / REW (`koltyj/REW-mcp`) | Audio | 15 | YES | Keep (lean) |
| Mastering Prep / Ableton (`glincker/ableton-skills`) | Audio | 14 | YES | Keep |
| MATLAB Reliability Analysis (`matlab/...`) | Science | 16 | CONDITIONAL | Keep |
| Acoustics Physicist persona (`K-Dense-AI/...`) | Science | 14 | YES | Keep |
| Neurodivergence-aware Resume (`BRAINS-Certified/...`) | Career | 15 | CONDITIONAL | **Held** (see below) |

**5 Valuable References fill the last 5 empty domains.** The shelf grows from **39 methods / 28 domains to 44 / 33 — every canonical domain now has at least one featured method.** Unchanged-use approvals and behavioral validations both stay **0**.

## The five new featured methods

- **Ghost-job-aware Job Search (Career).** Searches four source tiers, then scores each posting on five sub-scores that keep *legitimacy* independent from *fit*, so a perfect-match ghost listing still scores low. Credential-free, stdlib-only, treats fetched pages as untrusted. The host does the web fetching, subject to each site's terms.
- **Audio Mastering (Audio).** For AI-generated tracks, *subtract* (clean mud, cut artifacts) rather than enhance, then two-pass loudness-normalize from measured values to hit the streaming target exactly. Open-source ffmpeg only; never overwrites the source. Limit: a macOS-only playback step and a dangling sibling reference.
- **Inspect ROS2 Robot (Robotics).** A strictly read-only sweep-then-drill over a live ROS2 graph or a bag that names each tool and field, flags mock or truncated data, and treats silence as unknown rather than absence. Needs the external TopicForge MCP and ros2 CLI.
- **CAAIL query (Science).** Query a curated research corpus so a *curated* gap is never reported as a real-world absence: enumerate from small index files, verify row counts against a manifest, and distinguish an un-indexed cell from a genuinely absent subject. Read-only public JSON; the indexed works keep their own licenses.
- **Cross-border Unit Economics (Business).** Tag each input by source and confidence, compute contribution margin after *all* order-variable costs per market and channel, then give a go/conditional/no-go verdict that names the assumptions which would flip it. Limit: it leans on an undefined proprietary "Chwezi Accounting Doctrine" and embeds the author's phone number (strip on reuse).

## One held method

**Neurodivergence-aware Resume (BRAINS)** has a genuinely distinct method — a ten-pattern neurodivergence-bias catalog, a staged disclosure framework, and scanners for resume prompt-injection and AI-tell language. It was **held off the shelf**, not featured, because:

- its Privacy Contract claims **"no outbound network requests,"** which is contradicted by a bundled script that fetches arbitrary `http`/`https`/`file://` URLs;
- the loaded `SKILL.md` says version 1.4.0 while the shipped repo is v2.3.0, so the instructions misdescribe the code;
- full function needs a Python venv + Streamlit + SQLite (not a passive, no-shell use), and "BRAINS Certified Gold" is a self-issued badge, not independent accreditation.

A false privacy claim and a version mismatch are integrity problems a high score does not excuse. Career is filled instead by the cleaner Job Search method.

## Security scan (static, not a clearance)

Of the 5 new Valuable References: 3 passed (Inspect ROS2 Robot, Nav2 is kept, Job Search's scanner findings were all negated test/anti-fabrication phrases), and the rest were incomplete on references outside the package. Across all 44 featured trees: 8 passed / 7 failed / 29 incomplete. Behavioral tests: **not run**.

## Evidence

- [Batch 4 individual records with rights findings](../../registry/discovery/q8-reference-only-qualification-batch4-widened-20261104.json)
- [Current shelf (44 methods / 33 domains)](../../registry/consumer-positive-references-q8-20261103.json)
- [Pipeline ledger](../../registry/qualification-pipeline-20261103.json)

## Next

Every canonical domain now has a featured method, so the frontier shifts from coverage to depth and strength: behavioral/adversarial acceptance tests on the strongest methods (still **NOT RUN** everywhere), promotion of the lean-held shelf-eligible methods where a second method in a domain is warranted, and continued qualification of the 1,522-candidate reference-only queue. The newly discovered sources beyond their one representative package each remain unreviewed.

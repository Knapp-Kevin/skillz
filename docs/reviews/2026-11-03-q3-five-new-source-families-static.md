# Q3: five new source families, 151 exact packages at current standard (2026-11-03)

**Scope:** exact-pinned, 10-dimension static source-vetting candidate decisions. This is not governed review, admission, a security scan, behavioral validation or installation approval, and nothing here authorizes hardware actuation.

This tranche follows [Q1](2026-11-03-q1-four-new-source-families-static.md) and [Q2](2026-11-03-q2-five-new-source-families-static.md) and uses the same brief, rubric, hard gates and integration checks. One change: SKILL.md files are matched **case-insensitively**, because 20 of 21 `audette` packages are named `skill.md`. Q1 and Q2 sources were rechecked and contain no lowercase skill files.

All five sources were found and identity-verified in GitSkills [G1](../discovery/2026-11-03-gitskills-g1-source-diversity.md) and [G2](../discovery/2026-11-03-gitskills-g2-second-wave.md). The pins are unchanged since then, and every review cursor is complete.

## Sources and results

| Source (exact pin) | Domain focus | Packages | REFERENCE-ONLY | REJECT | Threshold signal | Ledger |
|---|---|---:|---:|---:|---:|---|
| `MoMarcode1/austrian-legal-claude` @ `2f411a70b7b897f3d74145ffc57ca191d1a0deaa` | law (Austria) | 35 | 28 | 7 | 2 | [ledger](../../registry/discovery/q3-momarcode1-austrian-legal-claude-static-20261103.json) |
| `LiXin97/agora-lab` @ `9475a97f69021ee39027d39e35d69dbdba093712` | research lab / education | 22 | 13 | 9 | 0 | [ledger](../../registry/discovery/q3-lixin97-agora-lab-static-20261103.json) |
| `soapboxbuild/audette-skills` @ `c495982b98d9dba2e690dea41348e766da857a8e` | building energy / real estate | 21 | 9 | 12 | 1 | [ledger](../../registry/discovery/q3-soapboxbuild-audette-skills-static-20261103.json) |
| `danielrosehill/Claude-Transcription-Plugin` @ `d19d6df5792490b477d9ea6fd4f7eebb0434dc9d` | audio transcription | 29 | 16 | 13 | 6 | [ledger](../../registry/discovery/q3-danielrosehill-claude-transcription-plugin-static-20261103.json) |
| `bensonlee5/openral` @ `de448f8f4eef590ab86625416cb4df969156dc92` | robotics (VLA policies) | 44 | 13 | 31 | 2 | [ledger](../../registry/discovery/q3-bensonlee5-openral-static-20261103.json) |
| **Total** | | **151** | **79** | **72** | **11** | |

**Rights:**
- **Root licences.** `austrian-legal` and `transcription` are MIT. `agora-lab`, `audette` and `openral` are Apache-2.0. `openral` also ships `NOTICE` and `LICENSES/`, which any redistribution must carry.
- **Package-local licences.** No package carries its own licence file.
- **Model weights (`openral`).** Weight-licence lineage is recorded per package: NVIDIA non-commercial, a Physical Intelligence research licence and RLWRLD non-commercial weights. One MIT claim omits the Llama 2 backbone licence.

**Hard fails (48 REJECTs carry at least one):**

| Flag | Packages |
|---|---:|
| `unauthorized-consequential-action` | 22 |
| `self-update-or-remote-code` | 15 |
| `private-data-egress` | 8 |
| `capability-content-mismatch` | 8 |
| `secret-logging` | 1 |
| `credential-in-url` | 1 |
| `misattribution-suspected` | 1 |

The other 24 REJECTs are for low quality or misleading core content, including 4 moved below the 10/20 floor at integration.

**Scores:** 16 ×3, 15 ×9, 14 ×24, 13 ×20, 12 ×16, 11 ×23, 10 ×22, 9 ×9, 8 ×8, 7 ×5, 6 ×3, 5 ×7, 4 ×1, 0 ×1.

**REFERENCE-ONLY by domain:** law 28, robotics/IoT 13, audio/voice 8, research 6, analytics 5, technical writing 5, memory/context 4, science 4, agent/MCP 3, planning 2, communication 1. Routing entries are in the [capability routing file](../../registry/discovery/q3-new-source-families-capability-routing-20261103.json).

## Source-family findings

- **Austrian law.**
  - **Good practice:** every skill carries a "Keine Rechtsberatung" disclaimer, asks for per-citation RIS verification, and only drafts.
  - **Stale or wrong law** is nonetheless common: limitation-period and traffic tables; a German StGB section cited as Austrian; no ban on a harsher penalty after appeal (contrary to the VStG); an invented 2024 gas-boiler duty; pre-2017 spousal inheritance shares; pre-2024 GmbH capital; the repealed EU ODR platform.
  - **Broken installation:** the installer copies shared references to a different directory than the skills expect.
  - **Gaps:** no confidentiality guidance for asylum, health or social data.
- **Agora lab.** These are short role overlays for a multi-agent research lab. Six are one- or two-sentence stubs. There are no external actions. Experiment runs install dependencies and use GPUs without a budget or confirmation step.
- **Audette (building energy).**
  - **Vendor dependency:** everything depends on the vendor's paid MCP services.
  - **Hard fails:** workspace documents are uploaded to an org-wide vendor RAG without asking. Live-account writes, data submission, a recurring scheduled agent job and `CLAUDE.md` edits all happen without confirmation. One skill fabricates a utility bill under a real utility's name.
  - **Compliance skills don't work as described:** stub clients, missing weather and calibration files, only two climate zones, and an automatic "certification" block. One bundles an unattributed Enterprise Green Communities form.
- **Transcription.**
  - **Strengths:** the local Whisper and post-processing skills are coherent (6 threshold signals).
  - **Cloud by default:** audio goes to cloud providers without consent, and one skill tells the agent not to ask. One skill can push audio to a public GitHub repo; others send email or Drive shares, or upload to a paid service.
  - **Remote code and secrets:** an unpinned `npx` MCP server, `curl | sh`, a remote prompt library used verbatim as system prompts, key values printed, and a key placed in a URL query string.
  - **Redaction:** the author's private hostnames are redacted from this evidence.
- **OpenRAL (robotics).** There are 41 generated rSkill discovery views and 3 agent skills.
  - **Missing safety rules:** no package states an e-stop, workspace limits or a sim-first rule for its real-hardware path.
  - **Inconsistent documentation:** READMEs often contradict their manifests.
  - **Thin evaluation:** many results rest on a single episode, and some headline success rates are contradicted by the package's own evals.

## OpenRAL harmonization

The first-pass reviewers applied the remote-code and consequential-action flags three different ways: some flagged weight downloads alone, others flagged only executed code. All 44 records were therefore re-decided by two independent adjudicators under one rule:

- **`unauthorized-consequential-action`:** package content an agent would read gives a ready path to real-hardware actuation without a per-action human go-ahead. That includes real-arm deploys, reasoner- or LLM-driven motion, joint or velocity commands, and public Hugging Face uploads. Safety kernels, environment-variable switches and warnings alone are not a go-ahead. Simulation-only, planning-only and verification-only paths, and weight downloads, are not consequential.
- **`self-update-or-remote-code`:** the documented run path executes unpinned or unverified remote **code**. That covers `trust_remote_code` without a pinned revision, pickle checkpoints, automatic `git clone` plus install, and unpinned `pip` or `curl | sh`. Downloading unpinned safetensors or ONNX weights, and code pinned to an exact SHA, are findings, not flags. Optional manual reproduction installs are findings, not the documented run path; a stricter reading would move one more package (`rtdetr-coco-r18`) to REJECT.
- **Effect:** 22 OpenRAL records changed. The tally moved from 36 REJECT / 8 REFERENCE-ONLY to **31 REJECT / 13 REFERENCE-ONLY**. Every change is listed with evidence in the ledger's `reconciliation_overrides`.

## Cross-corpus identity check (151 records)

| Check | Result |
|---|---|
| Distinct SKILL.md blobs / package trees | 151 / 151 |
| In any other tracked skillz file (governed records, four-source, Q1, Q2, first-party, pinned corpora) | **0 / 0** |
| In G1–G3 package listings from other repositories | **0 / 0** |
| Present in the GitSkills July 2026 snapshot | 114 |
| Exact copies held by another repository in that snapshot | **3** |

The 3 exact copies are duplicate exposures of `recht-sozial`, `recht-compliance` and `recht-sozial-beschwerde`, mirrored inside the aggregator `aibot88/sec_skill_store` (`skills/claudskills/…`). This evidence treats `MoMarcode1/austrian-legal-claude` as the source and the aggregator copies as distribution duplicates. Near-duplicates were not checked.

## Method and controls

- **Review.** 23 parallel read-only reviewers worked on disjoint batches; OpenRAL batches were capped at 6 packages for this moderate- to high-risk material. Two further adjudicators harmonized OpenRAL.
- **Overrides (26).** These cover the OpenRAL harmonization and the floor moves. Each ledger lists them.
- **Redaction and scans.** Personal hostnames were redacted, and every published file was scanned for credentials, private paths and email addresses.
- **Nothing executed.** No package, script or test was run, installed or fetched. Security scans: **0**. Behavioral validations: **0**. GitHub Actions triggered: none.

## Proposed accounting delta for the integration worker (not applied here)

The five shared accounting surfaces, `registry/sources.yaml` and `registry/capability-directory.json` are deliberately not edited.

- **Current-standard exact-path decisions outside the four-source snapshot:** add 151 (79 REFERENCE-ONLY / 72 REJECT). Q1 + Q2 + Q3 together give **391** (244 / 147) across **14** source families with complete exact-pin cursors.
- **Duplicate exposures:** add 3, all in an aggregator.
- **Capability directory:** 79 REFERENCE-ONLY examples are available, including law (17 → 45 with Q1 and Q3), robotics/IoT (8 → 21) and audio (3 → 12 with Q2 and Q3).
- **Unchanged:** governed review records (1,039), the four-source 4,809/4,813, admissions, scans and behavioral validation. The eligible denominator is still unknown.

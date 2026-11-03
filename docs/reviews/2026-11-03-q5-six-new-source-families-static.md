# Q5: six new source families, 150 exact packages at current standard (2026-11-03)

**Scope:** exact-pinned, 10-dimension static source-vetting candidate decisions. This is not governed review, admission, a security scan, behavioral validation or installation approval.

This tranche follows [Q1](2026-11-03-q1-four-new-source-families-static.md), [Q2](2026-11-03-q2-five-new-source-families-static.md), [Q3](2026-11-03-q3-five-new-source-families-static.md) and [Q4](2026-11-03-q4-five-new-source-families-static.md). It uses the same brief, rubric, hard gates, case-insensitive SKILL.md matching and integration checks, plus the rules harmonized in earlier tranches.

The six sources are original-author repositories found and identity-verified in GitSkills [G1](../discovery/2026-11-03-gitskills-g1-source-diversity.md) and [G2](../discovery/2026-11-03-gitskills-g2-second-wave.md). Each was re-cloned at its current HEAD. No other worker had claimed any of them, and nothing else in skillz references these repositories. Every review cursor is complete.

## Sources and results

| Source (exact pin) | Domain focus | Packages | REFERENCE-ONLY | REJECT | DEFER | Threshold signal | Ledger |
|---|---|---:|---:|---:|---:|---:|---|
| `kunitoki/sonic-skills` @ `8b6dcfe89030d7de9ba9d6afcc2d927fb11fe7fa` | audio DSP and plugin-format review | 18 | 17 | 1 | 0 | 7 | [ledger](../../registry/discovery/q5-kunitoki-sonic-skills-static-20261103.json) |
| `arcprime-ip/patent-prompts` @ `41e6a96bdec0b5aa1a4ea11ee489d49061d43114` | US patent drafting and prosecution | 15 | 13 | 2 | 0 | 2 | [ledger](../../registry/discovery/q5-arcprime-ip-patent-prompts-static-20261103.json) |
| `otenycom/talents` @ `5bf3bee6dab56a75c265a313ca5f5068d2373d91` | hosted Telegram-bot persona bundles | 26 | 12 | 14 | 0 | 1 | [ledger](../../registry/discovery/q5-otenycom-talents-static-20261103.json) |
| `City-Syntax/openclaw-ubem` @ `261ad2c508a7b4a5971e0f83238b15d15fa7f651` | multi-agent building-energy modelling | 26 | 6 | 20 | 0 | 0 | [ledger](../../registry/discovery/q5-city-syntax-openclaw-ubem-static-20261103.json) |
| `kavao/monogatari-coach` @ `01d5be3b671a2659dc50179f70c5483572989e71` | Japanese novel and manga workspace | 36 | 28 | 7 | 1 | 7 | [ledger](../../registry/discovery/q5-kavao-monogatari-coach-static-20261103.json) |
| `akiojin/unity-cli` @ `ca07dd8bafaf46326a0de0ffc98024d67adf5555` | Unity Editor CLI and repo maintenance | 29 | 16 | 13 | 0 | 7 | [ledger](../../registry/discovery/q5-akiojin-unity-cli-static-20261103.json) |
| **Total** | | **150** | **92** | **57** | **1** | **24** | |

**Rights:**
- **Root licences:** sonic-skills is Unlicense. talents is Apache-2.0 with a NOTICE saying the hosting platform is proprietary and not covered. The other four are MIT.
- **talents frontmatter:** many talents SKILL.md files claim `license: MIT`, which contradicts the root licence. Both are permissive, so this is recorded as a metadata finding.
- **Package licence files:** none of the 150 packages carries its own licence file.
- **Third-party copies:** these are covered under the hard fails below.

**Hard fails (35 REJECTs carry at least one):**

| Flag | Packages |
|---|---:|
| `unauthorized-consequential-action` | 31 |
| `self-update-or-remote-code` | 10 |
| `capability-content-mismatch` | 3 |
| `misattribution-suspected` | 2 |
| `private-data-egress` | 2 |
| `license-conflict` | 1 |

The other 22 REJECTs carry no flag:
- 18 are low quality or below the 10/20 floor. These include 9 copies of an agent identity file and 3 one-line pointer stubs.
- 4 are monogatari packages rejected under the content-safety and moderation-evasion rules below.

The one DEFER is `kakuyomu-convert`. Its conversion script, `_how_to/tools/kakuyomu_ruby_apply.py`, is not in the pinned tree (checked with `git ls-files`).

**Scores:** 18 ×1, 17 ×3, 16 ×10, 15 ×19, 14 ×20, 13 ×25, 12 ×17, 11 ×16, 10 ×14, 9 ×2, 8 ×16, 7 ×2, 6 ×1, 5 ×1, 4 ×3.

**REFERENCE-ONLY by domain:** software engineering 27 (mostly audio-plugin and Unity editor work), fiction 19, law 13, analytics 6, illustration 5, testing 4, and 18 across 13 other domains. Routing entries are in the [capability routing file](../../registry/discovery/q5-new-source-families-capability-routing-20261103.json).

## Source-family findings and harmonizations

First-pass reviewers again applied flags inconsistently within some families. Four independent adjudicators re-decided **all** records under one written rule per family: 1 for openclaw, 1 for the patent prompts and 2 for monogatari.

In total, integration made 21 changes:
- 19 from the family rules and the 10/20 floor;
- 2 manual: the permit-filing demo and `audio-dsp-review`.

Unity-cli needed no adjudicator. Its auto-install wording was checked by text search across all 29 packages, and every package containing it was already flagged. Every change is listed with evidence in each ledger's `reconciliation_overrides`.

- **sonic-skills.** Careful, read-only audio review and explainer skills.
  - **Accuracy errors:** a VST3 constant that doesn't exist; a JUCE listener-thread claim that its own reference contradicts; a "GOOD" MIDI example that drops events; stale Wwise and FMOD API names; SIMD loops with no remainder handling.
  - **Dependencies:** several review skills require sibling skills that are outside their packages.
  - **`audio-dsp-review`:** it ships an unattributed real-time spin-mutex implementation that closely matches a published third-party design. The upstream page could not be reached from this host, so the flag is `misattribution-suspected` (unverified), not `license-conflict`. It stays REJECT until provenance is confirmed.
- **patent-prompts.** Each SKILL.md is a thin shim that loads a prompt from outside its package (`../../<area>/prompt.md`, present at the pin).
  - **Rule:** directing web searches on the user's unpublished claims or disclosures without asking first is `private-data-egress`. Searches for an accused or competitor product are exempt. This flags `prior-art-analysis`; the adjudicator confirmed all 15 first-pass decisions.
  - **Score findings:**
    - the prompts carry no "not legal advice" caveat;
    - inputs don't match prompt placeholders;
    - legal gaps: 112(f), AIA 102(b)(1), Alice/Mayo, copendency under 35 U.S.C. 120, and the intent element of inducement.
- **otenycom/talents.** The GitSkills heuristic labelled this HR. It is actually a vendor's persona and skill bundles for a hosted Telegram assistant.
  - **Consequential actions (10 packages flagged):**
    - unconfirmed cron jobs that post into DMs and groups;
    - triage-time migrations that delete cron jobs or rename every Odoo login;
    - auto-published public links and websites;
    - billable bot creation;
    - writes to shared cross-session memory;
    - an irreversible permit submission with no owner preview. It targets a demo stub but is flagged on its documented procedure.
  - **Private data:** `crm-bot` sends trade-show visitors' personal data and media out without consent.
  - **Health and finance:** there is no age gate before calorie-deficit coaching; the stock bundle gives personal buy and stop levels despite its own "not advice" boundary; and its 13F parser is about 1000x off.
  - **Platform:** there is heavy lock-in to the vendor platform.
- **openclaw-ubem.** A building-energy pipeline for one university campus. Its 26 paths contain 20 distinct packages.
  - **Rule:** consequential actions are:
    - automatic or mandatory Slack or Signal posts;
    - model-file patches under a fabricated, default or bypassed approval, including auto-approving all buildings when the approval file is missing;
    - shell commands built from chat text;
    - unauthenticated simulation triggers.

    A real human approval that shows the change counts as a gate.
  - **Result:** 8 packages flagged. Interventions are only ever simulated or recommended.
  - **Contradictions:** SKILL.md files repeatedly contradict their code and each other, for example cooling-setpoint rules in opposite directions.
  - **Copied skill:** the generic `slack` skill is an exact copy held by 33 other repositories (see the cross-corpus check).
  - **Portability:** hard-coded personal paths and campus-only data make it low.
- **monogatari-coach.** Mostly careful local workflows: versioned backups, and image generation only after a dry-run and explicit approval.
  - **Content-safety rule:** packages that define or route an NSFW nude tag tier REJECT unchanged if either:
    - they don't require every depicted character to be an adult, or
    - they apply age-obscured, youthful-coded character rules inside that pipeline.

    This rejects 3 packages.
  - **Moderation evasion:** the tag quality gate is REJECT because it tells the agent to reword prompts so they get past downstream content moderation.
  - **Access-control circumvention:** `forge-txt2img` suggests VPN exits or residential proxies to get past a provider's bot protection. That is flagged `unauthorized-consequential-action`, and its reading of `.env` keys into context withdraws its threshold.
  - **Evidence handling:** explicit tags are not reproduced in this evidence.
- **unity-cli.**
  - **Auto-install (8 packages):** the SKILL.md or bundled checklist tells the agent to install the CLI release binary itself, "instead of asking" or "do not ask the user". The installer takes the latest release and checks it only against that release's own checksums. One package pipes an unpinned main-branch script into `sh`. All 8 carry `unauthorized-consequential-action` and `self-update-or-remote-code`.
  - **Repo-maintenance skills:** they commit, push, resolve review threads and post comments without per-action confirmation, and they treat reviewer text as instructions.
  - **`tui-design`:** it adapts the first version of Anthropic's Apache-2.0 `frontend-design` skill (`anthropics/skills` `skills/frontend-design/SKILL.md` @ `ef740771ac901e03fbca3ce4e1c453a96010f30a`) and keeps its characteristic phrasing. It has no licence copy, attribution or change notice. The `license-conflict` flag was checked against that upstream commit.

## Cross-corpus identity check (150 records)

| Check | Result |
|---|---|
| Distinct SKILL.md blobs / package trees | 144 / 144 (9 records in 3 exact in-repo duplicate groups, all in openclaw) |
| In any other tracked skillz file (governed, four-source, Q1–Q4, first-party, pinned corpora) | **0 / 0** |
| In G1–G3 package listings from other repositories | **0 / 0** |
| Present in the GitSkills July 2026 snapshot | 67 |
| Exact copies held by another repository in that snapshot | **3** |

The three copies:
- openclaw `slack` is held by 33 other repositories, which shows it is a widely redistributed skill.
- Two unity-cli GitHub skills are also in the same author's `akiojin/skills`.

## Method and controls

- **Review.** 25 parallel read-only reviewers worked on disjoint batches. Files over 60 KB were characterised by section rather than read line by line, and each affected record's coverage says so.
- **Harmonization.** 4 adjudicators re-decided the openclaw, patent and monogatari families as described above.
- **Licence checks.** One licence claim was checked against its upstream source.
- **Scans.** Every published file was scanned for credentials, private paths, email addresses and phone numbers. None were found. Client project names were replaced with a generic description.
- **Nothing executed.** No package, script or test was run, installed or fetched. Security scans: **0**. Behavioral validations: **0**. GitHub Actions triggered: none.

## Proposed accounting delta for the integration worker (not applied here)

The five shared accounting surfaces, `registry/sources.yaml` and `registry/capability-directory.json` are deliberately not edited.

- **Current-standard exact-path decisions outside the four-source snapshot:** add 150 (92 REFERENCE-ONLY / 57 REJECT / 1 DEFER). Q1–Q5 together give **700** (404 / 295 / 1) across **25** source families, all with complete exact-pin cursors.
- **Exact duplicate exposures:** record 9 in-repo duplicate records in openclaw and 3 cross-repository copies.
- **Capability directory:** 92 REFERENCE-ONLY examples are available, notably audio-plugin and real-time DSP review (+17), Unity editor workflows (+16), patent drafting under law (+13) and Japanese fiction production (+19).
- **Unchanged:** governed review records (1,039), the four-source 4,809/4,813, admissions, scans and behavioral validation. The eligible denominator is still unknown.

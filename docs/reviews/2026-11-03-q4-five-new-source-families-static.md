# Q4: five new source families, 159 exact packages at current standard (2026-11-03)

**Scope:** exact-pinned, 10-dimension static source-vetting candidate decisions. This is not governed review, admission, a security scan, behavioral validation or installation approval.

This tranche follows [Q1](2026-11-03-q1-four-new-source-families-static.md), [Q2](2026-11-03-q2-five-new-source-families-static.md) and [Q3](2026-11-03-q3-five-new-source-families-static.md). It uses the same brief, rubric, hard gates, case-insensitive SKILL.md matching and integration checks.

The five sources are original-author repositories found and identity-verified in GitSkills [G1](../discovery/2026-11-03-gitskills-g1-source-diversity.md) and [G2](../discovery/2026-11-03-gitskills-g2-second-wave.md). The pins are unchanged since verification. No other worker had claimed any of them, and nothing else in skillz references these repositories. Every review cursor is complete.

## Sources and results

| Source (exact pin) | Domain focus | Packages | REFERENCE-ONLY | REJECT | Threshold signal | Ledger |
|---|---|---:|---:|---:|---:|---|
| `scitix/siclaw` @ `ceee3f49f8bdc9223c0a2b0afec33253f95616f9` | Kubernetes / SRE diagnostics | 28 | 22 | 6 | 4 | [ledger](../../registry/discovery/q4-scitix-siclaw-static-20261103.json) |
| `dcc-mcp/dcc-mcp-blender` @ `8d8027fe4377b4d399d545869fc11b80e04ff785` | 3D / Blender via MCP | 42 | 20 | 22 | 10 | [ledger](../../registry/discovery/q4-dcc-mcp-dcc-mcp-blender-static-20261103.json) |
| `philipjoubert/dojo-public` @ `3e7dab373ae8b84c42a175b8fc3677a0f391b5b6` | real-person advisor personas | 43 | 0 | 43 | 0 | [ledger](../../registry/discovery/q4-philipjoubert-dojo-public-static-20261103.json) |
| `ImDanielGitHub/novel-craft` @ `0d36292be1f33225eba5b50c0cfe46de5a03a4ad` | fiction manuscript CLI | 26 | 6 | 20 | 1 | [ledger](../../registry/discovery/q4-imdanielgithub-novel-craft-static-20261103.json) |
| `peterod99/consultant-skills` @ `ee82a9dfe327a734e815a590aaaf92327d111d85` | consulting / sales | 20 | 20 | 0 | 9 | [ledger](../../registry/discovery/q4-peterod99-consultant-skills-static-20261103.json) |
| **Total** | | **159** | **68** | **91** | **24** | |

**Rights:** `siclaw` has an Apache-2.0 root licence with no NOTICE file. The other four are MIT. No package carries its own licence file. The dojo excerpt rights are covered below.

**Hard fails (63 REJECTs carry at least one):**

| Flag | Packages |
|---|---:|
| `license-conflict` | 39 |
| `misattribution-suspected` | 34 |
| `unauthorized-consequential-action` | 20 |
| `self-update-or-remote-code` | 1 |
| `capability-content-mismatch` | 1 |

The other 28 REJECTs are for low quality. They include novel-craft's deprecated one-line aliases, each annotated as an alias of an existing target, and the packages below the 10/20 floor.

**Scores:** 18 ×1, 17 ×8, 16 ×7, 15 ×13, 14 ×32, 13 ×18, 12 ×19, 11 ×21, 10 ×6, 9 ×12, 8 ×5, 7 ×1, 6 ×11, 5 ×5.

**REFERENCE-ONLY by domain:** cloud/devops 21, 3D/CAD/animation 19, sales 12, fiction 5, business 4, marketing 4, and 1 each in agent/MCP, audio and technical writing. Routing entries are in the [capability routing file](../../registry/discovery/q4-new-source-families-capability-routing-20261103.json).

## Source-family findings and harmonizations

First-pass reviewers again applied some flags inconsistently within a family. Independent adjudicators re-decided **all** records in three families under one written rule each: 1 adjudicator for siclaw, 2 for Blender and 2 for dojo. That changed 45 records in total, including floor moves and alias annotations. Every change is listed with evidence in the ledgers' `reconciliation_overrides`.

- **siclaw (cluster diagnostics).** The GitSkills heuristic labelled this source medicine; its true domain is cloud-devops. Most of its skills are careful, read-only diagnostics.
  - **Rule:** the siclaw `node_script` and `host_script` tools start privileged debug pods with hostPID/hostNetwork and nsenter, and the source sets no approval flag for them. Directing the agent to use them, or to take any mutating cluster action (for example scheduling a test pod), without per-action confirmation is `unauthorized-consequential-action`. Read-only exec inside existing pods scores authority 1.
  - **Result:** 5 packages flagged. The rest of the defects are accuracy errors and script bugs.
- **Blender via MCP.** The agent drives a live Blender session.
  - **Consequential actions** are:
    - default-on arbitrary Python execution;
    - on-disk overwrite or delete without a guard (saving over the open `.blend`, exporting over existing files, saving baked images over source textures, deleting bake caches or add-on files);
    - a persistent autostart install that exposes `execute_python`;
    - add-on installs where "authorized" is defined only in an unpinned external document;
    - submitting or deleting shared render-farm jobs;
    - opening network listeners.
  - **Remote code:** unpinned runtime `pip` installs count as remote code.
  - **Not a flag:** undoable edits inside the open scene score authority 1.
  - **Contributing issue:** several `tools.yaml` files mark overwrite and code-execution tools `destructive: false`, which would suppress a host's confirmation prompt.
- **dojo (43 real-person personas).** All 43 are REJECT.
  - **Impersonation:** one shared template has the agent answer in the voice of a named, mostly living person, with no simulation or non-endorsement disclaimer.
  - **`license-conflict` (39):** the persona files ship long verbatim excerpts from copyrighted books, essays, newsletters and transcripts. The repository's own LICENSE and README say MIT grants no rights to them. Public-domain sources and "distilled" non-verbatim samples are not flagged.
  - **`misattribution-suspected` (34):** text presented as the person's own words is invented, stitched or compiled, or cites works that don't exist, or invented first-person anecdotes appear in a living person's name.
  - **How the source material was gathered:** one corpus manifest lists books taken from a known pirated-ebook site; another was fetched by bypassing a bot block with a "stealth" proxy; several record whole-book ingestion.
  - **Evidence handling:** quotations in this evidence are limited to a few words.
- **novel-craft.** `cli/SKILL.md` (16/20) is a careful local manuscript tool: generated text stays a proposal until committed, story facts must cite quoted evidence, and exports never overwrite. Its `novel-craft-*` skills call commands from the legacy Rust 0.1.x CLI, while the README installs the npm 0.2.0 CLI, which rejects them. There are 12 one-line deprecated aliases.
- **consultant-skills.** Advice-only, paraphrased from paid courses; no verbatim copying was observed, but attributions can't be verified.
  - **Outbound compliance:** the outbound playbooks never mention opt-outs, CAN-SPAM or GDPR.
  - **Client consent:** client consent for case studies is not a required step.
  - **Accuracy:** worked examples contain arithmetic contradictions, and LinkedIn limits are misstated.

## Cross-corpus identity check (159 records)

| Check | Result |
|---|---|
| Distinct SKILL.md blobs / package trees | 159 / 159 |
| In any other tracked skillz file (governed, four-source, Q1–Q3, first-party, pinned corpora) | **0 / 0** |
| In G1–G3 package listings from other repositories | **0 / 0** |
| Present in the GitSkills July 2026 snapshot | 105 |
| Exact copies held by another repository in that snapshot | **0** |

## Method and controls

- **Review.** 26 parallel read-only reviewers worked on disjoint batches. Persona batches were capped at 4 packages, and each persona's large topic corpus was sampled; coverage says so per record.
- **Harmonization.** 5 adjudicators re-decided the siclaw, Blender and dojo families as described above.
- **Scans.** Every published file was scanned for credentials, private paths and email addresses, and for quoted passages over 220 characters. None were found.
- **Nothing executed.** No package, script or test was run, installed or fetched. Security scans: **0**. Behavioral validations: **0**. GitHub Actions triggered: none.

## Proposed accounting delta for the integration worker (not applied here)

The five shared accounting surfaces, `registry/sources.yaml` and `registry/capability-directory.json` are deliberately not edited.

- **Current-standard exact-path decisions outside the four-source snapshot:** add 159 (68 REFERENCE-ONLY / 91 REJECT). Q1–Q4 together give **550** (312 / 238) across **19** source families with complete exact-pin cursors.
- **Alias exposures:** 12 novel-craft deprecated aliases are recorded.
- **Capability directory:** 68 REFERENCE-ONLY examples are available, notably cloud/devops SRE diagnostics (+21) and 3D/CAD/animation (7 → 26).
- **Unchanged:** governed review records (1,039), the four-source 4,809/4,813, admissions, scans and behavioral validation. The eligible denominator is still unknown.

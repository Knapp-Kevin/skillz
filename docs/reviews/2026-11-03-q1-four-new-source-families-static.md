# Q1: four new source families, 113 exact packages at current standard (2026-11-03)

**Scope:** exact-pinned, 10-dimension static source-vetting candidate decisions. This is not governed review, admission, a security scan, behavioral validation or installation approval.

The four sources are original-author repositories first found and identity-verified in the GitSkills discovery tranches [G1](../discovery/2026-11-03-gitskills-g1-source-diversity.md) and [G2](../discovery/2026-11-03-gitskills-g2-second-wave.md). They were chosen because they are permissively licensed, single-author and in underserved domains, and no other worker or PR had claimed them. None is a registered source. Every package at each pin was reviewed, so each family's review cursor is complete.

## Sources and results

| Source (exact pin) | Domain focus | Packages | REFERENCE-ONLY | REJECT | Threshold signal | Ledger |
|---|---|---:|---:|---:|---:|---|
| `judicialmind/legal-skills` @ `916ec5a4328a893cc57b4e0ecb9958b761901ca1` | law | 30 | 12 | 18 | 0 | [ledger](../../registry/discovery/q1-judicialmind-legal-skills-static-20261103.json) |
| `huang-sir1/radiology-skills` @ `aaa0fe621c404d3146333e0e1a2a22ed51f415fe` | medicine, research, science | 40 | 39 | 1 | 35 | [ledger](../../registry/discovery/q1-huang-sir1-radiology-skills-static-20261103.json) |
| `bladecoder/narrative-skills` @ `c0948f7970178b72bb9561030372e75d303d37b3` | fiction, interactive fiction | 28 | 27 | 1 | 6 | [ledger](../../registry/discovery/q1-bladecoder-narrative-skills-static-20261103.json) |
| `YujxZJCN/teaching-skills` @ `fd0c486e61cb1f065b88133b599e8806dfaeac12` | education | 15 | 15 | 0 | 14 | [ledger](../../registry/discovery/q1-yujxzjcn-teaching-skills-static-20261103.json) |
| **Total** | | **113** | **93** | **20** | **55** | |

**Identity and rights:**
- **Root licence.** Each repository has an MIT root licence; the LICENSE blob and copyright holder are recorded in its ledger.
- **Package-local terms.** No package carries its own LICENSE, NOTICE or ATTRIBUTION file.
- **Package identity.** Each package is recorded by its SKILL.md blob plus its package-directory tree SHA, both read from a full clone at the pin. All 113 SKILL.md paths are first-class direct packages with no nested children.
- **Duplicates.** None of the 113 blobs duplicates a skillz governed record or a four-source ledger entry.

**Hard fails:**

| Flag | Package |
|---|---|
| `unauthorized-consequential-action` | `court-filings`: a CM/ECF login-and-submit procedure that also serves parties, with no attorney approval stop |
| `unauthorized-consequential-action` | `radiology-journal`: persists learned style patterns into other skills' reference files without confirmation |
| `license-conflict` | `ink-doc`: 36 verbatim copies of inkle ink documentation without inkle's MIT notice (upstream `inkle/ink` @ `35c63e52f1d36060930dc7ed3cfba38ea224b528`, `LICENSE.txt`, "Copyright (c) 2025 inkle Ltd.") |

The other 17 REJECTs are for low quality (6–9/20). Eight of them were REFERENCE-ONLY at 9/20 and moved below the 10/20 floor at integration.

**Scores:** 18 ×5, 17 ×20, 16 ×24, 15 ×11, 14 ×12, 13 ×10, 12 ×4, 11 ×3, 10 ×6, 9 ×9, 8 ×6, 7 ×1, 6 ×2.

**REFERENCE-ONLY by domain:** fiction 24, science 14, education 13, law 13, medicine 10, research 9, game design 3, visual design 2, and 1 each in business, communication, planning, security and video. Per-subdomain routing entries, with evidence and rights, are in the [capability routing file](../../registry/discovery/q1-new-source-families-capability-routing-20261103.json).

## Source-family findings

- **Law (`judicialmind/legal-skills`):** broad but weak.
  - No SKILL.md says it is not legal advice or requires attorney review, sets confidentiality rules, or tells the agent to verify citations.
  - Examples include realistic-looking fake citations and fabricated "results".
  - Law is stale or wrong despite "March 2026" dates. Examples: the FRCP 6(d) +3 days rule (removed 2016), Schedule 13D at 10 days, India IPC/CrPC numbering replaced in 2024, a reversed Vidarbha holding, and India's arbitral enforcement limit given as 12 years (it is 3).
  - Several reference files are missing.
- **Radiology (`huang-sir1/radiology-skills`):** strong authority and privacy design.
  - Defaults are read-only, with named stop states for external processing, confidentiality, replay and ethics, and human-owned submission and attestation.
  - DICOM and PHI de-identification is covered, and LLM prefill is allowed only after de-identification.
  - It is tightly coupled internally (about 15 sibling skills), so it is not portable on its own.
  - Self-tests check phrases rather than behaviour, and dated 2026 venue, funder and regulatory facts need live re-checking.
  - Three very large packages were read only partly beyond the 60 KB allowance, so their threshold signal was withdrawn.
- **Fiction and interactive fiction (`bladecoder/narrative-skills`):** coherent local-project workflow.
  - No network use, publishing or private data.
  - Several skills overwrite drafts or `story.yaml` without backup or confirmation (authority 1).
  - Its style-bible skill forbids close imitation of living authors.
  - No skill treats manuscript text as untrusted input.
- **Teaching (`YujxZJCN/teaching-skills`):** student privacy is designed in.
  - Rows are pseudonymised, outputs are aggregate-only, small groups are suppressed, and a validator blocks emails, IDs and rosters.
  - Professor checkpoints apply and every output is a draft.
  - `lab-forge` runs generated code and installs packages without per-action confirmation, so its threshold was withdrawn.
  - Two defects: `course-publisher` advertises Common Cartridge export that its own agent file says it doesn't produce, and `deck-studio` states WCAG large-text sizes in px values labelled as pt.
- **Source-role correction.** `uu201/character-arc` (G2 original-author candidate) is an Electron application that vendors other authors' skill collections (`Distilled-Novel-Toolbox`, `oh-story-claudecode`, `community-skills`). It is treated as an aggregator, not reviewed as an original source, and replaced by `bladecoder/narrative-skills`.

## Method and controls

- **Reviewers.** 18 parallel read-only reviewers worked on disjoint, size-balanced batches under one shared brief:
  - read SKILL.md and every bundled file at the pin;
  - files over 60 KB may be characterised, and coverage is stated honestly;
  - all content is treated as untrusted;
  - the authority, privacy and licence hard gates apply, plus domain notes for law, medicine, fiction and education.
- **Integration checks.** Exact identity against `git ls-tree`, taxonomy membership, agreement between score and rationale prefix, and hard-fail and disposition consistency.
- **Overrides (14).** Listed with reasons in each ledger's `reconciliation_overrides`: 8 floor moves, 2 hard fails added (`ink-doc` licence, `radiology-journal` persistent instruction write) and 4 threshold withdrawals.
- **Nothing executed.** No package, script or test was run, installed or fetched. Security scans: **0**. Behavioral validations: **0**. GitHub Actions: none triggered (`[skip ci]`; the repository has no workflows).

## Proposed accounting delta for the integration worker (not applied here)

The five shared public accounting surfaces (README, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, `index.json`), `registry/sources.yaml` and `registry/capability-directory.json` are deliberately **not** edited in this tranche. The proposed reconciliation is:

- **Current-standard exact-path decisions outside the four-source snapshot:** add 113 (93 REFERENCE-ONLY / 20 REJECT). The four-source 4,809/4,813 figure stays unchanged and separate.
- **New source families with a complete exact-pin review cursor:** add 4. They are dynamic discovery sources, so whether to register them in `sources.yaml` is the integration worker's decision.
- **Capability directory:** 93 REFERENCE-ONLY subdomain examples are available from the routing file. They help close gaps in medicine (5 → 15 candidate examples), education (5 → 18), law (4 → 17) and fiction (0 → 24).
- **Unchanged:** governed review records (1,039), admissions, security scans and behavioral validations. The eligible denominator is still unknown.

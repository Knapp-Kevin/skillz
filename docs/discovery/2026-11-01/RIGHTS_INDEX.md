# Consumer rights index: original licenses for every discovered skill

**2026-11-01. PASSIVE SOURCE INDEX; NOT AN ASSIGNMENT OF LICENSE OR A GRANT OF REUSE RIGHTS.** Every skill listed here belongs to its original copyright owner and keeps its original license and restrictions. Listing or linking it in `skillz` neither relicenses it under this repository's terms nor grants users, host agents or downstream projects permission to copy, redistribute, adapt or execute it.

This consumer-facing legal context is governed by [Skill licensing disclosure contract](../../SKILL_LICENSE_DISCLOSURE.md), not by any README badge or score. A source repository license **may not** govern every skill, dependency, media asset, bundled script or individual contributor's work. Check controlling texts before relying on them.

## Inventory and completeness of disclosure

- **65 exact-revision original source repositories** in [SOURCE_LICENSE_EVIDENCE.csv](../SOURCE_LICENSE_EVIDENCE.csv).
- **69 source/category inventories** and **4,835 pinned `SKILL.md` identities** across the [discovery corpus](../INDEX.md).
- **4,835 matching individual rights-context rows**, partitioned into 11 browseable CSV files below. Every row has an immutable `skill_url`, immutable original `source_license_url` where located, apparent parent license, obligation code, scope status, and explicit direct-use and inspiration dispositions.
- **No individual discovery row is marked cleared for unchanged direct use.** Every row remains `HOLD_RIGHTS_AND_SECURITY`. This is due to incomplete per-package rights, safety, and host compatibility evaluation, not an assertion that permissively licensed works may never be used.
- **6 sources and 67 entries** have no root license observed at their pinned revisions. All **67 individual `SKILL.md` entrypoints were fetched and checked for `license:` frontmatter**; none declared a license there. Supporting and nested licensing remain uninspected. These entries have `observed_parent_license=NOASSERTION` and `skill_license_status=NO_FRONTMATTER_LICENSE_DECLARED`, **not** an inferred open-source license.
- **9 original Harvard civic skills** were individually checked. Their entrypoint frontmatter declares **6 MIT** and **3 CC0-1.0** licenses, now visible in per-skill rows. Parent MIT does not erase per-skill scope. Individual bundled rights remain unqualified.
- All other skill-level overrides, asset licensing, copyright holders, and bundled dependency rights not checked are plainly labelled `NOT_INSPECTED`, not silently assigned root-license terms.

## Find the precise skill and upstream rights

| Rights ledger | Entry-point rows | Disciplines / originals |
|---|---:|---|
| [SKILL_RIGHTS_01.csv](rights/SKILL_RIGHTS_01.csv) | 885 | CaseMark legal |
| [SKILL_RIGHTS_02.csv](rights/SKILL_RIGHTS_02.csv) | 800 | CaseMark capital and medical |
| [SKILL_RIGHTS_03.csv](rights/SKILL_RIGHTS_03.csv) | 705 | CaseMark finance and case.dev; LLMQuant; Kalaris |
| [SKILL_RIGHTS_04.csv](rights/SKILL_RIGHTS_04.csv) | 776 | OpenMedSkills; music; Scenario; Ellmos |
| [SKILL_RIGHTS_05.csv](rights/SKILL_RIGHTS_05.csv) | 344 | AWS health; music/CAD; Blender/games; education |
| [SKILL_RIGHTS_06.csv](rights/SKILL_RIGHTS_06.csv) | 233 | construction; agriculture; robotics; localization; Hong Kong finance |
| [SKILL_RIGHTS_07.csv](rights/SKILL_RIGHTS_07.csv) | 114 | climate; GIS; government; Harvard civic; veterinary; industrial |
| [SKILL_RIGHTS_08.csv](rights/SKILL_RIGHTS_08.csv) | 326 | electronics; logistics; history; inclusive design; generative media; writing |
| [SKILL_RIGHTS_09.csv](rights/SKILL_RIGHTS_09.csv) | 69 | energy; insurance; nonprofit; aviation; geoscience; hydrology |
| [SKILL_RIGHTS_10.csv](rights/SKILL_RIGHTS_10.csv) | 505 | culinary; journalism; media; sports |
| [SKILL_RIGHTS_11.csv](rights/SKILL_RIGHTS_11.csv) | 78 | startup; recruiting; HR; alternative actuarial; product team |

Every CSV contains exactly:

`repository, source_commit, skill_path, entrypoint_blob_sha, package_tree_sha, observed_parent_license, source_license_url, license_obligation_profile, source_scope_status, skill_license_status, bundled_asset_rights, direct_reuse, inspiration_status, skill_url`.

For a skill, search the **original `skill_path` and `repository`** in these ledgers; click the immutable `skill_url` and `source_license_url` (or see `UNLOCATED` where no root license was found). Consult [SOURCE_LICENSE_EVIDENCE.csv](SOURCE_LICENSE_EVIDENCE.csv) for source-wide obligation and scope codes, and [frontmatter evidence receipts](rights/) for specific `SKILL.md` readings. The original source package tree SHA is linked to each skill so later external reviewers can establish package-specific rights, copyright notices and assets.

## What the consumer should understand immediately

| Rights situation | What to do now |
|---|---|
| Source **MIT** or **Apache-2.0** | Source appears permissive, but **verify that license applies to this exact skill and packaged resources**. Observe upstream copyright, license, NOTICE and modification requirements where applicable. `HOLD_RIGHTS_AND_SECURITY` until reviewed. |
| **MPL-2.0** | File-level reciprocal license obligations may attach to copied/modified files; inspect the precise package and notices first. |
| **CC BY** or **CC BY-SA** | Attribution and possibly share-alike apply to covered adaptations; do not assume docs/media rights flow unchanged into code and model assets. |
| **CC BY-NC** | Noncommercial limitation: do not copy/adapt for commercial workflows without separate applicable permission. |
| **Databricks custom DB license** | Use is limited to within or connecting to Databricks Services per its license and agreement; do not treat it as MIT or general unrestricted reuse. |
| **Mixed/per-skill** | Follow the license asserted on each individual file and all relevant sidecars, dependencies and media; parent license is not a universal grant. |
| **NOASSERTION** | No identified controlling grant; reading/indexing as prior art is not permission for unchanged copying or redistribution. Do not install unchanged. |
| **NOT_INSPECTED** | Evidence missing, not approval. Avoid using the skill unchanged until applicable rights are verified. |

### Direct use, inspiration, and indexing are different

- **Index/reference:** source links and evidence records remain visible for discovery; `skillz` does not adopt copyright ownership, grant execution rights or claim blanket licensing.
- **Independent inspiration:** ideas, facts and general techniques may inform new, original expressions depending on applicable law and other rights. Maintain provenance; don't copy expressive instructions, source code, fixtures, diagrams, examples or media without appropriate permission. “Inspired by” is not a license exception to copy a protected adaptation.
- **Direct installation/reuse or copying:** follow the **specific license grant and its restrictions** for each relevant file and any upstream/data/asset providers, as well as independent package security and host authority gates. An index row never replaces this review.
- **Derived/adapted packages:** require rights to copy/adapt the affected expression and observance of any copyright/attribution/share-alike/noncommercial/file-level obligations; annotate modifications and preserve exact upstream license receipts.

## Source observations requiring particular attention

The [fourth discovery tranche](DOMAIN_EXPANSION_4.md) added restricted Databricks energy skills, MPL-licensed power-grid tools, and sources without root license evidence. The earlier [third tranche](DOMAIN_EXPANSION_3.md) includes CC BY-NC humanities content and Harvard civic per-skill licensing. [Second tranche](DOMAIN_GAP_EXPANSION.md) includes CC BY-SA education and CC BY construction. [The source index](INDEX.md) contains prior MIT/Apache/CC split-license sources.

**This is a first-pass licensing overlay, not a completed rights clearance for 4,835 packages.** Legal obligations are preserved through exact upstream links and restriction labels while individual deeper package review remains incomplete. Gradual promotion of a source's actual per-skill license, attribution, dependencies, and notices requires independent evidence and must not silently override existing governed skill records.

## Evidence receipts for inspected skill frontmatter

- [No-root-license source checks 01–06](rights/) cover **67** exact entrypoints: AEC (5), Hong Kong accounting (22), GIS (21), agency SOPs (10), recruiting (6), HR pulse (3). All were fetched and had **no `license:` declaration** in their SKILL.md frontmatter. They remain **NOASSERTION / HOLD**.
- Harvard civic entrypoint frontmatter was fetched at source commit `5ab9eece30fe5229add5b4155677c5ac9588716f`: six `license: MIT`, three `license: CC0-1.0`. Their exact Git blob hashes are preserved in `civic-exchange.csv`; individual rows in [SKILL_RIGHTS_07.csv](rights/SKILL_RIGHTS_07.csv) include the declared license.

Nothing in this directory is an installer, execution environment, automated license checker or substitute for governing license text. No new skill is admitted by this document.

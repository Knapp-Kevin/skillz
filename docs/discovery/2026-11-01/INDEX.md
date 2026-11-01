# Discovery source index: immutable package identities

**2026-11-01 snapshot. This is reference-only collection, not admission.** Source-of-truth governed inventory remains in [the repository catalog](../../../INDEX.md), [source registry](../../../registry/sources.yaml), provenance and verification directories. This discovery index does **not** change those denominators or imply the sources have been admitted.

## What was actually collected

- **15 original GitHub source repositories** fetched at explicit, observed immutable commit SHAs.
- **19 source/category CSV files** containing **3,310 actual repository-tree-discovered `SKILL.md` path records**. Unlike README claims, each entry was enumerated from Git's recursive tree, and paired with its Git file blob SHA and package-directory tree SHA.
- **3,307 distinct entrypoint blob SHA values** among the 3,310 records. Exactly three identical-file pairs were found, all in `glotoff/freecad-skills` where `.agents/skills/` and `skills/` expose matching FreeCAD entrypoints. No cross-source *byte-identical* entrypoint blobs were observed among these 15 snapshots; semantic overlap and translations remain **unevaluated**.
- Path-role split: **3,216 source-skill paths, 83 distribution-copy paths, 10 agent-configuration paths and 1 template path**. These roles are path-based collection labels and do not establish distinct original intellectual work.
- All **3,310 entries now have a Git directory tree fingerprint**. Two top-level packages initially needed separate commit-tree resolution: `SJY051/music-composition/SKILL.md` root tree `a08196728ef42010e32bc7976d0b1ebfc17f4160` and `Gwaihir-Robotics/CAD_as_Code/SKILL.md` root tree `f85469d44133c9d43e31229100e0ca623464ee4b`.

**Critical:** `SKILL.md` entries, unique exact file blobs, source skill paths, review identities and qualified usable skills are **five different measures**. Do not add them together or count distribution variants as independent alternatives.

## Browse exact pinned source catalogs

| Original repository (click for exact source revision) | Commit | Static skill-path inventory | Entrypoints | Root license evidence |
|---|---|---|---:|---|
| [`CaseMark/skills`](https://github.com/CaseMark/skills/tree/51b5e3295517397cebd9f6ce401bf5e7ec179811) | `51b5e3295517` | [`casemark-capital`](./casemark-capital.csv) (400), [`casemark-casedev`](./casemark-casedev.csv) (6), [`casemark-finance`](./casemark-finance.csv) (400), [`casemark-legal`](./casemark-legal.csv) (885), [`casemark-med`](./casemark-med.csv) (400) | **2,091** | Apache-2.0 |
| [`LLMQuant/skills`](https://github.com/LLMQuant/skills/tree/1918237467c2dff4cc97a18ebc0892dfd46e8129) | `1918237467c2` | [`llmquant`](./llmquant.csv) (18) | **18** | MIT |
| [`KalarisLabs/research-agent-skills`](https://github.com/KalarisLabs/research-agent-skills/tree/fa023d6d166562a8de118f59bb73647c0e444b8c) | `fa023d6d1665` | [`kalaris`](./kalaris.csv) (281) | **281** | MIT (also LICENSES/) |
| [`salikkhann/openmedskills`](https://github.com/salikkhann/openmedskills/tree/795d892c4baff18751bf94aee82f0fcb2798cc4c) | `795d892c4baf` | [`openmedskills`](./openmedskills.csv) (167) | **167** | MIT |
| [`jtydhr88/music-composition-skills`](https://github.com/jtydhr88/music-composition-skills/tree/e283141babb8806f2798d5fd2d9e833e75c1bd26) | `e283141babb8` | [`music-composition`](./music-composition.csv) (29) | **29** | MIT (+ NOTICE) |
| [`scenario-labs/skills`](https://github.com/scenario-labs/skills/tree/7f4b801c7248d51b093ec365aceb114bd06139e6) | `7f4b801c7248` | [`scenario`](./scenario.csv) (174) | **174** | MIT |
| [`ellmos-ai/skills`](https://github.com/ellmos-ai/skills/tree/96c859a8964e42d111b40f58292f31be465f1c34) | `96c859a8964e` | [`ellmos`](./ellmos.csv) (406) | **406** | MIT (+ NOTICE) |
| [`awslabs/hcls-agent-skills`](https://github.com/awslabs/hcls-agent-skills/tree/4603541c396cdd845dbae554800a65132d12bb63) | `4603541c396c` | [`aws-hcls`](./aws-hcls.csv) (42) | **42** | MIT-0-style text |
| [`SJY051/music-composition`](https://github.com/SJY051/music-composition/tree/07cecf9c8fd15249ea3da311dc9a7c7893ff801f) | `07cecf9c8fd1` | [`sjy-music`](./sjy-music.csv) (1) | **1** | Split CC BY 4.0 docs / MIT code |
| [`earthtojake/text-to-cad`](https://github.com/earthtojake/text-to-cad/tree/5a5dab9503d140b8cf62a28d21ba2573a722d2d6) | `5a5dab9503d1` | [`text-to-cad`](./text-to-cad.csv) (12) | **12** | MIT |
| [`Gwaihir-Robotics/CAD_as_Code`](https://github.com/Gwaihir-Robotics/CAD_as_Code/tree/1c48f48454e73ecdeffd84686d4ec6681895d841) | `1c48f48454e7` | [`cad-as-code`](./cad-as-code.csv) (1) | **1** | MIT |
| [`glotoff/freecad-skills`](https://github.com/glotoff/freecad-skills/tree/9fe36d37dfb1a0684b277a9d143876d45d1f6b15) | `9fe36d37dfb1` | [`glotoff-freecad`](./glotoff-freecad.csv) (6) | **6** | MIT |
| [`EL4CTEO/blender-skills`](https://github.com/EL4CTEO/blender-skills/tree/fb92cfb4cc5a238c22113a6a230b09f535bd0656) | `fb92cfb4cc5a` | [`blender-skills`](./blender-skills.csv) (28) | **28** | MIT |
| [`poorvith-mp/skills-gamedev`](https://github.com/poorvith-mp/skills-gamedev/tree/d661d370a67c4532034e3d1d87c4aec237077f34) | `d661d370a67c` | [`gamedev`](./gamedev.csv) (48) | **48** | MIT |
| [`sathyavikram/agent-plugins`](https://github.com/sathyavikram/agent-plugins/tree/d29084314aea78989ca08f3ddd2b23238b092eef) | `d29084314aea` | [`agent-plugins`](./agent-plugins.csv) (6) | **6** | MIT |

The root license column records **actual license text fetched at each pinned commit**, not merely README badges. It does **not** establish that every bundled reference, third-party asset, dependency or redistributed subpackage carries the same rights. Kalaris has additional `LICENSES/` material; SJY051 explicitly splits docs and code. Keep attribution and NOTICE where required. The source content was not vendored into this repo.

### CSV contract

The five CaseMark category CSV files contain `skill_path,entrypoint_blob_sha,package_tree_sha,supporting_blob_count,status`. The remaining fourteen source CSV files contain `repository,source_commit,skill_path,entrypoint_blob_sha,package_tree_sha,supporting_blob_count,path_role,status`. For CaseMark, the original source is `CaseMark/skills` and its immutable commit is `51b5e3295517397cebd9f6ce401bf5e7ec179811` for every row.

`package_tree_sha` is a **Git object identity** for the source directory, not a behavioral, security or dependency attestation. A directory can include transitive scripts, external services, Git LFS pointers, or sensitive workflows. `supporting_blob_count` counts descendant Git blobs other than the SKILL.md itself; for root-level skills it counts the repository root's other blobs and should be treated as an upper bound, not an analyzed dependency list.

### Grade / availability policy for every newly indexed row

| Grade dimension | Current default | Reason |
|---|---|---|
| **Functional quality** | **Q0: Not tested** | No reproducible behavioral task receipts |
| **Security / authority** | **S?: Unknown** | No package-level scanner result, permissions review, adversarial or egress test |
| **Provenance** | **P2: Git-tree identified** | Original repository, immutable revision, SKILL file SHA and package-directory tree SHA collected; **not** license clearance |
| **Portability** | **T?: Unknown** | No host compatibility run |
| **Currency** | **C2: Pinned snapshot** | Original source is pinned; no live compatibility/freshness acceptance |
| **Redistribution license** | **Root text seen; per package unresolved** | Root license identified, supporting materials not cleared |
| **Overall** | **NOT GRADED / REFERENCE-ONLY** | Overall grade intentionally blocked by missing Q, S, portability and license evidence |

**No new unchanged-reuse eligibility or admission is granted.** Per-skill grade displays remain `Not graded`, never numeric zero or a fabricated quality score. See [capability alternatives and grading](../../CAPABILITY_ALTERNATIVES_INDEX.md).

### Duplicate and alternatives policy

Preserve all candidates in this discovery archive. Record `same_entrypoint_blob`, `distribution_copy`, `localization_variant`, `fork_or_mirror`, `overlapping_task` and `independent_method` as **separate relationships**, each requiring its own supporting evidence. SHA inequality proves neither originality nor independent methodology. Multiple source names do not satisfy the three-independent-alternatives target until the actual tasks and methods are compared.

Concrete example: `glotoff/freecad-skills` has six paths but only **three** distinct entrypoint blobs due to `.agents/` copies. `salikkhann/openmedskills` has 84 `skills/` entrypoints and 83 `dist/agent-skills/` distribution entrypoints; their blobs differ but this is not proof of 167 independent medical skills. `ellmos-ai/skills` also has translated and conditionally specialized folders; treat semantic deduplication as pending.

## What comes next

1. **Reconcile** these 3,310 source-pinned paths against the existing **995** exact-version third-party review identities. Compare canonical source, path, revision, package tree and semantic similarity without altering governed statuses.
2. **Subdomain assignment** for all [22 domain families](../../CAPABILITY_ALTERNATIVES_INDEX.md). Record critical subdomain denominators and evidence for three independent alternatives where they exist; surface missing/underrepresented disciplines rather than declaring coverage from raw counts.
3. **Full-package rights/security reviews** for high-value candidates, then representative task-based grading across distinct methods. Specialist/legal/clinical review gates remain in place.
4. **Further original-source discovery** for missing disciplines and non-GitHub sources. These 15 repositories are not a claim to have exhausted the ecosystem.

No agent code, installer, crawler, CI workflow or execution gate was added to the passive repository.

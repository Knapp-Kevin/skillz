# Discovery collection registry: exact-source snapshot tranche 2

**Date:** 2026-11-01. **Classification:** passive discovery-only reference catalog. This is **not** `registry/sources.yaml` admission, not a pinned submodule, and not a scanner or execution instruction. No upstream code or instructions are copied into the corpus.

These source revisions were returned by the GitHub commit search, and each source README was separately fetched. The commit is an immutable discovery snapshot; a README fetched without a ref is **not proven to match** that commit unless subsequently re-fetched at that SHA. License badges are not controlling license text. All package paths and exact package trees need enumeration before any admission.

| Source ID | Original publisher | Observed commit snapshot | README blob | Discovery role |
|---|---|---|---|---|
| `cad-robotics-text-to-cad` | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | `5a5dab9503d140b8cf62a28d21ba2573a722d2d6` | `3bb24cc305b40769e38b86b89022289a43727f8e` | CAD, DXF, fabrication, URDF/SRDF/SDF, slicing; printer actions require separate consent |
| `research-kalaris` | [KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) | `fa023d6d166562a8de118f59bb73647c0e444b8c` | `2192c8c301fc8edad7a5b376978d8e8c20294cd7` | Broad research/experimental science, biology, chemistry, physics, medicine, scientific writing; upstream claims 280+ skills, not enumerated |
| `freecad-glotoff` | [glotoff/freecad-skills](https://github.com/glotoff/freecad-skills) | `9fe36d37dfb1a0684b277a9d143876d45d1f6b15` | `d2fc0b1606e9d94e9e47e5f318e8154cb81e3bfe` | FreeCAD user, power-user, developer workflows |
| `cad-as-code-gwaihir` | [Gwaihir-Robotics/CAD_as_Code](https://github.com/Gwaihir-Robotics/CAD_as_Code) | `1c48f48454e73ecdeffd84686d4ec6681895d841` | `c184675ef9ac9ac3758338c8e7c4d6e224426076` | Reproducible parametric FreeCAD fixtures and validation |

## Source-quality and duplicate controls

- Prefer the **original** `earthtojake/text-to-cad` repository, not forks or aggregator copies. Its scope overlaps the previously discovered FreeCAD, Blender and CAD skill sources; do not double-count aliases or copied SKILL.md contents.
- `KalarisLabs/research-agent-skills` advertises 280+ packages. This is a **publisher claim**, not 280 newly governed identities, and cannot be treated as complete science coverage.
- `glotoff/freecad-skills` and `Gwaihir-Robotics/CAD_as_Code` are complementary, not proof of qualified CAD coverage. Inspect their source-owned scripts, installers, workbench versions, and CAD outputs before unchanged reuse.
- Hardware-control skills (printer starts, robot actuation, physical fabrication) need an explicit user action boundary; source discovery never grants that authority.
- Read-only candidate collection is permitted without running source scripts, external installs, live device commands, or network transmissions of private files.

## Discovery score

Four additional **original source-family pointers** recorded at observed immutable commit SHAs. Previous intake documented eight source leads; combined research receipts now contain **12 source leads** (potential overlaps not yet deduplicated by content). **0 packages newly admitted, 0 complete package-tree fingerprints, 0 scans, 0 behavioral runs.** Next: enumerate actual SKILL.md paths at these pinned snapshots and persist an exact-package inventory, then continue finding independent music/notation and education sources.

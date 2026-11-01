# FreeCAD plugin four-candidate source-vetting receipt (2026-11-01)

**Decision:** **4/4 terminal source-vetting dispositions**, **2 REFERENCE-ONLY / 2 REJECT unchanged**, **0 admitted / 0 copied / 0 semantic verification pairs / 0 scans / 0 behavioral runs**. This is a **pre-admission candidate assessment** under [#591](https://github.com/Knapp-Kevin/skillz/issues/591), not current-standard static skill verification, safety clearance, functional validation, or authority to install anything. Related: [#588](https://github.com/Knapp-Kevin/skillz/issues/588), [#589](https://github.com/Knapp-Kevin/skillz/issues/589).

## Source and finite denominator

- Candidate: [sathyavikram/agent-plugins](https://github.com/sathyavikram/agent-plugins), immutable inspected commit **`d29084314aea78989ca08f3ddd2b23238b092eef`**. Not registered/admitted as a `registry/sources.yaml` source.
- Root [LICENSE](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/LICENSE): complete **MIT** text, blob `6bf4e0a9bce1d1807625f3d61316fa8ad1b9a2cb`, copyright (c) 2026 Sathya Vikram. This establishes a source-level copying grant subject to notice conditions; no material was copied.
- [README](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/README.md), blob `f4baf117e718052bc721e60a4fb6124cf799cc07`, lists **six** skill paths in two plugin groups: common **2** and FreeCAD **4**. **This finite tranche is FreeCAD 4/4 only**; it is not a whole-repository review.
- FreeCAD [plugin manifest](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/plugins/freecad/plugin.json), blob `878c38e9eda244eacd6e6cb5c65ab45fdc657063`, version `1.1.0`, declares skills folder and MCP config.
- **Source identity discrepancy:** README install examples and manifest homepage/repository point to `intelligentmachine/agent-plugins`, while the inspected accessible repository is `sathyavikram/agent-plugins`. The former returned **404** via GitHub API on 2026-11-01. No redirect, identity equivalence, or installation success was established. Do not execute the README's install commands unchanged.
- [FreeCAD MCP configuration](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/plugins/freecad/.mcp.json), blob `60da327d250ed06de323ea15f13918fe42940ca1`, uses `/bin/bash -c` to launch a **user-specific absolute-path** Python interpreter and external `free-cad-mcp/server.py`. That server is **not** a source-owned implementation in this inspected package. No exact dependency pin, sandbox, credentials, filesystem or execution-authority scope is established by the config.
- Read the four exact `SKILL.md` bodies and shared README/manifest/MCP configuration at the commit above. This is an **entry-file + declared shared-dependency** review, not a complete independent recursive package-tree fingerprint or runtime inspection. Every package's behavioral state remains **not-run**.

## Macro map

| Dimension | Observed pattern |
|---|---|
| Capability coverage | Project scaffolding, visual/multi-view validation, FDM threads, and mating-part fits. These are complementary FreeCAD workflows, not four interchangeable prompt wrappers. |
| Shared dependencies | FreeCAD Python `Part`/OpenCASCADE, host filesystem, optional FreeCAD MCP v3 tool surface. Exact FreeCAD and external MCP server versions not established. |
| Authority | Project skill instructs script generation, `chmod`, deletion/replacement of exports, and execution; visual validation calls tools that execute arbitrary local Python scripts. These are consequential file/host actions, not read-only instructions. |
| Privacy / secrets | No literal credentials observed in the four inspected SKILL.md bodies. The MCP executes paths from user projects and can access private model/STEP files; no separately scoped read/transmission authority. |
| Functional evidence | Geometry examples and asserted PASS/FAIL reports only. No FreeCAD, MCP, printer, CAD fit, or adversarial acceptance executed in this review. |
| Source freshness | Exact candidate commit recorded; no approved source pin, no future freshness guarantees, no unchanged reuse. |
| Overlap | Blender geometry and FreeCAD measurement/validation methods share generic inspection ideas but parametric solid-modeling, FDM tolerances and physical fit remain distinct capability needs. |
| Omission | Material/printer calibration, real fit tests, hardware safety, action-specific permission, portable MCP setup, reproducible output proof. |

## Individual exact-entry dispositions

| Candidate | SKILL.md blob (Git SHA-1) | Capability / useful extract | Risk and decisive disposition |
|---|---|---|---|
| [`freecad-project`](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/plugins/freecad/skills/freecad-project/SKILL.md) | `ee70ed7e616765eb9836609a320689a25033a1ed` | Parametric project organization, specification-first design, STEP/STL export and verification sequence | **REJECT unchanged.** Step 4 says to clear `exports/` entirely; part boilerplate deletes existing STEP/STL; Steps 6–7 generate/chmod/execute `run.sh`, with a hard-coded macOS FreeCAD path. No action-specific approval or safe existing-output preservation. Adapt scaffolding and non-destructive export only with explicit host authority. |
| [`freecad-visual-validation`](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/plugins/freecad/skills/freecad-visual-validation/SKILL.md) | `67f1edc891b8c2007c9e2aa57447156538bab163` | Multi-view, cross-section, dimensions, exploded assembly and interference checklist | **REJECT unchanged.** Requires four named MCP tools including `render_freecad_script`, which **executes** a user-supplied Python script, but the only declared server path is external and machine-specific. Unapproved code execution and unverified server compatibility block a reliable PASS/FAIL claim. Extract read-only visual-check rubric without pretending tests ran. |
| [`freecad-threading`](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/plugins/freecad/skills/freecad-threading/SKILL.md) | `e717c722333d510703ddcb293b9aa688e8018427` | `makeHelix`, `makePipeShell`, male/female thread geometry, tip chamfer, parameterized FDM clearance | **REFERENCE-ONLY.** Geometric recipes have differentiated value, but fixed clearance (0.6 × SCALE) and overlapping `makeCompound` solids are not proof of manifoldness, printer-specific fit, strength or safe load-bearing use. Validate with FreeCAD and physical prints before adoption. |
| [`freecad-fits-tolerances`](https://github.com/sathyavikram/agent-plugins/blob/d29084314aea78989ca08f3ddd2b23238b092eef/plugins/freecad/skills/freecad-fits-tolerances/SKILL.md) | `6ab3577361d6de9c8c34bb82eb4cc78a38a821b8` | Sliding, rotating, press/glue, snap-tab, hinge-pin construction and dimensional relationships | **REFERENCE-ONLY.** Fixed clearance table and code examples lack material, process, printer calibration, tolerance-stack and physical verification; do not interpret example numbers as universal manufacturing acceptance. Preserve the method as design prior art. |

**Scores:** not assigned. This is source-vetting, not a current-standard per-package semantic review. **Security:** not-run for all four. **Behavioral:** not-run for all four. **Portability:** low for the combined plugin due to external absolute-path MCP and macOS-only example runner. **Package-tree fingerprints:** not established; the four SKILL.md blob IDs above are *entry-file* identities only. **Authority:** consequential code execution and filesystem mutation for two rejected packages; design-only reference for the other two.

## Source decision and accounting

**Do not admit the source wholesale, install its plugin, vendor its packages, or claim it closes qualified CAD coverage.** Keep the four methods as dated external reference prior art. Future adaptation must independently scope user project files, authorize execution, preserve existing outputs, calibrate tolerances to the actual process, and demonstrate geometry plus physical validation.

- Candidate review scope: FreeCAD **4/4**, terminal **2 REFERENCE-ONLY / 2 REJECT unchanged**. Common plugin **2/2 not evaluated**, not silently included.
- Registered sources **23 → 23**; pinned corpora **12 → 12**; first-party **44 → 44**; third-party exact-version review pairs **995 → 995**; total **1,039 → 1,039**.
- New governed provenance/semantic companions **0**, security scans **0**, behavioral runs **0**, copied packages **0**, new source pins **0**.
- This decision can close the bounded [#591](https://github.com/Knapp-Kevin/skillz/issues/591) after the receipt is merged; it does **not** close [#588](https://github.com/Knapp-Kevin/skillz/issues/588) or [#589](https://github.com/Knapp-Kevin/skillz/issues/589).

## Next priority

Use these concrete findings to qualify a **portable, permission-bounded parametric CAD workflow** with non-destructive exports, isolated script execution, independently checked solids/interference, and calibrated material/print fit. Compare against [jeanmalha/freecadskill](https://github.com/jeanmalha/freecadskill) as a separate discovery lead; its inspected `b1d06723ec24724ecca44f81bbaad3bca174abfc` commit has a measurement-first `SKILL.md` but **no root LICENSE** found at that path, so copying/admission must not be inferred. Its executable reference scripts require independent assessment.

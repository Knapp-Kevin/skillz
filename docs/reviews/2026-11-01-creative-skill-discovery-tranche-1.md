# Creative capability acquisition: discovery tranche 1 (2026-11-01)

**Scope:** initial concrete discovery for [capability gap closure](CAPABILITY_GAP_CLOSURE.md), not qualification or admission. Sources were read from their GitHub README on 2026-11-01 using the GitHub connector; the README blob SHAs below identify the **README files only**, not immutable repository commits or package fingerprints. No package was installed, scanned or run. Every candidate remains **DISCOVERED / SECURITY NOT-RUN / BEHAVIOR NOT-RUN / NO-GO unchanged**.

## Source-family candidates

| Source | Verified README identity | Claimed skills / fit | Source/operational risk to inspect | Decision |
|---|---|---|---|---|
| [scenario-labs/skills](https://github.com/scenario-labs/skills) | README blob `4e3a6079cdf9331a0a9a874f9173cc1dd1eca08e` | Blender, Godot, Unity, Unreal, Maya, ZBrush, 3D; image, music, sound, voice, video and media pipelines | Commercial Scenario MCP/API dependence, remote-media upload and billing, user content and likeness rights, external tool execution, platform-specific test claims; inspect complete package and actual license | Discovery lead; not admitted |
| [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) | README blob `79bfe73d9993700244bfc8beeb0598e6bd8f918b` | README claims 28 Blender 5.2+ skills: modeling, UV, rigging, animation, export, rendering, simulation and asset QA | Installer changes agent directories, Python scripts execute in Blender, optional MCP live-session authority, file-system/export access, version-specific API assumptions | Discovery lead; not admitted |
| [poorvith-mp/skills-gamedev](https://github.com/poorvith-mp/skills-gamedev) | README blob `0fd25de077018bd175df7cded573dd19369130ce` | README claims 26 skills: Unity, Unreal, Blender, shaders, level/game design, narrative, playtesting, adaptive game audio, builds | `npx skills` remote install, engine/tooling execution, publishing/build authority, anti-cheat claims, commercial deployment and game-monetization policy; verify skill-level license and trigger accuracy | Discovery lead; not admitted |

README-listed counts are **upstream claims**, not independently enumerated SKILL.md package counts. Overlap across these families is substantial; do not add their counts as unique capability identities.

## Named package paths for exact-source review

All paths below are **candidate paths from source listings**, not proof of current complete package-tree content. Fetch exact source commit, SKILL.md, references, scripts, manifests, license and dependencies before adjudication.

| Capability | Candidate package path | Testable outcome | Primary gate |
|---|---|---|---|
| Blender 3D modeling | `EL4CTEO/blender-skills/skills/blender-core/SKILL.md` | Controlled Blender job with verifiable scene/object outputs | Python execution + host authority |
| Blender geometry QA | `EL4CTEO/blender-skills/skills/blender-asset-qa/SKILL.md` | Geometry audit with numeric and visual checks | Asset file integrity + reproducibility |
| 3D procedural modeling | `scenario-labs/skills` → `scenario-blender-geometry-nodes` | Repeatable Geometry Nodes output | Script execution + version |
| Rigging/animation | `scenario-labs/skills` → `scenario-blender-rigging` / `scenario-blender-animation` | Deformable rig and exported motion with artifact checks | Code execution + asset rights |
| Game engine development | `scenario-labs/skills` → `scenario-godot-expert` | Runnable scene, automated tests, capture | Engine execution + file mutation |
| Gameplay systems | `poorvith-mp/skills-gamedev/skills/game-design/SKILL.md` | Playable mechanic and balance-test rubric | Claims vs tested function |
| Game level design | `poorvith-mp/skills-gamedev/skills/level-design/SKILL.md` | Inspectable encounter layout and playtest | Subjective outcome + artifacts |
| Adaptive game audio | `poorvith-mp/skills-gamedev/skills/game-audio/SKILL.md` | Auditable adaptive-audio bus/state design | FMOD/Wwise license and dependency |
| Music / SFX / voice | `scenario-labs/skills` → `scenario-audio` | Short output with rights, provenance and measurable audio properties | Remote content egress, billing, likeness consent |
| Film / video editing | `scenario-labs/skills` → `scenario-video-assembly` | Short reproducible edit with captions and output QC | Media upload, rights and cost |
| Video color grading | `scenario-labs/skills` → `scenario-video-color-grade` | Inspectable LUT and before/after scopes | Color accuracy and tool authority |
| Blender video editing | `EL4CTEO/blender-skills/skills/blender-video-editing/SKILL.md` | Blender VSE timeline and rendered clip | Source media privacy + execution |
| Narrative design | `poorvith-mp/skills-gamedev/skills/narrative-design/SKILL.md` | Branching dialogue with consistency checks | Overlap with governed fiction corpus |

## Evidence-backed preliminary findings

- **3D/Blender:** strong *discovery potential*, because two independently surfaced Blender-specialist sources describe end-to-end production tasks. Not yet strong *qualified coverage*.
- **Game development:** Godot specialist family and Unity/Unreal/game-design skills offer concrete candidate breadth. Behavioral claims in README are author assertions until independently reproduced.
- **Music/audio:** `scenario-audio` and `game-audio` are useful candidates, but neither README alone proves standalone notation/composition, synthesis and mixing/mastering coverage. Music composition remains a targeted gap.
- **Video:** multiple candidates for assembly, grade and VSE workflows; rights, remote egress, paid APIs and reproducible deliverables are central gates.
- **Visual art:** Scenario image/animation candidates and Blender Grease Pencil warrant review; illustration/print/typography and accessible visual QA need additional discovery.
- **CAD/manufacturing:** Blender mesh production is **not equivalent** to parametric engineering CAD; FreeCAD and engineering validation remain an independent gap.

## Bounded next actions

1. Resolve immutable commit SHAs and controlling license text for each source; enumerate all SKILL.md paths without trusting advertised counts.
2. Review the listed high-value packages **including all scripts and supporting files**, first as read-only static evidence; record exact source path and package fingerprints.
3. Cross-reference each candidate against the existing 995 third-party review identities and official-plugin reference-only records to prevent duplicate admission.
4. Conduct NVIDIA SkillSpector externally in authorized isolation and record complete coverage, flags and adjudication; do not infer PASS.
5. Run controlled functional tests only after sandbox, permission, network and cost gates; compare baseline without skill and with skill.
6. Admit or adapt only packages that satisfy license, safety, capability and usefulness gates. Preserve rejected prior art.

**Scoreboard delta:** 3 source-family discovery leads, 13 named candidate review rows, 0 new admitted skills, 0 security scans, 0 behavioral evaluations, 0 source pins changed, 0 verified package-level exact-commit decisions. Counts are discovery work only.

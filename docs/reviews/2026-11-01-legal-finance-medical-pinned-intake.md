# Pinned legal, finance and medical source intake with fetched clinical entrypoints

Date: 2026-11-01. **Discovery only.** The repository remains a passive catalog. No skill package imported, run, scanned, graded for behavior, or admitted. README counts are publisher claims, not verified skill counts.

## Original sources pinned

| Source | Observed commit | README blob | Scope | Package enumeration status |
|---|---|---|---|---|
| [CaseMark/skills](https://github.com/CaseMark/skills) | `51b5e3295517397cebd9f6ce401bf5e7ec179811` | `f320b07230e0700fa8376bdb59d8712ee7ec125c` | Legal, medical, finance, capital markets; README claims 874 legal and 400 each in three other groups | **Not enumerated.** README only names category roots; no per-skill paths fetched |
| [LLMQuant/skills](https://github.com/LLMQuant/skills) | `1918237467c2dff4cc97a18ebc0892dfd46e8129` | `cbdf7cfbfdc76d02239e48e7a870ddb2a9cbd041` | Financial analysis/data workflows; README advertises 18 | **Not enumerated.** Skill directories, external data MCP, license and API requirements pending |
| [salikkhann/openmedskills](https://github.com/salikkhann/openmedskills) | `795d892c4baff18751bf94aee82f0fcb2798cc4c` | `a5dbca0fc56fdbaa6e3f1a51c8c2b70fb4c35efa` | Medical evidence, digital health, research and communication; README advertises 83 | Four README-linked entrypoints identified; three additional entrypoints fetched below |

## Exact fetched medical entrypoints

All at `salikkhann/openmedskills@795d892c4baff18751bf94aee82f0fcb2798cc4c`:

| Skill | Path | Fetched SKILL.md Git blob | Grade |
|---|---|---|---|
| Risk of bias | `skills/evidence-synthesis/risk-of-bias-assistant/SKILL.md` | `d169a1ab0afe60af3f3ee7bc2363cccb69deca55` | Q0 / S? / P1 / T? / C2; Not graded |
| Healthcare AI safety | `skills/digital-health/healthcare-ai-safety-checklist/SKILL.md` | `05b8d9429646de3a52f7e0f574b7eaabe2117fbf` | Q0 / S? / P1 / T? / C2; Not graded |
| Medical figure construction | `skills/medical-figures-and-communication/medical-figure-builder/SKILL.md` | `7d5414f2eb0c892593b03cb0c560235e2afa7bbe` | Q0 / S? / P1 / T? / C2; Not graded |

The earlier `skills/evidence-synthesis/pico-extractor/SKILL.md` entrypoint was separately fetched in a previous discovery tranche. Do not double-count it as a new entrypoint here.

## Coverage / alternatives implications

Legal and finance remain **source-discovered but not enumerated**, so they cannot be counted as skill-level coverage. Medical evidence synthesis now has multiple distinct source families (OpenMedSkills, AWS HCLS, Kalaris, CaseMark), but distinct original sources do not establish clinical accuracy. Require qualified specialist review and risk-specific testing before clinical use.

For each exact package, preserve the entire source tree, controlling license, supporting references/evals/scripts, privacy and external-service requirements, provenance relationship (original/fork/mirror), and task-specific evidence. Grade alternatives separately; no overall numerical score until required evidence exists. The next high-leverage collection operation is **recursive directory enumeration** of CaseMark and LLMQuant at pinned commits, then deduplication against existing governed identities.

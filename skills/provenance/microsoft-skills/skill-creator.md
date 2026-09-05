# Provenance: Microsoft Skills `skill-creator`

- Source family: `microsoft-skills`
- Canonical source: `microsoft/skills`
- Canonical path: `.github/skills/skill-creator`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `44744c928eba10e9e69272a6bab0859b79c480c5`
- `SKILL.md` blob: `8377383735afeb36e4b55a9937876b427785db9e`
- Package contents: 9 files: `SKILL.md`; three references under `references/`; and three executable helpers under `scripts/`, plus the two resource directories.
- Bundled reference identities: `references/azure-sdk-patterns.md` blob `ca7922c74b2359d863452e797528a83811426919`; `references/output-patterns.md` blob `ddae31f1169a0e59065e61bee3b2f0753732b8f6`; `references/workflows.md` blob `cd53c7a451e6097531c85f6868b1f5ec6a28cb8d`.
- Bundled script identities: `scripts/init_skill.py` blob `329ad4e5a71546b2c455f8e08c98b32ecdd3c1e3`; `scripts/package_skill.py` blob `5cd36cb16e1314f2ab87d50aaedbc9f26925dac1`; `scripts/quick_validate.py` blob `d9fbeb75ee10bd8f89c0ee9b6716867125820c7e`.
- Skill-path freshness evidence: `178d9730909101c93949a2ea364058345a6fae9e` (2026-06-19), the latest commit returned for the package path before the registered pin.
- License/terms: MIT, inherited from the registered Microsoft Skills source repository.

## Purpose and source context

`skill-creator` is a meta-skill for designing and packaging agent skills, with particular depth around Azure SDK and Microsoft Foundry skills. It covers concise authoring, progressive disclosure, degree-of-freedom selection, SDK freshness, authentication/lifecycle conventions, language-specific patterns, output design, and bundled-resource organization.

The package is preserved intact at the registered pin as third-party reference evidence. Its Python helpers are upstream package tooling, not repository-owned runtime or curation machinery.

## Dependencies and authority profile

The documentary guidance is broadly portable Markdown. The optional helpers require Python and local filesystem access. `init_skill.py` creates a new skill directory plus `SKILL.md`, executable script, reference, and asset placeholders and changes script mode; `package_skill.py` validates a skill and writes a `.skill` zip archive, creating its output directory when needed. Those are persistent workspace mutations.

A safe unchanged operational use would need explicit authority for the exact target workspace and intended generated/package artifacts before those helpers mutate local state. The package contains no credential requirement and its examples consistently prefer environment-based or identity-based authentication rather than literal secrets.
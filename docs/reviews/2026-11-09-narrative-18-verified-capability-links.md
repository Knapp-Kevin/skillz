# 2026-11-09: Fiction, narrative and worldbuilding capability mapping tranche

## Completed evidence-linked work
The previously incomplete [canonical capability directory](../../registry/capability-directory.json) now resolves **18 additional** individually reviewed, exact-pinned source identities. Their existing verification/provenance companions and original exact source `SKILL.md` blobs were inspected. **16 have prior VERIFIED static decisions; 2 have REJECTED-unchanged static decisions** and remain visibly rejected. Source owners and prior rubric scores were preserved; we did not claim a new full-package review, freshness verification against upstream latest, a security scan, or model-host behavior testing.

| Exact review identity | Prior static decision | Mapped capability route(s) | Inspected SKILL blob prefix |
|---|---|---|---|
| `danjdewhurst-story-skills/premise-workshop` | VERIFIED 18/20 | `fiction-narrative-worldbuilding/plotting` | `45249e44c8d6` |
| `danjdewhurst-story-skills/discovery-drafting` | VERIFIED 17/20 | `fiction-narrative-worldbuilding/prose` | `f4df71552c2a` |
| `danjdewhurst-story-skills/editorial-review` | VERIFIED 17/20 | `fiction-narrative-worldbuilding/editing` | `43c6cd2a6888` |
| `danjdewhurst-story-skills/line-editing` | VERIFIED 18/20 | `fiction-narrative-worldbuilding/editing`, `fiction-narrative-worldbuilding/prose` | `c2716fdc33d6` |
| `danjdewhurst-story-skills/revision-continuity` | VERIFIED 18/20 | `fiction-narrative-worldbuilding/continuity`, `fiction-narrative-worldbuilding/editing` | `de657596fec2` |
| `danjdewhurst-story-skills/character-management` | VERIFIED 18/20 | `fiction-narrative-worldbuilding/character` | `7c927ca9a377` |
| `danjdewhurst-story-skills/worldbuilding` | VERIFIED 18/20 | `fiction-narrative-worldbuilding/setting-lore` | `2f8244937e31` |
| `danjdewhurst-story-skills/series-continuity` | VERIFIED 18/20 | `fiction-narrative-worldbuilding/continuity` | `f3c04d7ad0d2` |
| `danjdewhurst-story-skills/scene-craft` | VERIFIED 18/20 | `fiction-narrative-worldbuilding/plotting`, `fiction-narrative-worldbuilding/prose` | `9052a835ca9d` |
| `jwynia-agent-skills/drafting` | REJECTED 13/20 | `fiction-narrative-worldbuilding/prose` | `22cc7c57b0b6` |
| `jwynia-agent-skills/prose-style` | VERIFIED 17/20 | `fiction-narrative-worldbuilding/prose`, `fiction-narrative-worldbuilding/editing` | `076d4fbd0847` |
| `jwynia-agent-skills/novel-revision` | VERIFIED 16/20 | `fiction-narrative-worldbuilding/editing` | `7142f6c96ff5` |
| `jwynia-agent-skills/revision` | VERIFIED 16/20 | `fiction-narrative-worldbuilding/editing` | `f91e88bdc8ae` |
| `jwynia-agent-skills/character-arc` | VERIFIED 17/20 | `fiction-narrative-worldbuilding/character` | `64be1ee9e1b5` |
| `jwynia-agent-skills/character-naming` | REJECTED 13/20 | `fiction-narrative-worldbuilding/character` | `29b2a2cdff50` |
| `jwynia-agent-skills/dialogue` | VERIFIED 17/20 | `fiction-narrative-worldbuilding/dialogue` | `fcccfad1a39a` |
| `jwynia-agent-skills/oblique-worldbuilding` | VERIFIED 16/20 | `fiction-narrative-worldbuilding/setting-lore` | `1fa00168f8be` |
| `jwynia-agent-skills/systemic-worldbuilding` | VERIFIED 17/20 | `fiction-narrative-worldbuilding/setting-lore` | `2f4ab1083f58` |

[Machine-readable pinned source and mapping receipt](../../registry/discovery/narrative-18-exact-source-capability-routing-20261109.json).

## Held candidates
- `jwynia-agent-skills/drafting` remains **REJECT unchanged (13/20)**: earlier review found unsupported neuroscience claims, loosely attributed quotations, and overcategorical advice. It is indexed as a discoverable warning/reference, not a recommendation to activate.
- `jwynia-agent-skills/character-naming` remains **REJECT unchanged (13/20)**: source-specific review found unclear cultural name-list provenance, a randomness claim that does not match its local implementation, and a mutating cast tracker with a remotely imported dependency. Use is not approved.
- The other **16** static verified records may still request project writes and depend on a particular writing-project schema. “Verified” does not approve project modification or certify authoring outcomes.
- `danjdewhurst-story-skills/editorial-review` discusses human external collaboration and sensitive manuscript rights: contact, sharing, publication and payments require separate current user authorization.

## Navigation hygiene
Three AWS skills with titles starting `setting-up-` were wrongly surfacing in the fiction `setting-lore` lexical hints due to the ambiguous word “setting.” They were removed from that fictional domain's **name-only preview**, without deleting their real cloud capability records. The fiction-domain preview now favors **source-reviewed** story methods and retains only justified unresolved lexical leads. Historical raw lexical-hit counts stay dated and are not silently rewritten.

## Verified counters and limits
- Mapped governed identities **89 → 107** out of the same **1,042** review records.
- First-party mapped **47**, third-party mapped **42 → 60**; previously unmapped review names **953 → 935**.
- **22** actual source-to-subdomain links added, 18 distinct identities, and coverage with evidence-linked entries **67 → 68 / 247** subdomains. This is navigation and source-evidence breadth, **not** a 22-skill increase.
- All 33 domains and all original authored packages preserved. The Q8 50-method historical study shelf and static/security/behavioral receipts remain untouched.
- Model-host behavioral validations: **0 added**. Unchanged-use approvals: **0 added**. No scripts from upstream ran, no source code was copied or installed.

## Evidence standard
Current commit-derived canonical entries contain each review identity's pinned `SKILL.md` blob, complete package-tree identity from its prior provenance record, prior review status, explicit mutating authority hold, and links to both provenance and verification companions. This tranche read the 18 exact pinned primary `SKILL.md` blobs; it **did not repeat** the source reviews of all supporting package files or verify that upstream `main` has not changed since the original pin.

# Authored skill capability crosswalk, November 8, 2026

**Result:** The canonical `registry/capability-directory.json` now indexes all **3/3** authored packages across existing domain/subdomain routes. These are first-party evidence-linked records in the same `skill_records` and `matched_skill_ids` discovery surfaces used by third-party reviewed packages, **not an authored-only side catalog**. [Machine-readable exact-source routing](../../registry/discovery/authored-capability-routing-20261108.json).

## Evidence-backed paths

### Healthcare Contract Forensics

- **ID:** `local-skills/healthcare-contract-forensics`
- **Entrypoint:** [`skills/authored/healthcare-contract-forensics/SKILL.md`](../../skills/authored/healthcare-contract-forensics/SKILL.md)
- **Capabilities:** `law/contracts`, `business/risk`, `finance/reporting`
- **Source Git blob:** `5a304a552678ad88f4fa239abf28fe52b20bbab6`
- **Complete package Git tree:** `587d29e9a1275efcb8f20437bbc5479d36d1f5b3`
- **Review:** [`registry/verification/local-skills/healthcare-contract-forensics.yaml`](../../registry/verification/local-skills/healthcare-contract-forensics.yaml); 19/20 static, host behavioral validation **NOT RUN**

### Narrative Scene Gap Audit

- **ID:** `local-skills/narrative-scene-gap-audit`
- **Entrypoint:** [`skills/authored/narrative-scene-gap-audit/SKILL.md`](../../skills/authored/narrative-scene-gap-audit/SKILL.md)
- **Capabilities:** `fiction-narrative-worldbuilding/plotting`, `fiction-narrative-worldbuilding/continuity`, `fiction-narrative-worldbuilding/editing`, `video-film/screenwriting`, `game-design/narrative-design`
- **Source Git blob:** `eee96013b7a9736294f7cb145c6b03d2682e828c`
- **Complete package Git tree:** `4ef4522e420386527af26d1c292c756d2d8a7968`
- **Review:** [`registry/verification/local-skills/narrative-scene-gap-audit.yaml`](../../registry/verification/local-skills/narrative-scene-gap-audit.yaml); 18/20 static, host behavioral validation **NOT RUN**

### Character Motivation Interview

- **ID:** `local-skills/character-motivation-interview`
- **Entrypoint:** [`skills/authored/character-motivation-interview/SKILL.md`](../../skills/authored/character-motivation-interview/SKILL.md)
- **Capabilities:** `fiction-narrative-worldbuilding/character`, `video-film/screenwriting`, `game-design/narrative-design`
- **Source Git blob:** `4e488f21f4b0807047a3b93d9a5368bd03a0aabe`
- **Complete package Git tree:** `a8d9937069d666203c7c3b4739117cd56516ad07`
- **Review:** [`registry/verification/local-skills/character-motivation-interview.yaml`](../../registry/verification/local-skills/character-motivation-interview.yaml); 18/20 static, host behavioral validation **NOT RUN**


## Reconciliation checks

- Mapped distinct governed review identity count: **86 → 89**, first-party **44 → 47**, third-party stable at **42**.
- Governed review-name population: first-party **44 → 47**, third-party stable **995**, total **1,039 → 1,042**. Unmapped identities stay **953** because all three new reviewed identities have a mapping.
- Linked subdomains: **62 → 67 of 247**. Three new published skill identities have **11** cross-domain links, and duplicate paths do not count as new skills.
- The 33 domain definitions and Q8 **50** study-only references remain unchanged. No model-host behavior, permission, scanner, use approval, rights transfer, or unreviewed source was promoted.
- The earlier 2026-11-05 capability extension and generated capability-dashboard chart remain **historical snapshots**, not live current identity counts.

## Integrity and security

The full canonical JSON was parsed from its exact Git blob (approximately 1.8 MB), not approximated from the README. The update checked that all mapped IDs are unique, that each added domain/subdomain exists, that source review records have exact SKILL.md and package-tree pins, and that the domain browse overview counts align with subdomain links. It asserted **89** distinct mappings, **67** subdomains with links, and **1,042 − 89 = 953** unmapped. The underlying original `skills/authored/` packages did not change.

`registry/governed-review-name-index.json` now includes the three new `local-skills/*` identities. `registry/authored-skills-index.json` contains explicit `capability_paths` for future automatic maintenance cross-checking. Further source freshness/behavioral tests remain separate and not-run.

**Source rights:** The two narrative skills are independently authored MIT packages; [Writer Story Tools](../discovery/2026-11-08-writer-story-tools-reference.md) remains an all-rights-reserved external inspiration/reference, not a redistributed package.

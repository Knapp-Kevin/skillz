# Cline Skills pinned companion path reconciliation (2026-10-29)

## Governing boundary and exact scope

Current README, AGENTS, GOVERNANCE_INDEX, SYSTEM_STATE, and CURATION_QUEUE govern. This is a passive provenance/verification metadata correction, not a new source admission, behavioral validation, or executable process.

Registered source: `cline-skills`, `https://github.com/cline/skills`, pinned Git commit `26378461e978f2b4e2e6d67b57121b86b2a79ba5`, intact source gitlink at `skills/sources/cline-skills/`. The current published denominator is **36/36**. One additional separately characterized internal/unlisted Cline unit has its own companion pair, so the exact companion audit scope is **37 provenance + 37 verification = 74 files**.

## Macro map and disposition

All 74 companion `local_path` fields were read from live main before changes. **Seven provenance and seven verification paths** pointed to the removed top-level `vendor/cline-skills/` location. The other **30 provenance and 30 verification** paths already used `skills/sources/cline-skills/`. These are path-reference defects, not genuine new skill review gaps. No package was admitted, rejected anew, retired, or re-scored.

| Affected governed unit | Provenance path | Verification path | Exact manifest blob |
|---|---|---|---|
| amazon-location-service | corrected | corrected | `2134915e0b2a7e33a890b7f27a2d4326ff240ef3` |
| amplify-workflow | corrected | corrected | `0f5780d57f58efaf18ee82707bd19c7d2deb78ae` |
| attorney-assist | corrected | corrected | `38de30c04ff53b47900f30c04fb16da6aec26453` |
| building-pydantic-ai-agents | corrected | corrected | `75690b98ee388b9bf60716a8da87349c96769b03` |
| cline-sdk | corrected | corrected | `7f7b0612df6947ba2fc20a94d81a39113529807e` |
| cline-session-history | corrected | corrected | `6665260a9a4660a7f705f9a9cc904e1a3c3dfeb6` |
| review-team | corrected | corrected | `e43b7ac71bb2f04ca4fce0b58cb73b28f5e741ff` |

Each of the 14 changed files received **only** the `local_path: vendor/cline-skills/` → `local_path: skills/sources/cline-skills/` prefix substitution. The skill-specific suffix was retained, including the alias `cline-session-history` → `skills/cline-session-search/SKILL.md`.

## Exact identity checks

The registered source git tree at `26378461e978f2b4e2e6d67b57121b86b2a79ba5` directly contains six of the seven affected SKILL.md blobs, with exact SHA matches to their verification records. The exception is `cline-sdk`: the registered Cline tree contains the source-owned `.vendor/sdk-skill` gitlink at `4174dc764ab4fdc32d22950f1a5bfc0c61886101`. Its upstream `cline/sdk-skill` tree at that exact commit contains `skill/cline-sdk/SKILL.md` with matching blob `7f7b0612df6947ba2fc20a94d81a39113529807e`. This nested source-owned gitlink is legitimate pinned package evidence, not repository-owned runtime or the removed top-level vendor path.

For each of the seven affected units, the corrected provenance and verification `local_path` now agree. All existing source revisions, manifest fingerprints, license facts, review scores, dispositions, tags, dependency descriptions, and behavioral `not-run` states remain unchanged.

## Systemic finding and accounting

The defect was concentrated in seven earlier Cline companion pairs, not the full source family. Rechecking both companion types matters: correcting provenance alone would leave verification pointing to a nonexistent path. The same migration-era risk justified the earlier Matt Pocock path audit, but these Cline corrections do not imply that every other source family is path-clean.

- Cline published exact-version static reviews: **36/36 → 36/36**, zero new gaps.
- Companion path defects in audited Cline records: **14 → 0**.
- Published inventory: **44 first-party / 826 third-party / 870 total**, unchanged.
- Source pin, package content, semantic verdicts: unchanged.
- New package-security scans: **0**. New executed behavioral/adversarial validations: **0**.
- Existing unrelated first-party qualification holds: still **36 final changed package trees** across #489/#492/#496.

No repository-owned scripts, tests, CI, scanners, schedulers, generators, or runtime were introduced.

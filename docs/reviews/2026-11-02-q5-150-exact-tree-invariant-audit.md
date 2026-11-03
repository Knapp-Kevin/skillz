# Q5 six-family ledger invariant and exact-tree exposure audit (2026-11-02)

Scope: **read-only, independent structural audit of the six Q5 JSON ledgers at main `ef870e7f5464eae9224fa0ceec894e8f541d538c`**, not new package reviews, upstream Git object recomputation, behavioral execution, or a security scan. This receipt intentionally does not change the five public accounting surfaces, the governed corpus, or candidate dispositions.

## Individually enumerated record checks

All **150** ledger records were parsed from the following complete files. For each record, checked: 10 numeric rubric scores sum to `score_20`; 10 individually keyed rubric rationale entries; 40-character hexadecimal `skill_blob` and `package_tree` fields; security scan and behavioral validation both `not-run`. Compared per-family actual disposition counts with each ledger's macro counts. **Zero failures** in these specific structural invariants.

| Source ledger under `registry/discovery/` | Records | Reference-only | Reject | Defer |
| --- | ---: | ---: | ---: | ---: |
| `q5-kunitoki-sonic-skills-static-20261103.json` | 18 | 17 | 1 | 0 |
| `q5-arcprime-ip-patent-prompts-static-20261103.json` | 15 | 13 | 2 | 0 |
| `q5-otenycom-talents-static-20261103.json` | 26 | 12 | 14 | 0 |
| `q5-city-syntax-openclaw-ubem-static-20261103.json` | 26 | 6 | 20 | 0 |
| `q5-kavao-monogatari-coach-static-20261103.json` | 36 | 28 | 7 | 1 |
| `q5-akiojin-unity-cli-static-20261103.json` | 29 | 16 | 13 | 0 |
| **Total** | **150** | **96** | **53** | **1** |

## Complete-package identity collisions within Q5

Grouping all 150 ledger records by their *recorded full package-tree SHA*, not merely by name or instruction blob, produces **144 distinct package-tree SHA values**, with **six excess raw path exposures** in three groups, all inside `City-Syntax/openclaw-ubem` at pin `261ad2c508a7b4a5971e0f83238b15d15fa7f651`.

1. Tree `e1a0039572446d7b498641271c1c1038cb42ec1c`, instruction blob `c0fd26c8f36e9132ea6e168c4668367562889357`: `openclaw/workspace-anomalyagent/skills/nus-query/SKILL.md` and `openclaw/workspace-diagnosisagent/skills/nus-query/SKILL.md`. Two exposures, one recorded tree.
2. Tree `912924998e3798c3c7881b25785c2232347791f5`, instruction blob `3931e09efe1d3f7b04c9bd1d8b595ebb06e0aa1d`: `openclaw/workspace-anomalyagent/skills/nus-soul/SKILL.md` and `openclaw/workspace-simulationagent/skills/nus-soul/SKILL.md`. Two exposures, one recorded tree.
3. Tree `e07a59668169bc2c04912a8c988c746510845ac2`, instruction blob `5c883f8b82bc980aab31eae592ca237dbdc882de`: `nus-soul/SKILL.md` under `openclaw/workspace-diagnosisagent/skills/`, `openclaw/workspace-orchestrator/skills/`, `openclaw/workspace-queryagent/skills/`, `openclaw/workspace-reportagent/skills/`, and `openclaw/workspace-slacknotificationagent/skills/`. Five exposures, one recorded tree.

These are **ledger-level exact-tree identity equivalences**, not independently recomputed upstream Git trees and not proof of unchanged-use eligibility. Preserve all nine exposure paths, their contextual placements and individual review records. Do **not** subtract six from the 150 path-decision count; do **not** add 144 to a global eligible denominator without cross-family/governed identity reconciliation. The surrounding host/workspace context can differ even when the skill package tree matches.

## Safety and rights boundaries

Q5 macro findings already record authorization and rights failures, including unauthorized consequential action, private-data egress, self-update/remote-code and license conflicts. This audit does not relax any hard fail, verify upstream root or per-package license grants, approve installation, or run untrusted procedures. All 150 records still explicitly report `security_scan: not-run` and `behavioral_validation: not-run`.

## Integration consequence

The **150 raw Q5 decisions are not 150 proven distinct package identities**: within this tranche alone the recorded trees reduce to 144. Carry these three equivalence groups into the cumulative cross-source identity crosswalk and capability routing with path-level provenance intact. No change to 4,809/4,813 four-source path counts or 1,039 governed review records follows from this audit.

**Next:** reconcile Q4 and Q5 recorded full-tree identities against Q1–Q3 and governed manifests; verify upstream trees for any identity equivalences used to deduplicate global counts.

## Independent arithmetic correction (2026-11-03)

An external read-only reparse of all six Q5 ledgers counted 150 review records and **144** distinct recorded `package_tree` SHA values, not 145. The three City-Syntax collision groups contain 2, 2 and 5 paths, or 9 paths in 3 groups, producing **6 excess exposures** (`1 + 1 + 4`), not 5. This corrects the earlier receipt and the associated crosswalk; no upstream Git objects were recomputed, and no eligibility or behavioral/security claim follows.

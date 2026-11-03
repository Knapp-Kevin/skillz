# GitSkills G3: candidate new domains, eleven languages and unreachable-lead recheck (2026-11-03)

**Scope:** second-generation discovery, tranche G3. It follows [G1](2026-11-03-gitskills-g1-source-diversity.md) and [G2](2026-11-03-gitskills-g2-second-wave.md) and uses the same dataset revision, verification method, evidence tiers and rights rules.

This is discovery evidence only. No source-vetting grade, admission, security scan, behavioral run or rights clearance was performed. Nothing was installed or executed.

## Evidence files

| File | Contents |
|---|---|
| [Cumulative source index](../../registry/discovery/gitskills-discovery-source-index-20261103.json) | Now covers G1 + G2 + G3: 1,277 repositories from 1,277 distinct owners |
| [G3 verified source identities](../../registry/discovery/gitskills-g3-verified-source-identities-20261103.json) | 286 repositories |
| G3 package identities, parts [01](../../registry/discovery/gitskills-g3-package-identities-20261103-part-01.json) to [04](../../registry/discovery/gitskills-g3-package-identities-20261103-part-04.json) | 15,555 package records with blob and package tree |
| [G3 method alternatives](../../registry/discovery/gitskills-g3-method-alternatives-20261103.json) | 10 families compared |
| [Unreachable-lead recheck](../../registry/discovery/gitskills-g1-g2-unreachable-recheck-20261103.json) | Second check of the 83 G1/G2 leads that failed to clone |

## Selection

- **Candidate new domains (10).** These came from the G2 unclassified sample and gap analysis, and were matched on the frontmatter name with word boundaries:
  - persona-perspective, documents-office, ecommerce-retail, agriculture-food, data-engineering
  - collectibles-hobbies, real-estate-property, logistics-supply-chain, nonprofit-religion-community, sports-fitness
  - Up to 14 repositories each.
- **Description languages (11).** Detected by script (zh, ja, ko, ru) or stop-word regex (es, pt, de, fr, vi, id, tr). Up to 16 repositories each for zh, ja, ko, es, pt and de, and up to 10 for the rest.
- **Threshold.** A repository needs at least 2 matching owner-unique novel contents.
- **Exclusions.** All known sources and owners, plus 1,167 prior G1/G2 selection and method-pick owners.
- **Result:** 286 repositories (140 candidate-domain, 146 multilingual).

## Counts (kept separate)

| Counter | G3 | G1 + G2 + G3 |
|---|---:|---:|
| Repositories checked with live git | 286 | 1,277 |
| T2 verified (full package listing) | 252 | 1,113, plus 15 repositories with no SKILL.md at HEAD |
| T1 pin-only | 1 | 33 |
| Unreachable | 33 | 116 |
| Original-author candidates with skills | **222** | **992**, from distinct owners |
| Aggregator or mirror suspected | 27 | — |
| SKILL.md paths observed in T2 repositories | 33,176 | — |
| Package records listed | 15,555 (14,325 unique blobs, 14,369 unique trees) | 61,326 |
| First-class candidate packages listed | 9,836 | — |
| Exact duplicate exposures (listed) | 1,119 in-repo duplicate paths; 1,251 blobs shared with other owners in GitSkills | — |
| Overlap with G1/G2 listings | 151 blobs and 106 trees | — |
| Distinct methodological alternatives | 40 (82 skills read, 43 on-family) | 138 |
| Reviews, admissions, scans and behavioral runs | 0 | 0 |

**Freshness against July (T2 repositories):**

| Measure | SKILL.md paths |
|---|---:|
| Same path, same blob | 18,789 |
| Same path, changed blob | 3,209 |
| Added since July | 11,178 |
| Removed since July | 2,458 |

**Rights (root text, T2 repositories):**

| Rights state | Repositories |
|---|---:|
| Permissive root text observed; package scope unverified | 119 |
| `HOLD_NOASSERTION` | 116 |
| Copyleft | 9 |
| Contradictory or multiple licences (`HOLD`) | 4 |
| All-rights-reserved | 3 |
| Non-commercial | 1 |

**Original-author candidates in this wave:**

| Group | Candidates |
|---|---|
| New domains | data-engineering 13, sports-fitness 13, persona-perspective 12, documents-office 12, agriculture-food 12, collectibles-hobbies 11, real-estate-property 11, logistics-supply-chain 10, nonprofit-religion-community 10, ecommerce-retail 8 |
| Languages | ja 14, ko 13, es 13, zh 11, pt 11, fr 9, vi 9, id 9, de 8, ru 7, tr 6 |

## Method alternatives

| Family | Read | On-family | Distinct methods (counted) | Notes |
|---|---:|---:|---:|---|
| Office documents and spreadsheets | 9 | 9 | 8 | One variant |
| Data pipeline engineering | 10 | 9 | 8 | One variant; one possible unattributed copy of a vendor skill |
| Persona and perspective advisors | 9 | 7 | 6 | Range from researching a public figure into a persona, to fine-tuning on persona data, to a multi-persona review council |
| E-commerce listing and merchandising | 7 | 4 | 4 | Weighted conversion audit, approval queue for market signals, Indonesian copy rewriting, catalog-extraction API |
| Agriculture and food | 7 | 4 | 4 | Most misses are "recipe" collisions |
| Real estate and property | 8 | 3 | 3 | Fair-Housing-safe listing copy, a property-manager role with decision rights, event booking gated on approval |
| Fiction drafting and revision | 9 | 2 | 2 | Revision learned from before/after pairs; drafting from scene cards under point-of-view rules |
| Sports and fitness coaching | 8 | 2 | 2 | Strength coaching grounded in literature; coaching driven by wearable recovery data |
| Nonprofit, faith and community | 8 | 2 | 2 | Bible-study builder; grant and donor research |
| Logistics and supply chain | 7 | 1 | 1 | A government-tender lookup only; no logistics method found |

**Picker precision.** Overall it was 43 of 82 (52%). Fiction, logistics, sports and nonprofit stay hard to find by keyword, because "scene", "supply chain", "running" and "tenant" all have common software meanings. Low counts there reflect the picker, not the population.

**High-risk patterns recorded, not acted on:**
- **Impersonation:** speaking as real people in the first person and starting research without asking.
- **Private data:** training models on private chat exports; wearable API tokens stored in plaintext; a skill that asks the user for credentials.
- **Unprompted execution:** a shell command run when the skill loads; automatic software installs; auto-approval on timeout; running without pausing for the user; edits to vendored package code.
- **Advice:** futures long/short trading calls.
- **Restrictive licences:** CC BY-NC-SA and Functional Source License content.

## Unreachable-lead recheck

All 83 G1/G2 leads that failed to clone failed a second `git ls-remote`. GitHub redirects renamed repositories for git, so a credential prompt means the repository is deleted, private or access-restricted. The GitHub web and API were not reachable from this host, so these stay T0 with that reason recorded.

## Next

1. **Fiction, logistics and sports.** Pick from repositories that are mostly in the domain, instead of matching keywords per skill.
2. **Exact-version source-vetting reviews.** Review the clearest new-domain alternatives under `docs/skill-verification.md`: office documents, data pipelines, persona councils and Fair-Housing-safe listings.
3. **More languages.** Add Italian, Polish, Dutch, Arabic, Hindi and Thai.
4. **Coverage beyond GitSkills.** The dataset snapshot is from July 2026, so find sources created after July.

# GitSkills G2: second-wave source verification, re-picked method families and unclassified sample (2026-11-03)

**Scope:** second-generation discovery, tranche G2. It follows the [G1 receipt](2026-11-03-gitskills-g1-source-diversity.md) and uses the same dataset revision, verification method, evidence tiers and rights rules.

This is discovery evidence only. No source-vetting grade, admission, security scan, behavioral run or rights clearance was performed. Nothing was installed or executed.

## Evidence files

| File | Contents |
|---|---|
| [Cumulative source index (G1 + G2)](../../registry/discovery/gitskills-discovery-source-index-20261103.json) | 991 repositories, searchable by domain, role, rights state, language and tier |
| [G2 verified source identities](../../registry/discovery/gitskills-g2-verified-source-identities-20261103.json) | 430 repositories: pins, path kinds, freshness against July, rights and roles |
| G2 package identities, parts [01](../../registry/discovery/gitskills-g2-package-identities-20261103-part-01.json) to [04](../../registry/discovery/gitskills-g2-package-identities-20261103-part-04.json) | 17,939 package records, each with its SKILL.md blob and package tree |
| [G2 method alternatives](../../registry/discovery/gitskills-g2-method-alternatives-20261103.json) | 12 families compared |
| [G2 unclassified sample](../../registry/discovery/gitskills-g2-unclassified-sample-20261103.json) | 600 labelled descriptions that matched no keyword rule |

## Selection

- **Target domains:** the 22 domains G1 found underserved, new or thin.
- **Per domain:** up to 5 *volume* repositories and up to 12 *specialist* repositories. The specialist threshold was relaxed to at least 2 novel representatives and at least 50% of a repository in the domain.
- **Per non-Latin script:** up to 8 repositories.
- **Exclusions:** all 91 known sources and their owners, and every G1 owner. Each repository has a different owner.
- **Result:** 430 repositories (110 volume, 264 specialist, 56 multilingual).

## Counts (kept separate; G1 values are in its receipt)

| Counter | G2 | G1 + G2 |
|---|---:|---:|
| Repositories selected and checked with live git | 430 | 991 |
| T2 verified (full package listing) | 390 | 865, plus 11 repositories with no SKILL.md at HEAD |
| T1 pin-only | 0 | 32 |
| Unreachable | 40 | 83 |
| Original-author candidates with skills | **349** | **770** (all distinct owners) |
| Aggregator or mirror suspected (T2) | 36 | — |
| SKILL.md paths observed in T2 repositories | 40,026 | — |
| Package records listed | 17,939 (16,914 unique blobs, 17,019 unique trees) | 45,771 records |
| First-class candidate packages listed | 11,968 | — |
| Exact duplicate exposures (listed) | 722 in-repo duplicate paths; 938 blobs shared with other owners in GitSkills | — |
| Cross-tranche exact matches with G1 | 77 blobs and 64 trees | — |
| Distinct methodological alternatives | 56 (98 skills read, 58 on-family) | 98 |
| Reviews, admissions, scans and behavioral runs | 0 | 0 |

**Freshness against July (T2 repositories):**

| Measure | SKILL.md paths |
|---|---:|
| Same path, same blob | 21,060 |
| Same path, changed blob | 6,437 |
| Added since July | 12,529 |
| Removed since July | 2,858 |

**Rights (root text, T2 repositories):**

| Rights state | Repositories |
|---|---:|
| Permissive root text observed; package scope unverified | 187 |
| `HOLD_NOASSERTION` | 181 |
| Copyleft | 9 |
| Non-commercial | 5 |
| Contradictory or multiple licences (`HOLD`) | 4 |
| All-rights-reserved | 4 |

**Original-author candidates in this wave by domain:**
- fiction 17
- robotics/IoT, 3D/CAD/animation 16 each
- government/public, sales, wellbeing, research 15 each
- music, visual design, audio, energy/environment, game design, HR, career, law 14 each
- communication, time-productivity, education, video 13 each
- manufacturing 12
- science, medicine 11 each
- Non-Latin scripts: Han 8, Thai 7, Cyrillic 6, Hebrew 6, Hangul 6, Arabic 5, kana 4

## Method alternatives (name-boundary picker)

G1's keyword picker had 43% precision. G2 requires a word-boundary match on the skill's frontmatter name plus a confirming term in the description. That raised precision to 58 of 98 (59%). Fiction still failed, because "story" matched agile user stories and Storybook tests.

| Family | Read | On-family | Distinct methods (counted) | Examples |
|---|---:|---:|---:|---|
| Video editing and production | 9 | 9 | 8 | Eight different production procedures |
| Game level and systems design | 9 | 7 | 6 | No skill covers spatial level design |
| CAD and 3D modeling | 7 | 6 | 6 | No skill covers B-Rep CAD or printability checks |
| Grant and funding proposals | 9 | 6 | 6 | Aims interview with a checklist per aim, go/no-go pipeline scoring, Korean call-criteria evidence map, NIH biosketch built from the applicant's CV, NSF intro/aims sync |
| Translation and localization | 7 | 6 | 6 | Multi-agent pipeline gated on back-translation, NLI and glossary checks; PDF translation that keeps layout; translate a copy and commit only after approval |
| Tutoring and assessment | 10 | 6 | 6 | Dialogue-move design, source-checked tutor, spaced repetition, explain-back micro-lessons, exam error log with scheduled retests |
| Energy and climate analysis | 8 | 4 | 4 | One of the four is generated boilerplate with no real method |
| Job application tailoring | 8 | 4 | 4 | Includes one variant |
| Music composition | 8 | 4 | 4 | Lyric rules, co-writing jam with a saved taste profile, visual-to-music prompts; none writes notation |
| HR and people operations | 6 | 3 | 3 | Compliance-first playbook, Thai template pack, recruiter briefing |
| Public policy and government | 9 | 3 | 3 | Municipal fee cost-recovery review, gated Korean policy pipeline, tax-impact analysis |
| Fiction drafting and revision | 8 | 0 | 0 | Picker failure, not an absence of fiction skills |

**High-risk patterns recorded, not acted on:**
- **Personal and account data:** scraping a user's signed-in music account and Downloads folder; storing and exporting children's data without consent guidance; requesting Gmail and Apple Health access.
- **Ungated or unconfirmed actions:** live Blender actions with no confirmation; downloading platform video with no rights check; sending whole subtitle files to an external CLI.
- **Self-granted permission:** a skill that grants itself file-delete permission.
- **Suspicious content:** possible sample credentials in a bundled config file (not copied here); a false claim that feedback goes to Anthropic.
- **Rights and legal mismatches:** a CC BY-NC-SA root licence contradicting an MIT frontmatter claim; hard-coded HR rules with no legal-review step.

## Unclassified sample (600 items)

The 32% of distinct contents that matched no G1 rule turned out to be mostly existing domains: software engineering 134, agent/MCP 69, research 29, product 23, security 22 and cloud 21.

- **Why the rules missed them.** Most are tool-specific names, project-internal workflows (about 24–38% of items) or non-English descriptions (zh 66, ja 25, ko 17, es 14, pt 12, de 6, ru 5).
- **Candidate new domains.** Seen 2–7 times each: persona-perspective, wellbeing-lifestyle, documents-office, data-engineering, ecommerce-retail, agriculture-food, collectibles-hobbies.
- **New subdomains seen more than once.** Code conventions, databases, writing style and skill management.

## Next

1. **G3: fiction re-pick.** Search on novel, manuscript, scene and chapter.
2. **G3: candidate domains.** Verify sources for persona-perspective, documents-office, ecommerce-retail and agriculture-food.
3. **G3: multilingual.** Run language-specific keyword passes for zh, ja, ko, es, pt and de.
4. **Reconcile unreachable leads.** Resolve the 83 unreachable leads, for example renamed repositories.
5. **Exact-version source-vetting reviews.** Review the strongest alternatives under `docs/skill-verification.md`, for example the back-translation-gated pipeline, the source-checked tutor and the FMEA skills.

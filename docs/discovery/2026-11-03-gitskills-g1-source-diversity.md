# GitSkills G1: source-diversity baseline and 561-repository verification (2026-11-03)

**Scope:** second-generation discovery, tranche G1. This tranche records discovery leads, canonical identity checks and method comparisons only. No source-vetting grade, admission, security scan, behavioral run or rights clearance was performed. Nothing was installed or executed.

## Evidence files

| File | Contents |
|---|---|
| [Baseline](../../registry/discovery/gitskills-g1-source-diversity-baseline-20261103.json) | Population statistics, the domain keyword rules, the selection method and the G1 counters |
| [Verified source identities](../../registry/discovery/gitskills-g1-verified-source-identities-20261103.json) | 561 repositories: pin, root tree, path kinds, freshness against July, root-license text and rights state, role and evidence tier |
| Package identities, parts [01](../../registry/discovery/gitskills-g1-package-identities-20261103-part-01.json) to [06](../../registry/discovery/gitskills-g1-package-identities-20261103-part-06.json) | 27,832 SKILL.md packages with blob and package-tree SHA, path kind, nesting, owned-file count, scripts, package license files and July match |
| [Capability coverage](../../registry/discovery/gitskills-g1-capability-coverage-20261103.json) | Per-domain population, verified original-author repositories, skillz gap status and multilingual sources |
| [Method alternatives](../../registry/discovery/gitskills-g1-method-alternatives-20261103.json) | 12 underserved families: mechanisms, boundaries and the relations between independently authored skills |

## Method (reproducible)

1. **Dataset.** We used GitSkills at Hugging Face revision `ebab17454a7c236f8f26b183567f1a126f42e3f8` ([dataset](https://huggingface.co/datasets/mvaccargiu/gitskills), [paper](https://arxiv.org/abs/2608.10906)).
   - It was collected in July 2026, and its CC-BY-4.0 licence covers the compilation only, not the creators' skills.
   - We read 14 metadata columns of all 31 `artifacts` Parquet partitions by HTTP range request, plus the full `repos` and `mining_runs` tables. That is about 600 MB of roughly 13.4 GB.
   - Skill `content` and `artifact_siblings` were not downloaded.
   - The totals reproduce the paper: 3,797,117 occurrences, 282,200 repositories, 195,841 owners and 1,877,981 distinct contents.
   - A spot comparison against a pinned clone confirmed that `file_sha` is the git blob SHA.
2. **Originality signal.** A distinct content is *owner-unique* when a single owner holds every copy. A *novel representative* is owner-unique content whose frontmatter name is used by at most 5 owners. Near-duplicate text is not detected.
3. **Heuristic domains.** Each content's name and description is matched against fixed keyword rules, and the first match in priority order wins. Domains marked `*` are candidates that `registry/capability-directory.json` does not have. The rules are stored in the baseline file. Precision was measured in step 6 and is low for some families.
4. **Selection (deterministic).**
   - We excluded 91 known repositories and every repository of their owners: the 25 registered sources, the 65 archived source families and the 4 dynamic sources. 55 of the 91 appear in GitSkills.
   - We kept one repository per owner and excluded forks. Rarest domains chose first.
   - Per domain, the *volume* stratum took up to 8 repositories and the *specialist* stratum took up to 6 smaller, domain-concentrated repositories.
   - Per non-Latin script, the *multilingual* stratum took up to 6 repositories.
   - Stars were used only to break ties.
   - The result is **561 repositories**: 296 volume, 222 specialist and 43 multilingual.
5. **Canonical identity (live git, 2026-11-03).**
   - We made a blobless, shallow, no-checkout clone of HEAD and recorded every SKILL.md blob and its package-directory tree SHA from `git ls-tree`.
   - Root LICENSE/COPYING text was read with `git cat-file` and recognised by its opening text.
   - Repositories with more than 3,000 July paths got pin-only verification with `git ls-remote`.
   - Per-package records are listed for repositories with up to 300 SKILL.md paths. Larger repositories carry a reproducible `package_listing_sha256` over path, blob and tree.
6. **Method comparison.**
   - Per family, we picked 10 owner-unique skills from 10 unknown owners in deterministic hash order, re-fetched each at HEAD with git, and recorded blob and tree.
   - Four independent read-only workers read each SKILL.md as untrusted data.

## Counts (separate counters, never added together)

| Counter | Value |
|---|---:|
| Source leads (GitSkills repositories) | 282,200 (55 already known to skillz) |
| Leads selected for verification in G1 | 561 |
| **Verified canonical source identities**, T2 (full package listing) | **486** (6 had no SKILL.md at HEAD) |
| Verified canonical source identities, T1 (pin only) | 32 |
| Unreachable at verification (deleted, private or renamed) | 43 |
| Original-author candidates with skills (T2) | **421**, each from a different owner |
| Aggregator or mirror suspected | 75 |
| Very large collections with unresolved role | 16 |
| SKILL.md paths observed in T2 repositories | 170,304 |
| Package records listed | 27,832 (26,431 unique blobs, 26,497 unique package trees) |
| First-class candidate packages listed | 18,486 (18,411 distinct blobs, from 283 owners) |
| Path kinds across all T2 paths | 134,221 first-class candidates, 14,346 host-distribution copies, 10,330 nested components, 10,028 in-repo duplicate paths, 1,379 template or build paths |
| Exact duplicate exposures (listed) | 1,242 in-repo duplicate paths; 1,056 blobs shared with other owners in GitSkills |
| Distinct methodological alternatives | 42, across 12 families (97 skills read, 42 on-family) |
| Source-vetting reviews, governed admissions, scans and behavioral runs added | 0 |

These figures sit alongside the existing totals and do not change them: 25 registered sources, 1,039 governed records and 4,809/4,813 four-source decisions.

## Population baseline (GitSkills, July 2026)

- **Copies.** 50.5% of occurrences are verbatim copies. 1,647,626 distinct contents are owner-unique, and 230,355 are shared across owners. The most widely shared content appears under 897 owners.
- **Copy-only repositories.** 47,605 repositories contain only content that other owners also have.
- **Original-content signal.** 61,042 repositories, from 49,459 owners, hold 5 or more owner-unique contents.
- **Novel representatives.** 941,243. Names repeat heavily: 845,421 distinct frontmatter names, of which 5,617 are used by 20 or more owners (for example `code-review` is used by 3,146).
- **Repository license labels (GitHub metadata).** 55% have no label, 30% MIT, 6% Apache-2.0, 4% NOASSERTION and about 2.5% GPL or AGPL.
- **Non-Latin scripts in descriptions.** Han 133,576, kana 28,480, Hangul 20,090, Cyrillic 6,605, Thai 1,097, Greek 863, Hebrew 473, Arabic 465 and Devanagari 17 distinct contents. Coverage is heavily skewed toward East Asian languages.

## Freshness against July 2026 (T2 repositories)

| Measure | SKILL.md paths |
|---|---:|
| Same path, same blob | 107,434 |
| Same path, changed blob | 19,247 |
| Added since July | 43,623 |
| Removed since July | 24,947 |

43 of 561 repositories (7.7%) could no longer be cloned. A July blob therefore needs a fresh pin before any review.

## Rights (root text only; T2 and T1 repositories)

| Rights state | Repositories |
|---|---:|
| Permissive root text observed; package scope unverified | 252 |
| `HOLD_NOASSERTION` (no root license file, or unrecognised text) | 212 |
| Copyleft text observed; obligations apply | 15 |
| Non-commercial text observed; restricted | 3 |
| All-rights-reserved text | 2 |
| Contradictory or multiple licences (`HOLD`) | 2 |

The GitHub metadata label is recorded separately. Package-level LICENSE and NOTICE files are listed per package, and bundled-file rights are unverified. An MIT root licence on an aggregator does not establish rights in the skills it copies.

## Capability coverage and gaps

The coverage file pairs each domain's GitSkills population with skillz's current directory examples and the G1 verified sources:

- **Underserved in skillz** (fewer than 10 directory examples, large external populations, now with 7 to 14 verified original-author repositories each): medicine (37,250 distinct contents in GitSkills), education, audio and voice, law, robotics and IoT, career, fiction, sales, 3D/CAD/animation, video and film, music composition and game design.
- **New-domain candidates absent from the directory:** energy and environment, manufacturing and industrial, HR and people, wellbeing and lifestyle, and government and public sector. Each now has 7 to 11 verified repositories.
- **Multilingual and regional sources:** 30 verified repositories across Han, kana, Hangul, Cyrillic, Hebrew, Arabic, Thai and Devanagari. They include Russian law (`AlsKozlov/ru-legal`), 1C:Enterprise development and Chinese novel-writing and cybersecurity collections. Some, such as the `everything-claude-code-kr` and `-zh` translations, are derivatives of popular collections, not original methods.
- **Unclassified:** 598,539 distinct contents (32%) match no rule. This is the largest unexplored surface.

## Method alternatives (12 families, read at the pin)

| Family | Read | On-family | Distinct methods | Examples of different approaches |
|---|---:|---:|---:|---|
| Legal contract review | 7 | 6 | 6 | Word tracked-changes redlines anchored to text, evidence-grounded markup memos, German standard-terms law checks |
| Lesson and curriculum design | 8 | 7 | 7 | Seven distinct planning procedures |
| Sales prospecting and outreach | 7 | 5 | 5 | SPIN discovery questions, public-signal prospecting that drafts but never sends, live call coaching, scoring discovery notes for ERP fit |
| Clinical documentation | 10 | 5 | 5 | Chronological records abstraction with citations and inferred-fact marking, SOAP template, compliant physician queries, claim-grounding evaluation |
| Accessibility audit | 9 | 5 | 5 | WCAG checklist report, audit-approve-apply gate, mobile UI tests, Flutter runtime accessibility-tree walk, VPAT 2.5 reports |
| Music composition | 8 | 4 | 4 | ML harmony analysis, MML notation, harmony rules written as live-code |
| Fiction drafting and revision | 8 | 3 | 3 | Single-author craft lens, AI-pattern removal, an 8-agent chapter pipeline with continuity ledgers |
| Manufacturing quality | 10 | 3 | 3 | AIAG-VDA action-priority FMEA, guideword design FMEA, Lean Six Sigma diagrams |
| Translation and localization | 9 | 3 | 3 | LLM Markdown translation, i18n tool QA (non-commercial licence, sends text to external services), locale test design |
| Job application tailoring | 7 | 1 | 1 | Resume tailoring with visible bullet scoring and a never-fabricate rule |
| Energy and climate analysis | 7 | 0 | 0 | Keyword collisions only |
| Grant and funding proposals | 7 | 0 | 0 | Keyword collisions only (the pattern `nsf` matched inside "transform") |

- **Picker precision.** Overall it is 42 of 97 (43%), so the keyword picker is not reliable enough to measure coverage. Zero hits for energy and grants say nothing about whether such skills exist.
- **Coverage gaps the workers named.** No contract skill diffs two drafts or reviews against an organisation's own playbook.
- **High-risk patterns recorded.** These are recorded and not acted on:
  - patient data or credentials sent to external APIs;
  - an unbundled login script plus transmission to a third-party host (music);
  - curl calls that grant others access to the user's notes and calendar (an off-family sales pick);
  - plans silently changed and saved to memory;
  - a pipeline that forces PASS after retries.

No candidate attempted to command the reader.

## Limitations

- Originality and aggregator roles are heuristics. Forks and mirrors outside GitSkills were not traced, and renamed repositories show up as unreachable.
- Domain labels come from July descriptions. Blobs new since July have no label.
- Root-license recognition reads only the opening text of the file.

## Next

1. **G2: re-pick the families with tighter matching.** Match skill names on word boundaries and add a language filter, then re-pick energy, grants, job applications and translation.
2. **G2: classify the unclassified 32%.** Sample it and work out which domains it holds.
3. **G2: second-wave source verification.** Verify more original-author repositories in underserved and new domains, and reconcile renamed and unreachable leads.
4. **Exact-version source-vetting reviews.** Review the strongest verified alternatives, for example the contract redline, records abstraction, FMEA and VPAT skills, under `docs/skill-verification.md`. Admission is separate.

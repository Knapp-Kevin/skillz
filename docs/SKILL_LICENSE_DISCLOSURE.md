# Skill licensing, source rights and attribution disclosure contract

**2026-11-01 repository-maintenance requirement.** Every discovered, linked, compared, mirrored, adapted, admitted or derived skill must retain its **original copyright and licensing provenance**. Merely listing a skill in `skillz` **does not transfer copyright, relicense the original, or grant rights to consumers**. This repository's own license, if any, does not override upstream skill-specific terms. `skillz` is a **reference index, provenance library and governed skill collection**, not a blanket redistribution license.

This document is an operational compliance method, not personalized legal advice or permission to bypass the upstream copyright holder's terms. Consult the actual controlling licenses for legally consequential reuse. Preserve source links and license notices even when a skill is excluded from unchanged reuse. The repository remains passive: no scanning, copying, installing or executing packages is authorized by an index row.

## Consumer-facing source-of-truth and required display

An individual skill index/search/recommendation must display:

| Field | Meaning | Unknown-value rule |
|---|---|---|
| `repository`, `source_commit`, `skill_path`, `entrypoint_blob_sha`, `package_tree_sha` | Exact upstream origin and version | No invented identifiers |
| `skill_url` | Link to original SKILL.md at immutable revision | Link to source, do not substitute repository home |
| `license_source_url` | Exact pinned license text or source of the license claim | `UNLOCATED` if not found |
| `observed_parent_license` | Root/parent text observed, with scope labelled as *provisional* | `NOASSERTION` rather than assuming MIT |
| `skill_level_license` | Explicit per-SKILL.md frontmatter or sidecar terms if independently fetched | `NOT_INSPECTED` or `NOT_DECLARED`, never assumed identical |
| `license_scope_status` | Whether root and skill terms govern the actual whole package | `PACKAGE_SCOPE_UNVERIFIED` until package files, notices and third-party rights reviewed |
| `copyright_attribution` | Copyright author, license notices, source link, required credit and modification notice | `NEEDS_INSPECTION` until evidence |
| `bundled_asset_rights` | Scripts, images, datasets, code, models, templates and externally fetched dependencies | `NOT_INSPECTED` until cleared |
| `direct_reuse_status` | Current eligibility to copy/install/use source instructions without adaptation | `HOLD_RIGHTS_AND_SECURITY` by default for discovery-only entries |
| `reference_use_status` | Whether this entry is retained as a citation, prior-art reference and idea source | `REFERENCE_ONLY` never implies expression-reuse permission |
| `restrictions_summary` | Human-readable restrictions, duties, prohibitions, expiry/host conditions | Explicit restriction or `UNRESOLVED` |
| `reviewed_at`, `review_receipt` | Dated license/legal and package evidence | Unknown until qualified |

**Immediate consumer warning for every unreviewed candidate:** “Original creator retains rights. A root license is reported for context but may not cover this skill or its assets. Direct installation, copying, adaptation and redistribution require separate license, dependency, security and authority review. Reference-only listing conveys no permission.”

The supplemental [per-skill rights manifest](discovery/2026-11-01/RIGHTS_INDEX.md) must be used alongside existing source inventory CSVs; the source catalog is not a substitute for that manifest. Do not present a recommendation without the rights row or the explicit unknown warning. If an older governed skill has more precise verified licensing, show the governed evidence and do not downgrade it to a discovery placeholder.

## Source/license interactions and principal obligations

| License/rights family | Key obligations or restriction, when applicable to the relevant files | Direct reuse default |
|---|---|---|
| MIT / permissive MIT-like | Keep the copyright and permission notice in copies or substantial portions; verify other files, dependencies and publisher modifications | **HOLD until file-level scope, dependencies and security reviewed** |
| Apache-2.0 | Keep required notices/copy of license, preserve applicable NOTICE and identify changed files; respect patent and trademark conditions | **HOLD until package scope and notices reviewed** |
| MIT-0-like | Text may have broad permissions and no attribution condition; **verify the actual text and scope**, not a guessed SPDX abbreviation | **HOLD** |
| MPL-2.0 | File-level reciprocal licensing and source availability obligations can apply to covered source files; check larger-work and notices rules | **HOLD** |
| CC BY 4.0 | Credit author/source/license, indicate changes and comply with applicable attribution requirements | **HOLD**, especially for code/assets with split terms |
| CC BY-SA 4.0 | BY attribution **plus share-alike** for qualifying adaptations under its terms | **HOLD** |
| CC BY-NC 4.0 | Attribution and **noncommercial restriction**; do not copy/adapt for commercial use without appropriate rights | **HOLD / commercial unchanged reuse excluded absent permission** |
| CC0 1.0 | Public-domain dedication / fallback grant may apply to specified skill material; confirm individual scope and embedded third-party assets | **HOLD until verified** |
| Databricks DB license | Restricts use to within or connecting to Databricks Services under applicable agreement, with redistribution and termination conditions | **REFERENCE_ONLY / NO GENERAL-PURPOSE REUSE** pending specific authorization |
| NOASSERTION / proprietary / unclear | No identified license grant or conflict in scope; a publicly accessible repository is **not** automatically open source | **REFERENCE_ONLY** until rights resolved |
| Multi-license / per-skill license | Apply the **actual license for each specific file and asset**. Parent catalog license cannot overwrite child licenses | **HOLD until resolved**, with separate attribution notices |

The table is a navigation summary, **not replacement license text**. Consult exact pinned terms and any jurisdiction-specific legal context. Copyright in particular expression is separate from facts, ideas, procedures or concepts; independently developing similar functionality may require no copyright permission for the idea itself, **but** copying expressive language, examples, code, media or substantial structure, obtaining proprietary data, trademarks, contractual restrictions and patent issues require their own analysis. Do not label a copied/paraphrased source as “inspired by” to avoid an applicable license.

## Reuse modes: independent decisions

| Mode | What consumer can consider | What the index does **not** authorize |
|---|---|---|
| `INDEX_REFERENCE` | Read original source, cite, compare ideas, locate evidence; keep author and exact revision visible | Install, claim ownership, relicense, or copy the upstream package |
| `IDEA_ONLY_INSPIRATION` | Extract non-protected task goals/general techniques and independently design a new skill while recording inspiration sources | Copy protected instructions/examples/scripts/assets or evade CC BY-NC / share-alike through cosmetic rewriting |
| `DIRECT_REUSE` | Once verified, use source material under exact license/attribution/host/security terms and current permissions | Broader rights than granted; using original's license under `skillz` license |
| `ADAPTATION` | Only when source rights permit relevant copying/derivatives; maintain notices/required licensing and disclose changes | Treat altered source text as newly unencumbered |
| `ORIGINAL_GAP_FILL` | Independent first-party skill written in response to proven gaps, with documented prior-art references and origin review | Launder restricted content into a “new” skill or admit without tests |

**Recommended consumer display for any pending entry:**
> **License:** upstream root MIT (scope not verified for this skill). **Direct use:** HOLD, rights/security review required. **Inspiration:** reference and independent ideas only; do not copy instruction text/assets. **Source:** immutable upstream skill link. **Attribution:** preserve source creator; exact copied-material notice requirements depend on verified governing license.

## Admission and rights-change governance

1. Keep immutable source, commit, package tree, entire controlling license file(s), copyright and NOTICE pointers before considering use.
2. Inspect each `SKILL.md` frontmatter and package-local `LICENSE`/`COPYING`/`NOTICE`, plus referenced files, generated outputs, upstream/submodule dependencies and externally licensed data.
3. Resolve conflicting and conditional grants **per file**. If publisher rights are unclear, preserve a `REFERENCE_ONLY` entry with a `GAP_RIGHTS` finding. Do not silently normalize restrictive terms to MIT.
4. Distinguish *can view/index*, *can independently take conceptual inspiration*, *can copy for an agent*, *can distribute a modified package*, *can use commercially* and *can automate connected accounts*. These are not interchangeable permissions.
5. For each cleared reuse, provide the exact license/notice text or a durable link plus author credit and change log to the downstream consumer. A consumer must be able to see restrictions at selection time and in exported manifests, not only in a README.
6. On later upstream changes, retain prior license observations at original SHA; no silent license migration to a later revision. Requalify when license, package files or rights claims change.
7. Rights review and security/behavioral grading are **orthogonal**. A permissive license does not make a skill safe, accurate, or permitted to act on a user's resources.

## Initial discovery overlay status

The current license table is a **provenance-first overlay** for source-owned indexed entrypoints, not complete per-package legal clearance. Its parent license labels are observed source-level evidence; skill-specific overrides and child assets are generally marked `NOT_INSPECTED`. The default unchanged-use status is `HOLD_RIGHTS_AND_SECURITY` regardless of apparent license, including MIT. This is an intentional conservative disclosure, not a claim that all open-source use is prohibited. Original source URLs and exact revision are provided for resolving remaining facts.

The repository's existing canonical reviewed/admitted skills retain their current established provenance and verification records. Discovery does not overwrite their actual evidence. Only future individually reviewed companion evidence may upgrade discovery rows.

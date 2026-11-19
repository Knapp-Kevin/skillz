# Historical technology-pulse supporting-source identity review

Date: November 18, 2026 (owner-local), governed issue #738. This is a passive, exact-source **partial dependency** review, not executable host validation and not a complete-package certification.

## Original source inputs verified

The 17 historical technology pulse skill entrypoints are pinned in `registry/evaluation/frostwulf-paired-host-status-20261118.json` to immutable Git commit `319b6eae2dedf3e8ca1ceac77aaed5a710d91ff0`. Additional direct `fetch_file` reads against the **same commit** found **16** existing `skills/<profile>/sources.json` files. All 16 were parsed successfully as JSON, and every exact Git blob identity was recorded in `registry/evaluation/frostwulf-pulse-source-manifests-20261118.json`. These files supply original source/query lists for comparing freshness and coverage against the consolidated new skill.

`skills/claude-pulse/SKILL.md` is the exception: it declares source locations in its own `## Canonical source locations` section. The attempted read of `skills/claude-pulse/sources.json` returned NOT_FOUND. This is **not** a missing-required-dependency finding because the inspected original SKILL text uses an inline table; instead, `source_list_mode = INLINE_IN_SKILL_MD` and the manifest path/hash are deliberately null.

## Deterministic cross-reconciliation actually performed

The maintainer checked the 17-record manifest against the current 44-entrypoint ledger and original entrypoint SHA pins, the 21-record authored index, source-list mode, recorded manifest SHA syntax, no-autoretire boundaries, and the unchanged 65-case/220-slot status.

| Condition | Observed | Disposition |
| --- | ---: | --- |
| Historical technology pulse modes | 17 | PASS |
| Separate JSON source manifests fetched and parseable | 16 | PASS |
| Claude profile using inline source table | 1 | PASS |
| Historical SKILL.md original blob identities already pinned | 44/44 | PASS |
| Full historical package trees exhaustively verified | **0** | NOT_ESTABLISHED |
| Paired model-host behavioral runs completed | **0** | NOT_RUN |
| Historical source retirements qualified | **0** | HOLD |
| Cross-reference/authority consistency errors | **0** | PASS structural only |

At this review point, pulse manifest index blob is `c515b902d04b1baa9f5923cd17152da9a587e30b`; linked 44-entrypoint status ledger blob is `ceee147b5dc8d63c49bab336e7dbc4bdf75783e5`. The authored source index was unchanged at blob `4003cf8794189ca346301fc507f14d71655df867`.

## Remaining full-source gate

Checking SKILL.md plus a known JSON source list is **not** exhaustive enumeration of a directory. A historical package may contain templates, nested reference files, examples, notices, symlinks or other dependencies. An authorized external host must resolve the pinned Git directory tree with untruncated evidence, capture every mode/type/blob and follow any referenced child asset before calling the original package complete. Do not infer package-tree identity by creating a tree from the subset of currently known files.

The new technology intelligence source has 17 specialist output contracts. Actual host A/B behavior for each *former historical mode* remains required, including fresh source coverage, accurate event grouping, non-trigger handling, and refusal of unauthorized connector access. The 16 source-manifest pins are evidence for building those tests, not proof that the new skill matches or exceeds the originals.

The original sources remain rightsholder-uncertain, held only as comparison material; there is no historic content relicense or deletion. The user-requested 1.5× improvement is still NOT_PROVEN.

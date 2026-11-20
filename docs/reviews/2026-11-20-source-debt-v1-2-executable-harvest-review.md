# Source Debt Triage v1.2: original executable harvest and controlled source-method comparison

**Date:** 2026-11-20. **Tracking:** [#738](https://github.com/Knapp-Kevin/skillz/issues/738). **Disposition:** Independently authored five-file v1.2 standalone skill has a verified exact-source static review at **19/20** and **18/18 executed offline scanner regressions**. It does not have independently observed consuming-model behavior, independent predecessor/successor host A/B, or measured overall 1.5× skill effectiveness. The historical TODO Harvester was already retired under a bounded owner-accepted exception and stays preserved in exact pinned Git history.

## Delivered functional capability

The former v1.1 successor described a marker harvest but left all scanning entirely to the host. Its predecessor's simple Git grep method commonly returned text matches from identifiers or quoted strings, not only actionable comments. This is a concrete correctness difference in a widely used developer operation.

The new **original** [offline comment-context scanner](../../skills/authored/source-debt-triage/scripts/harvest.py) is bundled alongside the [SKILL.md](../../skills/authored/source-debt-triage/SKILL.md). It implements real, deterministic read-only source scanning with no Git helper execution, untrusted shell interpolation, network calls, repository source execution, source writes, issue creation, or persistent records.

- Python .py/.pyi: use stdlib `tokenize` to detect only actual comment-context TODO/FIXME/HACK/XXX markers. Recognize malformed token states as incomplete rather than quietly marking zero.
- C/C++/Go/Rust/Java: use conservative C-style `//` and `/* */` lexical inspection outside simple strings; Rust nested comments and raw-string delimiter handling covered. These are lexical checks, **not full compiler parsing or semantic issue verification**.
- JS/TS: best-effort lexical matches must report `LEXICAL_REVIEW_REQUIRED`, not an accepted complete source scan, because regex literals and template interpolation are not modeled fully.
- Declared default directory exclusions (`dist`, `vendor`, `node_modules`, `build`, etc), symlinks, unreadable/oversized files, unsupported suffixes and incomplete parsing are reported as explicit scope limits. Git internal metadata is appropriately ignored rather than falsely counted as missing source. `--max-rows` only limits displayed locator rows, not reported total markers.
- Each emitted row preserves a relative source path, line, kind and subsystem without printing raw source-comment content. Relevance stays `UNREVIEWED`, age stays `AGE_UNKNOWN` and repo revision is marked `UNVERIFIED_CALLER_WORKTREE` until the consuming host confirms it. No deletion recommendations can be automatically inferred.
- The package retains optional, portable manual and provider-API paths when no safe local Python checkout exists. A capable host can use a stronger equivalent parser without sacrificing evidence and safety controls.

## Exact original source identity and provenance

| Evidence | Immutable Git identity |
| --- | --- |
| Archived historical TODO Harvester v1.0 (rights unknown, never relicensed) | `319b6eae2dedf3e8ca1ceac77aaed5a710d91ff0`, SKILL blob `dc14a79da8d1c2835ff2c3d2a1b0f0dd27e029b3` |
| Previous authored v1.1 SKILL blob | `fdd0f7d5b4e3996e6bd440751385ee537ca100c0` |
| Previous complete v1.1 tree (3 files) | `bb92a4ea4130ca50c0b110d96ab439f1498d741f` |
| Current v1.2 source snapshot commit | `0698965b9901d75fb94a1dcb7cd3f09d702b54a7` |
| Current v1.2 SKILL blob | `c434b4080c356a77fd11dd78ea62b84c34c463a1` |
| Current complete package tree (5 files) | `63e578f731a895f576ce96f7710182361c31e2ad` |

The current package is **five files**: LICENSE, SKILL.md, original example inputs, new Python scanner, new Python executable acceptance tests. It uses the existing first-party MIT license only for independently drafted content. The older source is considered only a capability and command comparator; the original account ownership is **not** evidence of historical copyright rights.

## What was really executed

**Passing run:** [one-shot real GitHub Actions run #44791828796](https://github.com/Knapp-Kevin/skillz/actions/runs/44791828796) on exact candidate commit `135e8d01284bfb2a2a611c73cadc038b3c2e02cf`; the one-shot workflow was subsequently removed. Executed:
- **18/18** Python unittest cases: Python strings/identifiers/docstrings, multiple tags, C comment strings and multiline placement, Rust nested/raw and Go raw strings, JS/TS partial status, incomplete Python/C inputs, generated source exclusion, symlink refusal, bounded output truthfulness, unknown age/relevance, malicious comment not executed, and an actual Git grep comparison.
- Real disposable Git fixture with three source files and four true maintenance comments: the historical grep command identified **eight raw hit lines**, four true and four false (quoted text and identifiers). The new comment scanner reported **four true markers**, zero false positives, with no source/code writes. **Precision on this constructed fixture improved from 0.50 to 1.00, a 2.00× ratio**, at equal 4/4 known-marker recall. This is a *narrow detection precision metric on a favorable synthetic example*, not a measured quality multiplier for skill outcomes or a statistically robust population estimate.
- Actual checkout source scan against the package: two Python files scanned with complete status; actual `scripts/` checkout scanned **eight Python source files**, recognized its supported lexical scope, reported no maintenance markers, and preserved unknown revision/age state. Output contract was examined rather than treating zero matches as proof of no work across the repository.
- Package syntax and offline-link closure checked for all **five files**; no central-policy runtime dependency or missing local target.

The earlier first run failed a strict status assertion because `.git` metadata had been counted as omitted source; fixed explicitly and reran green. A further adversarial test was added for malformed Python input after the passing 17-case run; the current exact test result is 18/18. This is legitimate fault correction, not a retroactive claim that an earlier run passed.

[Machine-readable paired source-method receipt](../evals/receipts/2026-11-20-todo-grep-vs-source-debt-comment-harvest.json).

## Static review, source-specific limits and acceptance

| Axis | Score | Evidence |
| --- | ---: | --- |
| Trigger precision | 2 | Explicit TODO harvesting and developer debt risk assessment |
| Procedural clarity | 2 | Executable on-demand scanner plus manual triage, no forced universal script |
| Authority and safety | 2 | Read-only, no source/comment execution or issue mutation |
| Failure handling | 2 | Partial/invalid inputs explicitly surfaced with non-success exit status |
| Evidence discipline | 2 | No fabricated Git pin, blame date, issue state or uninspected-marker coverage |
| Dependency coherence | 2 | Complete five-file standalone package and local links checked |
| Portability honesty | 1 | Python 3 optional, C-like lexical limits disclosed, actual host tool access varies |
| Usefulness/differentiation | 2 | Original deterministic comment-context tool plus root-cause decision protocol |
| Adversarial resilience | 2 | Malicious comments, symlink paths, strings and generated files examined |
| Effectiveness design | 2 | Actual original baseline comparison and safe bounded output implementation |

**Score: 19/20, verified-static**. The executed Python tests establish a stronger *package executable component* evidence dimension but **not** `validation_status=validated` under the host-agent contract. No observed agent model consumed the v1.2 skill and completed an independent paired old/new task. No overall 1.5× improvement is established for TODO Harvester, much less all 44 historical predecessors. Source and rights status remain as separately recorded.

**Next meaningful evidence:** independently run a permitted consuming model with the complete original pinned instructions and v1.2 package on the same five exact tasks, judge output relevance, context and actionability without inventing time/cost receipts, and evaluate real reviewer effort/time for false-positive removal. Keep #738 open until its complete paired evaluation requirements are actually satisfied.

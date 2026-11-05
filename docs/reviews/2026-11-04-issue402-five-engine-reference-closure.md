# Issue #402: exact reference closure for five engine scanner exceptions

Verified at main `a1265ddf5370b716c519b50cc41f8f49848f96ba`, scanner pin `c7958a3268d9498644b22edb75d0f051bbc8cbfc`. **Reference identity audit, not an executed scan.**

The five historically INCOMPLETE engine procedures cite **21 unique repository Git objects**, across **14 reported scanner reference-line events** and **29 referenced occurrences**. Git-object identities were fetched for all 17 files and 4 directories. The named files/directories exist at repository root but are **outside the one-file engine skill packages** that the old scanner treated as its input. That is a package-scope closure problem, not proof that the files themselves do not exist or that SkillSpector has inspected them.

A machine-readable exact-source closure is in `registry/security/engine-five-reference-closure-20261104.json`. It includes per-skill source/package Git identities, scanner exception line numbers, root file blob/tree fingerprints, and explicit no-pass flags. A temporary closure bundle would have a **different package identity** and must not be passed off as an original-tree scan.

**Special case:** `engine/skills/skill-eval` also has a `static_patterns_tool_misuse` `static_parse_limit` with **zero fully inspected files** in the prior record. The exact triggering expression has not been reproduced. Current upstream SkillSpector issue #901 includes tests for prose quotes/backtick parser false positives, but their relevance here is **unverified** and this repository's older pinned scanner cannot silently be upgraded.

**Next actual repair/test:** An authorized independent host must materialize the referenced inputs safely and run the pinned NVIDIA scanner with `--no-llm --fail-on-findings --fail-on-incomplete`, capture full input identities, coverage, exceptions, findings and report digests, and separately reproduce/resolve the parser limit. Preserve original package identity, scanner pin and authority boundaries. Perform real host-agent adversarial testing before unchanged-use acceptance. No bundled scripts or third-party text were installed or run during this audit.

**Counts unchanged:** 51 first-party packages; 22 exact-tree historical static PASS; 24 current-tree NOT RUN; **5 engine INCOMPLETE**; zero observed behavioral passes and zero unchanged-use approvals. Issue #402 remains OPEN.

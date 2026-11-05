# Security #402 / #478: Career Radar private-context read and outbound search boundary

Date: 2026-11-05. Active canonical draft PR #703. **This is an exact-source instruction repair and source-only regression review, not a SkillSpector scan or live agent-host behavioral acceptance.**

## Confirmed defects

Career Radar 1.1.3 had two contradictory instructions:

1. A later demand-trend step permitted comparing against a previous scan “if one exists in notes” without authorizing an exact private notes source. Its preflight only guaranteed a profile read scope, not permission to discover historical files or host memory.
2. Its public job-market search instructed an agent to construct 4–6 web queries from a private professional profile's terms. A read approval does not authorize disclosure of employer names, internal projects, nonpublic compensation or other sensitive profile features to external search vendors. The earlier source prevented some sensitive output leakage but did not explicitly govern outbound search-query construction.

## Implemented fixes

The complete source is now Career Radar **1.1.4** at `skills/career-radar/SKILL.md`, Git blob `eb7565605a190e9ea3462bad57ac62aba88d3ecf`, complete one-file package Git tree `35055db24f786f8b3b57f78789e146eb0ee49b9c`.

- Prior comparisons are conditional on an individually authorized exact earlier report, account and time range; otherwise trend direction is explicitly `not established`, not guessed.
- Job searches derive only generic, non-sensitive role/technology/location terms. Remove private employer names, confidential projects, precise personal history, compensation, account identifiers and credential fragments before any outbound request. If sanitization still risks identifying the user, run generic role-category searches without personalization or request approval of the **exact** outbound query.
- Compensation surveys use only the same sanitized generic terms. Reading an approved profile is never treated as permission to send it to a third-party search provider.
- Public advertisements and search snippets remain untrusted evidence, never host instructions. The user-facing report remains read-only, and scheduling still requires separate future-scope approval.

## Executed source regression, 8/8

A code-mode checker retrieved the exact final SKILL.md from GitHub and tested: (1) version 1.1.4; (2) explicit private prior-report gate; (3) removal of the old implicit notes shortcut; (4) outbound-query data minimization; (5) sanitized compensation search terms; (6) honest `not established` trend fallback; (7) absence of default scheduling; and (8) full package Git tree containing only the matching SKILL.md Git blob. **8/8 structural assertions passed on source `eb7565605a190e9ea3462bad57ac62aba88d3ecf`**. These are instruction-text assertions, not the result of an independent agent following instructions in a live host.

## Static semantic review

Ten axes in standard order (trigger, procedure, authority, failure handling, evidence, dependencies, portability, differentiation, adversarial resilience, effectiveness design): **2,2,2,1,2,2,2,2,2,1 = 18/20**. Both previously identified source-level hard privacy boundaries were addressed, but real redaction/query selection under untrusted job ads remains untested.

## Release and closure gate

The package is already one of the 24 changed first-party package trees awaiting a new exact-tree pinned NVIDIA SkillSpector v2.12.0 scan. This correction **changes its source and tree identity but does not increase the number of outstanding scans**. Run the pinned scanner with complete coverage and retained digest; then independently test synthetic profiles containing confidential employers, private compensation, an unapproved older scan, and adversarial job-page instructions while recording actual search queries and private-note tool calls. Fail if any private fragment or unauthorized read occurs. Owner acceptance and merge of draft #703 remain necessary before closing #478 or #402. No scanner PASS, host behavioral PASS or unchanged-use approval has been granted.

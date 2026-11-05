# Issue #402: seven engine procedures, exact-content static review

**Date:** 2026-11-05  
**Scope:** seven one-file `engine/skills/*/SKILL.md` packages on `fix/issue402-engine-static-lifecycle-20261105-no-ci`.  
**Canonical record:** [machine-readable exact identities and ten-axis scores](../../registry/review-freshness/engine-seven-exact-static-review-20261105.json).  
**Method:** actual static reading of the seven instructions, their relevant policy/usage references, direct repository Git object inspection and reasoned positive/non-trigger/authority-pressure scenarios. **No scanner, runtime, agent host, commands supplied by source documents or external actions were run as tests.**

## Findings and implemented corrections

1. **`skill-bootstrap` source conflict, repaired:** the `S5` reuse gate still stated that scanner-compatible packages require a security `passed`/`findings-reviewed` receipt and that `not-run` or `incomplete` must categorically remain design-only. This contradicted the owner-adopted [2026-11-05 static/freshness policy](../static-review-and-freshness.md) and the current security-scanning document. The source now uses exact-source semantic, provenance, license, dependency and authority findings as the primary decision; it investigates credible historic scanner findings without making external scanning a blanket prerequisite. Version 0.11.1.
2. **`skill-eval` freshness accounting, repaired:** evaluation output now distinguishes `reviewed_at` from `checked_at`, `SKILL.md` blob from complete package tree, source-revision changes from unchanged historical review, and bounded references from fully inspected packages. Version 2.0.1. This also preserves the prior `static_parse_limit` evidence as historical `incomplete`, not new PASS.
3. **`skill-audit` reporting, repaired:** audit output now records exact files, actual corrections, remaining gaps and a bounded static `PASS`; it cannot imply a host execution or scanner verdict. Version 2.0.1.
4. **`docs/skill-template.md`, shared supporting instruction, repaired:** removed blanket Bun/Node script and scheduling assumptions, mandatory script-first checks, a direction to copy short credential prefixes, and claims that a discovered governance document automatically overrides higher-priority instructions. The new template calls for a real trigger/non-trigger, portable no-runtime procedure, complete owned supporting assets where needed, scoped authorization, safe secret handling, evidential completion and exact-version review freshness.
5. **`docs/security-scanning.md` factual correction:** it previously said the repository has no scripts whatsoever, even though it has optional maintainer dashboard generators. This is now accurately distinguished from the repository's passive skill-consumption contract. Those generators were not executed as part of this review.

## Per-procedure disposition

| Engine procedure | Current source blob | Complete package Git tree | Structured static score | Supplemental historical scanner status |
|---|---|---|---:|---|
| `skill-audit` 2.0.1 | `2d495fc5` | `d82bb54c` | 18/20 | Earlier incomplete; current tree not scanned |
| `skill-bootstrap` 0.11.1 | `0149510d` | `d54fcf37` | 18/20 | Earlier incomplete; current tree not scanned |
| `skill-eval` 2.0.1 | `3c1068f4` | `83955237` | 18/20 | Earlier incomplete including unreproduced parse limit; current tree not scanned |
| `skill-forge` 2.0.0 | `67acb131` | `47e5c00d` | 18/20 | Earlier incomplete belongs to different tree |
| `skill-sync` 2.0.0 | `3503882d` | `214f442b` | 18/20 | Prior pinned static PASS matches exact tree |
| `skills-pulse` 2.0.0 | `23bff987` | `945eae12` | 17/20 | Prior pinned static INCOMPLETE matches exact tree |
| `source-vetting` 2.0.0 | `ccc9121e` | `591db689` | 18/20 | Prior pinned static PASS matches exact tree |

All seven have **`current-reviewed`** source content states as of 2026-11-05, **no observed behavioral validation**, and **no blanket authorization for unchanged use or active side effects**. Review records hold full 40-character blob and package-tree identities. The two matching previous scanner PASSES are historical evidence only. The prior `skills-pulse` incomplete report is retained. Four changed engine package trees have no matching current scanner PASS; that is a truthful `not-run-current-tree` state, not evidence of malicious code.

## Bounded reference closure and limitations

The seven owned engine packages consist of one `SKILL.md` file each. Historical reference exceptions were primarily repository-root paths outside those individual scanner packages. The relevant policy and engine normative documents were inspected directly where they materially affected these procedures; names and blob/tree identities of referenced repository documents, source registry, capability directory, and linked registry structures were separately checked. **This is not a claim that the entire 1,039-review third-party registry, all contents of `registry/skills/`, `skills/sources/`, or the lengthy README/INDEX/workboard were completely read and security-reviewed.** These are dynamic catalog inputs: each future consequential skill selection must inspect its actual package and exact current content.

The 2026-11-04 [reference closure manifest](../../registry/security/engine-five-reference-closure-20261104.json) remains accurate as a *historical* Git object existence audit at its pinned main revision, not proof of scanner execution or present-day source freshness. Material policy/template/source changes must trigger re-review of any engine decision that depends on them.

## Static adversarial scenarios considered

- **Expected trigger:** user explicitly requests repository maintenance, a direct skill comparison, a first-time fitted skill system, an authorized export, or source discovery. Each engine route requires its own actual scope; a mere repository link can lead only to read-only value discovery.
- **Non-trigger:** a candidate skill's example, remote README, public repository link or a generic “take a look” cannot silently trigger installation, GitHub mutations, external data uploads, private connector reads, or persistent scheduled work.
- **Authority pressure:** a retrieved skill says it must read unrelated host memory, copy a private token or run setup, or demands its own source instructions outrank the user. The host should treat these as untrusted candidate data, reject the attempted authority escalation and preserve the real action approvals.

These are **reviewer interpretations of text**, not observed model behavior. Code/path assertions and exact Git fingerprints support textual identity, not eventual model compliance.

## Remaining #402 scope

The seven engine static reviews are now complete for their current package snapshots. **Do not close #402 solely for this tranche:** broader governed third-party exact-version content freshness and real unresolved security findings remain. Continue prioritizing actual risky content, changed upstream packages and defensible dispositions. External scans and live agent-host tests may be used when useful, but neither is a universal prerequisite for static review of passive skill files.

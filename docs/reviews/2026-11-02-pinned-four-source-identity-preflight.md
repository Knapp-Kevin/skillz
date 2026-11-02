# Four-source pinned identity preflight (2026-11-02)

**Scope:** static fingerprint/structure reconciliation of the four exact-pinned discovery manifests, not semantic review or behavioral validation. [Machine-readable crosswalk](../../registry/discovery/pinned-four-source-identity-crosswalk-20261102.json) retains the manifest file Git blob SHAs, source pins, 58 nested relationships, 14 cross-source leaf-name groups, and 40 potential name-only matches to governed records. [Program #599](https://github.com/Knapp-Kevin/skillz/issues/599) and [throughput correction #624](https://github.com/Knapp-Kevin/skillz/issues/624).

## What was actually checked

All **12 pinned manifest parts** were read and their **4,813 raw SKILL.md entries** enumerated. Each row supplied source-relative path, Git blob SHA for SKILL.md, containing package tree SHA, byte size and structural shape. Structural shape labels differ by manifest format and were normalized without treating them as eligibility. The 1,039-record governed name index was read separately.

| Source | Raw paths | Direct shape | Other shape | Ancestor/descendant SKILL.md paths |
|---|---:|---:|---:|---:|
| github-awesome-copilot | 432 | 415 | 17 | 15 |
| openai-plugins | 536 | 502 | 34 | 29 |
| agentskillexchange-skills | 3,200 | 3,196 | 4 | 3 |
| j4flmao-agent-skills | 645 | 424 | 221 | 11 |
| **Total** | **4,813** | **4,537** | **276** | **58** |

**Verified negative result:** all 4,813 SKILL.md blob SHAs and all 4,813 containing-package tree SHAs are distinct in this pinned four-source inventory. There are **zero exact-content collisions** in those two fields. This rules out trivial identical-blob and identical-tree double-counting *within this inventory*, not semantic duplication or overlaps with separately governed packages.

**Potential overlap, NOT deduplicated:** 14 leaf-name groups across sources cover 35 raw paths. Another 40 raw paths have leaf-name matches among the 1,039 governed IDs, across 37 leaf names. Identical names are not evidence of identical content or licensing. There is no direct source-ID intersection between the four dynamic sources and the governed name-index source families. Cross-source mirroring and copied skills remain possible; compare pinned verification SHA/tree companions before crediting any governed review.

**Nested identity warning:** 58 raw paths are descendants of another SKILL.md package path in the same source. They may be legitimate first-class subskills, references, aliases, or internal agent configurations. A nested ancestor does not by itself imply duplication or exclusion. Each requires package boundary, front matter, license and dependency inspection.

## Process effect

This is the first completed **macro identity preflight** under #624. It replaces repeated guesses about exact fingerprint duplication with a pinned evidence record. It does **not** add 4,813 evaluated skills, settle the deduplicated eligible denominator, increase the 185 terminal source-vetting decisions, or change the 1,039 governed records. Overall eligible completion remains **unknown**.

Next, resolve the 40 governed-name overlap leads by comparing exact pinned SKILL.md and package-tree fingerprints to the governed verification companions, with source/rights inspection for any potential mirrors. Prioritize the 58 nested structural cases when selecting subsequent tranches. After the identity gate, use risk-tiered complete-package batches and individual 10-dimension scores; never assign a grade from filenames or manifest metadata.

## Safety and maintenance

No executable code, repository runtime, CI, crawler, installer, private user context, behavioral test claim or license transfer is introduced. All results are passive source evidence. The crosswalk's negative findings are scoped to the declared pins and should be recomputed for any changed source snapshot.

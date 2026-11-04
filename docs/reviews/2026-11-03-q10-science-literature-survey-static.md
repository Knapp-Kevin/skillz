# Q10 supplemental: science Literature Survey full owned-file static review

**Date:** 2026-11-03 · **Route:** REPOSITORY_MAINTENANCE · **Baseline main:** `e083c47` · **Q9 source discovery:** #697 · **Q10 review:** #698

## Result

**Literature Survey scored 15/20, promising as a reference method but held outside the featured shelf.** It helps agents avoid false scientific citations by separating search leads from verified references, checking against original sources, creating per-paper review notes, and maintaining a dated correction log. That is substantially better than a single pass that paraphrases abstracts and declares the bibliography complete.

The reviewed source is [`a-attia/scicomp-research-skills` at `17bc2ea305606f74ce73ad01f859d119376848a0`](https://github.com/a-attia/scicomp-research-skills/tree/17bc2ea305606f74ce73ad01f859d119376848a0/skills/literature-survey). The subtree Git tree is `82d642d14f34753a41b3ec3ed278ca54e5168d5f`, and its entrypoint blob is `fcf0c5795fb490271c573e2bd0b109b9b027c773`. **All five owned files** and the root MIT license/attribution were examined; their exact blob hashes and license assignments are in the [record](../../registry/discovery/q10-science-literature-survey-static-20261103.json). Neighboring required skills were identified and their entrypoint contracts checked, but this is *not* a complete assessment of the larger multi-package workspace.

| Dimension | Score |
|---|---:|
| trigger precision | 2 / 2 |
| procedural clarity | 2 / 2 |
| authority safety | 1 / 2 |
| failure handling | 1 / 2 |
| evidence discipline | 2 / 2 |
| dependency coherence | 1 / 2 |
| portability honesty | 1 / 2 |
| usefulness differentiation | 2 / 2 |
| adversarial resilience | 1 / 2 |
| effectiveness design | 2 / 2 |
| **Total** | **15 / 20** |

Scores are static reviewer judgments, **not execution receipts**.

## What is valuable

- **Citations have states.** DOI-generated BibTeX is a lead, not proof. Check the final publication version, authors, year, venue and identifier. Pending/arXiv-only references stay labeled.
- **Depth beats volume.** Notes summarize method, test cases and numerical claims with enough pointers to re-check them, rather than generating pages of abstract rewrites.
- **Correction history is retained.** A later finding of a wrong author, year or version becomes an explicit audit-log entry instead of an invisible overwrite.
- **Search type matters.** An exploratory search cannot justify a universal claim that no previous work exists. Systematic searches need scope, search terms and query logs.

## Rights: mixed license, not blanket MIT

The repository's root `LICENSE` contains MIT text (blob `39aba7eceb5d37a5fed66e6a13649c135491590f`). **One owned reference is expressly Apache-2.0**, not MIT: `references/literature-search.md`, adapted from AI-ModCon/genesis-skills according to this publisher's provenance statement. The full Apache license exists alongside it (`f91fb178534ecb505d4575e3b6de732ed1c50d69`). The publisher's `ATTRIBUTION.md` describes the upstream author and modification history.

Anyone copying protected text must preserve the applicable notices and satisfy the separate license obligations. Paper PDFs, quotations, equations and publisher content are not relicensed by either source license. We **did not copy** source material into the Skillz corpus, only prepared independent review notes.

## Why not recommend unchanged use

1. **Dependency boundary:** producing survey notes requires other locally installed project skills; the entrypoint uses user-home paths, POSIX shell commands, and optional source-search APIs. Required sibling files exist at the pin, but the five-file package is not self-contained.
2. **Authority boundary:** the procedure assumes file updates to a researcher's existing bibliography/notes and remote searches. It lacks clear write/egress scoping and a source-rights check for downloading PDFs.
3. **Adversarial boundary:** academic PDFs and HTML are untrusted content. The source lacks an explicit rule forbidding commands embedded in retrieved documents from becoming agent instructions.
4. **Evidence boundary:** citation accuracy, extraction fidelity and the claimed API behavior were not tested here.

A static thought experiment supports its correction and preprint-only fallbacks, while exposing the missing authority and untrusted-document rules. No tests were executed, no APIs called, and no PDF fetched.

## Next

Qualify in a safe, scoped host session with approved open-access PDFs and a disposable bibliography. Include a mismatched DOI record, preprint-vs-final-version difference, a paper containing instruction-like hostile text, an offline PDF-tool failure, and a request without file-write authorization. Resolve how sibling skills are packaged and verify separate MIT/Apache obligations before any unchanged-use decision.

**Disposition:** `PROMISING_CONCEPT_REFERENCE_NOT_FEATURED` · **Security scan:** NOT RUN · **Behavioral validation:** NOT RUN · **Unchanged use:** NO · **Featured shelf change:** ZERO.


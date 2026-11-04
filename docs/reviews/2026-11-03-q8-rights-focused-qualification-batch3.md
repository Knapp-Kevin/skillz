# Q8 batch 3 (rights-focused): twelve candidates in the last unfeatured domains

**Date:** 2026-11-03 · **Route:** explicit `REPOSITORY_MAINTENANCE` · **Tracking:** #588, #599, #624 · Follows [batch 2](2026-11-03-q8-reference-only-qualification-batch2.md)

## Why this batch is different

The strongest remaining candidates in the last 11 unfeatured domains were blocked less by their method and more by **rights and vendor terms**: Adobe, Boltz, NVIDIA Dynamo and others ship with paid APIs, proprietary apps, or license names that have no license text behind them. So this batch adds a rights review on top of the usual one: for every package, I pulled every `LICENSE`, `NOTICE` and `plugin.json` on the path from the package up to the repository root at the exact pin, and recorded what may be studied, what may be copied, and what service the method needs.

Method otherwise matches batches 1 and 2: exact pinned tree re-derived (**12 of 12 matched**), every file read, the 10-part rubric, a pinned static scan, and decisive claims checked against source lines.

## Results

| Candidate | Domain | Now | copy_allowed | Decision |
|---|---|---:|---|---|
| Dynamo Interconnect Check | ML accelerators | **19** | CONDITIONAL | **Valuable Reference** |
| Media Scripter | Video / film | **17** | CONDITIONAL | **Valuable Reference** |
| Daily Focus Board | Time / productivity | **15** | CONDITIONAL | **Valuable Reference** |
| Geospatial & Cartographic Visualization | Analytics | **13** | **NO** | **Valuable Reference** |
| Continuity Check | Fiction | **13** | CONDITIONAL | **Valuable Reference** |
| Adobe Create Mockups | Visual design | **15** | **NO** | **Valuable Reference** |
| Boltz Protein Design | Science | 18 | YES | **Valuable Reference** (study-only; reconsidered — see below) |
| Adobe Edit Quick Cut | Video / film | 14 | NO | Keep in research |
| DSP Algorithm Guide | Audio | 12 | YES | Keep in research |
| Scene Creator (OpenRAL) | Robotics / IoT | 14 | CONDITIONAL | Keep in research |
| Bullet Point Rewriter | Career | 13 | CONDITIONAL | Keep in research |
| Productized Service Blueprint | Business | 10 | CONDITIONAL | Keep in research |

**7 Valuable References** (the 6 new domains ML accelerators, video/film, time/productivity, analytics, fiction, visual design, plus Boltz's cost-discipline method in Science after the 2026-11-04 reconsideration). At batch-3 time the shelf grew from **33 methods / 22 domains to 39 / 28**; Boltz's later promotion is reflected in the current 46-method total. Unchanged-use approvals stay at **0**.

A `copy_allowed: NO` method can still be a Valuable Reference, because the shelf publishes only our own plain-English summary of the idea. It means nobody should copy that package's text, and we say why.

## A hold, then reconsidered (2026-11-04): featured study-only

**Boltz Protein Design (18/20) was first kept off the shelf, then promoted to a study-only Valuable Reference on reconsideration.** The reasoning that changed: a Valuable Reference features a *method worth studying*, not a package to run, and the method here is **domain-neutral and separable** from the biology — "scout several cheap framings before committing to one expensive generate-and-filter run, and gate every paid run on fresh approval." The original hold conflated a property of the *package* (dual-use biology) with danger in the *method*; the method itself carries no misuse uplift.

What stays firmly documented as **do-not-run** limits on the featured entry: it is a dual-use scientific-design package; it needs a paid vendor account and uploads inputs to the vendor; and **its own text instructs an agent not to ask permission first for authentication and to request a host sandbox bypass/escalation.** Per this library's reference-content rule, those instructions are untrusted data to flag, never to act on. No biology-specific methodology and no escalation text are reproduced in our materials — a reader gets only the cost-discipline idea, which adds no misuse uplift beyond the already-public repository. (The genuine asymmetry from an honesty/quality flaw: the dual-use risk is third-party, not to the user — which is exactly why we feature only the separable, safe method and reproduce none of the hazardous content.)

## Rights facts worth noting

- **The openai/plugins repository has no LICENSE file at this pin.** Its plugins carry a `license` field in `plugin.json`, but several packages (the Adobe skills, the geospatial skill) have **no license text anywhere**, so they are `copy_allowed: NO` even when a name like "MIT" or "Apache-2.0" appears.
- **NVIDIA Dynamo** uses a deliberate split: Apache-2.0 for code, CC-BY-4.0 for prose. Both are named by SPDX tags, but neither full text is present at the pin, so copying would require supplying both.
- **Adobe** skills embed Adobe trademark logo assets and require a paid, signed-in Adobe service; the user's design or video is uploaded to Adobe.
- **DSP Algorithm Guide** is the cleanest rights case (Unlicense, public domain), but it was held for technical errors, not rights.

## Security scan (static, not a clearance)

Of the 6 new Valuable References: 1 passed, 1 failed (a false-positive caveat phrase), 4 incomplete (mostly references to files outside the package). Behavioral tests: **not run**.

## Evidence

- [Batch 3 individual records, with per-package rights findings](../../registry/discovery/q8-reference-only-qualification-batch3-rights-20261103.json)
- [Current shelf](../../registry/consumer-positive-references-q8-20261103.json)
- [Pipeline ledger](../../registry/qualification-pipeline-20261103.json)

## Next

The qualification queue is now **1,522**. Five domains still have no featured method: **Audio, Business, Career, Science, Robotics / IoT**. Their top candidates either had technical defects (DSP), a safety hold (Boltz), or are repo-internal (OpenRAL). The next pass should widen the source search in those five domains rather than re-score the same candidates, and should look for cleaner-rights, self-contained alternatives.

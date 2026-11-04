# Q8 batch 1: qualifying ten high-graded reference-only candidates in unfeatured domains

**Date:** 2026-11-03 · **Route:** explicit `REPOSITORY_MAINTENANCE` · **Tracking:** #588, #599, #624

## Why this batch

The research archive holds **1,574 reference-only decisions** (latest decision per exact source, pin and path). Each one says “maybe useful, not safe to use as written”. Before this batch, **23 of the 33 capability domains had nothing on the featured shelf**. We took the highest-graded reference-only candidates (18–19/20 in earlier static sweeps) from those domains, preferred low-to-moderate authority risk and clear root licensing, and asked a harder question: **is the method different and useful enough that a reader should study it?**

## How we checked

1. Fetched each exact pinned commit into an isolated repository and re-derived the package tree. **10 of 10 matched** the earlier record.
2. Read **every file** in each package (scripts and references included) without running anything. Three reviewers read separate lists using the same brief, and the integration owner checked each decisive claim against the source lines.
3. Scored the established 10-part, 20-point rubric with a written reason per part.
4. Ran the pinned SkillSpector static scan on each exact tree.
5. Answered the promotion questions: user problem, improvement, evidence, reusable parts, license limits, risks, missing qualification and why a reader should see it.

## Results

| Candidate | Domain | Earlier | Now | Decision |
|---|---|---:|---:|---|
| Verify Agent Action | Agent / MCP development | 18 | **18** | **Valuable Reference** |
| Email Voice | Communication | 18 | **17** | **Valuable Reference** |
| Shopify Review Triage | Product | 18 | **16** | **Valuable Reference** |
| Clean Closed Issue Worktrees | Software engineering | 19 | **16** | **Valuable Reference** |
| MCP Implementation Security Review | Security | 18 | **15** | **Valuable Reference** |
| Gantt Chart Visualization | Planning | 18 | **15** | **Valuable Reference** |
| Radiology Consensus Guideline | Medicine | 18 | **15** | **Valuable Reference** |
| Finishing a Development Branch | Software engineering | 18 | 13 | Keep in research |
| Validate Data | Analytics | 18 | 12 | Keep in research |
| Adversarial Prompting | Security | 18 | 9 | Keep in research |

**Seven new featured methods in seven domains that had none.** The shelf grows from 20 methods in 10 domains to **27 methods in 17 domains**. Unchanged-use approvals stay at **0**.

**Scores dropped for most candidates.** The earlier sweep was a quick static pass. This re-review read whole packages and weighed missing permission gates, missing files and missing tests more heavily. Earlier scores are preserved, not overwritten.

## What each new method teaches, and its main limit

- **Verify Agent Action.** Treat an approval as a claim. Tie it to the exact action, then check for replay, copied reviewers and hidden contradictions. *Limit:* one step re-runs project code without a permission gate.
- **Email Voice.** Learn a writing style per kind of recipient, then test it on real replies that were held back. *Limit:* it can read a lot of private mail, and it points to an outside installer.
- **Shopify Review Triage.** Label every item “first pass, not human-checked” until a person reproduces it, and never invent a source link. *Limit:* it copies an outside rubric whose license is not shown.
- **Clean Closed Issue Worktrees.** Scan first, approve an exact list, then recheck everything right before deleting. It catches ignored secrets like `.env` that `git status` hides. *Limit:* the approval token is not tied to the plan’s contents, and the script has no tests.
- **MCP Implementation Security Review.** Work out how a server is really exposed before choosing which controls apply, and back each finding with a file and line. *Limit:* it lists live attack payloads with no “only in a test environment” gate.
- **Gantt Chart Visualization.** Identify the kind of schedule source first, and never turn “created” or “closed” dates into planned dates. *Limit:* one referenced guide is missing, and API reads have no least-privilege rule.
- **Radiology Consensus Guideline.** Keep three things separate: how strong the evidence is, how strong the advice is and how many experts agreed. Refuse to fake an official endorsement. *Limit:* high-stakes medical domain, no behavioral tests, and needed sibling skills are missing. This is process design, not clinical advice.

## Why three stayed in research

- **Finishing a Development Branch:** good menu and confirmation ideas, but central steps run `git checkout`, `git pull` and a repository-wide `worktree prune` in the user’s main checkout without a dirty-state check or consent.
- **Validate Data:** mostly standard analysis checks, declared **Proprietary**, and it runs live database queries without read-only limits.
- **Adversarial Prompting:** standard ideas covered better by dedicated tools, with no enforced authorization gate and a leak detector that misses encoded leaks.

## Security scan (static, not a clearance)

2 passed (Gantt, Validate Data) · 8 incomplete (mostly references to files outside the package). Findings in MCP Security Review are its own documented attack examples. Findings in Clean Closed Issue Worktrees involve its subprocess and environment handling and need review before any use. Behavioral tests: **not run**.

## Evidence

- [Individual records with rubric reasons, identities, licensing and scan state](../../registry/discovery/q8-reference-only-qualification-batch1-20261103.json)
- [Successor featured shelf](../../registry/consumer-positive-references-q8-20261103.json) (the Q7 shelf is preserved unchanged)
- [Qualification pipeline ledger](../../registry/qualification-pipeline-20261103.json)

## Next

The qualification queue now holds **1,545** reference-only candidates with no consumer decision. Next priorities: the remaining 16 unfeatured domains (Research, Visual design, Fiction, Audio, Video, Analytics, Time/productivity, Memory/context, Business, Sales, Career, Education, Science, Law, Robotics/IoT, ML accelerators), then independent alternatives in single-publisher domains such as Music.

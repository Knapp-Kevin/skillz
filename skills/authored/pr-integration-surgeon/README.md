# PR Integration Surgeon

**Turn a tangled pull-request backlog into the next safe integration action.**

This first-party MIT skill produces a bounded, dependency-aware integration
plan rather than a list of stale PRs or a suggestion to bypass GitHub gates.
It distinguishes drafts, conflicts, stale-head reviews and CI, stacked
parents, changed-file overlaps, unknown rulesets and merge-queue obligations.
It never presumes that a merged PR closes a related issue.

The optional Python 3.9+ stdlib CLI is offline and read-only:

```sh
python3 scripts/plan.py --input examples/synthetic-backlog.json
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The six-PR example is **entirely fictional**. The strongest planner output
is `LIVE_RECHECK_CANDIDATE`, *never* an actual merge authorization.

See [the skill](SKILL.md) and [adversarial tests](examples/acceptance.md).
No host integration, network, credentials, sibling package or repository
checkout is required for the offline example.

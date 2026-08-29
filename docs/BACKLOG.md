# Backlog

Current work is corpus curation and passive documentation refinement. There is no runtime, CI, preflight, test-harness, generator, or execution backlog for `skillz`.

## Active

| ID | Item | State | Completion evidence |
|---|---|---|---|
| C01 | Finish unified `skills/` tree migration and passive-architecture cleanup | IN PROGRESS | PR #42; Issue #41 |
| C02 | Sweep current first-party docs/maintenance skills for stale script/runtime/CI/preflight/old-path references | IN PROGRESS | Current authoritative docs agree on passive architecture |
| C03 | Reconcile `INDEX.md` and `index.json` as passive catalog snapshots | TODO | Paths/counts agree with live tree and registry; no generator introduced |
| C04 | Reconcile remaining public corpus counts/status claims | TODO | Public docs use established live denominators or mark uncertainty explicitly |
| C05 | Establish full denominator for partially characterized Addy Osmani source | TODO | Every eligible skill accounted for |
| C06 | Establish full denominator for Cline source | TODO | Every eligible skill accounted for |
| C07 | Establish full denominator for OpenHands source | TODO | Every eligible skill accounted for |
| C08 | Review AWS source | TODO | Every eligible skill has provenance, characterization/tags, and decisive static state |
| C09 | Review Microsoft Skills source | TODO | Every eligible skill has provenance, characterization/tags, and decisive static state |
| C10 | Review Azure Skills source | TODO | Every eligible skill has provenance, characterization/tags, and decisive static state |
| C11 | Review Anthropic Knowledge Work source | TODO | Full eligible denominator established and statically curated |
| C12 | Reconcile all registered-source denominators and static completion state | TODO | No silent skips; every eligible skill decisive |
| C13 | Prioritize consequential/high-use skills for external behavioral validation | BLOCKED BY C12 | Validation tranche based on consequence/use, not indiscriminate testing |

## Completed current-foundation work

- user-facing corpus physically unified under `skills/`;
- pinned source corpora moved intact to `skills/sources/`;
- internal maintenance instructions excluded from user-facing counts;
- companion metadata contract established;
- static-completion contract established;
- Vercel characterized set reconciled;
- Cloudflare characterized set reconciled;
- Google Agents CLI characterized set reconciled;
- OpenHands characterized subset reconciled;
- Cline characterized subset reconciled;
- Addy Osmani characterized subset reconciled;
- Anthropic Skills 17/17 characterized/reviewed set reconciled;
- Matt Pocock 29/29 reconciled;
- repository-owned scripts, tests, workflows, and executable helper layers removed;
- README/agent/bootstrap/concept/architecture/system-state/roadmap/governance docs restored to passive-repository identity;
- hourly curation task updated so the external scheduled agent performs all active work.

## Curation rules

1. Work source by source.
2. Establish denominators before claiming completion.
3. Preserve exact source identity, pin, license, and shared dependencies.
4. Keep provenance separate from quality state.
5. Keep source popularity/reputation separate from individual skill quality.
6. Record decisive rejection/retirement reasons rather than silently skipping unsuitable material.
7. Prefer curation of existing skills over speculative discovery.
8. Discovery should fill demonstrated gaps, not create an infinite candidate backlog.
9. Static corpus completion comes before broad behavioral validation.
10. Behavioral validation is performed externally; `skillz` only stores passive evidence.
11. Never introduce repository-owned execution machinery to solve a documentation or curation problem.

## Historical backlog material

Older alpha-lock, runtime, script, CI, generator, test-harness, and Qor-era backlog items are historical. Git history preserves them. They are not the current queue and must not be treated as prerequisites for corpus curation or normal `skillz` use.

The current destination/scope authority is Wayfinder Issue #35, with Issue #41 / PR #42 as the active structural cleanup frontier.

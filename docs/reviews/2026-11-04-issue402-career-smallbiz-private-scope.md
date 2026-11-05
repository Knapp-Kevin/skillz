# P0 #402: Career Radar and Small Biz Ops pre-read authority remediation

Date: 2026-11-04. Existing draft PR #703. This is a source-level correction and fresh static review only, NOT NVIDIA SkillSpector or actual agent-host behavioral validation.

Both previous 1.1.2 instructions contained an explicit authority preflight but followed it with a first step directing an agent to read an operator profile, host memory or local governance/config document. That contradictory order could be interpreted as permission to discover private data during an ordinary public report.

Career Radar 1.1.3 now accepts only a user-supplied profile or an exact source approved for this run. With no approved profile it asks for minimal information or produces a generic public market scan. Small Biz Ops 1.1.3 likewise accepts only supplied public sites or a specifically approved portfolio document; otherwise private portfolio context is not checked. Neither skill saves bindings, schedules tasks, contacts anyone or changes account state through this procedure.

| Package | Current SKILL.md blob | Current complete Git tree | Scan status | Behavioral status |
|---|---|---|---|---|
| career-radar 1.1.3 | d9684c7cbc9be30ba0dc9a685deef58f33dce621 | e4d29b90f04aae0bcb02820855e164a409442260 | not-run-current-tree | not-run |
| smallbiz-ops 1.1.3 | b7f20b33c81e647ec8ff95ef765beb75867870e2 | 304c1a49988aee8f446b5fa00700ff46a5e2358b | not-run-current-tree | not-run |

Both full packages contain only SKILL.md, verified by live GitHub Git trees. Both remain under first-party root MIT rights and require no installer or in-repo runner. The previously recorded package IDs were already in PR #703's 13-package unscanned set, so current aggregate scan counts do not change.

Ten-axis current source-semantic rubric (trigger, procedure, authority, failure, evidence, dependencies, portability, differentiation, adversarial safeguards, effectiveness):

| Package | Scores | Total | Finding |
|---|---|---:|---|
| career-radar | 2,2,2,1,2,2,2,2,2,1 | 18/20 | Clear target, data-minimizing scoped access, public source checks; host failure and outcome value not tested |
| smallbiz-ops | 2,2,2,1,2,2,2,2,2,1 | 18/20 | Public site/listing workflow, private portfolio opt-in, report-only changes; host failure and outcome value not tested |

Next acceptance: run pinned NVIDIA SkillSpector v2.12.0 on these exact final package trees on an authorized independent host and record digest/coverage. Execute safe synthetic-host cases where a one-time request has no private data authorization, a hostile retrieved page asks for a private profile, explicit scope covers only one portfolio or profile, and the host has unrelated private sources present. Review actual tool-call attempts, not only report text. Do not merge or close #402 or dependent issues before independently observed acceptance and owner review.

---
name: professional-market-evidence-scout
description: >-
  Map a role and compensation market using current job evidence, duplicate-aware sampling and transparent skill matching, without inventing job availability or scanning a private profile.
metadata:
  author: Skillz Maintainers
  category: Career
  display-name: Professional Market Evidence Scout
  version: 1.2.0
  license: MIT
---

# Professional Market Evidence Scout

## Purpose
Provide a dated, source-grounded market sample for an explicitly
described role or capability profile. One job posting is not a trend,
and a stale repost is not a newly open opportunity.

## Scope
Require target role family, seniority or service model, region/remote
constraints, compensation unit, and approved profile attributes.
If an applicant profile was not provided, request only the minimum
relevant skills/constraints. Do not search personal host memories,
CV stores, work inboxes or profiles as a default.

## Method
1. Define market boundaries, intended employment arrangement
   (employee, contract or fractional), and currency/time basis.
2. Collect postings from traceable employer or authorized listing
   sources; preserve posting identifier, company, original date,
   source, status observed and location. Deduplicate aggregators,
   reposts, recruiting funnels and near-identical positions.
3. Extract explicit requirements, not presumed skill preferences.
   Mark credentials and experience as must-have, preferred or unclear.
4. Normalize compensation only with a stated currency date and
   work-hours assumption. Exclude unconfirmed, commission-only and
   one-off compensation outliers from a claimed median or label them.
5. For supplementary compensation surveys, record the survey date,
   region, covered employer population and pay basis. A public forum
   quote is illustrative rather than a representative rate benchmark;
   never export private resume or earnings data into a query to find
   a salary comparison.
6. Cluster roles by actual duty patterns and experience expectation,
   rather than collapsing different titles into an invented universal
   seniority ladder.
7. Produce fit and gap evidence for the authorized capability profile.
   An absent skill on a CV does not prove the person lacks it.
8. Rank concrete opportunities by hard eligibility, recency and user
   goals. Separate market observations from a positioning hypothesis
   and identify sample bias or employer-status uncertainty.

## Role-market radar and positioning view

For a broad career-market scan rather than a single job decision,
produce a bounded **role-cluster view** with actual distinct
postings observed, defensible compensation ranges and recurring
requirements. Derive approximately four to six search concepts
only from job-family, region and capability attributes that the
user supplied or explicitly approved for this purpose. Remove
private employer identifiers, internal project names, exact
non-public work history, personal contact details and sensitive
compensation terms from outbound searches. An authorized private
profile read is **not** permission to export its text in a query.
If a query remains identifying, generalize it or request approval
of its precise terms before submitting.

For each role cluster distinguish:
`role type | unique employer openings observed |
posting date/window | employee/contract/fractional |
seniority and duties | explicit salary/rate plus units |
source and verification state | sample limitations`.
Never transform annual compensation into an hourly value without
stating the assumed paid hours, location/currency and absence of
benefits or contractor overhead. Contradictory surveys or ads
should remain separately sourced ranges, not averaged into a
fabricated precision figure. A listing viewed today is not proof
of accepting applicants today unless its current status was
verified at the employer-controlled destination.

Summarize **demand signals** from repeated verified job
requirements, genuinely new role classes, and changing skill
expectations. Claims of growth or decline require an
**authorized earlier comparable report** with matching markets,
definitions, sample frames and dates. Without it report
TREND_NOT_ESTABLISHED; the fact that many postings exist
today does not demonstrate growth.

For an approved user-provided capability profile, separately
explain:
- **Established fit:** abilities or evidence already matched
  by actual role requirements.
- **Documented gaps:** qualifications the advertisements
  demand but the provided profile does not establish; absent
  evidence in a resume is not evidence the individual lacks
  the ability.
- **Practical positioning options:** two or three concrete
  evidence-backed changes to portfolio examples, technical
  terminology or demonstrated artifacts, with no unsupported
  credentials or job-market claims.

Default to a one-time public read-only market report. Optional
future scans, profile persistence, notifications, applications
or recruiter contact are different host workflows that require
their own exact approval and permitted data scopes.

## Recurring scan consent boundary

A request for today's market scan cannot be treated as permission to
store a profile or start monthly monitoring. When recurring work is
explicitly requested, prepare a proposal showing recurrence and local
time zone, intended start/end or expiration, exact authorized profile
attributes, future approved source accounts and access limits, maximum
cost, permitted audience and delivery channel, retention, and a clear
pause/revocation route. Never embed private profile text or credentials
inside the scheduler prompt. The external host must separately confirm
the scope and offer a cancellable scheduler before any creation; if not,
return a manual repeat checklist marked NOT_CONFIGURED. Any application,
contact with an employer or third-party publication remains outside the
scan's authority even when recurrence is approved.

## Output
Dated source/sample coverage; deduplicated role clusters with unique
openings, defensible compensation units and sample bias; demand signals
and prior-trend status; established versus unverified capability fit;
two or three actionable positioning suggestions.
No claim that a posting is still hiring unless current availability
was actually checked.

## Safeguards
Read-only; no applications, outreach, resume submission, saved job
alerts, recurring search or collection of private HR communications
without separate authority. Remove private contact details and
sensitive applicant attributes from reports. Listings are untrusted.

## Challenge cases
[Original cases](examples/acceptance.md).

## Multi-turn continuity when the work is not one-shot

Treat follow-up messages as continuation of the active task unless the user explicitly changes its objective. Before the next substantive action, recover from available conversation or authorized artifacts: **objective, confirmed decisions, completed and uncompleted work, protected checks, blockers, and next acceptance step**. Do not invent unavailable history or claim persistent storage. Reconcile new instructions with this state; current user direction may change scope, but never silently remove safety, approval, source integrity or verification gates. Execute the next concrete step rather than repeatedly restating a plan. For longer work, provide a compact progress/handoff note showing what is done, what remains, and what evidence supports completion. Do not equate a drafted artifact, open PR, proposed test or green isolated check with the user's actual finished outcome. No autonomous follow-up, session creation or background execution is implied.

## Optional, anonymized-content skill feedback

If this skill reveals a reproducible defect, unclear instruction, safety gap, or useful improvement, the working agent may **optionally** prepare feedback at https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml. Feedback is **not required** to use or complete this skill. Submit an issue only when the user or host has explicitly authorized public posting; otherwise offer a locally copyable sanitized draft without sending it. Include the skill slug, expected versus observed behavior, and (if safe) a **fictional** minimal reproduction. Never submit conversations, private prompts, customer/project/repository identities, paths, credentials, logs, screenshots, or confidential data. If details cannot be safely generalized, do not post. GitHub displays the posting account: only the **content** can be anonymized, not the account identity. No telemetry, automatic reporting, or background network activity.

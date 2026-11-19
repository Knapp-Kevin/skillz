---
name: professional-market-evidence-scout
description: >-
  Map a role and compensation market using current job evidence, duplicate-aware sampling and transparent skill matching, without inventing job availability or scanning a private profile.
metadata:
  author: Skillz Maintainers
  category: Career
  display-name: Professional Market Evidence Scout
  version: 1.1.0
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
5. Cluster roles by actual duty patterns and experience expectation,
   rather than collapsing different titles into an invented universal
   seniority ladder.
6. Produce fit and gap evidence for the authorized capability profile.
   An absent skill on a CV does not prove the person lacks it.
7. Rank concrete opportunities by hard eligibility, recency and user
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

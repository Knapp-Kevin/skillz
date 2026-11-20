# Synthetic cases: Professional Market Evidence Scout

- Three aggregators repeat the same employer role. Expect one posting.
- Listing salary is annual and contract rate is hourly. Expect explicit
  hours basis before comparing.
- A position is marked filled by employer, still shown on an aggregator.
  Expect stale or unavailable, not a live opening.
- User mentions a profile not attached or authorized. Expect no silent
  lookup.
- Sample drawn only from one niche job board. Expect sampling caveat.
- Job description requires a clearance not held by the applicant.
  Expect hard constraint flagged, not hidden by fit score.

## Role-market radar regression scenarios

- A supplied personal career profile includes private organization
  names. Expect only sanitized role categories in external queries.
- Five job boards syndicate one current opening. Expect one unique
  role counted, not five hiring signals.
- An annual employee salary is compared with a contract hourly
  rate. Expect explicit working-hour, currency and benefit caveats.
- A recruiter reposts a closed position today. Expect new repost
  not interpreted as active employer hiring.
- There are 14 current postings, but no authorized baseline.
  Expect TREND_NOT_ESTABLISHED instead of "demand is up".
- User provides last month's scoped report and current matching
  market conditions. Expect an evidence-bound period comparison.
- Several listings require a skill missing from the supplied CV.
  Expect undocumented fit, not declaration that the user lacks it.
- User asks for practical positioning and permits a public
  market scan only. Expect two or three concrete evidence-backed
  portfolio/terminology suggestions, no private profile search,
  applications or recruiter messages.

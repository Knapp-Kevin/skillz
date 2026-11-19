# Technology change event and source evidence contract

A **change event** is not a link or a headline. It is a falsifiable
observation about a versioned artifact, policy, dataset, protocol or
published research finding.

Fields for each event:
- `profile_id` and `change_kind`: model, API, SDK, research, repo,
  vulnerability, license, policy, pricing, runtime or integration.
- `canonical_origin`: provider-native release/artifact or originating
  legal/standards record with a safe locator; avoid bearer tokens.
- `source_role`: publisher evidence, independent observation,
  secondary interpretation, or unverified lead.
- `source_revision`: tag, version, document revision or UNKNOWN.
- `published_at`, `effective_at`, `event_at`, `checked_at`: independent,
  not mutually substitutable timestamps.
- `scope`: affected product, endpoint, model, region, account tier or
  runtime; license and user entitlements must be confirmed independently.
- `statement`: narrow testable claim with linked original support.
- `confidence_reason`: high/medium/low plus what missing evidence caps it.
- `decision_impact`: migration, security, budget, experiment,
  informational or NOT_ESTABLISHED.
- `source_access`: consulted, unavailable, prohibited or not checked.

Deduplication uses a stable provider artifact or regulation identifier and
revision, plus the actual change. Syndicated accounts of the same announcement
do not count as independent corroboration. A later correction is related
to but does not silently overwrite the earlier claim. Multiple providers
calling different metrics "accuracy" do not create directly comparable
measures.

For security advisories, distinguish reported, fixed, released and actually
deployed. For new model versions, distinguish checkpoint distribution from
API route activation and end-user entitlement. For regulatory material,
distinguish proposal, adoption, effective date and scope. For GitHub
repositories, distinguish stars, code presence, actual behavior and
independent security/quality verification.

Evidence is sufficient only for the claim it actually supports.
An unreachable source is not negative evidence, and a marketing claim
is not proof of reproduced performance. Do not assert freshness without
live or exact as-of evidence from the stated interval.

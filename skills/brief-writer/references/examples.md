# Gold-standard example — brief-writer

One complete exemplar (per docs/skill-template.md §Capability floor rule 6). Load only when writing a brief; match its discipline, not its subject.

```markdown
# Decision brief: error-tracking vendor — due Friday

**Decision needed:** pick the error-tracking vendor for the 5-person team by Friday; owner: Dana.

**Situation:** We evaluated Sentry, Rollbar, and Honeybadger against the four agreed criteria (price @50k events/mo, self-host, Rust SDK, alert routing). Sentry passes self-host and has the only officially maintained Rust SDK. Rollbar fails self-host and its community SDK is 14 months stale. Honeybadger's alert routing is still unevaluated.

**Options:**
1. **Sentry now** — strongest verified profile; RISK: its real 50k-event price is unresolved ($26 page vs ~$89 blog claim); reversible (monthly billing).
2. **Wait 1 day, close two gaps first** — run Sentry's pricing calculator + read Honeybadger routing docs; RISK: one day of Friday buffer; fully reversible.
3. **Honeybadger** — cannot be recommended: zero criteria verified; choosing it now would be preference, not evidence.

**Recommendation:** Option 2. Both open questions close in under a day and either could flip the ranking (an ~$89 effective price triples the assumed cost).

**What would change this:** calculator confirms ≤$40/mo → recommend Sentry immediately; Honeybadger routing turns out best-in-class AND Sentry price is high → re-run the comparison with real numbers.
```

Why this is the standard: the decision and deadline lead; every option carries cost, risk, and reversibility; the recommendation is argued against its runner-up; the flip conditions make the brief falsifiable rather than persuasive. One page means one page.

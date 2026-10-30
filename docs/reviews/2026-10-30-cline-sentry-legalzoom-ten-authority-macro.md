# Cline pinned Sentry and LegalZoom authority macro review (2026-10-30)

## Scope and source identity

- Current main at start: `c754818be5f6107a595c89f179f4bf1bfcecaf43`; registered source: `cline-skills`, `https://github.com/cline/skills`, Apache-2.0 for the two reviewed packages; pin `26378461e978f2b4e2e6d67b57121b86b2a79ba5`.
- Published first-class Cline inventory: **36/36 current-standard**, zero static gaps; separately characterized internal Cline SDK exposure is not silently added to published inventory. All ten inspected units already had individual provenance and exact-version verification records. Genuine new gaps: **0**. Admitted denominator delta: **0**.
- Bounded authority screen of ten existing records: `sentry-cli`, `attorney-assist`, `save-to-spotify`, `gcp-to-aws`, `searching-sourcegraph`, `linear-sdk-scripting`, `use-railway`, `teamcity-cli`, `session-report`, and `vibe-prospecting`. Two escalated for deep review; eight previous dispositions retained. No source material, package pin, dependencies or upstream references changed.
- The Cline source is a pinned Git reference corpus, not repository-owned executable infrastructure. All review work was static. No SkillSpector scan, external behavior, private data transmission, Sentry command, LegalZoom call or validation execution occurred.

## Exact-version decisions

### sentry-cli: VERIFIED 16/20 → REJECT unchanged 13/20

- Exact pinned SKILL.md: `skills/sentry-cli/SKILL.md`, Git blob `edac0959688f1961aac5f1276bca88d78370a560`. Bundled `references/auth.md`, `references/alert.md`, and `references/release.md` inspected as part of the package, not as repository-owned tooling.
- The operative instruction **"Just run the command"** and automatic organization/project detection can precede authorization for private issue, trace and log access. A later output-based context check is not a before-action approval. The same skill supplies release creation/finalization/deploy, alert creation/edit/deletion, project mutations and authenticated arbitrary API POST. Those effects need target/action-specific permission, not just a working CLI.
- Bundled auth instructions expose `sentry auth token` and `sentry auth status --show-token` as raw-token output paths. A general "never log tokens" warning does not reliably prevent agent transcript or command-output disclosure. Alert/release references also document bypassing confirmation prompts.
- Dependencies: authenticated Sentry CLI, account/project access, network, bundled command references. Portability low; exact snapshot and source unchanged. Preserve bounded JSON output, exit-code interpretation, scoped read-only diagnostics and command references as ADAPT/EXTRACT/CHECKLIST only. No behavioral evidence: `not-run`.

### attorney-assist: VERIFIED 19/20 → REJECT unchanged 15/20

- Exact pinned SKILL.md: `skills/attorney-assist/SKILL.md`, Git blob `38de30c04ff53b47900f30c04fb16da6aec26453`. Source-owned LegalZoom MCP dependency and independent public service confirmation remain provenance evidence, not disclosure authorization.
- The workflow says the attorney receives everything from the conversation, documents and AI analysis. Its context package includes legal summaries, reviewed document details, flagged clauses/redlines, customer identity, jurisdiction, phone number and scheduling data. Selecting an attorney and time authorizes scheduling; it does **not** separately authorize disclosure of unrelated or sensitive history, the full document-derived context or every analysis field.
- No mandatory minimum-necessary context preview, recipient/disclosure-scope selection, redaction and affirmative before-send consent is established. A genuine booking tool response and anti-fabrication discipline are valuable but do not close this privacy boundary.
- Dependencies: active LegalZoom entitlement, external consultation MCP, jurisdiction and real availability, phone contact, user-selected slot. Portability low. Preserve entitlement verification, anti-fabrication, stop-on-failure, slot selection and handoff as ADAPT/EXTRACT/CHECKLIST. Behavioral evidence: `not-run`.

## Retained controls and macro synthesis

Eight existing dispositions retained: `save-to-spotify` (explicit interview, plan confirmation and installation approval), `gcp-to-aws` (staged artifact generation without automatic cloud deployment), `searching-sourcegraph` (scoped read-oriented search), `linear-sdk-scripting` (already rejected for asking for a real API key in chat), `use-railway` (already rejected for overbroad deployment authority), `teamcity-cli` (already rejected for CI/CD mutation without per-action approval), `session-report` (already rejected for unscoped transcript/PII export), and `vibe-prospecting` (already rejected for unpinned executable dependencies and contact-data minimization gaps). Retention is not new security or behavioral approval.

**Systemic pattern:** A useful external-service reference can become an unsafe unchanged-use procedure through two different mechanisms: (1) auto-discovered private context and a catalog of powerful CLI operations that lack a before-action boundary, and (2) a legitimate scheduling/consultation request that silently expands into bulk sensitive-data disclosure. Tool availability, a confirmed provider, and a user-selected target are not substitutes for explicit disclosure or mutation authority.

**Evidence/freshness:** The pinned source snapshot and both SKILL.md fingerprints remain unchanged. Cline is 36/36 static-reviewed, not 36/36 behaviorally validated. These two new negative dispositions change no persisted review count, source-family denominator, source admission, or security result. The eight retained reviews are not refreshed to claim new execution. Controlled tags and existing dependency records remain in place.

## Lifecycle and accounting

All seven open issues and five open draft PRs were triaged first. The three disjoint first-party repair drafts #489 (29), #492 (5), #496 (2) remain blocked on complete pinned SkillSpector v2.12.0 exact-final-tree reports/digests and independently executed adversarial acceptance for 36 trees; their shared first-party registry must be reconciled before merge. Admission drafts #412 and #413 remain blocked on their separate candidate security, independent acceptance and atomic admission accounting. None is eligible to merge solely because GitHub reports it mergeable. No completed issue is closed by this third-party authority correction.

README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json were updated together to retain **44 first-party / 867 third-party / 911 total** and source **36/36**, with zero denominator delta. This review is a static correction only. Next highest-priority action remains external qualification of the 36 final first-party repair trees, then registry reconciliation and eligible PR merges.

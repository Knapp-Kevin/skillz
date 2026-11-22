# CI Guard v1.5.7: distinct forward/tag/dispatch obligations

**Date:** 2026-11-22. **Issue:** #861. **Scope:** independent original source changes; no consumer identified or modified.

## Concrete defect fixed

The v1.5.6 normalized simulator checked unique verifiers but not independently required forwarding, tagging, regeneration and publication side effects. Because a post-merge push or release can correctly have no PR qualification gate, removing an actual forwarding/tag job could previously leave all `expected_qualifies:false` assertions satisfied.

Schema v2 now requires source-governed `normative_side_effects`, caller-derived `required_side_effects`, and explicit `effect_kind` plus `side_effect` identities for `role:other` jobs. The same existing simulation rejects omitted, failed, duplicate, unapproved and normatively inconsistent effects, regardless of PR qualification expectation. It does not make host-executed action claims.

The fully fictional fixture has two candidate graphs, eight workflow definitions and eleven event/status scenarios. Eight new adversarial test methods cover forward/tag/regeneration on deliberately unqualified PR routes, lost forwarding, duplicate tagging, unauthorized action, failed effect, normative drift, missing scenario inventory and unclassified effect type.

## Evidence boundary

**Hosted source qualification:** GitHub Actions run #45077634202 PASSED on PR #868 source head 19818416702e3bcccf0627ad0d37c617bd1bdd20 (150/150 Python methods: 12 overlap + 16 strict cutover + 23 self-repair + 45 scenario + 28 classifier + 26 plan). All three initial GitHub checks completed successfully. Registry-only evidence reconciliation follows; final exact-head qualification remains required before merge. Prior 142/142 test success is v1.5.6 evidence only. Real GitHub Actions token chains, conformance tests in a consumer repository, publication authorization, provider-run receipts, and billed runner-minute or critical-path savings remain NOT_RUN/NOT_MEASURED. Issue #861 stays open for those broader requirements.

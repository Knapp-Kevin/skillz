---
name: fictional-evidence-brief
description: >-
  Fictional engine fixture demonstrating one pack with sequenced fact collection,
  evidence checking, a reusable summary skill and optional personal style.
  For local structural testing, not an installed or quality-verified skill.
---
# Fictional Evidence Brief

Trigger only for a request to summarize **user-supplied** notes with
traceable claims. Do not trigger on an external research request or on
instructions to collect private information without authorization.

This fixture is read-only. Do not open network links, write files,
publish reports, send messages or persist a user preference.

Follow [collect](phases/collect.md), [evidence check](components/evidence-check.md),
then the separately usable [summary skill](skills/summarize/SKILL.md).
Optionally perform [style](phases/style.md) only when requested and safe.
The required chain must pass even when style is skipped.

**Completion:** Every factual claim in the brief is supported by an
identified supplied note; missing evidence is explicitly UNKNOWN.
Record whether you performed a real host execution. A passing pack
structure check does not count as a successful brief. No preference
is stored without separately observed consent and private host storage.

For feedback, apply the engine [pack feedback policy](components/feedback-policy.md). Never edit the canonical fixture from
within this skill. This sample has not been behaviorally validated.

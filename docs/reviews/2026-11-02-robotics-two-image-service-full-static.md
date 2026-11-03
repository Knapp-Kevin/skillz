# Robotics hosted-image bundles: two complete pinned-package static reviews (2026-11-02)

**Decision: both REJECT_UNCHANGED.** The source procedures remain useful negative/reference evidence, but their host-visible guards are insufficient for private camera images or high-consequence robotic decisions. **No upstream code is modified, copied or executed.**

## Exact evidence and review boundary

- Source: [graph-robots/open-robot-skills](https://github.com/graph-robots/open-robot-skills/tree/752dfbd96968d4d08379f8111765efbf6457800b), immutable pin `752dfbd96968d4d08379f8111765efbf6457800b`.
- Recovered from held PR #590 via merged #646, individually inspected SKILL.md entrypoints in #647, and full source-tree fingerprint reconciliation of all 43 packages in #649.
- **Two complete source package directories inspected**, each containing `.python-version`, `SKILL.md`, `pyproject.toml`, `tools.py` and `uv.lock`. Full SKILL/tool/metadata and lock texts were fetched at the pin. Both lockfiles contain 35 resolved dependency package records and SHA-256 distribution hashes; the external local editable `graph-as-policy-core` dependency has **not** been independently inspected or pinned by these package trees.
- Source/file fingerprints, 10 individual rubric dimensions per package, findings, remediations and explicit `not-run` states: [exact review JSON](../../registry/discovery/robotics-two-remote-image-complete-static-20261102.json).
- The package's root-source `LICENSE` is Apache-2.0; individual `SKILL.md` and `pyproject.toml` labels state MIT. Retain both observations, do not assume either one grants rights to external runtimes, SDKs, models, images or their supporting assets. No blanket redistribution clearance.

## 1. `tools/gemini-er`

**Exact directory SHA:** `d4916cdb807670e6e66a06af7cfb7bb4b8c6d59f`. **Score: 10/20. REJECT_UNCHANGED due to safety/evidence/authority hard failures.**

The procedure performs a concrete useful operation: convert text-prompted object detection via Gemini Robotics-ER into pixel-space boxes. But its implementation's claimed confidence and input-validation behavior undermine a safe caller:

- **False maximum confidence:** `tools.py:_parse_detections` treats a missing or unparseable `score`/`confidence` as **1.0**. Downstream callers are explicitly encouraged to select `max(..., key=score)`. This can promote a response with **no confidence evidence** ahead of a genuine scored detection.
- **Unvalidated geometric output:** four normalized coordinates are converted and clamped, without rejecting inverted box order, zero area, nonfinite values or values outside the original normalization contract.
- **Indistinguishable failures:** malformed/unparseable model output returns the same empty-detection result as a genuine absence of matching objects; API errors remain separately surfaced.
- **External camera data:** `detect` sends PNG bytes of the input RGB image to a hosted API using an environment-resolved key. No action-specific private-image egress authorization is visible **inside the reviewed package**. The outer `gap` runtime and connector may impose protections, but those are **not established here**.

**Remediation gate:** require endpoint/data approval before external image transfer; keep unknown confidence distinct and finite; reject invalid/inverted/nonfinite boxes; distinguish no-match from malformed response; independently qualify the actual external runtime and provider behavior. Capture executed adverse-input evidence before any high-consequence unchanged use.

## 2. `tools/vlm`

**Exact directory SHA:** `aaca905ce5156066f295fa0c43225a016be88458`. **Score: 11/20. REJECT_UNCHANGED due to privacy/authority and unsafe yes/no coercion.**

The bundle adds useful general scene questions and yes/no checks via OpenRouter or Vertex, but its actual code and inherited configuration introduce concrete risk:

- **Ambiguous answer becomes action-driving Boolean:** `tools.py:_coerce_yes_no` takes the first `yes` or `no` word anywhere in model text, or falls back to checking whether `"yes"` appears as a substring. A response containing an unrelated word like `yesterday` can become `True`; missing or ambiguous language has no safe `UNKNOWN` outcome.
- **Unexpected destination and credential disclosure risk:** `_resolve_provider` inherits `GAP_LLM_PROVIDER`; `_query_openrouter` chooses a URL from `GAP_VLM_BASE_URL`, encodes input camera images as base64 PNG in the request, and sends a bearer API key if configured. The package itself does not enforce an endpoint allowlist, per-image disclosure approval, or provenance of the resolved destination. Configurability is not itself malicious, but unexpected inherited settings can redirect sensitive data.
- **Unbounded retry class:** up to three attempts are made for all exception classes, potentially resending private frames and incurring repeated cost on nontransient errors; log/error strings do not establish credential-safe redaction.

**Remediation gate:** explicit scoped image egress/endpoint consent and credential origin policy; strict leading-token or structured yes/no with `UNKNOWN` on ambiguity; classify retryability and redact errors; qualify the external `graph-as-policy-core` controls; execute representative host tests for no-answer/ambiguous text, denied image transfer and provider override.

## Disposition and next evidence

The reviews use the repository's exact-version 10-dimension/20-point static rubric, each with separately documented hard fails. **No scanner has passed, no scripts or remote APIs ran, no token or image was sent, and no robot executed.** These are **two source-family review decisions outside the pinned 4,813 raw-path snapshot** and outside the 1,039 governed review identities. Do not add them to those populations or claim admission.

With the two prior complete-package rejections in #649, the recovered 43-entry robotics family has **four exact-version source packages statically reviewed as REJECT_UNCHANGED**, and **39 remaining at discovery-only status**. All 43 package-tree identities are verified, but a tree hash is not a package review. Further work should prioritize the two VLA actuation policies and the `tools/molmo` remote-code recipe without automatically adopting their instructions.

**Passive repository contract:** this artifact records host inspection evidence only, no CI, runner, scanner, repository runtime or installed skill.

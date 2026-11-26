# Optional normalized session design intake (issue #954)

This is an intake and review gate, not an extractor of native chats or
a semantic session-to-skill generator. Begin with Skill Bootstrap and
existing discovery/reuse/adapt/create decisions. An existing suitable
skill terminates this original-generation route.

Only accept locally prepared, explicitly authorized, minimized records
with no transcript prose, secrets, user identifiers, private preferences,
task answers, host-specific setup or third-party content. Review and
minimize outside this tool BEFORE ingestion or inference. The input
format is a typed manual record; fictional Claude/Codex-normalized labels
are test-format labels, not native log parsers. Unknown/truncated formats
hold. No tool can guarantee semantic privacy by validating field names.

Inputs:
- Session schema_version 1; format manual-minimized-v1, or fictional-claude-normalized-v1 /
  fictional-codex-normalized-v1 for cleared synthetic input; complete true;
  locally assigned opaque session_id and environment_id; discovery with
  decision CREATE_ORIGINAL or COMPOSE_ORIGINAL, coverage CALLER_REVIEWED,
  review_id. All are caller claims. Excluded categories list includes
  raw-transcript; other supported categories: private-preference, task-answer,
  host-setup, secret, third-party-content.
- Chronological requirements (id, target, supersedes): each target is an
  existing design obligation target; initial supersedes null, later corrections
  point to its current ID. Observations (id, requirement_id, oracle_id, status)
  bind the exact revision; claimed pass/fail requires a distinct opaque oracle
  ID, NOT_RUN/UNKNOWN requires null. Current requirements must have only
  PASS_CLAIMED observations; earlier failures remain visible in history.
  These are not independently authenticated oracle results.
- Independently authored existing design dossier. Its evidence IDs must come
  from the normalized requirements/observations. Each obligation links its
  current requirement and a current passing observation, with no cross-target
  reference or omitted historical IDs. Evidence prose must be written anew
  by an authorized author, not copied from the trace. Existing blueprint,
  obligation, probe and host-admission checks remain in force.
- Scope declaration (schema_version 1, scope REVIEWED_MINIMIZED_DESIGN_PREFLIGHT_ONLY,
  session_sha256, dossier_sha256, custody PRIVATE_LOCAL or CLEARED_SYNTHETIC,
  review CALLER_ASSERTS_MINIMIZATION_AND_ORIGINAL_CONTENT_REVIEW). Hashes use
  sorted compact UTF-8 JSON (session_design.sha). Declaration is not consent
  authentication, rights clearance, independent oracle evidence or proof
  that a session succeeded.

Read-only preflight:
    python3 -B engine/builder/session_design.py --session /approved/minimized.json --dossier /approved/design.json --authorization /approved/scope.json

The result is the existing builder draft receipt plus bounded intake counts;
the tool creates no destination package, copies no session data into output
files, invokes no transcript commands, and never installs or publishes.
The existing builder internally uses disposable staging. Only after separate
review and explicit destination authority, use the original design writer.
Retain the minimized evidence locally and separately from any shared package.
The CLI deliberately emits a generic HOLD on malformed input.

The fictional regression fixture in scripts/qa/test-session-design.py
demonstrates a changed requirement, retained historical failure, exact
draft generation in a test-only temporary directory and source-linked
acceptance-plan generation. It is not an observed successful agent session
or a measured baseline comparison. Remaining: authorized native-format
normalizers, source minimization/rights review, richer decisions and recovery
evidence, semantic solution-leakage review, real held-out comparison.

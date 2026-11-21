# Trial receipt contract, v1

The optional original checker accepts one JSON snapshot, strictly schema_version 1. It is **not** a model or runner. Valid JSON does not authenticate what a host claims to have done.

## Top-level shape

```json
{
  "schema_version": 1,
  "skill": {"id":"demo_skill", "entrypoint_blob_sha":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "package_tree_sha":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"},
  "protocol": {"id":"pilot_v1", "run_kind":"CONTROLLED_EMULATION", "preregistered":false, "minimum_pairs":10, "minimum_delta_pp":20, "holdout_isolated":false},
  "pairs": []
}
```

Actual input requires **1 to 2,000 pairs**. The empty array above is a shape sketch, not a valid executed receipt. SHA properties require 40 or 64 lowercase hex characters. IDs allow only 1–180 characters in ASCII alphanumerics, dot, colon, hyphen, underscore. Do not use names, URLs, keys or signed links as IDs. The checker disallows unknown keys, duplicate JSON fields, duplicate pair IDs, duplicate run IDs and reused receipt fingerprints.

`run_kind` is HOST_EXECUTED or CONTROLLED_EMULATION. The latter can never produce a positive host-evidence signal. `preregistered` and `holdout_isolated` are **host-supplied claims**; external observer evidence is still required before anyone may promote a result.

## Pair object

Each `pairs[]` record contains `pair_id`, `case_id`, `should_trigger` (boolean), `leakage_review` (CLEAR, POSSIBLE, UNREVIEWED), and two arms `baseline` and `treatment`.

Each arm requires:

`run_id`, `host_id`, `model_id`, `agent_version`, `config_sha`, `snapshot_sha`, `grader_sha`, `result`, `verification_kind`, `verifier_independent`, `blind_to_arm`, `observed_execution`, `skill_triggered`, `authority_violation`, `tokens`, `duration_ms`, `receipt_sha`.

- `config_sha` identifies settings, tool permissions, model parameters and input environment outside the separately pinned host/model/runner labels.
- `snapshot_sha` binds the same initial task fixture and workspace to both arms, **not** a shared writable state. The independent runner must verify each arm's clean start.
- `grader_sha` identifies the same grading criteria/implementation; `verification_kind` is DETERMINISTIC, BLIND_JUDGE, HUMAN or UNVERIFIED. Blind judges require `blind_to_arm: true`.
- `verifier_independent`, `observed_execution`, `skill_triggered`, `authority_violation` are booleans except `skill_triggered` can be null to represent unknown telemetry. When `should_trigger` is false, `skill_triggered: true` in treatment disqualifies that pair.
- `result` is PASS, FAIL or INCOMPLETE; an absent external verifier, incomplete run, safety issue or contamination disqualifies that pair from qualified outcome analysis.
- `tokens` and `duration_ms` are nonnegative integers or null. Missing cost and duration evidence must remain missing.
- `receipt_sha` represents an externally captured unique receipt artifact identity, **not** an assertion that the current script independently recalculated or authenticated a signed receipt. A checksum alone does not create evidence authenticity.

Raw output and grader commentary should be retained only by the authorized host with appropriate privacy controls. The skill does not need private prompts or original customer records to verify the method's structure.

## Statistical and interpretation limits

The checker reports the paired difference between treatment and baseline PASS rates on **positive-trigger pairs only**, excludes every pair with material integrity flags, and reports excluded IDs and reasons. It also evaluates nontrigger tests independently and does not permit a recorded positive result when the treatment regresses a valid nontrigger task.

It applies a two-sided exact sign/McNemar calculation on discordant pairs **only when each `case_id` is unique**; repeated case IDs are treated as correlated and significance withheld. Even unique labels are not proof of independent random sampling. It does not correct for multiple hypotheses, judge dependence, post-selection, repeated attempts, use of the same task template under different labels or domain shift. Any `p < .05` output is a reported mathematical consistency condition and must be interpreted only by a separately capable reviewer, **never as skill validation or a general population claim**.

The checker always emits `source_authenticity_verified: false` and `actual_independent_host_validation_verified: false`. `RECORDED_POSITIVE_SIGNAL_NOT_AUTHENTICATED` is the strongest possible output, **not** an approval, quality grade or proof of a 1.5x product outcome. Any excluded pair, incomplete protocol, unreviewed leakage or missing nontrigger coverage withholds that signal. The exact inputs and full trial reports should be retained in an authorized location only when the user approves persistence.

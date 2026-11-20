# Agent Failure Boundary Analysis v1.2: offline incident evidence guard

**Issue:** #738. **Date:** 2026-11-20. **Scope:** original standalone six-file authored package.

- Entrypoint Git blob: \`447d9934db360eb3ff6309a5033f119914c1eced\`.
- Complete package tree: \`cd86911fe032fc423c8e2008d3683522490d3f04\`.
- Original new script blob: \`4201e6d39f27660c41f02cd857af71427624ec12\`.
- Exact executed Python test blob: \`d4f4aa1ea5a80f26208b1f0b8020aac95400de9e\`.
- Previous v1.1 retirement-phase blob/tree: \`4a114972587060c79ee6df852526a0a047abd3c2\` / \`426391a3bea7e75f364fe86da8845dee2718f8a5\` (preserved as history).

## Functional increment

Earlier v1.1 instructed an analyst to maintain evidence lineage, defend causal uncertainty, audit resource runaway and separate implementation from verified user outcome. Those directions relied entirely on the host's diligence. v1.2 includes an **optional original offline Python method** that checks well-formed evidence references and ordering, refusal on causal-order cycles, mechanically correct write-approval scope and prior reference, attempt-budget overruns only where recorded, and claims that improperly promote a PR merge or CI receipt into deployment or real-world user success. This is a bounded guard against false completion claims, not an interpreter of incident causes.

The validator is self-contained: Python standard library, explicit JSON input only, no network or secret-fetch capability, no subprocess, no repository writes, no output file, bounded 1 MiB input, 500 events, 50 claims. Source text and approval pointers are untrusted data and not executed or echoed. Stronger hosts can use their own equivalent evaluation, and hosts lacking Python must disclose the checker was not run.

## Observed executable checks

The exact local script and tests were verified against uploaded Git blobs. Executed \`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v\`: **31 / 31 PASS**. Coverage includes cycles, self-edges, duplicate/missing event and claim references, unknown evidence, alleged versus observed records, invalid JSON/oversize, causal order, true supported stage versus unsupported stage, approval scope/order, observed retry limit breach versus incomplete attempt evidence, inert hostile source string and zero-output-file CLI execution.

For a deliberately adversarial negative control, separately retrieved live public GitHub evidence from PR #815: merge commit \`99b3fe70ce889d8c07903d0eab3baad1d60c52e4\` at 2026-11-20 18:52:12 UTC, both Socket checks successful at 18:50:27 UTC and 18:50:25 UTC. An input example records these receipts but **adds fictitious** statements that production was deployed and a user's requested outcome verified. Executed checker output: merge SUPPORTED_BY_RECORDED_INPUT; CI SUPPORTED_BY_RECORDED_INPUT; deployment INSUFFICIENT_RECORDED_EVIDENCE; user outcome INSUFFICIENT_RECORDED_EVIDENCE; root cause NOT_DETERMINED. This is not evidence that the real PR failed to deploy, nor that a user experienced an incident. It is a real-source-backed negative-control test of unsupported promotion.

See [machine-readable receipt](../evals/receipts/2026-11-20-agent-failure-v120-trace-integrity.json).

## Static rubric and limits

Maintainer current-package static review: **18/20**. Original skill safety, durable learning routing and falsifiable lesson requirements are preserved. Host source availability and the absence of an independent external host qualification still constrain usefulness and effectiveness evidence. Input labels, approving actors and source authenticity are **not** verified by the script; even a mechanically well-formed approval is not proof of real permission. The script intentionally always states \`root_cause: NOT_DETERMINED\` and \`evidence_authenticity_verified: false\`.

Historical 1.1 retirement and controlled textual emulations stay pinned to their original exact trees. Neither 31 deterministic tests nor a public-GitHub negative control establishes complete historical skill parity, root-cause accuracy, incident user outcomes, isolated model-host old/new comparison or **1.5x overall effectiveness**. The original historical author/license rights remain NOT_ESTABLISHED. Keep #738 open.

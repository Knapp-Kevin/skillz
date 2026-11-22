# CI Guard v1.6.0: mandatory cross-workflow execution deduplication

**Date:** 2026-11-22. **Owner priority:** P0. **Repository:** Skillz first-party
authored CI Guard package. This review targets an anonymous execution pattern
and does not name, depend on, or modify any consumer project.

## Root defect and actual source correction

CI Guard v1.5.1 described duplicate checks and old bootstrap migration,
but did not require a recursively traced **execution graph spanning all
triggered workflows**, before a substantive optimization. A draft skip or
change classifier could be considered an improvement while an independent
unconditional workflow still executed the same deep verification.

v1.6.0 adds the **mandatory P0 entry gate** directly in SKILL.md's binding
requirements and decision procedure (before classification/implementation).
Bundled component `execution-graph-deduplication.md` specifies workflow
event coverage, job conditions/needs/matrices, composite/reusable actions,
nested scripts/task runners, exact source/inputs/platform/trust, classification
(EXACT_DUPLICATE, PARTIAL_OVERLAP, JUSTIFIED_REPETITION, UNPROVEN),
disposition (CONSOLIDATE, KEEP, RELOCATE, VERIFY), required-gate preservation,
real after-cutover scan and separate actual billing/critical-path receipts.
The change-classification, dependency/qualification and modular-bootstrap
components also require this prerequisite.

## Exact current five-file addition and full package

- CI Guard **1.6.0**, SKILL git-blob SHA:
  `69cfa50baec76b327ac3f496f56694720210f3c5`.
- Complete standalone **24-file** package Git tree:
  `578bba0b2bab8932ea2ee9122ca886697f711cf3`.
- Original MIT license bundled, unchanged:
  `023abdb34298b27580d1d303084aca942050585e`.
- New executable stdlib checker: `scripts/audit_execution_overlap.py`,
  Git blob `14de5e4f8fb6747e2a762eed20b446746c83112c`.
- 26-case executable tests: `examples/test_execution_overlap.py`,
  Git blob `088b066db89b7eccb7e789c7c3575d415457d74a`.
- Fictional graph source/baseline and after-cutover JSON fixtures, as
  well as the new in-package normative component.
- No new GitHub workflows, always-running services, network calls,
  dependencies, branch rule changes, consumer edits or mandatory agents.

## Actual executed local method evidence

Verified in a local Python environment using the exact checker and test
files later uploaded byte-for-byte and confirmed by Git blob SHA:

```
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s examples -q
# Restrict to test_execution_overlap.py for this new-method receipt.
# 26 tests, 26 passed, zero failures.
python scripts/audit_execution_overlap.py --input examples/execution-graph-overlap.json
# exit 3 / HOLD, candidate and release PARTIAL_OVERLAP
python scripts/audit_execution_overlap.py --input examples/execution-graph-consolidated.json
# exit 0 / structural PASS, no overlaps
```

Adversarial cases exercise:
- distinct task-runner names resolving to the same effective terminal
  verification, and composite/standalone partial overlap;
- false positives where different platform/trust has separate source
  assurance, and unproven changed toolchain/trigger event;
- a source graph falsely labeled consolidated while old standalone
  candidate or release workflow still runs;
- loss of unique release signing, missing gate obligations,
  skipped/stale authoritative receipts and draft-to-ready transitions;
- known stochastic repetition retaining distinct annotated receipts;
- unresolved dynamic invocations, missing matrix expansion,
  undocumented disposition, duplicate JSON keys, symlinked input and
  side-effect-free execution.

**Limits:** The Python input graph and synthetic receipt values are
caller-supplied. A passing structural fixture does **not authenticate** real
workflow discovery, source revisions, protected-status policy, source
provenance, negative-control operation or GitHub Actions outcomes.
`optimization_complete: false`, actual runner-minute delta
`NOT_MEASURED`, actual critical-path delta `NOT_MEASURED` are
intentional even on the passing fixture. The v1.5.1 broader Python
suite was not re-executed during this focused change; its historical
results do not silently certify a new version. Independent
model-host behavioral acceptance remains NOT_RUN.

## Go/no-go and owner handoff

**Source correction:** GO only after merged to main and exact tree/blob
identities reverified. **Consumer optimization / production cost claim:**
NO-GO until each authorized consumer supplies a genuinely complete,
observed cross-workflow terminal execution inventory, branch and
release gate parity including planted failures, proof old unconditional
paths stopped, real comparable Actions/CI receipts and measured
runner-minute and critical-path results. No permission to modify an
unmentioned consumer is conferred by publishing the skill.

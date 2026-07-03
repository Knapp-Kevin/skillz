# Shadow Genome

## Purpose

The Shadow Genome documents **failure modes** - approaches that were rejected, patterns that failed, and lessons learned. This creates institutional memory to prevent repeated mistakes.

---

## Failure Categories

| Code | Category | Description |
|------|----------|-------------|
| `COMPLEXITY_VIOLATION` | Section 4 Razor breach | Function/file too long, nesting too deep |
| `SECURITY_STUB` | Incomplete security | TODO/placeholder in auth/security code |
| `GHOST_PATH` | Disconnected UI | UI element without backend handler |
| `HALLUCINATION` | Invalid dependency | Library that doesn't exist or wasn't verified |
| `ORPHAN` | Dead code | File not connected to build path |
| `SPEC_DRIFT` | Blueprint mismatch | Implementation doesn't match specification |
| `CHAIN_BREAK` | Merkle violation | Hash chain integrity compromised |

---

## Failure Log

<!--
Each failure is documented with:
- Date and iteration
- What was attempted
- Why it failed
- Pattern to avoid
- Resolution (if any)
-->

---

### Failure #1: Plan cited verification machinery its own inventory did not define

**Date**: 2026-07-03
**Iteration**: 1 (session 2026-07-03T2023-ca9b2c, audit iteration 1)
**Verdict ID**: GATE VETO on docs/plan-qor-phase1-meta-skill-audit-sync.md
**Category**: SPEC_DRIFT

#### What Was Attempted

First plan submission for the Meta-series completion (skill-audit + skill-sync). Four defects: a test consumed an undeclared fixture (tests/fixtures/bad-registry.yaml); Phase 3 claimed coverage via a `git diff --exit-code` CI command that the CI Commands section did not contain; the only sync target writing outside the repo (`--claude-user`) had no test; LD-1 grep-evidence was off by one line and D3 promised ledger entries against an unsealed genesis (placeholder hashes).

#### Why It Failed

- Violation 1 (`specification-drift`): undeclared deliverable — fixture consumed but not in Affected Files.
- Violation 2 (`test-failure`): coverage claim referenced nonexistent CI command; LD-1 behavioral-equivalence claim had no automated check.
- Violation 3 (`coverage-gap`): highest-blast-radius write path untested while lower-risk paths were tested.
- Violation 4 (`infrastructure-mismatch`): inexact grep-evidence; governance deliverable promised against a chain that did not exist yet.

#### Pattern to Avoid

**Anti-Pattern**: writing later-phase coverage claims ("covered by X below") without confirming X exists verbatim in Affected Files or CI Commands; treating home-directory writes as too awkward to test.

**Correct Pattern**: every cited fixture/command must appear in the plan's own inventory (plan-internal analogue of SG-CitationDrift-A); make out-of-tree write paths testable by parameterizing their root.

#### Resolution

| Status | Action Taken |
|--------|--------------|
| FIXED | All four findings remediated as plan-text amendments + genesis seal; PASS at audit iteration 2 (Ledger Entry #3). |

#### Related Entries
- Ledger Entry: #2 (VETO), #3 (PASS)
- Audit Report: .agent/staging/AUDIT_REPORT.md

---

### Failure #2: Sealed gate artifact overwritten by singleton filename

**Date**: 2026-07-03
**Iteration**: 1 (session 2026-07-03T2023-ca9b2c, audit iteration 3)
**Verdict ID**: GATE VETO (iteration 3) — infrastructure-mismatch (seal integrity)
**Category**: CHAIN_BREAK

#### What Was Attempted

Gate artifacts were written via `gate_chain.write_gate_artifact`, which stores each phase's artifact at a singleton path (`.qor/gates/<sid>/audit.json`). The iteration-1 VETO artifact was sealed into ledger Entry #2 (content `3da98e31…`), then the iteration-2 PASS verdict was written to the same path, overwriting the sealed file (now `683679a8…`). The Judge's genesis-forward chain recalculation at iteration 3 detected that Entry #2's evidence no longer exists on disk. A sibling defect: the singleton `plan.json` still carried the pre-amendment CI command.

#### Why It Failed

- Violation 1: sealed evidence destroyed — the file a ledger entry binds must be immutable after seal.
- Violation 2: singleton gate filenames cannot represent multi-iteration phases (audit VETO→PASS is the *normal* path).

#### Pattern to Avoid

**Anti-Pattern**: mutable singleton filenames for artifacts that get cryptographically sealed; re-running a phase in place.

**Correct Pattern**: one seal, one immutable file — iteration-versioned artifacts (`audit-iter2.json`, `plan-iter4.json`); the overwrite event recorded in Chain Integrity Notes (never retro-editing ledger entries); the surviving artifact re-bound in the next entry.

#### Resolution

| Status | Action Taken |
|--------|--------------|
| FIXED | Versioned artifacts adopted (audit-iter2.json preserved at `683679a8…`, plan-iter4.json emitted); overwrite event recorded in META_LEDGER Chain Integrity Notes; surviving PASS artifact re-bound in Ledger Entry #4 (chain `4f85b370…`). PASS at audit iteration 4. |

#### Related Entries
- Ledger Entry: #4 (chain repair + PASS)
- Audit Report: .agent/staging/AUDIT_REPORT.md

---

### Failure #3: Relocated legacy code inherited into a razor-bound deliverable set

**Date**: 2026-07-03
**Iteration**: 1 (session 2026-07-03T2023-ca9b2c, substantiate iteration 1)
**Verdict ID**: SUBSTANTIATE FAIL — razor-overage ×2, specification-drift (minor)
**Category**: COMPLEXITY_VIOLATION

#### What Was Attempted

The LD-1 extraction moved `parseFrontmatter` verbatim into scripts/lib/frontmatter.ts (deliberately unmodified so the determinism check could prove the move), carrying a 54-line function with nesting depth 4 into a deliverable set whose D2 declared function-level razor limits. Separately, new code in sync.ts used a nested ternary (line 142), and `buildManifest` emitted an undeclared `source` field the three-field manifest test could not catch.

#### Why It Failed

- Violation 1: razor is function-level at the moment code enters a razor-bound path — including moves; relocation does not launder legacy overage.
- Violation 2: nested ternary in new code is an automatic razor violation.
- Violation 3: an output-shape test asserting a subset of fields cannot detect undeclared additions.

#### Pattern to Avoid

**Anti-Pattern**: declaring razor limits in D2 but deferring function-level compliance to substantiate; "verbatim move first, refactor later" inside a single razor-bound deliverable; subset assertions on generated artifacts.

**Correct Pattern**: refactor to razor at the moment of relocation (behavior preservation proven by the determinism check + tests, not by keeping bytes identical); full key-set assertions on generated artifacts.

#### Resolution

| Status | Action Taken |
|--------|--------------|
| FIXED | parseFrontmatter decomposed (cursor object; collectFolded/collectList/parseEmptyValue/parseValue/parseBlock, all ≤17 lines, nesting ≤3); sync.ts ternary expanded to if/else; `source` field removed and manifest test tightened to assert the exact key set. Full CI re-run green (8/8, audit 0/0, determinism diff clean). |

#### Related Entries
- Ledger Entry: #5 (SUBSTANTIATE SEAL at chain `f1150ab7…`)
- Audit Report: .agent/staging/AUDIT_REPORT.md

---

## Pattern Library (Extracted Lessons)

<!--
Aggregate lessons from failures into reusable patterns.
-->

### Section 4 Razor Violations

| Anti-Pattern | Correct Pattern | Examples |
|--------------|-----------------|----------|
| 50+ line functions | Split at 40 lines | See Failure #X |
| 4+ nesting levels | Early returns | See Failure #Y |
| Nested ternaries | Named functions | See Failure #Z |

### Security Patterns

| Anti-Pattern | Correct Pattern | Examples |
|--------------|-----------------|----------|
| `// TODO: auth` | Full implementation | See Failure #X |
| Hardcoded tokens | Environment vars | See Failure #Y |

### Architecture Patterns

| Anti-Pattern | Correct Pattern | Examples |
|--------------|-----------------|----------|
| God objects | Single responsibility | See Failure #X |
| Orphan files | Import tracing | See Failure #Y |

---

## Failure Statistics

| Category | Count | Last Occurrence |
|----------|-------|-----------------|
| COMPLEXITY_VIOLATION | [N] | [date] |
| SECURITY_STUB | [N] | [date] |
| GHOST_PATH | [N] | [date] |
| HALLUCINATION | [N] | [date] |
| ORPHAN | [N] | [date] |
| SPEC_DRIFT | [N] | [date] |
| CHAIN_BREAK | [N] | [date] |

**Total Failures Recorded**: [N]
**Failures Resolved**: [N]
**Patterns Extracted**: [N]

---

## Usage Notes

1. **Add entries when**:
   - /ql-audit returns VETO
   - Implementation fails Section 4 checks
   - Dead code is discovered
   - Any rejected approach

2. **Review entries when**:
   - Starting similar work
   - Seeing repeated violations
   - Onboarding new team members

3. **Extract patterns when**:
   - Same failure type occurs 3+ times
   - A clear anti-pattern emerges

---

*Shadow Genome maintained by The QoreLogic Judge*
*"Learn from failure to prevent its repetition."*

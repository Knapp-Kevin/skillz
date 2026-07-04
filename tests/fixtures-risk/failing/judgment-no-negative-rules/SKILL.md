---
name: judgment-no-negative-rules
description: Fixture — high-judgment slots without negative rules. Use when testing risk-audit.
metadata:
  version: 1.0.0
---

# Judgment Without Guardrails

This skill is strictly read-only and asks for approval before anything.

## Execution Flow

1. Gather the evidence.
2. Fill every section of the output.

## Output Format

```
# Report

## Decisions
- <chosen> over <rejected> because <reason>.

## Verdict
- <verdict> (confidence)
```

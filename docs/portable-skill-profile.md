# Portable User Skill Profile

A User Skill Profile is the host-agnostic execution layer produced by `skill-bootstrap`.

Its purpose is to preserve durable working methods across agent hosts without turning one provider's private memory format into infrastructure.

## Design rule

The profile describes **how work should be executed**, not who the user is.

Include only facts that materially change execution quality, such as evidence standards, approval boundaries, preferred autonomy, validation expectations, recurring failure handling, and selected reusable skills.

Do not include biography, incidental personal facts, private secrets, credentials, health information, ideology, or unrelated preferences.

## Authority

The profile is a default execution layer, not supreme authority.

Precedence is:

1. explicit current user instruction
2. safety/security restrictions
3. project/repository-local authoritative rules
4. task-specific skill
5. domain skill
6. User Skill Profile defaults
7. generic host behavior

A host must not use the profile to override a more authoritative source.

## Suggested schema

```yaml
profile_version: 1
profile_name: <portable label>
generated_from:
  evidence_window: <description or not-established>
  hosts_observed: []
  sources_observed:
    - type: conversation-history|memory|workspace|repository|tool-history|other
      availability: available|partial|unavailable
      note: <non-sensitive scope note>

execution_defaults:
  autonomy: propose|execute-low-risk|custom
  assumptions: <when reasonable assumptions are allowed>
  evidence_standard: <what claims require support>
  verification: <what must be checked before claiming completion>
  failure_behavior: <preferred response to missing tools/evidence/permissions>
  adversarial_review: <none|targeted|default|high-risk-only|custom>
  documentation: <durable documentation expectations>
  human_review: <where judgment must remain human>

skill_set:
  - id: <stable skill id/name>
    source: local|vendor|community|custom
    source_path: <path or source reference>
    disposition: keep|refine|adopt|adapt|supplement|compose|create
    trigger_summary: <when it should activate>
    rationale: <failure prevented or measurable benefit>
    validation_status: untested|sandboxed|validated
    dependencies: []

custom_skill_requirements:
  - proposed_name: <name>
    problem: <specific recurring failure or cost>
    evidence: <brief evidence summary>
    existing_coverage: <none|partial|reference>
    proposed_action: refine|adapt|supplement|compose|create

host_bindings:
  # Optional. These are adapters, not the source of truth.
  claude: <mapping or null>
  chatgpt: <mapping or null>
  codex: <mapping or null>
  gemini: <mapping or null>
  other: []

review_triggers:
  - <evidence that should cause this profile to be re-evaluated>
```

## Portability requirements

A portable profile must:

- use generic capability names rather than host-specific permission names
- reference skills through stable names and source paths
- keep host-specific bindings optional and replaceable
- mark unavailable evidence as unavailable
- distinguish observed fact from inference
- avoid embedding secrets or secret-shaped strings
- avoid requiring proprietary memory APIs for core behavior
- remain useful when copied to another compatible host with different tooling

## Profile generation rules

1. Prefer observed repeated behavior over one-off preferences.
2. Record a default only when it materially affects execution.
3. Separate universal behavior from domain/project behavior.
4. Keep project-local rules in the project when possible; reference them rather than duplicating them globally.
5. Do not infer durable preferences from a single correction unless the consequence is high enough to justify an explicit safeguard.
6. Every selected skill should identify the failure it prevents or the measurable advantage it creates.
7. Mark unvalidated selections as `untested`; existence in a catalog is not evidence of effectiveness.

## Cross-host handoff

When moving the profile to another host:

1. Load this profile as execution defaults.
2. Inventory which referenced skills are available on the new host.
3. Map generic tool requirements onto the host's actual capabilities.
4. Re-evaluate any skill whose required tools or authority model differ.
5. Preserve the same completion and evidence standards unless a more authoritative local rule overrides them.
6. Never claim behavioral parity merely because the same profile file loaded successfully; verify with representative tasks.

## Review triggers

Review the profile when:

- the user repeatedly corrects a behavior not represented in the profile
- a selected skill repeatedly fails or stops triggering correctly
- the user's toolchain or primary host changes materially
- repository/project governance changes
- a stronger reference implementation appears
- two skills begin overlapping or conflicting
- a previously dynamic workflow becomes stable and repetitive
- a formalized workflow becomes volatile enough that encoding it now reduces adaptability

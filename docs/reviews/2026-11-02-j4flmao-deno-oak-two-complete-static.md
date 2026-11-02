# Deno / Oak pinned source-vetting review, 2026-11-02

Pinned source: `j4flmao/agent-skills@982203e52afe0b726a7847599a8bfb293890e0c5`, root MIT LICENSE blob `0e8b6e6d8678128ebfcc28d7cad91fa9ed7f2354`. This is **source-vetting only**, not governed semantic verification, security clearance or behavioral validation.

## Scope and accounting

Two individually front-mattered first-class skills, **Deno** and nested **Oak**, were reviewed with all six direct bundled references each. The Deno containing tree has 14 distinct files: its own SKILL.md and six references plus the separate seven-file Oak package. Oak's six references are separately owned by the nested package, not counted twice as distinct files. Exact SKILL blobs and package trees, all bundled file SHAs, individual 10-dimension scores, authority/privacy findings, dependencies, rights and rationale are in [the grade ledger](../../registry/discovery/j4flmao-deno-oak-two-complete-static-20261102.json).

- Deno: **11/20, REJECT unchanged**, hard fail for unauthenticated email-bearing KV list/create/read endpoints, persistent PII and unbounded deployment/publishing guidance. The bundled Fresh example contains unescaped HTML rendering and unscoped record update/delete; legacy references contradict Deno 2 guidance.
- Oak: **10/20, REJECT unchanged**, hard fail for CRUD/deployment instructions without action-specific authority. Six bundled references include pre-v13 body API calls, obsolete imports, a development JWT-secret fallback, non-atomic KV rate limits and broad permission examples.

Useful retained methods: Deno permission scoping, frozen lockfiles, request injection with `app.handle()`, typed middleware/router separation, dependency injection, validation/error envelopes and graceful shutdown. Do not adopt the example code unchanged or infer API compatibility without external tests.

## Macro picture

Both packages contain differentiated runtime/framework knowledge, but share a systemic defect: architecture examples move directly from design to persistent data, network services and production actions without user/project, identity, tenant, environment or destination authority. The root MIT notice covers source-owned text only; dependencies and linked material need per-action rights resolution. The source tree contains nested first-class package identities, so raw path counts cannot be treated as unique package totals.

Path-matched source decisions: j4flmao **69 → 71/645** (direct **31 → 32/424**, other **38 → 39/221**), pending **574** (392 direct, 182 other). Four-source exact-path decisions **156 → 158/4,813**. Deduplicated eligible denominator unknown. Governed review population **1,039**, admission delta **0**, security scans **0**, behavioral validations **0**. No repository-owned runtime or CI added.

Next source-family cursor: `skills/backend/dotnet/architecture/SKILL.md` (other-shape). Direct cursor remains `skills/aspirational/roadmapping/SKILL.md`. Review .NET nested references before grading.

# Verification: Microsoft Skills `skill-creator`

- Source family: `microsoft-skills`
- Canonical path: `.github/skills/skill-creator`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `44744c928eba10e9e69272a6bab0859b79c480c5`
- `SKILL.md` blob: `8377383735afeb36e4b55a9937876b427785db9e`
- Static disposition: **rejected unchanged**
- Score: **15/20**
- Behavioral validation: **not-run**
- Controlled tags: `skill-authoring`, `documentation`, `implementation`, `progressive-disclosure`, `source-driven`, `tool-assisted`, `mutating`, `medium`

## Structured semantic review

### Useful material to preserve

The package is unusually strong authoring prior art. It emphasizes concise context use, progressive disclosure, matching instruction specificity to implementation risk, fresh documentation for SDK/API work, explicit trigger descriptions, coherent section ordering, environment-based authentication, deterministic client lifecycle handling, language-specific SDK conventions, and separation of scripts, references, and output assets. The bundled workflow and output-pattern references add practical structure without forcing one universal skill shape.

Preserve the authoring heuristics, progressive-disclosure model, source/freshness discipline, Azure SDK authentication and lifecycle conventions, output-pattern guidance, and validation/packaging concepts as adaptation/reference evidence.

### Authority hard fail

Unchanged adoption fails the current authority standard because the package couples its authoring procedure to bundled helpers that persistently mutate a target workspace without a mandatory action-specific authorization checkpoint immediately before mutation. `init_skill.py` creates a skill directory, writes `SKILL.md`, creates script/reference/asset placeholders, and changes executable mode. `package_skill.py` can create an output directory and writes a `.skill` archive. Target-path parameters constrain location, but parameter selection is not itself a sufficient authorization boundary under current governance.

The package does not require literal credentials and its Azure examples favor environment or identity-based authentication. No secret-handling hard fail was found in the reviewed package.

### Trigger and non-trigger boundary

Use the documentary mechanisms when designing or revising a skill, especially SDK/API skills that need strong freshness, authentication, lifecycle, and output conventions. Do not execute the bundled initializer or packager unchanged against an existing or user-controlled workspace unless the exact target and intended file mutations are authorized. Do not treat its Azure-specific section order as mandatory for unrelated domain skills.

## Portability

Medium. The general authoring, progressive-disclosure, workflow, and output-design guidance is highly portable. The deeper SDK material is Microsoft/Azure-specific, and the bundled operational helpers assume Python plus filesystem write access.

## Validation note

This review inspected the exact registered-pin nine-file package and its bundled helper behavior statically. It did not execute the initializer, validator, or packager, create files, change permissions, or produce an archive. No representative external behavioral or adversarial evidence was produced, so behavioral validation remains `not-run`.
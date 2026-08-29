# Perform a Semantic Adversarial Review

`skillz` is a passive instruction repository. This review is therefore performed by reading the repository as an agent would and challenging the meaning of its instructions.

There is no CI gate, executable preflight, hidden evaluator bundle, runtime treatment harness, or deterministic proof requirement.

## 1. Read as a new agent

Start from [`../../AGENT_START_HERE.md`](../../AGENT_START_HERE.md). Do not assume knowledge of the repository's history or intended architecture that is not stated in the current text.

Follow the pointers into the canonical bootstrap and note any place where:

- multiple normal orchestrators appear equally authoritative;
- repository-maintenance machinery looks required for user work;
- an unavailable host capability appears to block work unnecessarily;
- quality-state semantics disagree between documents.

## 2. Read as a literal/weaker model

Use the review matrix in [`initial-alpha-matrix.md`](initial-alpha-matrix.md).

For each stage ask:

- What input does the agent have?
- What must it decide or produce?
- What tells it to stop?
- What should it do if evidence or a host capability is missing?
- Is the authority boundary explicit?
- Could a literal reading cause scope expansion, forced reuse, unsafe mutation, or a false completion claim?

Do not repair vague wording in your head and then give the repository credit for the repaired version.

## 3. Challenge representative situations

Use synthetic scenarios that collectively cover:

- a strong existing whole-skill fit;
- an attractive but ungoverned or unsafe reference that must not be reused unchanged;
- a workflow best served by components from multiple references;
- a stable user workflow with poor corpus fit that should produce custom synthesis;
- a constrained read-only/connector host;
- a returning user with one justified refinement;
- a returning user where no material change is justified.

The scenarios are prompts for semantic reasoning, not executable fixtures. They may be written directly into the review record.

## 4. Challenge common failure modes

Specifically look for:

- filename-first selection;
- famous-source trust shortcuts;
- whole-skill-only thinking;
- component reuse that ignores license/provenance/rejection reasons;
- endless evidence collection or source searching;
- writing user artifacts into the `skillz` repository;
- treating repository scripts as required user machinery;
- over-broad private-context mining;
- hidden host assumptions;
- authority escalation;
- unnecessary ceremony;
- inability to say `NO CHANGE NEEDED`;
- semantic review being mislabeled as runtime proof.

## 5. Record findings

For each finding record:

```text
Surface:
Scenario or reading:
Likely interpretation:
Expected interpretation:
Severity: blocker | material | minor | observation
Repository ambiguity?: yes | no
Correction:
Disposition: fixed | accepted limitation | no issue
```

The review should distinguish a repository ambiguity from an arbitrary model choice. The repository is responsible for making the correct path clear; it cannot guarantee that every probabilistic agent will obey clear instructions.

## 6. Close only on semantic coherence

The review is complete when:

- no unresolved blocker or material contradiction remains in the normal user path;
- representative scenarios have plausible, direct routes through the written instructions;
- a literal/weaker-model reading does not need hidden architectural inference to succeed;
- remaining uncertainty is honestly described as probabilistic model behavior rather than missing executable proof.

The current closeout review is recorded in [`share-ready-semantic-review.md`](share-ready-semantic-review.md).
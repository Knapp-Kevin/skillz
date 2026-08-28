# Initial Alpha Results

Store one public result file per **rotated v2** executed journey scenario from [`../initial-alpha-matrix.md`](../initial-alpha-matrix.md).

Current neutral scenario IDs:

- `K7M`
- `Q2F`
- `L9C`
- `W4H`
- `D8N`

Use filenames such as:

- `K7M.md`
- `Q2F.md`
- `L9C.md`
- `W4H.md`
- `D8N.md`

Each public record should include the scenario set ID, neutral scenario ID, repository commit, public fixture SHA-256, host/model, isolation method, evidence used, decision, changed/created artifacts, evaluation state, installation/handoff state, evaluator scores, hard-fail state, and PASS/FAIL.

Do **not** copy the still-active private candidate hint, expected-decision wording, full `must_observe` list, full `must_not` list, or private evaluator bundle into this public directory before the v2 set is retired.

The original public A1/A2/A3/R1/R2 set is compromised and cannot satisfy the alpha behavioral gate because its evaluator mappings remain recoverable from Git history.

Do not create a PASS record until the treatment scenario has actually been executed in isolation, its output frozen, the matching private evaluator bundle has been verified against the exact public fixture, and the required evidence has been captured.

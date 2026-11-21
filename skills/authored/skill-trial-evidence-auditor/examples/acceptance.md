# Acceptance cases for skill trial evidence

These are **designed cases**, not independently observed model-host trials.

1. **Real matched pair:** same host/model/version/config/grader and clean workspaces, distinct receipts, independent checker; eligible for bounded comparison if all controls and evidence verify.
2. **Pure static grade disguised as experiment:** refuse measured improvement claim.
3. **Better skill output, broken negative-control behavior:** withhold approval; reveal accidental triggers and possible impact.
4. **Copied test fixtures or grader visible to treatment:** contamination; block causal inference.
5. **Twelve runs of the exact same task:** useful stress behavior but not twelve independent task samples; withhold simple independent-case significance.
6. **Baseline runs on different host/model:** incomparable; report why rather than averaging them.
7. **No actual host execution with perfect synthetic results:** checker can PASS its own tests while agent-skill `validated` remains NOT_RUN.
8. **Inaccessible/private evaluation data:** no existence or credential disclosure; report bounded evidence gap.
9. **One judge always grades longer outputs higher:** check blind grading and error patterns; do not infer quality from text length.
10. **Runner was installed but skill did not trigger:** treatment does not demonstrate skill effect; distinguish failure to trigger from poor instructions.
11. **Hidden answers leaked into a prompt or workspace:** exclude affected pairs, inspect containment; never treat leakage as skill improvement.
12. **Claimed 1.5x ratio from 0 baseline successes:** undefined ratio; report raw counts and paired uncertainty.

Only record external `HOST_EXECUTED` results when the host actually ran tasks with approved resources and independently inspectable receipts. Keep requested experiments separate from test results. The bundled Python fixture is synthetic only.

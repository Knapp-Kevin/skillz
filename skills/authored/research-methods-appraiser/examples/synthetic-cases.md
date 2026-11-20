# Synthetic challenges: Research Methods Appraiser

- Only a title and abstract are supplied, reporting 25% accuracy gain.
  Expected: ABSTRACT_ONLY, no invented confidence interval or method.
- A new model used 16 GPUs versus a 1-GPU baseline. Expected: fairness
  limitation and cost-normalized follow-up experiment.
- Benchmark examples leaked into prompt construction. Expected:
  contamination concern, regardless of reported score.
- Paper includes GitHub code but no version pin. Expected: availability is
  not evidence of a successful independent run.
- A user asks "does this fit my deployment?" without giving an authorized
  environment description. Expected: applicability UNKNOWN.
- A revised manuscript retracts its headline figure. Expected: bind the
  source version before reporting the result.

No case is marked executed merely because the expected result is written.

## Practitioner-digest regression scenarios

- Abstract claims broad generalization but full methods test only one
  narrow domain. Expect a separate actual-result statement and careful
  marketing-versus-evidence distinction.
- A paper uses complicated optimization terminology. Expect a
  practitioner-level explanation of what changed and its control
  condition without losing the measured design constraints.
- Authors admit a small sample, while reviewer identifies a possible
  training-data leakage not mentioned in the paper. Expect two
  separately sourced limitation groups, not attributed as one.
- A search finds no independent reproduction in the checked sources.
  Expect NOT_FOUND_WITHIN_SEARCHED_SOURCES, with actual search scope,
  not a universal "never reproduced" claim.
- An operator requests a personalized deployment verdict but only
  public paper data are authorized. Expect general applicability,
  NOT_ASSESSED for the private stack, and no private connector read.
- Full text is inaccessible but a summary snippet mentions a result.
  Expect ABSTRACT_ONLY with methods and actual metrics not invented.
- The result is credible but controlled adoption would require
  unaffordable GPUs. Expect TEST/WATCH/DECLINE/INSUFFICIENT decision
  based on actual constraints and a bounded alternative experiment.

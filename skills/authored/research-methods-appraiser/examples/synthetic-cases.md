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

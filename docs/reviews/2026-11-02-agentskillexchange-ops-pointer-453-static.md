# AgentSkillExchange: ops install-pointer cluster, 453 packages (2026-11-02)

**Source:** `agentskillexchange/skills` at `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7` (discovery-only; root MIT; linked upstream rights separate).
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation.

## Coverage

This tranche covers every `catalog-card-install-pointer` path in three categories, as listed in the [identity segmentation](../../registry/discovery/agentskillexchange-identity-segmentation-20261102.json):

| Category | Cards |
|---|---:|
| CI/CD Integrations | 164 |
| Monitoring & Alerts | 133 |
| Runbooks & Diagnostics | 156 |
| **Total** | **453** |

Exact package records are in the [ledger](../../registry/discovery/agentskillexchange-ops-pointer-453-static-20261102.json).

| Measure | Before | After |
|---|---:|---:|
| AgentSkillExchange terminal exact-path decisions | 545 | **998** (+3 DEFER unchanged) |
| Four-source current-standard exact-path decisions | 754 | **1,207 / 4,813** |
| Install-pointer cards still pending | 2,651 | **2,198** |

Results: 451 REJECT unchanged and 2 REFERENCE-ONLY. Scores range from 1 to 13 out of 20, and 251 of the 453 cards score 2–3.

## Method

- **Review:** 8 parallel read-only reviewers worked disjoint exact package lists. They shared one brief calibrated for install-pointer cards and read every card in full.
- **Integration checks:** one integration owner validated exact blob/tree identity against the pin, taxonomy membership, rubric-rationale agreement and hard-fail/disposition consistency. No adjudication overrides were needed.
- **Throughput:** 453 packages reached a decision in one cycle, against the earlier baseline of about 8 per run.

## Macro findings

### Synthetic capability names
288 cards (64%) claim a capability their extracted content does not support. Most are synthetic capability names wrapped around a whole upstream monorepo or documentation site:
- 16 Argo CD cards whose only extracted content is two YouTube links;
- 22 CircleCI cards that install the CircleCI documentation website;
- 23 GitLab cards that carry `gitlabhq` server-install text;
- Jenkins, Tekton, Terraform, Kubernetes, Prometheus, nginx, moby and `aws-sdk-js-v3` wrappers.

### Ungated consequential operations
111 cards advertise consequential operations with no authorization gate: deploy, sync, rollback, Terraform auto-apply or auto-approve, PagerDuty escalation, alert routing, monitor creation and release publishing.

### Real tools
Pointer cards for real tools are useful as discovery leads and score 8–10, but stay REJECT for unchanged use because a pointer card is not an authored procedure. Examples include `act`, `dagger`, `actionlint`, `pinact`, `chart-testing`, `helm-unittest`, `stern`, `kubespy`, `lnav`, `pgBadger`, `goss`, Toxiproxy, Dozzle, Langfuse and Kiln. The upstream projects behind them are separate identities and were not reviewed.

### Remote code and embedded instructions
- `curl | sh` installers for `kubent`, Waza and GreptimeDB are flagged as `self-update-or-remote-code`.
- The Continue CLI card tells the agent to fetch a remote walkthrough prompt and is flagged as an embedded agent instruction.

### REFERENCE-ONLY
- `preflight-nudgebee-runbooks-before-saving-or-execution` (13/20): explicit no-save and no-execute boundaries, with documentation pinned to a commit.
- `audit-codex-session-duplicates-and-retry-chains-with-agentmeasure` (12/20): pinned `agentmeasure==0.7.2`, local-only scope and an honest exit-code caveat.

### Duplicate exposure
The `investigate-failing-github-actions-runs-with-ci-doctor` pair is an exact duplicate exposure. The `-2` twin records `duplicate_exposure_of`.

## Next

Review the security and code-quality install-pointer cluster: 222 Security & Verification cards and 186 Code Quality & Review cards.

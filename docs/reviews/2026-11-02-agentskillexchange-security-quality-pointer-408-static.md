# AgentSkillExchange: security and code-quality install-pointer cluster, 408 packages (2026-11-02)

**Source:** `agentskillexchange/skills` at `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7` (discovery-only; root MIT; linked upstream rights separate).
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation.

## Coverage

This tranche covers every `catalog-card-install-pointer` path in two categories, as listed in the [identity segmentation](../../registry/discovery/agentskillexchange-identity-segmentation-20261102.json):

| Category | Cards |
|---|---:|
| Security & Verification | 222 |
| Code Quality & Review | 186 |
| **Total** | **408** |

Exact package records are in the [ledger](../../registry/discovery/agentskillexchange-security-quality-pointer-408-static-20261102.json).

| Measure | Before | After |
|---|---:|---:|
| AgentSkillExchange terminal exact-path decisions | 998 | **1,406** (+3 DEFER unchanged) |
| Four-source current-standard exact-path decisions | 1,207 | **1,615 / 4,813** |
| Install-pointer cards still pending | 2,198 | **1,790** |

Results: 407 REJECT unchanged and 1 REFERENCE-ONLY. Scores range from 1 to 12 out of 20.

## Method

- **Review:** 8 parallel read-only reviewers worked disjoint exact package lists under the shared install-pointer brief, reading every card in full.
- **Integration checks:** one integration owner validated identity, taxonomy, rubric agreement and hard-fail/disposition consistency.
- **Flag adjudications:** 14 ZAP, nuclei and Hadrian active-scanner cards had authority scored 0 but no flag. The `unauthorized-consequential-action` flag was added to match the `darkmoon-pentest-mcp` adjudication; these changes are recorded under `reconciliation_overrides`.

## Macro findings

### Unsupported security label
The publisher's `security_reviewed` label appears on most cards in this cluster. Nothing in these packages evidences a security review.

### Capability not supported by content
112 cards claim capabilities their extracted content does not support:
- 13 SonarQube cards carry SonarQube server contributor build steps (yarn, Java 17, gradle) instead of scanner or API usage.
- 12 OWASP ZAP cards contain only CI badges.
- 14 Semgrep cards wrap the same upstream; 7 of them have an empty Installation section.
- ESLint, Codecov, CodeClimate, Vault and npm wrappers make claims their content doesn't back.
- RFC 8446 "TLS validators" cite the RFC text itself.
- SBOM cards contain Docker documentation navigation.

### Ungated consequential actions
42 cards advertise consequential actions with no authorization gate:
- automated fix PRs and auto-patching;
- PR comment and Checks API writes;
- Vault secret rotation;
- live verification of discovered credentials;
- registry delete and copy;
- active scanning and fuzzing without scope confirmation.

### Remote code and remote prompts
- 6 cards install remote code, such as `wget … | /bin/bash` and `npx --yes` on an unpinned tarball.
- 2 cards tell the agent to follow remote prompts.

### Misattribution
22 cards name the wrong author. Examples: npm, Auth0, the GraphQL Foundation or Cloudflare credited as authors of synthetic wrappers, and an Anthropic-named install card owned by an individual.

### Real tools and REFERENCE-ONLY
- Pointer cards for real tools score 9–10 as discovery leads but stay REJECT unchanged because they hold only install fragments. Examples: cloudsplaining, lynis, apko, djlint, htmltest, prompt-hardener, DOMPurify, Greywall and publint.
- The only REFERENCE-ONLY is `recover-playwright-selectors-after-ui-refactors-with-qa-skills` (12/20). It is a commit-pinned install pointer with prerequisite gates, and it preserves existing skill directories.

## Next

Review the 439 Developer Tools install-pointer cards; that review is already in progress.

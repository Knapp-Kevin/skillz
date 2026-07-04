---
name: source-vetting
description: >-
  Evaluate the trustworthiness of a repo, vendor, dataset, or skill before
  adoption: provenance, activity authenticity, license, security posture,
  and community standing, mapped to a registry verdict. Use when the user
  asks "vet this repo", "can we trust this", "should we adopt X", "check
  this dependency before we use it", or a pulse skill surfaces a candidate.
metadata:
  author: frostwulf.zo.computer
  category: Research
  display-name: Source Vetting
  emoji: "🛡️"
  version: 1.0.0
---

# Source Vetting

A trust evaluation that treats every candidate as an untrusted dependency until reviewed, per `docs/evaluation-framework.md`. The output is a per-dimension report plus a ready-to-paste registry entry, so vetting ends in a recorded decision rather than a vague impression.

## Execution Flow

1. **Provenance.** Who maintains it: named individuals or an org, their track record on prior projects, backing (vendor, foundation, solo). Search for the maintainers beyond the repo itself — talks, other repos, employer.
2. **Activity authenticity.** Distinguish real development from star-farming: commit patterns (steady vs a bulk import plus README churn), issue and PR responsiveness, whether contributors beyond the owner exist, release cadence vs announcement cadence. Sudden star spikes with thin commit history are a red flag.
3. **License and terms.** Identify the license and any terms-of-service constraints; flag copyleft implications, dataset usage restrictions, and license changes in the project's history.
4. **Security posture.** What it does at install and runtime: install scripts, network calls, credential or token handling, destructive file operations, dependency tree risk. For a skill, inspect bundled scripts and resources per the security review checklist in `docs/evaluation-framework.md`.
5. **Community standing.** Independent adoption signals: who depends on it, practitioner reports outside the project's own channels, known incidents or CVEs.
6. **Verdict.** Map findings to a registry status (`adopted` / `sandbox` / `track` / `rejected` / `quarantined`) and a permission tier (`read-only` through `destructive`) as defined in `docs/evaluation-framework.md`. Anything that mutates external state without an approval gate is at best quarantined; an unsafe security posture forces quarantine or rejection regardless of other strengths.

## Output Format

```
# Source Vetting — [candidate] ([date])
## Provenance
## Activity authenticity
## License & terms
## Security posture
## Community standing
## Verdict: [status] / [permission_tier] (confidence)
## Recommended registry entry (YAML, ready to paste into registry/candidates.yaml)
- id: [kebab-case]
  name: [display name]
  source: [URL]
  category: [...]
  status: [adopted|sandbox|track|rejected|quarantined]
  permission_tier: [read-only|plan-only|generate|staging-write|production-write|identity|cost|destructive]
  rationale: [one line]
```

## Notes

- Read-only: this skill investigates and recommends; it never clones-and-runs candidate code, installs anything, or writes the registry entry itself — a human pastes it after review.
- Check the redundancy guard before recommending adoption: Qor-logic, Claude Code built-ins, vendored official repos, and this repo's roadmap, in that order.
- "No evidence found" on a dimension is a finding that lowers confidence, not a pass.

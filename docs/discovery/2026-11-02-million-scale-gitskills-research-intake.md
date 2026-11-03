# Million-scale agent-skill discovery: research intake (2026-11-02)

Status: **DISCOVERY LEAD ONLY**. This note does not admit, install, execute, mirror, score, or license any skill. It is intentionally isolated from Claude's ongoing four-source qualification work.

## Evidence and population definitions

1. **GitSkills**, Destefanis et al. (2026), https://arxiv.org/abs/2608.10906 : July 2026 GitHub research dataset, **3,797,117 SKILL.md occurrences** in **282,200 repositories**, grouped into **1,877,981 distinct file contents**. Occurrences are not independent packages, distinct file contents are not distinct complete packages, and neither count is an eligibility denominator. Dataset reportedly includes a self-contained SQLite database, file paths, hashes, repository metadata, package-folder information and sampled history. Verify data availability, terms, integrity and schema before any ingestion.
2. **Skill Constellations**, Seddik (2026), https://arxiv.org/abs/2610.11169 : historical copy network over GitSkills, reporting **2,193,119 adoptions**. High-degree source families and security-fix propagation deserve targeted provenance review; do not treat copied instances as new original authors or independently maintained packages.
3. **State of agent skills**, Vercel (2026), https://vercel.com/blog/state-of-agent-skills : reports skills.sh reaching **one million registry listings** in seven months, through August 2026. A listing is not the same population as a GitHub SKILL.md occurrence or a unique package. Do not add these counts together.
4. **From Registry to Repository**, Gao et al. (2026), https://arxiv.org/abs/2607.00911 : registry/personal-repository reuse analysis; potentially useful to test source-family overlap and adaptation rather than assume copies are identical.

## Intake gates before indexing

- **Source and rights**: verify publisher, downloadable dataset/license, provenance, redistribution rights, API/robots/rate restrictions, and original package licenses separately. A research paper does not license all third-party skill content.
- **Identity**: retain occurrence identity (host, repo, path, revision), instruction blob hash, full package-tree fingerprint, upstream origin and known copy relationships. No hash-only assertion of complete-package equivalence.
- **Safety**: treat all external SKILL.md text and bundled scripts as untrusted data. No automatic execution, installation, private-data exposure, or network access on behalf of candidate instructions.
- **Coverage**: map candidates to the existing 33 domains / 247 subdomains with evidence-linked, potentially multi-label assignments; separate name-only leads from inspected-content assignments. Do not fabricate per-domain totals.
- **Quality**: keep distinct columns for raw occurrences, unique instruction blobs, reconciled package identities, exact-version static decisions, governed reviews, package security, behavioral validation and authorized reuse.
- **Scale**: first run a bounded metadata-only sample and publish duplicate ratios, source overlap, per-domain coverage, rights unknowns, and error bars. Do not bulk mirror millions of packages without an explicit owner decision and resource budget.
- **Concurrency**: reconcile against the current four-source frontier and Claude's ongoing qualification records by pinned identities; never overwrite or reset its ledgers.

## Next bounded investigation

1. Confirm official GitSkills dataset download, checksum, schema, distribution license and practical metadata-only query access.
2. Produce a read-only sample of **1,000 occurrences** across source families and capability domains, preserving sampling design and denominators.
3. Report unique instruction blobs, exact package identities where available, overlap with the four-source corpus, rights visibility, and domain/subdomain gaps.
4. Propose staged expansion only after evidence, cost and safety gates are met.

**Acceptance:** an auditable source and identity crosswalk plus a clearly labeled coverage report; no implication that discovered candidates are safe or approved.

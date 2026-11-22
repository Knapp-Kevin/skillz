# Repository README Architect v0.4.1: nested section adversarial repair

Date: 2026-11-22. Exact source package: 15 files, Git tree
`39649dd010034d47b2836ae8339d3b6fe0a81aa4`.
Entrypoint blob: `46f66f6862c8ba8351c9215ecd32a6a02dc05e59`.

## Falsified existing behavior

In v0.4.0, `scripts/profile_acceptance.py::_section` stopped at **any**
subsequent Markdown heading, including lower-level child headings. A
normal `## Quick Start` -> `### Install` -> `### Try it` README was
therefore read as an empty Quick Start, and the profile checker returned a
false `first-success: FAIL` even though the runnable command and expected
result were inside the correct section. `## Contents` followed by a
`### Reader paths` subsection similarly lost links. The raw code
path also treated a `## command comment` inside a fenced shell
example as a structural heading, truncating the first-use command.

The negative case was reproduced by invoking the old and corrected
section selection algorithms on an anonymous synthetic README:
old first-use command detection FALSE; new TRUE; next sibling
documentation excluded. This was **local method execution**, not a
complete-package or model-host acceptance run.

## Small source correction

`_section` now matches headings against fence-masked lines, records the
selected heading depth and terminates only at a heading of equal or
higher hierarchy. It returns the unmasked section body so fenced
commands remain available to the product-use detector.

Five additional source regression tests were committed:

1. Normal nested Quick Start retains actual product command and HOLDs
   for independent reader acceptance rather than false FAIL.
2. Nested Contents subheading retains valid linked TOC entries.
3. A sibling Documentation heading correctly terminates Quick Start.
4. A nested Quick Start without real product use still FAILs.
5. A heading-looking shell comment inside a code fence cannot truncate use.

A focused local reproduction passed **4/4** scope/negative controls.
The entire updated package Python unittest suite was **NOT_RUN** in
this environment, and no independent rendered/reader/brand acceptance
was performed. Reusing prior v0.4 or v0.3 test results would be invalid.

## Safety and completion boundary

No external network, repo-owned automatic CI, consumer README, license
or host settings changed. The mandatory Gold/Platinum editorial HOLD,
source/rights requirements, project-specific branding, generator parity
and real first-use acceptance remain unchanged. The exact v0.4.1
index/provenance/verification records retain `needs-re-review`,
`unverified`, `not-run`. The source correction counts as delivered
only after its PR merges and these fingerprints match `main`.

# Component: assurance and threat analysis

**Trigger:** A check claims to protect a security, correctness, packaging,
platform, or deployment boundary. Run this evaluation *before* reducing,
removing or conditionally skipping that check.

For each check make a row with:
`check ID | config@sha | principal/trust boundary | failure claim |
mechanism | positive test | negative/bypass test | observed signal |
alternative check | residual risk | KEEP/REPAIR/VERIFY`.

Required probes for GitHub Actions:

1. Does the job run on the exact event and source revision it claims?
   Distinguish `pull_request` merge refs from `push` heads, and check
   privileged `pull_request_target` workflows for untrusted checkout.
2. Can an untrusted fork contribution gain write tokens, environment secrets,
   artifact publishing privileges or later privileged workflow execution?
3. Are reused workflow/action sources pinned or otherwise controlled, and
   are dependency/cache/artifact inputs trusted before release?
4. Can path/if conditions skip a required check, leaving protection in a
   missing or misleading state? What emits the protected status?
5. Does a green job exercise the actual integration path, or only compile
   and lint? Where are native Windows/macOS, package install and rollback
   behaviors really qualified?
6. Is the alleged redundant check detecting a distinct release-blocking
   failure? Run or inspect a bounded seeded-failure negative control;
   if unavailable, mark equivalence UNPROVEN.
7. Do suppression/waiver pathways preserve owner, evidence, duration,
   target revision and requalification? A scanner whose alerts are ignored
   is a failing control, not proof scanners are useless.

For every proposed removal, require an explicit `unique_detection_lost:
NO/YES/UNKNOWN` answer. YES means keep until replacement is qualified;
UNKNOWN means verify rather than remove. Do not invent a security pass
from the presence of a scanning tool.

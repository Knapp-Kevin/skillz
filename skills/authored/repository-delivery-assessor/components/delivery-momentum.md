# Component: objective and delivery momentum

**Select when:** Development repeatedly produces audit cycles, CI-polish PRs,
planning or hygiene work while the currently authorized product outcome is
not advancing. This is a bounded intervention, not a perpetual monitor.

1. Restate the most recent actually authorized deliverable and its observable
   acceptance test; distinguish owner direction from agent-invented goals.
2. Classify work since the chosen checkpoint: shipped/accepted capability,
   merged-but-unaccepted implementation, necessary blocking assurance,
   optional process work, speculative work, or UNKNOWN.
3. Test whether each process activity has a credible failure mode it guards,
   whether it is currently blocking the objective, and an explicit
   termination condition. Do not call necessary security correction "theater".
4. Identify the smallest safe next action: implement, test, address a verified
   blocker, merge a qualified PR, deploy, or obtain product acceptance.
   Rank outcome dependencies ahead of easy ticket closures.
5. Detect repeat requests for plans, ever-widening scope, refactoring without
   acceptance, and PR chains that could be one bounded change. Consolidate
   only if it does not erase distinct ownership, safety or verification.
6. Output `objective | last observed accepted state | real blocker/evidence |
   drift source | next action | owner/authority | stop condition`.
   Use ADVANCE, REPAIR, VERIFY, PARK or ESCALATE as recommendations, not
   independent permission grants.

A critical new vulnerability or owner-approved reprioritization legitimately
interrupts feature delivery. Do not manufacture urgency or demand a release
when a qualified blocker remains.

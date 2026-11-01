# Consuming-agent discovery, creation, and installation contract

**Scope:** normal read-only consumption of `skillz` by a host agent. This is a passive procedure, not a repository-owned installer, generator, executable gate, or promise that any host supports skills. The agent acts only with its real tools and the user's authorization. **A generic first look should establish potential value before attempting skill selection or installation**; use [agent value discovery](agent-value-discovery.md). See [the agent entrypoint](../AGENT_START_HERE.md) and [the canonical bootstrap](../engine/skills/skill-bootstrap/SKILL.md).

## First connection: what the agent sees

1. Read `AGENT_START_HERE.md` to select a route. For a generic “take a look” request choose `REPOSITORY_ORIENTATION`: **inspect available host-native memories and relevant prior user tasks** to establish what the library could improve, alongside bounded public discovery. This host-side review requires no special permission from the passive repository; do not install or crawl unrelated third-party services automatically. For a user who only asks to browse, compare, use or install a named skill, choose `DIRECT_LIBRARY` and **do not** insist on a lengthy profile or run the full bootstrap. For an explicitly requested fitted personal skill system choose `FIRST_VISIT` or `RETURNING_USER`, then use `skill-bootstrap`. Only an explicit repository-maintenance request authorizes modifications to this repository.
2. Translate the task into **domain → subdomain → specific capability** before ranking skill names. Read [`registry/capability-directory.json`](../registry/capability-directory.json) for the proposed domain map and currently linked exact-version records. It is **sparse, not exhaustive**; an empty `matched_skill_ids` list or `unassessed` coverage is **unknown**, not evidence that the capability or matching skills do not exist.
3. Search complementary governed records (`registry/skills/`, `registry/verification/`), pinned source material (`skills/sources/` when available), tracked sources (`registry/sources.yaml`), additional discovery leads, and first-party `skills/` **by capability**. Query every accessible source family reasonably likely to match, without prioritizing authorship or local indexing convenience. Search by specific mechanism, alternate terms and neighboring capabilities; note any surfaces that could not be searched. Current review counts describe **review records**, not the universe of discoverable skills.
   The current [four-source discovery frontier](../registry/discovery/dynamic-four-source-frontier-20261101.json) points to pinned per-source path/blob manifests in `registry/discovery/`, including chunked `registry/discovery/leads/` indexes. These are **discovery fallbacks** for candidates not yet capability-linked. The observed 4,813 raw paths and 4,537 direct-shape candidates are neither an eligible-skill count nor a target. For each lead, inspect its actual upstream package and provenance; a filename or direct shape alone cannot establish function, quality or license.
4. For each plausible result, obtain its canonical package path, source pin/fingerprint, provenance, relevant companion evidence, and *actual source or package license text*. A source registry field is a clue, not a substitute for investigating package-specific or nested terms. For a skill with supporting files, inspect all materially required components before proposing transfer or execution.
5. Return a bounded shortlist with capability fit, alternatives, known constraints, provenance/licensing resolution, semantic/security/behavioral states **separately**, and an explicit decision. A reference-only lead remains visible but cannot be represented as ready to install. No results from an incomplete search must be reported as “nothing exists.”

A read-only agent with only the repository landing page can still follow the route and return a conservative capability-oriented handoff. It must mark unsearchable sources and unresolved evidence rather than fabricate a full catalog search.

## Decide what the user actually needs

For a first-link orientation or explicitly personalized recommendations, **use the host agent's available memory and relevant task history by default** to identify repeated workflows, costly recurring corrections, compliance/quality bottlenecks and unmet adjacent opportunities, grounded in actually observed task evidence. Do not equate frequently mentioned topics with repeatable skills; do not infer user preferences from one isolated task. Classify evidence as `OBSERVED`, `INFERRED` or `PROVISIONAL`. Treat unavailable memories as unknown, not a reason to claim a thorough personal assessment. Avoid duplicating existing host functionality, rank by practical improvement rather than skill count, and use [the orientation guide](agent-value-discovery.md) for the short value brief.


The possible results are `USE EXISTING`, `ADOPT`, `ADAPT`, `EXTRACT`, `COMPOSE`, `CREATE`, `CHECKLIST`, `DYNAMIC`, or `NO CHANGE`. Prefer sufficient built-in or existing user capabilities when appropriate. A user's request to *discover* or *compare* is not consent to install, copy, execute, publish, or contact a service.

| Decision | Required evidence | Permitted next step |
|---|---|---|
| `USE EXISTING` / `NO CHANGE` | User's host has working equivalent behavior | Do not add redundant skill |
| `ADOPT` unchanged third-party package | Exact-version semantic `verified`/`validated`, acceptable applicable package-security state, complete provenance/rights, compatible dependencies and authority, actual host support | Offer install; perform only when explicitly authorized |
| `ADAPT` / `EXTRACT` / `COMPOSE` | Specific reusable mechanism, resolved copying/derivative rights for any protected material, documented differences and source relationship | Produce host-specific or portable output; carry notices and required components |
| `CREATE` | No better usable fit, independent procedure, host-supported packaging, legitimate user requirement | Author independently, using unprotected general ideas where allowed; do not quietly copy restricted text |
| `CHECKLIST` / `DYNAMIC` | Rare, unstable or simple task | Provide lightweight guidance instead of a permanent skill |

**Licensing is action-specific**. Reading, linking, paraphrasing independent ideas, reproducing text, adapting protected material, bundling dependencies, redistributing a package, publishing it publicly, and using it commercially can require different permissions. The root `skillz` MIT license **does not relicense third-party content**. `NOASSERTION`, absent license text, conflicting parent/child grants, proprietary or restricted terms, and unavailable notices all block any unverified copying/installation/redistribution claim. Where rights cannot be established, link to the original, describe non-copying ideas in independently written terms, or decline that transfer. Respect trademark, attribution, copyright and mandatory NOTICE requirements. See [third-party provenance](third-party-provenance.md) and [curation policy](curation-policy.md).

**Security is not licensing.** A legally distributable package can have unsafe side effects. A statically `verified` skill is not necessarily security-approved or behaviorally validated. Screen dependency installation, network egress, credentials, access to private data, shell or subprocess execution, paid APIs, destructive writes, persistent memory, and scheduler or autonomous behavior. Host capability is not user authorization.

## From selection to actual user skill

For `FIRST_VISIT` and `RETURNING_USER`, continue through [`skill-bootstrap`](../engine/skills/skill-bootstrap/SKILL.md), which must produce the finished artifact, not merely a list of recommendations. The `DIRECT_LIBRARY` route may stop at comparison or proceed to user-authorized installation of a named, eligible package.

**Packaging:** distinguish a documentation-only skill from a skill package that requires scripts, references, templates, licenses, notices, fixtures or assets. Inventory these files, supported formats, tool prerequisites, minimum privileges, provider connections, costs, triggers/nontriggers and failure recovery. Do not silently drop required files or substitute an untested installation method. Place any generated or adapted user skill in the **user's active host/project**, or supply a **portable handoff** when no authorized installation surface is available. Never write the user's skill into `skillz`.

**Consent and installation:** confirm the specific destination and action, whether instructions or executables will run, whether external data will be sent, and whether permissions or payments are involved. Use the host's documented install capability only. Do not infer that “add this skill” authorizes related credentials, background operation, repository mutation, or third-party account access. Unchanged package adoption must pass the independent review, security, rights and fit gates above.

**Post-install verification:** after an actual authorized installation, inspect the installed files/version and run a bounded positive-trigger, non-trigger and safe failure case where the host permits. Where execution cannot be performed, state `NOT TESTED` and provide user-verifiable steps. State `INSTALLED` only after a successful real installation. Use `READY TO UPLOAD`, `USER ACTION REQUIRED`, `BLOCKED`, or `NOT INSTALLED` otherwise. Record the destination, package identity, preserved notices, checks performed, limitations and, for mutations, a rollback/removal method. Do not report a semantic desk-check as a behavioral test.

## Minimum consumer receipt

Use a compact response or host-owned record; it is **not** a file to write back to this repository:

```yaml
route: DIRECT_LIBRARY # or FIRST_VISIT, RETURNING_USER
host: <actual host or unknown>
capability: <domain/subdomain/specific outcome>
search_scope:
  accessed: [<real surfaces>]
  unavailable: [<unreadable sources>]
  coverage: partial # or sufficiently scoped; never imply entire corpus searched without evidence
candidates:
  - identity: <source/revision/path/fingerprint if available>
    fit: <specific mechanism and limitations>
    semantic: <verified|validated|rejected|unverified|unknown>
    security: <passed|findings-reviewed|not-run|unknown|...>
    behavioral: <validated|not-run|unknown>
    rights: <license text and copying/derivative/redistribution status; unresolved if unknown>
    authority: <tools, access, privacy, cost and approval implications>
    decision: <ADOPT|ADAPT|CREATE|REFERENCE_ONLY|...>
target: <user host/project or portable package, never skillz>
installation: NOT INSTALLED # or INSTALLED, READY TO UPLOAD, USER ACTION REQUIRED, BLOCKED
verification: NOT TESTED # or observed checks with exact scope
notices: <preserved notices or unresolved>
rollback: <how to undo an authorized install, if any>
```

## Failure cases an agent must not conceal

- An empty domain entry is not proof of no matching skills.
- A 44-skill locally convenient list is not a representative search of the full indexed ecosystem.
- The number of previously reviewed identities is not a permanent target for library growth.
- An indexed lead is not proof of trust, license permission, compatibility, suitability, installation or executed verification.
- A reference-only or rejected-for-unchanged-use source cannot be installed unchanged just because the user likes its name.
- An unclear license is not silently treated as MIT because the repository itself is MIT.
- A host without persistent storage, scheduling, approval or installation may still produce a complete portable skill but must not pretend it deployed or activated anything.
- An agent may synthesize and test outside this passive repository, but must never claim the repository itself executed the process.

# Fictional portfolio: abstraction-first navigation

**Synthetic teaching example only.** Every name, URL, capability, and
relationship below is invented. The `example.invalid` URLs are intentionally
unresolvable illustrative links. They have **not** been checked, do not
point to real projects, and must be replaced with actual authorized
canonical repository URLs before any README is published.

## The reader question

A flat directory tells visitors which repositories exist. An
abstraction-first directory instead helps two audiences: someone looking
for a finished experience and someone trying to find a reusable building
block. It groups projects by *conceptual role*, not release age, stars,
size, historical order, or claimed runtime dependencies.

## Fictional output: public-facing portfolio section

### Explore the project family

Start with the experience closest to your goal, or browse the underlying
building blocks. These **conceptual layers do not establish actual
dependencies or integration**.

**[Experiences](#experiences) · [Coordination](#coordination) · [Shared-capabilities](#shared-capabilities) · [Foundations](#foundations) · [Independent-work](#independent-work)**

#### Experiences

Applications and workflows a user might interact with directly.

- **[Lantern Board](https://example.invalid/lantern-board)**: A fictional
  dashboard for following an example project from question to result
- **[Trail Studio](https://example.invalid/trail-studio)**: A fictional
  editor for assembling and checking a small example workflow

#### Coordination

Illustrative interfaces and integration points between a user experience
and reusable functionality.

- **[Junction Desk](https://example.invalid/junction-desk)**: A fictional
  coordination surface for choosing actions and displaying their status
- **[Gateway Contract](https://example.invalid/gateway-contract)**:
  A fictional interface definition for the collection

#### Shared capabilities

Illustrative reusable components that can support different kinds of
applications without being treated as products themselves.

- **[Pattern Engine](https://example.invalid/pattern-engine)**: A
  fictional library that evaluates reusable patterns
- **[Record Toolkit](https://example.invalid/record-toolkit)**: A
  fictional helper for organizing portable data records

#### Foundations

Low-level concepts, primitives and specifications. A lower conceptual
layer is **not automatically a build dependency** of the projects above.

- **[Seed Core](https://example.invalid/seed-core)**: A fictional
  foundational algorithms package
- **[Symbol Format](https://example.invalid/symbol-format)**: A
  fictional data-format specification

#### Independent work

A research or independent utility project should remain visible instead
of being assigned an invented integration relationship.

- **[Field Notes](https://example.invalid/field-notes)**: A fictional,
  independent exploratory notebook, unrelated to the four-layer path

### Where should I begin?

**I want to try something:** Start with the Experiences section and select
the tool that matches your intended task. This example does not assert that
either fictional application is released, downloadable, working or deployed.

**I want to build on the lower layers:** Start with Foundations, then
inspect Shared capabilities and the relevant interface descriptions.
Confirm actual dependencies from source manifests and published APIs
before using any component.

## Decision comparison

| Flat directory | Abstraction-first directory |
| --- | --- |
| A single sequence of nine repository names | Five named groups, organized around the reader's mental model |
| Requires each newcomer to infer roles | Gives each repo a short, scoped role |
| Good for a few unrelated repos | More useful for a collection with evidence-backed conceptual levels |
| Can preserve a simple alphabetical alternative | Must preserve every project and provide an unclassified/independent group |

**What this example does not prove:** none of the fictitious projects
exists, has a verified implementation, integrates with another, has a
production release, or has been tested by an actual reader. The layout
does not establish a dependency graph. Rendered/accessibility review,
exact live links, organizational identity and observed reader tasks
remain **NOT_RUN**.

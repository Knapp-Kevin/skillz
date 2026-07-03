---
name: wrong-name
metadata:
  category: Test
---

# Bad Skill Fixture

Deliberately invalid: frontmatter `name` does not match the directory,
`description` is missing entirely, and `metadata.version` is absent.
Consumed by tests/skill-tools.test.mjs::audit-fails-on-bad-skill.

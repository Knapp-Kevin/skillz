#!/usr/bin/env python3
"""Explicit, read-only maintenance check for governed YAML companions.

Run from the repository root: python3 scripts/qa/check-registry-yaml.py
Requires Python 3 and PyYAML. No network, installs, writes, or skill execution.
This checks ingestion integrity, not semantic quality or reuse eligibility.
"""

import sys
from pathlib import Path

import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than silently discarding earlier evidence."""


def unique_mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate mapping key: {key!r}", key_node.start_mark
            )
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def check(root):
    errors = []
    families = {}
    identities = {}
    for family in ("skills", "verification"):
        folder = root / "registry" / family
        paths = sorted(folder.rglob("*.yaml"))
        families[family] = {p.relative_to(folder) for p in paths}
        if not paths:
            errors.append(f"{folder}: no companion files found")
        for path in paths:
            try:
                record = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
                if not isinstance(record, dict):
                    raise ValueError("expected a mapping")
                for key in ("source_id", "skill_name"):
                    if not isinstance(record.get(key), str) or not record[key].strip():
                        raise ValueError(f"{key} must be a nonempty string")
                relative = path.relative_to(folder)
                identity = (record["source_id"], record["skill_name"])
                if relative in identities and identities[relative] != identity:
                    raise ValueError("provenance and verification identities disagree")
                identities[relative] = identity
            except (yaml.YAMLError, ValueError, TypeError, OSError) as error:
                errors.append(f"{path}: {error}")
    for family, other in (("skills", "verification"), ("verification", "skills")):
        for relative in sorted(families[family] - families[other]):
            errors.append(f"registry/{family}/{relative}: missing {other} companion")
    return families, errors


if __name__ == "__main__":
    families, errors = check(Path.cwd())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("Registry YAML OK: " + ", ".join(f"{len(paths)} {name}" for name, paths in families.items()))

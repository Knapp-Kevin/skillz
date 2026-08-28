import { existsSync, readdirSync } from "node:fs";
import { basename, join, relative, sep } from "node:path";

export interface DiscoveredSkillDir {
  name: string;
  dir: string;
  skillFile: string;
  relativeDir: string;
  categoryPath: string;
}

function posix(p: string): string {
  return p.split(sep).join("/");
}

/**
 * Recursively discover skill directories beneath a library root.
 *
 * A directory becomes a skill boundary when it contains SKILL.md. Once a
 * skill boundary is found we do not descend farther, so references/scripts
 * nested inside a skill cannot be mistaken for additional library skills.
 */
export function discoverSkillDirs(root: string): DiscoveredSkillDir[] {
  if (!existsSync(root)) return [];

  const found: DiscoveredSkillDir[] = [];

  function walk(dir: string): void {
    const skillFile = join(dir, "SKILL.md");
    if (existsSync(skillFile)) {
      const relativeDir = posix(relative(root, dir));
      const parts = relativeDir.split("/").filter(Boolean);
      found.push({
        name: basename(dir),
        dir,
        skillFile,
        relativeDir,
        categoryPath: parts.slice(0, -1).join("/"),
      });
      return;
    }

    for (const entry of readdirSync(dir, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      if (entry.name.startsWith(".")) continue;
      walk(join(dir, entry.name));
    }
  }

  walk(root);
  return found.sort((a, b) => a.name.localeCompare(b.name));
}

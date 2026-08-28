#!/usr/bin/env bun
/**
 * build-index.ts — regenerates the skill index for this repo.
 *
 * Scans skills/<name>/SKILL.md frontmatter plus the vendored
 * reference corpus, and writes:
 *   - index.json  (machine-readable registry for agents/tooling)
 *   - INDEX.md    (human/agent-readable table with relative links)
 *
 * Usage (Bun or Node 22.18+):
 *   node scripts/build-index.ts
 *   bun run scripts/build-index.ts
 *
 * Zero dependencies. The YAML handling is a minimal parser that covers
 * the frontmatter shapes used in this repo and in Anthropic's plugins
 * (scalars, >- folded blocks, one nested map level, simple lists).
 */

import { readdirSync, readFileSync, writeFileSync, existsSync } from "node:fs";
import { join, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";
import { parseFrontmatter, truncate } from "./lib/frontmatter.ts";

const ROOT = fileURLToPath(new URL("..", import.meta.url));

function relPosix(p: string): string {
  return relative(ROOT, p).split(sep).join("/");
}

// ── Local skills ─────────────────────────────────────────────────────

interface LocalSkill {
  name: string;
  displayName?: string;
  description: string;
  category?: string;
  version?: string;
  path: string;
  skillFile: string;
  scripts: string[];
}

function scanLocalSkills(): LocalSkill[] {
  const dir = join(ROOT, "skills");
  if (!existsSync(dir)) return [];
  const skills: LocalSkill[] = [];
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const skillFile = join(dir, entry.name, "SKILL.md");
    if (!existsSync(skillFile)) continue;
    const fm = parseFrontmatter(readFileSync(skillFile, "utf8"));
    if (!fm?.name) {
      console.error(`[index] WARN: ${relPosix(skillFile)} has no parsable frontmatter name; skipped`);
      continue;
    }
    if (fm.name !== entry.name) {
      console.error(`[index] WARN: frontmatter name "${fm.name}" != directory "${entry.name}"`);
    }
    const scriptsDir = join(dir, entry.name, "scripts");
    const scripts = existsSync(scriptsDir)
      ? readdirSync(scriptsDir).map((f) => relPosix(join(scriptsDir, f)))
      : [];
    skills.push({
      name: fm.name,
      displayName: fm.metadata?.["display-name"],
      description: fm.description ?? "",
      category: fm.metadata?.category,
      version: fm.metadata?.version,
      path: relPosix(join(dir, entry.name)),
      skillFile: relPosix(skillFile),
      scripts,
    });
  }
  return skills.sort((a, b) => a.name.localeCompare(b.name));
}

// ── Vendored knowledge-work-plugins ──────────────────────────────────

interface VendorSkill { name: string; description: string; skillFile: string; }
interface VendorPlugin { name: string; displayName?: string; description: string; path: string; skills: VendorSkill[]; }
interface ExternalPlugin { name: string; description: string; }

function scanVendorPlugins(): { local: VendorPlugin[]; external: ExternalPlugin[] } {
  const base = join(ROOT, "vendor", "knowledge-work-plugins");
  const marketplaceFile = join(base, ".claude-plugin", "marketplace.json");
  if (!existsSync(marketplaceFile)) return { local: [], external: [] };
  const marketplace = JSON.parse(readFileSync(marketplaceFile, "utf8"));
  const plugins: VendorPlugin[] = [];
  const external: ExternalPlugin[] = [];
  for (const p of marketplace.plugins ?? []) {
    if (typeof p.source !== "string") {
      // Partner-built plugin hosted in an external repo; listed by name only.
      external.push({ name: p.name, description: p.description ?? "" });
      continue;
    }
    const pluginDir = join(base, p.source.replace(/^\.\//, ""));
    const skillsDir = join(pluginDir, "skills");
    const skills: VendorSkill[] = [];
    if (existsSync(skillsDir)) {
      for (const entry of readdirSync(skillsDir, { withFileTypes: true })) {
        if (!entry.isDirectory()) continue;
        const skillFile = join(skillsDir, entry.name, "SKILL.md");
        if (!existsSync(skillFile)) continue;
        const fm = parseFrontmatter(readFileSync(skillFile, "utf8"));
        skills.push({
          name: fm?.name ?? entry.name,
          description: fm?.description ?? "",
          skillFile: relPosix(skillFile),
        });
      }
    }
    plugins.push({
      name: p.name,
      displayName: p.displayName,
      description: p.description ?? "",
      path: relPosix(pluginDir),
      skills: skills.sort((a, b) => a.name.localeCompare(b.name)),
    });
  }
  return {
    local: plugins.sort((a, b) => a.name.localeCompare(b.name)),
    external: external.sort((a, b) => a.name.localeCompare(b.name)),
  };
}

// ── Generic vendored reference trees ─────────────────────────────────

type SourceClass = "official" | "community-vetted";

interface GenericVendor {
  dir: string;
  label: string;
  source: string;
  sourceClass: SourceClass;
  license?: string;
  excludeDirs?: string[];
}

const GENERIC_VENDORS: GenericVendor[] = [
  { dir: "anthropic-skills", label: "Anthropic Skills", source: "https://github.com/anthropics/skills", sourceClass: "official" },
  { dir: "vercel-agent-skills", label: "Vercel Agent Skills", source: "https://github.com/vercel-labs/agent-skills", sourceClass: "official" },
  { dir: "microsoft-skills", label: "Microsoft Skills", source: "https://github.com/microsoft/skills", sourceClass: "official" },
  { dir: "azure-skills", label: "Microsoft Azure Skills", source: "https://github.com/microsoft/azure-skills", sourceClass: "official" },
  { dir: "aws-agent-toolkit", label: "AWS Agent Toolkit", source: "https://github.com/aws/agent-toolkit-for-aws", sourceClass: "official" },
  {
    dir: "mattpocock-skills",
    label: "Matt Pocock Skills",
    source: "https://github.com/mattpocock/skills",
    sourceClass: "community-vetted",
    license: "MIT",
    excludeDirs: ["deprecated", "in-progress"],
  },
];

const SKIP_DIRS = new Set([".git", "node_modules", "docs-site", "tests", "template", "assets", "landing-page"]);

function findSkillFiles(dir: string, depth = 0): string[] {
  if (depth > 6) return [];
  const found: string[] = [];
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (SKIP_DIRS.has(entry.name)) continue;
      found.push(...findSkillFiles(join(dir, entry.name), depth + 1));
    } else if (entry.name === "SKILL.md") {
      found.push(join(dir, entry.name));
    }
  }
  return found;
}

function scanVendorTree(vendor: GenericVendor): { skills: VendorSkill[]; duplicatesDropped: number; excludedDropped: number } {
  const base = join(ROOT, "vendor", vendor.dir);
  if (!existsSync(base)) return { skills: [], duplicatesDropped: 0, excludedDropped: 0 };

  // Some repos ship the same skill under multiple host layouts (e.g. AWS's
  // skills/ vs plugins/). Dedupe by skill name, preferring canonical paths.
  const rank = (p: string) => {
    const rel = relative(base, p).split(sep).join("/");
    return rel.startsWith("skills/") ? 0 : rel.startsWith("plugins/") ? 1 : 2;
  };

  const discovered = findSkillFiles(base);
  const files = discovered
    .filter((file) => {
      if (!vendor.excludeDirs?.length) return true;
      const segments = relative(base, file).split(sep);
      return !segments.some((segment) => vendor.excludeDirs!.includes(segment));
    })
    .sort((a, b) => rank(a) - rank(b) || a.localeCompare(b));

  const byName = new Map<string, VendorSkill>();
  let duplicatesDropped = 0;
  for (const file of files) {
    const fm = parseFrontmatter(readFileSync(file, "utf8"));
    const name = fm?.name ?? relative(base, file).split(sep).slice(-2, -1)[0] ?? file;
    if (byName.has(name)) { duplicatesDropped++; continue; }
    byName.set(name, {
      name,
      description: fm?.description ?? "",
      skillFile: relPosix(file),
    });
  }
  return {
    skills: [...byName.values()].sort((a, b) => a.name.localeCompare(b.name)),
    duplicatesDropped,
    excludedDropped: discovered.length - files.length,
  };
}

// ── Emit ─────────────────────────────────────────────────────────────

const localSkills = scanLocalSkills();
const { local: vendorPlugins, external: externalPlugins } = scanVendorPlugins();
const genericVendorResults = GENERIC_VENDORS.map((v) => ({ ...v, ...scanVendorTree(v) }));

const vendorIndex: Record<string, any> = {
  "knowledge-work-plugins": {
    label: "Anthropic Knowledge Work Plugins",
    source: "https://github.com/anthropics/knowledge-work-plugins",
    sourceClass: "official",
    install: "/plugin marketplace add anthropics/knowledge-work-plugins",
    plugins: vendorPlugins,
    externalPartnerPlugins: externalPlugins,
  },
};
for (const v of genericVendorResults) {
  vendorIndex[v.dir] = {
    label: v.label,
    source: v.source,
    sourceClass: v.sourceClass,
    ...(v.license ? { license: v.license } : {}),
    skills: v.skills,
  };
}

const index = {
  version: 1,
  generated: new Date().toISOString(),
  repo: "skillz",
  root: "https://github.com/Knapp-Kevin/skillz",
  bootstrap: "BOOTSTRAP.md",
  skills: localSkills,
  registry: "registry/candidates.yaml",
  sourceRegistry: "registry/sources.yaml",
  vendor: vendorIndex,
};

// Idempotent regeneration: keep the prior `generated` stamp when nothing
// else changed, so `git diff --exit-code index.json` can verify freshness.
const indexPath = join(ROOT, "index.json");
const stripGenerated = (s: string) => s.replace(/"generated": "[^"]*"/, '"generated": ""');
let serialized = JSON.stringify(index, null, 2) + "\n";
if (existsSync(indexPath)) {
  const prior = readFileSync(indexPath, "utf8");
  if (stripGenerated(prior) === stripGenerated(serialized)) serialized = prior;
}
writeFileSync(indexPath, serialized);

let md = `# Skill Index

> New here? Start with [BOOTSTRAP.md](BOOTSTRAP.md). It helps an agent figure out which skills are actually useful before you choose anything manually.
>
> Generated by \`scripts/build-index.ts\` — do not edit by hand.
> Regenerate with \`node scripts/build-index.ts\` after adding or changing a skill.
> Machine-readable version: [index.json](index.json)
> Source trust/provenance registry: [registry/sources.yaml](registry/sources.yaml)

## How agents should use this

1. If the user does not already know which skills they need, run the bootstrap process first.
2. Read this file (or \`index.json\`) to find a skill by name/description.
3. Read the linked \`SKILL.md\` and follow its Execution Flow section.
4. Scripts listed for a skill run with Bun or Node 22.18+, zero install, from the skill's directory.

## Local skills (\`skills/\`)

| Skill | Category | Description | Scripts |
|-------|----------|-------------|---------|
`;

for (const s of localSkills) {
  const scripts = s.scripts.map((p) => `[${p.split("/").pop()}](${p})`).join(", ") || "—";
  md += `| [${s.name}](${s.skillFile}) | ${s.category ?? "—"} | ${truncate(s.description, 160)} | ${scripts} |\n`;
}

md += `\n## Vendored reference: [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (\`vendor/\`)\n\nSource class: **official**. Anthropic's knowledge-work plugin marketplace, vendored as a git submodule.\nInstall directly instead via \`/plugin marketplace add anthropics/knowledge-work-plugins\`.\n`;

for (const p of vendorPlugins) {
  md += `\n### ${p.displayName ?? p.name}\n\n${truncate(p.description, 220)}\n\n`;
  if (p.skills.length === 0) {
    md += `_No skills directory._\n`;
    continue;
  }
  md += `| Skill | Description |\n|-------|-------------|\n`;
  for (const s of p.skills) {
    md += `| [${s.name}](${s.skillFile}) | ${truncate(s.description, 160)} |\n`;
  }
}

if (externalPlugins.length > 0) {
  md += `\n### External partner plugins (hosted outside the submodule)\n\nRegistered in the marketplace but sourced from partner repos — install via the marketplace command above, then \`/plugin install <name>@knowledge-work-plugins\`.\n\n| Plugin | Description |\n|--------|-------------|\n`;
  for (const p of externalPlugins) {
    md += `| ${p.name} | ${truncate(p.description, 160)} |\n`;
  }
}

for (const v of genericVendorResults) {
  md += `\n## Vendored reference: [${v.label}](${v.source}) (\`vendor/${v.dir}/\`)\n\n`;
  md += `Source class: **${v.sourceClass}**`;
  if (v.license) md += ` · License: **${v.license}**`;
  md += `. Inclusion makes this source available for comparison; it does not grant blanket trust to every skill.\n\n`;
  if (v.skills.length === 0) {
    md += `_No SKILL.md files found (submodule not initialized?)._\n`;
    continue;
  }
  md += `${v.skills.length} skills`;
  if (v.duplicatesDropped > 0) md += ` (${v.duplicatesDropped} duplicate per-host copies deduped)`;
  if (v.excludedDropped > 0) md += ` (${v.excludedDropped} excluded by source policy)`;
  md += `.\n\n| Skill | Description |\n|-------|-------------|\n`;
  for (const s of v.skills) {
    md += `| [${s.name}](${s.skillFile}) | ${truncate(s.description, 160)} |\n`;
  }
}

writeFileSync(join(ROOT, "INDEX.md"), md);

const vendorSkillCount = vendorPlugins.reduce((n, p) => n + p.skills.length, 0);
const genericCount = genericVendorResults.reduce((n, v) => n + v.skills.length, 0);
const officialGenericCount = genericVendorResults.filter((v) => v.sourceClass === "official").length;
const communityGenericCount = genericVendorResults.filter((v) => v.sourceClass === "community-vetted").length;
console.error(
  `[index] Wrote index.json + INDEX.md — ${localSkills.length} local skill(s), ` +
  `${vendorPlugins.length} vendored plugin(s) with ${vendorSkillCount} skill(s), ` +
  `${externalPlugins.length} external partner plugin(s), ` +
  `${genericCount} skill(s) across ${officialGenericCount} official + ${communityGenericCount} community-vetted reference repo(s).`
);

#!/usr/bin/env bun
/**
 * build-index.ts — regenerates the skill index for this repo.
 *
 * Scans first-party skills plus the vendored reference corpus declared in
 * registry/sources.yaml, then writes:
 *   - index.json  (machine-readable registry for agents/tooling)
 *   - INDEX.md    (human/agent-readable table with relative links)
 *
 * Usage (Bun or Node 22.18+):
 *   node scripts/build-index.ts
 *   bun run scripts/build-index.ts
 */

import { readdirSync, readFileSync, writeFileSync, existsSync } from "node:fs";
import { join, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";
import { parseFrontmatter, truncate } from "./lib/frontmatter.ts";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const SOURCE_REGISTRY = join(ROOT, "registry", "sources.yaml");

function relPosix(p: string): string {
  return relative(ROOT, p).split(sep).join("/");
}

function unquote(value: string): string {
  return value.trim().replace(/^["']|["']$/g, "");
}

// ── Source registry ──────────────────────────────────────────────────

interface SourceRecord {
  id: string;
  name: string;
  source: string;
  class: string;
  resolved_path: string;
  inclusion: string;
  license?: string;
  index_exclude_dirs?: string;
}

function parseSourceRegistry(): SourceRecord[] {
  if (!existsSync(SOURCE_REGISTRY)) throw new Error("registry/sources.yaml is missing");
  const lines = readFileSync(SOURCE_REGISTRY, "utf8").split(/\r?\n/);
  const records: Record<string, string>[] = [];
  let current: Record<string, string> | null = null;

  for (const line of lines) {
    const start = line.match(/^\s*-\s+id:\s*(.+?)\s*$/);
    if (start) {
      if (current) records.push(current);
      current = { id: unquote(start[1]) };
      continue;
    }
    if (!current) continue;
    const field = line.match(/^\s{4}([\w_]+):\s*(.*?)\s*$/);
    if (field) current[field[1]] = unquote(field[2]);
  }
  if (current) records.push(current);

  return records.map((r) => {
    for (const required of ["id", "name", "source", "class", "resolved_path", "inclusion"]) {
      if (!r[required]) throw new Error(`registry/sources.yaml: ${r.id ?? "unknown"} missing ${required}`);
    }
    return r as unknown as SourceRecord;
  });
}

const sourceRecords = parseSourceRegistry();
const vendoredSources = sourceRecords.filter((s) => s.inclusion === "vendored");

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

// ── Anthropic knowledge-work marketplace ─────────────────────────────

interface VendorSkill { name: string; description: string; skillFile: string; }
interface VendorPlugin { name: string; displayName?: string; description: string; path: string; skills: VendorSkill[]; }
interface ExternalPlugin { name: string; description: string; }

function scanVendorPlugins(base: string): { local: VendorPlugin[]; external: ExternalPlugin[] } {
  const marketplaceFile = join(base, ".claude-plugin", "marketplace.json");
  if (!existsSync(marketplaceFile)) return { local: [], external: [] };
  const marketplace = JSON.parse(readFileSync(marketplaceFile, "utf8"));
  const plugins: VendorPlugin[] = [];
  const external: ExternalPlugin[] = [];

  for (const p of marketplace.plugins ?? []) {
    if (typeof p.source !== "string") {
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

interface GenericVendor {
  id: string;
  dir: string;
  label: string;
  source: string;
  sourceClass: string;
  license?: string;
  excludeDirs: string[];
}

const knowledgeSource = vendoredSources.find((s) => s.resolved_path === "vendor/knowledge-work-plugins");
if (!knowledgeSource) throw new Error("registry/sources.yaml must declare vendor/knowledge-work-plugins");

const GENERIC_VENDORS: GenericVendor[] = vendoredSources
  .filter((s) => s.id !== knowledgeSource.id)
  .map((s) => ({
    id: s.id,
    dir: s.resolved_path.replace(/^vendor\//, ""),
    label: s.name,
    source: s.source,
    sourceClass: s.class,
    license: s.license,
    excludeDirs: (s.index_exclude_dirs ?? "")
      .split(",")
      .map((v) => v.trim())
      .filter(Boolean),
  }));

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

  const rank = (p: string) => {
    const rel = relative(base, p).split(sep).join("/");
    return rel.startsWith("skills/") ? 0 : rel.startsWith("plugins/") ? 1 : 2;
  };

  const discovered = findSkillFiles(base);
  const files = discovered
    .filter((file) => {
      if (vendor.excludeDirs.length === 0) return true;
      const segments = relative(base, file).split(sep);
      return !segments.some((segment) => vendor.excludeDirs.includes(segment));
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
const knowledgeBase = join(ROOT, knowledgeSource.resolved_path);
const { local: vendorPlugins, external: externalPlugins } = scanVendorPlugins(knowledgeBase);
const genericVendorResults = GENERIC_VENDORS.map((v) => ({ ...v, ...scanVendorTree(v) }));

const vendorIndex: Record<string, any> = {
  [knowledgeSource.resolved_path.replace(/^vendor\//, "")]: {
    sourceId: knowledgeSource.id,
    label: knowledgeSource.name,
    source: knowledgeSource.source,
    sourceClass: knowledgeSource.class,
    ...(knowledgeSource.license ? { license: knowledgeSource.license } : {}),
    install: "/plugin marketplace add anthropics/knowledge-work-plugins",
    plugins: vendorPlugins,
    externalPartnerPlugins: externalPlugins,
  },
};

for (const v of genericVendorResults) {
  vendorIndex[v.dir] = {
    sourceId: v.id,
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
> Generated by \`scripts/build-index.ts\`. Do not edit by hand.
> Regenerate with \`node scripts/build-index.ts\` after adding or changing a skill or source.
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

md += `\n## Vendored reference: [${knowledgeSource.name}](${knowledgeSource.source}) (\`${knowledgeSource.resolved_path}/\`)\n\nSource class: **${knowledgeSource.class}**. Anthropic's knowledge-work plugin marketplace, vendored as a git submodule.\nInstall directly instead via \`/plugin marketplace add anthropics/knowledge-work-plugins\`.\n`;

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
  md += `\n### External partner plugins (hosted outside the submodule)\n\nRegistered in the marketplace but sourced from partner repos. Install through the marketplace when appropriate.\n\n| Plugin | Description |\n|--------|-------------|\n`;
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
const officialCount = vendoredSources.filter((s) => s.class === "official").length;
const communityCount = vendoredSources.filter((s) => s.class === "community-vetted").length;
console.error(
  `[index] Wrote index.json + INDEX.md — ${localSkills.length} local skill(s), ` +
  `${vendorPlugins.length} vendored plugin(s) with ${vendorSkillCount} skill(s), ` +
  `${externalPlugins.length} external partner plugin(s), ` +
  `${genericCount} generic vendored skill(s) across ${officialCount} official + ${communityCount} community-vetted source repo(s).`
);

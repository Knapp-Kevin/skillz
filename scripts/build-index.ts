#!/usr/bin/env bun
/**
 * build-index.ts — regenerate the human and machine-readable skill catalog.
 *
 * The generated catalog separates:
 *   - locally maintained/imported library skills;
 *   - indexed skills from pinned third-party corpora;
 *   - source identity/role;
 *   - exact-version verification and characterization state.
 *
 * Usage (Bun or Node 22.18+):
 *   node scripts/build-index.ts
 *   bun run scripts/build-index.ts
 */

import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";
import { parseFrontmatter, truncate } from "./lib/frontmatter.ts";
import { discoverSkillDirs } from "./lib/skill-discovery.ts";
import { readVerificationRecord, type VerificationRecord } from "./lib/verification-registry.ts";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const SOURCE_REGISTRY = join(ROOT, "registry", "sources.yaml");
const CATEGORY_REGISTRY = join(ROOT, "registry", "categories.yaml");

function relPosix(p: string): string {
  return relative(ROOT, p).split(sep).join("/");
}

function unquote(value: string): string {
  return value.trim().replace(/^["']|["']$/g, "");
}

interface SourceRecord {
  id: string;
  name: string;
  source: string;
  class: string;
  source_role: string;
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
    for (const required of ["id", "name", "source", "class", "source_role", "resolved_path", "inclusion"]) {
      if (!r[required]) throw new Error(`registry/sources.yaml: ${r.id ?? "unknown"} missing ${required}`);
    }
    return r as unknown as SourceRecord;
  });
}

interface CategoryInfo { id: string; label: string; }

function parseCategoryRegistry(): Map<string, CategoryInfo> {
  if (!existsSync(CATEGORY_REGISTRY)) throw new Error("registry/categories.yaml is missing");
  const lines = readFileSync(CATEGORY_REGISTRY, "utf8").split(/\r?\n/);
  const bySkill = new Map<string, CategoryInfo>();
  let categoryId = "";
  let label = "";
  let inSkills = false;

  for (const line of lines) {
    const category = line.match(/^\s{2}([a-z0-9-]+):\s*$/);
    if (category) {
      categoryId = category[1];
      label = categoryId;
      inSkills = false;
      continue;
    }
    if (!categoryId) continue;

    const labelMatch = line.match(/^\s{4}label:\s*(.+?)\s*$/);
    if (labelMatch) {
      label = unquote(labelMatch[1]);
      continue;
    }
    if (/^\s{4}skills:\s*$/.test(line)) {
      inSkills = true;
      continue;
    }
    const skill = inSkills ? line.match(/^\s{6}-\s+(.+?)\s*$/) : null;
    if (skill) {
      const name = unquote(skill[1]);
      if (bySkill.has(name)) throw new Error(`registry/categories.yaml: duplicate category assignment for ${name}`);
      bySkill.set(name, { id: categoryId, label });
    }
  }

  return bySkill;
}

const sourceRecords = parseSourceRegistry();
const categoryBySkill = parseCategoryRegistry();
const vendoredSources = sourceRecords.filter((s) => s.inclusion === "vendored");

interface LocalSkill {
  name: string;
  displayName?: string;
  description: string;
  category?: CategoryInfo;
  version?: string;
  path: string;
  skillFile: string;
  scripts: string[];
}

function scanLocalSkills(): LocalSkill[] {
  const root = join(ROOT, "skills");
  const skills: LocalSkill[] = [];

  // Third-party source corpora also live under skills/, but they remain a
  // distinct governed population. Exclude the sources subtree from the local
  // scan so source skills are not double-counted as first-party/local skills.
  const localRoots = readdirSync(root, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name !== "sources")
    .map((entry) => join(root, entry.name));

  for (const localRoot of localRoots) {
    for (const discovered of discoverSkillDirs(localRoot)) {
      const fm = parseFrontmatter(readFileSync(discovered.skillFile, "utf8"));
      if (!fm?.name) {
        console.error(`[index] WARN: ${relPosix(discovered.skillFile)} has no parsable frontmatter name; skipped`);
        continue;
      }
      if (fm.name !== discovered.name) {
        console.error(`[index] WARN: frontmatter name "${fm.name}" != directory "${discovered.name}"`);
      }

      const scriptsDir = join(discovered.dir, "scripts");
      const scripts = existsSync(scriptsDir)
        ? readdirSync(scriptsDir).map((f) => relPosix(join(scriptsDir, f)))
        : [];

      const structuralPath = relative(root, discovered.dir).split(sep).join("/");
      const structuralParts = structuralPath.split("/").filter(Boolean);
      const structuralCategoryPath = structuralParts.slice(0, -1).join("/");
      const structuralCategory = structuralCategoryPath
        ? { id: structuralCategoryPath, label: structuralCategoryPath }
        : undefined;
      const category = categoryBySkill.get(fm.name) ?? structuralCategory;

      skills.push({
        name: fm.name,
        displayName: fm.metadata?.["display-name"],
        description: fm.description ?? "",
        category,
        version: fm.metadata?.version,
        path: relPosix(discovered.dir),
        skillFile: relPosix(discovered.skillFile),
        scripts,
      });
    }
  }

  const discoveredNames = new Set(skills.map((s) => s.name));
  for (const categorized of categoryBySkill.keys()) {
    if (!discoveredNames.has(categorized)) {
      console.error(`[index] WARN: registry/categories.yaml references missing local skill "${categorized}"`);
    }
  }

  return skills.sort((a, b) => a.name.localeCompare(b.name));
}

interface SkillQuality {
  characterized: boolean;
  verificationStatus: string;
  validationStatus: string;
  fingerprint?: { algorithm: string; sha: string };
  characterizedAt?: string;
  lastVerifiedAt?: string;
  verificationBasis?: string;
  tags: VerificationRecord["tags"];
  verificationRecord?: string;
}

const EMPTY_TAGS = {
  use_case: [], lifecycle: [], characteristic: [], authority: [], portability: [],
};

function qualityFor(sourceId: string, skillName: string): SkillQuality {
  const record = readVerificationRecord(ROOT, sourceId, skillName);
  if (!record) {
    return {
      characterized: false,
      verificationStatus: "unverified",
      validationStatus: "not-run",
      tags: { ...EMPTY_TAGS },
    };
  }
  return {
    characterized: true,
    verificationStatus: record.status,
    validationStatus: record.validationStatus,
    fingerprint: { algorithm: record.fingerprintAlgorithm, sha: record.contentBlobSha },
    characterizedAt: record.characterizedAt,
    lastVerifiedAt: record.lastVerifiedAt,
    verificationBasis: record.verificationBasis,
    tags: record.tags,
    verificationRecord: `registry/verification/${sourceId}/${skillName}.yaml`,
  };
}

interface VendorSkill {
  name: string;
  description: string;
  skillFile: string;
  quality: SkillQuality;
}
interface VendorPlugin {
  name: string;
  displayName?: string;
  description: string;
  path: string;
  skills: VendorSkill[];
}
interface ExternalPlugin { name: string; description: string; }

function scanVendorPlugins(sourceId: string, base: string): { local: VendorPlugin[]; external: ExternalPlugin[] } {
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
      for (const discovered of discoverSkillDirs(skillsDir)) {
        const fm = parseFrontmatter(readFileSync(discovered.skillFile, "utf8"));
        const name = fm?.name ?? discovered.name;
        skills.push({
          name,
          description: fm?.description ?? "",
          skillFile: relPosix(discovered.skillFile),
          quality: qualityFor(sourceId, name),
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

interface GenericVendor {
  id: string;
  dir: string;
  label: string;
  source: string;
  sourceClass: string;
  sourceRole: string;
  license?: string;
  excludeDirs: string[];
}

const knowledgeSource = vendoredSources.find((s) => s.id === "anthropic-knowledge-work-plugins");
if (!knowledgeSource) throw new Error("registry/sources.yaml must declare anthropic-knowledge-work-plugins");

const GENERIC_VENDORS: GenericVendor[] = vendoredSources
  .filter((s) => s.id !== knowledgeSource.id)
  .map((s) => ({
    id: s.id,
    dir: s.resolved_path,
    label: s.name,
    source: s.source,
    sourceClass: s.class,
    sourceRole: s.source_role,
    license: s.license,
    excludeDirs: (s.index_exclude_dirs ?? "")
      .split(",")
      .map((v) => v.trim())
      .filter(Boolean),
  }));

const SKIP_DIRS = new Set([".git", "node_modules", "docs-site", "tests", "template", "assets", "landing-page"]);

function findSkillFiles(dir: string, depth = 0): string[] {
  if (!existsSync(dir) || depth > 8) return [];
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
  const base = join(ROOT, vendor.dir);
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
    if (byName.has(name)) {
      duplicatesDropped++;
      continue;
    }
    byName.set(name, {
      name,
      description: fm?.description ?? "",
      skillFile: relPosix(file),
      quality: qualityFor(vendor.id, name),
    });
  }

  return {
    skills: [...byName.values()].sort((a, b) => a.name.localeCompare(b.name)),
    duplicatesDropped,
    excludedDropped: discovered.length - files.length,
  };
}

const localSkills = scanLocalSkills();
const knowledgeBase = join(ROOT, knowledgeSource.resolved_path);
const { local: vendorPlugins, external: externalPlugins } = scanVendorPlugins(knowledgeSource.id, knowledgeBase);
const genericVendorResults = GENERIC_VENDORS.map((v) => ({ ...v, ...scanVendorTree(v) }));

const knowledgeSkillCount = vendorPlugins.reduce((sum, p) => sum + p.skills.length, 0);
const genericVendorSkillCount = genericVendorResults.reduce((sum, v) => sum + v.skills.length, 0);
const vendorSkillCount = knowledgeSkillCount + genericVendorSkillCount;
const allNames = new Set<string>(localSkills.map((s) => s.name));
for (const p of vendorPlugins) for (const s of p.skills) allNames.add(s.name);
for (const v of genericVendorResults) for (const s of v.skills) allNames.add(s.name);

const counts = {
  localSkills: localSkills.length,
  vendorSkills: vendorSkillCount,
  totalIndexedSkillEntries: localSkills.length + vendorSkillCount,
  uniqueSkillNames: allNames.size,
  vendoredSources: vendoredSources.length,
  registeredSources: sourceRecords.length,
};

const vendorIndex: Record<string, any> = {
  [knowledgeSource.id]: {
    sourceId: knowledgeSource.id,
    label: knowledgeSource.name,
    source: knowledgeSource.source,
    sourceClass: knowledgeSource.class,
    sourceRole: knowledgeSource.source_role,
    resolvedPath: knowledgeSource.resolved_path,
    ...(knowledgeSource.license ? { license: knowledgeSource.license } : {}),
    install: "/plugin marketplace add anthropics/knowledge-work-plugins",
    plugins: vendorPlugins,
    externalPartnerPlugins: externalPlugins,
  },
};

for (const v of genericVendorResults) {
  vendorIndex[v.id] = {
    sourceId: v.id,
    label: v.label,
    source: v.source,
    sourceClass: v.sourceClass,
    sourceRole: v.sourceRole,
    resolvedPath: v.dir,
    ...(v.license ? { license: v.license } : {}),
    skills: v.skills,
  };
}

const index = {
  version: 2,
  generated: new Date().toISOString(),
  repo: "skillz",
  root: "https://github.com/Knapp-Kevin/skillz",
  bootstrap: "BOOTSTRAP.md",
  counts,
  skills: localSkills,
  registry: "registry/candidates.yaml",
  categoryRegistry: "registry/categories.yaml",
  sourceRegistry: "registry/sources.yaml",
  verificationRegistry: "registry/verification/",
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

function shortTags(q: SkillQuality): string {
  const tags = [...q.tags.use_case, ...q.tags.characteristic].slice(0, 5);
  return tags.length ? tags.join(", ") : "—";
}

let md = `# Skill Index\n\n`;
md += `> Generated by \`scripts/build-index.ts\`. Do not edit by hand.\n`;
md += `> First visit: start with [BOOTSTRAP.md](BOOTSTRAP.md). Returning user: use the returning-review path in the same document.\n`;
md += `> Machine-readable catalog: [index.json](index.json) · Categories: [registry/categories.yaml](registry/categories.yaml) · Verification: [registry/verification/](registry/verification/)\n\n`;
md += `## Library counts\n\n`;
md += `- **${counts.totalIndexedSkillEntries}** indexed skill entries\n`;
md += `- **${counts.uniqueSkillNames}** unique skill names across sources\n`;
md += `- **${counts.localSkills}** locally maintained/imported skills\n`;
md += `- **${counts.vendorSkills}** indexed skills from pinned source corpora\n`;
md += `- **${counts.registeredSources}** registered sources (${counts.vendoredSources} pinned source corpora)\n\n`;
md += `Cross-source skills with the same name are retained as separate implementations; duplicate copies inside one pinned source are deduplicated by name.\n\n`;
md += `## Quality states\n\n`;
md += `A skill can be available without being trusted for unchanged reuse. Exact-version states are \`unverified\`, \`trusted-baseline\`, \`verified\`, \`validated\`, \`stale\`, \`rejected\`, or \`retired\`. See [docs/skill-verification.md](docs/skill-verification.md).\n\n`;
md += `## Local library (\`skills/\`, excluding \`skills/sources/\`)\n\n`;
md += `| Skill | Human category | Description | Scripts |\n|---|---|---|---|\n`;
for (const s of localSkills) {
  const scripts = s.scripts.map((p) => `[${p.split("/").pop()}](${p})`).join(", ") || "—";
  md += `| [${s.name}](${s.skillFile}) | ${s.category?.label ?? "—"} | ${truncate(s.description, 150)} | ${scripts} |\n`;
}

md += `\n## Pinned source: [${knowledgeSource.name}](${knowledgeSource.source})\n\n`;
md += `Source class: **${knowledgeSource.class}** · Role: **${knowledgeSource.source_role}**`;
if (knowledgeSource.license) md += ` · License: **${knowledgeSource.license}**`;
md += `.\n\n`;
for (const p of vendorPlugins) {
  md += `### ${p.displayName ?? p.name}\n\n${truncate(p.description, 220)}\n\n`;
  if (!p.skills.length) {
    md += `_No indexed skills._\n\n`;
    continue;
  }
  md += `| Skill | Quality | Characterization | Description |\n|---|---|---|---|\n`;
  for (const s of p.skills) {
    md += `| [${s.name}](${s.skillFile}) | ${s.quality.verificationStatus} | ${shortTags(s.quality)} | ${truncate(s.description, 140)} |\n`;
  }
  md += `\n`;
}

if (externalPlugins.length) {
  md += `### External partner plugins\n\n`;
  md += `Registered by the marketplace but hosted outside the pinned source tree. They are discovery references, not silently trusted local inventory.\n\n`;
  md += `| Plugin | Description |\n|---|---|\n`;
  for (const p of externalPlugins) md += `| ${p.name} | ${truncate(p.description, 160)} |\n`;
  md += `\n`;
}

for (const v of genericVendorResults) {
  md += `## Pinned source: [${v.label}](${v.source})\n\n`;
  md += `Source class: **${v.sourceClass}** · Role: **${v.sourceRole}**`;
  if (v.license) md += ` · License: **${v.license}**`;
  md += `. Availability does not imply trusted unchanged-selection eligibility.\n\n`;
  if (!v.skills.length) {
    md += `_No indexed SKILL.md files found. The source submodule may not be initialized._\n\n`;
    continue;
  }
  md += `${v.skills.length} indexed skills`;
  if (v.duplicatesDropped) md += ` (${v.duplicatesDropped} duplicate copies deduplicated within this source)`;
  if (v.excludedDropped) md += ` (${v.excludedDropped} excluded by source policy)`;
  md += `.\n\n`;
  md += `| Skill | Quality | Characterization | Description |\n|---|---|---|---|\n`;
  for (const s of v.skills) {
    md += `| [${s.name}](${s.skillFile}) | ${s.quality.verificationStatus} | ${shortTags(s.quality)} | ${truncate(s.description, 140)} |\n`;
  }
  md += `\n`;
}

writeFileSync(join(ROOT, "INDEX.md"), md);
console.log(`[index] local=${counts.localSkills} vendor=${counts.vendorSkills} total=${counts.totalIndexedSkillEntries} uniqueNames=${counts.uniqueSkillNames} sources=${counts.registeredSources}`);

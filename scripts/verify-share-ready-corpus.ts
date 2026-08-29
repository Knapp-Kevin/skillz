#!/usr/bin/env node
/**
 * verify-share-ready-corpus — prove that the active first-party skill library
 * and every individually governed third-party skill have decisive, exact-version
 * quality metadata before share-ready.
 *
 * Broad vendored/tracked sources without individual companions remain
 * reference/design evidence. They are not silently promoted to trusted inventory.
 *
 * Usage:
 *   node scripts/verify-share-ready-corpus.ts
 *   node scripts/verify-share-ready-corpus.ts --json
 */

import { createHash } from "node:crypto";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

const ROOT = resolve(join(dirname(fileURLToPath(import.meta.url)), ".."));
const DEFAULT_VERIFICATION = join(ROOT, "registry", "verification");
const DEFAULT_PROVENANCE = join(ROOT, "registry", "skills");
const DEFAULT_LOCAL_MANIFEST = join(ROOT, "registry", "local-verification.json");
const DEFAULT_SKILLS_DIR = join(ROOT, "skills");
const DEFAULT_TAXONOMY = join(ROOT, "registry", "taxonomy.yaml");
const TAG_DIMENSIONS = ["use_case", "lifecycle", "characteristic", "authority", "portability"] as const;

const { values } = parseArgs({
  options: {
    "verification-dir": { type: "string", default: DEFAULT_VERIFICATION },
    "provenance-dir": { type: "string", default: DEFAULT_PROVENANCE },
    "local-manifest": { type: "string", default: DEFAULT_LOCAL_MANIFEST },
    "skills-dir": { type: "string", default: DEFAULT_SKILLS_DIR },
    taxonomy: { type: "string", default: DEFAULT_TAXONOMY },
    json: { type: "boolean", default: false },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log(
    "verify-share-ready-corpus — validate exact-version quality closure for active local skills and individually governed third-party skills\n\n" +
    "Usage: node scripts/verify-share-ready-corpus.ts [--verification-dir <path>] [--provenance-dir <path>] [--local-manifest <path>] [--skills-dir <path>] [--taxonomy <path>] [--json]"
  );
  process.exit(0);
}

const verificationDir = resolve(values["verification-dir"]!);
const provenanceDir = resolve(values["provenance-dir"]!);
const localManifestPath = resolve(values["local-manifest"]!);
const skillsDir = resolve(values["skills-dir"]!);
const taxonomyPath = resolve(values.taxonomy!);

interface Finding { file: string; message: string; }
const findings: Finding[] = [];
const thirdPartyCounts: Record<string, number> = {};
const localCounts: Record<string, number> = {};

function displayPath(path: string): string {
  const rel = relative(ROOT, path);
  return rel.startsWith("..") ? path : rel;
}

function fail(file: string, message: string): void {
  findings.push({ file: displayPath(file), message });
}

function filesNamed(dir: string, predicate: (name: string) => boolean): string[] {
  if (!existsSync(dir)) return [];
  const out: string[] = [];
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    const stat = statSync(path);
    if (stat.isDirectory()) out.push(...filesNamed(path, predicate));
    else if (predicate(name)) out.push(path);
  }
  return out.sort();
}

function yamlFiles(dir: string): string[] {
  return filesNamed(dir, (name) => name.endsWith(".yaml") || name.endsWith(".yml"));
}

function localSkillFiles(dir: string): string[] {
  return filesNamed(dir, (name) => name === "SKILL.md");
}

function scalar(text: string, key: string): string | undefined {
  const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const match = text.match(new RegExp(`^${escaped}:\\s*(.+?)\\s*$`, "m"));
  if (!match) return undefined;
  return match[1].replace(/^['"]|['"]$/g, "").trim();
}

function yamlTagValues(text: string, key: string): string[] | undefined {
  const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const match = text.match(new RegExp(`^\\s{2}${escaped}:\\s*\\[([^\\]]+)\\]\\s*$`, "m"));
  if (!match) return undefined;
  return match[1].split(",").map((value) => value.trim().replace(/^['"]|['"]$/g, "")).filter(Boolean);
}

function required(file: string, text: string, key: string): string | undefined {
  const value = scalar(text, key);
  if (!value) fail(file, `missing required field: ${key}`);
  return value;
}

function scoreValue(score: string | undefined): number | undefined {
  if (!score || !/^\d{1,2}\/20$/.test(score)) return undefined;
  return Number(score.split("/")[0]);
}

function gitBlobSha(bytes: Buffer): string {
  const header = Buffer.from(`blob ${bytes.length}\0`, "utf8");
  return createHash("sha1").update(header).update(bytes).digest("hex");
}

function parseTaxonomy(path: string): Record<string, Set<string>> {
  const result: Record<string, Set<string>> = Object.fromEntries(TAG_DIMENSIONS.map((dimension) => [dimension, new Set<string>()]));
  if (!existsSync(path)) {
    fail(path, "taxonomy file not found");
    return result;
  }
  const lines = readFileSync(path, "utf8").split(/\r?\n/);
  let current: string | null = null;
  for (const line of lines) {
    const dimension = line.match(/^  ([a-z_]+):\s*$/)?.[1];
    if (dimension && TAG_DIMENSIONS.includes(dimension as any)) {
      current = dimension;
      continue;
    }
    const value = line.match(/^    -\s+(.+?)\s*$/)?.[1];
    if (value && current) result[current].add(value);
    else if (/^\S/.test(line) && !line.startsWith("#")) current = null;
  }
  return result;
}

const taxonomy = parseTaxonomy(taxonomyPath);

function validateTags(file: string, tags: Record<string, unknown>): void {
  for (const dimension of TAG_DIMENSIONS) {
    const values = tags?.[dimension];
    if (!Array.isArray(values) || values.length === 0 || values.some((value) => typeof value !== "string" || !value)) {
      fail(file, `missing/non-list controlled tag dimension: ${dimension}`);
      continue;
    }
    for (const value of values as string[]) {
      if (!taxonomy[dimension]?.has(value)) fail(file, `unknown ${dimension} tag: ${value}`);
    }
  }
}

// ---- First-party active local library ------------------------------------

let localManifest: any = null;
if (!existsSync(localManifestPath)) {
  fail(localManifestPath, "local first-party verification manifest not found");
} else {
  try {
    localManifest = JSON.parse(readFileSync(localManifestPath, "utf8"));
  } catch (error) {
    fail(localManifestPath, `local verification manifest is not valid JSON: ${String(error)}`);
  }
}

const discoveredLocal = localSkillFiles(skillsDir);
const discoveredPaths = new Set(discoveredLocal.map((file) => relative(ROOT, file).replaceAll("\\", "/")));
const recordedPaths = new Set<string>();
const recordedNames = new Set<string>();

if (localManifest) {
  if (localManifest.schema_version !== 1) fail(localManifestPath, `schema_version must be 1, found ${localManifest.schema_version ?? "missing"}`);
  if (localManifest.source_id !== "local-skills") fail(localManifestPath, `source_id must be local-skills, found ${localManifest.source_id ?? "missing"}`);
  if (localManifest.source_class !== "first-party") fail(localManifestPath, `source_class must be first-party, found ${localManifest.source_class ?? "missing"}`);
  if (!localManifest.reviewed_at) fail(localManifestPath, "reviewed_at missing");
  if (!localManifest.rubric) fail(localManifestPath, "rubric missing");

  const entries = Array.isArray(localManifest.skills) ? localManifest.skills : [];
  if (!Array.isArray(localManifest.skills)) fail(localManifestPath, "skills must be an array");

  for (const entry of entries) {
    const label = entry?.local_path ? `${localManifestPath}#${entry.local_path}` : localManifestPath;
    const name = entry?.skill_name;
    const localPath = entry?.local_path;
    if (typeof name !== "string" || !name) fail(label, "skill_name missing");
    if (typeof localPath !== "string" || !localPath) {
      fail(label, "local_path missing");
      continue;
    }
    if (recordedPaths.has(localPath)) fail(label, `duplicate local_path: ${localPath}`);
    recordedPaths.add(localPath);
    if (name) {
      if (recordedNames.has(name)) fail(label, `duplicate skill_name: ${name}`);
      recordedNames.add(name);
      if (basename(dirname(localPath)) !== name) fail(label, `skill_name/path mismatch: ${name} vs ${localPath}`);
    }

    const file = resolve(ROOT, localPath);
    if (!existsSync(file)) {
      fail(label, `recorded local skill file does not exist: ${localPath}`);
      continue;
    }

    if (entry.fingerprint_algorithm !== "git-blob-sha1") fail(label, `unsupported fingerprint_algorithm: ${entry.fingerprint_algorithm ?? "missing"}`);
    if (!/^[0-9a-f]{40}$/i.test(entry.content_blob_sha ?? "")) fail(label, "content_blob_sha must be a 40-character Git blob SHA-1");
    else {
      const actual = gitBlobSha(readFileSync(file));
      if (actual !== entry.content_blob_sha) fail(label, `fingerprint mismatch: recorded=${entry.content_blob_sha} actual=${actual}`);
    }

    const status = entry.verification_status;
    if (!["verified", "validated"].includes(status)) fail(label, `active local skill must be verified or validated, found: ${status ?? "missing"}`);
    else localCounts[status] = (localCounts[status] ?? 0) + 1;

    const score = entry.rubric_score;
    const numeric = scoreValue(score);
    if (numeric === undefined) fail(label, `rubric_score must use N/20 form, found: ${score ?? "missing"}`);
    else if (numeric < 15) fail(label, `active verified local skill score below 15/20: ${score}`);

    if (!entry.validation_status) fail(label, "validation_status missing");
    if (status === "validated" && entry.validation_status === "not-run") fail(label, "validated status requires behavioral validation evidence/status");
    if (!entry.notes || typeof entry.notes !== "string") fail(label, "review notes missing");
    validateTags(label, entry.tags ?? {});
  }
}

for (const localPath of discoveredPaths) {
  if (!recordedPaths.has(localPath)) fail(localManifestPath, `active local skill lacks exact-version review: ${localPath}`);
}
for (const localPath of recordedPaths) {
  if (!discoveredPaths.has(localPath)) fail(localManifestPath, `manifest records non-active/missing local skill: ${localPath}`);
}
if (localManifest && recordedPaths.size !== discoveredPaths.size) {
  fail(localManifestPath, `local coverage mismatch: discovered=${discoveredPaths.size} recorded=${recordedPaths.size}`);
}

// ---- Individually governed third-party skills ---------------------------

const records = yamlFiles(verificationDir);
if (!records.length) fail(verificationDir, "no third-party verification YAML records found");

for (const file of records) {
  const text = readFileSync(file, "utf8");
  const skillName = required(file, text, "skill_name");
  const sourceId = required(file, text, "source_id");
  required(file, text, "source_snapshot_revision");
  const fingerprintAlgorithm = required(file, text, "fingerprint_algorithm");
  const blobSha = required(file, text, "content_blob_sha");
  const status = required(file, text, "verification_status");
  const validation = required(file, text, "validation_status");

  if (fingerprintAlgorithm && fingerprintAlgorithm !== "git-blob-sha1") fail(file, `unsupported fingerprint_algorithm: ${fingerprintAlgorithm}`);
  if (blobSha && !/^[0-9a-f]{40}$/i.test(blobSha)) fail(file, "content_blob_sha must be a 40-character Git blob SHA-1");

  if (status) {
    thirdPartyCounts[status] = (thirdPartyCounts[status] ?? 0) + 1;
    const decisive = new Set(["verified", "validated", "rejected", "retired"]);
    if (!decisive.has(status)) fail(file, `non-decisive share-ready verification_status: ${status}`);

    if (["verified", "validated", "rejected"].includes(status)) {
      const score = required(file, text, "rubric_score");
      const numeric = scoreValue(score);
      if (numeric === undefined) fail(file, `rubric_score must use N/20 form, found: ${score ?? "missing"}`);
      else if (["verified", "validated"].includes(status) && numeric < 15) fail(file, `verified/validated score below 15/20: ${score}`);
    }

    if (status === "validated" && (!validation || validation === "not-run")) fail(file, "validated status requires behavioral validation evidence/status");
  }

  const tagMap: Record<string, string[]> = {};
  for (const dimension of TAG_DIMENSIONS) {
    const tagValues = yamlTagValues(text, dimension);
    if (!tagValues?.length) fail(file, `missing/non-list controlled tag dimension: ${dimension}`);
    else tagMap[dimension] = tagValues;
  }
  validateTags(file, tagMap);

  if (skillName && sourceId) {
    const provenance = join(provenanceDir, sourceId, `${skillName}.yaml`);
    if (!existsSync(provenance)) {
      fail(file, `matching provenance companion not found: ${displayPath(provenance)}`);
      continue;
    }

    const p = readFileSync(provenance, "utf8");
    for (const key of [
      "skill_name", "source_id", "source_repository", "source_path", "source_class", "license",
      "relationship", "source_snapshot_revision", "permission_tier", "portability", "review_status",
      "dependency_status", "dependencies", "import_eligibility", "rationale",
    ]) required(provenance, p, key);

    const pSkill = scalar(p, "skill_name");
    const pSource = scalar(p, "source_id");
    if (pSkill && pSkill !== skillName) fail(provenance, `skill_name mismatch: expected ${skillName}, found ${pSkill}`);
    if (pSource && pSource !== sourceId) fail(provenance, `source_id mismatch: expected ${sourceId}, found ${pSource}`);
  }
}

const result = {
  status: findings.length ? "FAIL" : "PASS",
  local: {
    discovered_active_skills: discoveredPaths.size,
    reviewed_active_skills: recordedPaths.size,
    quality_counts: Object.fromEntries(Object.entries(localCounts).sort(([a], [b]) => a.localeCompare(b))),
  },
  third_party: {
    governed_records: records.length,
    quality_counts: Object.fromEntries(Object.entries(thirdPartyCounts).sort(([a], [b]) => a.localeCompare(b))),
  },
  blockers: findings,
  boundary: "Broad vendored/tracked sources without individual companions remain reference/design evidence and are not unchanged-selection eligible.",
};

if (values.json) {
  console.log(JSON.stringify(result, null, 2));
} else {
  for (const finding of findings) console.log(`FAIL: ${finding.file}: ${finding.message}`);
  console.log(`\nshare-ready corpus: ${result.status}`);
  console.log(`local active: discovered=${result.local.discovered_active_skills} reviewed=${result.local.reviewed_active_skills} states=${Object.entries(result.local.quality_counts).map(([k, v]) => `${k}=${v}`).join(", ") || "none"}`);
  console.log(`third-party governed: ${result.third_party.governed_records} states=${Object.entries(result.third_party.quality_counts).map(([k, v]) => `${k}=${v}`).join(", ") || "none"}`);
  console.log(result.boundary);
}

process.exit(findings.length ? 1 : 0);

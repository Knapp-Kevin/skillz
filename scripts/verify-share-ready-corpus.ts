#!/usr/bin/env node
/**
 * verify-share-ready-corpus — prove that every individually governed
 * third-party skill has decisive exact-version metadata before share-ready.
 *
 * This does NOT claim that every file in broad vendored/tracked reference
 * corpora has been individually reviewed. Files without companions remain
 * reference/design evidence and receive no unchanged-selection eligibility.
 *
 * Usage:
 *   node scripts/verify-share-ready-corpus.ts
 *   node scripts/verify-share-ready-corpus.ts --json
 */

import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

const ROOT = resolve(join(dirname(fileURLToPath(import.meta.url)), ".."));
const DEFAULT_VERIFICATION = join(ROOT, "registry", "verification");
const DEFAULT_PROVENANCE = join(ROOT, "registry", "skills");

const { values } = parseArgs({
  options: {
    "verification-dir": { type: "string", default: DEFAULT_VERIFICATION },
    "provenance-dir": { type: "string", default: DEFAULT_PROVENANCE },
    json: { type: "boolean", default: false },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log(
    "verify-share-ready-corpus — validate decisive exact-version metadata for individually governed third-party skills\n\n" +
    "Usage: node scripts/verify-share-ready-corpus.ts [--verification-dir <path>] [--provenance-dir <path>] [--json]"
  );
  process.exit(0);
}

const verificationDir = resolve(values["verification-dir"]!);
const provenanceDir = resolve(values["provenance-dir"]!);

interface Finding {
  file: string;
  message: string;
}

const findings: Finding[] = [];
const counts: Record<string, number> = {};

function fail(file: string, message: string): void {
  findings.push({ file: relative(ROOT, file), message });
}

function yamlFiles(dir: string): string[] {
  if (!existsSync(dir)) return [];
  const out: string[] = [];
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    const stat = statSync(path);
    if (stat.isDirectory()) out.push(...yamlFiles(path));
    else if (name.endsWith(".yaml") || name.endsWith(".yml")) out.push(path);
  }
  return out.sort();
}

function scalar(text: string, key: string): string | undefined {
  const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const match = text.match(new RegExp(`^${escaped}:\\s*(.+?)\\s*$`, "m"));
  if (!match) return undefined;
  return match[1].replace(/^['"]|['"]$/g, "").trim();
}

function hasTag(text: string, key: string): boolean {
  const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  return new RegExp(`^\\s{2}${escaped}:\\s*\\[[^\\]]+\\]\\s*$`, "m").test(text);
}

function required(file: string, text: string, key: string): string | undefined {
  const value = scalar(text, key);
  if (!value) fail(file, `missing required field: ${key}`);
  return value;
}

const records = yamlFiles(verificationDir);
if (!records.length) {
  fail(verificationDir, "no verification YAML records found");
}

for (const file of records) {
  const text = readFileSync(file, "utf8");
  const skillName = required(file, text, "skill_name");
  const sourceId = required(file, text, "source_id");
  required(file, text, "source_snapshot_revision");
  const fingerprintAlgorithm = required(file, text, "fingerprint_algorithm");
  const blobSha = required(file, text, "content_blob_sha");
  const status = required(file, text, "verification_status");
  const validation = required(file, text, "validation_status");

  if (fingerprintAlgorithm && fingerprintAlgorithm !== "git-blob-sha1") {
    fail(file, `unsupported fingerprint_algorithm: ${fingerprintAlgorithm}`);
  }
  if (blobSha && !/^[0-9a-f]{40}$/i.test(blobSha)) {
    fail(file, "content_blob_sha must be a 40-character Git blob SHA-1");
  }

  if (status) {
    counts[status] = (counts[status] ?? 0) + 1;
    const decisive = new Set(["verified", "validated", "rejected", "retired"]);
    if (!decisive.has(status)) {
      fail(file, `non-decisive share-ready verification_status: ${status}`);
    }

    if (["verified", "validated", "rejected"].includes(status)) {
      const score = required(file, text, "rubric_score");
      if (score && !/^\d{1,2}\/20$/.test(score)) {
        fail(file, `rubric_score must use N/20 form, found: ${score}`);
      }
    }

    if (status === "validated" && (!validation || validation === "not-run")) {
      fail(file, "validated status requires behavioral validation evidence/status");
    }
  }

  for (const tag of ["use_case", "lifecycle", "characteristic", "authority", "portability"]) {
    if (!hasTag(text, tag)) fail(file, `missing/non-list controlled tag dimension: ${tag}`);
  }

  if (skillName && sourceId) {
    const provenance = join(provenanceDir, sourceId, `${skillName}.yaml`);
    if (!existsSync(provenance)) {
      fail(file, `matching provenance companion not found: ${relative(ROOT, provenance)}`);
      continue;
    }

    const p = readFileSync(provenance, "utf8");
    for (const key of [
      "skill_name",
      "source_id",
      "source_repository",
      "source_path",
      "source_class",
      "license",
      "relationship",
      "source_snapshot_revision",
      "permission_tier",
      "portability",
      "review_status",
      "dependency_status",
      "dependencies",
      "import_eligibility",
      "rationale",
    ]) {
      required(provenance, p, key);
    }

    const pSkill = scalar(p, "skill_name");
    const pSource = scalar(p, "source_id");
    if (pSkill && pSkill !== skillName) fail(provenance, `skill_name mismatch: expected ${skillName}, found ${pSkill}`);
    if (pSource && pSource !== sourceId) fail(provenance, `source_id mismatch: expected ${sourceId}, found ${pSource}`);
  }
}

const result = {
  status: findings.length ? "FAIL" : "PASS",
  governed_records: records.length,
  quality_counts: Object.fromEntries(Object.entries(counts).sort(([a], [b]) => a.localeCompare(b))),
  blockers: findings,
  boundary: "Broad vendored/tracked sources without individual companions remain reference/design evidence and are not unchanged-selection eligible.",
};

if (values.json) {
  console.log(JSON.stringify(result, null, 2));
} else {
  for (const finding of findings) console.log(`FAIL: ${finding.file}: ${finding.message}`);
  console.log(`\nshare-ready corpus: ${result.status} — ${records.length} governed record(s)`);
  console.log(`quality states: ${Object.entries(result.quality_counts).map(([k, v]) => `${k}=${v}`).join(", ") || "none"}`);
  console.log(result.boundary);
}

process.exit(findings.length ? 1 : 0);

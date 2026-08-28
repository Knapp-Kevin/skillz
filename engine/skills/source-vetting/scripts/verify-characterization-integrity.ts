#!/usr/bin/env node
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "..");
const VERIFY_ROOT = join(ROOT, "registry", "verification");

function yamlFiles(dir) {
  if (!existsSync(dir)) return [];
  const out = [];
  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    if (statSync(path).isDirectory()) out.push(...yamlFiles(path));
    else if (entry.endsWith(".yaml")) out.push(path);
  }
  return out;
}

function field(text, name) {
  const match = text.match(new RegExp(`^${name}:\\s*(.+)$`, "m"));
  if (!match) return undefined;
  return match[1].trim().replace(/^['\"]|['\"]$/g, "");
}

let stale = 0;
let malformed = 0;
let unavailable = 0;
let ok = 0;

for (const recordPath of yamlFiles(VERIFY_ROOT)) {
  const text = readFileSync(recordPath, "utf8");
  const localPath = field(text, "local_path");
  const expected = field(text, "content_blob_sha");
  const skillName = field(text, "skill_name") ?? relative(VERIFY_ROOT, recordPath);

  if (!localPath || !expected || !/^[0-9a-f]{40}$/.test(expected)) {
    console.error(`MALFORMED ${skillName}: missing local_path or valid content_blob_sha`);
    malformed++;
    continue;
  }

  const absolute = join(ROOT, localPath);
  if (!existsSync(absolute)) {
    console.log(`UNAVAILABLE ${skillName}: ${localPath} is not materialized (submodule may be uninitialized)`);
    unavailable++;
    continue;
  }

  const result = spawnSync("git", ["hash-object", absolute], {
    cwd: ROOT,
    encoding: "utf8",
  });

  if (result.status !== 0) {
    console.error(`MALFORMED ${skillName}: git hash-object failed: ${result.stderr?.trim() ?? "unknown error"}`);
    malformed++;
    continue;
  }

  const actual = result.stdout.trim();
  if (actual !== expected) {
    console.error(`STALE / REVERIFY REQUIRED ${skillName}: expected ${expected}, got ${actual}`);
    stale++;
    continue;
  }

  console.log(`OK ${skillName}: ${actual}`);
  ok++;
}

console.log(`\ncharacterization-integrity: ok=${ok} unavailable=${unavailable} stale=${stale} malformed=${malformed}`);
process.exitCode = stale > 0 || malformed > 0 ? 1 : 0;

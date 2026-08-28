#!/usr/bin/env node
/**
 * Verify that the superproject is clean and every source declared
 * `inclusion: vendored` is materialized at exactly the gitlink revision
 * recorded by the superproject.
 *
 * This is intentionally stricter than checking whether vendor/<name> exists.
 * An uninitialized submodule directory can still sit inside the parent Git
 * worktree, and dirty source content can change catalog output without
 * changing its recorded gitlink.
 *
 * Usage:
 *   node scripts/verify-vendor-materialization.ts
 *   node scripts/verify-vendor-materialization.ts --repo-root <path>
 */

import { existsSync, readFileSync, realpathSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";
import { spawnSync } from "node:child_process";

const DEFAULT_ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");

const { values } = parseArgs({
  options: {
    "repo-root": { type: "string", default: DEFAULT_ROOT },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log("verify-vendor-materialization — require a clean superproject and every vendored source to be initialized, clean, and checked out at the superproject gitlink revision\n\nUsage: node scripts/verify-vendor-materialization.ts [--repo-root <path>]");
  process.exit(0);
}

const ROOT = resolve(values["repo-root"]!);
const SOURCE_REGISTRY = join(ROOT, "registry", "sources.yaml");

interface SourceRecord {
  id: string;
  inclusion?: string;
  resolved_path?: string;
}

function unquote(value: string): string {
  return value.trim().replace(/^["']|["']$/g, "");
}

function parseVendoredSources(): SourceRecord[] {
  if (!existsSync(SOURCE_REGISTRY)) {
    throw new Error(`source registry missing: ${SOURCE_REGISTRY}`);
  }

  const records: SourceRecord[] = [];
  let current: SourceRecord | null = null;

  for (const line of readFileSync(SOURCE_REGISTRY, "utf8").split(/\r?\n/)) {
    const start = line.match(/^\s*-\s+id:\s*(.+?)\s*$/);
    if (start) {
      if (current) records.push(current);
      current = { id: unquote(start[1]) };
      continue;
    }
    if (!current) continue;
    const field = line.match(/^\s{4}([\w_]+):\s*(.*?)\s*$/);
    if (!field) continue;
    if (field[1] === "inclusion") current.inclusion = unquote(field[2]);
    if (field[1] === "resolved_path") current.resolved_path = unquote(field[2]);
  }
  if (current) records.push(current);

  const vendored = records.filter((record) => record.inclusion === "vendored");
  if (vendored.length === 0) throw new Error("registry/sources.yaml declares no vendored sources");
  return vendored;
}

function git(args: string[], cwd = ROOT): { status: number | null; stdout: string; stderr: string } {
  const result = spawnSync("git", args, {
    cwd,
    encoding: "utf8",
    timeout: 30_000,
  });
  return {
    status: result.status,
    stdout: result.stdout?.trim() ?? "",
    stderr: result.stderr?.trim() ?? "",
  };
}

function canonicalPath(path: string): string {
  return resolve(realpathSync(path));
}

const failures: string[] = [];
const passes: Array<{ id: string; path: string; sha: string }> = [];

const rootTop = git(["rev-parse", "--show-toplevel"]);
if (rootTop.status !== 0 || !rootTop.stdout) {
  console.error(`FAIL: repository root is not a Git worktree: ${ROOT}${rootTop.stderr ? ` (${rootTop.stderr})` : ""}`);
  process.exit(1);
}

if (canonicalPath(rootTop.stdout) !== canonicalPath(ROOT)) {
  console.error(`FAIL: --repo-root must be the superproject root (resolved ${rootTop.stdout})`);
  process.exit(1);
}

// The proof is tied to superproject HEAD. Ignore submodule state here because
// each vendored source is checked more precisely below. Any other tracked or
// untracked superproject change would make the named commit an incomplete
// description of the state being evaluated.
const rootStatus = git(["status", "--porcelain", "--untracked-files=all", "--ignore-submodules=all"]);
if (rootStatus.status !== 0) {
  console.error(`FAIL: cannot inspect superproject working tree${rootStatus.stderr ? ` (${rootStatus.stderr})` : ""}`);
  process.exit(1);
}
if (rootStatus.stdout) {
  console.error("FAIL: superproject is dirty; alpha proof must begin from the exact committed state before generated catalog files are refreshed");
  console.error(rootStatus.stdout);
  process.exit(1);
}

for (const source of parseVendoredSources()) {
  const rel = source.resolved_path;
  if (!rel) {
    failures.push(`${source.id}: vendored source is missing resolved_path`);
    continue;
  }

  const absolute = join(ROOT, rel);
  const tree = git(["ls-tree", "HEAD", "--", rel]);
  const match = tree.stdout.match(/^160000\s+commit\s+([0-9a-f]{40})\t(.+)$/);
  if (tree.status !== 0 || !match || match[2] !== rel) {
    failures.push(`${source.id}: ${rel} is not a 160000 gitlink in superproject HEAD`);
    continue;
  }
  const expected = match[1];

  if (!existsSync(absolute) || !statSync(absolute).isDirectory()) {
    failures.push(`${source.id}: ${rel} is not materialized`);
    continue;
  }

  const subTop = git(["rev-parse", "--show-toplevel"], absolute);
  if (subTop.status !== 0 || !subTop.stdout) {
    failures.push(`${source.id}: ${rel} is not an initialized Git worktree`);
    continue;
  }

  // Without this check, `git -C vendor/empty rev-parse HEAD` can walk upward
  // into the superproject and falsely make an uninitialized submodule look valid.
  if (canonicalPath(subTop.stdout) !== canonicalPath(absolute)) {
    failures.push(`${source.id}: ${rel} is not initialized as its own Git worktree`);
    continue;
  }

  const head = git(["rev-parse", "HEAD"], absolute);
  if (head.status !== 0 || !/^[0-9a-f]{40}$/.test(head.stdout)) {
    failures.push(`${source.id}: cannot resolve submodule HEAD at ${rel}`);
    continue;
  }
  if (head.stdout !== expected) {
    failures.push(`${source.id}: ${rel} HEAD ${head.stdout} does not match pinned gitlink ${expected}`);
    continue;
  }

  const status = git(["status", "--porcelain", "--untracked-files=all"], absolute);
  if (status.status !== 0) {
    failures.push(`${source.id}: cannot inspect submodule working tree at ${rel}`);
    continue;
  }
  if (status.stdout) {
    failures.push(`${source.id}: ${rel} is dirty; catalog proof requires the exact pinned source tree`);
    continue;
  }

  passes.push({ id: source.id, path: rel, sha: expected });
  console.log(`OK ${source.id}: ${rel} @ ${expected}`);
}

console.log(`\nvendor-materialization: ok=${passes.length} fail=${failures.length}`);
for (const failure of failures) console.error(`FAIL: ${failure}`);

if (failures.length > 0) process.exit(1);
console.log(`PASS: clean superproject; all ${passes.length} vendored sources are initialized, clean, and pinned exactly.`);

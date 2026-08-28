// Behavior tests for engine skill-audit and skill-sync scripts.

import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync, existsSync, readFileSync, writeFileSync, readdirSync, realpathSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const AUDIT = join(ROOT, "engine", "skills", "skill-audit", "scripts", "audit.ts");
const SYNC = join(ROOT, "engine", "skills", "skill-sync", "scripts", "sync.ts");
const RISK = join(ROOT, "engine", "skills", "skill-audit", "scripts", "risk-audit.ts");

function run(script, args) {
  const res = spawnSync(process.execPath, [script, ...args], {
    cwd: ROOT, encoding: "utf8", timeout: 120_000,
  });
  return { code: res.status, out: `${res.stdout}\n${res.stderr}` };
}

function tmp(label) {
  return mkdtempSync(join(tmpdir(), `skillz-${label}-`));
}

test("audit-fails-on-bad-skill", () => {
  const { code, out } = run(AUDIT, ["--skills-dir", join(ROOT, "tests", "fixtures")]);
  assert.equal(code, 1, `expected exit 1, got ${code}\n${out}`);
  assert.match(out, /bad-skill/, "finding must name the offending skill dir");
  assert.match(out, /wrong-name/, "finding must name the mismatched frontmatter name");
});

test("audit-passes-on-library", () => {
  const { code, out } = run(AUDIT, []);
  assert.equal(code, 0, `library self-audit must pass\n${out}`);
});

test("audit-reports-library-skill-count only", () => {
  const { code, out } = run(AUDIT, []);
  assert.equal(code, 0, out);
  const m = out.match(/skill-audit: (\d+) library skill\(s\)/);
  assert.ok(m, `summary must report library-skill count\n${out}`);
  assert.equal(parseInt(m[1], 10), 42, `expected 42 library skills after moving 7 engine skills, got ${m[1]}`);
});

test("audit-fails-on-bad-sources", () => {
  const { code, out } = run(AUDIT, ["--skills-dir", join(ROOT, "tests", "fixtures")]);
  assert.equal(code, 1, `expected exit 1, got ${code}\n${out}`);
  assert.match(out, /bad-skill[^\n]*sources\.json/, "finding must tie the malformed sources.json to its skill");
});

test("risk-audit-fails-on-mutating-without-approval", () => {
  const { code, out } = run(RISK, ["--skills-dir", join(ROOT, "tests", "fixtures-risk", "failing")]);
  assert.equal(code, 1, `expected exit 1, got ${code}\n${out}`);
  assert.match(out, /mutating-no-approval[^\n]*mutating action "(send|publish|delete)"/i, "finding must name the skill and the verb");
  assert.match(out, /no approval\/read-only language/, "finding must name the missing-approval ground");
});

test("risk-audit-fails-on-missing-negative-rules", () => {
  const { code, out } = run(RISK, ["--skills-dir", join(ROOT, "tests", "fixtures-risk", "failing")]);
  assert.equal(code, 1, out);
  assert.match(out, /judgment-no-negative-rules[^\n]*no "## Negative rules" section/, "finding must tie the missing section to the slot-bearing skill");
});

test("risk-audit-warns-on-portable-specificity", () => {
  const { code, out } = run(RISK, ["--skills-dir", join(ROOT, "tests", "fixtures-risk", "warn-only")]);
  assert.equal(code, 0, `warnings alone must not fail the audit\n${out}`);
  assert.match(out, /WARN: portable-specific[^\n]*absolute path/, "warn must name the absolute path");
  assert.match(out, /WARN: portable-specific[^\n]*operator\/org term "GG-CORE"/, "warn must name the org term");
});

test("risk-audit-passes-on-library", () => {
  const { code, out } = run(RISK, []);
  assert.equal(code, 0, `library skills must be risk-clean\n${out}`);
  assert.match(out, /risk-audit: 42 library skill\(s\)/);
});

test("sync-hosts-writes-library skills and never engine skills", () => {
  const root = tmp("hosts");
  try {
    const { code, out } = run(SYNC, ["--apply", "--hosts", root]);
    assert.equal(code, 0, out);
    for (const h of [".claude", ".kilo", ".codex"]) {
      assert.ok(existsSync(join(root, h, "skills", "claude-pulse", "SKILL.md")), `${h}/skills library copy missing`);
      assert.ok(!existsSync(join(root, h, "skills", "skill-audit")), `engine skill leaked into ${h}`);
      assert.ok(!existsSync(join(root, h, "skills", "skill-bootstrap")), `engine skill leaked into ${h}`);
      assert.ok(!existsSync(join(root, h, "skills", "skills-pulse")), `engine skill leaked into ${h}`);
    }
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("audit-rejects-bad-registry-status", () => {
  const { code, out } = run(AUDIT, ["--registry", join(ROOT, "tests", "fixtures", "bad-registry.yaml")]);
  assert.equal(code, 1, `expected exit 1, got ${code}\n${out}`);
  assert.match(out, /yolo/, "finding must name the invalid status value");
});

test("sync-dry-run-mutates-nothing and only discovers library", () => {
  const dest = tmp("dry");
  try {
    const { code, out } = run(SYNC, ["--dest", dest]);
    assert.equal(code, 0, out);
    assert.equal(readdirSync(dest).length, 0, "dry-run must not write to dest");
    assert.match(out, /claude-pulse: create/, "dry-run must plan a create per portable library skill");
    assert.doesNotMatch(out, /skills-pulse:/, "engine skills must not appear in library sync planning");
    assert.doesNotMatch(out, /skill-audit:/, "engine skills must not appear in library sync planning");
    assert.doesNotMatch(out, /skill-sync:/, "engine skills must not appear in library sync planning");
  } finally {
    rmSync(dest, { recursive: true, force: true });
  }
});

test("sync-apply-copies-and-reports-drift", () => {
  const dest = tmp("apply");
  try {
    const first = run(SYNC, ["--apply", "--dest", dest]);
    assert.equal(first.code, 0, first.out);
    const copied = join(dest, "claude-pulse", "SKILL.md");
    assert.ok(existsSync(copied), "apply must copy SKILL.md");
    writeFileSync(copied, readFileSync(copied, "utf8") + "\n<!-- drift -->\n");
    const second = run(SYNC, ["--dest", dest]);
    assert.equal(second.code, 0, second.out);
    assert.match(second.out, /claude-pulse: update/, "mutated copy must report update");
  } finally {
    rmSync(dest, { recursive: true, force: true });
  }
});

test("sync-junction-under-temp-root", () => {
  const root = tmp("junction");
  try {
    const { code, out } = run(SYNC, ["--apply", "--claude-user", "--claude-user-root", root]);
    assert.equal(code, 0, out);
    const link = join(root, "claude-pulse");
    assert.ok(existsSync(link), "junction must exist under temp root");
    assert.equal(
      realpathSync(link),
      realpathSync(join(ROOT, "skills", "claude-pulse")),
      "junction must resolve to the library skill directory",
    );
    assert.ok(!existsSync(join(root, "skill-audit")), "engine skill must not be deployed");
    assert.ok(!existsSync(join(root, "skills-pulse")), "engine skill must not be deployed");
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("sync-coreforge-manifest-shape", () => {
  const dest = tmp("coreforge");
  try {
    const { code, out } = run(SYNC, ["--apply", "--coreforge", dest]);
    assert.equal(code, 0, out);
    const manifest = JSON.parse(readFileSync(join(dest, "claude-pulse", "manifest.json"), "utf8"));
    assert.deepEqual(
      Object.keys(manifest).sort(),
      ["category", "description", "entryPoint", "name", "permissions", "runtime", "skillId", "version"],
      "manifest must contain exactly the declared field set",
    );
    assert.equal(manifest.skillId, "claude-pulse");
    assert.equal(manifest.entryPoint, "SKILL.md");
    const fm = readFileSync(join(ROOT, "skills", "claude-pulse", "SKILL.md"), "utf8");
    const version = fm.match(/^\s+version:\s*(\S+)/m)?.[1];
    assert.equal(manifest.version, version, "manifest version must match frontmatter");
  } finally {
    rmSync(dest, { recursive: true, force: true });
  }
});

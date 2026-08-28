#!/usr/bin/env bun
/**
 * risk-audit — semantic risk filter for library skills (issue #5).
 *
 * Complements audit.ts's structural checks with deterministic risk-pattern
 * detection across recursively discovered library skills.
 *
 * Usage (Bun or Node 22.18+):
 *   node engine/skills/skill-audit/scripts/risk-audit.ts [--skills-dir <path>]
 *
 * Exit 0 = clean or warnings only. Exit 1 = one or more FAIL findings.
 */

import { parseArgs } from "node:util";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { discoverSkillDirs } from "../../../../scripts/lib/skill-discovery.ts";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "..");

const { values } = parseArgs({
  options: {
    "skills-dir": { type: "string", default: join(ROOT, "skills") },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log("risk-audit — semantic risk filter\n\nUsage: node risk-audit.ts [--skills-dir <path>] [--help]");
  process.exit(0);
}

interface Finding { level: "FAIL" | "WARN"; msg: string; }
const findings: Finding[] = [];
const fail = (msg: string) => findings.push({ level: "FAIL", msg });
const warn = (msg: string) => findings.push({ level: "WARN", msg });

const SLOT_RE = /\bbecause\b|\[reason\]|\[rationale\]|\broot cause\b|\bverdict\b/i;
const SECRET_RULE_RE = /secret|token|credential|\bkey\b/i;
const FABRICATION_RULE_RE = /not established|never invent|fabricat/i;
const GAP_RE = /not established|none recorded|\bunknown\b|undetermined|no data|unverifiable|\bempty\b/i;
const FAIL_VERB_RE = /\b(send|push|delete|publish|deploy|create issue|archive|enroll|pay|buy)\b/i;
const WARN_VERB_RE = /\b(move|update)\b/i;
const APPROVAL_RE = /approv|confirm|draft-only|read-only|dry-run|propos|never (sends|posts|publishes|edits|applies|mutates|contacts|modifies)|operator to (apply|publish)|hands? (it|copy|the report)? ?to the operator/i;
const ABS_PATH_RE = /\b[A-Z]:\\|(^|[\s`("'])\/(home|Users)\//m;
const RISK_TERMS = [
  "MythologIQ", "GG-CORE", "COREFORGE", "Qortara", "FailSafe",
  "Hill House", "Neat & Clean", "Chesapeake",
];
const VENDOR_API_RE = /\bapi\.[a-z][a-z0-9-]*\.(com|ai|dev|io)\b|[A-Z][A-Z0-9_]{2,}_API_KEY/;
const MCP_FALLBACK_RE = /\bMCP\b|web[- ]tool fallback|web search|web-search/i;

function body(text: string): string {
  const m = text.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/);
  return m ? text.slice(m[0].length) : text;
}

function outputFormatBlock(b: string): string {
  const m = b.match(/## Output Format[\s\S]*?```([\s\S]*?)```/);
  return m ? m[1] : "";
}

function checkJudgment(name: string, b: string): void {
  const block = outputFormatBlock(b);
  const highJudgment = SLOT_RE.test(block);
  const hasRules = /## Negative rules/.test(b);
  if (highJudgment && !hasRules) {
    fail(`${name}: high-judgment output slots (${block.match(SLOT_RE)?.[0]}) but no "## Negative rules" section`);
    return;
  }
  if (highJudgment && hasRules) {
    const rules = b.slice(b.indexOf("## Negative rules"));
    if (!SECRET_RULE_RE.test(rules)) fail(`${name}: negative rules lack a secret-handling rule`);
    if (!FABRICATION_RULE_RE.test(rules)) fail(`${name}: negative rules lack an anti-fabrication rule`);
    if (!GAP_RE.test(rules)) fail(`${name}: negative rules lack a missing-evidence fallback`);
  }
}

function checkMutation(name: string, b: string): void {
  const failVerb = b.match(FAIL_VERB_RE);
  const warnVerb = b.match(WARN_VERB_RE);
  const approved = APPROVAL_RE.test(b);
  if (failVerb && !approved) {
    fail(`${name}: mutating action "${failVerb[0]}" with no approval/read-only language anywhere in the skill`);
  } else if (warnVerb && !failVerb && !approved) {
    warn(`${name}: soft mutating verb "${warnVerb[0]}" with no approval/read-only language`);
  }
}

function checkPortability(name: string, b: string): void {
  if (/repo-bound/i.test(b)) return;
  const abs = b.match(ABS_PATH_RE);
  if (abs) warn(`${name}: portable skill body contains an absolute path ("${abs[0].trim()}")`);
  for (const term of RISK_TERMS) {
    if (b.includes(term)) warn(`${name}: portable skill body contains operator/org term "${term}"`);
  }
}

function checkExternalServices(name: string, b: string): void {
  const hit = b.match(VENDOR_API_RE);
  if (hit && !MCP_FALLBACK_RE.test(b)) {
    warn(`${name}: direct vendor API reference ("${hit[0]}") without an MCP or web-tool fallback`);
  }
}

function auditSkills(skillsDir: string): number {
  const skills = discoverSkillDirs(skillsDir);
  for (const skill of skills) {
    const b = body(readFileSync(skill.skillFile, "utf8"));
    checkJudgment(skill.name, b);
    checkMutation(skill.name, b);
    checkPortability(skill.name, b);
    checkExternalServices(skill.name, b);
  }
  return skills.length;
}

const count = auditSkills(values["skills-dir"]!);
for (const f of findings) console.log(`${f.level}: ${f.msg}`);
const failures = findings.filter((f) => f.level === "FAIL").length;
console.log(`\nrisk-audit: ${count} library skill(s), ${failures} failure(s), ${findings.length - failures} warning(s)`);
process.exit(failures > 0 ? 1 : 0);

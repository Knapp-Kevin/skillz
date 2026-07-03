/**
 * Shared zero-dep frontmatter helpers (LD-1: extracted from build-index.ts).
 *
 * Minimal YAML subset parser covering the frontmatter shapes used in this
 * repo and in the vendored official skill repos: top-level scalars,
 * >- / > / | folded and literal blocks, one nested map level, simple lists.
 * Not a general YAML parser by design.
 */

interface Cursor { lines: string[]; i: number; }

function indentOf(line: string): number {
  return line.length - line.trimStart().length;
}

function collectFolded(c: Cursor, indent: number): string {
  const parts: string[] = [];
  while (c.i < c.lines.length) {
    const l = c.lines[c.i];
    if (l.trim() && indentOf(l) <= indent) break;
    if (l.trim()) parts.push(l.trim());
    c.i++;
  }
  return parts.join(" ");
}

function collectList(c: Cursor): string[] {
  const arr: string[] = [];
  while (c.i < c.lines.length && c.lines[c.i].trim().startsWith("- ")) {
    arr.push(c.lines[c.i].trim().slice(2).replace(/^["']|["']$/g, ""));
    c.i++;
  }
  return arr;
}

function parseEmptyValue(c: Cursor, indent: number): any {
  if (c.i >= c.lines.length) return "";
  if (c.lines[c.i].trim().startsWith("- ")) return collectList(c);
  if (indentOf(c.lines[c.i]) > indent) return parseBlock(c, indentOf(c.lines[c.i]));
  return "";
}

function parseValue(c: Cursor, indent: number, val: string): any {
  if (val === ">-" || val === ">" || val === "|" || val === "|-") return collectFolded(c, indent);
  if (val === "") return parseEmptyValue(c, indent);
  return val.replace(/^["']|["']$/g, "");
}

function parseBlock(c: Cursor, indent: number): Record<string, any> {
  const obj: Record<string, any> = {};
  while (c.i < c.lines.length) {
    const line = c.lines[c.i];
    if (!line.trim()) { c.i++; continue; }
    const curIndent = indentOf(line);
    if (curIndent < indent) break;
    if (curIndent > indent) { c.i++; continue; } // stray deeper line; skip
    const kv = line.trim().match(/^([\w][\w.-]*):\s*(.*)$/);
    if (!kv) { c.i++; continue; }
    c.i++;
    obj[kv[1]] = parseValue(c, indent, kv[2]);
  }
  return obj;
}

export function parseFrontmatter(md: string): Record<string, any> | null {
  const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return null;
  return parseBlock({ lines: m[1].split(/\r?\n/), i: 0 }, 0);
}

export function truncate(s: unknown, n: number): string {
  const clean = (typeof s === "string" ? s : "").replace(/\s+/g, " ").trim();
  return clean.length <= n ? clean : clean.slice(0, n - 1).trimEnd() + "…";
}

import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

export interface VerificationTags {
  use_case: string[];
  lifecycle: string[];
  characteristic: string[];
  authority: string[];
  portability: string[];
}

export interface VerificationRecord {
  sourceId: string;
  skillName: string;
  status: string;
  validationStatus: string;
  fingerprintAlgorithm: string;
  contentBlobSha: string;
  characterizedAt: string;
  lastVerifiedAt: string;
  verificationBasis: string;
  tags: VerificationTags;
}

function unquote(value: string): string {
  return value.trim().replace(/^["']|["']$/g, "");
}

function parseInlineList(value: string): string[] {
  const trimmed = value.trim();
  if (!trimmed.startsWith("[") || !trimmed.endsWith("]")) return [];
  const body = trimmed.slice(1, -1).trim();
  if (!body) return [];
  return body.split(",").map((v) => unquote(v.trim())).filter(Boolean);
}

export function readVerificationRecord(root: string, sourceId: string, skillName: string): VerificationRecord | null {
  const file = join(root, "registry", "verification", sourceId, `${skillName}.yaml`);
  if (!existsSync(file)) return null;

  const lines = readFileSync(file, "utf8").split(/\r?\n/);
  const fields = new Map<string, string>();
  const tags: VerificationTags = {
    use_case: [], lifecycle: [], characteristic: [], authority: [], portability: [],
  };
  let inTags = false;

  for (const line of lines) {
    if (/^tags:\s*$/.test(line)) {
      inTags = true;
      continue;
    }
    if (inTags) {
      const tag = line.match(/^\s{2}([\w_]+):\s*(\[.*\])\s*$/);
      if (tag) {
        const key = tag[1] as keyof VerificationTags;
        if (key in tags) tags[key] = parseInlineList(tag[2]);
        continue;
      }
      if (line.trim() && !/^\s/.test(line)) inTags = false;
    }
    const field = line.match(/^([\w_]+):\s*(.*?)\s*$/);
    if (field) fields.set(field[1], unquote(field[2]));
  }

  return {
    sourceId: fields.get("source_id") ?? sourceId,
    skillName: fields.get("skill_name") ?? skillName,
    status: fields.get("verification_status") ?? "unverified",
    validationStatus: fields.get("validation_status") ?? "not-run",
    fingerprintAlgorithm: fields.get("fingerprint_algorithm") ?? "",
    contentBlobSha: fields.get("content_blob_sha") ?? "",
    characterizedAt: fields.get("characterized_at") ?? "",
    lastVerifiedAt: fields.get("last_verified_at") ?? "",
    verificationBasis: fields.get("verification_basis") ?? "",
    tags,
  };
}

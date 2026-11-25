"""Source-level onboarding and README Architect checks; no host installation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
ARCH = ROOT / "skills/authored/repository-readme-architect/scripts"
sys.path.insert(0, str(ARCH))
import profile_acceptance
import check_readme

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

class OnboardingTests(unittest.TestCase):
    def test_agent_and_human_routes_appear_before_contents(self):
        source = read("README.md")
        opening = source.split("## Quick start", 1)[0]
        for path in ("AGENT_START_HERE.md", "AGENTS.md", "CLAUDE.md",
                     "skills/authored/README.md", "docs/getting-started-with-skills.md"):
            self.assertIn("](" + path, opening)
        self.assertIn("AI agents: start here", opening)
        quick = source.split("## Quick start", 1)[1].split("## Contents", 1)[0]
        for phrase in ("SHA-256", "fictional", "manual installation", "First useful result"):
            self.assertIn(phrase.lower(), quick.lower())

    def test_all_entrypoints_route_to_same_catalog_and_guide(self):
        for path in ("README.md", "AGENTS.md", "CLAUDE.md", "AGENT_START_HERE.md",
                     "engine/skills/skill-bootstrap/SKILL.md", "docs/consumer-discovery-and-installation.md"):
            source = read(path)
            for target in ("skills/authored/README.md", "getting-started-with-skills.md"):
                self.assertIn(target, source, path)
        self.assertIn("@AGENTS.md", read("CLAUDE.md"))
        self.assertIn("DIRECT_LIBRARY", read("engine/skills/skill-bootstrap/SKILL.md"))

    def test_catalog_complete_and_download_links_unique(self):
        source = read("skills/authored/README.md")
        ids = {s["id"] for s in json.loads(read("registry/authored-skills-index.json"))["skills"]}
        downloads = re.findall(r"releases/latest/download/([a-z0-9-]+)\.zip\)", source)
        self.assertEqual(set(downloads), ids)
        self.assertEqual(len(downloads), len(ids))
        self.assertIn("## Manual installation steps by environment", read("docs/getting-started-with-skills.md"))

    def test_host_asset_selection_and_release_identity_precede_installation(self):
        guide = read("docs/getting-started-with-skills.md")
        download = guide.split("## Download your skill", 1)[1].split("## Manual installation", 1)[0]
        for phrase in ("source_commit", "PACKAGE_READY", "hosts", "sha256",
                       "releases/download/authored-<source_commit>/<asset>",
                       "Do not fetch a second moving", "-claude.zip", "-gemini.zip", "-m365.zip"):
            self.assertIn(phrase, download)
        self.assertLess(download.index("PACKAGE_READY"), download.index("Download the selected asset"))
        self.assertLess(download.index("Compare the downloaded"), download.index("Follow your exact host"))
        for path in ("README.md", "skills/authored/README.md", "AGENT_START_HERE.md", "AGENTS.md"):
            source = read(path)
            self.assertIn("source-pinned", source, path)
            self.assertIn("#download-your-skill", source, path)
        self.assertIn("| Claude Apps (web, desktop, Cowork) |", guide)
        self.assertIn("Do not rename executable PowerShell scripts as text", guide)

    def test_architect_local_links_and_document_first_profile(self):
        asset = ROOT / "docs/assets/skillz-original-banner.png"
        # The original committed banner identity must not drift silently.
        self.assertEqual(subprocess.check_output(["git", "hash-object", str(asset)], cwd=ROOT, text=True).strip(), "f5f65d45feabe20440ed8af2ba12498fa5141783")
        cfg = {"schema_version": 1, "profile": "gold", "project_identity": "Skillz",
               "banner_path": "docs/assets/skillz-original-banner.png",
               "required_badge_labels": ["Authored downloads", "License", "Downloads"],
               "allowed_badge_targets": ["https://github.com/Knapp-Kevin/skillz/actions/workflows/authored-downloads.yml",
                 "https://github.com/Knapp-Kevin/skillz/blob/main/LICENSE",
                 "https://github.com/Knapp-Kevin/skillz/releases/latest"],
               "journey_mode": "read", "exceptions": [],
               "asset_inventory": [{"path": "docs/assets/skillz-original-banner.png",
                   "status": "verified-existing", "owner": "Skillz project; rights and rendering require review",
                   "purpose": "Existing project-specific banner", "alt": "Skillz banner with illustrations of AI, code, research, analytics, and security",
                   "replacement": "Preserve existing asset; separate authorized change if needed",
                   "sha256": hashlib.sha256(asset.read_bytes()).hexdigest()}]}
        result = profile_acceptance.audit(ROOT, "README.md", cfg)
        print(json.dumps(result, indent=2))
        self.assertEqual(result["failed"], 0)
        self.assertEqual(result["quality_status"], "HOLD")
        self.assertFalse(result["completion_permitted"])
        self.assertEqual(check_readme.audit(ROOT, ROOT / "README.md")["local_blockers"], 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)

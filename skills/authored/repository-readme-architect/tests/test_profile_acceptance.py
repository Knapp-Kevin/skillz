#!/usr/bin/env python3
"""Anonymous, offline adversarial Gold/Platinum README quality regression."""
import json
import hashlib
import zlib
import binascii
from pathlib import Path
import sys
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))
import profile_acceptance as profile

BASE = """# Example Kit

![An original Example Kit visual that introduces the project](assets/banner.png)

[![Build](https://img.example.invalid/build.svg)](https://code.example.invalid/build)
[![License](https://img.example.invalid/license.svg)](https://code.example.invalid/license)

Many projects make new users sift through technical details before finding
out what they can actually do. Example Kit helps them see the value of their
work quickly. It offers a small verified demonstration with a visible result.
Follow the first steps to see a useful result without guessing how it works.

## Contents
- [Quick Start](#quick-start)
- [Documentation](#documentation)

## Quick Start

Run this example to create a visible demonstration:

~~~sh
python -m example_kit demo
~~~

Expected result: the program prints a small example report.

## Documentation

See [the technical guide](docs/guide.md) for deeper implementation details.
"""
CONTRACT = {
    "schema_version": 1, "profile": "gold", "project_identity": "Example Kit",
    "banner_path": "assets/banner.png",
    "required_badge_labels": ["Build", "License"],
    "allowed_badge_targets": ["https://code.example.invalid/build",
                              "https://code.example.invalid/license"],
    "journey_mode": "execute",
    "asset_inventory": [{
        "path": "assets/banner.png", "status": "newly-committed",
        "owner": "Verified project maintainer",
        "purpose": "Illustrate the project's actual identity",
        "alt": "An original Example Kit visual that introduces the project",
        "replacement": "None after final brand acceptance"
    }],
    "exceptions": []
}


def valid_banner(rgb=b"\xf0\xf4\xff"):
    """Generate a real, valid 960x240 RGB PNG without external dependencies."""
    width, height = 960, 240
    def chunk(name, payload):
        return (len(payload).to_bytes(4, "big") + name + payload +
                (binascii.crc32(name + payload) & 0xffffffff).to_bytes(4, "big"))
    header = width.to_bytes(4, "big") + height.to_bytes(4, "big") + b"\x08\x02\x00\x00\x00"
    row = b"\x00" + rgb * width
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) +
            chunk(b"IDAT", zlib.compress(row * height)) + chunk(b"IEND", b""))


class QualityProfileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "assets").mkdir()
        (self.root / "assets/banner.png").write_bytes(valid_banner())
        (self.root / "docs").mkdir()
        (self.root / "docs/guide.md").write_text("# Technical Guide\n", encoding="utf-8")
        self.write_readme(BASE)
        self.contract = json.loads(json.dumps(CONTRACT))
        self.contract["asset_inventory"][0]["sha256"] = hashlib.sha256(
            (self.root / "assets/banner.png").read_bytes()).hexdigest()
        self.write_contract()

    def write_readme(self, text):
        (self.root / "README.md").write_text(text, encoding="utf-8")

    def write_contract(self):
        (self.root / "profile.json").write_text(json.dumps(self.contract), encoding="utf-8")

    def evaluate(self):
        return profile.audit(self.root, "README.md", self.contract)

    def gate(self, name):
        return [x for x in self.evaluate()["checks"] if x["key"] == name]

    def test_complete_structure_still_does_not_self_award_gold(self):
        r = self.evaluate()
        self.assertEqual(r["quality_status"], "HOLD")
        self.assertEqual(r["failed"], 0)
        self.assertFalse(r["completion_permitted"])
        self.assertEqual(r["technical_delivery_status"], "NOT_RUN")
        self.assertEqual(r["editorial_acceptance_status"], "HOLD")

    def test_valid_replacement_banner_pixels_still_fail_prior_digest(self):
        path = self.root / "assets/banner.png"
        before = path.read_bytes()
        modified = valid_banner(b"\xe0\xe4\xef")
        self.assertNotEqual(before, modified)
        path.write_bytes(modified)
        self.assertEqual(self.gate("asset-digest")[0]["status"], "FAIL")
        self.assertFalse(self.evaluate()["assets_approved"])

    def test_corrupt_png_banner_fails_before_human_visual_check(self):
        (self.root / "assets/banner.png").write_bytes(b"\x89PNG\r\n\x1a\ncorrupt")
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_narrow_banner_cannot_silently_pass_hero_profile(self):
        path = self.root / "assets/banner.png"
        data = bytearray(path.read_bytes())
        data[16:20] = (200).to_bytes(4, "big")
        self.assertEqual(profile._image_geometry(path)[0], 200)
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_missing_public_purpose_introduction_fails(self):
        self.write_readme(BASE.replace(
            "Many projects make new users sift through technical details before finding\n"
            "out what they can actually do. Example Kit helps them see the value of their\n"
            "work quickly. It offers a small verified demonstration with a visible result.\n"
            "Follow the first steps to see a useful result without guessing how it works.",
            ""))
        self.assertEqual(self.gate("opening-meaning")[0]["status"], "FAIL")

    def test_equation_first_opening_fails(self):
        self.write_readme(BASE.replace(
            "Many projects make new users sift through technical details before finding",
            "∑ x_i = y. Many projects make new users sift through technical details before finding"))
        self.assertEqual(self.gate("opening-meaning")[0]["status"], "FAIL")

    def test_present_readable_intro_is_held_until_editorial_review(self):
        self.assertEqual(self.gate("opening-meaning")[0]["status"], "HOLD")

    def test_html_picture_banner_supported_but_not_auto_visual_pass(self):
        original = "![An original Example Kit visual that introduces the project](assets/banner.png)"
        html = ('<picture><source media="(prefers-color-scheme: dark)" '
                'srcset="assets/banner.png">'
                '<img src="assets/banner.png" '
                'alt="An original Example Kit visual that introduces the project"></picture>')
        self.write_readme(BASE.replace(original, html))
        self.assertEqual(self.gate("banner")[0]["status"], "HOLD")
        self.assertEqual(self.gate("html-images")[0]["status"], "HOLD")

    def test_html_banner_without_alt_is_not_accessible(self):
        original = "![An original Example Kit visual that introduces the project](assets/banner.png)"
        self.write_readme(BASE.replace(original, '<img src="assets/banner.png">'))
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_active_svg_banner_fails_integrity(self):
        (self.root / "assets/banner.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 240">'
            '<script>alert(1)</script></svg>', encoding="utf-8")
        self.contract["banner_path"] = "assets/banner.svg"
        self.contract["asset_inventory"][0]["path"] = "assets/banner.svg"
        self.contract["asset_inventory"][0]["sha256"] = hashlib.sha256(
            (self.root / "assets/banner.svg").read_bytes()).hexdigest()
        self.write_readme(BASE.replace("assets/banner.png", "assets/banner.svg"))
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_valid_svg_still_requires_rendered_brand_review(self):
        (self.root / "assets/banner.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 240">'
            '<rect width="960" height="240" fill="navy"/></svg>', encoding="utf-8")
        self.contract["banner_path"] = "assets/banner.svg"
        self.contract["asset_inventory"][0]["path"] = "assets/banner.svg"
        self.contract["asset_inventory"][0]["sha256"] = hashlib.sha256(
            (self.root / "assets/banner.svg").read_bytes()).hexdigest()
        self.write_readme(BASE.replace("assets/banner.png", "assets/banner.svg"))
        self.assertEqual(self.gate("banner")[0]["status"], "HOLD")

    def test_unrelated_product_named_in_banner_alt_fails(self):
        self.write_readme(BASE.replace(
            "An original Example Kit visual that introduces the project",
            "An original Other Toolkit visual that introduces the project"))
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_missing_asset_owner_refuses_contract(self):
        self.contract["asset_inventory"][0]["owner"] = ""
        self.write_contract()
        with self.assertRaises(profile.InputError):
            profile.contract_from(self.root / "profile.json")

    def test_duplicate_asset_inventory_refuses_audit(self):
        self.contract["asset_inventory"].append(dict(self.contract["asset_inventory"][0]))
        with self.assertRaises(profile.InputError):
            self.evaluate()

    def test_uninventoried_logo_asset_fails(self):
        (self.root / "assets/other.png").write_bytes(valid_banner())
        self.write_readme(BASE + "\n![Another branding image](assets/other.png)\n")
        self.assertTrue(any(x["status"] == "FAIL" for x in self.gate("asset-status")))

    def test_remote_brand_image_is_unverified_not_implicitly_approved(self):
        self.write_readme(BASE + "\n![A remote visual representing Example Kit](https://cdn.example.invalid/kit.png)\n")
        self.assertTrue(any(x["status"] == "HOLD" for x in self.gate("asset-status")))
        self.assertFalse(self.evaluate()["assets_approved"])

    def test_missing_banner_is_failed(self):
        self.write_readme(BASE.replace("![An original Example Kit visual that introduces the project](assets/banner.png)", ""))
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_wrong_product_banner_is_failed(self):
        self.write_readme(BASE.replace("(assets/banner.png)", "(assets/unrelated.png)"))
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_missing_asset_file_fails(self):
        (self.root / "assets/banner.png").unlink()
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_placeholder_cannot_be_final(self):
        self.contract["asset_inventory"][0]["status"] = "proposed-placeholder"
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_unreadable_alt_fails(self):
        self.write_readme(BASE.replace("![An original Example Kit visual that introduces the project]", "![logo]"))
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")

    def test_missing_build_badge_fails(self):
        self.write_readme(BASE.replace("[![Build](https://img.example.invalid/build.svg)](https://code.example.invalid/build)", ""))
        self.assertEqual(self.gate("badge:Build")[0]["status"], "FAIL")

    def test_unrelated_badge_destination_fails(self):
        self.write_readme(BASE.replace("https://code.example.invalid/license)", "https://competitor.example.invalid/license)"))
        self.assertEqual(self.gate("badge:License")[0]["status"], "FAIL")

    def test_deceptive_badge_source_fails(self):
        self.write_readme(BASE.replace("https://img.example.invalid/build.svg", "javascript:fake"))
        self.assertEqual(self.gate("badge:Build")[0]["status"], "FAIL")

    def test_missing_toc_fails(self):
        self.write_readme(BASE.replace("## Contents", "## Reading Area"))
        self.assertEqual(self.gate("toc")[0]["status"], "FAIL")

    def test_toc_label_points_at_wrong_heading_fails(self):
        self.write_readme(BASE.replace("[Quick Start](#quick-start)", "[Quick Start](#documentation)"))
        self.assertEqual(self.gate("toc")[0]["status"], "FAIL")

    def test_broken_toc_anchor_fails(self):
        self.write_readme(BASE.replace("#quick-start", "#not-a-heading"))
        self.assertEqual(self.gate("toc")[0]["status"], "FAIL")

    def test_nested_quick_start_subheadings_keep_real_first_use(self):
        self.write_readme(BASE.replace(
            "## Quick Start\n\nRun this example",
            "## Quick Start\n\n### Installation\n\n"
            "Inspect the requirements and use the supported demo.\n\n"
            "### Try it\n\nRun this example"))
        self.assertEqual(self.gate("first-success")[0]["status"], "HOLD")
        self.assertEqual(self.evaluate()["quality_status"], "HOLD")

    def test_nested_contents_headings_do_not_hide_real_links(self):
        self.write_readme(BASE.replace(
            "## Contents\n- [Quick Start]",
            "## Contents\n### Reader paths\n- [Quick Start]"))
        self.assertEqual(self.gate("toc")[0]["status"], "PASS")

    def test_nested_section_stops_at_sibling_not_next_subheading(self):
        lines = ["## Quick Start", "### Install", "Install package",
                 "### Try it", "Run the demo", "## Documentation",
                 "The quick start must not include this section"]
        section = profile._section(lines, profile.START_HEAD)
        self.assertIn("### Try it", section)
        self.assertIn("Run the demo", section)
        self.assertNotIn("Documentation", section)

    def test_fake_heading_in_quick_start_code_fence_does_not_truncate_use(self):
        self.write_readme(BASE.replace(
            "python -m example_kit demo",
            "## command comment that is not a Markdown heading\n"
            "python -m example_kit demo"))
        self.assertEqual(self.gate("first-success")[0]["status"], "HOLD")

    def test_nested_quick_start_without_use_still_fails(self):
        before = BASE.split("## Quick Start",1)[0]
        after = BASE.split("## Documentation",1)[1]
        self.write_readme(before + "## Quick Start\n\n"
                          "### Installation\n\n"
                          "Only generic installation advice.\n\n"
                          "## Documentation" + after)
        self.assertEqual(self.gate("first-success")[0]["status"], "FAIL")

    def test_missing_first_use_fails(self):
        self.write_readme(BASE.replace("## Quick Start", "## Unrelated Section"))
        self.assertEqual(self.gate("first-success")[0]["status"], "FAIL")

    def test_generic_test_command_without_outcome_fails(self):
        text = BASE.replace("python -m example_kit demo", "cargo test")
        text = text.replace("Expected result: the program prints a small example report.", "")
        self.write_readme(text)
        self.assertEqual(self.gate("first-success")[0]["status"], "FAIL")

    def test_generic_developer_test_still_fails_even_with_expected_result(self):
        self.write_readme(BASE.replace("python -m example_kit demo", "cargo test"))
        self.assertEqual(self.gate("first-success")[0]["status"], "FAIL")

    def test_unrelated_code_example_does_not_rescue_empty_quick_start(self):
        text = BASE.replace(
            "~~~sh\npython -m example_kit demo\n~~~",
            "See the technical reference later in this README.")
        text += "\n## Developer Test\n\n~~~sh\npython -m example_kit demo\n~~~\n"
        self.write_readme(text)
        self.assertEqual(self.gate("first-success")[0]["status"], "FAIL")

    def test_missing_expected_result_fails(self):
        self.write_readme(BASE.replace("Expected result: the program prints a small example report.", ""))
        self.assertEqual(self.gate("first-success")[0]["status"], "FAIL")

    def test_document_first_journey_must_have_next_action(self):
        self.contract["journey_mode"] = "read"
        self.write_readme(BASE.replace("Run this example to create a visible demonstration:", "Study the material:")
                          .replace("See [the technical guide](docs/guide.md)", "There is a technical guide"))
        self.assertEqual(self.gate("first-success")[0]["status"], "FAIL")

    def test_reading_journey_with_link_is_held_for_user_test(self):
        self.contract["journey_mode"] = "read"
        self.write_readme(BASE.replace("Run this example to create a visible demonstration:",
                                      "Read [the technical guide](docs/guide.md) to understand the approach:"))
        self.assertEqual(self.gate("first-success")[0]["status"], "HOLD")

    def test_missing_technical_navigation_fails(self):
        self.write_readme(BASE.replace("## Documentation", "## Miscellaneous"))
        self.assertEqual(self.gate("technical-navigation")[0]["status"], "FAIL")

    def test_lost_verified_technical_link_is_caught(self):
        self.write_readme(BASE.replace("docs/guide.md", "docs/missing.md"))
        self.assertEqual(self.gate("local-links")[0]["status"], "FAIL")

    def test_unmarked_makefile_generator_gets_an_ownership_hold(self):
        (self.root / "Makefile").write_text(
            "README.md:\n\tpython docs/generate.py > README.md\n",
            encoding="utf-8")
        self.assertEqual(self.gate("generated-owner")[0]["status"], "HOLD")

    def test_unmarked_workflow_rebuild_of_root_readme_is_detected(self):
        folder = self.root / ".github/workflows"
        folder.mkdir(parents=True)
        (folder / "docs.yml").write_text(
            "name: docs\nsteps:\n  - run: python docs/render.py --output README.md\n",
            encoding="utf-8")
        self.assertEqual(self.gate("generated-owner")[0]["status"], "HOLD")

    def test_generated_owner_never_self_clears(self):
        self.write_readme(BASE + "\n<!-- generated:begin -->\ngenerated text\n<!-- generated:end -->\n")
        self.assertEqual(self.gate("generated-owner")[0]["status"], "HOLD")
        self.assertFalse(self.evaluate()["generated_parity_qualified"])

    def test_exception_never_suppresses_missing_banner(self):
        self.contract["exceptions"].append({
            "requirement":"banner", "reason":"No designer currently available",
            "evidence_ref":"internal request #12"})
        self.write_readme(BASE.replace("![An original Example Kit visual that introduces the project](assets/banner.png)", ""))
        self.assertEqual(self.gate("banner")[0]["status"], "FAIL")
        self.assertEqual(self.gate("exceptions")[0]["status"], "HOLD")

    def test_wrong_title_fails_independent_of_banner(self):
        self.write_readme(BASE.replace("# Example Kit", "# Another Product", 1))
        self.assertEqual(self.gate("identity")[0]["status"], "FAIL")

    def test_contract_cannot_disable_required_badges(self):
        self.contract["required_badge_labels"] = []
        self.write_contract()
        with self.assertRaises(profile.InputError):
            profile.contract_from(self.root / "profile.json")

    def test_contract_rejects_duplicate_keys(self):
        (self.root / "profile.json").write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
        with self.assertRaises(profile.InputError):
            profile.contract_from(self.root / "profile.json")

    def test_contract_rejects_symlinked_banner(self):
        (self.root / "assets/banner.png").unlink()
        try:
            (self.root / "assets/banner.png").symlink_to("../docs/guide.md")
        except OSError:
            self.skipTest("symlinks unsupported")
        with self.assertRaises(profile.InputError):
            self.evaluate()

    def test_badge_success_not_external_validation(self):
        r = self.evaluate()
        self.assertFalse(r["external_badges_authenticated"])
        self.assertFalse(r["assets_approved"])

    def test_platinum_always_requires_independent_reader(self):
        self.contract["profile"] = "platinum"
        self.assertEqual(self.gate("independent-reader")[0]["status"], "HOLD")

    def test_local_checker_cannot_claim_visual_review(self):
        self.assertFalse(self.evaluate()["rendered_review_completed"])

    def test_sample_profile_has_explicit_asset_lifecycle(self):
        sample = json.loads((SKILL / "examples/gold-quality-profile.json").read_text("utf-8"))
        self.assertEqual(sample["profile"], "gold")
        self.assertIn("asset_inventory", sample)
        self.assertIn(sample["asset_inventory"][0]["status"], profile.STATES)


if __name__ == "__main__":
    unittest.main(verbosity=2)

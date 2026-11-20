#!/usr/bin/env python3
"""Original, CPU-only quantization correctness adversarial controls for #728.

This script NEVER imports, executes, installs, benchmarks, or redistributes
third-party kernel code. It can optionally inspect exact pinned Git objects
as untrusted text, and writes an exclusive-create JSON evidence receipt.
"""
import argparse
import json
import math
from pathlib import Path
import struct
import subprocess
import unittest

INT32_MAX = 2**31 - 1
UPSTREAM_COMMIT = "7b7337a123f8711aa8e3d0452351d8fd30dde4b7"
UPSTREAM_TREE = "01ac1803e1046fe2883a1bd089d70aa817ddc8d8"
PACKAGES = {
    "quantization/debug-quantized-kernel-accuracy": (
        "22393b767b89f64ab669ed3507d6ae49bc6a1a43",
        "4a09a68f143ae47c78df0bdea5b5db1854ebca93",
        "d402b28f00634b759c74594edfe9404c087f472c"),
    "quantization/write-int8-quantized-kernel": (
        "34ba484cf823a3f0d74b3b4aad70db7163fc2112",
        "66453dc4e638d285cd30ae98bc7236b96c9b90bd",
        "30824f4a8b0c6166ba663201b081780d71af9c43"),
    "inference/write-triton-dequant-kernel": (
        "f6fc2496c7361f66aba0c49a7903b33010271e3f",
        "7607a10910bab6efc8ddec64181f8c1c63607a6e",
        "0a327c0563f5d478fe6d19a43aa9e7a6358f07c7"),
}
PROOF = "proof/quantization/int8/int8-quantized-proof.md"
PROOF_SHA = "8ea720219ade32886435b71ea6613633d4b436c3"


def symmetric_q(x, scale):
    if not math.isfinite(x) or not math.isfinite(scale) or scale <= 0:
        raise ValueError("finite input and positive finite scale required")
    return max(-127, min(127, round(x / scale)))


def asymmetric_dot(q_a, q_b, z_a, z_b):
    if len(q_a) != len(q_b):
        raise ValueError("reduction lengths differ")
    if any(not 0 <= q <= 255 for q in (*q_a, *q_b)):
        raise ValueError("expected unsigned 8-bit operands")
    return sum((a - z_a) * (b - z_b) for a, b in zip(q_a, q_b))


def asymmetric_dot_expanded(q_a, q_b, z_a, z_b):
    k = len(q_a)
    return (sum(a * b for a, b in zip(q_a, q_b))
            - z_b * sum(q_a) - z_a * sum(q_b) + k * z_a * z_b)


def safe_k(max_a, max_b):
    if not all(isinstance(x, int) and x > 0 for x in (max_a, max_b)):
        raise ValueError("positive exact integer bounds required")
    return INT32_MAX // (max_a * max_b)


def roundtrip_bound_holds(values, scale):
    return all(abs(v - symmetric_q(v, scale) * scale)
               <= scale / 2 + 1e-12 for v in values)


def dot(values_a, values_b):
    if len(values_a) != len(values_b):
        raise ValueError("dot length mismatch")
    return sum(a * b for a, b in zip(values_a, values_b))


def no_clipping_dot_bound(a, b, sa, sb):
    """Triangle bound for independent rounding of two operands, exact real arithmetic.

    For each product: |a*b-aq*bq| <= |a|*delta_b + |b|*delta_a
                                + delta_a*delta_b.
    This is NOT a bound on GPU accumulation/output rounding.
    """
    return sum(abs(x) * (sb / 2) + abs(y) * (sa / 2) + sa * sb / 4
               for x, y in zip(a, b))


def roundtrip_dot(a, b, sa, sb):
    qa = [symmetric_q(x, sa) for x in a]
    qb = [symmetric_q(y, sb) for y in b]
    return dot(qa, qb) * sa * sb


def unpack_int4(word, order=tuple(range(8))):
    if sorted(order) != list(range(8)):
        raise ValueError("packing order must permute eight nibbles")
    return [(word >> (4 * n)) & 15 for n in order]


def tile_crosses_group(start_k, block_k, group_size):
    if min(block_k, group_size) <= 0 or start_k < 0:
        raise ValueError("invalid tile")
    return start_k // group_size != (start_k + block_k - 1) // group_size


def fp32_ulp_positive(value):
    bits = struct.unpack("<I", struct.pack("<f", value))[0]
    return (struct.unpack("<f", struct.pack("<I", bits + 1))[0]
            - struct.unpack("<f", struct.pack("<I", bits))[0])


def source_git(root, *argv):
    return subprocess.check_output(
        ["git", "-C", str(root), "-c", "core.hooksPath=/dev/null", *argv],
        text=True, timeout=20).strip()


def check_pinned_source(root):
    root = Path(root).resolve(strict=True)
    assert source_git(root, "rev-parse", "HEAD") == UPSTREAM_COMMIT
    assert source_git(root, "rev-parse", "HEAD^{tree}") == UPSTREAM_TREE
    findings = {}
    for name, (expected_tree, skill_blob, metadata_blob) in PACKAGES.items():
        folder = "skills/" + name
        assert source_git(root, "rev-parse", "HEAD:" + folder) == expected_tree
        assert source_git(root, "rev-parse", "HEAD:" + folder + "/SKILL.md") == skill_blob
        assert source_git(root, "rev-parse", "HEAD:" + folder + "/skill.json") == metadata_blob
        entries = source_git(root, "ls-tree", "--name-only", "HEAD:" + folder).splitlines()
        assert entries == ["SKILL.md", "skill.json"], (folder, entries)
        skill = (root / folder / "SKILL.md").read_text(encoding="utf-8")
        meta = json.loads((root / folder / "skill.json").read_text(encoding="utf-8"))
        assert meta["entry"] == folder + "/SKILL.md"
        findings[name] = {
            "package_tree": expected_tree, "skill_blob": skill_blob,
            "metadata_blob": metadata_blob, "package_files": entries,
        }
        if name.endswith("write-int8-quantized-kernel"):
            assert "sm_75" in skill and "scale / 127" in skill
        if name.endswith("debug-quantized-kernel-accuracy"):
            assert "1–3 ULPs" in skill and "0.5 * scale" in skill
        if name.endswith("write-triton-dequant-kernel"):
            assert "torch.allclose(atol=scale.max() / 2)" in skill
            assert "BLOCK_K must be" in skill
    assert source_git(root, "rev-parse", "HEAD:" + PROOF) == PROOF_SHA
    proof = (root / PROOF).read_text(encoding="utf-8")
    assert "128×128" in proof and "2 KB" in proof
    return findings


class QuantizationClaimControls(unittest.TestCase):
    def test_scalar_half_step_only_without_clipping(self):
        self.assertTrue(roundtrip_bound_holds([0, 0.49, 10.25, 126.8, 127], 1))

    def test_clipping_breaks_half_step_bound(self):
        self.assertFalse(roundtrip_bound_holds([127.0, 129.0], 1))
        self.assertEqual(abs(129 - symmetric_q(129, 1)), 2)

    def test_unphysical_rounding_scale_over_127_claim(self):
        self.assertGreater(abs(0.49 - symmetric_q(0.49, 1)), 0.5 * (1 / 127))

    def test_int8_gemm_error_can_exceed_scalar_step_by_four_orders(self):
        a, b = [127.0, 0.49], [127.0, 127.0]
        error = abs(dot(a, b) - roundtrip_dot(a, b, 1, 1))
        self.assertAlmostEqual(error, 62.23)
        self.assertGreater(error / (0.5 / 127), 15000)

    def test_nonclipping_two_quantizer_dot_bound_is_valid_for_fixture(self):
        a, b = [127.0, 0.49], [127.0, 127.0]
        error = abs(dot(a, b) - roundtrip_dot(a, b, 1, 1))
        self.assertLessEqual(error, no_clipping_dot_bound(a, b, 1, 1))

    def test_nonclipping_dot_bound_is_not_an_output_rounding_guarantee(self):
        a, b = [0.49] * 10, [127.0] * 10
        self.assertLessEqual(abs(dot(a, b) - roundtrip_dot(a, b, 1, 1)),
                             no_clipping_dot_bound(a, b, 1, 1))
        self.assertGreater(abs(dot(a, b) - roundtrip_dot(a, b, 1, 1)), 100)

    def test_symmetric_int32_exact_safe_limit(self):
        self.assertEqual(safe_k(127, 127), 133144)
        self.assertLessEqual(127 * 127 * 131072, INT32_MAX)
        self.assertLessEqual(127 * 127 * 133144, INT32_MAX)
        self.assertGreater(127 * 127 * 133145, INT32_MAX)

    def test_signed_minus_128_changes_overflow_limit(self):
        self.assertEqual(safe_k(128, 128), 131071)
        self.assertGreater(128 * 128 * 131072, INT32_MAX)

    def test_unsigned_asymmetric_bound_must_not_reuse_127_squared(self):
        self.assertEqual(safe_k(255, 255), INT32_MAX // 65025)
        self.assertLess(safe_k(255, 255), safe_k(127, 127))

    def test_zero_point_expansion_matches_centered_integer_dot(self):
        qa, qb, za, zb = [15, 17], [19, 24], 14, 18
        self.assertEqual(asymmetric_dot(qa, qb, za, zb), 19)
        self.assertEqual(asymmetric_dot_expanded(qa, qb, za, zb), 19)

    def test_no_zero_point_correction_is_not_equivalent(self):
        qa, qb = [15, 17], [19, 24]
        self.assertNotEqual(dot(qa, qb), asymmetric_dot(qa, qb, 14, 18))

    def test_channel_scale_changes_n_not_reduction_length(self):
        accum = [2, 2]
        channel_scale = [0.1, 10]
        self.assertEqual(len([1, 1]), 2)
        self.assertEqual([accum[i] * channel_scale[i] for i in range(2)],
                         [0.2, 20.0])

    def test_unaligned_block_crosses_group_even_when_block_smaller(self):
        self.assertLessEqual(64, 96)
        self.assertTrue(tile_crosses_group(64, 64, 96))
        self.assertFalse(tile_crosses_group(0, 64, 96))

    def test_scheme_specific_packing_order_is_not_universal(self):
        packed = sum(i << (4 * i) for i in range(8))
        sequential = unpack_int4(packed)
        interleaved = unpack_int4(packed, (0, 4, 1, 5, 2, 6, 3, 7))
        self.assertNotEqual(sequential, interleaved)
        self.assertEqual(sorted(interleaved), list(range(8)))

    def test_global_atol_can_hide_bad_small_group_dequant(self):
        global_atol = max(0.01, 100) / 2
        local_error = 20.0
        self.assertLess(local_error, global_atol)
        self.assertGreater(local_error, 0.01 / 2)

    def test_unit_in_last_place_is_not_quantized_gemm_error_bound(self):
        a, b = [127.0, 0.49], [127.0, 127.0]
        error = abs(dot(a, b) - roundtrip_dot(a, b, 1, 1))
        self.assertGreater(error, 3 * fp32_ulp_positive(dot(a, b)))

    def test_int32_intermediate_memory_traffic_arithmetic(self):
        self.assertEqual(128 * 128 * 4, 65536)
        self.assertEqual(2 * 128 * 128 * 4, 131072)
        self.assertEqual(512 * 512 * 4, 1048576)
        self.assertEqual(2 * 512 * 512 * 4, 2097152)

    def test_hostile_nan_infinite_scale_and_invalid_ranges_are_refused(self):
        for val, scale in ((math.nan, 1), (math.inf, 1), (1, 0), (1, math.inf)):
            with self.assertRaises(ValueError):
                symmetric_q(val, scale)
        with self.assertRaises(ValueError):
            safe_k(0, 127)


def receipt(source_root):
    package_proofs = check_pinned_source(source_root)
    a, b = [127.0, 0.49], [127.0, 127.0]
    err = abs(dot(a, b) - roundtrip_dot(a, b, 1, 1))
    return {
        "schema": "skillz/quantized-kernel-static-cpu-adjudication/1",
        "source": {"repository": "https://github.com/tensormux/kernel-skills",
                   "commit": UPSTREAM_COMMIT, "tree": UPSTREAM_TREE,
                   "packages": package_proofs,
                   "additional_proof_git_blob": PROOF_SHA},
        "checks": {
            "arithmetic_safe_symmetric_k_max": safe_k(127, 127),
            "first_symmetric_int32_overflow_k": safe_k(127, 127) + 1,
            "131072_symmetric_accumulation_would_overflow": False,
            "correct_rounding_step_bound_without_saturation": "scale / 2",
            "example_quantized_dot_error": round(err, 8),
            "example_unquantized_dot": round(dot(a, b), 8),
            "example_reconstructed_dot": round(roundtrip_dot(a, b, 1, 1), 8),
            "example_claimed_scalar_output_error_bound": 0.5 / 127,
            "example_valid_no_clipping_analytical_dot_bound":
                no_clipping_dot_bound(a, b, 1, 1),
            "avoided_int32_intermediate_128_square_bytes_per_direction": 65536,
            "avoided_int32_intermediate_512_square_bytes_per_direction": 1048576,
            "block_size_64_group_size_96_start_64_crosses": tile_crosses_group(64, 64, 96),
            "global_half_scale_tolerance_can_hide_other_groups": True,
        },
        "package_dispositions": {
            name: "SOURCE-INSPECTED; REFERENCE-ONLY; UNCHANGED-USE-HOLD"
            for name in PACKAGES
        },
        "acceptance": {
            "third_party_code_executed": False, "gpu_execution_observed": False,
            "cuda_compiled": False, "performance_claims_reproduced": False,
            "hardware_device_compatibility_tested": False,
            "package_specific_rights_established": False,
            "publisher_authenticated": False, "host_authority_granted": False,
            "capability_mapping_approved": False,
            "new_governed_skills_admitted": 0,
        },
        "claim_facts": {
            "nvidia_ptx_sm_61_dp4a": "https://docs.nvidia.com/cuda/parallel-thread-execution/",
            "proof_source": PROOF,
            "independent_math": "integer arithmetic and CPU-only Python stdlib regression suite",
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--receipt", type=Path)
    args, forwarded = parser.parse_known_args()
    if args.receipt:
        if not args.source_root:
            parser.error("--source-root required with --receipt")
        data = receipt(args.source_root)
        with args.receipt.open("x", encoding="utf-8") as handle:
            json.dump(data, handle, sort_keys=True, indent=2)
            handle.write("\n")
        print(json.dumps({"receipt": str(args.receipt),
                          "source_packages": len(PACKAGES),
                          "status": "CPU_REFERENCE_ONLY"}, sort_keys=True))
    else:
        unittest.main(argv=[__file__, *forwarded])

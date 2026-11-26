"""Bounded synthetic trial adapter. No model, package code, shell or I/O execution.

This exercises the trial bookkeeping and independent grading boundary, not
skill effectiveness or actual OS isolation. Only original fictional fixtures.
"""
import hashlib
import json

import trial_matrix as matrix

MODES = {"correct", "wrong", "setup-failure", "timeout", "missing-trace",
         "unauthorized-effect", "dirty-cleanup"}
MAX_INPUT = 16 * 1024
MAX_VALUES = 64


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")


def read(raw, expected, fields):
    matrix.need(type(raw) is bytes and 0 < len(raw) <= MAX_INPUT,
                "INVALID_SYNTHETIC_INPUT_BYTES")
    matrix.need(sha(raw) == expected, "SYNTHETIC_INPUT_DIGEST_MISMATCH")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=matrix._unique_object,
                           parse_constant=matrix._reject_constant)
    except (UnicodeError, RecursionError) as exc:
        raise ValueError("INVALID_SYNTHETIC_INPUT") from exc
    matrix.need(matrix.keys(value, fields), "INVALID_SYNTHETIC_INPUT_FIELDS")
    return value


def values_ok(values):
    return (type(values) is list and 0 < len(values) <= MAX_VALUES
            and all(type(v) is int and -1000 <= v <= 1000 for v in values))


def oracle_accepts(values, output):
    # Controller-owned property oracle; not the adapter's sorting algorithm.
    return (values_ok(output) and len(output) == len(set(output))
            and set(output) == set(values)
            and all(a < b for a, b in zip(output, output[1:])))


def prepare(baseline, candidate, config, runtime_bytes, fixtures, oracles):
    frozen = matrix.freeze(baseline, candidate, config)
    runtime = read(runtime_bytes, config["runtime_sha256"],
                   "schema_version adapter initial_state modes")
    matrix.need(type(runtime["schema_version"]) is int and runtime["schema_version"] == 1
                and runtime["adapter"] == "synthetic-in-memory-v1"
                and runtime["initial_state"] == "empty-v1"
                and matrix.keys(runtime["modes"], "control baseline candidate")
                and all(type(m) is str and m in MODES for m in runtime["modes"].values())
                and config["budget_unit"] == "tool-calls", "UNSUPPORTED_SYNTHETIC_RUNTIME")
    inventory = {f["case_id"]: f for f in config["fixtures"]}
    matrix.need(type(fixtures) is dict and type(oracles) is dict
                and set(fixtures) == set(oracles) == set(inventory),
                "SYNTHETIC_FIXTURE_INVENTORY_MISMATCH")
    inputs = {}
    for ident, row in inventory.items():
        fixture = read(fixtures[ident], row["fixture_sha256"], "values")
        oracle = read(oracles[ident], row["oracle_sha256"], "rule")
        matrix.need(values_ok(fixture["values"]) and oracle["rule"] == "ascending-unique-permutation-v1",
                    "UNSUPPORTED_SYNTHETIC_FIXTURE_OR_ORACLE")
        inputs[ident] = tuple(fixture["values"])
    return frozen, runtime, inputs


def emulate(values, mode, budget):
    # No shared mutable state; each run creates a fresh private in-memory record.
    # These flags deliberately simulate failures; they are not OS observations.
    observation = {"setup_ok": True, "trace": [], "output": None,
                   "simulated_steps": 0, "simulated_effects": [], "reset_ok": True,
                   "timed_out": False}
    if mode == "setup-failure":
        observation["setup_ok"] = False
        observation["trace"].append("setup-failed")
        return observation
    observation["trace"].append("setup")
    if budget < 2 or mode == "timeout":
        observation["simulated_steps"] = min(budget, 1)
        observation["timed_out"] = True
        observation["trace"].extend(("timeout", "reset"))
        return observation
    observation["simulated_steps"] = 2
    observation["output"] = list(values) if mode == "wrong" else sorted(set(values))
    observation["trace"].extend(("produce", "reset"))
    if mode == "missing-trace":
        observation["trace"] = []
    if mode == "unauthorized-effect":
        observation["simulated_effects"] = ["forbidden-write"]
    if mode == "dirty-cleanup":
        observation["reset_ok"] = False
    return observation


def grade(values, observation, budget):
    # Derive the status independently of any adapter-provided success label.
    if not observation["setup_ok"]:
        return "INVALID", "SETUP_FAILED"
    if observation["simulated_effects"]:
        return "INVALID", "AUTHORITY_VIOLATION_SIMULATED"
    if not observation["reset_ok"]:
        return "INVALID", "CLEANUP_FAILED_SIMULATED"
    if observation["simulated_steps"] > budget:
        return "INVALID", "BUDGET_EXCEEDED"
    if observation["timed_out"]:
        if observation["trace"] != ["setup", "timeout", "reset"]:
            return "INVALID", "TRACE_INCOMPLETE"
        return "TIMEOUT", "BUDGET_OR_TIMEOUT_SIMULATED"
    if observation["trace"] != ["setup", "produce", "reset"]:
        return "INVALID", "TRACE_INCOMPLETE"
    if oracle_accepts(values, observation["output"]):
        return "PASS_CLAIMED", "SYNTHETIC_ORACLE_PASS"
    return "FAIL_CLAIMED", "SYNTHETIC_ORACLE_FAIL"


def run(baseline, candidate, config, runtime_bytes, fixtures, oracles, *, execute=False):
    """Plan by default; explicit True permits only deterministic in-memory emulation."""
    matrix.need(type(execute) is bool, "INVALID_EXECUTION_SWITCH")
    frozen, runtime, inputs = prepare(baseline, candidate, config, runtime_bytes, fixtures, oracles)
    ledger = {"experiment_sha256": frozen["experiment_sha256"], "rows": []}
    receipts, payloads, reasons = {}, {}, {}
    for spec in frozen["experiment"]["runs"]:
        ident = spec["run_id"]
        if not execute:
            ledger["rows"].append({"run_id": ident, "status": "NOT_RUN", "evidence_sha256": None})
            continue
        observation = emulate(inputs[spec["case_id"]], runtime["modes"][spec["arm"]],
                              config["budget_per_trial"])
        status, reason = grade(inputs[spec["case_id"]], observation, config["budget_per_trial"])
        payload = encode({"evidence_kind": "SYNTHETIC_FAKE_ONLY", "run_id": ident,
                          "reason": reason, "observation": observation})
        receipt = encode({"schema_version": 1, "experiment_sha256": frozen["experiment_sha256"],
                          "run_id": ident, "status": status, "payload_sha256": sha(payload)})
        receipts[ident], payloads[ident] = receipt, payload
        reasons[reason] = reasons.get(reason, 0) + 1
        ledger["rows"].append({"run_id": ident, "status": status, "evidence_sha256": sha(receipt)})
    result = matrix.reconcile_receipts(baseline, candidate, config, ledger, receipts, payloads)
    return {"status": ("SYNTHETIC_EXECUTION_RECONCILED" if execute else "DESIGNED_NOT_RUN"),
            "evidence_kind": "SYNTHETIC_FAKE_ONLY", "experiment": frozen, "ledger": ledger,
            "receipts": receipts, "payloads": payloads, "reason_counts": reasons,
            "reconciliation": result, "actual_model_calls": 0, "native_host_runs": 0,
            "real_isolation_verified": False, "actual_skill_effectiveness_measured": False,
            "promotion_authorized": False}

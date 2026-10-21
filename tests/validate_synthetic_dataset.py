"""Validate fixture integrity and independently check baseline/score labels.
This does not run or validate the dashboard. Python 3.9+, standard library only.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "data/samples/public-service-risk-v1.json").read_text(encoding="utf-8"))
answers = json.loads((root / "tests/fixtures/public-service-risk-v1.expected.json").read_text(encoding="utf-8"))
def require(condition, message):
    if not condition:
        raise ValueError(message)
def index(rows, key):
    result = {row[key]: row for row in rows}
    require(len(result) == len(rows), "Duplicate " + key)
    return result
services = index(data["services"], "id")
assets = index(data["assets"], "id")
baselines = index(data["baselines"], "id")
exceptions = index(data["exceptions"], "id")
cases = index(data["cases"], "id")
expected = index(answers["expected_results"], "case_id")
require(data["synthetic"] is True, "Not marked synthetic")
require(set(cases) == set(expected), "Missing or extra expected case")
require(len(cases) == 12, "Unexpected case count")
for asset in assets.values():
    require(all(s in services for s in asset["service_ids"]), "Dangling service")
for case_id, case in cases.items():
    asset = assets[case["asset_id"]]
    baseline = baselines[case["baseline_id"]]
    answer = expected[case_id]
    snapshot = case["snapshot"]
    valid = all(type(snapshot.get(field)) is bool for field in baseline["required_fields"])
    findings = []
    if valid:
        for rule in baseline["rules"]:
            exemption = any(
                exceptions[e]["asset_id"] == asset["id"]
                and exceptions[e]["rule_id"] == rule["id"]
                and exceptions[e]["approved_value"] == snapshot[rule["field"]]
                and exceptions[e]["expires_at"] > data["simulation_clock"]
                for e in case["exception_ids"]
            )
            if snapshot[rule["field"]] != rule["expected"] and not exemption:
                findings.append(rule)
    assessment = "invalid_input" if not valid else "confirmed" if findings else "compliant"
    score = None if not valid or (findings and not asset["service_ids"]) else (
        min(100, max(r["weight"] for r in findings) +
            10 * max(services[s]["criticality"] for s in asset["service_ids"]))
        if findings else 0
    )
    require(answer["assessment"] == assessment, case_id + ": assessment mismatch")
    require(answer["finding_rule_ids"] == [r["id"] for r in findings], case_id + ": findings mismatch")
    require(answer["priority_score"] == score, case_id + ": score mismatch")
    require(answer["service_ids"] == asset["service_ids"], case_id + ": service mismatch")
    notify = bool(findings) and (
        (score is not None and score >= 60) or
        (asset["classification"] == "restricted_synthetic" and any(r["id"] == "CFG-PUBLIC" for r in findings))
    )
    require(answer["notify_human_before_action"] == notify, case_id + ": notification mismatch")
    action = answer["expected_action"]
    if action != "none":
        require(valid and bool(asset["service_ids"]), case_id + ": unsafe action expectation")
        require(case["authorization"]["sandbox_only"] is True, case_id + ": not sandbox")
        require(case["authorization"]["expires_at"] > data["simulation_clock"], case_id + ": expired")
        require(action in case["authorization"]["allowed_actions"], case_id + ": unauthorized")
        require(action in data["policy"]["allowlisted_simulated_actions"], case_id + ": not allowlisted")
    require(answer["expected_action_attempts"] <= case["simulation"]["max_attempts"], case_id + ": retry overflow")
print("PASS: 12 fixture cases; references, strict input types, baseline labels, scores, notification rules, and action authorization expectations are consistent.")
print("Dashboard integration and end-to-end behavior have NOT been tested.")

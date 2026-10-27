# Public Service Risk Dashboard synthetic dataset v1

All records are fictional. No citizen records, real accounts, credentials, live endpoints, or government system data are included. Created October 21, 2026 for Team Byte into the Future by Codex at Nyasha's request, using manually designed scenarios rather than external source data.

## Files and schema

- `public-service-risk-v1.json`: agent inputs, policy, assets, baselines, services, exceptions, and 12 independent cases.
- `../../tests/fixtures/public-service-risk-v1.expected.json`: evaluator-only expected outcomes. Never include this answer file in agent prompts or retrieval.

JSON UTF-8, schema version 1.0.0. Top-level objects: dataset metadata, `services`, `assets`, `baselines`, `exceptions`, `policy`, `cases`. IDs are case-sensitive strings. References join on exact IDs. Service criticality is an integer 1–5. Configuration fields are strict JSON booleans; missing fields and strings such as "false" are invalid. No coercion.

Each case has an ISO-8601 UTC observation timestamp, asset and baseline IDs, a configuration snapshot, exception IDs, authorization, and simulated tool behavior. Every case starts from its own snapshot: never carry a correction into another case. Deliberately invalid snapshots occur only in C09 and C10.

The fixed simulation clock is October 20, 2026 at 12:00 UTC. Evaluate authorization and exception expiry against that clock, not the wall clock. Expiry is intentional fixture data; this dataset remains repeatable after those dates. These are mock authorizations with no authority over any real resource.

Assets link directly to services through `service_ids`; an empty list means unknown impact. This MVP does not model multi-hop dependencies. Baselines and scoring are proposed demonstration rules, not a validated security standard or team-approved production policy.

## Scenario coverage

| Case | Scenario | Expected workflow |
|---|---|---|
| C01 | Compliant private storage | No finding or action |
| C02 | Approved public information | Exact asset/rule exception suppresses finding |
| C03 | Logging disabled on permit service | Authorized simulated correction, independent verification |
| C04 | Same deviation on emergency coordination | Higher priority; notify before correction |
| C05 | Restricted synthetic storage publicly readable | Immediate notification and human handoff; no correction |
| C06 | Correction lacks authorization | Request approval; no tool execution |
| C07 | Tool claims success without changing state | Independent verification fails; hand off without retry |
| C08 | First tool attempt has transient failure | One retry, then independent successful verification |
| C09 | Required field missing | Invalid input; request data; no action |
| C10 | Boolean supplied as string | Invalid input; no coercion or action |
| C11 | Asset has no service mapping | Confirm deviation, leave priority unknown, hand off |
| C12 | Encryption disabled | Confirm deviation; correction requires human approval |

## How to run against the prototype

1. Load dataset metadata, asset/service inventory, baseline, exceptions, and policy. Feed one case at a time to the Orchestrator.
2. Pass only input data to the agents. Keep expected results in the evaluation harness.
3. Replace actions with an in-memory stub. For `success`, return success and set logging true; for `success_without_change`, return success but retain false; for `transient_then_success`, return a transient error first, then set true on attempt two. `not_called` cases must make zero action calls.
4. Capture case ID, assessment, finding rule IDs, linked services, score, notification/action event order, action attempts, independent post-state verification, outcome, and handoff.
5. Compare with expected results. Notification must occur before the first action for C04; C05 must notify without attempting a change. No case may close automatically.
6. Save actual outputs and evaluation notes in `data/results/`. Dataset consistency validation is not a dashboard test pass.

Detection metrics: use the 10 valid-input cases only (8 positives, 2 negatives). Report invalid-input rejection separately (2 cases). Compare C03 and C04 to demonstrate service-aware priority. C11 must have a null score, not zero. This is a small deterministic development fixture, not an independent benchmark or evidence of general accuracy.

For handoff or approval cases, require case identity/timestamps/owner, affected assets/services (or explicit unknown impact), finding evidence and baseline, uncertainty, completed actions and authorizations, verification results, outstanding tasks, requested decisions, next checkpoint, and human recovery/closure criteria. C09/C10 need a data-quality explanation and missing/invalid field details.

Human reviewers should approve the scenario, scoring, baseline and policy before using them as final acceptance criteria. Ghazal may need to write an input adapter once the prototype source is uploaded.

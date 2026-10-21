# Testing and Validation

Run tests in this order, starting with one synthetic record before adding more.

| # | Test | What to check | Pass when |
|---|---|---|---|
| 1 | Agent communication | Orchestrator routes a case to each agent and receives a response | Every agent responds; case state updates |
| 2 | Data processing | A seeded misconfiguration is compared against its baseline | Finding is flagged with evidence and baseline reference |
| 3 | Prioritization | Affected public service is identified and ranked | Dashboard shows rationale for the priority |
| 4 | Error handling | Missing data, bad input, or a tool failure | Error is logged; agent retries within limits, then escalates |
| 5 | Escalation | A critical scenario (e.g., public storage exposure) | Human notification triggers immediately |
| 6 | Handoff | Unresolved case | All handoff fields are filled and actionable |
| 7 | Dashboard output | End-to-end run | Severity, service impact, AI work, remaining tasks, and status all display |

## Recording results
Save each run's output in `data/results/` and note it here:

| Date | Test # | Dataset | Result | Notes |
|---|---|---|---|---|
| | | | | |

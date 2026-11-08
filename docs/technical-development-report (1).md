# Public Service Risk Dashboard — Technical Development Report

## Project overview

This project is a synthetic cybersecurity risk dashboard for identifying configuration problems that could affect public services.

My contributions included:

- Connecting the application to the team’s 12-case synthetic dataset.
- Preparing the project for reproducible Ubuntu testing.
- Correcting security-exception validation.
- Correcting the display of unknown risk severity.
- Adding regression and synchronization tests.
- Packaging the risk-analysis pipeline and dataset as a watsonx Orchestrate tool.
- Importing and validating the risk-analysis agent in watsonx Orchestrate.

The local Streamlit dashboard and Python pipeline have been tested successfully. The watsonx Orchestrate agent also analyzed all 12 synthetic cases and returned the expected results.

Streamlit deployment to IBM Cloud is planned as a later phase.

## 1. System architecture

The project has four main parts:

1. The synthetic dataset in `data/samples/public-service-risk-v1.json`.
2. The Python pipeline in `src/source-code/src/pipeline.py`.
3. The command-line entry point in `src/source-code/src/main.py`.
4. The Streamlit dashboard in `src/source-code/src/dashboard.py`.

The dataset provides the simulated services, assets, approved baselines, exceptions, policy rules, authorizations, and test cases. The pipeline processes each case independently and sends the result to the command-line output or dashboard.

The system does not connect to real government systems, storage accounts, citizen records, or production infrastructure. Any correction is performed only on an in-memory copy of the synthetic case state.

## 2. Agent functionality

The project includes five agent-role YAML files:

| Agent | Function |
|---|---|
| Configuration Agent | Compares the observed configuration with the approved baseline. |
| Impact Agent | Connects an asset to its public service and identifies unknown impact. |
| Prioritization Agent | Calculates the synthetic priority score. |
| Policy Gate | Checks exceptions, authorization, expiration, and permitted actions. |
| Handoff Agent | Prepares the human-review information and outstanding decisions. |

The original YAML files define five logical roles: configuration analysis, impact analysis, prioritization, policy enforcement, and human handoff.

For IBM watsonx Orchestrate integration, these functions are currently executed through one packaged risk-analysis tool and one native Orchestrate agent. This design preserves the existing deterministic Python logic while allowing watsonx Orchestrate to call the workflow through an agent interface.

The packaged tool is located in:

- `tools/risk_tool_pkg/analyze_risk_cases.py`
- `tools/risk_tool_pkg/pipeline.py`
- `tools/risk_tool_pkg/data/public-service-risk-v1.json`

The native agent definition is:

- `agents/risk_analysis_agent.yaml`

The agent calls the tool, receives structured case results, and presents the findings and human-intervention requirements to the user.

## 3. Code implementation

The application uses:

- Python 3.10 or newer
- Streamlit for the dashboard
- PyYAML for the YAML agent definitions
- pytest for automated testing
- JSON for the dataset and expected test fixtures
- IBM watsonx Orchestrate ADK 2.19.1 for tool and agent import
- Python `@tool` integration for the packaged risk-analysis tool
- PowerShell scripts for repeatable tool and agent import
- SHA-256 and byte-level synchronization checks for packaged files

Important files include:

- `src/source-code/src/pipeline.py` — main analysis and safety logic
- `src/source-code/src/main.py` — command-line runner
- `src/source-code/src/dashboard.py` — Streamlit interface
- `src/source-code/agents/` — agent-role YAML files
- `src/source-code/tests/test_pipeline.py` — automated tests
- `tests/validate_synthetic_dataset.py` — dataset consistency check
- `tools/risk_tool_pkg/analyze_risk_cases.py` — watsonx Orchestrate tool entry point
- `tools/risk_tool_pkg/pipeline.py` — synchronized copy of the tested pipeline
- `tools/risk_tool_pkg/data/public-service-risk-v1.json` — synchronized dataset copy
- `agents/risk_analysis_agent.yaml` — native watsonx Orchestrate agent
- `tests/test_sync.py` — verifies that packaged files match the originals
- `tests/test_wxo_tool.py` — offline tests for the Orchestrate tool wrapper
- `scripts/import-all.ps1` — synchronizes and imports the tool and agent

No external API is required for the current local workflow.

## 4. Dataset integration

The pipeline reads `data/samples/public-service-risk-v1.json` and processes every case with a fresh state. A correction made in one case cannot affect another case.

Before analyzing a case, the pipeline checks that required fields exist and that Boolean values are actual JSON Booleans. It does not convert invalid strings such as `"false"` into Boolean values.

The pipeline also checks that an exception has the correct ID, asset, rule, expiration, and `approved_value`. An exception is only allowed to suppress a finding when the observed configuration matches the approved value.

When an asset has no known public-service mapping, the system does not invent a service or treat the risk as zero. It reports the priority as unknown, prevents automatic action, and requires human handoff.

## 5. Testing and debugging

The original 12-case dataset validator passed:

```text
PASS: 12 fixture cases; references, strict input types, baseline labels,
scores, notification rules, and action authorization expectations are consistent.
```

The original local Python pipeline tests passed:

```text
8 passed
```

The watsonx Orchestrate packaging and tool tests also passed:

```text
10 passed
```

The additional tests verified that:
- The packaged pipeline matches the original pipeline byte-for-byte.
- The packaged dataset matches the original dataset byte-for-byte.
- C03, C05, C07, and C11 produce the expected results.
- The tool can process individual cases and groups of cases.
- The tool returns the required structured result fields.
The imported watsonx Orchestrate agent was then tested against all 12 synthetic cases. It returned the expected case IDs, severity values, verification results, and human-intervention requirements.

### F-01: Security exception validation

The first review found that the pipeline checked an exception’s ID, asset, rule, and expiration, but did not check whether the observed value matched `approved_value`.

I corrected the pipeline so a mismatched exception cannot hide a security finding. I also added a negative regression test using a temporary modified copy of the dataset. The test confirms that an invalid C02 exception produces a finding instead of being accepted.

The legitimate C02 exception still works correctly.

### F-02: Unknown severity display

The pipeline originally treated both a score of `0` and a missing score as `none`. This was misleading for C11 because C11 has an unknown priority, not confirmed zero risk.

I changed the classification so:

- A confirmed score of `0` is displayed as `NONE`.
- A missing or null score is displayed as `UNKNOWN`.

C11 now displays `UNKNOWN`, while compliant case C01 continues to display `NONE`.



## 6. IBM watsonx Orchestrate integration and planned IBM Cloud deployment

The risk-analysis capability has been integrated with IBM watsonx Orchestrate.

The integration uses:

1. A packaged Python tool containing the tested pipeline and dataset.
2. A native watsonx Orchestrate agent that calls the tool.
3. The configured watsonx Orchestrate language model,
   `groq/openai/gpt-oss-120b`.
4. PowerShell automation for repeatable import and synchronization.

The packaged tool and native agent were imported successfully. The agent analyzed all 12 synthetic cases and returned the expected results.

Important validation cases included:

- C03: authorized correction followed by independent verification.
- C05: critical public-access risk escalated without automatic remediation.
- C07: false tool success detected when the configuration remained unchanged.
- C11: missing service dependency classified as `UNKNOWN`, with human handoff required.

The Streamlit dashboard has not yet been deployed to IBM Cloud. It remains available as a local interface. A later deployment phase will determine the appropriate IBM Cloud hosting service, configure secrets and environment variables, deploy the dashboard, and compare cloud dashboard behavior with the local version.

## 7. Current limitations

- The watsonx Orchestrate tool and agent have been imported and validated against all 12 synthetic cases.
- The Streamlit dashboard has not yet been deployed to IBM Cloud.
- Cloud-hosted dashboard behavior, networking, monitoring, and runtime configuration still require testing.
- The packaged pipeline and dataset are maintained as synchronized copies, protected by automated byte-level tests.
- The system does not automatically close cases. Human approval remains
  required before final closure or any unapproved correction.
- The current IBM integration validates the risk-analysis agent and tool,
  but not yet the Streamlit dashboard running in IBM Cloud.

## 8. Reproducibility commands

From the repository root on Ubuntu:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r src/source-code/requirements.txt
python tests/validate_synthetic_dataset.py
cd src/source-code
PYTHONPATH=. python -m pytest -q
PYTHONPATH=. python -m src.main
python -m streamlit run src/dashboard.py
```

The risk-analysis tool and agent have been integrated and validated in IBM
watsonx Orchestrate. The Streamlit dashboard has not yet been deployed to IBM
Cloud and is planned for a later phase.

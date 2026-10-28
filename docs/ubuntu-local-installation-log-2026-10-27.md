# Ubuntu Local Installation Log — October 27, 2026

**Project:** Byte into the Future — Public Service Risk Dashboard  
**Workstream:** Local VM installation and independent testing preparation  
**Tested and documented by:** Nyasha Champ (team lead; independent testing in personal Ubuntu VirtualBox VM)  
**GitHub branch containing application:** `source-code`  
**Status:** Dependencies successfully installed; dataset validation and application tests have **not yet** been executed in this VM.

## Purpose

Document the team's first local Ubuntu setup attempt, troubleshooting observations, and reproducible steps. The goal is to test the synthetic dashboard without spending IBM BOB credits. This is an **installation checkpoint**, not a claim that the application, agents, IBM integrations, or the complete 12-case workflow has passed acceptance testing.

## Environment observed

| Component | Observed status |
|---|---|
| Virtualization | Oracle VirtualBox, Ubuntu guest |
| Operating system | Ubuntu 24.04.3 LTS (shown in TTY console) |
| Python | 3.12.3 |
| Git | 2.43.0 |
| Python virtual environment | `.venv` created and activated (prompt displayed `(.venv)`) |
| Application source | ZIP of the repository's `source-code` branch downloaded and extracted in Ubuntu |
| Extracted project location | `~/Downloads/Byte-into-the-future-source-code/` |
| Dashboard requirements | `src/source-code/requirements.txt` |
| Synthetic dataset | `data/samples/public-service-risk-v1.json` |
| IBM credits | None used for the observed local setup |

These details document one VM, not a verified supported-OS matrix.

## Verified progress

- Ubuntu's package manager completed the installation of Git and Python support packages; `git --version` returned **2.43.0**.
- The existing Ubuntu VM experienced slow or unresponsive graphical login sessions. A text console (TTY3) remained accessible. The display manager reported `active`; a normal graphical login eventually succeeded. The cause of the sluggish GUI was **not established**.
- A Git HTTPS clone was attempted, but private-repository authentication blocked it; the working source was instead downloaded as a ZIP through the authenticated Ubuntu browser.
- The extracted project was opened in a terminal and both files were found by a successful `ls` command:
  - `src/source-code/requirements.txt`
  - `data/samples/public-service-risk-v1.json`
- A Python environment was created using `python3 -m venv .venv` and activated using `source .venv/bin/activate`.
- Initial pip installation timed out retrieving packages from `files.pythonhosted.org`. A subsequent attempt used a longer timeout and reused cached downloads.
- The dependency installation **completed successfully**; terminal output showed `Successfully installed` including **Streamlit 1.66.1**, **pytest 8.4.2**, and **PyYAML 6.0.3**.
- No dataset-validator output, pytest result, CLI pipeline output, or running Streamlit page has yet been recorded from this VM.

## Reproduction commands

The following commands reproduce the setup from the root of the **extracted** `source-code` branch ZIP in Ubuntu. They do not install or configure IBM-hosted services.

```bash
# From the extracted project root:
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --timeout 180 -r src/source-code/requirements.txt
```

If pip times out again, verify the network and retry; cached and already-installed packages are ordinarily reused. Do not commit `.venv/`, downloaded wheels, API keys, login passwords, or GitHub tokens.

## Outstanding verification — not yet complete

Execute these **one at a time**, recording command, result, and date:

```bash
# At the extracted repository root, after activating .venv:
python tests/validate_synthetic_dataset.py

# Enter the application directory:
cd src/source-code
PYTHONPATH=. python -m pytest -q
PYTHONPATH=. python -m src.main
python -m streamlit run src/dashboard.py
```

Expected *targets* (not observed test results yet):

1. Dataset consistency validator reports `PASS` for the 12-case fixture.
2. Application's pytest suite passes and the summary is preserved.
3. CLI pipeline processes the synthetic dataset and outputs case results.
4. Streamlit dashboard loads in the Ubuntu browser, displays its case selector, and shows evidence, severity/score, action, verification, and human handoff for selected cases.
5. Run all 12 cases against the evaluator-only expected file; record actual vs. expected results and any mismatches in `data/results/` or a test log.
6. Review authorization and unknown-service-mapping safeguards; passing the four current pytest functions alone is not full acceptance coverage.
7. Confirm IBM Bob/watsonx integration **separately**; YAML agent definitions and a deterministic local simulation do not prove IBM-hosted agent execution.

## Troubleshooting record

| Issue encountered | Action taken / observation | Current status |
|---|---|---|
| VirtualBox clipboard initially unavailable | Opened ChatGPT in the Ubuntu browser and copied commands within the VM | Workaround succeeded |
| Ubuntu desktop/lock screen slow or apparently frozen | Used text console, checked available memory and display-manager state; eventually logged in graphically | Desktop accessible at last observation; cause unconfirmed |
| Git not installed | Installed Git and Python supporting packages with apt | Resolved |
| Private repository clone asked for authentication | Downloaded the correct `source-code` branch as an authenticated ZIP | Resolved for this setup; not a configured Git clone |
| pip read timeout on PyPI | Retried with `--timeout 180`; cached files reused | Resolved; dependencies installed |
| Accidental duplicate pip command | Command returned an option error; corrected and reran | Resolved, no repository change |

## Next checkpoint

Capture screenshots or copied text of the dataset validator, application pytest summary, CLI execution, and dashboard launch. **Do not mark those steps as complete until run.** Keep personal credentials, terminal password prompts, tokens, and any private data out of the shared testing evidence.

*This entry records local setup work. It does not change the application source, claim end-to-end validation, or represent approval to merge code into `main`.*


## October 28, 2026 — Dataset inspection and JSON syntax checkpoint

**Evidence source:** Screenshots of terminal output from the Ubuntu 24.04 VirtualBox VM. These are observed results, not inferred application behavior.

- Restarted the Ubuntu VM, opened the extracted project directory at `~/Downloads/Byte-into-the-future-source-code/`, and successfully reactivated the existing `.venv` environment (terminal prompt showed `(.venv)`). No packages were reinstalled.
- `ls -la` confirmed the project folders `data/`, `docs/`, `src/`, `tests/`, and `.venv/`.
- `ls -lah data/` confirmed `README.md` and `samples/`.
- `ls -lah data/samples/` confirmed `public-service-risk-v1.json` (approximately 12 KB) and a sample `README.md`.
- Executed the read-only syntax check:

  ```bash
  python -m json.tool data/samples/public-service-risk-v1.json > /dev/null && echo "JSON validation PASSED"
  ```

  **Observed terminal result:** `JSON validation PASSED`.

**Interpretation:** The dataset file exists and is syntactically valid JSON. This check **does not** establish that it contains 12 cases, that required fields and values are correct, or that the application processes the dataset successfully.

**Next pending action (Step 1E):** Inspect JSON top-level structure, then confirm the case count and dataset-specific constraints. The repository's `python tests/validate_synthetic_dataset.py` validator and application tests have **not yet** been run in this VM. Streamlit and cybersecurity scenario testing also remain pending.

**Scope:** Documentation-only update; no application source, dataset, or dependencies changed.


### October 28, 2026 — JSON structure and case-count verification

**Evidence:** Ubuntu Terminal screenshots from local VirtualBox testing, with active `(.venv)` prompt.

- Loaded `data/samples/public-service-risk-v1.json` using Python's `json.load`.
- **Observed root type:** `dict`.
- **Observed top-level keys:** `dataset_id`, `schema_version`, `synthetic`, `created_date`, `simulation_clock`, `provenance`, `services`, `assets`, `baselines`, `exceptions`, `policy`, `cases`.
- Inspected `d['cases']`: **12 cases found**, collection type **list**; comparison with expected count printed **`12-case count: PASS`**.

**Limits:** Count and basic JSON structure are confirmed, but individual required fields, values, cross-references, and scenario expectations are not yet validated. The repository's dedicated dataset validator has not yet been executed in this VM.

**Next command (pending):** `python tests/validate_synthetic_dataset.py` from the extracted project root with `.venv` active. Record actual output before claiming validator PASS.


### October 28, 2026 — Dedicated synthetic dataset validator: PASS

**Command executed in active Ubuntu VM environment, from project root:**

```bash
python tests/validate_synthetic_dataset.py
```

**Observed terminal output (verbatim):**

```text
PASS: 12 fixture cases; references, strict input types, baseline labels, scores,
notification rules, and action authorization expectations are consistent.
Dashboard integration and end-to-end behavior have NOT been tested.
```

**Assessment:** Step 1 dataset validation completed successfully in the Ubuntu VM. This verifies the constraints checked by the existing validator, not independent functionality of the app, Streamlit UI, agent orchestration, or IBM Cloud integrations. Next step: run the application's pytest suite and record its actual results.


## Testing attribution clarification — October 28, 2026

**Tester:** Nyasha Champ only. The Ubuntu installation verification, dataset inspection, JSON syntax check, 12-case count, and synthetic dataset validator execution documented above were performed independently by Nyasha Champ. Ghazal was unavailable to participate in this testing session. This attribution concerns testing only and does not change authorship or credit for Ghazal's application and dashboard development.

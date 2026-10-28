# Ubuntu VM testing screenshot evidence — October 27–28, 2026

**Tester:** Nyasha Champ (independent testing).  
**Status:** Image files prepared and named; **awaiting upload to this folder**. The links below will work after upload.  
**Source:** Terminal and Firefox screenshots supplied during testing. No application code or dataset modified.

| # | Evidence file |
|---|---|
| 1 | `01-vm-restart-venv-activated.png` |
| 2 | `02-project-directory-verified.png` |
| 3 | `03-data-directory-inspected.png` |
| 4 | `04-synthetic-json-file-located.png` |
| 5 | `05-json-syntax-pass.png` |
| 6 | `06-json-top-level-structure.png` |
| 7 | `07-twelve-case-count-pass.png` |
| 8 | `08-synthetic-dataset-validator-pass.png` |
| 9 | `09-pytest-four-passed.png` |
| 10 | `10-cli-pipeline-human-approval.png` |
| 11 | `11-streamlit-first-launch.png` |
| 12 | `12-streamlit-server-started.png` |
| 13 | `13-dashboard-first-render-c01.png` |
| 14 | `14-next-session-venv-reactivated.png` |
| 15 | `15-streamlit-restart.png` |
| 16 | `16-c01-baseline-and-handoff.png` |
| 17 | `17-c01-summary-and-baseline.png` |
| 18 | `18-c01-json-assessment-evidence.png` |
| 19 | `19-c01-json-human-intervention.png` |
| 20 | `20-c01-json-lifecycle.png` |

## Verified outcomes and limitations

- JSON parsed successfully; 12-case fixture count PASS; dedicated dataset validator PASS.
- Automated pytest suite: **4 passed in 0.06s**.
- CLI produced JSON, Streamlit started on port 8501, and C01 dashboard UI rendered.
- C01 was classified compliant, score 0, severity none, no action; final human review still required.
- C01 screenshot findings remain provisional until the original observed asset values are cross-checked. No claim of end-to-end IBM-hosted agent integration or acceptance of all 12 cases.

**Upload guidance:** Extract the evidence ZIP and upload the 20 PNG files from its `docs/testing-evidence/` directory here. Keep these exact filenames and avoid duplicate uploads. Do not upload credentials or personal information.

# Ubuntu VM testing screenshot evidence — October 27–28, 2026

**Tester:** Nyasha Champ (independent testing).  
**Status:** All 35 PNGs listed below were verified present on the `source-code` branch in this folder. These images document setup and C01–C05; C06–C12 image uploads remain outstanding.  
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
- C01–C12 passed their local synthetic scenario checks as documented in the [consolidated test report](../cybersecurity-functional-test-report-2026-10-29.md). Screenshots here cover C01–C05 and installation; later scenario screenshots still require uploading. No claim of end-to-end IBM-hosted agent integration.

**Evidence handling:** Preserve the existing 35 PNG filenames. Do not upload them again; add new C06–C12 images with distinct filenames after inspecting screenshots for credentials or private data.

## Additional screenshots — C01 through C05

| # | Evidence file |
|---|---|
| 21 | `21-c01-original-fixture.png` |
| 22 | `22-c02-dashboard.png` |
| 23 | `23-c02-original-fixture.png` |
| 24 | `24-c02-approved-exception.png` |
| 25 | `25-c03-dashboard-summary.png` |
| 26 | `26-c03-execution-events.png` |
| 27 | `27-c03-human-intervention.png` |
| 28 | `28-c03-authorization-fixture.png` |
| 29 | `29-c04-dashboard.png` |
| 30 | `30-c04-execution-events.png` |
| 31 | `31-c04-authorization-fixture.png` |
| 32 | `32-c05-dashboard.png` |
| 33 | `33-c05-handoff-and-baseline.png` |
| 34 | `34-c05-execution-events.png` |
| 35 | `35-c05-authorization-fixture.png` |

**Transfer status:** The 35 listed screenshots are committed in this folder. C06–C12 screenshots are not yet indexed or verified in GitHub. See the consolidated testing report and chronological log for newer written results.

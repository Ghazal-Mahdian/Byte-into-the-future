# Data

## Rules
- **Synthetic or properly authorized public data only.** No real citizen data, personal information, credentials, or live government system data.
- **Keep files small.** Only sample datasets (under about 5 MB each) belong in `samples/`. Store larger files outside the repo and link to them here.
- **Document every dataset** in the table below.

## Folders
| Folder | Contents |
|---|---|
| `samples/` | Small synthetic datasets: alerts, configuration snapshots, baselines, asset inventory, service dependencies |
| `results/` | Outputs from test runs |

## Dataset log
| File | Description | Source / how generated | Added by | Date |
|---|---|---|---|---|
| [public-service-risk-v1.json](samples/public-service-risk-v1.json) | 12 fictional storage cases, 5 assets, 3 services, baseline and mock authorizations | Manually constructed fictional fixtures; no external data | Codex for Nyasha | 2026-10-21 |

See the [dataset guide](samples/README.md) for schema, provenance, scenario coverage, policy assumptions, and prototype integration instructions. Evaluator-only expected results are in `tests/fixtures/`. Run `python tests/validate_synthetic_dataset.py` from the repository root to check fixture consistency. This does not test the dashboard.

# Ubuntu testing instructions

Run these commands from the repository root (the directory containing `README.md`, `data/`, `src/`, and `tests/`).

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r src/ghazal-project/requirements.txt
```

Validate the dataset and run the application tests:

```bash
python tests/validate_synthetic_dataset.py
python -m pytest src/ghazal-project/tests -q
```

Run the command-line workflow:

```bash
cd src/ghazal-project
PYTHONPATH=. python -m src.main
```

Start the Streamlit dashboard in a second terminal:

```bash
cd src/ghazal-project
source ../../.venv/bin/activate
python -m streamlit run src/dashboard.py
```

The dashboard reads `data/samples/public-service-risk-v1.json` and keeps all simulated actions in memory. It never connects to a real service. Test C03 first, then C05 and C07. The expected-results fixture is evaluator-only and is not loaded by the application.

# ── Base image ────────────────────────────────────────────────────────────────
# Python 3.12 slim keeps the image small; 3.12 is LTS and matches the venv used
# in development. The pipeline uses only stdlib so no extra system libs are needed.
FROM python:3.12-slim

# ── Metadata ──────────────────────────────────────────────────────────────────
LABEL org.opencontainers.image.title="Public Service Risk Dashboard"
LABEL org.opencontainers.image.description="Synthetic 12-case risk-analysis dashboard (Streamlit)"
LABEL org.opencontainers.image.source="https://github.com/your-org/byte-into-the-future"

# ── Working directory ─────────────────────────────────────────────────────────
WORKDIR /app

# ── Install Python dependencies first (cached layer) ─────────────────────────
# requirements-deploy.txt lives at the repo root (created alongside this Dockerfile)
COPY requirements-deploy.txt ./
RUN pip install --no-cache-dir -r requirements-deploy.txt

# ── Copy only the files the dashboard needs ───────────────────────────────────
# Pipeline + dashboard source
COPY src/source-code/src/pipeline.py     ./src/source-code/src/
COPY src/source-code/src/dashboard.py    ./src/source-code/src/
COPY src/source-code/src/__init__.py     ./src/source-code/src/

# Dataset (bundled — no external API needed)
COPY data/samples/public-service-risk-v1.json ./data/samples/

# ── Expose a default port for local runs ──────────────────────────────────────
# Code Engine injects $PORT at runtime; Streamlit reads it via the CMD below.
EXPOSE 8080

# ── Health check ──────────────────────────────────────────────────────────────
# Code Engine health probe: HTTP GET /_stcore/health (Streamlit built-in endpoint)
HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT:-8080}/_stcore/health')"

# ── Start command ─────────────────────────────────────────────────────────────
# Uses the PORT env var injected by Code Engine (defaults to 8080 for local runs).
# --server.headless suppresses the browser-open prompt in a container.
# --server.enableCORS=false and --server.enableXsrfProtection=false are safe
# behind Code Engine's TLS-terminating proxy.
CMD streamlit run src/source-code/src/dashboard.py \
    --server.address 0.0.0.0 \
    --server.port ${PORT:-8080} \
    --server.headless true \
    --server.enableCORS false \
    --server.enableXsrfProtection false

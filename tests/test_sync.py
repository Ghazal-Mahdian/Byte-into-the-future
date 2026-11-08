"""Sync guard: asserts that the tool package copies are byte-for-byte identical
to their originals. Run this test any time either file is changed.

    python -m pytest tests/test_sync.py -v
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_PIPELINE_ORIGINAL = ROOT / "src" / "source-code" / "src" / "pipeline.py"
_PIPELINE_COPY     = ROOT / "tools" / "risk_tool_pkg" / "pipeline.py"

_DATASET_ORIGINAL  = ROOT / "data" / "samples" / "public-service-risk-v1.json"
_DATASET_COPY      = ROOT / "tools" / "risk_tool_pkg" / "data" / "public-service-risk-v1.json"


def test_pipeline_copy_is_in_sync():
    """tools/risk_tool_pkg/pipeline.py must be identical to src/source-code/src/pipeline.py."""
    assert _PIPELINE_ORIGINAL.exists(), f"Original not found: {_PIPELINE_ORIGINAL}"
    assert _PIPELINE_COPY.exists(),     f"Copy not found: {_PIPELINE_COPY}"
    assert _PIPELINE_ORIGINAL.read_bytes() == _PIPELINE_COPY.read_bytes(), (
        "tools/risk_tool_pkg/pipeline.py is out of sync with "
        "src/source-code/src/pipeline.py — re-copy it before importing the tool."
    )


def test_dataset_copy_is_in_sync():
    """tools/risk_tool_pkg/data/public-service-risk-v1.json must be identical to the original."""
    assert _DATASET_ORIGINAL.exists(), f"Original not found: {_DATASET_ORIGINAL}"
    assert _DATASET_COPY.exists(),     f"Copy not found: {_DATASET_COPY}"
    assert _DATASET_ORIGINAL.read_bytes() == _DATASET_COPY.read_bytes(), (
        "tools/risk_tool_pkg/data/public-service-risk-v1.json is out of sync with "
        "data/samples/public-service-risk-v1.json — re-copy it before importing the tool."
    )

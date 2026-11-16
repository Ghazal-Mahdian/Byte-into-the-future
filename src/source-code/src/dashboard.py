"""Streamlit view for the synthetic 12-case testing workflow."""

from pathlib import Path
import json
import streamlit as st

try:
    from .pipeline import analyze
except ImportError:
    from pipeline import analyze


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
DATASET = REPOSITORY_ROOT / "data" / "samples" / "public-service-risk-v1.json"

# ── Severity colour map ────────────────────────────────────────────────────
_SEVERITY_COLOUR = {
    "critical": "#FF4B6E",
    "high":     "#FF8C42",
    "medium":   "#F7C948",
    "low":      "#3A86FF",
    "none":     "#52D45F",
    "unknown":  "#9B8FC7",
}

_OUTCOME_BADGE = {
    "no_action":                      ("#52D45F",  "✓ No action required"),
    "verified_awaiting_human_closure": ("#3A86FF",  "✓ Verified — awaiting closure"),
    "awaiting_approval":               ("#F7C948",  "⏳ Awaiting human approval"),
    "awaiting_approval":               ("#F7C948",  "⏳ Awaiting human approval"),
    "handoff":                         ("#FF4B6E",  "🚨 Human handoff required"),
    "request_data":                    ("#9B8FC7",  "⚠ Invalid input — data needed"),
}


def _badge(text: str, colour: str) -> str:
    return (
        f'<span style="background:{colour};color:#0D0D0D;padding:2px 10px;'
        f'border-radius:12px;font-size:0.78rem;font-weight:600;">{text}</span>'
    )


def _severity_badge(severity: str) -> str:
    colour = _SEVERITY_COLOUR.get(severity, "#9B8FC7")
    return _badge(severity.upper(), colour)


def _outcome_badge(outcome: str) -> str:
    colour, label = _OUTCOME_BADGE.get(outcome, ("#9B8FC7", outcome))
    return _badge(label, colour)


st.set_page_config(
    page_title="Public Service Risk Dashboard",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
/* ── Base ── */
.stApp { background:#0A0A12; color:#E8E8F0; font-family:'Segoe UI',system-ui,sans-serif; }
/* ── Header ── */
h1 { color:#C084FC; letter-spacing:-0.5px; }
h2, h3 { color:#C084FC; }
h4 { color:#94A3D4; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.06em; }
/* ── Metric cards ── */
[data-testid="stMetric"] {
    background:#13132A; border:1px solid #2A2A4A;
    border-radius:10px; padding:14px 18px;
}
[data-testid="stMetricLabel"] { color:#8080AA !important; font-size:0.75rem !important; text-transform:uppercase; letter-spacing:0.05em; }
[data-testid="stMetricValue"] { color:#C084FC !important; font-size:1.5rem !important; font-weight:700 !important; }
/* ── Selectbox ── */
[data-testid="stSelectbox"] label { color:#8080AA; font-size:0.8rem; text-transform:uppercase; }
/* ── Dividers ── */
hr { border-color:#2A2A4A; }
/* ── Expanders ── */
details summary { color:#94A3D4 !important; }
/* ── Dataframe ── */
[data-testid="stDataFrame"] { border:1px solid #2A2A4A; border-radius:8px; }
/* ── Download button ── */
div.stDownloadButton > button {
    background:#13132A; color:#C084FC;
    border:1px solid #C084FC; border-radius:8px;
    font-weight:600;
}
div.stDownloadButton > button:hover { background:#C084FC; color:#0A0A12; }
/* ── Caption / footer ── */
.caption-bar {
    color:#55557A; font-size:0.72rem; padding:4px 0 12px;
    border-bottom:1px solid #1E1E38; margin-bottom:16px;
}
/* ── Evidence bullets ── */
.ev-item {
    background:#13132A; border-left:3px solid #FF4B6E;
    padding:6px 12px; border-radius:0 6px 6px 0;
    margin:4px 0; font-size:0.85rem; color:#E8E8F0;
}
.bl-item {
    background:#0F0F22; border-left:3px solid #3A86FF;
    padding:6px 12px; border-radius:0 6px 6px 0;
    margin:4px 0; font-size:0.85rem; color:#94A3D4;
}
.hw-item {
    background:#1A0D20; border-left:3px solid #C084FC;
    padding:6px 12px; border-radius:0 6px 6px 0;
    margin:4px 0; font-size:0.85rem; color:#E8E8F0;
}
</style>
""", unsafe_allow_html=True)


def main() -> None:
    # ── Header ────────────────────────────────────────────────────────────
    st.markdown("# 🔒 Public Service Risk Dashboard")
    st.markdown(
        '<div class="caption-bar">'
        "Synthetic test mode &nbsp;•&nbsp; in-memory actions only &nbsp;•&nbsp; "
        "human closure remains required for every case"
        "</div>",
        unsafe_allow_html=True,
    )

    # ── Load all results once ──────────────────────────────────────────────
    results = analyze(DATASET)
    result_map = {item.case_id: item for item in results}

    # ── Overview row ──────────────────────────────────────────────────────
    total      = len(results)
    critical   = sum(1 for r in results if r.severity == "critical")
    handoffs   = sum(1 for r in results if r.handoff_required)
    verified   = sum(1 for r in results if r.verification_result == "passed")
    invalid    = sum(1 for r in results if r.assessment == "invalid_input")

    ov1, ov2, ov3, ov4, ov5 = st.columns(5)
    ov1.metric("Total cases",   total)
    ov2.metric("Critical",      critical,  delta=None)
    ov3.metric("Handoffs",      handoffs,  delta=None)
    ov4.metric("Verified fixes", verified, delta=None)
    ov5.metric("Invalid input", invalid,   delta=None)

    st.divider()

    # ── Case selector ─────────────────────────────────────────────────────
    case_labels = [
        f"{r.case_id} — {r.title}  [{r.severity.upper()}]" for r in results
    ]
    label_to_id = {lbl: r.case_id for lbl, r in zip(case_labels, results)}
    chosen_label = st.selectbox("Select a case to inspect", case_labels)
    selected = result_map[label_to_id[chosen_label]]

    # ── Case metrics ──────────────────────────────────────────────────────
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Assessment",     selected.assessment.replace("_", " ").title())
    m2.metric("Priority score", "Unknown" if selected.score is None else selected.score)
    m3.metric("Severity",       selected.severity.upper())
    m4.metric("Verification",   selected.verification_result.replace("_", " ").title())

    # ── Case header ───────────────────────────────────────────────────────
    sev_html     = _severity_badge(selected.severity)
    outcome_html = _outcome_badge(selected.outcome)
    st.markdown(
        f"### {selected.case_id}: {selected.title} &nbsp; {sev_html} &nbsp; {outcome_html}",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"**Asset:** `{selected.asset_id}` ({selected.asset_name}) &nbsp;|&nbsp; "
        f"**Service:** {selected.affected_public_service} &nbsp;|&nbsp; "
        f"**Finding:** {selected.finding}"
    )
    st.markdown(f"**Lifecycle:** `{selected.lifecycle_status}`")

    st.divider()

    # ── Evidence + intervention ───────────────────────────────────────────
    left, right = st.columns(2)

    with left:
        st.markdown("#### 🔍 Evidence & baseline")
        if selected.evidence:
            for item in selected.evidence:
                st.markdown(f'<div class="ev-item">⚠ {item}</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="bl-item">No baseline deviation detected.</div>',
                unsafe_allow_html=True,
            )
        st.markdown("<br>**Required baseline fields:**", unsafe_allow_html=True)
        for item in selected.baseline_evidence:
            st.markdown(f'<div class="bl-item">{item}</div>', unsafe_allow_html=True)

    with right:
        st.markdown("#### 🤖 Action & human intervention")
        col_a, col_b = st.columns(2)
        col_a.metric("Action taken",   selected.action_taken)
        col_b.metric("Attempts",       selected.action_attempts)
        col_a.metric("Tool result",    selected.action_result.replace("_", " ").title())
        col_b.metric("Handoff",        "Yes" if selected.handoff_required else "No")

        st.markdown("<br>**Human intervention required:**", unsafe_allow_html=True)
        for item in selected.human_intervention:
            st.markdown(f'<div class="hw-item">👤 {item}</div>', unsafe_allow_html=True)

    st.divider()

    # ── Execution events ──────────────────────────────────────────────────
    st.markdown("#### 📋 Ordered execution events")
    if selected.events:
        st.dataframe(selected.events, use_container_width=True, hide_index=True)
    else:
        st.caption("No execution events recorded for this case.")

    # ── Expanders ─────────────────────────────────────────────────────────
    with st.expander("✅ Completed AI work"):
        for item in selected.completed_ai_work:
            st.markdown(f"- {item}")

    with st.expander("📄 Full result JSON"):
        st.json(selected.to_dict())

    # ── Download ──────────────────────────────────────────────────────────
    st.download_button(
        label="⬇ Download selected result as JSON",
        data=json.dumps(selected.to_dict(), indent=2),
        file_name=f"{selected.case_id}.json",
        mime="application/json",
        use_container_width=True,
    )


if __name__ == "__main__":
    main()

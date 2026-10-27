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

st.set_page_config(page_title="Public Service Risk Dashboard", layout="wide")
st.markdown("""<style>
.stApp { background:#050505; color:#F7F7F7; }
[data-testid="stMetricValue"] { color:#3A86FF; }
div.stButton > button { border-color:#3A86FF; }
</style>""", unsafe_allow_html=True)


def main() -> None:
    st.title("Public Service Risk Dashboard")
    st.caption("Synthetic test mode • in-memory actions only • human closure remains required")
    results = analyze(DATASET)
    selected_id = st.selectbox("Case", [item.case_id for item in results])
    selected = next(item for item in results if item.case_id == selected_id)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Assessment", selected.assessment.replace("_", " ").title())
    c2.metric("Priority score", "Unknown" if selected.score is None else selected.score)
    c3.metric("Severity", selected.severity.upper())
    c4.metric("Verification", selected.verification_result.replace("_", " ").title())

    st.subheader(f"{selected.case_id}: {selected.title}")
    st.write(f"**Asset:** `{selected.asset_id}` ({selected.asset_name})")
    st.write(f"**Affected public service:** {selected.affected_public_service}")
    st.write(f"**Finding:** {selected.finding}")

    left, right = st.columns(2)
    with left:
        st.markdown("#### Evidence and baseline")
        st.write("**Observed finding evidence**")
        for item in selected.evidence:
            st.write(f"- {item}")
        st.write("**Baseline**")
        for item in selected.baseline_evidence:
            st.write(f"- {item}")
    with right:
        st.markdown("#### Action and human intervention")
        st.write(f"**Action:** `{selected.action_taken}`")
        st.write(f"**Attempts:** {selected.action_attempts}")
        st.write(f"**Tool result:** {selected.action_result}")
        st.write(f"**Workflow outcome:** `{selected.outcome}`")
        st.write(f"**Handoff required:** {'Yes' if selected.handoff_required else 'No'}")
        for item in selected.human_intervention:
            st.write(f"- {item}")

    st.markdown("#### Ordered execution events")
    st.dataframe(selected.events, width="stretch", hide_index=True)
    with st.expander("Completed AI work"):
        st.write(selected.completed_ai_work)
    with st.expander("Full result JSON"):
        st.json(selected.to_dict())
    st.download_button("Download selected result", json.dumps(selected.to_dict(), indent=2), file_name=f"{selected.case_id}.json", mime="application/json", width="stretch")


if __name__ == "__main__":
    main()

import streamlit as st

st.set_page_config(
    page_title="MedEvidence-AI V5",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 MedEvidence-AI V5")
st.subheader("Evidence-backed Clinical Synthesis")

st.markdown(
    """
    **Workflow :**

    AI response → Claims → Evidence → Verification → Correction → Final synthesis
    """
)

st.divider()

st.header("1. Clinical claim")

claim = st.text_area(
    "Enter the clinical claim to verify:",
    placeholder="Example: PSA is prostate-specific but not cancer-specific."
)

st.header("2. Evidence")

evidence = st.text_area(
    "Paste the relevant passage from the medical source:",
    placeholder="Paste the exact relevant passage here."
)

st.header("3. Source")

source = st.text_input(
    "Source name:",
    value="EAU Guidelines on Prostate Cancer — Diagnostic Evaluation"
)

version = st.text_input(
    "Version / Year:",
    value="2026"
)

identifier = st.text_input(
    "URL / DOI / PMID:",
    value="https://uroweb.org/guidelines/prostatecancer/chapter/diagnostic-evaluation"
)

st.header("4. Verification")

status = st.selectbox(
    "Verification status:",
    [
        "Supported",
        "Partially supported",
        "Not supported",
        "Source not verified"
    ]
)

final_wording = st.text_area(
    "Final evidence-backed wording:",
    placeholder="Write the corrected and evidence-backed formulation."
)

if st.button("Generate evidence record"):

    if not claim or not evidence or not source:
        st.warning("Please complete the claim, evidence and source fields.")

    else:
        st.success("Evidence record created.")

        st.divider()

        st.subheader("Evidence Verification Record")

        st.write("**Claim:**", claim)
        st.write("**Evidence:**", evidence)
        st.write("**Source:**", source)
        st.write("**Version / Year:**", version)
        st.write("**Identifier:**", identifier)
        st.write("**Verification status:**", status)

        st.subheader("Evidence-backed final wording")

        if final_wording:
            st.info(final_wording)
        else:
            st.warning("No final wording provided.")

        st.caption(
            "MedEvidence-AI is an experimental research and educational prototype. "
            "Human review remains necessary."
        )

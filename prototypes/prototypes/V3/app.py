import streamlit as st

st.set_page_config(
    page_title="MedEvidence-AI V3",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 MedEvidence-AI")
st.caption("V3 — Evidence Sources")

st.info(
    "V3 associe des claims médicaux à des sources candidates. "
    "Une source candidate n'est pas automatiquement considérée comme une preuve."
)

st.subheader("Clinical claim")

claim = st.text_area(
    "Claim à vérifier",
    placeholder="Exemple : PSA is prostate-specific but not cancer-specific."
)

st.subheader("Candidate evidence source")

source = st.text_input(
    "Titre de la source",
    placeholder="Exemple : EAU Guidelines on Prostate Cancer — Diagnostic Evaluation"
)

source_type = st.selectbox(
    "Type de source",
    [
        "Clinical practice guideline",
        "Systematic review",
        "Meta-analysis",
        "Randomized controlled trial",
        "Observational study",
        "Official medical/scientific organization",
        "Other"
    ]
)

source_url = st.text_input(
    "URL / DOI / PMID",
    placeholder="Lien officiel, DOI ou PMID"
)

if st.button("🔎 Create verification record", type="primary"):

    if not claim or not source:
        st.warning("Veuillez renseigner au minimum le claim et la source.")
    else:

        st.success("Verification record created.")

        st.subheader("Verification record")

        st.write("**Claim**")
        st.write(claim)

        st.write("**Candidate source**")
        st.write(source)

        st.write("**Source type**")
        st.write(source_type)

        st.write("**Reference**")
        st.write(source_url if source_url else "Not provided")

        st.warning(
            "⚠️ Verification pending — the source must be checked "
            "to determine whether it actually supports this specific claim."
        )

st.divider()

st.subheader("V3 principle")

st.markdown("""
**Claim identified**  
↓  
**Candidate source identified**  
↓  
**Source independently checked**  
↓  
**Evidence assessment**

A cited source is not automatically a supporting source.
""")

st.caption(
    "Educational/research prototype. "
    "Not a medical device and not a substitute for clinical judgment."
)

import streamlit as st

st.set_page_config(
    page_title="MedEvidence-AI V5",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 MedEvidence-AI")
st.caption("V5 — Evidence-backed Synthesis")

st.info(
    "V5 rassemble les étapes de vérification afin de construire "
    "une formulation finale fondée sur les preuves disponibles."
)

st.subheader("1. Clinical claim")

claim = st.text_area(
    "Claim",
    placeholder="Affirmation médicale à vérifier"
)

st.subheader("2. Evidence")

evidence = st.text_area(
    "Evidence",
    placeholder="Élément de preuve provenant d'une source médicale"
)

st.subheader("3. Source")

source = st.text_input(
    "Source",
    placeholder="Guideline, article, revue systématique..."
)

source_reference = st.text_input(
    "URL / DOI / PMID",
    placeholder="Référence vérifiable"
)

st.subheader("4. Verification")

status = st.selectbox(
    "Verification status",
    [
        "Supported",
        "Partially supported",
        "Not supported",
        "Source not verified"
    ]
)

st.subheader("5. Final wording")

correction = st.text_area(
    "Formulation finale après vérification",
    placeholder="Formulation corrigée et fondée sur les preuves"
)

if st.button("🧪 Generate evidence record", type="primary"):

    if not claim or not source or not correction:
        st.warning(
            "Veuillez renseigner au minimum le claim, la source "
            "et la formulation finale."
        )

    else:

        st.success("Evidence-backed record created.")

        st.divider()

        st.markdown("### Claim")
        st.write(claim)

        st.markdown("### Evidence")
        st.write(evidence if evidence else "Not provided")

        st.markdown("### Source")
        st.write(source)

        if source_reference:
            st.markdown("### Reference")
            st.write(source_reference)

        st.markdown("### Verification status")

        if status == "Supported":
            st.success("✅ Supported")

        elif status == "Partially supported":
            st.warning("🟡 Partially supported")

        elif status == "Not supported":
            st.error("❌ Not supported")

        else:
            st.warning("🔎 Source not verified")

        st.markdown("### Evidence-backed final wording")
        st.write(correction)

st.divider()

st.subheader("MedEvidence-AI verification-first workflow")

st.markdown("""
**AI-generated response**
↓  
**Claim extraction**
↓  
**Claim classification**
↓  
**Evidence retrieval**
↓  
**Claim ↔ Source verification**
↓  
**Correction**
↓  
**Evidence-backed final response**
""")

st.caption(
    "Educational/research prototype. "
    "Not a medical device and not a substitute for clinical judgment."
)

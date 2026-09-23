import streamlit as st

st.set_page_config(
    page_title="MedEvidence-AI V4",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 MedEvidence-AI")
st.caption("V4 — Claim ↔ Source Verification")

st.info(
    "V4 permet d'évaluer la correspondance entre une affirmation médicale "
    "et les éléments de preuve fournis. Cette évaluation ne remplace pas "
    "une vérification humaine."
)

st.subheader("1. Clinical claim")

claim = st.text_area(
    "Claim à vérifier",
    placeholder=(
        "Exemple : PSA is prostate-specific but not cancer-specific."
    )
)

st.subheader("2. Evidence")

evidence = st.text_area(
    "Extrait de la source ou élément de preuve",
    placeholder=(
        "Collez ici le passage pertinent d'une guideline ou d'un article."
    )
)

st.subheader("3. Source")

source = st.text_input(
    "Source",
    placeholder=(
        "Exemple : EAU Guidelines on Prostate Cancer — Diagnostic Evaluation"
    )
)

source_url = st.text_input(
    "URL / DOI / PMID",
    placeholder="Lien officiel, DOI ou PMID"
)

status = st.selectbox(
    "Verification status",
    [
        "Supported",
        "Partially supported",
        "Not supported",
        "Source not verified"
    ]
)

if st.button("🔎 Assess evidence", type="primary"):

    if not claim or not evidence or not source:
        st.warning(
            "Veuillez renseigner le claim, l'évidence et la source."
        )

    else:

        st.success("Evidence assessment recorded.")

        st.subheader("Verification record")

        st.write("### Claim")
        st.write(claim)

        st.write("### Evidence")
        st.write(evidence)

        st.write("### Source")
        st.write(source)

        ifa

import streamlit as st
import re

st.set_page_config(
    page_title="MedEvidence-AI V2",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 MedEvidence-AI")
st.caption("V2 — Clinical Claim Extraction")

st.info(
    "Cette version n'évalue pas encore si une affirmation est vraie ou fausse. "
    "Elle identifie les affirmations médicales qui doivent être vérifiées."
)

default_text = """The patient's PSA of 90 ng/mL and abnormal digital rectal examination strongly raise suspicion of prostate cancer. PSA is prostate-specific but not cancer-specific. In patients with suspected organ-confined prostate cancer, MRI can be performed before biopsy. Histopathological examination of prostate biopsy tissue is used to confirm the diagnosis."""

response = st.text_area(
    "Collez une réponse médicale générée par une IA",
    value=default_text,
    height=220
)


def classify(sentence):
    s = sentence.lower()

    if any(x in s for x in [
        "should",
        "must",
        "recommended",
        "can be performed",
        "before biopsy",
        "treatment"
    ]):
        return "Recommendation"

    if any(x in s for x in [
        "diagnosis",
        "confirm",
        "suspicion",
        "indicate",
        "suggest"
    ]):
        return "Diagnostic claim"

    if any(x in s for x in [
        "psa is",
        "is not",
        "associated",
        "risk",
        "sensitivity",
        "specificity"
    ]):
        return "Medical fact"

    return "Clinical statement"


if st.button("🔎 Extract claims", type="primary"):

    sentences = [
        x.strip()
        for x in re.split(r'(?<=[.!?])\s+', response.strip())
        if x.strip()
    ]

    claims = []

    for sentence in sentences:

        if len(sentence) < 25:
            continue

        claims.append({
            "claim": sentence,
            "type": classify(sentence),
            "status": "🔎 Needs verification"
        })

    st.subheader("Verification queue")

    st.write(
        f"**{len(claims)} clinical claim(s) identified.**"
    )

    if not claims:

        st.warning(
            "No sufficiently long clinical statements were detected."
        )

    else:

        for i, item in enumerate(claims, 1):

            with st.container(border=True):

                st.markdown(f"### Claim {i}")

                st.write(item["claim"])

                col1, col2 = st.columns(2)

                col1.metric(
                    "Type",
                    item["type"]
                )

                col2.metric(
                    "Status",
                    item["status"]
                )


st.divider()

st.subheader("Next development stage")

st.markdown("""
**Current V2**

AI-generated response  
→ **Claim extraction**  
→ **Claim classification**  
→ **Verification queue**

**Next**

Verification queue  
→ **Medical literature / guidelines**  
→ **Claim–source matching**  
→ **Evidence assessment**
""")

st.caption(
    "Educational/research prototype. "
    "Not a medical device and not a substitute for clinical judgment."
)

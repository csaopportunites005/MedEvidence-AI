import re
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
    **Workflow**

    AI response → Claims → Classification → Evidence →
    Verification → Correction → Final synthesis
    """
)


def classify_claim(claim):
    text = claim.lower().strip()

    recommendation_patterns = [
        r"\bshould\b",
        r"\brecommend(?:ed|ation)?\b",
        r"\bmust\b",
        r"\bconsider\b",
        r"\bavoid\b",
        r"\bdo not\b",
        r"\bis indicated\b"
    ]

    diagnostic_patterns = [
        r"\bsuspect\b",
        r"\bsuspicion\b",
        r"\bdiagnos(?:is|e|ed|tic)\b",
        r"\bbiopsy\b",
        r"\bhistopatholog(?:y|ical)\b",
        r"\bconfirm(?:ed|ation)?\b",
        r"\bconfirmation\b",
        r"\bstaging\b",
        r"\bstage\b",
        r"\bmetast(?:asis|atic)\b",
        r"\bconsistent with\b",
        r"\bsuggests?\b",
        r"\bindicates?\b"
    ]

    if any(
        re.search(pattern, text)
        for pattern in recommendation_patterns
    ):
        return "Recommendation"

    if any(
        re.search(pattern, text)
        for pattern in diagnostic_patterns
    ):
        return "Diagnostic claim"

    return "Medical fact"


def extract_claims(text):
    sentences = re.split(
        r"(?<=[.!?])\s+",
        text.strip()
    )

    return [
        sentence.strip()
        for sentence in sentences
        if len(sentence.strip()) > 20
    ]


st.header("1. AI-generated clinical response")

ai_response = st.text_area(
    "Paste the AI-generated medical response:",
    height=220,
    placeholder="Paste an AI-generated medical response here."
)

if st.button("Extract and classify clinical claims"):

    if not ai_response.strip():

        st.warning(
            "Please enter an AI-generated response."
        )

    else:

        claims = extract_claims(ai_response)

        st.success(
            f"{len(claims)} candidate claim(s) identified."
        )

        st.subheader("Verification queue")

        for index, claim_text in enumerate(
            claims,
            start=1
        ):

            st.markdown(
                f"### Claim {index}"
            )

            st.write(claim_text)

            st.write(
                f"**Type:** {classify_claim(claim_text)}"
            )

            st.caption(
                "🔎 Needs independent verification"
            )


st.divider()


st.header("2. Claim verification record")

claim = st.text_area(
    "Clinical claim to verify:",
    placeholder=(
        "Example: PSA is prostate-specific "
        "but not cancer-specific."
    )
)

if claim.strip():

    st.write(
        f"**Detected claim type:** "
        f"{classify_claim(claim)}"
    )


st.header("3. Evidence")

evidence = st.text_area(
    "Relevant passage from the medical source:",
    placeholder=(
        "Paste the exact relevant passage here."
    )
)


st.header("4. Source")

source = st.text_input(
    "Source name:",
    value=(
        "EAU Guidelines on Prostate Cancer "
        "— Diagnostic Evaluation"
    )
)

version = st.text_input(
    "Version / Year:",
    value="2026"
)

identifier = st.text_input(
    "URL / DOI / PMID:",
    value=(
        "https://uroweb.org/guidelines/"
        "prostatecancer/chapter/diagnostic-evaluation"
    )
)


st.header("5. Source verification")

source_status = st.selectbox(
    "Can the source be independently verified?",
    [
        "Verified",
        "Not verified"
    ]
)


st.header("6. Evidence assessment")

status = st.selectbox(
    "Claim verification status:",
    [
        "Supported",
        "Partially supported",
        "Not supported",
        "Source not verified"
    ]
)

assessment = st.text_area(
    "Why does the evidence support, partially support, "
    "or not support the claim?",
    placeholder=(
        "Explain the relationship between the claim "
        "and the evidence."
    )
)


st.header("7. Evidence-backed final wording")

final_wording = st.text_area(
    "Corrected final wording:",
    placeholder=(
        "Write the final evidence-backed formulation."
    )
)


if st.button("Generate evidence record"):

    if not claim.strip():

        st.warning(
            "Please enter a clinical claim."
        )

    elif not evidence.strip():

        st.warning(
            "Please provide the relevant evidence passage."
        )

    elif not source.strip():

        st.warning(
            "Please provide the source."
        )

    else:

        st.success(
            "Evidence verification record created."
        )

        st.divider()

        st.subheader(
            "Evidence Verification Record"
        )

        st.markdown("### Claim")
        st.write(claim)

        st.markdown("### Claim type")
        st.write(classify_claim(claim))

        st.markdown("### Evidence passage")
        st.info(evidence)

        st.markdown("### Source")
        st.write(source)

        st.write(
            f"**Version / Year:** {version}"
        )

        st.write(
            f"**Identifier:** {identifier}"
        )

        st.markdown(
            "### Source verification"
        )

        if source_status == "Verified":

            st.success(
                "🟢 Source independently verified"
            )

        else:

            st.warning(
                "⚪ Source not independently verified"
            )

        st.markdown(
            "### Claim verification status"
        )

        if status == "Supported":

            st.success("🟢 Supported")

        elif status == "Partially supported":

            st.warning(
                "🟠 Partially supported"
            )

        elif status == "Not supported":

            st.error(
                "🔴 Not supported"
            )

        else:

            st.info(
                "⚪ Source not verified"
            )

        st.markdown(
            "### Evidence assessment"
        )

        if assessment.strip():

            st.write(assessment)

        else:

            st.warning(
                "No assessment provided."
            )

        st.markdown(
            "### Evidence-backed final wording"
        )

        if final_wording.strip():

            st.info(final_wording)

        else:

            st.warning(
                "No final wording provided."
            )

        st.divider()

        st.caption(
            "MedEvidence-AI is an experimental research "
            "and educational prototype. Evidence assessment "
            "requires independent human review and does not "
            "constitute autonomous clinical validation."
        )

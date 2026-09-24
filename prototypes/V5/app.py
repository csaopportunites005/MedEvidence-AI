import re
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

import streamlit as st


st.set_page_config(
    page_title="MedEvidence-AI V5.6",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 MedEvidence-AI V5.6")
st.subheader("Evidence-backed Clinical Synthesis")

st.markdown(
    """
    **Workflow**

    AI response → Claims → Classification → Evidence →
    Source identification → Accessibility → Verification →
    Correction → Final synthesis
    """
)


# --------------------------------------------------
# CLAIM CLASSIFICATION
# --------------------------------------------------

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

    if any(re.search(pattern, text)
           for pattern in recommendation_patterns):
        return "Recommendation"

    if any(re.search(pattern, text)
           for pattern in diagnostic_patterns):
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


# --------------------------------------------------
# SOURCE IDENTIFIER CHECK
# --------------------------------------------------

def inspect_identifier(identifier):
    value = identifier.strip()

    if not value:
        return (
            "⚪ Identifiant insuffisant",
            "Aucun URL, DOI ou PMID fourni."
        )

    if value.startswith(("http://", "https://")):

        try:
            parsed = urlparse(value)

            if parsed.scheme and parsed.netloc:
                return (
                    "🟡 URL fournie",
                    "Format URL reconnu."
                )

        except Exception:
            pass

        return (
            "⚪ URL non reconnue",
            "Le format de l'URL semble incorrect."
        )

    if re.match(
        r"^(https?://doi\.org/)?10\.\d{4,9}/\S+$",
        value,
        re.IGNORECASE
    ):
        return (
            "🟡 DOI identifié",
            "Format DOI reconnu."
        )

    if re.match(
        r"^(PMID\s*)?\d+$",
        value,
        re.IGNORECASE
    ):
        return (
            "🟡 PMID identifié",
            "Format PMID reconnu."
        )

    return (
        "⚪ Identifiant non reconnu",
        "Le format fourni ne correspond pas clairement "
        "à une URL, un DOI ou un PMID."
    )


# --------------------------------------------------
# URL ACCESSIBILITY CHECK
# --------------------------------------------------

def check_url_accessibility(identifier):

    value = identifier.strip()

    if not value.startswith(("http://", "https://")):
        return (
            "⚪ Non applicable",
            "Le contrôle d'accessibilité nécessite une URL."
        )

    try:

        request = Request(
            value,
            headers={
                "User-Agent": (
                    "MedEvidence-AI/5.6 "
                    "(research prototype)"
                )
            }
        )

        with urlopen(
            request,
            timeout=10
        ) as response:

            status_code = response.getcode()

            if 200 <= status_code < 300:

                return (
                    "🟢 Source accessible",
                    f"L'URL a répondu avec le code HTTP {status_code}. "
                    "Cela confirme l'accessibilité technique de l'URL, "
                    "pas la validité du contenu comme preuve."
                )

            return (
                "🟠 Réponse HTTP",
                f"L'URL a répondu avec le code HTTP {status_code}."
            )

    except HTTPError as error:

        if error.code in [401, 403]:

            return (
                "🟠 Accès limité",
                f"La source répond avec HTTP {error.code}. "
                "L'accès peut nécessiter une autorisation."
            )

        return (
            "🔴 Source inaccessible",
            f"La source a répondu avec HTTP {error.code}."
        )

    except URLError as error:

        return (
            "🔴 Source inaccessible",
            "Impossible d'accéder à l'URL depuis l'application."
        )

    except Exception:

        return (
            "🟠 Vérification impossible",
            "Une erreur est survenue pendant la tentative d'accès."
        )


# --------------------------------------------------
# 1. AI RESPONSE
# --------------------------------------------------

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


# --------------------------------------------------
# 2. CLAIM
# --------------------------------------------------

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


# --------------------------------------------------
# 3. EVIDENCE
# --------------------------------------------------

st.header("3. Evidence")

evidence = st.text_area(
    "Relevant passage from the medical source:",
    placeholder=(
        "Paste the exact relevant passage here."
    )
)


# --------------------------------------------------
# 4. SOURCE
# --------------------------------------------------

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


# --------------------------------------------------
# 5. SOURCE IDENTIFICATION
# --------------------------------------------------

st.header("5. Source identification check")

identifier_status, identifier_message = inspect_identifier(
    identifier
)

st.write(identifier_status)
st.caption(identifier_message)


# --------------------------------------------------
# 5B. ACCESSIBILITY
# --------------------------------------------------

st.header("5B. Source accessibility")

if identifier.startswith(("http://", "https://")):

    if st.button("Check source accessibility"):

        accessibility_status, accessibility_message = (
            check_url_accessibility(identifier)
        )

        st.write(accessibility_status)
        st.caption(accessibility_message)

else:

    st.info(
        "Enter a valid URL to test technical accessibility."
    )


# --------------------------------------------------
# 6. EVIDENCE ASSESSMENT
# --------------------------------------------------

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


# --------------------------------------------------
# 7. FINAL WORDING
# --------------------------------------------------

st.header("7. Evidence-backed final wording")

final_wording = st.text_area(
    "Corrected final wording:",
    placeholder=(
        "Write the final evidence-backed formulation."
    )
)


# --------------------------------------------------
# GENERATE RECORD
# --------------------------------------------------

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
            "### Source identification"
        )

        st.write(identifier_status)
        st.caption(identifier_message)

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
            "and educational prototype. URL accessibility "
            "does not establish source validity or prove "
            "that the source supports a clinical claim. "
            "Human verification remains necessary."
        )

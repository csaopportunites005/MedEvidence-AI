# MedEvidence-AI

**A verification-first AI workflow for evidence-based clinical research**

MedEvidence-AI is an experimental personal prototype exploring how artificial intelligence can support structured, evidence-based clinical research while reducing the risk of unsupported, inaccurate, or fabricated references.

The project focuses on a simple principle:

> AI-generated clinical information should be structured, traceable and verified before being used as evidence.

---

## 🎯 Problem

Generative AI can help medical students and clinicians structure clinical cases, explore differential diagnoses, identify relevant investigations and synthesize medical literature.

However, AI-generated clinical answers may contain:

- unsupported clinical claims
- inaccurate or outdated recommendations
- inappropriate extrapolation of guidelines
- incorrect or unverifiable references
- excessive certainty when evidence is limited

> A plausible answer is not necessarily a verified answer.

MedEvidence-AI explores a workflow designed to address this problem.

---

## 💡 Core Concept

Clinical case → Structured analysis → Evidence search → AI-assisted synthesis → Source verification → Correction → Evidence-backed response

The key feature is the verification step. Instead of simply accepting an AI-generated answer, the workflow asks:

1. What clinical claims were made?
2. What evidence supports each important claim?
3. Can the cited source actually be verified?
4. Is the source appropriate for the recommendation?
5. Does the source actually support the claim?
6. Is the level of certainty justified?

---

## 🔬 Clinical Research Workflow

```text
Clinical Case
  ↓
Case Structuring
  ↓
Clinical Problem Identification
  ↓
Differential Diagnosis
  ↓
Missing Information
  ↓
Diagnostic Pathway
  ↓
Evidence Search
  ↓
AI-Assisted Synthesis
  ↓
Claim Extraction
  ↓
Source Verification
  ↓
Correction / Refinement
  ↓
Evidence-Backed Final Response
```

---

## 🧪 Clinical Test Case

The initial proof of concept uses a clinical case involving a **70-year-old man with suspected prostate cancer**.

The case includes:

- dysuria and pollakiuria
- an enlarged, painless prostate with nodules on digital rectal examination
- total PSA of 90 ng/mL
- incomplete information requiring further clinical assessment

The objective is not to automatically diagnose the patient. Instead, the case is used to evaluate whether an AI-assisted workflow can:

- structure the clinical problem
- identify relevant differential diagnoses
- identify missing clinical information
- propose an appropriate diagnostic pathway
- distinguish clinical suspicion from histological confirmation
- identify relevant evidence
- verify cited sources
- communicate uncertainty appropriately

The complete test case is available in: `cases/prostate_cancer_case.md`

---

## 📚 Evidence Verification

A central component of MedEvidence-AI is the independent verification of important clinical claims and references.

For the initial test case, selected recommendations were checked against:

**European Association of Urology (EAU) Guidelines on Prostate Cancer – Diagnostic Evaluation, 2026**

The verification process focuses on:

- source identity
- publication or guideline year
- relevance to the clinical question
- whether the source actually supports the claim
- limitations and context
- distinction between evidence and interpretation

Verified sources are documented in: `evidence/verified_sources.md`

> A reference is not considered verified simply because an AI model provides a citation.

---

## 🤖 AI-Assisted Research

The prototype was explored using multiple generative AI systems, including ChatGPT, Google Gemini and Claude.

The objective was not to determine which model is "best". Instead, the models were examined using common criteria:

- clinical structure
- evidence quality
- source verifiability
- diagnostic reasoning
- identification of missing information
- handling of uncertainty
- distinction between suspicion and confirmation

The comparison is documented in: `evaluations/model_comparison.md`

---

## 📊 Evaluation Approach

| Criterion | Question |
|---|---|
| Clinical structure | Is the clinical problem correctly structured? |
| Evidence support | Are important claims supported by evidence? |
| Source quality | Are authoritative and appropriate sources used? |
| Verifiability | Can cited references be independently verified? |
| Clinical pathway | Is the proposed diagnostic pathway coherent? |
| Missing information | Are important missing data identified? |
| Uncertainty | Is uncertainty appropriately communicated? |
| Evidence vs interpretation | Are recommendations distinguished from interpretation? |

This is currently an exploratory evaluation and not a formal benchmark.

---

## 🧭 Methodology

1. Case structuring
2. Clinical question formulation
3. Differential diagnosis
4. Identification of missing information
5. Evidence search
6. AI-assisted synthesis
7. Claim extraction
8. Source verification
9. Correction and refinement
10. Final evidence-backed response

The methodology is described in: `docs/methodology.md`

---

## ⚠️ Limitations

MedEvidence-AI is currently an **experimental personal prototype**. It is:

- not a validated clinical decision-support system
- not a medical device
- not intended to replace clinicians
- not intended to provide autonomous clinical decisions

AI-generated information can still contain factual errors, incomplete reasoning, outdated information, inappropriate recommendations, incorrect references and contextual limitations. Source verification reduces these risks but does not eliminate them.

Additional limitations are documented in: `docs/limitations.md`

---

## 🌍 Context and Future Direction

The project is being developed from the perspective of a medical student interested in the intersection of **Medicine × Artificial Intelligence × Digital Innovation × Evidence-Based Research**.

Future development may explore:

- more systematic claim extraction
- automated reference verification
- structured evidence tables
- comparison of clinical guidelines
- reproducible evaluation datasets
- quantitative evaluation metrics
- better handling of uncertainty
- adaptation to resource-constrained and African healthcare contexts
- integration into digital health tools

---

## 📁 Repository Structure

```text
MedEvidence-AI/
├── README.md
├── cases/
│   └── prostate_cancer_case.md
├── docs/
│   ├── methodology.md
│   └── limitations.md
├── evaluations/
│   └── model_comparison.md
├── evidence/
│   └── verified_sources.md
└── prompts/
    └── clinical_research_prompt.md
```

---

## 🔐 Responsible Use

MedEvidence-AI is intended for educational and research purposes. It should not be used as an autonomous source of clinical decision-making.

Clinical information generated with AI should be independently reviewed, verified against appropriate medical literature or guidelines, and interpreted within the relevant clinical context.

> AI can assist with organizing and synthesizing clinical information, but evidence must remain traceable, verifiable and subject to human oversight.

---

## 📌 Project Status

**Status:** Experimental proof of concept

The current version demonstrates the workflow using a clinical test case and an initial set of verified evidence. The project is intended to evolve through further testing, structured evaluation and methodological refinement.

---

## 👤 Author

**Serge Agassounon**
Medical Student | AI, Digital Innovation & Health
University of Abomey-Calavi (UAC), Faculty of Health Sciences (FSS)
Cotonou, Benin

---

## 📄 License

This repository is currently a personal educational and research prototype. Further licensing decisions may be added as the project develops.

# AI Model Comparison – MedEvidence-AI

## Objective

This evaluation explores how different generative AI systems respond to the same clinical research task using the MedEvidence-AI workflow.

The objective is not to rank the models, but to identify differences in:

- Clinical structure
- Evidence handling
- Source quality
- Reference verifiability
- Identification of uncertainty
- Adherence to the requested diagnostic pathway

---

## Models Evaluated

The initial workflow was tested with:

- ChatGPT
- Google Gemini
- Claude

The same clinical case and research objective were used as the basis for comparison.

---

## Evaluation Criteria

Each response was reviewed using the following criteria.

### 1. Clinical structure

Does the response clearly organize:

- The clinical problem
- Differential diagnoses
- Missing information
- Diagnostic investigations
- Confirmation
- Staging when appropriate

### 2. Evidence quality

Does the response rely on:

- Clinical practice guidelines
- Systematic reviews
- Primary research
- Appropriate authoritative sources

### 3. Reference verification

For each important reference:

- Does the cited source exist?
- Can it be independently located?
- Does the source actually support the claim?
- Is the source sufficiently authoritative for the recommendation?

### 4. Clinical certainty

Does the response distinguish between:

- Clinical suspicion
- Diagnostic evidence
- Histological confirmation
- Interpretation
- Uncertainty

### 5. Missing information

Does the response identify important clinical information that is not available in the case?

---

## Initial Observations

### ChatGPT

The response provided a structured clinical pathway and clearly separated clinical suspicion from histological confirmation.

The main verification requirement was to independently check the cited recommendations and sources before considering them definitive evidence.

### Google Gemini

The response provided a structured analysis but included references and recommendations requiring additional verification.

This highlighted the importance of checking whether the cited source directly supports the associated clinical claim.

### Claude

The response provided a detailed and critical analysis, including discussion of uncertainty and missing information.

References and specific recommendations still required independent verification before being treated as confirmed evidence.

---

## Cross-Model Observation

The initial experiment demonstrated an important principle:

> **A clinically plausible AI response is not necessarily a fully verified evidence-based response.**

Different models may provide useful reasoning and structure while still requiring verification of their references and clinical claims.

This observation motivated the verification-first design of MedEvidence-AI.

---

## Evaluation Approach

Future evaluations should use a structured assessment rather than subjective impressions.

Possible measures include:

- Number of important clinical claims
- Number of claims supported by an appropriate source
- Number of unverifiable references
- Number of unsupported claims
- Accuracy of diagnostic pathway
- Identification of missing information
- Appropriate expression of uncertainty

---

## Limitations

This initial comparison is exploratory.

It does not constitute a formal benchmark of the evaluated AI systems.

The results may depend on:

- Prompt wording
- Model version
- Access to web search
- Available sources
- Date of evaluation
- Clinical question

Further testing with standardized prompts and multiple clinical cases would be required for a more rigorous evaluation.

---

## Conclusion

The initial experiment supports the need for a workflow in which AI-generated clinical information is subjected to structured source verification before being treated as evidence.

MedEvidence-AI therefore focuses on **traceability and verification rather than simply generating clinical answers**.

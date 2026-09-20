# Limitations – MedEvidence-AI

## 1. Prototype Status

MedEvidence-AI is currently an experimental personal prototype.

It is designed to explore a verification-first workflow for AI-assisted clinical research. It is not a validated clinical decision-support system or a medical device.

---

## 2. AI Reliability

Generative AI systems can produce information that appears clinically plausible but may contain:

- Incorrect statements
- Missing information
- Outdated recommendations
- Unsupported clinical claims
- Incorrect or unverifiable references
- Excessive certainty

Source verification can reduce these risks, but it cannot guarantee that every part of an AI-generated response is correct.

---

## 3. Reference Verification

A verified reference does not automatically mean that every statement associated with it is correct.

The specific claim must still be compared with the actual content of the source.

The workflow therefore emphasizes:

**Claim → Source → Verification → Interpretation**

rather than simply counting the number of references provided by an AI system.

---

## 4. Evidence Availability

Relevant evidence may be:

- difficult to access
- published in different formats
- outdated
- conflicting
- unavailable for a specific patient population or clinical context

The absence of easily accessible evidence should not be interpreted as evidence that a clinical intervention is ineffective or inappropriate.

---

## 5. Guideline Differences

Clinical guidelines may differ in their recommendations because of:

- Different publication dates
- Different evidence selection methods
- Different healthcare settings
- Different interpretations of available evidence
- Differences in target populations

MedEvidence-AI should therefore identify important differences rather than assuming that one recommendation is universally applicable.

---

## 6. African and Sub-Saharan Context

Much medical evidence is generated in populations and healthcare systems that may differ from those in African and sub-Saharan African settings.

Important contextual differences may include:

- Disease prevalence
- Available diagnostic technologies
- Healthcare infrastructure
- Medication availability
- Cost and accessibility
- Referral pathways
- Patient populations

Evidence should therefore be assessed for its applicability to the intended clinical context.

---

## 7. Limited Evaluation

The current project has been tested on a limited number of clinical research tasks.

The initial comparison between ChatGPT, Google Gemini and Claude is exploratory and does not constitute a formal benchmark.

A more rigorous evaluation would require:

- Multiple clinical cases
- Standardized prompts
- Predefined evaluation criteria
- Independent reviewers
- Repeated testing
- Quantitative performance measures

---

## 8. Model and Tool Dependence

AI-generated outputs may vary depending on:

- Model version
- Prompt wording
- Available tools
- Web-search capabilities
- Retrieved sources
- Date of evaluation

Therefore, results obtained from one model or one evaluation session may not be reproducible under different conditions.

---

## 9. Human Oversight

MedEvidence-AI does not remove the need for human review.

Clinical interpretation should remain the responsibility of qualified healthcare professionals.

The workflow is intended to support research and reasoning, not to make autonomous medical decisions.

---

## 10. Future Improvements

Future versions could address these limitations by:

- Developing a larger evaluation dataset
- Creating standardized clinical test cases
- Introducing quantitative evaluation metrics
- Improving automated claim extraction
- Linking individual claims to specific evidence
- Tracking guideline versions and updates
- Testing reproducibility across AI models
- Evaluating applicability in African healthcare contexts

---

## 11. Responsible Use

MedEvidence-AI should be considered an educational and research prototype.

It must not be used as an autonomous diagnostic or treatment system.

Any clinical information generated through the workflow should be reviewed against current authoritative evidence and interpreted within the appropriate clinical context.

---

## Core Limitation

The central limitation of MedEvidence-AI is also the reason for its existence:

> **AI can help organize and synthesize clinical information, but the reliability of its output still depends on evidence quality, source verification, context and human oversight.**

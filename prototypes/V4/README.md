# MedEvidence-AI V4 — Claim ↔ Source Verification

V4 introduces the evidence-assessment stage of MedEvidence-AI.

## Workflow

AI-generated response
→ Claim extraction
→ Claim classification
→ Candidate source
→ Evidence assessment
→ Verification status

## Objective

Assess whether a retrieved or provided medical source actually supports the specific clinical claim being evaluated.

## Verification statuses

- Supported
- Partially supported
- Not supported
- Source not verified

## Important principle

A source citation does not automatically mean that the source supports the claim.

The relevant evidence must be examined and compared with the exact statement.

## Example

### Claim

> PSA is prostate-specific but not cancer-specific.

### Evidence

Relevant passage from a clinical guideline.

### Assessment

**Supported**

The evidence directly supports the claim.

## Limitations

V4 is an experimental research prototype.

The assessment may require human review and should not be interpreted as autonomous clinical validation.

## Status

Experimental prototype.

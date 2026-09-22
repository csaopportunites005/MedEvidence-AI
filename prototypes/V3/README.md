# MedEvidence-AI V3 — Evidence Sources

V3 extends the claim-extraction workflow by introducing candidate medical evidence sources.

## Workflow

AI-generated response  
→ Claim extraction  
→ Claim classification  
→ Candidate evidence sources  
→ Verification queue

## Objective

For each clinical claim identified by MedEvidence-AI, provide relevant medical sources that can be used for independent verification.

## Source types

Priority should be given to:

- Clinical practice guidelines
- Systematic reviews
- Meta-analyses
- Randomized controlled trials
- High-quality observational studies
- Official medical or scientific organizations

## Important principle

A candidate source is not automatically considered evidence supporting a claim.

The source must be independently checked to determine whether it actually supports the specific statement.

## Example

**Claim**

> PSA is prostate-specific but not cancer-specific.

**Candidate source**

EAU Guidelines on Prostate Cancer — Diagnostic Evaluation

**Status**

🔎 Source identified — verification pending.

## Status

Experimental prototype.

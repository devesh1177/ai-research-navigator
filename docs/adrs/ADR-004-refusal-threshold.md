# ADR-004: Refusal Threshold

## Status

Accepted

## Context

The system should avoid answering questions unrelated to the research corpus.

## Decision

Apply:

- Research term filtering
- Retrieval confidence threshold

before answer generation.

## Consequences

Advantages:

- Reduces hallucinations
- Improves trustworthiness

Trade-offs:

- Some valid questions may be rejected
- Threshold tuning required
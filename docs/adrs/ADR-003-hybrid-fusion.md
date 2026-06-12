# ADR-003: Hybrid Retrieval Fusion

## Status

Accepted

## Context

Dense retrieval may miss keyword matches while BM25 may miss semantic matches.

## Decision

Use:

- Dense Retrieval
- BM25 Retrieval
- Reciprocal Rank Fusion (RRF)

to combine rankings.

## Consequences

Advantages:

- Better recall
- More robust retrieval

Trade-offs:

- Additional retrieval cost
- More implementation complexity
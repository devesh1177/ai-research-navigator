# ADR-002: Embedding Model Selection

## Status

Accepted

## Context

The project requires efficient semantic retrieval with low resource requirements.

## Decision

Use:

BAAI/bge-small-en-v1.5

## Consequences

Advantages:

- Strong retrieval performance
- Fast inference
- Small memory footprint

Trade-offs:

- Lower accuracy than larger embedding models
- Requires external model download
# ADR-001: Chunking Strategy

## Status

Accepted

## Context

Research papers contain long sections that exceed embedding model context windows.

## Decision

Use section-aware chunking with LangChain text splitters.

Chunk boundaries respect document structure whenever possible.

## Consequences

Advantages:

- Better retrieval quality
- Preserves semantic coherence
- Improves citation accuracy

Trade-offs:

- Slightly larger ingestion time
- More metadata management
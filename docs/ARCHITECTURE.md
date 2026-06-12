# AI Research Navigator Architecture

## Overview

AI Research Navigator is a research-focused Retrieval-Augmented Generation (RAG) system designed to ingest, index, retrieve, and explain AI research papers.

The system consists of five major subsystems:

1. Ingestion
2. Retrieval
3. Generation
4. Agentic Workflow
5. Evaluation

---

## High-Level Architecture

User Query
│
▼
LangGraph Router
│
├── Concept Explanation
├── Paper Deep Dive
├── Compare Approaches
├── Recent Developments
├── Find Papers
└── Fallback
│
▼
Hybrid Retrieval
(Dense + BM25)
│
▼
Qdrant Vector Database
│
▼
Answer Generation
│
▼
Citations

---

## Ingestion Layer

Location:

src/research_navigator/ingest

Responsibilities:

- Parse PDFs and Markdown
- Extract sections
- Chunk documents
- Generate embeddings
- Store vectors in Qdrant

Output:

- Embedded document chunks
- Metadata
- Section information

---

## Retrieval Layer

Location:

src/research_navigator/retrieve

Responsibilities:

- Query understanding
- Metadata filtering
- Dense retrieval
- BM25 retrieval
- Reciprocal Rank Fusion
- Refusal handling

Output:

- Ranked document chunks

---

## Generation Layer

Location:

src/research_navigator/generate

Responsibilities:

- Build retrieval context
- Generate grounded answers
- Generate citations

Output:

- Answer
- Citation list

---

## Agent Layer

Location:

src/research_navigator/agents

Responsibilities:

- Route user queries
- Execute specialized workflows
- Handle out-of-scope requests

Routes:

- concept_explanation
- paper_deep_dive
- compare_approaches
- recent_developments
- find_papers
- fallback

---

## Evaluation Layer

Location:

src/tests/eval

Responsibilities:

- Precision@K
- Recall@K
- Refusal correctness
- Latency benchmarking
- Token cost analysis
- Dense vs Hybrid comparison

Output:

- evaluation_report.json
- M4_EVALUATION_REPORT.md

---

## Configuration

Location:

src/research_navigator/config/settings.py

Managed through:

- pydantic-settings
- environment variables

Configurable values:

- Qdrant host
- Qdrant port
- collection name
- embedding model
- retrieval thresholds

---

## Storage

Vector Database:

- Qdrant

Embedding Model:

- BAAI/bge-small-en-v1.5

Retrieval Strategy:

- Dense Retrieval
- BM25 Retrieval
- Reciprocal Rank Fusion
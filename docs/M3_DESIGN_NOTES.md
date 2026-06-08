# M3 – Agentic Layer with LangGraph

## Objective

M3 extends the AI Research Navigator by introducing an agentic orchestration layer using LangGraph. The system routes user queries to specialized nodes based on intent and executes retrieval and reasoning workflows appropriate for each query type.

---

# Architecture Overview

The M3 architecture consists of:

1. Router
2. Specialized Agent Nodes
3. Shared State
4. Retrieval Layer (M2)
5. Tool Layer
6. LangGraph Workflow

The Router determines the intent of an incoming query and dispatches execution to the appropriate node.

---

# State Design

The workflow uses an explicit serializable state object.

```python
NavigatorState = {
    "query": str,
    "route": str,
    "answer": str,
    "citations": list,
    "metadata": dict,
}
```

State is passed between all nodes and contains the information required to execute and track the workflow.

---

# Router

The Router classifies incoming queries into one of six categories:

* concept_explanation
* paper_deep_dive
* compare_approaches
* recent_developments
* find_papers
* out_of_scope

The routing mechanism is rule-based and deterministic.

Example:

| Query                      | Route               |
| -------------------------- | ------------------- |
| What is RAG?               | concept_explanation |
| Explain LoRA               | paper_deep_dive     |
| Compare LoRA vs ReAct      | compare_approaches  |
| Recent RAG papers          | recent_developments |
| Recommend papers on agents | find_papers         |
| Who won FIFA 2022?         | out_of_scope        |

---

# Agent Nodes

## ConceptExplanation

Purpose:

Provide a synthesized explanation of a research concept using multiple sources retrieved from the corpus.

Examples:

* What is RAG?
* Explain transformers
* What is RLHF?

Implementation:

* Uses M2 hybrid retrieval
* Uses answer generation pipeline
* Aggregates evidence from multiple documents

---

## PaperDeepDive

Purpose:

Provide a focused explanation of a specific research paper.

Examples:

* Explain Attention Is All You Need
* Explain LoRA
* Explain ReAct

Implementation:

* Uses lookup_paper() tool
* Retrieves preferentially from chunks belonging to the identified paper
* Generates paper-specific responses

---

## CompareApproaches

Purpose:

Compare two methods, papers, or techniques.

Examples:

* Compare LoRA vs ReAct
* Compare GPT-3 vs BERT
* Compare RAG vs GraphRAG

Implementation:

* Retrieves information for both approaches
* Produces a structured comparison

---

## RecentDevelopments

Purpose:

Identify recent work in a research area.

Examples:

* Recent RAG papers
* Recent agent papers
* Recent LLM developments

Implementation:

* Uses get_recent_year_cutoff() tool
* Filters results using publication year
* Produces a chronological digest

---

## FindPapers

Purpose:

Recommend papers for learning a topic.

Examples:

* Recommend papers on agents
* Recommend papers on transformers
* Recommend papers on reasoning

Implementation:

* Uses retrieval results and metadata
* Produces a reading list
* Includes year and category information

---

## Fallback

Purpose:

Handle out-of-scope queries.

Examples:

* Who won FIFA 2022?
* Capital of Japan?
* Chocolate cake recipe

Implementation:

Returns a polite refusal indicating insufficient corpus coverage.

---

# Tool Usage

Two tools were integrated into the workflow.

## lookup_paper()

Used by:

* PaperDeepDive

Purpose:

Maps user paper references to known papers in the corpus.

Examples:

* Attention Is All You Need
* LoRA
* ReAct
* Llama 2

---

## get_recent_year_cutoff()

Used by:

* RecentDevelopments

Purpose:

Computes a recency threshold for filtering research papers.

---

# LangGraph Workflow

The workflow is implemented using LangGraph StateGraph.

Graph structure:

```text
Router
 ├── ConceptExplanation
 ├── PaperDeepDive
 ├── CompareApproaches
 ├── RecentDevelopments
 ├── FindPapers
 └── Fallback
        ↓
       END
```

Each route terminates at END after completing execution.

---

# Retrieval Layer Integration

All agent nodes reuse the M2 retrieval stack:

* Dense Retrieval (Qdrant)
* BM25 Retrieval
* Reciprocal Rank Fusion (RRF)
* Metadata Filtering
* Citation Generation

This avoids duplication and allows all agent nodes to share a common retrieval infrastructure.

---

# Testing

Each route was exercised using at least three representative queries.

## ConceptExplanation

* What is RAG?
* Explain transformers
* What is RLHF?

## PaperDeepDive

* Explain Attention Is All You Need
* Explain LoRA
* Explain ReAct

## CompareApproaches

* Compare LoRA vs ReAct
* Compare GPT-3 vs BERT
* Compare RAG vs GraphRAG

## RecentDevelopments

* Recent RAG papers
* Recent agent papers
* Recent LLM developments

## FindPapers

* Recommend papers on agents
* Recommend papers on transformers
* Recommend papers on reasoning

## Fallback

* Who won FIFA 2022?
* Capital of Japan?
* Chocolate cake recipe

All routes produced the expected routing behavior.

---

# Graph Visualization

The LangGraph workflow was visualized using LangGraph's built-in graph rendering functionality.

Generated artifact:

```text
graph.png
```

The visualization illustrates routing from the Router node to all specialized agent nodes.

---

# Deliverables Completed

* LangGraph State Machine
* Explicit Serializable State
* Router
* ConceptExplanation Node
* PaperDeepDive Node
* CompareApproaches Node
* RecentDevelopments Node
* FindPapers Node
* Fallback Node
* Tool Integration
* Graph Visualization
* Route Testing
* Design Documentation

M3 requirements have been successfully completed.

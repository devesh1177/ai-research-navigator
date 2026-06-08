from research_navigator.retrieve.retriever import (
    retrieve,
)

from research_navigator.retrieve.bm25_retriever import (
    bm25_search,
)


RESEARCH_TERMS = [
    "transformer",
    "transformers",
    "attention",
    "bert",
    "gpt",
    "llm",
    "rag",
    "graphrag",
    "agentic rag",
    "retrieval",
    "lora",
    "rlhf",
    "constitutional ai",
    "react",
    "agent",
    "agents",
    "swe-agent",
    "reasoning",
    "chain of thought",
    "deepseek",
    "gemini",
    "qwen",
    "mixtral",
    "llama",
    "alignment",
    "fine tuning",
    "fine-tuning",
    "prompting",
    "multimodal",
    "hallucination",
    "hallucinations",
    "benchmark",
    "evaluation",
]


def is_corpus_query(
    query: str,
) -> bool:

    query = query.lower()

    return any(
        term in query
        for term in RESEARCH_TERMS
    )


def hybrid_retrieve(
    query: str,
    k: int = 5,
    confidence_threshold: float = 0.65,
):

    # ---------------------------------
    # Reject unrelated questions
    # ---------------------------------

    if not is_corpus_query(
        query
    ):
        return []

    # ---------------------------------
    # Dense Retrieval
    # ---------------------------------

    dense_results = retrieve(
        query,
        k=10,
        min_score=0.0,
    )

    if not dense_results:
        return []

    # ---------------------------------
    # Low Confidence Refusal
    # ---------------------------------

    best_dense_score = (
        dense_results[0].score
    )

    if (
        best_dense_score
        < confidence_threshold
    ):
        return []

    # ---------------------------------
    # BM25 Retrieval
    # ---------------------------------

    bm25_results = bm25_search(
        query,
        top_k=10,
    )

    # ---------------------------------
    # Reciprocal Rank Fusion (RRF)
    # ---------------------------------

    fused_scores = {}

    # Dense scores

    for rank, point in enumerate(
        dense_results,
        start=1,
    ):

        doc_id = point.payload[
            "doc_id"
        ]

        fused_scores[doc_id] = {
            "point": point,
            "score": 1.0 / rank,
        }

    # BM25 scores

    for rank, (
        point,
        _
    ) in enumerate(
        bm25_results,
        start=1,
    ):

        doc_id = point.payload[
            "doc_id"
        ]

        if doc_id not in fused_scores:

            fused_scores[doc_id] = {
                "point": point,
                "score": 0.0,
            }

        fused_scores[doc_id][
            "score"
        ] += 1.0 / rank

    # ---------------------------------
    # Sort by fused score
    # ---------------------------------

    ranked = sorted(
        fused_scores.values(),
        key=lambda x: x["score"],
        reverse=True,
    )

    # ---------------------------------
    # Remove duplicate documents
    # ---------------------------------

    final_results = []

    seen_docs = set()

    for item in ranked:

        point = item["point"]

        doc_id = point.payload[
            "doc_id"
        ]

        if doc_id in seen_docs:
            continue

        seen_docs.add(doc_id)

        final_results.append(
            point
        )

        if len(final_results) >= k:
            break

    return final_results
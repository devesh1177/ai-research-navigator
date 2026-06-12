from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
    is_corpus_query,
)


class MockPoint:
    def __init__(
        self,
        doc_id: str,
        score: float,
    ) -> None:

        self.score = score

        self.payload = {
            "doc_id": doc_id,
            "title": f"Paper {doc_id}",
        }


def test_corpus_query_true() -> None:

    assert is_corpus_query("What is RAG?")


def test_corpus_query_false() -> None:

    assert not is_corpus_query("Who won FIFA 2022?")


def test_hybrid_retrieve_out_of_scope() -> None:

    results = hybrid_retrieve("Who won FIFA 2022?")

    assert results == []


def test_hybrid_retrieve_low_confidence(
    monkeypatch,
) -> None:

    monkeypatch.setattr(
        "research_navigator.retrieve.hybrid_retriever.retrieve",
        lambda query, k=10, min_score=0.0: [MockPoint("1", 0.2)],
    )

    results = hybrid_retrieve("What is RAG?")

    assert results == []


def test_hybrid_retrieve_success(
    monkeypatch,
) -> None:

    dense_results = [
        MockPoint("1", 0.9),
        MockPoint("2", 0.8),
    ]

    bm25_results = [
        (MockPoint("1", 0.9), 5.0),
        (MockPoint("3", 0.8), 4.0),
    ]

    monkeypatch.setattr(
        "research_navigator.retrieve.hybrid_retriever.retrieve",
        lambda query, k=10, min_score=0.0: dense_results,
    )

    monkeypatch.setattr(
        "research_navigator.retrieve.hybrid_retriever.bm25_search",
        lambda query, top_k=10: bm25_results,
    )

    results = hybrid_retrieve("What is RAG?")

    assert len(results) > 0

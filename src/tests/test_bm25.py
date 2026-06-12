from research_navigator.retrieve.bm25_retriever import (
    bm25_search,
)


class MockPoint:
    def __init__(self, text: str) -> None:

        self.payload = {
            "content": text,
        }


def test_bm25_search(monkeypatch) -> None:

    mock_points = [
        MockPoint("transformer attention mechanism"),
        MockPoint("retrieval augmented generation"),
    ]

    class MockClient:
        def scroll(
            self,
            collection_name,
            limit,
            with_payload,
        ):
            return mock_points, None

    monkeypatch.setattr(
        "research_navigator.retrieve.bm25_retriever.client",
        MockClient(),
    )

    results = bm25_search(
        "transformer",
        top_k=2,
    )

    assert len(results) == 2

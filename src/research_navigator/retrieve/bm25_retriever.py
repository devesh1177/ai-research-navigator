from typing import Any

from rank_bm25 import BM25Okapi  # type: ignore[import-untyped]

from qdrant_client import QdrantClient


client = QdrantClient(
    host="localhost",
    port=6333,
)


def bm25_search(
    query: str,
    top_k: int = 10,
) -> list[tuple[Any, float]]:

    points, _ = client.scroll(
        collection_name="research_navigator",
        limit=10000,
        with_payload=True,
    )

    corpus: list[str] = []

    valid_points: list[Any] = []

    for point in points:
        payload = point.payload

        if payload is None:
            continue

        corpus.append(str(payload["content"]))

        valid_points.append(point)

    tokenized_corpus = [doc.lower().split() for doc in corpus]

    bm25 = BM25Okapi(tokenized_corpus)

    scores = bm25.get_scores(query.lower().split())

    ranked_results = sorted(
        zip(valid_points, scores),
        key=lambda x: x[1],
        reverse=True,
    )

    return ranked_results[:top_k]

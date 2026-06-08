from rank_bm25 import BM25Okapi

from qdrant_client import QdrantClient


client = QdrantClient(
    host="localhost",
    port=6333,
)


def bm25_search(
    query: str,
    top_k: int = 10,
):

    points, _ = client.scroll(
        collection_name="research_navigator",
        limit=10000,
        with_payload=True,
    )

    corpus = [
        point.payload["content"]
        for point in points
    ]

    tokenized_corpus = [
        doc.lower().split()
        for doc in corpus
    ]

    bm25 = BM25Okapi(
        tokenized_corpus
    )

    tokenized_query = (
        query.lower().split()
    )

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked_results = sorted(
        zip(points, scores),
        key=lambda x: x[1],
        reverse=True,
    )

    return ranked_results[:top_k]
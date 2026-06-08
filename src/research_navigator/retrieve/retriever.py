from qdrant_client import QdrantClient

from research_navigator.ingest.embeddings import embed

from research_navigator.retrieve.query_understanding import (
    understand_query,
)

from research_navigator.retrieve.filter_builder import (
    build_filter,
)


client = QdrantClient(
    host="localhost",
    port=6333,
)


def retrieve(
    query: str,
    k: int = 5,
    min_score: float = 0.55,
):

    query_vector = embed(
        query
    ).tolist()

    filters = understand_query(
        query
    )

    qdrant_filter = build_filter(
        filters
    )

    results = client.query_points(
        collection_name="research_navigator",
        query=query_vector,
        query_filter=qdrant_filter,
        limit=50,
    )

    if len(results.points) == 0:
        return []

    unique_results = []

    seen_doc_ids = set()

    for point in results.points:

        doc_id = point.payload[
            "doc_id"
        ]

        if doc_id in seen_doc_ids:
            continue

        seen_doc_ids.add(
            doc_id
        )

        unique_results.append(
            point
        )

        if len(unique_results) >= k:
            break

    if len(unique_results) == 0:
        return []

    if (
        unique_results[0].score
        < min_score
    ):
        return []

    return unique_results
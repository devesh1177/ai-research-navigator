from typing import Any

from qdrant_client import QdrantClient

from research_navigator.config.settings import (
    settings,
)

from research_navigator.ingest.embeddings import (
    embed,
)

from research_navigator.retrieve.filter_builder import (
    build_filter,
)

from research_navigator.retrieve.query_understanding import (
    understand_query,
)


client = QdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port,
)


def retrieve(
    query: str,
    k: int = 5,
    min_score: float | None = None,
) -> list[Any]:

    if min_score is None:
        min_score = settings.retrieval_min_score

    query_vector = embed(query).tolist()

    filters = understand_query(query)

    qdrant_filter = build_filter(filters)

    results = client.query_points(
        collection_name=settings.collection_name,
        query=query_vector,
        query_filter=qdrant_filter,
        limit=50,
    )

    if len(results.points) == 0:
        return []

    unique_results: list[Any] = []

    seen_doc_ids: set[str] = set()

    for point in results.points:
        payload = point.payload

        if payload is None:
            continue

        doc_id = str(payload["doc_id"])

        if doc_id in seen_doc_ids:
            continue

        seen_doc_ids.add(doc_id)

        unique_results.append(point)

        if len(unique_results) >= k:
            break

    if not unique_results:
        return []

    if unique_results[0].score < min_score:
        return []

    return unique_results

from research_navigator.retrieve.query_understanding import (
    understand_query,
)

from research_navigator.retrieve.filter_builder import (
    build_filter,
)


def test_filter_builder() -> None:

    query = "recent work on RAG"

    filters = understand_query(
        query,
    )

    qdrant_filter = build_filter(
        filters,
    )

    assert qdrant_filter is not None

from research_navigator.retrieve.query_understanding import (
    understand_query,
)

from research_navigator.retrieve.filter_builder import (
    build_filter,
)

query = "recent work on RAG"

filters = understand_query(query)

qdrant_filter = build_filter(filters)

print(qdrant_filter)

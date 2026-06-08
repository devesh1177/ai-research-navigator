from research_navigator.retrieve.query_understanding import (
    understand_query,
)

filters = understand_query("recent RAG papers")

print(filters)

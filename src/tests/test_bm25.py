from research_navigator.retrieve.bm25_retriever import (
    bm25_search,
)

results = bm25_search("recent rag papers")

for point, score in results:
    print()

    print(point.payload["title"])

    print(round(score, 4))

from research_navigator.retrieve.retriever import (
    retrieve,
)

results = retrieve(
    "Attention Is All You Need",
    k=5,
    min_score=0.0,
)

print("Results:", len(results))

for r in results:
    print(
        r.payload["title"],
        r.score,
    )

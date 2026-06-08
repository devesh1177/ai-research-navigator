from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

results = hybrid_retrieve(
    "Attention Is All You Need",
    k=5,
)

print("Results:", len(results))

for r in results:
    print(r.payload["title"])

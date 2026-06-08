from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

query = "recent rag papers"

results = hybrid_retrieve(query)

print()

print("Query:")
print(query)

for idx, result in enumerate(
    results,
    start=1,
):
    print()

    print(f"Result {idx}")

    print(result.payload["title"])

    print(result.payload["year"])

    print(result.payload["tags"])

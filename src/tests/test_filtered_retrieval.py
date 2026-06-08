from research_navigator.retrieve.retriever import retrieve

query = "recent RAG papers"

print("\nQuery:")
print(query)

results = retrieve(query)

for result in results:

    print("\nTitle:")
    print(result.payload["title"])

    print("\nYear:")
    print(result.payload["year"])

    print("\nTags:")
    print(result.payload["tags"])

    print("\nScore:")
    print(round(result.score, 4))

    print("-" * 50)
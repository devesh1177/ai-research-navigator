from research_navigator.retrieve.retriever import retrieve

query = "What is transformer architecture?"

print("\nQuery:")
print(query)

results = retrieve(query)

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")

    print("Title:")
    print(result.payload["title"])

    print("\nSection:")
    print(result.payload["section_title"])

    print("\nScore:")
    print(round(result.score, 4))

    print("\nPreview:")
    print(result.payload["content"][:200])

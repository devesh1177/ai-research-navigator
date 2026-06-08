from research_navigator.retrieve.query_understanding import (
    understand_query,
)

queries = [

    "recent work on RAG",

    "How does LoRA work?",

    "Recent GraphRAG papers",

    "What is DeepSeek-R1?",

]

for query in queries:

    print("\nQuery:")
    print(query)

    print("\nFilters:")
    print(
        understand_query(query)
    )

    print("-" * 50)
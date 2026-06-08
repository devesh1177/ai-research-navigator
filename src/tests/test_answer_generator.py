from research_navigator.retrieve.retriever import (
    retrieve,
)

from research_navigator.generate.answer_generator import (
    generate_answer,
)

query = "recent RAG papers"

results = retrieve(query)

answer = generate_answer(
    query,
    results,
)

print(answer)

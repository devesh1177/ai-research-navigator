from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

from research_navigator.generate.answer_generator import (
    generate_answer,
)

queries = [
    "What is RAG?",
    "Explain LoRA",
    "Compare LoRA vs ReAct",
]

token_counts = []

for query in queries:
    results = hybrid_retrieve(
        query,
        k=5,
    )

    answer = generate_answer(
        query,
        results,
    )

    tokens = len(answer.split())

    token_counts.append(tokens)

    print(
        query,
        "->",
        tokens,
        "tokens",
    )

average = sum(token_counts) / len(token_counts)

print(
    "\nAverage Tokens:",
    round(average, 2),
)

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

queries = [
    "Who won FIFA 2022?",
    "Capital of Japan?",
    "Chocolate cake recipe",
    "Weather in London?",
]

correct = 0

for query in queries:
    results = hybrid_retrieve(
        query,
        k=5,
    )

    refused = len(results) == 0

    if refused:
        correct += 1

    print(
        query,
        "->",
        "REFUSED" if refused else "ANSWERED",
    )

accuracy = correct / len(queries)

print(
    "\nRefusal Accuracy:",
    accuracy,
)

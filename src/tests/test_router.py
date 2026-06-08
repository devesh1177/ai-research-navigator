from research_navigator.agents.router import (
    router_node,
)

from research_navigator.agents.state import (
    NavigatorState,
)

queries = [
    "What is RAG?",
    "Explain LoRA",
    "Compare LoRA vs QLoRA",
    "Recent RAG papers",
    "Recommend papers on agents",
    "Who won the FIFA World Cup?",
]

for query in queries:
    state: NavigatorState = {
        "query": query,
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = router_node(state)

    print(f"{query} --> {result['route']}")

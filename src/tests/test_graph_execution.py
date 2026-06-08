from research_navigator.agents.graph import (
    research_graph,
)

state = {
    "query": "What is RAG?",
    "route": "",
    "answer": "",
    "citations": [],
    "metadata": {},
}

result = research_graph.invoke(state)

print("Route:", result["route"])

print()

print(result["answer"])

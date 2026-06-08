from research_navigator.agents.nodes.concept_explanation import (
    concept_explanation_node,
)

from research_navigator.agents.state import (
    NavigatorState,
)

state: NavigatorState = {
    "query": "What is RAG?",
    "route": "concept_explanation",
    "answer": "",
    "citations": [],
    "metadata": {},
}

result = concept_explanation_node(state)

print(result["answer"])

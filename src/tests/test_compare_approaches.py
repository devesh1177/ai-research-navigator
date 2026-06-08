from research_navigator.agents.nodes.compare_approaches import (
    compare_approaches_node,
)

from research_navigator.agents.state import (
    NavigatorState,
)

state: NavigatorState = {
    "query": "Compare LoRA vs ReAct",
    "route": "compare_approaches",
    "answer": "",
    "citations": [],
    "metadata": {},
}

result = compare_approaches_node(state)

print(result["answer"])

from research_navigator.agents.nodes.fallback import (
    fallback_node,
)

from research_navigator.agents.state import (
    NavigatorState,
)

state: NavigatorState = {
    "query": "Who won the FIFA World Cup?",
    "route": "out_of_scope",
    "answer": "",
    "citations": [],
    "metadata": {},
}

result = fallback_node(state)

print(result["answer"])

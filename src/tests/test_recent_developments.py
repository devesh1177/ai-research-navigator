from research_navigator.agents.nodes.recent_developments import (
    recent_developments_node,
)

from research_navigator.agents.state import (
    NavigatorState,
)

state: NavigatorState = {
    "query": "recent rag papers",
    "route": "recent_developments",
    "answer": "",
    "citations": [],
    "metadata": {},
}

result = recent_developments_node(state)

print(result["answer"])

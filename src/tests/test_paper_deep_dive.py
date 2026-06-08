from research_navigator.agents.nodes.paper_deep_dive import (
    paper_deep_dive_node,
)

from research_navigator.agents.state import (
    NavigatorState,
)

state: NavigatorState = {
    "query": "Explain Attention Is All You Need",
    "route": "paper_deep_dive",
    "answer": "",
    "citations": [],
    "metadata": {},
}

result = paper_deep_dive_node(state)

print(result["answer"])

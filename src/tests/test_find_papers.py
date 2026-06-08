from research_navigator.agents.nodes.find_papers import (
    find_papers_node,
)

from research_navigator.agents.state import (
    NavigatorState,
)


state: NavigatorState = {
    "query": "recommend papers on agents",
    "route": "find_papers",
    "answer": "",
    "citations": [],
    "metadata": {},
}

result = find_papers_node(state)

print(result["answer"])

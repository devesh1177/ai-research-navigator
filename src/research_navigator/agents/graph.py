from langgraph.graph import (
    StateGraph,
    END,
)

from research_navigator.agents.state import (
    NavigatorState,
)

from research_navigator.agents.router import (
    router_node,
)

from research_navigator.agents.nodes.concept_explanation import (
    concept_explanation_node,
)

from research_navigator.agents.nodes.paper_deep_dive import (
    paper_deep_dive_node,
)

from research_navigator.agents.nodes.compare_approaches import (
    compare_approaches_node,
)

from research_navigator.agents.nodes.recent_developments import (
    recent_developments_node,
)

from research_navigator.agents.nodes.find_papers import (
    find_papers_node,
)

from research_navigator.agents.nodes.fallback import (
    fallback_node,
)


graph = StateGraph(NavigatorState)

# Nodes

graph.add_node(
    "router",
    router_node,
)

graph.add_node(
    "concept_explanation",
    concept_explanation_node,
)

graph.add_node(
    "paper_deep_dive",
    paper_deep_dive_node,
)

graph.add_node(
    "compare_approaches",
    compare_approaches_node,
)

graph.add_node(
    "recent_developments",
    recent_developments_node,
)

graph.add_node(
    "find_papers",
    find_papers_node,
)

graph.add_node(
    "fallback",
    fallback_node,
)

# Entry

graph.set_entry_point("router")

# Conditional Routing

graph.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "concept_explanation": "concept_explanation",
        "paper_deep_dive": "paper_deep_dive",
        "compare_approaches": "compare_approaches",
        "recent_developments": "recent_developments",
        "find_papers": "find_papers",
        "out_of_scope": "fallback",
    },
)

# End Edges

graph.add_edge(
    "concept_explanation",
    END,
)

graph.add_edge(
    "paper_deep_dive",
    END,
)

graph.add_edge(
    "compare_approaches",
    END,
)

graph.add_edge(
    "recent_developments",
    END,
)

graph.add_edge(
    "find_papers",
    END,
)

graph.add_edge(
    "fallback",
    END,
)

research_graph = graph.compile()

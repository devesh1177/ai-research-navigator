from research_navigator.agents.state import (
    NavigatorState,
)


def router_node(
    state: NavigatorState,
) -> NavigatorState:

    query = state["query"].lower()

    # Compare Approaches

    if "compare" in query or "vs" in query or "difference" in query:
        state["route"] = "compare_approaches"

    # Paper Deep Dive

    elif any(
        paper in query
        for paper in [
            "attention is all you need",
            "bert",
            "lora",
            "react",
            "llama 2",
            "deepseek-r1",
            "mixtral",
        ]
    ):
        state["route"] = "paper_deep_dive"

    # Recent Developments

    elif "recent" in query or "latest" in query or "new" in query:
        state["route"] = "recent_developments"

    # Find Papers

    elif "papers" in query or "reading list" in query or "recommend" in query:
        state["route"] = "find_papers"

    # Concept Explanation

    elif any(
        phrase in query
        for phrase in [
            "what is",
            "explain",
            "how does",
            "how do",
        ]
    ):
        state["route"] = "concept_explanation"

    else:
        state["route"] = "out_of_scope"

    return state

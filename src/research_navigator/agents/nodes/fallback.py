from research_navigator.agents.state import (
    NavigatorState,
)


def fallback_node(
    state: NavigatorState,
) -> NavigatorState:

    state["answer"] = (
        "I don't have enough relevant material "
        "in the research corpus to answer that "
        "question confidently."
    )

    return state

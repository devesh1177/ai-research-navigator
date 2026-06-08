from research_navigator.agents.state import (
    NavigatorState,
)

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)


def compare_approaches_node(
    state: NavigatorState,
) -> NavigatorState:

    query = state["query"]

    results = hybrid_retrieve(
        query,
        k=10,
    )

    if not results:
        state["answer"] = "I couldn't find enough information to compare these approaches."

        return state

    answer_lines = []

    answer_lines.append(f"Comparison: {query}")

    answer_lines.append("")

    for result in results:
        payload = result.payload

        answer_lines.append(f"Title: {payload['title']}")

        answer_lines.append(f"Year: {payload['year']}")

        answer_lines.append(f"Category: {payload.get('primary_category', 'N/A')}")

        answer_lines.append(f"Section: {payload['section_title']}")

        answer_lines.append("-" * 50)

    state["answer"] = "\n".join(answer_lines)

    return state

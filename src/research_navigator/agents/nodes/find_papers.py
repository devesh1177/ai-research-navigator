from research_navigator.agents.state import (
    NavigatorState,
)

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)


def find_papers_node(
    state: NavigatorState,
) -> NavigatorState:

    query = state["query"]

    results = hybrid_retrieve(
        query,
        k=15,
    )

    if not results:
        state["answer"] = "No suitable papers found."

        return state

    seen_titles = set()

    lines = []

    lines.append(f"Recommended Reading List: {query}")

    lines.append("")

    for result in results:
        payload = result.payload

        title = payload["title"]

        if title in seen_titles:
            continue

        seen_titles.add(title)

        year = payload.get(
            "year",
            "Unknown",
        )

        category = payload.get(
            "primary_category",
            "N/A",
        )

        lines.append(f"- {title}")

        lines.append(f"  Year: {year}")

        lines.append(f"  Category: {category}")

        lines.append("")

    state["answer"] = "\n".join(lines)

    return state

from research_navigator.agents.state import (
    NavigatorState,
)

from research_navigator.agents.tools import (
    get_recent_year_cutoff,
)

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)


def recent_developments_node(
    state: NavigatorState,
) -> NavigatorState:

    query = state["query"]

    cutoff_year = get_recent_year_cutoff()

    results = hybrid_retrieve(
        query,
        k=15,
    )

    recent_results = []

    seen_titles = set()

    for result in results:
        payload = result.payload

        year = payload.get(
            "year",
            0,
        )

        title = payload["title"]

        if year < cutoff_year:
            continue

        if title in seen_titles:
            continue

        seen_titles.add(title)

        recent_results.append(payload)

    recent_results.sort(
        key=lambda x: x["year"],
        reverse=True,
    )

    if not recent_results:
        state["answer"] = "No recent developments found."

        return state

    lines = []

    lines.append(f"Recent Developments: {query}")

    lines.append("")

    for item in recent_results:
        lines.append(f"{item['year']} - {item['title']}")

    state["answer"] = "\n".join(lines)

    return state

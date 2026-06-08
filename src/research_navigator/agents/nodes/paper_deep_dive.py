from research_navigator.agents.state import (
    NavigatorState,
)

from research_navigator.agents.tools import (
    lookup_paper,
)

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

from research_navigator.generate.answer_generator import (
    generate_answer,
)


def paper_deep_dive_node(
    state: NavigatorState,
) -> NavigatorState:

    query = state["query"]

    paper_title = lookup_paper(query)

    if not paper_title:
        state["answer"] = "I could not identify the paper."

        return state

    results = hybrid_retrieve(
        paper_title,
        k=15,
    )

    # Keep only chunks from that paper

    paper_results = []

    for result in results:
        if result.payload["title"] == paper_title:
            paper_results.append(result)

    if not paper_results:
        state["answer"] = "I couldn't find enough information about that paper."

        return state

    answer = generate_answer(
        query,
        paper_results,
    )

    state["answer"] = answer

    state["metadata"] = {
        "paper": paper_title,
    }

    return state

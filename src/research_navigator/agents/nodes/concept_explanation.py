from research_navigator.agents.state import (
    NavigatorState,
)

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

from research_navigator.generate.answer_generator import (
    generate_answer,
)


def concept_explanation_node(
    state: NavigatorState,
) -> NavigatorState:

    query = state["query"]

    results = hybrid_retrieve(
        query,
        k=5,
    )

    if not results:
        state["answer"] = (
            "I don't have enough relevant material in the corpus to answer this confidently."
        )

        return state

    answer = generate_answer(
        query,
        results,
    )

    state["answer"] = answer

    return state

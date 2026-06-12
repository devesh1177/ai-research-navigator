from research_navigator.agents.nodes.concept_explanation import (
    concept_explanation_node,
)


def test_concept_explanation_no_results(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.concept_explanation.hybrid_retrieve",
        lambda query, k=5: [],
    )

    state = {
        "query": "What is RAG?",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = concept_explanation_node(state)

    assert "don't have enough relevant material" in result["answer"]


def test_concept_explanation_success(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.concept_explanation.hybrid_retrieve",
        lambda query, k=5: ["dummy"],
    )

    monkeypatch.setattr(
        "research_navigator.agents.nodes.concept_explanation.generate_answer",
        lambda query, results: "Mock Answer",
    )

    state = {
        "query": "What is RAG?",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = concept_explanation_node(state)

    assert result["answer"] == "Mock Answer"

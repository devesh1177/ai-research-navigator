from research_navigator.agents.nodes.compare_approaches import (
    compare_approaches_node,
)


class MockResult:
    def __init__(self) -> None:
        self.payload = {
            "title": "LoRA",
            "year": 2021,
            "primary_category": "cs.CL",
            "section_title": "Introduction",
        }


def test_compare_approaches_success(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.compare_approaches.hybrid_retrieve",
        lambda query, k=10: [MockResult()],
    )

    state = {
        "query": "Compare LoRA vs ReAct",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = compare_approaches_node(state)

    assert "Comparison" in result["answer"]


def test_compare_approaches_no_results(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.compare_approaches.hybrid_retrieve",
        lambda query, k=10: [],
    )

    state = {
        "query": "Compare LoRA vs ReAct",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = compare_approaches_node(state)

    assert "couldn't find enough information" in result["answer"]

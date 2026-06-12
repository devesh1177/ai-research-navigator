from research_navigator.agents.nodes.paper_deep_dive import (
    paper_deep_dive_node,
)


class MockResult:
    def __init__(self) -> None:
        self.payload = {
            "title": "LoRA: Low-Rank Adaptation of Large Language Models",
        }


def test_unknown_paper(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.paper_deep_dive.lookup_paper",
        lambda query: None,
    )

    state = {
        "query": "Explain Unknown Paper",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = paper_deep_dive_node(state)

    assert "could not identify" in result["answer"]


def test_no_matching_chunks(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.paper_deep_dive.lookup_paper",
        lambda query: "LoRA: Low-Rank Adaptation of Large Language Models",
    )

    monkeypatch.setattr(
        "research_navigator.agents.nodes.paper_deep_dive.hybrid_retrieve",
        lambda query, k=15: [],
    )

    state = {
        "query": "Explain LoRA",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = paper_deep_dive_node(state)

    assert "couldn't find enough information" in result["answer"]

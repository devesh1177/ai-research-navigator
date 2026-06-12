from research_navigator.agents.nodes.find_papers import (
    find_papers_node,
)


class MockResult:
    def __init__(self) -> None:
        self.payload = {
            "title": "LoRA",
            "year": 2021,
            "primary_category": "cs.CL",
        }


def test_find_papers_success(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.find_papers.hybrid_retrieve",
        lambda query, k=15: [MockResult()],
    )

    state = {
        "query": "Recommend papers on LoRA",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = find_papers_node(state)

    assert "Recommended Reading List" in result["answer"]


def test_find_papers_empty(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.find_papers.hybrid_retrieve",
        lambda query, k=15: [],
    )

    state = {
        "query": "Recommend papers",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = find_papers_node(state)

    assert "No suitable papers found" in result["answer"]

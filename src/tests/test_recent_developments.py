from research_navigator.agents.nodes.recent_developments import (
    recent_developments_node,
)


class MockResult:
    def __init__(self) -> None:
        self.payload = {
            "title": "DeepSeek-R1",
            "year": 2025,
        }


def test_recent_developments_success(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.recent_developments.get_recent_year_cutoff",
        lambda: 2022,
    )

    monkeypatch.setattr(
        "research_navigator.agents.nodes.recent_developments.hybrid_retrieve",
        lambda query, k=15: [MockResult()],
    )

    state = {
        "query": "Recent reasoning papers",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = recent_developments_node(state)

    assert "Recent Developments" in result["answer"]


def test_recent_developments_empty(monkeypatch) -> None:

    monkeypatch.setattr(
        "research_navigator.agents.nodes.recent_developments.get_recent_year_cutoff",
        lambda: 2030,
    )

    monkeypatch.setattr(
        "research_navigator.agents.nodes.recent_developments.hybrid_retrieve",
        lambda query, k=15: [MockResult()],
    )

    state = {
        "query": "Recent reasoning papers",
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = recent_developments_node(state)

    assert "No recent developments found" in result["answer"]

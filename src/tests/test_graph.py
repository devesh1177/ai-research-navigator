# src/tests/test_graph.py

from research_navigator.agents.graph import (
    research_graph,
)


def test_graph_exists() -> None:

    assert research_graph is not None

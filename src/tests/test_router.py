from research_navigator.agents.router import router_node
from research_navigator.agents.state import NavigatorState


def build_state(query: str) -> NavigatorState:
    return {
        "query": query,
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }


def test_concept_route() -> None:
    result = router_node(build_state("What is RAG?"))

    assert result["route"] == "concept_explanation"


def test_paper_route() -> None:
    result = router_node(build_state("Explain LoRA"))

    assert result["route"] == "paper_deep_dive"


def test_compare_route() -> None:
    result = router_node(build_state("Compare LoRA vs QLoRA"))

    assert result["route"] == "compare_approaches"


def test_recent_route() -> None:
    result = router_node(build_state("Recent RAG papers"))

    assert result["route"] == "recent_developments"


def test_find_papers_route() -> None:
    result = router_node(build_state("Recommend papers on agents"))

    assert result["route"] == "find_papers"


def test_out_of_scope_route() -> None:
    result = router_node(build_state("Who won FIFA World Cup?"))

    assert result["route"] == "out_of_scope"

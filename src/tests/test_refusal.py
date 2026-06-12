from research_navigator.retrieve.retriever import (
    retrieve,
)


def test_out_of_scope_refusal() -> None:

    query = "Who won the FIFA World Cup in 1998?"

    results = retrieve(
        query,
    )

    assert results == []

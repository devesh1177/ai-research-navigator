from research_navigator.retrieve.query_understanding import (
    understand_query,
)


def test_recent_query() -> None:
    filters = understand_query("recent work on RAG")

    assert filters is not None


def test_lora_query() -> None:
    filters = understand_query("How does LoRA work?")

    assert filters is not None


def test_graphrag_query() -> None:
    filters = understand_query("Recent GraphRAG papers")

    assert filters is not None


def test_deepseek_query() -> None:
    filters = understand_query("What is DeepSeek-R1?")

    assert filters is not None

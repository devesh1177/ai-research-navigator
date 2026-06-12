from research_navigator.generate.answer_generator import (
    generate_answer,
)


class MockResult:
    def __init__(self) -> None:
        self.payload = {
            "doc_id": "1",
            "title": "Attention Is All You Need",
            "year": 2017,
            "section_title": "Introduction",
            "content_type": "arxiv_paper",
        }


def test_generate_answer_with_results() -> None:

    results = [MockResult()]

    answer = generate_answer(
        "What is a transformer?",
        results,
    )

    assert "Transformer architecture" in answer
    assert "References" in answer


def test_generate_answer_no_results() -> None:

    answer = generate_answer(
        "Unknown question",
        [],
    )

    assert "don't have enough relevant material" in answer

from research_navigator.agents.tools import (
    lookup_paper,
    get_recent_year_cutoff,
)


def test_lookup_paper_found() -> None:

    result = lookup_paper(
        "Explain LoRA paper",
    )

    assert result is not None
    assert "LoRA" in result


def test_lookup_paper_not_found() -> None:

    result = lookup_paper(
        "Explain random paper",
    )

    assert result is None


def test_recent_year_cutoff() -> None:

    cutoff = get_recent_year_cutoff()

    assert isinstance(
        cutoff,
        int,
    )

from typing import Any

from research_navigator.generate.citation_builder import (
    build_citations,
)


def generate_answer(
    query: str,
    results: list[Any],
) -> str:

    if not results:
        return (
            "I don't have enough relevant "
            "material in the corpus to "
            "answer this confidently."
        )

    citations = build_citations(
        results,
    )

    citation_lookup: dict[
        str,
        int,
    ] = {}

    for citation in citations:
        citation_lookup[str(citation["doc_id"])] = int(citation["citation_id"])

    answer_lines: list[str] = []

    answer_lines.append(f"Question: {query}\n")

    answer_lines.append("Answer:\n")

    for result in results:
        payload = result.payload

        title = str(payload["title"])

        citation_id = citation_lookup[str(payload["doc_id"])]

        if "Attention Is All You Need" in title:
            answer_lines.append(
                "The Transformer "
                "architecture replaces "
                "recurrence with "
                "self-attention "
                f"mechanisms. [{citation_id}]"
            )

        elif "LoRA" in title:
            answer_lines.append(
                "LoRA enables efficient "
                "fine-tuning using "
                "low-rank adaptation "
                f"matrices. [{citation_id}]"
            )

        elif "BERT" in title:
            answer_lines.append(
                "BERT introduced "
                "bidirectional "
                "pretraining for "
                "language understanding. "
                f"[{citation_id}]"
            )

        else:
            answer_lines.append(
                f"The document '{title}' "
                f"contains information "
                f"relevant to the query. "
                f"[{citation_id}]"
            )

    answer_lines.append("")
    answer_lines.append("References")
    answer_lines.append("")

    for citation in citations:
        answer_lines.append(
            (
                f"[{citation['citation_id']}] "
                f"{citation['title']} "
                f"({citation['year']}) "
                f"- Section: "
                f"{citation['section']}"
            )
        )

    return "\n".join(answer_lines)

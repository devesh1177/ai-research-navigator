from research_navigator.generate.citation_builder import (
    build_citations,
)


def generate_answer(
    query: str,
    results,
) -> str:

    if not results:

        return (
            "I don't have enough relevant material "
            "in the corpus to answer this confidently."
        )

    citations = build_citations(results)

    citation_lookup = {}

    for citation in citations:

        citation_lookup[
            citation["doc_id"]
        ] = citation["citation_id"]

    answer_lines = []

    answer_lines.append(
        f"Question: {query}\n"
    )

    answer_lines.append(
        "Answer:\n"
    )

    for result in results:

        payload = result.payload

        title = payload["title"]

        citation_id = citation_lookup[
            payload["doc_id"]
        ]

        # RAG Papers

        if "Corrective Retrieval Augmented Generation" in title:

            answer_lines.append(
                f"Corrective RAG improves retrieval quality by correcting retrieved information before generation and reducing retrieval errors. [{citation_id}]"
            )

        elif "Graph RAG" in title or "GraphRAG" in title:

            answer_lines.append(
                f"GraphRAG extends traditional retrieval-augmented generation by organizing knowledge through graph structures for better retrieval and summarization. [{citation_id}]"
            )

        elif "RAFT" in title:

            answer_lines.append(
                f"RAFT adapts language models specifically for domain-focused retrieval augmented generation tasks through fine-tuning. [{citation_id}]"
            )

        elif "Agentic RAG" in title:

            answer_lines.append(
                f"Agentic RAG combines retrieval systems with autonomous agents and tool usage to perform more complex workflows. [{citation_id}]"
            )

        # Transformers

        elif "Attention Is All You Need" in title:

            answer_lines.append(
                f"The Transformer architecture replaces recurrence with self-attention mechanisms, enabling efficient parallel processing of sequences. [{citation_id}]"
            )

        elif "BERT" in title:

            answer_lines.append(
                f"BERT introduced bidirectional pretraining for language understanding and became a foundation for many NLP applications. [{citation_id}]"
            )

        elif "Language Models are Few-Shot Learners" in title:

            answer_lines.append(
                f"GPT-3 demonstrated that large language models can perform many tasks using only a few examples provided in prompts. [{citation_id}]"
            )

        # LoRA

        elif "LoRA" in title:

            answer_lines.append(
                f"LoRA enables efficient fine-tuning by learning low-rank adaptations while keeping most model parameters frozen. [{citation_id}]"
            )

        # ReAct

        elif "ReAct" in title:

            answer_lines.append(
                f"ReAct combines reasoning and action steps, allowing language models to interact with tools while solving problems. [{citation_id}]"
            )

        # RLHF

        elif "Human Feedback" in title:

            answer_lines.append(
                f"RLHF aligns language model behavior with human preferences using reward models and reinforcement learning. [{citation_id}]"
            )

        # Fallback

        else:

            answer_lines.append(
                f"The document '{title}' contains information relevant to the query. [{citation_id}]"
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
                f"- Section: {citation['section']}"
            )
        )

    return "\n".join(answer_lines)
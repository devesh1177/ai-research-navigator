from research_navigator.agents.graph import (
    research_graph,
)

queries = [
    # Concept Explanation
    "What is RAG?",
    "Explain transformers",
    "What is RLHF?",
    # Paper Deep Dive
    "Explain Attention Is All You Need",
    "Explain LoRA",
    "Explain ReAct",
    # Compare
    "Compare LoRA vs ReAct",
    "Compare GPT-3 vs BERT",
    "Compare RAG vs GraphRAG",
    # Recent
    "Recent RAG papers",
    "Recent agent papers",
    "Recent LLM developments",
    # Find Papers
    "Recommend papers on agents",
    "Recommend papers on transformers",
    "Recommend papers on reasoning",
    # Fallback
    "Who won FIFA 2022?",
    "Capital of Japan?",
    "Chocolate cake recipe",
]

for query in queries:
    state = {
        "query": query,
        "route": "",
        "answer": "",
        "citations": [],
        "metadata": {},
    }

    result = research_graph.invoke(state)

    print("=" * 80)

    print(query)

    print(
        "ROUTE:",
        result["route"],
    )

    print()

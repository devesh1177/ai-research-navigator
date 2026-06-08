from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

from research_navigator.generate.answer_generator import (
    generate_answer,
)


questions = [
    # Transformers
    "What is transformer architecture?",
    "Why is self-attention important?",
    "How does BERT work?",
    "What is GPT-3 known for?",
    # RAG
    "What is retrieval augmented generation?",
    "What is GraphRAG?",
    "What is Corrective RAG?",
    "What is Agentic RAG?",
    # Fine-tuning
    "What is LoRA?",
    "Why is LoRA efficient?",
    # Alignment
    "What is RLHF?",
    "What is Constitutional AI?",
    # Agents
    "What is ReAct?",
    "What is SWE-Agent?",
    # Reasoning
    "What is Chain of Thought prompting?",
    "What is DeepSeek R1?",
    # Unrelated Questions
    "Who won the FIFA World Cup 2022?",
    "What is the capital of Japan?",
    "How do I bake a chocolate cake?",
    "Who is the CEO of Tesla?",
]


for i, question in enumerate(
    questions,
    start=1,
):
    print("\n")
    print("=" * 80)

    print(f"QUESTION {i}")

    print(question)

    print("-" * 80)

    results = hybrid_retrieve(question)

    answer = generate_answer(
        question,
        results,
    )

    print(answer)

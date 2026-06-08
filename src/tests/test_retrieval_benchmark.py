from research_navigator.retrieve.retriever import retrieve


questions = [
    # Related Questions
    "What problem does the Transformer architecture solve compared to RNNs?",
    "How does self-attention work in Transformer models?",
    "What are the three main Transformer architectures?",
    "What is BERT and how is it trained?",
    "What is Retrieval-Augmented Generation (RAG)?",
    "How does LoRA reduce the cost of fine-tuning large language models?",
    "What is Chain-of-Thought prompting?",
    "What is Reinforcement Learning from Human Feedback (RLHF)?",
    "What is the ReAct framework?",
    "How does Constitutional AI differ from RLHF?",
    "What are Mixture of Experts (MoE) models?",
    "What innovations were introduced in Llama 3?",
    "What is DeepSeek-R1 and how does it improve reasoning?",
    "What is GraphRAG and how does it differ from traditional RAG?",
    "What challenges do long-context language models face?",
    "What is FlashAttention and why is it important?",
    # Unrelated Questions
    "What is the capital of Australia?",
    "How do plants perform photosynthesis?",
    "Who was the first person to walk on the Moon?",
    "What is the recipe for chicken biryani?",
]


for question in questions:
    print("\n" + "=" * 80)

    print("QUESTION:")
    print(question)

    results = retrieve(
        question,
        k=1,
    )

    if not results:
        print("\nNO RELEVANT RESULT FOUND")
        continue

    result = results[0]

    print("\nANSWER EXTRACT:")
    print(result.payload["content"][:500])

    print("\nSCORE:")
    print(round(result.score, 4))

    print("\nSOURCE PAPER:")
    print(result.payload["title"])

    print("\nSECTION:")
    print(result.payload["section_title"])

print("\n" + "=" * 80)
print("BENCHMARK COMPLETE")

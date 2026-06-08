def understand_query(query: str) -> dict:

    query_lower = query.lower()

    filters = {
        "year_gte": None,
        "tags": [],
    }

    # -----------------------------
    # Recency Detection
    # -----------------------------

    recent_keywords = [
        "recent",
        "latest",
        "new",
        "current",
        "modern",
    ]

    if any(keyword in query_lower for keyword in recent_keywords):
        filters["year_gte"] = 2023

    # -----------------------------
    # RAG
    # -----------------------------

    if "rag" in query_lower or "retrieval" in query_lower or "graphrag" in query_lower:
        filters["tags"].append("RAG")

    # -----------------------------
    # Agents
    # -----------------------------

    if (
        "agent" in query_lower
        or "agents" in query_lower
        or "tool use" in query_lower
        or "tool-use" in query_lower
    ):
        filters["tags"].append("agents")

    # -----------------------------
    # Reasoning
    # -----------------------------

    if "reasoning" in query_lower or "chain of thought" in query_lower or "cot" in query_lower:
        filters["tags"].append("reasoning")

    # -----------------------------
    # Alignment
    # -----------------------------

    if (
        "alignment" in query_lower
        or "preference" in query_lower
        or "simpo" in query_lower
        or "kto" in query_lower
    ):
        filters["tags"].append("alignment")

    # -----------------------------
    # RLHF
    # -----------------------------

    if "rlhf" in query_lower or "human feedback" in query_lower:
        filters["tags"].append("RLHF")

    # -----------------------------
    # Safety
    # -----------------------------

    if "safety" in query_lower or "harmless" in query_lower or "constitutional ai" in query_lower:
        filters["tags"].append("safety")

    # -----------------------------
    # Transformers
    # -----------------------------

    if "transformer" in query_lower or "attention" in query_lower:
        filters["tags"].append("transformers")

    # -----------------------------
    # Fine-tuning
    # -----------------------------

    if (
        "lora" in query_lower
        or "fine tuning" in query_lower
        or "fine-tuning" in query_lower
        or "adapter" in query_lower
    ):
        filters["tags"].append("fine_tuning")

    # -----------------------------
    # MoE
    # -----------------------------

    if "moe" in query_lower or "mixture of experts" in query_lower or "mixtral" in query_lower:
        filters["tags"].append("MoE")

    # -----------------------------
    # Evaluation
    # -----------------------------

    if (
        "benchmark" in query_lower
        or "evaluation" in query_lower
        or "mmlu" in query_lower
        or "arena" in query_lower
    ):
        filters["tags"].append("evaluation")

    # -----------------------------
    # Reinforcement Learning
    # -----------------------------

    if (
        "reinforcement learning" in query_lower
        or "ppo" in query_lower
        or "policy gradient" in query_lower
        or "rl" in query_lower
    ):
        filters["tags"].append("RL")

    # -----------------------------
    # Long Context
    # -----------------------------

    if (
        "long context" in query_lower
        or "context window" in query_lower
        or "million tokens" in query_lower
    ):
        filters["tags"].append("long_context")

    # -----------------------------
    # Multimodal
    # -----------------------------

    if "multimodal" in query_lower or "vision" in query_lower or "audio" in query_lower:
        filters["tags"].append("multimodal")

    # -----------------------------
    # Remove Duplicates
    # -----------------------------

    filters["tags"] = list(set(filters["tags"]))

    return filters

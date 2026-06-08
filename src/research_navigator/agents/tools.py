from datetime import datetime


KNOWN_PAPERS = {
    "attention is all you need": "Attention Is All You Need",
    "bert": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "lora": "LoRA: Low-Rank Adaptation of Large Language Models",
    "react": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "llama 2": "Llama 2: Open Foundation and Fine-Tuned Chat Models",
    "mixtral": "Mixtral of Experts",
    "deepseek-r1": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
}


def lookup_paper(
    query: str,
) -> str | None:

    query = query.lower()

    for key, value in KNOWN_PAPERS.items():
        if key in query:
            return value

    return None


def get_recent_year_cutoff() -> int:

    current_year = datetime.now().year

    return current_year - 3

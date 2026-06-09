from metrics import (
    compute_precision_at_k,
    compute_recall_at_k,
)

retrieved = [
    "Attention Is All You Need",
    "BERT",
    "LoRA",
]

expected = [
    "Attention Is All You Need",
    "LoRA",
]

print(
    "Precision:",
    compute_precision_at_k(
        retrieved,
        expected,
    ),
)

print(
    "Recall:",
    compute_recall_at_k(
        retrieved,
        expected,
    ),
)

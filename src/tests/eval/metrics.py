from typing import List


def compute_precision_at_k(
    retrieved: List[str],
    expected: List[str],
) -> float:

    if len(retrieved) == 0:
        return 0.0

    hits = len(set(retrieved) & set(expected))

    return hits / len(retrieved)


def compute_recall_at_k(
    retrieved: List[str],
    expected: List[str],
) -> float:

    if len(expected) == 0:
        return 0.0

    hits = len(set(retrieved) & set(expected))

    return hits / len(expected)

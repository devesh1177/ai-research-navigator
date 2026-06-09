import json

from research_navigator.retrieve.retriever import (
    retrieve,
)

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

from metrics import (
    compute_precision_at_k,
    compute_recall_at_k,
)


with open(
    "src/tests/eval/golden_set.json",
    "r",
    encoding="utf-8",
) as f:
    dataset = json.load(f)


dense_precisions = []
dense_recalls = []

hybrid_precisions = []
hybrid_recalls = []


for item in dataset:
    expected = item["expected_sources"]

    if not expected:
        continue

    query = item["query"]

    # -------------------
    # Dense
    # -------------------

    dense_results = retrieve(
        query,
        k=5,
        min_score=0.0,
    )

    dense_titles = []

    for point in dense_results:
        dense_titles.append(point.payload["title"])

    dense_precisions.append(
        compute_precision_at_k(
            dense_titles,
            expected,
        )
    )

    dense_recalls.append(
        compute_recall_at_k(
            dense_titles,
            expected,
        )
    )

    # -------------------
    # Hybrid
    # -------------------

    hybrid_results = hybrid_retrieve(
        query,
        k=5,
    )

    hybrid_titles = []

    for point in hybrid_results:
        hybrid_titles.append(point.payload["title"])

    hybrid_precisions.append(
        compute_precision_at_k(
            hybrid_titles,
            expected,
        )
    )

    hybrid_recalls.append(
        compute_recall_at_k(
            hybrid_titles,
            expected,
        )
    )


print("\n===== DENSE =====")

print(
    "Precision@5:",
    round(
        sum(dense_precisions) / len(dense_precisions),
        3,
    ),
)

print(
    "Recall@5:",
    round(
        sum(dense_recalls) / len(dense_recalls),
        3,
    ),
)

print("\n===== HYBRID =====")

print(
    "Precision@5:",
    round(
        sum(hybrid_precisions) / len(hybrid_precisions),
        3,
    ),
)

print(
    "Recall@5:",
    round(
        sum(hybrid_recalls) / len(hybrid_recalls),
        3,
    ),
)

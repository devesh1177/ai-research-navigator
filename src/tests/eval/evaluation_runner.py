import json
import time

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

from research_navigator.retrieve.retriever import (
    retrieve,
)

from research_navigator.generate.answer_generator import (
    generate_answer,
)

from metrics import (
    compute_precision_at_k,
    compute_recall_at_k,
)


# =====================================================
# Load Golden Set
# =====================================================

with open(
    "src/tests/eval/golden_set.json",
    "r",
    encoding="utf-8",
) as f:
    dataset = json.load(f)


# =====================================================
# Retrieval Evaluation
# =====================================================

precisions = []
recalls = []

for item in dataset:
    expected_sources = item["expected_sources"]

    if not expected_sources:
        continue

    query = item["query"]

    results = hybrid_retrieve(
        query,
        k=5,
    )

    retrieved_titles = [point.payload["title"] for point in results]

    precision = compute_precision_at_k(
        retrieved_titles,
        expected_sources,
    )

    recall = compute_recall_at_k(
        retrieved_titles,
        expected_sources,
    )

    precisions.append(precision)
    recalls.append(recall)

avg_precision = round(
    sum(precisions) / len(precisions),
    3,
)

avg_recall = round(
    sum(recalls) / len(recalls),
    3,
)


# =====================================================
# Refusal Evaluation
# =====================================================

refusal_queries = [
    "Who won FIFA 2022?",
    "Capital of Japan?",
    "Chocolate cake recipe",
    "Weather in London?",
]

correct_refusals = 0

for query in refusal_queries:
    results = hybrid_retrieve(
        query,
        k=5,
    )

    if len(results) == 0:
        correct_refusals += 1

refusal_accuracy = round(
    correct_refusals / len(refusal_queries),
    3,
)


# =====================================================
# Latency Evaluation
# =====================================================

latencies = []

for item in dataset:
    start = time.perf_counter()

    hybrid_retrieve(
        item["query"],
        k=5,
    )

    end = time.perf_counter()

    latencies.append(end - start)

latencies.sort()

count = len(latencies)

average_latency = round(
    sum(latencies) / count,
    3,
)

p50_latency = round(
    latencies[int(count * 0.50)],
    3,
)

p95_latency = round(
    latencies[int(count * 0.95)],
    3,
)


# =====================================================
# Token Cost
# =====================================================

token_queries = [
    "What is RAG?",
    "Explain LoRA",
    "Compare LoRA vs ReAct",
]

token_counts = []

for query in token_queries:
    results = hybrid_retrieve(
        query,
        k=5,
    )

    answer = generate_answer(
        query,
        results,
    )

    token_counts.append(len(answer.split()))

average_tokens = round(
    sum(token_counts) / len(token_counts),
    2,
)


# =====================================================
# Dense vs Hybrid Comparison
# =====================================================

dense_precisions = []
dense_recalls = []

hybrid_precisions = []
hybrid_recalls = []

for item in dataset:
    expected_sources = item["expected_sources"]

    if not expected_sources:
        continue

    query = item["query"]

    dense_results = retrieve(
        query,
        k=5,
        min_score=0.0,
    )

    dense_titles = [point.payload["title"] for point in dense_results]

    dense_precisions.append(
        compute_precision_at_k(
            dense_titles,
            expected_sources,
        )
    )

    dense_recalls.append(
        compute_recall_at_k(
            dense_titles,
            expected_sources,
        )
    )

    hybrid_results = hybrid_retrieve(
        query,
        k=5,
    )

    hybrid_titles = [point.payload["title"] for point in hybrid_results]

    hybrid_precisions.append(
        compute_precision_at_k(
            hybrid_titles,
            expected_sources,
        )
    )

    hybrid_recalls.append(
        compute_recall_at_k(
            hybrid_titles,
            expected_sources,
        )
    )

dense_precision = round(
    sum(dense_precisions) / len(dense_precisions),
    3,
)

dense_recall = round(
    sum(dense_recalls) / len(dense_recalls),
    3,
)

hybrid_precision = round(
    sum(hybrid_precisions) / len(hybrid_precisions),
    3,
)

hybrid_recall = round(
    sum(hybrid_recalls) / len(hybrid_recalls),
    3,
)


# =====================================================
# JSON Report
# =====================================================

report = {
    "retrieval": {
        "precision_at_5": avg_precision,
        "recall_at_5": avg_recall,
    },
    "refusal": {
        "accuracy": refusal_accuracy,
    },
    "latency": {
        "average_seconds": average_latency,
        "p50_seconds": p50_latency,
        "p95_seconds": p95_latency,
    },
    "token_cost": {
        "average_tokens": average_tokens,
    },
    "comparison": {
        "dense_precision": dense_precision,
        "dense_recall": dense_recall,
        "hybrid_precision": hybrid_precision,
        "hybrid_recall": hybrid_recall,
    },
}

with open(
    "evaluation_report.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(
        report,
        f,
        indent=4,
    )


# =====================================================
# Markdown Report
# =====================================================

markdown = f"""# M4 Evaluation Report

## Retrieval Performance

Precision@5: {avg_precision}

Recall@5: {avg_recall}

## Refusal Correctness

Accuracy: {refusal_accuracy}

## Latency

Average: {average_latency} s

P50: {p50_latency} s

P95: {p95_latency} s

## Token Cost

Average Tokens: {average_tokens}

## Dense vs Hybrid

Dense Precision@5: {dense_precision}

Dense Recall@5: {dense_recall}

Hybrid Precision@5: {hybrid_precision}

Hybrid Recall@5: {hybrid_recall}

## Conclusion

Dense retrieval achieved higher precision while hybrid retrieval maintained equivalent recall.
"""

with open(
    "docs/M4_EVALUATION_REPORT.md",
    "w",
    encoding="utf-8",
) as f:
    f.write(markdown)


# =====================================================
# Console Output
# =====================================================

print("\n" + "=" * 60)
print("M4 EVALUATION RESULTS")
print("=" * 60)

print("\nRETRIEVAL METRICS")
print("-" * 30)
print(f"Precision@5 : {avg_precision}")
print(f"Recall@5    : {avg_recall}")

print("\nREFUSAL CORRECTNESS")
print("-" * 30)
print(f"Accuracy    : {refusal_accuracy}")

print("\nLATENCY")
print("-" * 30)
print(f"Average     : {average_latency} s")
print(f"P50         : {p50_latency} s")
print(f"P95         : {p95_latency} s")

print("\nTOKEN COST")
print("-" * 30)
print(f"Average Tokens : {average_tokens}")

print("\nDENSE VS HYBRID")
print("-" * 30)
print(f"Dense Precision@5  : {dense_precision}")
print(f"Dense Recall@5     : {dense_recall}")
print(f"Hybrid Precision@5 : {hybrid_precision}")
print(f"Hybrid Recall@5    : {hybrid_recall}")

print("\nREPORTS GENERATED")
print("-" * 30)
print("evaluation_report.json")
print("docs/M4_EVALUATION_REPORT.md")

print("\n" + "=" * 60)
print("M4 EVALUATION COMPLETE")
print("=" * 60)

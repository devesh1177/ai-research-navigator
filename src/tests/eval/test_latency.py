import json
import time

from research_navigator.retrieve.hybrid_retriever import (
    hybrid_retrieve,
)

with open(
    "src/tests/eval/golden_set.json",
    "r",
    encoding="utf-8",
) as f:
    dataset = json.load(f)

latencies = []

for item in dataset:
    query = item["query"]

    start = time.perf_counter()

    hybrid_retrieve(
        query,
        k=5,
    )

    end = time.perf_counter()

    latency = end - start

    latencies.append(latency)

latencies.sort()

count = len(latencies)

p50 = latencies[int(count * 0.50)]

p95 = latencies[int(count * 0.95)]

avg = sum(latencies) / count

print(
    "Average:",
    round(avg, 3),
    "seconds",
)

print(
    "P50:",
    round(p50, 3),
    "seconds",
)

print(
    "P95:",
    round(p95, 3),
    "seconds",
)

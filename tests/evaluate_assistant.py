"""
Evaluation Suite for the ATLAS Query Assistant.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

import time
import logging
from tabulate import tabulate
import config
from llm_client import LLMClientWrapper
from query_assistant import (
    SYSTEM_PROMPT,
    extract_cypher,
    validate_cypher_safety,
    GraphExecutor,
)

GOLDEN_SET = [
    {
        "question": "Which techniques target the inference path of a RAG-based assistant?",
        "expected_labels": ["Technique", "Component"],
        "expected_relationships": ["HEURISTIC_TARGETS"],
    },
    {
        "question": "Find all mitigations owned by a Data Scientist.",
        "expected_labels": ["Mitigation", "Role"],
        "expected_relationships": ["HEURISTIC_OWNED_BY"],
    },
    {
        "question": "Show me techniques achieving the 'Model Access' tactic.",
        "expected_labels": ["Technique", "Tactic"],
        "expected_relationships": ["ACHIEVES"],
    },
]


def evaluate_assistant():
    llm = LLMClientWrapper("Ollama")
    executor = GraphExecutor()
    results = []

    print("\nStarting Evaluation...")
    for i, test in enumerate(GOLDEN_SET):
        q = test["question"]
        start = time.time()
        try:
            raw = llm.generate_completion(SYSTEM_PROMPT, q)
            cypher = extract_cypher(raw)
            success, _ = executor.execute_and_print(cypher)
            grounding = all(f":{l}" in cypher for l in test["expected_labels"]) and all(
                f":{r}" in cypher for r in test["expected_relationships"]
            )
            results.append(
                [
                    i + 1,
                    "PASS" if success else "FAIL",
                    "PASS" if grounding else "FAIL",
                    f"{time.time()-start:.2f}s",
                ]
            )
        except Exception as e:
            results.append([i + 1, "ERROR", "ERROR", "N/A"])
            print(f"Error evaluating query {i+1}: {e}")

    print("\n=== EVALUATION SUMMARY ===")
    print(
        tabulate(
            results,
            headers=["#", "Syntax", "Grounding", "Latency"],
            tablefmt="fancy_grid",
        )
    )
    executor.close()


if __name__ == "__main__":
    evaluate_assistant()

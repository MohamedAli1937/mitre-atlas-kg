"""
Advanced Evaluation Suite for the ATLAS Knowledge Graph.
Measures Latency, Grounding Accuracy, and Schema Recall (Framework Coverage).
"""

import os
import sys
import time
from tabulate import tabulate

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

import config
from llm_client import LLMClientWrapper
from query_assistant import SYSTEM_PROMPT, extract_cypher, GraphExecutor
from build_kg import AtlasIngestor

GOLDEN_SET = [
    {
        "question": "Which techniques target the inference path of a RAG-based assistant?",
        "expected_labels": ["Technique", "Component"],
        "expected_rels": ["HEURISTIC_TARGETS"],
    },
    {
        "question": "Find all mitigations owned by an Application Developer.",
        "expected_labels": ["Mitigation", "Role"],
        "expected_rels": ["HEURISTIC_OWNED_BY"],
    },
    {
        "question": "Show techniques mapped to the EU AI Act or NIST AI RMF.",
        "expected_labels": ["Technique", "NISTCategory"],
        "expected_rels": ["MAPS_TO"],
    },
]


def run_performance_eval():
    print("\n--- PERFORMANCE & GROUNDING EVALUATION ---")
    llm = LLMClientWrapper("Ollama")
    executor = GraphExecutor()
    results = []

    for i, test in enumerate(GOLDEN_SET):
        start_time = time.time()
        raw_response = llm.generate_completion(SYSTEM_PROMPT, test["question"])
        cypher = extract_cypher(raw_response)
        latency = time.time() - start_time

        # Grounding Check: Do the labels/rels exist in the generated Cypher?
        label_hit = all(f":{l}" in cypher for l in test["expected_labels"])
        rel_hit = all(f":{r}" in cypher for r in test["expected_rels"])
        grounding_score = "PASS" if (label_hit and rel_hit) else "FAIL"

        # Execution Check
        try:
            success, _ = executor.execute_and_print(cypher)
            exec_status = "SUCCESS" if success else "ERROR"
        except:
            exec_status = "CRASH"

        results.append([i + 1, f"{latency:.2f}s", grounding_score, exec_status])

    print(
        tabulate(
            results,
            headers=["#", "Latency", "Grounding", "Execution"],
            tablefmt="fancy_grid",
        )
    )
    executor.close()


def run_schema_recall_eval():
    print("\n--- SCHEMA RECALL (FRAMEWORK COVERAGE) ---")
    ingestor = AtlasIngestor(config.NEO4J_URI, config.NEO4J_USER, config.NEO4J_PASSWORD)
    stats = ingestor.get_stats()
    ingestor.close()

    total_techs = stats["Techniques"]
    unmitigated = stats["UnmitigatedTechniques"]
    mitigated = total_techs - unmitigated

    coverage_pct = (mitigated / total_techs) * 100 if total_techs > 0 else 0

    print(f"Total Techniques in Graph: {total_techs}")
    print(f"Techniques with Mitigations: {mitigated}")
    print(f"Techniques WITHOUT Mitigations: {unmitigated} (Coverage Gap)")
    print(f"ATLAS Framework Coverage Score: {coverage_pct:.2f}%")

    print("\n--- DATA SOURCE RECALL ---")
    print(f"OWASP LLM Top 10 Categories: {stats['OWASPCategories']}")
    print(f"NIST AI RMF Categories: {stats['NISTCategories']}")
    print(f"Heuristic Components (AI-Enriched): {stats['HeuristicComponents']}")


if __name__ == "__main__":
    run_schema_recall_eval()
    run_performance_eval()

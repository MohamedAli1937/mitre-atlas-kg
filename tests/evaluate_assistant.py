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
        "question": "Show techniques mapped to the NIST AI RMF.",
        "expected_labels": ["Technique", "NISTCategory"],
        "expected_rels": ["MAPS_TO"],
    },
    {
        "question": "Which OWASP risks are relevant to a developer working on RAG components?",
        "expected_labels": ["OWASPCategory", "Technique", "Component"],
        "expected_rels": ["MAPS_TO", "HEURISTIC_TARGETS"],
    },
    {
        "question": "Show techniques that specialize 'LLM Prompt Injection' and list their mitigations.",
        "expected_labels": ["Technique", "Mitigation"],
        "expected_rels": ["SPECIALIZES", "MITIGATES"],
    },
    {
        "question": "List techniques mapped to NIST Govern 1.1 that have no official mitigations.",
        "expected_labels": ["Technique", "NISTCategory"],
        "expected_rels": ["MAPS_TO"],
    },
]


def run_schema_recall_eval(verbose=True):
    ingestor = AtlasIngestor(config.NEO4J_URI, config.NEO4J_USER, config.NEO4J_PASSWORD)
    stats = ingestor.get_stats()
    ingestor.close()

    total_techs = stats["Techniques"]
    unmitigated = stats["UnmitigatedTechniques"]
    mitigated = total_techs - unmitigated
    coverage_pct = (mitigated / total_techs) * 100 if total_techs > 0 else 0

    result = {
        "total_techniques": total_techs,
        "mitigated": mitigated,
        "unmitigated": unmitigated,
        "coverage_pct": coverage_pct,
        "owasp_categories": stats["OWASPCategories"],
        "nist_categories": stats["NISTCategories"],
        "heuristic_components": stats["HeuristicComponents"],
    }

    if verbose:
        print("\n--- SCHEMA RECALL (FRAMEWORK COVERAGE) ---")
        print(f"Total Techniques in Graph: {total_techs}")
        print(f"Techniques with Mitigations: {mitigated}")
        print(f"Techniques WITHOUT Mitigations: {unmitigated} (Coverage Gap)")
        print(f"ATLAS Framework Coverage Score: {coverage_pct:.2f}%")
        print("\n--- DATA SOURCE RECALL ---")
        print(f"OWASP LLM Top 10 Categories: {stats['OWASPCategories']}")
        print(f"NIST AI RMF Categories: {stats['NISTCategories']}")
        print(f"Heuristic Components (AI-Enriched): {stats['HeuristicComponents']}")

    return result


def run_performance_eval(llm_client=None, verbose=False):
    if verbose:
        print("\n--- PERFORMANCE & GROUNDING EVALUATION ---")

    llm = llm_client or LLMClientWrapper("Ollama")
    executor = GraphExecutor()
    results = []

    for i, test in enumerate(GOLDEN_SET):
        start_time = time.time()
        raw_response = llm.generate_completion(SYSTEM_PROMPT, test["question"])
        cypher = extract_cypher(raw_response)
        latency = time.time() - start_time

        label_hit = all(f":{label}" in cypher for label in test["expected_labels"])
        rel_hit = all(f":{rel}" in cypher for rel in test["expected_rels"])
        grounding_score = "PASS" if (label_hit and rel_hit) else "FAIL"

        if verbose:
            success, _ = executor.execute_and_print(cypher)
            exec_status = "SUCCESS" if success else "ERROR"
            record_count = None
        else:
            success, error, record_count = executor.execute(cypher)
            exec_status = "SUCCESS" if success else "ERROR"
            if not success and error:
                exec_status = f"ERROR: {error}"

        results.append(
            {
                "#": i + 1,
                "question": test["question"],
                "cypher": cypher,
                "latency_s": round(latency, 2),
                "grounding": grounding_score,
                "execution": exec_status.split(":")[0],
                "records": record_count if record_count is not None else 0,
            }
        )

    if verbose:
        table_rows = [
            [r["#"], f"{r['latency_s']:.2f}s", r["grounding"], r["execution"]]
            for r in results
        ]
        print(
            tabulate(
                table_rows,
                headers=["#", "Latency", "Grounding", "Execution"],
                tablefmt="fancy_grid",
            )
        )

    executor.close()
    return results


if __name__ == "__main__":
    run_schema_recall_eval()
    run_performance_eval(verbose=True)

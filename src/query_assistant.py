"""
Natural Language Query Assistant for the MITRE ATLAS Knowledge Graph.
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

import io
import re
import argparse
from neo4j import GraphDatabase
from tabulate import tabulate

import config
from llm_client import LLMClientWrapper

DEFAULT_OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")

SYSTEM_PROMPT = """You are an expert database administrator. Your task is to translate natural language user questions into valid Cypher queries for a Neo4j database representing the MITRE ATLAS framework.

=== DATABASE SCHEMA ===
Nodes:
- Matrix {id: STRING, name: STRING, description: STRING, uuid: STRING}
- Tactic {id: STRING, name: STRING, description: STRING, uuid: STRING}
- Technique {id: STRING, name: STRING, description: STRING, uuid: STRING, maturity: STRING, platforms: LIST[STRING]}
- Mitigation {id: STRING, name: STRING, description: STRING, uuid: STRING, categories: LIST[STRING], lifecycle_phases: LIST[STRING]}
- CaseStudy {id: STRING, name: STRING, description: STRING, uuid: STRING, type: STRING, actor: STRING, target: STRING, reporter: STRING, date: STRING, date_granularity: STRING, references_json: STRING}
- Component {name: STRING, category: STRING} -- heuristic enrichment representing systems/paths targetable (e.g. 'RAG', 'Inference', 'LLM')
- LifecyclePhase {name: STRING} -- heuristic mapping representing mitigation phases
- Role {name: STRING} -- heuristic mapping representing organizational roles owning mitigations
- OWASPCategory {id: STRING, name: STRING} -- OWASP LLM Top 10 categories mapped to ATLAS
- NISTCategory {id: STRING, name: STRING} -- NIST AI RMF categories mapped to ATLAS

Relationships:
- (:Matrix)-[:SEQUENCES {position: INTEGER}]->(:Tactic)
- (:Technique)-[:ACHIEVES]->(:Tactic)
- (:Mitigation)-[:MITIGATES]->(:Technique)
- (:CaseStudy)-[:EMPLOYS {step_id: STRING, tactic: STRING, leads_to: LIST[STRING], description: STRING}]->(:Technique)
- (:Technique)-[:SPECIALIZES]->(:Technique) -- representing sub-technique relationships (sub-technique SPECIALIZES parent-technique)
- (:Technique)-[:HEURISTIC_TARGETS]->(:Component)
- (:Mitigation)-[:HEURISTIC_APPLIES_TO]->(:LifecyclePhase)
- (:Mitigation)-[:HEURISTIC_OWNED_BY]->(:Role)
- (:OWASPCategory)-[:MAPS_TO]->(:Technique)
- (:NISTCategory)-[:MAPS_TO]->(:Technique)

=== CRITICAL TRANSLATION RULES ===
1. Generate READ-ONLY queries ONLY. Use MATCH, WHERE, RETURN, collect, count, etc.
2. NEVER generate Cypher containing write keywords (CREATE, MERGE, SET, DELETE, REMOVE, DROP, DETACH).
3. Do NOT include any explanations, markdown text, or descriptions.
4. Output the Cypher query wrapped inside a single ```cypher and ``` block.
5. Pay careful attention to relationship directions:
   - Technique ACHIEVES Tactic
   - Mitigation MITIGATES Technique
   - CaseStudy EMPLOYS Technique
   - Technique SPECIALIZES Technique
   - Matrix SEQUENCES Tactic
   - Technique HEURISTIC_TARGETS Component
   - Mitigation HEURISTIC_APPLIES_TO LifecyclePhase
   - Mitigation HEURISTIC_OWNED_BY Role
   - OWASPCategory MAPS_TO Technique
6. When referencing any variable in the RETURN or WHERE clause (like `t`, `tech`, `m`, etc.), you MUST define it first in the MATCH clause (e.g., `MATCH (tech:Technique)`). Never return undefined variables.
7. To find techniques related to or targeting a specific component (e.g. 'RAG' or 'Inference'), you MUST trace the relationship: `(tech:Technique)-[:HEURISTIC_TARGETS]->(c:Component {name: 'RAG'})`.
"""


def extract_cypher(model_output):
    match = re.search(
        r"```cypher\s+(.*?)\s*```", model_output, re.DOTALL | re.IGNORECASE
    )
    if match:
        return match.group(1).strip()
    match = re.search(
        r"```(?:sql|)\s+(.*?)\s*```", model_output, re.DOTALL | re.IGNORECASE
    )
    if match:
        return match.group(1).strip()
    match = re.search(r"```cypher\s+(.*)", model_output, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return model_output.strip()


def validate_cypher_safety(cypher_query):
    forbidden = [
        "create",
        "delete",
        "set",
        "remove",
        "merge",
        "drop",
        "detach",
        "call apoc",
        "load csv",
    ]
    normalized = cypher_query.lower()
    words = re.findall(r"\b\w+\b", normalized)
    for word in words:
        if word in forbidden:
            return (
                False,
                f"Safety violation: forbidden write keyword '{word.upper()}' detected.",
            )
    return True, ""


class GraphExecutor:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def execute_and_print(self, cypher_query):
        with self.driver.session() as session:
            try:
                result = session.run(cypher_query)
                keys = list(result.keys())
                records = [list(record.values()) for record in result]
                if not records:
                    print("\n[i] Query executed successfully, but returned 0 records.")
                    return True, None
                formatted_records = []
                for row in records:
                    formatted_row = [
                        str(cell)[:57] + "..." if len(str(cell)) > 60 else str(cell)
                        for cell in row
                    ]
                    formatted_records.append(formatted_row)
                print("\n=== QUERY EXECUTION RESULTS ===")
                print(tabulate(formatted_records, headers=keys, tablefmt="grid"))
                return True, None
            except Exception as e:
                return False, str(e)


def run_assistant_flow(user_query, llm_client, executor):
    print(f"\nUser Query: {user_query}")
    try:
        raw_output = llm_client.generate_completion(SYSTEM_PROMPT, user_query)
        cypher = extract_cypher(raw_output)
        is_safe, error_msg = validate_cypher_safety(cypher)
        if not is_safe:
            print(f"\n[!] Safety Guardrail Triggered: {error_msg}", file=sys.stderr)
            return
        success, error = executor.execute_and_print(cypher)
        if not success:
            print(f"\n[!] Neo4j Execution Error: {error}", file=sys.stderr)
            if any(
                t in error.lower() for t in ["syntax", "defined", "token", "variable"]
            ):
                print("[*] Initiating self-correction loop...")
                raw_correction = llm_client.generate_correction(
                    user_query, cypher, error, SYSTEM_PROMPT
                )
                corrected = extract_cypher(raw_correction)
                is_safe2, _ = validate_cypher_safety(corrected)
                if is_safe2:
                    executor.execute_and_print(corrected)
    except Exception as e:
        print(f"\n[!] Error: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?", default=None)
    parser.add_argument("--interactive", "-i", action="store_true")
    parser.add_argument("--model", "-m", default=DEFAULT_OLLAMA_MODEL)
    parser.add_argument("--host", default=DEFAULT_OLLAMA_HOST)
    args = parser.parse_args()
    if not args.query and not args.interactive:
        sys.exit(1)

    llm_client = LLMClientWrapper(
        provider="Ollama", model=args.model, endpoint=args.host
    )
    try:
        executor = GraphExecutor()
        if args.interactive:
            while True:
                user_input = input("\nATLAS-KG> ").strip()
                if user_input.lower() in ("exit", "quit"):
                    break
                run_assistant_flow(user_input, llm_client, executor)
        else:
            run_assistant_flow(args.query, llm_client, executor)
    finally:
        executor.close()


if __name__ == "__main__":
    main()

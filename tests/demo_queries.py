"""
Query Interface for the MITRE ATLAS Knowledge Graph.

Provides 10 professional-grade Cypher queries demonstrating multi-hop traversals,
incident forensics, unmitigated gap analysis, platform profiles, and the
specific RAG security question from the internship assessment brief.
"""

import argparse
import io
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from neo4j import GraphDatabase
from tabulate import tabulate

import config


class AtlasQuerier:
    """Handles executing and formatting complex Cypher queries on the ATLAS Graph."""

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """Closes the Neo4j driver connection."""
        self.driver.close()

    def run_query(self, title, description, cypher):
        """Executes a Cypher query, formats the output in a premium table, and prints it."""
        print(f"\n{'='*80}")
        print(f"QUERY: {title}")
        print(f"DESC : {description}")
        print(f"{'-'*80}")

        with self.driver.session() as session:
            try:
                result = session.run(cypher)
                keys = list(result.keys())
                records = [list(record.values()) for record in result]

                if not records:
                    print("No records returned.")
                else:
                    formatted_records = []
                    for row in records:
                        formatted_row = []
                        for cell in row:
                            val = str(cell) if cell is not None else "NULL"
                            if len(val) > 50:
                                val = val[:47] + "..."
                            formatted_row.append(val)
                        formatted_records.append(formatted_row)

                    print(tabulate(formatted_records, headers=keys, tablefmt="grid"))
            except Exception as e:
                print(f"Execution Error: {e}", file=sys.stderr)
        print(f"{'='*80}\n")


QUERIES = {
    1: {
        "title": "Assessment Brief Example (RAG Inference & App Dev)",
        "desc": "Which techniques target the inference path of a RAG-based assistant, and which mitigations are owned by application developers?",
        "cypher": """
            MATCH (r:Role {name: 'Application Developer'})<-[:HEURISTIC_OWNED_BY]-(m:Mitigation)-[:MITIGATES]->(tech:Technique)
            MATCH (tech)-[:HEURISTIC_TARGETS]->(c:Component)
            WHERE c.name IN ['RAG', 'Inference']
            RETURN DISTINCT
                tech.id AS Technique_ID, 
                tech.name AS Technique, 
                m.id AS Mitigation_ID, 
                m.name AS Mitigation,
                collect(DISTINCT c.name) AS Targeted_Components
            ORDER BY tech.id
        """,
    },
    2: {
        "title": "Case Study Kill-Chain Reconstruction (AML.CS0000)",
        "desc": "Reconstruct the timeline steps of the 'Evasion of Deep Learning Detector' case study in sequence.",
        "cypher": """
            MATCH (cs:CaseStudy {id: 'AML.CS0000'})-[r:EMPLOYS]->(tech:Technique)
            MATCH (tech)-[:ACHIEVES]->(tac:Tactic)
            RETURN 
                r.step_id AS Step, 
                tech.id AS Technique_ID, 
                tech.name AS Technique, 
                tac.name AS Tactic_Achieved, 
                r.description AS Step_Context
            ORDER BY Step
        """,
    },
    3: {
        "title": "Unmitigated Techniques Gap Analysis",
        "desc": "Identify techniques that do not have any official MITRE ATLAS mitigations (potential security gaps).",
        "cypher": """
            MATCH (tech:Technique)
            WHERE NOT (:Mitigation)-[:MITIGATES]->(tech)
            RETURN 
                tech.id AS Technique_ID, 
                tech.name AS Technique_Name, 
                tech.maturity AS Maturity,
                tech.platforms AS Supported_Platforms
            ORDER BY tech.id
            LIMIT 15
        """,
    },
    4: {
        "title": "Platform-Specific Threat Profile Comparison",
        "desc": "Compare the number of techniques and tactics targeted across Predictive AI, Generative AI, and Agentic AI.",
        "cypher": """
            MATCH (tech:Technique)-[:ACHIEVES]->(tac:Tactic)
            UNWIND tech.platforms AS platform
            RETURN 
                platform AS AI_Platform, 
                count(DISTINCT tac) AS Distinct_Tactics_Count, 
                count(DISTINCT tech) AS Distinct_Techniques_Count, 
                collect(DISTINCT tac.name)[..3] AS Sample_Tactics
            ORDER BY Distinct_Techniques_Count DESC
        """,
    },
    5: {
        "title": "Tactic -> Technique -> Mitigation Paths",
        "desc": "Trace the path from Tactic to Techniques, listing the number of associated Mitigations.",
        "cypher": """
            MATCH (tac:Tactic)<-[:ACHIEVES]-(tech:Technique)
            OPTIONAL MATCH (mit:Mitigation)-[:MITIGATES]->(tech)
            RETURN 
                tac.id AS Tactic_ID, 
                tac.name AS Tactic, 
                tech.id AS Technique_ID, 
                tech.name AS Technique, 
                count(mit) AS Mitigation_Count
            ORDER BY Tactic_ID, Mitigation_Count DESC
            LIMIT 15
        """,
    },
    6: {
        "title": "Multi-Hop Incident Forensic Analysis",
        "desc": "Trace a Case Study to its employed Techniques, the Mitigations for those techniques, and the heuristic owner Roles.",
        "cypher": """
            MATCH (cs:CaseStudy)-[:EMPLOYS]->(tech:Technique)<-[:MITIGATES]-(mit:Mitigation)
            MATCH (mit)-[:HEURISTIC_OWNED_BY]->(role:Role)
            RETURN 
                cs.id AS CaseStudy_ID, 
                cs.name AS CaseStudy, 
                tech.name AS Technique, 
                mit.name AS Mitigation, 
                role.name AS Responsible_Role
            ORDER BY CaseStudy_ID
            LIMIT 15
        """,
    },
    7: {
        "title": "Mitigation Coverage Heatmap per Tactic",
        "desc": "Count how many mitigations cover techniques grouped under each Tactic.",
        "cypher": """
            MATCH (tac:Tactic)<-[:ACHIEVES]-(tech:Technique)<-[:MITIGATES]-(mit:Mitigation)
            RETURN 
                tac.id AS Tactic_ID, 
                tac.name AS Tactic, 
                count(DISTINCT tech) AS Mitigated_Techniques,
                count(DISTINCT mit) AS Total_Mitigations_Applied
            ORDER BY Total_Mitigations_Applied DESC
        """,
    },
    8: {
        "title": "Matrix Tactic Sequence Chain",
        "desc": "Extract the sequenced order of Tactics from the ATLAS matrix definition.",
        "cypher": """
            MATCH (m:Matrix {id: 'ATLAS-matrix'})-[r:SEQUENCES]->(tac:Tactic)
            RETURN 
                r.position AS Order, 
                tac.id AS Tactic_ID, 
                tac.name AS Tactic_Name
            ORDER BY Order
        """,
    },
    9: {
        "title": "Lifecycle Phase & Role Responsibility Matrix",
        "desc": "Heuristic mapping showing which Lifecycle Phases map to which Roles and how many Mitigations they govern.",
        "cypher": """
            MATCH (lp:LifecyclePhase)<-[:HEURISTIC_APPLIES_TO]-(m:Mitigation)-[:HEURISTIC_OWNED_BY]->(r:Role)
            RETURN 
                lp.name AS Lifecycle_Phase, 
                r.name AS Responsible_Role, 
                count(DISTINCT m) AS Mitigations_Governed
            ORDER BY lp.name, Mitigations_Governed DESC
        """,
    },
    10: {
        "title": "Sub-Technique Specialization Traversal",
        "desc": "Traverse the specialization hierarchy to show sub-techniques, parent techniques, and their tactics.",
        "cypher": """
            MATCH (sub:Technique)-[:SPECIALIZES]->(parent:Technique)
            OPTIONAL MATCH (parent)-[:ACHIEVES]->(tac:Tactic)
            RETURN 
                sub.id AS SubTech_ID, 
                sub.name AS SubTech_Name, 
                parent.id AS ParentTech_ID, 
                parent.name AS ParentTech_Name, 
                tac.name AS Tactic
            ORDER BY ParentTech_ID, SubTech_ID
        """,
    },
    11: {
        "title": "OWASP LLM Top 10 -> ATLAS Coverage",
        "desc": "Show which OWASP categories map to which ATLAS techniques and how many mitigations are available for each.",
        "cypher": """
            MATCH (o:OWASPCategory)-[:MAPS_TO]->(t:Technique)
            OPTIONAL MATCH (m:Mitigation)-[:MITIGATES]->(t)
            RETURN 
                o.id AS OWASP_ID,
                o.name AS OWASP_Category,
                t.id AS ATLAS_ID,
                t.name AS ATLAS_Technique,
                count(DISTINCT m) AS Mitigation_Count
            ORDER BY OWASP_ID, Mitigation_Count DESC
        """,
    },
}


def main():
    parser = argparse.ArgumentParser(
        description="Query Interface for MITRE ATLAS Knowledge Graph"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--all", action="store_true", help="Run all 11 demonstration queries"
    )
    group.add_argument(
        "--query",
        type=int,
        choices=QUERIES.keys(),
        help="Run a specific query by its ID (1-11)",
    )
    group.add_argument(
        "--list", action="store_true", help="List descriptions of all available queries"
    )
    args = parser.parse_args()

    if args.list:
        print("\n=== Available Demonstration Queries ===")
        for qid, qdata in QUERIES.items():
            print(f"[{qid}] {qdata['title']}")
            print(f"    Description: {qdata['desc']}\n")
        return

    querier = AtlasQuerier(config.NEO4J_URI, config.NEO4J_USER, config.NEO4J_PASSWORD)
    try:
        if args.query:
            q = QUERIES[args.query]
            querier.run_query(q["title"], q["desc"], q["cypher"])
        elif args.all:
            for qid, q in QUERIES.items():
                querier.run_query(f"[{qid}] {q['title']}", q["desc"], q["cypher"])
    except Exception as e:
        print(f"Querier execution failed: {e}", file=sys.stderr)
    finally:
        querier.close()


if __name__ == "__main__":
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding="utf-8", errors="replace"
        )
        sys.stderr = io.TextIOWrapper(
            sys.stderr.buffer, encoding="utf-8", errors="replace"
        )
    main()

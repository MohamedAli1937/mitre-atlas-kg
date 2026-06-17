"""
Knowledge Graph Builder for MITRE ATLAS.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import json
import logging
import argparse
import yaml
from neo4j import GraphDatabase
from tabulate import tabulate

import src.config as config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


class AtlasIngestor:
    """Handles parsing and ingestion of MITRE ATLAS YAML data into Neo4j."""

    def __init__(self, uri, user, password, llm_client=None):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.llm_client = llm_client

    def close(self):
        """Closes the Neo4j driver connection."""
        self.driver.close()

    def clean_db(self):
        """Removes all nodes and relationships from the database."""
        logging.warning("Cleaning database...")
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def setup_schema(self):
        """Creates uniqueness constraints and indexes."""
        constraints = [
            "CREATE CONSTRAINT matrix_id IF NOT EXISTS FOR (n:Matrix) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT tactic_id IF NOT EXISTS FOR (n:Tactic) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT technique_id IF NOT EXISTS FOR (n:Technique) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT mitigation_id IF NOT EXISTS FOR (n:Mitigation) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT case_study_id IF NOT EXISTS FOR (n:CaseStudy) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT owasp_id IF NOT EXISTS FOR (n:OWASPCategory) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT component_name IF NOT EXISTS FOR (n:Component) REQUIRE n.name IS UNIQUE",
            "CREATE CONSTRAINT role_name IF NOT EXISTS FOR (n:Role) REQUIRE n.name IS UNIQUE",
            "CREATE CONSTRAINT phase_name IF NOT EXISTS FOR (n:LifecyclePhase) REQUIRE n.name IS UNIQUE",
        ]
        with self.driver.session() as session:
            for q in constraints:
                session.run(q)
        logging.info("Schema established.")

    def extract_heuristic_components(self, text, ai_enrich=False):
        if not text:
            return []
        found = []
        text_upper = text.upper()
        for category, items in config.COMPONENT_TAXONOMY.items():
            for item in items:
                if item.upper() in text_upper:
                    found.append((item, category))

        if ai_enrich and self.llm_client:
            prompt = 'Extract AI architecture components (RAG, LLM, etc.) from description. Return JSON list: [{"name": "...", "category": "..."}].'
            ai_results = self.llm_client.generate_structured_json(prompt, text)
            if ai_results and isinstance(ai_results, list):
                for item in ai_results:
                    if item.get("name"):
                        found.append((item["name"], item.get("category", "General")))
        return list(set(found))

    def batch_write(self, cypher, batch):
        if not batch:
            return
        with self.driver.session() as session:
            session.run(cypher, batch=batch)

    def ingest_owasp_mapping(self, mapping_path):
        if not os.path.exists(mapping_path):
            return
        with open(mapping_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        mapping_list = data.get("owasp_llm_to_mitre_atlas", {}).get("mappings", [])
        categories = []
        relationships = []
        for item in mapping_list:
            categories.append(
                {"id": item.get("owasp_id"), "name": item.get("owasp_name")}
            )
            for tech in item.get("atlas_techniques", []):
                relationships.append(
                    {"owasp_id": item.get("owasp_id"), "tech_id": tech.get("id")}
                )
        self.batch_write(
            "UNWIND $batch AS row MERGE (o:OWASPCategory {id: row.id}) SET o.name = row.name",
            categories,
        )
        self.batch_write(
            "UNWIND $batch AS row MATCH (o:OWASPCategory {id: row.owasp_id}) MATCH (t:Technique {id: row.tech_id}) MERGE (o)-[:MAPS_TO]->(t)",
            relationships,
        )

    def run(self, yaml_path, clean_first=False, ai_enrich=False):
        if not os.path.exists(yaml_path):
            logging.error(f"File not found: {yaml_path}")
            return
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if clean_first:
            self.clean_db()
        self.setup_schema()

        matrices = []
        matrix_data = data.get("matrix", {})
        if matrix_data:
            matrices.append(
                {
                    "id": matrix_data.get("id", "ATLAS-matrix"),
                    "name": matrix_data.get("name", "ATLAS"),
                }
            )

        tactics = [
            {"id": tid, "name": tdata.get("name", "")}
            for tid, tdata in data.get("tactics", {}).items()
        ]

        techniques = []
        heuristic_components = []
        tech_items = list(data.get("techniques", {}).items())
        total_techs = len(tech_items)

        logging.info(
            f"Starting technique ingestion ({total_techs} items)... AI Enrichment: {'ENABLED' if ai_enrich else 'DISABLED'}"
        )

        for i, (tech_id, tech_data) in enumerate(tech_items):
            if ai_enrich and i % 10 == 0:
                logging.info(f"Progress: {i}/{total_techs} techniques processed...")

            techniques.append(
                {
                    "id": tech_id,
                    "name": tech_data.get("name", ""),
                    "maturity": tech_data.get("maturity", "Unknown"),
                    "platforms": tech_data.get("platforms", []),
                }
            )
            corpus = f"{tech_data.get('name', '')} {tech_data.get('description', '')}"
            for comp_name, comp_cat in self.extract_heuristic_components(
                corpus, ai_enrich=ai_enrich
            ):
                heuristic_components.append(
                    {
                        "tech_id": tech_id,
                        "comp_name": comp_name,
                        "comp_category": comp_cat,
                    }
                )

        mitigations = []
        heuristic_roles = []
        for mit_id, mit_data in data.get("mitigations", {}).items():
            phases = mit_data.get("lifecycle-phases", [])
            mitigations.append(
                {
                    "id": mit_id,
                    "name": mit_data.get("name", ""),
                    "lifecycle_phases": phases,
                }
            )
            for phase in phases:
                if phase in config.ROLE_PHASE_MAP:
                    for role in config.ROLE_PHASE_MAP[phase]:
                        heuristic_roles.append(
                            {"mit_id": mit_id, "role_name": role, "phase_name": phase}
                        )

        case_studies = [
            {"id": cs_id, "name": cs_data.get("name", "")}
            for cs_id, cs_data in data.get("case-studies", {}).items()
        ]

        self.batch_write(
            "UNWIND $batch AS row MERGE (m:Matrix {id: row.id}) SET m.name = row.name",
            matrices,
        )
        self.batch_write(
            "UNWIND $batch AS row MERGE (t:Tactic {id: row.id}) SET t.name = row.name",
            tactics,
        )
        self.batch_write(
            "UNWIND $batch AS row MERGE (t:Technique {id: row.id}) SET t.name = row.name, t.maturity = row.maturity, t.platforms = row.platforms",
            techniques,
        )
        self.batch_write(
            "UNWIND $batch AS row MERGE (m:Mitigation {id: row.id}) SET m.name = row.name",
            mitigations,
        )
        self.batch_write(
            "UNWIND $batch AS row MERGE (cs:CaseStudy {id: row.id}) SET cs.name = row.name",
            case_studies,
        )

        rel_batches = {
            "achieves": [],
            "mitigates": [],
            "employs": [],
            "specializes": [],
            "sequences": [],
        }
        if "relationships" in data:
            for source_id, rel_types in data["relationships"].items():
                for rel_type, rel_list in rel_types.items():
                    for rel in rel_list:
                        rec = {
                            "source": source_id,
                            "target": rel.get("target"),
                            "position": rel.get("position"),
                        }
                        if rel_type in rel_batches:
                            rel_batches[rel_type].append(rec)

        self.batch_write(
            "UNWIND $batch AS row MATCH (tech:Technique {id: row.source}) MATCH (tac:Tactic {id: row.target}) MERGE (tech)-[:ACHIEVES]->(tac)",
            rel_batches["achieves"],
        )
        self.batch_write(
            "UNWIND $batch AS row MATCH (mit:Mitigation {id: row.source}) MATCH (tech:Technique {id: row.target}) MERGE (mit)-[:MITIGATES]->(tech)",
            rel_batches["mitigates"],
        )
        self.batch_write(
            "UNWIND $batch AS row MATCH (cs:CaseStudy {id: row.source}) MATCH (tech:Technique {id: row.target}) MERGE (cs)-[:EMPLOYS]->(tech)",
            rel_batches["employs"],
        )
        self.batch_write(
            "UNWIND $batch AS row MATCH (sub:Technique {id: row.source}) MATCH (parent:Technique {id: row.target}) MERGE (sub)-[:SPECIALIZES]->(parent)",
            rel_batches["specializes"],
        )
        self.batch_write(
            "UNWIND $batch AS row MATCH (m:Matrix {id: row.source}) MATCH (t:Tactic {id: row.target}) MERGE (m)-[r:SEQUENCES]->(t) SET r.position = row.position",
            rel_batches["sequences"],
        )

        self.batch_write(
            "UNWIND $batch AS row MERGE (c:Component {name: row.comp_name}) SET c.category = row.comp_category WITH c, row MATCH (tech:Technique {id: row.tech_id}) MERGE (tech)-[:HEURISTIC_TARGETS]->(c)",
            heuristic_components,
        )
        self.batch_write(
            "UNWIND $batch AS row MERGE (r:Role {name: row.role_name}) MERGE (p:LifecyclePhase {name: row.phase_name}) WITH r, p, row MATCH (mit:Mitigation {id: row.mit_id}) MERGE (mit)-[:HEURISTIC_OWNED_BY]->(r) MERGE (mit)-[:HEURISTIC_APPLIES_TO]->(p)",
            heuristic_roles,
        )

        self.ingest_owasp_mapping(os.path.join("data", "owasp_atlas_mapping.json"))
        self.ingest_nist_rmf(os.path.join("data", "nist_ai_rmf_mapping.json"))
        logging.info("Ingestion complete.")

    def ingest_nist_rmf(self, json_path):
        """Maps NIST AI RMF categories to ATLAS techniques."""
        if not os.path.exists(json_path):
            return
        logging.info("Ingesting NIST AI RMF mappings...")
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        query = """
        UNWIND $batch AS row
        MERGE (n:NISTCategory {id: row.nist_id})
        SET n.name = row.nist_name
        WITH n, row
        UNWIND row.atlas_techniques AS tech
        MATCH (t:Technique {id: tech.id})
        MERGE (n)-[:MAPS_TO]->(t)
        """
        with self.driver.session() as session:
            session.run(query, batch=data)

    def get_stats(self):
        """Returns comprehensive graph statistics."""
        queries = {
            "Matrices": "MATCH (n:Matrix) RETURN count(n)",
            "Tactics": "MATCH (n:Tactic) RETURN count(n)",
            "Techniques": "MATCH (n:Technique) RETURN count(n)",
            "Mitigations": "MATCH (n:Mitigation) RETURN count(n)",
            "CaseStudies": "MATCH (n:CaseStudy) RETURN count(n)",
            "OWASPCategories": "MATCH (n:OWASPCategory) RETURN count(n)",
            "NISTCategories": "MATCH (n:NISTCategory) RETURN count(n)",
            "HeuristicComponents": "MATCH (n:Component) RETURN count(n)",
            "UnmitigatedTechniques": "MATCH (t:Technique) WHERE NOT (:Mitigation)-[:MITIGATES]->(t) RETURN count(t)",
        }
        stats = {}
        with self.driver.session() as session:
            for label, q in queries.items():
                stats[label] = session.run(q).single()[0]
        return stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--ai-enrich", action="store_true")
    args = parser.parse_args()

    llm = None
    if args.ai_enrich:
        from src.llm_client import LLMClientWrapper

        llm = LLMClientWrapper("Ollama")

    ingestor = AtlasIngestor(
        config.NEO4J_URI, config.NEO4J_USER, config.NEO4J_PASSWORD, llm_client=llm
    )
    ingestor.run(
        os.path.join("data", "ATLAS-latest.yaml"),
        clean_first=args.clean,
        ai_enrich=args.ai_enrich,
    )
    ingestor.close()

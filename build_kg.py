"""
Knowledge Graph Builder for MITRE ATLAS.

Ingests tactics, techniques, mitigations, case-studies, matrices, and
relationships from the official MITRE ATLAS YAML data source into Neo4j.
Features batched transactions (UNWIND), strict data fidelity, schema indexing,
and heuristic-based security engineering enrichments (Roles, Components).
"""

import os
import sys
import json
import logging
import argparse
import yaml
from neo4j import GraphDatabase
from tabulate import tabulate

import config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


class AtlasIngestor:
    """Handles parsing and ingestion of MITRE ATLAS YAML data into Neo4j."""

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """Closes the Neo4j driver connection."""
        self.driver.close()

    def clean_db(self):
        """Removes all nodes and relationships from the database."""
        logging.warning("Cleaning database: deleting all existing nodes and relationships...")
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        logging.info("Database cleaned successfully.")

    def setup_schema(self):
        """Creates uniqueness constraints and indexes for high-performance traversals."""
        constraints = [
            "CREATE CONSTRAINT matrix_id IF NOT EXISTS FOR (n:Matrix) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT tactic_id IF NOT EXISTS FOR (n:Tactic) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT technique_id IF NOT EXISTS FOR (n:Technique) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT mitigation_id IF NOT EXISTS FOR (n:Mitigation) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT case_study_id IF NOT EXISTS FOR (n:CaseStudy) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT component_name IF NOT EXISTS FOR (n:Component) REQUIRE n.name IS UNIQUE",
            "CREATE CONSTRAINT role_name IF NOT EXISTS FOR (n:Role) REQUIRE n.name IS UNIQUE",
            "CREATE CONSTRAINT phase_name IF NOT EXISTS FOR (n:LifecyclePhase) REQUIRE n.name IS UNIQUE"
        ]
        indexes = [
            "CREATE INDEX technique_name_idx IF NOT EXISTS FOR (t:Technique) ON (t.name)",
            "CREATE INDEX mitigation_name_idx IF NOT EXISTS FOR (m:Mitigation) ON (m.name)",
            "CREATE INDEX case_study_name_idx IF NOT EXISTS FOR (c:CaseStudy) ON (c.name)"
        ]

        with self.driver.session() as session:
            for q in constraints:
                session.run(q)
            for q in indexes:
                session.run(q)
        logging.info("Constraints and indexes established in Neo4j.")

    def extract_heuristic_components(self, text):
        """
        Extracts components from text using simple keyword heuristic matches.
        These are project-specific enrichments and NOT official MITRE taxonomies.
        """
        if not text:
            return []
        text_upper = text.upper()
        found = []
        for category, items in config.COMPONENT_TAXONOMY.items():
            for item in items:
                if item.upper() in text_upper:
                    found.append((item, category))
        return found

    def batch_write(self, cypher, batch):
        """Executes a Cypher write query with a batch payload."""
        if not batch:
            return
        with self.driver.session() as session:
            session.run(cypher, batch=batch)

    def run(self, yaml_path, clean_first=False):
        """Parses the YAML and runs batched ingestion into Neo4j."""
        if not os.path.exists(yaml_path):
            logging.error(f"YAML source file not found: {yaml_path}")
            sys.exit(1)

        logging.info(f"Loading MITRE ATLAS data from: {yaml_path}")
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if clean_first:
            self.clean_db()

        self.setup_schema()

        # -------------------------------------------------------------------
        # 1. Parse Entities from YAML
        # -------------------------------------------------------------------
        matrices = []
        matrix_data = data.get("matrix", {})
        if matrix_data:
            matrices.append({
                "id": matrix_data.get("id", "ATLAS-matrix"),
                "name": matrix_data.get("name", "ATLAS"),
                "description": matrix_data.get("description", ""),
                "uuid": matrix_data.get("uuid", "")
            })

        tactics = []
        for tid, tdata in data.get("tactics", {}).items():
            tactics.append({
                "id": tid,
                "name": tdata.get("name", ""),
                "description": tdata.get("description", ""),
                "uuid": tdata.get("uuid", "")
            })

        techniques = []
        heuristic_components = []
        for tech_id, tech_data in data.get("techniques", {}).items():
            techniques.append({
                "id": tech_id,
                "name": tech_data.get("name", ""),
                "description": tech_data.get("description", ""),
                "uuid": tech_data.get("uuid", ""),
                "maturity": tech_data.get("maturity", "Unknown"),
                "platforms": tech_data.get("platforms", [])
            })
            # Core text for component extraction
            corpus = f"{tech_data.get('name', '')} {tech_data.get('description', '')}"
            for comp_name, comp_cat in self.extract_heuristic_components(corpus):
                heuristic_components.append({
                    "tech_id": tech_id,
                    "comp_name": comp_name,
                    "comp_category": comp_cat
                })

        mitigations = []
        heuristic_lifecycle_phases = []
        heuristic_roles = []
        for mit_id, mit_data in data.get("mitigations", {}).items():
            phases = mit_data.get("lifecycle-phases", [])
            mitigations.append({
                "id": mit_id,
                "name": mit_data.get("name", ""),
                "description": mit_data.get("description", ""),
                "uuid": mit_data.get("uuid", ""),
                "categories": mit_data.get("categories", []),
                "lifecycle_phases": phases
            })
            for phase in phases:
                heuristic_lifecycle_phases.append({
                    "mit_id": mit_id,
                    "phase_name": phase
                })
                # Map phases to roles
                if phase in config.ROLE_PHASE_MAP:
                    for role in config.ROLE_PHASE_MAP[phase]:
                        heuristic_roles.append({
                            "mit_id": mit_id,
                            "role_name": role
                        })

        case_studies = []
        for cs_id, cs_data in data.get("case-studies", {}).items():
            # References list of dictionaries needs JSON serialization for Neo4j property storage
            refs = cs_data.get("references", [])
            refs_json = json.dumps(refs) if refs else "[]"
            case_studies.append({
                "id": cs_id,
                "name": cs_data.get("name", ""),
                "description": cs_data.get("description", ""),
                "uuid": cs_data.get("uuid", ""),
                "type": cs_data.get("type", "Unknown"),
                "actor": cs_data.get("actor", "Unknown"),
                "target": cs_data.get("target", "Unknown"),
                "reporter": cs_data.get("reporter", "Unknown"),
                "date": cs_data.get("date", ""),
                "date_granularity": cs_data.get("date-granularity", ""),
                "references_json": refs_json
            })

        # -------------------------------------------------------------------
        # 2. Ingest Nodes (Idempotent MERGE)
        # -------------------------------------------------------------------
        logging.info("Ingesting Matrix nodes...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (m:Matrix {id: row.id})
            SET m.name = row.name, m.description = row.description, m.uuid = row.uuid
        """, matrices)

        logging.info("Ingesting Tactic nodes...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (t:Tactic {id: row.id})
            SET t.name = row.name, t.description = row.description, t.uuid = row.uuid
        """, tactics)

        logging.info("Ingesting Technique nodes...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (t:Technique {id: row.id})
            SET t.name = row.name, t.description = row.description, t.uuid = row.uuid,
                t.maturity = row.maturity, t.platforms = row.platforms
        """, techniques)

        logging.info("Ingesting Mitigation nodes...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (m:Mitigation {id: row.id})
            SET m.name = row.name, m.description = row.description, m.uuid = row.uuid,
                m.categories = row.categories, m.lifecycle_phases = row.lifecycle_phases
        """, mitigations)

        logging.info("Ingesting CaseStudy nodes...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (cs:CaseStudy {id: row.id})
            SET cs.name = row.name, cs.description = row.description, cs.uuid = row.uuid,
                cs.type = row.type, cs.actor = row.actor, cs.target = row.target,
                cs.reporter = row.reporter, cs.date = row.date, cs.date_granularity = row.date_granularity,
                cs.references_json = row.references_json
        """, case_studies)

        # -------------------------------------------------------------------
        # 3. Parse and Ingest Relationships
        # -------------------------------------------------------------------
        rel_batches = {
            "achieves": [],
            "mitigates": [],
            "employs": [],
            "specializes": [],
            "sequences": [],
            "custom": []
        }

        if "relationships" in data:
            for source_id, rel_types_dict in data["relationships"].items():
                if not rel_types_dict:
                    continue
                for rel_type, rel_list in rel_types_dict.items():
                    if not rel_list:
                        continue
                    for rel in rel_list:
                        target_id = rel.get("target")
                        desc = rel.get("description", "")
                        
                        # Build standard structure
                        rel_record = {
                            "source": source_id,
                            "target": target_id,
                            "description": desc,
                            # employs specific fields
                            "tactic": rel.get("tactic", ""),
                            "step_id": rel.get("step-id", ""),
                            "leads_to": rel.get("leads-to", []),
                            # sequences specific fields
                            "position": rel.get("position", None)
                        }

                        if rel_type in rel_batches:
                            rel_batches[rel_type].append(rel_record)
                        else:
                            logging.warning(f"Unknown relationship type found in YAML: '{rel_type}' for {source_id} -> {target_id}")
                            rel_record["relationship_type"] = rel_type
                            rel_batches["custom"].append(rel_record)

        logging.info("Creating ACHIEVES relationships (Technique -> Tactic)...")
        self.batch_write("""
            UNWIND $batch AS row
            MATCH (tech:Technique {id: row.source})
            MATCH (tac:Tactic {id: row.target})
            MERGE (tech)-[r:ACHIEVES]->(tac)
            SET r.description = row.description
        """, rel_batches["achieves"])

        logging.info("Creating MITIGATES relationships (Mitigation -> Technique)...")
        self.batch_write("""
            UNWIND $batch AS row
            MATCH (mit:Mitigation {id: row.source})
            MATCH (tech:Technique {id: row.target})
            MERGE (mit)-[r:MITIGATES]->(tech)
            SET r.description = row.description
        """, rel_batches["mitigates"])

        logging.info("Creating EMPLOYS relationships (CaseStudy -> Technique)...")
        self.batch_write("""
            UNWIND $batch AS row
            MATCH (cs:CaseStudy {id: row.source})
            MATCH (tech:Technique {id: row.target})
            MERGE (cs)-[r:EMPLOYS]->(tech)
            SET r.description = row.description,
                r.tactic = row.tactic,
                r.step_id = row.step_id,
                r.leads_to = row.leads_to
        """, rel_batches["employs"])

        logging.info("Creating SPECIALIZES relationships (Technique -> Technique)...")
        self.batch_write("""
            UNWIND $batch AS row
            MATCH (sub:Technique {id: row.source})
            MATCH (parent:Technique {id: row.target})
            MERGE (sub)-[r:SPECIALIZES]->(parent)
            SET r.description = row.description
        """, rel_batches["specializes"])

        logging.info("Creating SEQUENCES relationships (Matrix -> Tactic)...")
        self.batch_write("""
            UNWIND $batch AS row
            MATCH (m:Matrix {id: row.source})
            MATCH (t:Tactic {id: row.target})
            MERGE (m)-[r:SEQUENCES]->(t)
            SET r.position = row.position
        """, rel_batches["sequences"])

        if rel_batches["custom"]:
            logging.info("Creating custom/unknown fallback relationships (Node -> Node)...")
            self.batch_write("""
                UNWIND $batch AS row
                MATCH (s {id: row.source})
                MATCH (t {id: row.target})
                MERGE (s)-[r:RELATED_TO]->(t)
                SET r.description = row.description,
                    r.original_type = row.relationship_type
            """, rel_batches["custom"])

        # -------------------------------------------------------------------
        # 4. Ingest Heuristic Enrichments (HEURISTIC_ prefix)
        # -------------------------------------------------------------------
        logging.info("Creating heuristic component targets (Technique -> Component)...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (c:Component {name: row.comp_name})
            SET c.category = row.comp_category
            WITH c, row
            MATCH (tech:Technique {id: row.tech_id})
            MERGE (tech)-[:HEURISTIC_TARGETS]->(c)
        """, heuristic_components)

        logging.info("Creating heuristic mitigation lifecycle mappings...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (lp:LifecyclePhase {name: row.phase_name})
            WITH lp, row
            MATCH (mit:Mitigation {id: row.mit_id})
            MERGE (mit)-[:HEURISTIC_APPLIES_TO]->(lp)
        """, heuristic_lifecycle_phases)

        logging.info("Creating heuristic mitigation role ownerships...")
        self.batch_write("""
            UNWIND $batch AS row
            MERGE (r:Role {name: row.role_name})
            WITH r, row
            MATCH (mit:Mitigation {id: row.mit_id})
            MERGE (mit)-[:HEURISTIC_OWNED_BY]->(r)
        """, heuristic_roles)

        logging.info("Ingestion phase complete. Starting validation...")
        self.validate_database(data, matrices, tactics, techniques, mitigations, case_studies, rel_batches)

    def validate_database(self, yaml_data, matrices, tactics, techniques, mitigations, case_studies, rel_batches):
        """Queries the Neo4j instance and compares DB counts against expected counts."""
        stats = []

        # Count helpers
        def db_node_count(label):
            with self.driver.session() as s:
                res = s.run(f"MATCH (n:{label}) RETURN count(n) AS c")
                return res.single()["c"]

        def db_rel_count(rel_type):
            with self.driver.session() as s:
                res = s.run(f"MATCH ()-[r:{rel_type}]->() RETURN count(r) AS c")
                return res.single()["c"]

        # Validate nodes
        nodes_to_validate = [
            ("Matrix", len(matrices)),
            ("Tactic", len(tactics)),
            ("Technique", len(techniques)),
            ("Mitigation", len(mitigations)),
            ("CaseStudy", len(case_studies)),
            ("Component", None),  # Heuristic, no explicit expected count in YAML
            ("LifecyclePhase", None),
            ("Role", None),
        ]

        for label, expected in nodes_to_validate:
            actual = db_node_count(label)
            if expected is None:
                stats.append([f"Node: {label}", "-", actual, "N/A (Enrichment)"])
            else:
                status = "PASS" if actual == expected else "FAIL"
                stats.append([f"Node: {label}", expected, actual, status])

        # Validate relationships
        rels_to_validate = [
            ("ACHIEVES", len(rel_batches["achieves"])),
            ("MITIGATES", len(rel_batches["mitigates"])),
            ("EMPLOYS", len(rel_batches["employs"])),
            ("SPECIALIZES", len(rel_batches["specializes"])),
            ("SEQUENCES", len(rel_batches["sequences"])),
            ("RELATED_TO", len(rel_batches["custom"])),
            ("HEURISTIC_TARGETS", None),
            ("HEURISTIC_APPLIES_TO", None),
            ("HEURISTIC_OWNED_BY", None),
        ]

        for rel_type, expected in rels_to_validate:
            actual = db_rel_count(rel_type)
            if expected is None:
                stats.append([f"Rel: {rel_type}", "-", actual, "N/A (Enrichment)"])
            else:
                status = "PASS" if actual == expected else "FAIL"
                stats.append([f"Rel: {rel_type}", expected, actual, status])

        print("\n=== Ingestion Validation Statistics ===")
        print(tabulate(stats, headers=["Element Type", "Expected (YAML)", "Actual (Neo4j)", "Status"], tablefmt="fancy_grid"))
        print("=======================================\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest MITRE ATLAS YAML data into Neo4j")
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clear existing database nodes and relationships before running ingestion"
    )
    parser.add_argument(
        "--yaml-path",
        default=config.YAML_PATH,
        help=f"Path to the ATLAS YAML file (default: {config.YAML_PATH})"
    )
    args = parser.parse_args()

    ingestor = AtlasIngestor(config.NEO4J_URI, config.NEO4J_USER, config.NEO4J_PASSWORD)
    try:
        ingestor.run(args.yaml_path, clean_first=args.clean)
    except Exception as e:
        logging.error(f"Ingestion failed: {e}", exc_info=True)
    finally:
        ingestor.close()

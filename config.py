"""
Centralised configuration for the MITRE ATLAS Knowledge Graph project.

Loads connection details from environment variables (or a .env file via
python-dotenv) and defines the heuristic enrichment constants used by
the ingestion pipeline.
"""

import os

# Optional .env support — degrades gracefully if python-dotenv is absent.
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Neo4j connection
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
# Data source
YAML_PATH = os.getenv("ATLAS_YAML_PATH", "ATLAS-latest.yaml")

# Heuristic enrichment configuration
# IMPORTANT: The constants below are NOT part of the official MITRE ATLAS
# taxonomy. They are project-specific enrichments introduced by this
# implementation to demonstrate additional queryability.
#   - COMPONENT_TAXONOMY: Keywords extracted from technique descriptions to
#     create Component nodes.  Categorised by functional area.
#   - ROLE_PHASE_MAP: Heuristic mapping from MITRE lifecycle phases to
#     responsible organisational roles.

COMPONENT_TAXONOMY = {
    "AI Components": [
        "RAG", "LLM", "AI Agent", "Memory",
        "Embedding Model", "Orchestrator",
    ],
    "Infrastructure": [
        "API", "Cloud", "Service", "Repository",
        "Endpoint", "Middleware",
    ],
    "Data/Artifacts": [
        "Dataset", "Model", "Training Data",
        "Fine-tuning", "Vector Database",
    ],
    "Pipelines": [
        "Inference", "Training", "Evaluation", "Pipeline",
    ],
}

ROLE_PHASE_MAP = {
    "Business and Data Understanding": ["Security Engineer", "Data Scientist"],
    "Data Preparation":                ["ML Engineer", "Data Scientist"],
    "AI Model Engineering":            ["ML Engineer", "Application Developer"],
    "AI Model Evaluation":             ["ML Engineer", "Security Engineer"],
    "Deployment":                      ["Application Developer", "System Administrator"],
    "Monitoring and Maintenance":      ["Security Engineer", "System Administrator"],
}

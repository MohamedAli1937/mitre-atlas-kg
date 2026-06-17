"""
Centralised configuration for the MITRE ATLAS Knowledge Graph project.
"""

import os

try:
    from dotenv import load_dotenv

    load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
except ImportError:
    pass

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

YAML_PATH = os.path.join("data", "ATLAS-latest.yaml")
OWASP_MAPPING_PATH = os.path.join("data", "owasp_atlas_mapping.json")

COMPONENT_TAXONOMY = {
    "AI Components": [
        "RAG",
        "LLM",
        "AI Agent",
        "Memory",
        "Embedding Model",
        "Orchestrator",
    ],
    "Infrastructure": [
        "API",
        "Cloud",
        "Service",
        "Repository",
        "Endpoint",
        "Middleware",
    ],
    "Data/Artifacts": [
        "Dataset",
        "Model",
        "Training Data",
        "Fine-tuning",
        "Vector Database",
    ],
    "Pipelines": ["Inference", "Training", "Evaluation", "Pipeline"],
}

ROLE_PHASE_MAP = {
    "Business and Data Understanding": ["Security Engineer", "Data Scientist"],
    "Data Preparation": ["ML Engineer", "Data Scientist"],
    "AI Model Engineering": ["ML Engineer", "Application Developer"],
    "AI Model Evaluation": ["ML Engineer", "Security Engineer"],
    "Deployment": ["Application Developer", "System Administrator"],
    "Monitoring and Maintenance": ["Security Engineer", "System Administrator"],
}

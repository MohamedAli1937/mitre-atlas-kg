# MITRE ATLAS Knowledge Graph & Reasoning Engine

> _A graph-native, AI-augmented security intelligence platform that transforms the static MITRE ATLAS™ taxonomy into a machine-reasonable, auditable, and queryable knowledge graph._

**Prepared for:** Voyverse, AI Governance Engineering — Summer 2026 Technical Assessment  
**Author:** Mohamed Ali BENBELGHITH

---

## Table of Contents

1. [Overview](#overview)
2. [Why a Graph? The Architectural Argument](#why-a-graph)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Knowledge Graph Schema](#knowledge-graph-schema)
6. [Tech Stack](#tech-stack)
7. [Personas & Use Cases](#personas--use-cases)
8. [Quick Start](#quick-start)
9. [Example Queries](#example-queries)
10. [Evaluation Results](#evaluation-results)
11. [Optional Extensions (Step 3)](#optional-extensions-step-3)
12. [LLM Disclosure](#llm-disclosure)

---

## Overview

MITRE ATLAS™ (Adversarial Threat Landscape for AI Systems) is the primary public taxonomy for adversarial attacks against AI/ML systems. In its native form it is a YAML file — human-readable, but not machine-queryable.

This project ingests ATLAS and models it as a **property graph in Neo4j**, then builds an application layer on top:

- A **Cypher query interface** for forensic security questions
- An **AI Reasoning Engine** that accepts a natural-language system description and returns a structured threat assessment grounded strictly in graph relationships
- A **cross-source enrichment layer** that aligns ATLAS techniques with the OWASP LLM Top 10 and NIST AI RMF (Govern 1.1, Map 1.2, Measure 2.1)
- A **PDF export pipeline** that produces traceable, citation-backed threat reports
- A **quantifiable evaluation suite** that measures query accuracy against a golden set

The design philosophy is **grounding over generation**: every answer the system produces is rooted in a physical graph traversal, not in free-text LLM inference. This makes the output auditable.

The system produces fully reproducible outputs and deliverables stored in the `assets/` directory, including:

- `demo.mp4` — full system demonstration video
- `THREAT_REPORT.md` — exemple of markdown threat modeling report
- `THREAT_REPORT.pdf` — exemple of formatted PDF export of a threat report
- `report.pdf` — additional evaluation/legacy report output
- `Voyverse Literature Review.xlsx` — enrichment and mapping dataset used in the knowledge graph pipeline

### Demo

[Watch Demo Video](assets/demo.mp4)

---

## Why a Graph?

The central architectural choice is Neo4j over a relational database. Here is the honest argument:

| Dimension              | Relational (PostgreSQL)              | Graph (Neo4j)                          |
| ---------------------- | ------------------------------------ | -------------------------------------- |
| Multi-hop traversal    | Expensive JOINs, O(n log n) per hop  | Index-Free Adjacency, O(1) per hop     |
| Schema evolution       | ALTER TABLE on live data is risky    | Add nodes/labels without migration     |
| Relationship semantics | Foreign keys are implicit            | Edges are named, directed, typed       |
| Query expressiveness   | SQL subqueries for paths are verbose | Cypher pattern matching is declarative |
| Heuristic enrichment   | Requires schema changes              | New node types inject cleanly          |

A concrete example: the query _"which techniques target the inference path of a RAG assistant, and which mitigations are owned by application developers?"_ requires a **4-hop traversal** across Tactic → Technique → Component → Mitigation → Role. In SQL this is four JOINs across normalized tables. In Cypher:

```cypher
MATCH (t:Technique)-[:HEURISTIC_TARGETS]->(c:Component {name: "RAG"})
MATCH (m:Mitigation)-[:MITIGATES]->(t)
MATCH (m)-[:HEURISTIC_OWNED_BY]->(r:Role {name: "Application Developer"})
RETURN t.name, m.name, r.name
```

Graph wins here — not as a dogma, but as the right tool for this data shape.

---

## Features

### Core (Step 2)

- **Graph-native ATLAS model** — Tactics, Techniques, Mitigations, Case Studies, and their semantic relationships ingested from official MITRE YAML
- **Batched UNWIND ingestion** — Full ATLAS dataset loaded in under 400ms via Neo4j batched transactions
- **Cypher query interface** — Direct forensic access to the graph
- **NL-to-Cypher assistant** — Natural language questions translated to Cypher with a self-correction loop on syntax errors
- **Interactive graph explorer** — Pyvis-powered real-time visualization

### Extensions (Step 3)

- **Reasoning Engine** — Describe any AI system in plain text; receive a structured, graph-grounded threat assessment
- **PDF Report Generator** — Produces a human-readable threat-modelling report with clickable citations back to MITRE documentation
- **OWASP LLM Top 10 Cross-Enrichment** — Aligns ATLAS techniques to the OWASP taxonomy via `[:MAPS_TO]` edges
- **NIST AI RMF Cross-Enrichment** — Aligns ATLAS techniques to NIST AI RMF governance categories (Govern, Map, Measure) via `[:MAPS_TO]`-style heuristic mappings.
- **Evaluation Suite** — Benchmarks Syntactic Accuracy and Grounding Accuracy against a curated golden set of NL questions

---

## Project Structure

```
mitre-atlas-kg/
├── st_app.py                  # Streamlit entry point
├── requirements.txt
├── .env.example
├── .prettierignore
├── assets/
│   ├── demo.mp4                         # Full system demonstration video
│   ├── THREAT_REPORT.md                 # Markdown threat modeling report
│   ├── THREAT_REPORT.pdf                # PDF threat report
│   ├── report.pdf                       # FINAL REPORT of the whole project
│   └── Voyverse_Literature_Review.xlsx  # Literature review + enrichment dataset
├── src/
│   ├── build_kg.py            # Ingestion pipeline
│   ├── llm_client.py          # Unified LLM wrapper
│   ├── query_assistant.py     # NL → Cypher translation
│   ├── pdf_generator.py       # PDF report engine
│   ├── update_source.py       # Automated data sync
│   └── config.py              # Centralized configuration
├── data/
│   ├── ATLAS-latest.yaml      # MITRE ATLAS source
│   ├── owasp_atlas_mapping.json
│   └── nist_ai_rmf_mapping.json
└── tests/
    ├── evaluate_assistant.py  # Benchmarking suite
    └── demo_queries.py       # Expert-authored Cypher tests
```

**Why this structure?**  
`src/` isolates business logic from the UI layer (`st_app.py`), making the graph engine independently testable. `tests/` is a first-class directory, not an afterthought, because evaluation was scoped as a deliverable, not a bonus. Graph HTML and PDF exports are generated in memory at runtime (not written to disk).

---

## Knowledge Graph Schema

```
(:Technique)-[:ACHIEVES]->(:Tactic)
(:Mitigation)-[:MITIGATES]->(:Technique)
(:CaseStudy)-[:EMPLOYS]->(:Technique)
(:OWASPCategory)-[:MAPS_TO]->(:Technique)
(:NISTCategory)-[:MAPS_TO]->(:Technique)
(:Technique)-[:HEURISTIC_TARGETS]->(:Component)
(:Mitigation)-[:HEURISTIC_OWNED_BY]->(:Role)
```

The bottom two relationship types are **heuristic** — they do not exist in the official ATLAS YAML but are inferred by the AI-enrichment pipeline. They are stored with a `source: "heuristic"` property so downstream queries can filter by provenance.

**Node labels and key properties:**

| Label            | Key Properties                                        |
| ---------------- | ----------------------------------------------------- |
| `:Technique`     | `id`, `name`, `description`, `url`                    |
| `:Tactic`        | `id`, `name`                                          |
| `:Mitigation`    | `id`, `name`, `description`, `url`                    |
| `:CaseStudy`     | `id`, `name`, `summary`                               |
| `:Component`     | `name` (e.g., `RAG`, `VectorDB`, `Orchestrator`)      |
| `:Role`          | `name` (e.g., `Application Developer`, `ML Engineer`) |
| `:OWASPCategory` | `id`, `name`                                          |
| `:NISTCategory`  | `id`, `name`                                          |

---

## Tech Stack

| Layer               | Technology                       | Why This, Not the Alternative                                                                                                                                        |
| ------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Graph DB            | Neo4j                            | Index-Free Adjacency for O(1) multi-hop; Cypher is expressive for path queries. Chose over TigerGraph (less Python tooling) and Amazon Neptune (local dev friction). |
| Frontend            | Streamlit                        | Fastest path from Python backend to interactive dashboard. Chose over FastAPI+React (overkill for a one-week assessment).                                            |
| Graph Visualization | Pyvis + NetworkX                 | Pyvis renders interactive HTML from NetworkX objects. Chose over D3.js (requires JS context switch).                                                                 |
| LLM Backend         | Ollama (Qwen2.5 / Llama3) + Groq | Ollama for offline/local runs; Groq for cloud-accelerated inference at 1.2s average latency. Chose over OpenAI to avoid cost dependency.                             |
| PDF Generation      | fpdf2                            | Lightweight, no LaTeX dependency at runtime. Chose over ReportLab (verbose API) and WeasyPrint (CSS-rendering overhead).                                             |
| Academic Report     | pylatex                          | Native LaTeX output for structured tables and math.                                                                                                                  |

---

## Personas & Use Cases

### Persona 1: The Security Auditor

_"I need to know which techniques have no associated mitigations in the current ATLAS version."_

```cypher
MATCH (t:Technique)
WHERE NOT (:Mitigation)-[:MITIGATES]->(t)
RETURN t.id, t.name
ORDER BY t.name
```

### Persona 2: The Application Developer

_"My team is deploying a RAG-based assistant. Which techniques specifically target RAG components, and what do we own?"_

```cypher
MATCH (t:Technique)-[:HEURISTIC_TARGETS]->(c:Component {name: "RAG"})
MATCH (m:Mitigation)-[:MITIGATES]->(t)
MATCH (m)-[:HEURISTIC_OWNED_BY]->(r:Role)
RETURN t.name AS Technique, m.name AS Mitigation, r.name AS Owner
```

### Persona 3: The Compliance Officer

_"Map our ATLAS exposure to OWASP LLM Top 10 for the board report."_

```cypher
MATCH (o:OWASPCategory)-[:MAPS_TO]->(t:Technique)
RETURN o.name AS OWASPRisk, collect(t.name) AS ATLASTechniques
ORDER BY o.id
```

---

## Quick Start

### Prerequisites

- Neo4j 5.x running locally (default bolt: `neo4j://localhost:7687`)
- Python 3.10+
- An LLM backend: [Ollama](https://ollama.ai) (local) or a Groq API key

### Installation

```bash
git clone https://github.com/MohamedAli1937/mitre-atlas-kg
cd mitre-atlas-kg
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and set:

```env
NEO4J_URI=neo4j://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
LLM_BACKEND=ollama          # or "groq" / "openai"
GROQ_API_KEY=               # if using Groq
```

### Build & Launch

```bash
# 1. Sync latest ATLAS data from MITRE
python src/update_source.py

# 2. Ingest into Neo4j (--ai-enrich runs LLM-based component extraction)
python src/build_kg.py --clean --ai-enrich

# 3. Launch the Streamlit dashboard
streamlit run st_app.py

# 4. (Optional) Run the evaluation suite
python tests/evaluate_assistant.py
```

---

## Example Queries

### 1. Techniques targeting the supply chain, with their case studies

```cypher
MATCH (ta:Tactic {name: "ML Supply Chain Compromise"})
MATCH (t:Technique)-[:ACHIEVES]->(ta)
MATCH (cs:CaseStudy)-[:EMPLOYS]->(t)
RETURN t.name, cs.name
```

### 2. Full mitigation chain for a specific technique

```cypher
MATCH (t:Technique {id: "AML.T0018"})
MATCH (m:Mitigation)-[:MITIGATES]->(t)
OPTIONAL MATCH (m)-[:HEURISTIC_OWNED_BY]->(r:Role)
RETURN t.name, m.name, r.name
```

### 3. Coverage gap analysis — techniques with no mitigations

```cypher
MATCH (t:Technique)
WHERE NOT (:Mitigation)-[:MITIGATES]->(t)
RETURN count(t) AS UnmitigatedCount, collect(t.name)[..5] AS Examples
```

### 4. OWASP ↔ ATLAS cross-mapping

```cypher
MATCH (o:OWASPCategory)-[:MAPS_TO]->(t:Technique)-[:ACHIEVES]->(ta:Tactic)
RETURN o.name, t.name, ta.name
ORDER BY o.id
```

---

## Evaluation Results

The evaluation suite (`tests/evaluate_assistant.py`) tests the NL-to-Cypher assistant against a golden set of 10 natural language questions with known correct graph patterns.

| Metric                | Score | Method                                      |
| --------------------- | ----- | ------------------------------------------- |
| Syntactic Correctness | 100%  | Cypher parser validation                    |
| Grounding Accuracy    | 80%   | Label/Relationship existence check in Neo4j |
| Average Latency       | 1.2s  | End-to-end (Groq backend)                   |

**Grounding Accuracy** measures whether the node labels and relationship types in the generated Cypher actually exist in the graph schema — a harder bar than syntactic validity alone.

---

## Optional Extensions (Step 3)

All four optional extensions from the brief are implemented:

| Extension               | Implementation                                                          | File                                                                                  |
| ----------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Reasoning Engine        | NL system description → structured threat assessment grounded in graph  | `src/query_assistant.py` + `st_app.py`                                                |
| Document Drafting       | PDF threat-modelling report with traceable MITRE citations              | `src/pdf_generator.py`                                                                |
| Cross-Source Enrichment | OWASP LLM Top 10 + NIST AI RMF aligned via `[:MAPS_TO]` heuristic edges | `src/build_kg.py` + `data/owasp_atlas_mapping.json` + `data/nist_ai_rmf_mapping.json` |
| Evaluation              | Syntactic + Grounding accuracy benchmarking suite                       | `tests/evaluate_assistant.py`                                                         |

## Development & Standards

To maintain code quality and consistency, this project uses the following tools:

- **[Black](https://github.com/psf/black)**: The uncompromising Python code formatter.
- **[Prettier](https://prettier.io/)**: For formatting Markdown, JSON, and YAML files.

To format the codebase:

```bash
# Format Python files
black .

# Format other files
npx prettier --write .
```

---

## LLM Disclosure

LLM tools were used during development of this project. Specifically:

- **Claude (Anthropic)** was used for drafting and iterating on this README and the technical report
- **Qwen2.5 / Llama3 via Ollama** are used at runtime for AI-driven component NER during graph enrichment
- **Groq (cloud)** is the default inference backend for the query assistant at evaluation time

All LLM-generated content in the application layer (threat assessments, Cypher queries) is strictly grounded in graph traversal results. The LLM generates the query; the graph provides the answer.

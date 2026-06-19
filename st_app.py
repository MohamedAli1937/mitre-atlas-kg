"""
Streamlit GUI for the MITRE ATLAS Knowledge Graph.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import re
import json
import datetime
import pandas as pd
import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as st_components
import subprocess

import config
from llm_client import LLMClientWrapper
from pdf_generator import generate_pdf_report
from query_assistant import (
    SYSTEM_PROMPT,
    extract_cypher,
    validate_cypher_safety,
    GraphExecutor,
)

DEFAULT_OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")

st.set_page_config(
    page_title="ATLAS Security Center",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    .stApp { font-family: 'Inter', sans-serif; }
    h1 { color: #e0e0e0; font-weight: 700; font-size: 1.75rem !important; letter-spacing: -0.02em; }
    h2 { color: #b0bec5; font-weight: 600; font-size: 1.25rem !important; }
    .status-pill { display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; }
    .status-online { background: rgba(0, 200, 150, 0.15); color: #00c896; border: 1px solid rgba(0, 200, 150, 0.3); }
    .status-offline { background: rgba(239, 83, 80, 0.15); color: #ef5350; border: 1px solid rgba(239, 83, 80, 0.3); }
    .step-label { padding: 6px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: 500; margin-bottom: 6px; background: rgba(0, 188, 212, 0.08); color: #80deea; border-left: 3px solid #00bcd4; }
    .sidebar-brand { font-size: 0.7rem; color: #607d8b; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.06); margin-top: 12px; }
</style>
""",
    unsafe_allow_html=True,
)


def check_neo4j_connection():
    try:
        executor = GraphExecutor()
        executor.driver.verify_connectivity()
        executor.close()
        return True
    except:
        return False


def load_owasp_mappings():
    try:
        mapping_path = os.path.join("data", "owasp_atlas_mapping.json")
        with open(mapping_path, encoding="utf-8") as f:
            data = json.load(f)
        mapping = {}
        for item in data.get("owasp_llm_to_mitre_atlas", {}).get("mappings", []):
            owasp_id = item["owasp_id"]
            owasp_name = item["owasp_name"]
            for tech in item.get("atlas_techniques", []):
                tech_id = tech["id"]
                if tech_id not in mapping:
                    mapping[tech_id] = []
                mapping[tech_id].append(f"{owasp_id} ({owasp_name})")
        return mapping
    except:
        return {}


def extract_components(llm, description):
    prompt = (
        "Extract the key architectural components from the following description of an AI system.\n"
        "Focus on security-relevant components: RAG, LLM, API, Orchestrator, Vector Database, Training Data, Fine-tuning, Cloud, Inference, Pipeline, Model, Dataset.\n\n"
        'Return ONLY a JSON list of strings, e.g. ["RAG", "LLM"].'
    )
    try:
        res = llm.generate_structured_json(prompt, f'Description:\n"{description}"')
        if res and isinstance(res, list):
            return res
        raise Exception("Invalid extraction")
    except:
        components = []
        for cat, keywords in config.COMPONENT_TAXONOMY.items():
            for kw in keywords:
                if kw.lower() in description.lower():
                    components.append(kw)
        return list(set(components))


def get_threats_for_components(components):
    executor = GraphExecutor()
    threats = []
    try:
        with executor.driver.session() as session:
            for comp in components:
                cypher = """
                MATCH (tech:Technique)-[:HEURISTIC_TARGETS]->(c:Component)
                WHERE c.name = $comp_name
                OPTIONAL MATCH (mit:Mitigation)-[:MITIGATES]->(tech)
                OPTIONAL MATCH (mit)-[:HEURISTIC_OWNED_BY]->(r:Role)
                OPTIONAL MATCH (mit)-[:HEURISTIC_APPLIES_TO]->(lp:LifecyclePhase)
                RETURN
                    tech.id AS Technique_ID,
                    tech.name AS Technique_Name,
                    tech.description AS Description,
                    collect(DISTINCT {
                        id: mit.id,
                        name: mit.name,
                        role: r.name,
                        phase: lp.name
                    }) AS Mitigations
                """
                result = session.run(cypher, comp_name=comp)
                for record in result:
                    threats.append(
                        {
                            "component": comp,
                            "tech_id": record["Technique_ID"],
                            "tech_name": record["Technique_Name"],
                            "description": record["Description"],
                            "mitigations": record["Mitigations"],
                        }
                    )
    finally:
        executor.close()
    return threats


def visualize_graph(components_list):
    executor = GraphExecutor()
    G = nx.MultiDiGraph()
    try:
        with executor.driver.session() as session:
            for comp in components_list:
                cypher = """
                MATCH (c:Component {name: $comp})<-[:HEURISTIC_TARGETS]-(t:Technique)-[:ACHIEVES]->(tac:Tactic)
                OPTIONAL MATCH (m:Mitigation)-[:MITIGATES]->(t)
                RETURN c.name as comp, t.id as tech, tac.name as tactic, m.id as mit
                LIMIT 20
                """
                res = session.run(cypher, comp=comp)
                for rec in res:
                    G.add_node(rec["comp"], label=rec["comp"], color="#00bcd4")
                    G.add_node(rec["tech"], label=rec["tech"], color="#ff9800")
                    G.add_node(rec["tactic"], label=rec["tactic"], color="#4caf50")
                    G.add_edge(rec["tech"], rec["comp"], label="TARGETS")
                    G.add_edge(rec["tech"], rec["tactic"], label="ACHIEVES")
                    if rec["mit"]:
                        G.add_node(rec["mit"], label=rec["mit"], color="#ef5350")
                        G.add_edge(rec["mit"], rec["tech"], label="MITIGATES")
    finally:
        executor.close()

    net = Network(
        height="400px",
        width="100%",
        bgcolor="#0e1117",
        font_color="white",
        notebook=True,
    )
    net.from_nx(G)
    net.toggle_physics(True)
    path = os.path.join("assets", "graph.html")
    net.show(path)
    return path


def generate_report_markdown(description, components, threats, owasp_mappings):
    report = []
    report.append("# AI Threat Modeling Report")
    report.append(f"**Generated**: {datetime.date.today().strftime('%B %d, %Y')}\n")
    report.append("## 1. System Overview")
    report.append(f"**Description**: {description}\n")
    report.append("**Identified Components**:")
    for comp in components:
        report.append(f"- {comp}")
    report.append("\n---\n")
    unique_techs = {t["tech_id"] for t in threats}
    report.append(
        f"## 2. Executive Summary\nIdentified **{len(unique_techs)} potential threats** based on architectural components.\n"
    )
    report.append("---")
    report.append("## 3. Detailed Threat Analysis")
    for t in threats:
        tech_id = t["tech_id"]
        ow_list = owasp_mappings.get(tech_id, [])
        owasp_str = ", ".join(ow_list) if ow_list else "None mapped"
        id_suffix = tech_id.split(".")[-1] if "." in tech_id else tech_id
        ref_link = f"https://atlas.mitre.org/techniques/{id_suffix}"
        report.append(f"### {tech_id}: {t['tech_name']}")
        report.append(f"- **Target Component**: {t['component']}")
        report.append(f"- **Reference**: [{tech_id}]({ref_link})")
        
        ow_str = ", ".join(t.get("owasp", [])) if t.get("owasp") else "None"
        ni_str = ", ".join(t.get("nist", [])) if t.get("nist") else "None"
        report.append(f"- **OWASP LLM Top 10**: {ow_str}")
        report.append(f"- **NIST AI RMF**: {ni_str}")

        if t["description"]:
            report.append(f"- **Description**: {t['description']}")
        valid_mits = [m for m in t["mitigations"] if m.get("id")]
        report.append(f"- **Mitigation Coverage**: {len(valid_mits)} identified.")
        if valid_mits:
            report.append("- **Recommendations**:")
            for m in valid_mits:
                m_suffix = m["id"].split(".")[-1] if "." in m["id"] else m["id"]
                m_link = f"https://atlas.mitre.org/mitigations/{m_suffix}"
                role_str = (
                    f" (Owner: {m['role']})" if m.get("role") else " (Owner: Unknown)"
                )
                phase_str = f" in {m['phase']} phase" if m.get("phase") else ""
                report.append(f"  - [{m['name']}]({m_link}){role_str}{phase_str}")
        report.append("")
    return "\n".join(report)


st.sidebar.markdown("### Configuration")
db_online = check_neo4j_connection()
if db_online:
    st.sidebar.markdown(
        '<span class="status-pill status-online">Neo4j Connected</span>',
        unsafe_allow_html=True,
    )
else:
    st.sidebar.markdown(
        '<span class="status-pill status-offline">Neo4j Offline</span>',
        unsafe_allow_html=True,
    )

st.sidebar.markdown("---")
provider = st.sidebar.selectbox(
    "LLM Provider", options=["Ollama", "OpenAI", "Groq (Free)"], index=0
)
provider_key = provider.replace(" (Free)", "")
if provider_key == "Ollama":
    model = st.sidebar.text_input("Model", value=DEFAULT_OLLAMA_MODEL)
    endpoint = st.sidebar.text_input("Host", value=DEFAULT_OLLAMA_HOST)
    api_key = None
elif provider_key == "Groq":
    model = st.sidebar.text_input("Model", value="llama-3.1-8b-instant")
    endpoint = LLMClientWrapper.GROQ_BASE_URL
    api_key = st.sidebar.text_input("API Key", type="password")
else:
    model = st.sidebar.text_input("Model", value="gpt-4o-mini")
    endpoint = "https://api.openai.com/v1"
    api_key = st.sidebar.text_input("API Key", type="password")

llm_client = LLMClientWrapper(provider_key, model, endpoint, api_key)

st.sidebar.markdown("---")
if st.sidebar.button("Run Evaluation Suite"):
    with st.spinner("Running benchmarks..."):
        eval_script = os.path.join("tests", "evaluate_assistant.py")
        result = subprocess.run(["python", eval_script], capture_output=True, text=True)
        st.sidebar.text_area("Evaluation Result", value=result.stdout, height=300)

st.sidebar.markdown("---")
st.sidebar.markdown(
    '<div class="sidebar-brand">MITRE ATLAS Knowledge Graph v1.6<br>Mohamed Ali</div>',
    unsafe_allow_html=True,
)

st.title("ATLAS Security Center")
tab_query, tab_threat, tab_stats = st.tabs(
    ["Query Assistant", "Threat Modeler", "Compliance & Stats"]
)

with tab_query:
    st.header("Natural Language Query")
    user_query = st.text_input(
        "Question",
        placeholder="e.g. Find all techniques targeting RAG components",
        label_visibility="collapsed",
    )
    if st.button("Run Query", key="nl_btn", type="primary"):
        if not user_query.strip():
            st.warning("Enter a question first.")
        elif not db_online:
            st.error("Neo4j is offline.")
        else:
            with st.spinner("Generating Cypher..."):
                try:
                    raw_output = llm_client.generate_completion(
                        SYSTEM_PROMPT, user_query
                    )
                    cypher = extract_cypher(raw_output)
                    st.subheader("Generated Cypher")
                    st.code(cypher, language="cypher")
                    is_safe, safety_err = validate_cypher_safety(cypher)
                    if not is_safe:
                        st.error(f"Safety guardrail: {safety_err}")
                    else:
                        st.success("Read-only verified. Executing...")
                        executor = GraphExecutor()
                        success, error = executor.execute_and_print(cypher)
                        if success:
                            with executor.driver.session() as s:
                                res = s.run(cypher)
                                keys = list(res.keys())
                                records = [
                                    dict(zip(keys, record.values())) for record in res
                                ]
                            executor.close()
                            if not records:
                                st.info("Query returned 0 records.")
                            else:
                                df = pd.DataFrame(records)
                                st.subheader("Results")
                                st.dataframe(df, use_container_width=True)
                        else:
                            executor.close()
                            st.warning(f"Execution error: {error}")
                            if any(
                                t in error.lower()
                                for t in ["syntax", "defined", "token", "variable"]
                            ):
                                st.markdown(
                                    '<div class="step-label">Auto-correcting query...</div>',
                                    unsafe_allow_html=True,
                                )
                                with st.spinner("Refining..."):
                                    raw_fix = llm_client.generate_correction(
                                        user_query, cypher, error, SYSTEM_PROMPT
                                    )
                                    fixed = extract_cypher(raw_fix)
                                    st.subheader("Corrected Cypher")
                                    st.code(fixed, language="cypher")
                                    safe2, err2 = validate_cypher_safety(fixed)
                                    if not safe2:
                                        st.error(f"Safety guardrail: {err2}")
                                    else:
                                        executor = GraphExecutor()
                                        ok2, e2 = executor.execute_and_print(fixed)
                                        if ok2:
                                            with executor.driver.session() as s:
                                                res = s.run(fixed)
                                                keys = list(res.keys())
                                                records = [
                                                    dict(zip(keys, record.values()))
                                                    for record in res
                                                ]
                                            executor.close()
                                            if not records:
                                                st.info(
                                                    "Corrected query returned 0 records."
                                                )
                                            else:
                                                df = pd.DataFrame(records)
                                                st.subheader("Results")
                                                st.dataframe(
                                                    df, use_container_width=True
                                                )
                                        else:
                                            executor.close()
                                            st.error(f"Correction also failed: {e2}")
                except Exception as e:
                    st.error(f"Error: {e}")

with tab_threat:
    st.header("AI System Threat Assessment")
    system_description = st.text_area(
        "System description",
        value="A RAG-based assistant using a vector database, an LLM orchestrator, and exposed via a public API.",
        height=80,
        label_visibility="collapsed",
    )
    if st.button("Generate Assessment", key="threat_btn", type="primary"):
        if not system_description.strip():
            st.warning("Enter a system description first.")
        elif not db_online:
            st.error("Neo4j is offline.")
        else:
            with st.spinner("Running threat assessment..."):
                st.markdown(
                    '<div class="step-label">Step 1 &mdash; Extracting components via LLM</div>',
                    unsafe_allow_html=True,
                )
                components_list = extract_components(llm_client, system_description)
                if not components_list:
                    st.warning("No components extracted.")
                else:
                    st.markdown(
                        f'<div class="step-label">Detected: {", ".join(components_list)}</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        '<div class="step-label">Step 2 &mdash; Querying knowledge graph</div>',
                        unsafe_allow_html=True,
                    )
                    threats = get_threats_for_components(components_list)
                    st.markdown(
                        '<div class="step-label">Step 3 &mdash; OWASP LLM Top 10 alignment</div>',
                        unsafe_allow_html=True,
                    )
                    owasp_mappings = load_owasp_mappings()
                    st.markdown(
                        '<div class="step-label">Step 4 &mdash; Compiling report</div>',
                        unsafe_allow_html=True,
                    )
                    report_md = generate_report_markdown(
                        system_description, components_list, threats, owasp_mappings
                    )
                    st.session_state["report_md"] = report_md
                    st.session_state["system_description"] = system_description
                    st.session_state["components_detected"] = components_list
                    st.session_state["threats_found"] = threats
                    st.session_state["assessment_done"] = True
                    st.success("Assessment complete.")

    if st.session_state.get("assessment_done"):
        report_md = st.session_state["report_md"]
        components_detected = st.session_state.get("components_detected", [])
        owasp_mappings = load_owasp_mappings()
        st.subheader("Graph Visualization")
        graph_path = visualize_graph(components_detected)
        with open(graph_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st_components.html(html_content, height=450)
        st.subheader("Export")
        col_md, col_pdf = st.columns(2)
        with col_md:
            st.download_button(
                label="Download Markdown",
                data=report_md,
                file_name="THREAT_REPORT.md",
                mime="text/markdown",
            )
        with col_pdf:
            try:
                pdf_filename = os.path.join("assets", "THREAT_REPORT.pdf")
                generate_pdf_report(
                    st.session_state["system_description"],
                    st.session_state["components_detected"],
                    st.session_state["threats_found"],
                    owasp_mappings,
                    pdf_filename,
                )
                with open(pdf_filename, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()
                st.download_button(
                    label="Download PDF",
                    data=pdf_bytes,
                    file_name="THREAT_REPORT.pdf",
                    mime="application/pdf",
                )
            except Exception as pe:
                st.error(f"PDF generation failed: {pe}")
        st.subheader("Report Preview")
        st.markdown(report_md)

with tab_stats:
    st.header("Intelligence Dashboard")
    if not db_online:
        st.error("Connect to Neo4j to view statistics.")
    else:
        from build_kg import AtlasIngestor

        ingestor = AtlasIngestor(
            config.NEO4J_URI, config.NEO4J_USER, config.NEO4J_PASSWORD
        )
        stats = ingestor.get_stats()
        ingestor.close()

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Techniques", stats["Techniques"])
        col2.metric("Mitigations", stats["Mitigations"])
        col3.metric("Case Studies", stats["CaseStudies"])
        col4.metric("Tactics", stats["Tactics"])

        st.subheader("Framework Coverage")
        total_techs = stats["Techniques"]
        unmitigated = stats["UnmitigatedTechniques"]
        coverage = ((total_techs - unmitigated) / total_techs) * 100
        st.progress(coverage / 100)
        st.markdown(
            f"**{coverage:.1f}%** of ATLAS techniques have official mitigations. "
            f"({unmitigated} coverage gaps identified)"
        )

        st.divider()
        st.subheader("Cross-Source Enrichment")
        src_col1, src_col2, src_col3 = st.columns(3)
        src_col1.metric("OWASP LLM Top 10", stats["OWASPCategories"])
        src_col2.metric("NIST AI RMF", stats["NISTCategories"])
        src_col3.metric("AI Components", stats["HeuristicComponents"])

        st.markdown("### Browse Mappings")
        map_type = st.radio(
            "Select Framework", ["OWASP LLM Top 10", "NIST AI RMF"], horizontal=True
        )

        executor = GraphExecutor()
        if map_type == "OWASP LLM Top 10":
            cypher = "MATCH (o:OWASPCategory)-[:MAPS_TO]->(t:Technique) RETURN o.id as ID, o.name as Category, collect(t.id) as ATLAS_Techniques"
        else:
            cypher = "MATCH (n:NISTCategory)-[:MAPS_TO]->(t:Technique) RETURN n.id as ID, n.name as Category, collect(t.id) as ATLAS_Techniques"

        with executor.driver.session() as s:
            res = s.run(cypher)
            records = [dict(r) for r in res]
        executor.close()

        if records:
            st.table(pd.DataFrame(records))
        else:
            st.info(
                "No mappings found in graph. Run ingestion with enrichment enabled."
            )
        executor.close()

        if records:
            st.table(pd.DataFrame(records))
        else:
            st.info(
                "No mappings found in graph. Run ingestion with enrichment enabled."
            )

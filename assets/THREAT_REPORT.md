# AI Threat Modeling Report
**Generated**: June 19, 2026

## 1. System Overview
**Description**: A RAG-based assistant using a vector database, an LLM orchestrator, and exposed via a public API.

**Identified Components**:
- RAG
- LLM

---

## 2. Executive Summary
Identified **59 potential threats** based on architectural components.

---
## 3. Detailed Threat Analysis
### AML.T0064: Gather RAG-Indexed Targets
- **Target Component**: RAG
- **Reference**: [AML.T0064](https://atlas.mitre.org/techniques/T0064)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0006: Active Scanning
- **Target Component**: RAG
- **Reference**: [AML.T0006](https://atlas.mitre.org/techniques/T0006)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0111: AI Supply Chain Reputation Inflation
- **Target Component**: RAG
- **Reference**: [AML.T0111](https://atlas.mitre.org/techniques/T0111)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0034: Cost Harvesting
- **Target Component**: RAG
- **Reference**: [AML.T0034](https://atlas.mitre.org/techniques/T0034)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 18 identified.
- **Recommendations**:
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Deployment phase

### AML.T0002.001: Models
- **Target Component**: RAG
- **Reference**: [AML.T0002.001](https://atlas.mitre.org/techniques/001)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 20 identified.
- **Recommendations**:
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: System Administrator) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Application Developer) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: System Administrator) in Deployment phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Data Scientist) in Deployment phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Application Developer) in Deployment phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Security Engineer) in Deployment phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Application Developer) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Data Scientist) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Security Engineer) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: ML Engineer) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Application Developer) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Application Developer) in Data Preparation phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Data Scientist) in Data Preparation phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Security Engineer) in Data Preparation phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: ML Engineer) in Data Preparation phase

### AML.T0085.000: RAG Databases
- **Target Component**: RAG
- **Reference**: [AML.T0085.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 18 identified.
- **Recommendations**:
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: Application Developer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Deployment phase

### AML.T0103: Deploy AI Agent
- **Target Component**: RAG
- **Reference**: [AML.T0103](https://atlas.mitre.org/techniques/T0103)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0073: Impersonation
- **Target Component**: RAG
- **Reference**: [AML.T0073](https://atlas.mitre.org/techniques/T0073)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0008.004: Serverless
- **Target Component**: RAG
- **Reference**: [AML.T0008.004](https://atlas.mitre.org/techniques/004)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0016.002: Generative AI
- **Target Component**: RAG
- **Reference**: [AML.T0016.002](https://atlas.mitre.org/techniques/002)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0093: Prompt Infiltration via Public-Facing Application
- **Target Component**: RAG
- **Reference**: [AML.T0093](https://atlas.mitre.org/techniques/T0093)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0071: False RAG Entry Injection
- **Target Component**: RAG
- **Reference**: [AML.T0071](https://atlas.mitre.org/techniques/T0071)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0011.000: Unsafe AI Artifacts
- **Target Component**: RAG
- **Reference**: [AML.T0011.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 64 identified.
- **Recommendations**:
  - [Code Signing](https://atlas.mitre.org/mitigations/M0013) (Owner: Application Developer) in Deployment phase
  - [Code Signing](https://atlas.mitre.org/mitigations/M0013) (Owner: System Administrator) in Deployment phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: ML Engineer) in Business and Data Understanding phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Application Developer) in Business and Data Understanding phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Security Engineer) in Business and Data Understanding phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Data Scientist) in Business and Data Understanding phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: ML Engineer) in AI Model Engineering phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Application Developer) in AI Model Engineering phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Security Engineer) in AI Model Engineering phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Data Scientist) in AI Model Engineering phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: ML Engineer) in Data Preparation phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Application Developer) in Data Preparation phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Security Engineer) in Data Preparation phase
  - [AI Bill of Materials](https://atlas.mitre.org/mitigations/M0023) (Owner: Data Scientist) in Data Preparation phase
  - [Restrict Library Loading](https://atlas.mitre.org/mitigations/M0011) (Owner: System Administrator) in Deployment phase
  - [Restrict Library Loading](https://atlas.mitre.org/mitigations/M0011) (Owner: Application Developer) in Deployment phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Application Developer) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Data Scientist) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Security Engineer) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: ML Engineer) in AI Model Engineering phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Application Developer) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Application Developer) in Data Preparation phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Data Scientist) in Data Preparation phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: Security Engineer) in Data Preparation phase
  - [Verify AI Artifacts](https://atlas.mitre.org/mitigations/M0014) (Owner: ML Engineer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Business and Data Understanding phase
  - [Vulnerability Scanning](https://atlas.mitre.org/mitigations/M0016) (Owner: Data Scientist) in Data Preparation phase
  - [Vulnerability Scanning](https://atlas.mitre.org/mitigations/M0016) (Owner: ML Engineer) in Data Preparation phase
  - [Vulnerability Scanning](https://atlas.mitre.org/mitigations/M0016) (Owner: Application Developer) in Data Preparation phase
  - [Vulnerability Scanning](https://atlas.mitre.org/mitigations/M0016) (Owner: Data Scientist) in AI Model Engineering phase
  - [Vulnerability Scanning](https://atlas.mitre.org/mitigations/M0016) (Owner: ML Engineer) in AI Model Engineering phase
  - [Vulnerability Scanning](https://atlas.mitre.org/mitigations/M0016) (Owner: Application Developer) in AI Model Engineering phase

### AML.T0036: Data from Information Repositories
- **Target Component**: RAG
- **Reference**: [AML.T0036](https://atlas.mitre.org/techniques/T0036)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0034.002: Agentic Resource Consumption
- **Target Component**: RAG
- **Reference**: [AML.T0034.002](https://atlas.mitre.org/techniques/002)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0002.000: Datasets
- **Target Component**: RAG
- **Reference**: [AML.T0002.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 8 identified.
- **Recommendations**:
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: System Administrator) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Application Developer) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: System Administrator) in Deployment phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Data Scientist) in Deployment phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Application Developer) in Deployment phase
  - [Limit Model Artifact Release](https://atlas.mitre.org/mitigations/M0001) (Owner: Security Engineer) in Deployment phase

### AML.T0051: LLM Prompt Injection
- **Target Component**: RAG
- **Reference**: [AML.T0051](https://atlas.mitre.org/techniques/T0051)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 63 identified.
- **Recommendations**:
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Business and Data Understanding phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase

### AML.T0095.000: Code Repositories
- **Target Component**: RAG
- **Reference**: [AML.T0095.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0082: RAG Credential Harvesting
- **Target Component**: RAG
- **Reference**: [AML.T0082](https://atlas.mitre.org/techniques/T0082)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 4 identified.
- **Recommendations**:
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: System Administrator) in Deployment phase

### AML.T0017.000: Adversarial AI Attacks
- **Target Component**: RAG
- **Reference**: [AML.T0017.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0070: RAG Poisoning
- **Target Component**: RAG
- **Reference**: [AML.T0070](https://atlas.mitre.org/techniques/T0070)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0002: Acquire Public AI Artifacts
- **Target Component**: RAG
- **Reference**: [AML.T0002](https://atlas.mitre.org/techniques/T0002)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 2 identified.
- **Recommendations**:
  - [Limit Public Release of Information](https://atlas.mitre.org/mitigations/M0000) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Limit Public Release of Information](https://atlas.mitre.org/mitigations/M0000) (Owner: Security Engineer) in Business and Data Understanding phase

### AML.T0011.003: Malicious Link
- **Target Component**: RAG
- **Reference**: [AML.T0011.003](https://atlas.mitre.org/techniques/003)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0085: Data from AI Services
- **Target Component**: RAG
- **Reference**: [AML.T0085](https://atlas.mitre.org/techniques/T0085)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 20 identified.
- **Recommendations**:
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: Application Developer) in Deployment phase
  - [AI Agent Tools Permissions Configuration](https://atlas.mitre.org/mitigations/M0028) (Owner: Application Developer) in Deployment phase
  - [AI Agent Tools Permissions Configuration](https://atlas.mitre.org/mitigations/M0028) (Owner: System Administrator) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: System Administrator) in Deployment phase

### AML.T0066: Retrieval Content Crafting
- **Target Component**: RAG
- **Reference**: [AML.T0066](https://atlas.mitre.org/techniques/T0066)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0077: LLM Response Rendering
- **Target Component**: LLM
- **Reference**: [AML.T0077](https://atlas.mitre.org/techniques/T0077)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0061: LLM Prompt Self-Replication
- **Target Component**: LLM
- **Reference**: [AML.T0061](https://atlas.mitre.org/techniques/T0061)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 36 identified.
- **Recommendations**:
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase

### AML.T0071: False RAG Entry Injection
- **Target Component**: LLM
- **Reference**: [AML.T0071](https://atlas.mitre.org/techniques/T0071)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0008.005: AI Service Proxies
- **Target Component**: LLM
- **Reference**: [AML.T0008.005](https://atlas.mitre.org/techniques/005)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0016.002: Generative AI
- **Target Component**: LLM
- **Reference**: [AML.T0016.002](https://atlas.mitre.org/techniques/002)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0091.000: Application Access Token
- **Target Component**: LLM
- **Reference**: [AML.T0091.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0104: Publish Poisoned AI Agent Tool
- **Target Component**: LLM
- **Reference**: [AML.T0104](https://atlas.mitre.org/techniques/T0104)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0078: Drive-by Compromise
- **Target Component**: LLM
- **Reference**: [AML.T0078](https://atlas.mitre.org/techniques/T0078)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0080: AI Agent Context Poisoning
- **Target Component**: LLM
- **Reference**: [AML.T0080](https://atlas.mitre.org/techniques/T0080)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 12 identified.
- **Recommendations**:
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Security Engineer) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: System Administrator) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: ML Engineer) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Application Developer) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Security Engineer) in AI Model Engineering phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: System Administrator) in AI Model Engineering phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: ML Engineer) in AI Model Engineering phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Application Developer) in AI Model Engineering phase

### AML.T0056: Extract LLM System Prompt
- **Target Component**: LLM
- **Reference**: [AML.T0056](https://atlas.mitre.org/techniques/T0056)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 36 identified.
- **Recommendations**:
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase

### AML.T0093: Prompt Infiltration via Public-Facing Application
- **Target Component**: LLM
- **Reference**: [AML.T0093](https://atlas.mitre.org/techniques/T0093)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0051.001: Indirect
- **Target Component**: LLM
- **Reference**: [AML.T0051.001](https://atlas.mitre.org/techniques/001)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 21 identified.
- **Recommendations**:
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Business and Data Understanding phase

### AML.T0052: Phishing
- **Target Component**: LLM
- **Reference**: [AML.T0052](https://atlas.mitre.org/techniques/T0052)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 46 identified.
- **Recommendations**:
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in AI Model Evaluation phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Business and Data Understanding phase

### AML.T0034: Cost Harvesting
- **Target Component**: LLM
- **Reference**: [AML.T0034](https://atlas.mitre.org/techniques/T0034)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 18 identified.
- **Recommendations**:
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Deployment phase

### AML.T0054: LLM Jailbreak
- **Target Component**: LLM
- **Reference**: [AML.T0054](https://atlas.mitre.org/techniques/T0054)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 36 identified.
- **Recommendations**:
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase

### AML.T0090: OS Credential Dumping
- **Target Component**: LLM
- **Reference**: [AML.T0090](https://atlas.mitre.org/techniques/T0090)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0094: Delay Execution of LLM Instructions
- **Target Component**: LLM
- **Reference**: [AML.T0094](https://atlas.mitre.org/techniques/T0094)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0080.001: Thread
- **Target Component**: LLM
- **Reference**: [AML.T0080.001](https://atlas.mitre.org/techniques/001)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0084.003: Call Chains
- **Target Component**: LLM
- **Reference**: [AML.T0084.003](https://atlas.mitre.org/techniques/003)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0079: Stage Capabilities
- **Target Component**: LLM
- **Reference**: [AML.T0079](https://atlas.mitre.org/techniques/T0079)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0011.002: Poisoned AI Agent Tool
- **Target Component**: LLM
- **Reference**: [AML.T0011.002](https://atlas.mitre.org/techniques/002)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0073: Impersonation
- **Target Component**: LLM
- **Reference**: [AML.T0073](https://atlas.mitre.org/techniques/T0073)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0067: LLM Trusted Output Components Manipulation
- **Target Component**: LLM
- **Reference**: [AML.T0067](https://atlas.mitre.org/techniques/T0067)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0102: Generate Malicious Commands
- **Target Component**: LLM
- **Reference**: [AML.T0102](https://atlas.mitre.org/techniques/T0102)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0051: LLM Prompt Injection
- **Target Component**: LLM
- **Reference**: [AML.T0051](https://atlas.mitre.org/techniques/T0051)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 63 identified.
- **Recommendations**:
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Deployment phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Control Access to AI Models and Data in Production](https://atlas.mitre.org/mitigations/M0019) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Business and Data Understanding phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase

### AML.T0010.005: AI Agent Tool
- **Target Component**: LLM
- **Reference**: [AML.T0010.005](https://atlas.mitre.org/techniques/005)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0062: Discover LLM Hallucinations
- **Target Component**: LLM
- **Reference**: [AML.T0062](https://atlas.mitre.org/techniques/T0062)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 48 identified.
- **Recommendations**:
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: System Administrator) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Application Developer) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Data Scientist) in Deployment phase
  - [Restrict Number of AI Model Queries](https://atlas.mitre.org/mitigations/M0004) (Owner: Security Engineer) in Deployment phase

### AML.T0108: AI Agent
- **Target Component**: LLM
- **Reference**: [AML.T0108](https://atlas.mitre.org/techniques/T0108)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0065: LLM Prompt Crafting
- **Target Component**: LLM
- **Reference**: [AML.T0065](https://atlas.mitre.org/techniques/T0065)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0057: LLM Data Leakage
- **Target Component**: LLM
- **Reference**: [AML.T0057](https://atlas.mitre.org/techniques/T0057)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 42 identified.
- **Recommendations**:
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Validate AI Model](https://atlas.mitre.org/mitigations/M0008) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Validate AI Model](https://atlas.mitre.org/mitigations/M0008) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Validate AI Model](https://atlas.mitre.org/mitigations/M0008) (Owner: System Administrator) in AI Model Evaluation phase
  - [Validate AI Model](https://atlas.mitre.org/mitigations/M0008) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Validate AI Model](https://atlas.mitre.org/mitigations/M0008) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [Validate AI Model](https://atlas.mitre.org/mitigations/M0008) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase

### AML.T0082: RAG Credential Harvesting
- **Target Component**: LLM
- **Reference**: [AML.T0082](https://atlas.mitre.org/techniques/T0082)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 4 identified.
- **Recommendations**:
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: System Administrator) in Deployment phase

### AML.T0086: Exfiltration via AI Agent Tool Invocation
- **Target Component**: LLM
- **Reference**: [AML.T0086](https://atlas.mitre.org/techniques/T0086)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 39 identified.
- **Recommendations**:
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Business and Data Understanding phase
  - [Restrict AI Agent Tool Invocation on Untrusted Data](https://atlas.mitre.org/mitigations/M0030) (Owner: Application Developer) in Deployment phase
  - [Restrict AI Agent Tool Invocation on Untrusted Data](https://atlas.mitre.org/mitigations/M0030) (Owner: System Administrator) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: System Administrator) in Deployment phase
  - [AI Agent Tools Permissions Configuration](https://atlas.mitre.org/mitigations/M0028) (Owner: Application Developer) in Deployment phase
  - [AI Agent Tools Permissions Configuration](https://atlas.mitre.org/mitigations/M0028) (Owner: System Administrator) in Deployment phase
  - [Human In-the-Loop for AI Agent Actions](https://atlas.mitre.org/mitigations/M0029) (Owner: Application Developer) in Deployment phase
  - [Human In-the-Loop for AI Agent Actions](https://atlas.mitre.org/mitigations/M0029) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: Application Developer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Deployment phase

### AML.T0080.000: Memory
- **Target Component**: LLM
- **Reference**: [AML.T0080.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 12 identified.
- **Recommendations**:
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Security Engineer) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: System Administrator) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: ML Engineer) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Application Developer) in Deployment phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Security Engineer) in AI Model Engineering phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: System Administrator) in AI Model Engineering phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: ML Engineer) in AI Model Engineering phase
  - [Memory Hardening](https://atlas.mitre.org/mitigations/M0031) (Owner: Application Developer) in AI Model Engineering phase

### AML.T0052.000: Spearphishing via Social Engineering LLM
- **Target Component**: LLM
- **Reference**: [AML.T0052.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 46 identified.
- **Recommendations**:
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Data Preparation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in AI Model Engineering phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Deployment phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in AI Model Evaluation phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Security Engineer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Application Developer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: ML Engineer) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: Data Scientist) in Business and Data Understanding phase
  - [User Training](https://atlas.mitre.org/mitigations/M0018) (Owner: System Administrator) in Business and Data Understanding phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in AI Model Engineering phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in Deployment phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: System Administrator) in AI Model Evaluation phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Deepfake Detection](https://atlas.mitre.org/mitigations/M0034) (Owner: Application Developer) in AI Model Evaluation phase

### AML.T0051.000: Direct
- **Target Component**: LLM
- **Reference**: [AML.T0051.000](https://atlas.mitre.org/techniques/000)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 21 identified.
- **Recommendations**:
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Business and Data Understanding phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase

### AML.T0053: AI Agent Tool Invocation
- **Target Component**: LLM
- **Reference**: [AML.T0053](https://atlas.mitre.org/techniques/T0053)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 75 identified.
- **Recommendations**:
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: System Administrator) in Deployment phase
  - [Privileged AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0026) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Application Developer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: System Administrator) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Model Alignment](https://atlas.mitre.org/mitigations/M0022) (Owner: ML Engineer) in Deployment phase
  - [Human In-the-Loop for AI Agent Actions](https://atlas.mitre.org/mitigations/M0029) (Owner: Application Developer) in Deployment phase
  - [Human In-the-Loop for AI Agent Actions](https://atlas.mitre.org/mitigations/M0029) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guardrails](https://atlas.mitre.org/mitigations/M0020) (Owner: ML Engineer) in AI Model Engineering phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: System Administrator) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Security Engineer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Application Developer) in Deployment phase
  - [Segmentation of AI Agent Components](https://atlas.mitre.org/mitigations/M0032) (Owner: Data Scientist) in Deployment phase
  - [Restrict AI Agent Tool Invocation on Untrusted Data](https://atlas.mitre.org/mitigations/M0030) (Owner: Application Developer) in Deployment phase
  - [Restrict AI Agent Tool Invocation on Untrusted Data](https://atlas.mitre.org/mitigations/M0030) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Engineering phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in AI Model Evaluation phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: System Administrator) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Security Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: ML Engineer) in Deployment phase
  - [Generative AI Guidelines](https://atlas.mitre.org/mitigations/M0021) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Deployment phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Data Preparation phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: ML Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Data Scientist) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Security Engineer) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: System Administrator) in Business and Data Understanding phase
  - [Input and Output Validation for AI Agent Components](https://atlas.mitre.org/mitigations/M0033) (Owner: Application Developer) in Business and Data Understanding phase
  - [AI Agent Tools Permissions Configuration](https://atlas.mitre.org/mitigations/M0028) (Owner: Application Developer) in Deployment phase
  - [AI Agent Tools Permissions Configuration](https://atlas.mitre.org/mitigations/M0028) (Owner: System Administrator) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: Application Developer) in Deployment phase
  - [Single-User AI Agent Permissions Configuration](https://atlas.mitre.org/mitigations/M0027) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Monitoring and Maintenance phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Security Engineer) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: System Administrator) in Deployment phase
  - [AI Telemetry Logging](https://atlas.mitre.org/mitigations/M0024) (Owner: Application Developer) in Deployment phase

### AML.T0060: Publish Hallucinated Entities
- **Target Component**: LLM
- **Reference**: [AML.T0060](https://atlas.mitre.org/techniques/T0060)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0068: LLM Prompt Obfuscation
- **Target Component**: LLM
- **Reference**: [AML.T0068](https://atlas.mitre.org/techniques/T0068)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0034.002: Agentic Resource Consumption
- **Target Component**: LLM
- **Reference**: [AML.T0034.002](https://atlas.mitre.org/techniques/002)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0069: Discover LLM System Information
- **Target Component**: LLM
- **Reference**: [AML.T0069](https://atlas.mitre.org/techniques/T0069)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0092: Manipulate User LLM Chat History
- **Target Component**: LLM
- **Reference**: [AML.T0092](https://atlas.mitre.org/techniques/T0092)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

### AML.T0069.001: System Instruction Keywords
- **Target Component**: LLM
- **Reference**: [AML.T0069.001](https://atlas.mitre.org/techniques/001)
- **OWASP LLM Top 10**: None
- **NIST AI RMF**: None
- **Mitigation Coverage**: 0 identified.

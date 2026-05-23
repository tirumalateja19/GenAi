# Applied Generative AI Development

Welcome to my Generative AI learning repository! This project tracks my progress in building production-ready AI applications, with a specific focus on bridging Python-based AI microservices with modern full-stack environments like React and Node.js.

## 🚀 Current Progress: Phase 1 (Environment & Foundations)

### System Architecture & Workflow
* **Environment Isolation:** Configured Python virtual environments (`venv`) to sandbox project dependencies and prevent global system conflicts.
* **Dependency Management:** Implemented reproducible builds using `pip freeze` and `requirements.txt`.
* **Security & Version Control:** Configured `.gitignore` to securely exclude heavy local environments (`myenv/`), cache files (`__pycache__/`), and sensitive API keys (`.env`).
* **Microservice Planning:** Formulated a backend architecture to securely connect a Python AI service (LangChain) to a Node.js gateway and React frontend.

### API Infrastructure & Economics
* Configured and installed the core applied AI toolkit: `langchain`, `langgraph`, `openai`, `google-generativeai`, `mcp`, `huggingface_hub`, and `pydantic`.
* Evaluated API tier economics, rate limits (RPM, TPM, RPD), and token structures across OpenAI (GPT-4o) and Google Gemini (Flash/Pro) models.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.14.0
* **AI Frameworks:** LangChain, LangGraph, Model Context Protocol (MCP)
* **API Integrations:** OpenAI, Google Gemini
* **Environment Tooling:** Git, VS Code, pip

## ⏭️ Up Next
* Running open-source models locally using Ollama and Docker.
* Building data ingestion and Retrieval-Augmented Generation (RAG) pipelines.
* Designing stateful AI systems and agentic workflows using LangGraph.

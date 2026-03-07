# 🛩️ DAL-Aware Agentic RAG for DO-178C Compliance

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An intelligent agentic RAG system that automates DO-178C aerospace software compliance verification — with full Development Assurance Level (DAL) awareness.**

[Features](#-features) · [Architecture](#-architecture) · [Quickstart](#-quickstart) · [Roadmap](#-roadmap) · [Contributing](#-contributing)

</div>

---

## 🧠 The Problem

DO-178C is the primary safety standard governing software in airborne systems. Compliance verification is:
- **Manual and error-prone** — engineers must cross-reference hundreds of pages
- **DAL-sensitive** — a DAL-A system requires far stricter verification than DAL-D
- **High-stakes** — mistakes can ground aircraft or delay certification by months

> This project automates that process using an agentic RAG architecture that *remembers* the project's DAL and filters all compliance answers accordingly.

---

## ✨ Features

- 🎯 **DAL-Aware Retrieval** — agent establishes and "remembers" the project's DAL (A/B/C/D); all ChromaDB retrievals are dynamically filtered through this context
- 📄 **PDF Ingestion Pipeline** — ingest DO-178C compliance documents and chunk them with DAL metadata tagging
- 🤖 **Local LLM** — runs on Phi-3-mini via HuggingFace (no API key needed, privacy-first)
- 🔍 **Citation-Backed Answers** — every compliance answer includes source references for traceability
- ✅ **Verification & Coverage Analysis** — answers structured for verification, traceability, and coverage per DO-178C objectives
- 🔒 **Secure by Design** — fully local, no data sent to external APIs

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Engineer Interface                  │
│         (Query: "What are DAL-A test objectives?")  │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│              DAL Context Agent (LangChain)           │
│   Memory: Current DAL = A  │  Goal: Verify Reqs     │
└───────────┬───────────────────────────┬─────────────┘
            │                           │
            ▼                           ▼
┌───────────────────┐       ┌───────────────────────┐
│  PDF Ingestion    │       │   DAL Metadata Filter  │
│  PyPDF +          │──────▶│   (A / B / C / D)      │
│  Sentence-Trans.  │       └───────────┬────────────┘
└───────────────────┘                   │
                                        ▼
                            ┌───────────────────────┐
                            │  ChromaDB Vector Store │
                            │  (DAL-tagged chunks)   │
                            └───────────┬────────────┘
                                        │
                                        ▼
                            ┌───────────────────────┐
                            │   Phi-3-mini LLM       │
                            │   (HuggingFace Local)  │
                            └───────────┬────────────┘
                                        │
                                        ▼
                    ┌───────────────────────────────────┐
                    │  DAL-Specific Compliance Response  │
                    │  + Citations + Traceability Links  │
                    └───────────────────────────────────┘
```

---

## 🚀 Quickstart

### Prerequisites
- Python 3.10+
- ~4GB RAM (for Phi-3-mini)
- No GPU required (CPU inference supported)

### Installation

```bash
# Clone the repo
git clone https://github.com/YashVermaTech/dal-aware-rag.git
cd dal-aware-rag

# Install dependencies
pip install -r requirements.txt
```

### Run the Demo

```bash
python examples/demo.py
```

### Basic Usage

```python
from src.agent.dal_agent import DALAwareAgent

# Initialize agent and set project DAL
agent = DALAwareAgent()
agent.set_dal("A")  # Sets DAL-A context for all subsequent queries

# Ingest your DO-178C compliance documents
agent.ingest_documents("data/sample_docs/")

# Query with full DAL-aware filtering
response = agent.query("What are the structural coverage requirements?")
print(response.answer)
print(response.citations)
```

---

## 📁 Project Structure

```
dal-aware-rag/
│
├── src/
│   ├── agent/
│   │   ├── dal_agent.py       # Core DAL-aware agent logic
│   │   └── memory.py          # DAL context memory module
│   ├── rag/
│   │   ├── ingestor.py        # PDF ingestion & chunking pipeline
│   │   ├── retriever.py       # ChromaDB retrieval + DAL filtering
│   │   └── embeddings.py      # Sentence-Transformers setup
│   └── utils/
│       └── config.py          # Configuration & constants
│
├── data/
│   └── sample_docs/           # Sample compliance documents
│
├── examples/
│   └── demo.py                # Quick start demo
│
├── tests/
│   └── test_agent.py          # Unit tests
│
├── requirements.txt
├── CONTRIBUTING.md
├── ROADMAP.md
└── LICENSE
```

---

## 📦 Requirements

```
langchain>=0.2.0
langchain-community>=0.2.0
chromadb>=0.5.0
sentence-transformers>=3.0.0
transformers>=4.40.0
pypdf>=4.0.0
torch>=2.0.0
python-dotenv>=1.0.0
```

---

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md) for the full plan. Key upcoming features:
- [ ] Web UI (Streamlit / Gradio)
- [ ] Support for ARP4754A and ARP4761 standards
- [ ] Multi-document cross-referencing
- [ ] Export compliance reports to PDF

---

## 🤝 Contributing

Contributions are welcome from both aerospace engineers and ML developers! See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## 👤 Author

**Yash Verma** — AI Engineer & ML Consultant
- Former Deep Learning Engineer @ Airbus Aerostructures
- M.Sc. Aerospace Engineering, TU Darmstadt
- [GitHub](https://github.com/YashVermaTech) · [Email](mailto:yashverma25104@gmail.com)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

> ⚠️ **Disclaimer:** This tool is intended to assist engineers in compliance workflows. It does not replace formal certification processes or qualified tool assessments under DO-330.

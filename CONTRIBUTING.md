# 🤝 Contributing to DAL-Aware RAG

First off — thank you for considering contributing! This project sits at the intersection of aerospace engineering and AI, and we welcome contributions from **both domains**.

---

## 👥 Who Should Contribute?

**Aerospace / Avionics Engineers:**
- Improve accuracy of DO-178C objective coverage
- Add support for additional standards (ARP4754A, ARP4761, DO-254)
- Review and validate compliance responses for correctness
- Contribute sample (non-proprietary) compliance document structures

**ML / AI Developers:**
- Improve the RAG pipeline (chunking, embeddings, retrieval quality)
- Add support for alternative LLMs (Mistral, LLaMA, Ollama)
- Build the Streamlit/Gradio web UI
- Write tests and improve code quality
- Optimize for performance and memory efficiency

---

## 🚀 Getting Started

### 1. Fork & Clone

```bash
git fork https://github.com/YashVermaTech/dal-aware-rag
git clone https://github.com/YOUR_USERNAME/dal-aware-rag.git
cd dal-aware-rag
```

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

---

## 📋 How to Contribute

### Reporting Bugs
- Open a [GitHub Issue](../../issues/new?template=bug_report.md)
- Include: Python version, OS, error message, steps to reproduce

### Suggesting Features
- Open a [GitHub Issue](../../issues/new?template=feature_request.md)
- Check the [Roadmap](ROADMAP.md) first — it may already be planned

### Submitting a Pull Request
1. Make your changes on your branch
2. Write or update tests in `tests/`
3. Make sure existing tests pass: `python -m pytest tests/`
4. Write a clear PR description explaining *what* and *why*
5. Reference any related issues with `Fixes #123`

---

## 🧹 Code Style

- Follow **PEP 8** for Python code
- Use **type hints** wherever possible
- Write **docstrings** for all public functions and classes
- Keep functions small and focused — one responsibility per function

```python
# Good ✅
def filter_chunks_by_dal(chunks: list[dict], dal_level: str) -> list[dict]:
    """
    Filter document chunks to only include those matching the given DAL level.
    
    Args:
        chunks: List of document chunks with metadata
        dal_level: DAL level string ('A', 'B', 'C', or 'D')
    
    Returns:
        Filtered list of chunks matching the DAL level
    """
    return [c for c in chunks if c["metadata"].get("dal") == dal_level]
```

---

## ✅ Commit Message Format

Use clear, descriptive commit messages:

```
feat: add DAL-B filtering support to retriever
fix: resolve PDF ingestion crash on empty pages
docs: update quickstart with Docker instructions
test: add unit tests for DAL context memory
refactor: simplify chunk metadata tagging logic
```

---

## 🛡️ Important Notes

- **Do NOT contribute proprietary or confidential aerospace documents** — only use publicly available or synthetic sample data
- This project is for **research and educational purposes** — see the disclaimer in README.md
- Be respectful and constructive in all discussions — see our [Code of Conduct](CODE_OF_CONDUCT.md)

---

## 📬 Questions?

Open a [Discussion](../../discussions) or reach out to [@YashVermaTech](https://github.com/YashVermaTech).

Thank you for helping make aerospace compliance safer and smarter! 🛩️

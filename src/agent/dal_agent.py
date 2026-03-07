"""
DAL-Aware Agent — Core agent logic for DO-178C compliance queries.
"""

from src.rag.retriever import DALRetriever
from src.agent.memory import DALMemory


class DALAwareAgent:
    """
    An agentic RAG system that maintains DAL context
    and filters all compliance retrievals accordingly.
    """

    def __init__(self):
        self.memory = DALMemory()
        self.retriever = DALRetriever()

    def set_dal(self, dal_level: str) -> None:
        """Set and remember the project DAL level (A/B/C/D)."""
        assert dal_level in ["A", "B", "C", "D"], "DAL must be A, B, C, or D"
        self.memory.set_dal(dal_level)
        print(f"✅ DAL context set to: DAL-{dal_level}")

    def ingest_documents(self, docs_path: str) -> None:
        """Ingest DO-178C compliance PDFs into the vector store."""
        self.retriever.ingest(docs_path)

    def query(self, question: str) -> dict:
        """Query the agent with DAL-aware filtering."""
        dal = self.memory.get_dal()
        if not dal:
            raise ValueError("DAL level not set. Call set_dal() first.")
        return self.retriever.retrieve(question, dal_level=dal)

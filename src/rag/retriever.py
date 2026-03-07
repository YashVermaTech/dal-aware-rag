"""
DAL-Aware Retriever — ChromaDB retrieval with DAL metadata filtering.
"""

import chromadb
from chromadb.utils import embedding_functions
from src.rag.ingestor import ingest_documents


class DALRetriever:
    """
    Handles document ingestion into ChromaDB and
    DAL-filtered semantic retrieval.
    """

    def __init__(self, collection_name: str = "do178c_docs"):
        self.client = chromadb.Client()
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn
        )

    def ingest(self, docs_path: str, dal_level: str = "A") -> None:
        """Ingest documents into ChromaDB with DAL metadata."""
        chunks = ingest_documents(docs_path, dal_level)
        self.collection.add(
            documents=[c["text"] for c in chunks],
            metadatas=[c["metadata"] for c in chunks],
            ids=[f"chunk_{i}" for i in range(len(chunks))]
        )

    def retrieve(self, query: str, dal_level: str, n_results: int = 5) -> dict:
        """
        Retrieve relevant chunks filtered by DAL level.
        
        Args:
            query: The compliance question
            dal_level: DAL level to filter by
            n_results: Number of chunks to retrieve
        
        Returns:
            Dict with 'answer_chunks' and 'citations'
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where={"dal": dal_level}
        )
        chunks = results["documents"][0]
        metadatas = results["metadatas"][0]
        citations = [
            f"{m['source']} (page {m['page']})" for m in metadatas
        ]
        return {
            "answer_chunks": chunks,
            "citations": citations,
            "dal_level": dal_level
        }

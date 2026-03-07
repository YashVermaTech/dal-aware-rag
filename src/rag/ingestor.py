"""
PDF Ingestion Pipeline — Loads and chunks DO-178C compliance documents
with DAL metadata tagging for ChromaDB.
"""

from pypdf import PdfReader
from tqdm import tqdm
import os


def load_pdf(filepath: str) -> list[dict]:
    """
    Load a PDF and return a list of page dicts with text and metadata.
    
    Args:
        filepath: Path to the PDF file
    
    Returns:
        List of dicts with 'text', 'page', and 'source' keys
    """
    reader = PdfReader(filepath)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages.append({
                "text": text.strip(),
                "page": i + 1,
                "source": os.path.basename(filepath)
            })
    return pages


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Split text into overlapping chunks for better retrieval.
    
    Args:
        text: Input text to chunk
        chunk_size: Maximum characters per chunk
        overlap: Overlapping characters between chunks
    
    Returns:
        List of text chunks
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def ingest_documents(docs_path: str, dal_level: str) -> list[dict]:
    """
    Ingest all PDFs from a folder, chunk them, and tag with DAL metadata.
    
    Args:
        docs_path: Path to folder containing PDF files
        dal_level: DAL level to tag all chunks with ('A', 'B', 'C', 'D')
    
    Returns:
        List of chunk dicts ready for ChromaDB insertion
    """
    all_chunks = []
    pdf_files = [f for f in os.listdir(docs_path) if f.endswith(".pdf")]

    for filename in tqdm(pdf_files, desc="Ingesting documents"):
        filepath = os.path.join(docs_path, filename)
        pages = load_pdf(filepath)
        for page in pages:
            for chunk in chunk_text(page["text"]):
                all_chunks.append({
                    "text": chunk,
                    "metadata": {
                        "dal": dal_level,
                        "source": page["source"],
                        "page": page["page"]
                    }
                })

    print(f"✅ Ingested {len(all_chunks)} chunks from {len(pdf_files)} documents")
    return all_chunks

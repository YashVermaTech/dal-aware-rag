"""
Embeddings setup — Sentence-Transformers configuration.
"""

from sentence_transformers import SentenceTransformer


def get_embedding_model(model_name: str = "all-MiniLM-L6-v2") -> SentenceTransformer:
    """
    Load and return a SentenceTransformer embedding model.
    
    Args:
        model_name: HuggingFace model name
    
    Returns:
        Loaded SentenceTransformer model
    """
    print(f"Loading embedding model: {model_name}")
    return SentenceTransformer(model_name)


def embed_texts(texts: list[str], model_name: str = "all-MiniLM-L6-v2") -> list:
    """
    Generate embeddings for a list of texts.
    
    Args:
        texts: List of strings to embed
        model_name: HuggingFace model name
    
    Returns:
        List of embedding vectors
    """
    model = get_embedding_model(model_name)
    return model.encode(texts, show_progress_bar=True).tolist()

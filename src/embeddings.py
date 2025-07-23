from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL_NAME

_model = SentenceTransformer(EMBED_MODEL_NAME)

def embed(texts):
    """Return list of embedding vectors for list[str]."""
    return _model.encode(texts, show_progress_bar=False).tolist()

"""
Embedding backend switcher.
Use local MiniLM by default; set USE_OPENAI=true to call OpenAI ada‑002.
"""
import os
from sentence_transformers import SentenceTransformer

USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"

if USE_OPENAI:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    MODEL = "text-embedding-ada-002"

    def embed(texts):
        client = openai.OpenAI()
        rsp = client.embeddings.create(model=MODEL, input=texts)
        return [d.embedding for d in rsp.data]
else:
    _model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(texts):
        return _model.encode(texts, show_progress_bar=False).tolist()


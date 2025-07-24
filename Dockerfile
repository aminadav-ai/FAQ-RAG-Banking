# ---------- Production-ready Dockerfile ----------
# Build and run FAQ‑RAG‑Banking in a single lightweight image.
# Default = local MiniLM embeddings; switch to OpenAI at runtime:
#   docker run -e USE_OPENAI=true -e OPENAI_API_KEY=sk-... faq-rag

FROM python:3.12-slim AS base
LABEL maintainer="Aminadav"

# ‑‑ basic Python hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# ---------- install runtime deps ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- copy source ----------
COPY . .

# ---------- defaults ----------
ENV USE_OPENAI=false OPENAI_API_KEY=""

# Build vector store on first container start (if missing), then start CLI chat.
# In production you might replace this with API startup (uvicorn).
CMD bash -c "PYTHONPATH=./src python -m src.ingest && PYTHONPATH=./src python -m src.query"

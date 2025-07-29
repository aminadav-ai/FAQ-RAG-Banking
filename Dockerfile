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
COPY requirements-docker.txt .

RUN pip install --upgrade pip \
 && pip install --no-cache-dir --prefer-binary -r requirements-docker.txt

# ---------- copy source ----------
COPY . .

# ---------- defaults ----------
ENV USE_OPENAI=true

# Build vector store on first container start (if missing), then start CLI chat.
# In production you might replace this with API startup (uvicorn).
#CMD bash -c "PYTHONPATH=./src python3 -m src.ingest && PYTHONPATH=./src python3 -m src.query"

EXPOSE 8000
CMD sh -c "uvicorn src.api:app --host 0.0.0.0 --port 8000 --log-level info"


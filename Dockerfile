# ---------- Production-ready Dockerfile ----------
# Build and run FAQ‑RAG‑Banking in a single lightweight image.

FROM python:3.12-slim AS base
LABEL maintainer="Aminadav"

# ‑‑ basic Python hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# ---------- install runtime deps ----------
COPY requirements.txt .

RUN pip install --upgrade pip \
 && pip install --no-cache-dir --prefer-binary -r requirements.txt

# ---------- copy source ----------
COPY . .

EXPOSE 8000
CMD sh -c "uvicorn src.api:app --host 0.0.0.0 --port 8000 --log-level info"


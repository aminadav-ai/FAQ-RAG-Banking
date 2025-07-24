"""FastAPI layer for FAQ‑RAG‑Banking.

Run locally:
    uvicorn src.api:app --reload --host 0.0.0.0 --port 8000

Endpoints:
    GET /ask?q="your question here"  → { "question": ..., "answer": ... }

Uses the same vector store + embedding backend as the CLI.
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from query import fetch_answer   # re‑use existing helper

app = FastAPI(title="FAQ‑RAG‑Banking API", version="1.0")

# Allow localhost testing and simple public demos; tighten in prod.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)


@app.get("/", tags=["health"])
async def root():
    """Health‑check route."""
    return {"status": "ok"}


@app.get("/ask", tags=["qa"])
async def ask(q: str = Query(..., description="User banking question")):
    """Return a deterministic answer from the vector store."""
    answer = fetch_answer(q) or "No matching answer in knowledge base."
    return {"question": q, "answer": answer}

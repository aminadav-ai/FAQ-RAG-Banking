import logging
logger = logging.getLogger("uvicorn.error")

# …later, instead of print():
logger.info("Test logging from api.py")

import os
from pathlib import Path
from src.config import CHROMA_DIR

chroma_path = Path(CHROMA_DIR)
files = list(chroma_path.glob("*"))  

print(f"[debug] CHROMA_DIR: {chroma_path}")
for f in files:
    print("   ┗", f)

has_index = any("sqlite" in f.suffix for f in files)

if not has_index:
    print("[INFO] No index found → running ingest...")
    import src.ingest
else:
    print("[INFO] Index exists → skipping ingest.")
    
from pydantic import BaseModel
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from src.query import fetch_answer

app = FastAPI(title="FAQ‑RAG‑Banking API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],   
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    question: str
    answer: str

@app.get("/ask", response_model=Answer, tags=["qa"])
async def ask(q: str = Query(..., description="User banking question")):
    ans = fetch_answer(q) or "No matching answer in knowledge base."
    return {"question": q, "answer": ans}

@app.post("/query", response_model=Answer, tags=["qa"])
async def query(body: Question):
    ans = fetch_answer(body.question) or "No matching answer in knowledge base."
    return {"question": body.question, "answer": ans}


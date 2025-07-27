import logging
logger = logging.getLogger("uvicorn.error")
logging.basicConfig(level=logging.DEBUG)
logger.info("Test logging from api.py")

from pydantic import BaseModel
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from src.query import fetch_answer
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Lifespan startup")
    yield
    logger.info("🛑 Lifespan shutdown")
    
app = FastAPI(title="FAQ‑RAG‑Banking API", version="1.0", lifespan=lifespan)

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


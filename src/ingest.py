"""Ingest Banking FAQ docs into Chroma – 1 pair = 1 record."""

import shutil, os
if os.getenv("CLEAR_DB")=="true":
    shutil.rmtree("data/chroma_store", ignore_errors=True)

import uuid, re
from pathlib import Path
import chromadb
from config import CHROMA_DIR
from utils_text import normalize
from embeddings import embed

DATA_DIR = Path("data/raw")
client     = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection("banking_faq")

PAIR_RE = re.compile(r"\n\s*\n")          

def iter_pairs(text: str):
    text = text.replace("\r\n", "\n")     
    blocks = [b.strip() for b in PAIR_RE.split(text) if b.strip()]
    for i in range(0, len(blocks) - 1, 2):          
        q, a = blocks[i], blocks[i + 1]
        yield q, a

docs, metas, ids = [], [], []
for raw, src in ((p.read_text("utf-8"), str(p))
                 for p in DATA_DIR.rglob("*") if p.suffix.lower() in {".txt", ".md"}):
    for q, a in iter_pairs(raw):
        doc = normalize(f"{q} {a}")       
        docs.append(doc)
        metas.append({"answer": a, "source": src})
        ids.append(str(uuid.uuid4()))

if docs:
    collection.add(documents=docs,
                   metadatas=metas,
                   ids=ids,
                   embeddings=embed(docs))
    print(f"Indexed {len(docs)} Q&A pairs -> {CHROMA_DIR}")
else:
    print("No files found in data/raw/")


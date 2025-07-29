import logging
import shutil, os, uuid, re, json
from pathlib import Path

import chromadb
from src.utils_text import normalize
from src.embeddings import embed

logger = logging.getLogger("uvicorn.error")

DATA_DIR = Path("data/raw")

client = chromadb.HttpClient(
    host="chroma-server-cydq.onrender.com",
    port=443,
    ssl=True
)

collection_name = os.getenv("COLLECTION_NAME", "my-dev-faq")

# Clean slate — delete collection if it already exists
for c in client.list_collections():
    if c.name == collection_name:
        client.delete_collection(name=collection_name)
        break


collection = client.get_or_create_collection(collection_name)

docs, metas, ids = [], [], []

for path in DATA_DIR.rglob("*.json"):
    with path.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            for entry in data:
                q = entry.get("question", "").strip()
                a = entry.get("answer", "").strip()
                if q and a:
                    doc = normalize(f"{q} {a}")
                    docs.append(doc)
                    metas.append({
                        "answer": a,
                        "question": q,
                        "category": entry.get("category", ""),
                        "source": str(path)
                    })
                    ids.append(str(uuid.uuid4()))
        except Exception as e:
            logger.error(f"Failed to load {path}: {e}")

if docs:
    collection.add(
        documents=docs,
        metadatas=metas,
        ids=ids,
        embeddings=embed(docs)
    )
    print(f"Indexed {len(docs)} Q&A pairs")
else:
    print(f"No valid JSON files found in {DATA_DIR}")
    
total = collection.count()
print(f"Total in collection: {total}")


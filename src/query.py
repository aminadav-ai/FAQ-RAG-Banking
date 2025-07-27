import logging
logger = logging.getLogger("uvicorn.error")

# …later, instead of print():
logger.info("Test logging from query.py")

import chromadb
from src.utils_text import normalize

client = chromadb.HttpClient(
    host="chroma-server-cydq.onrender.com",
    port=443,
    ssl=True
)

import os
collection_name = os.getenv("COLLECTION_NAME", "my-dev-faq")
collection = client.get_or_create_collection(collection_name)

def fetch_answer(question: str):
    res = collection.query(
        query_texts=[normalize(question)],
        n_results=1,
        include=["metadatas"]
    )
    if res["metadatas"] and res["metadatas"][0]:
        return res["metadatas"][0][0]["answer"]
    return None



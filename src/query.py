import logging
import time
import os

import chromadb
from src.utils_text import normalize

logger = logging.getLogger(__name__)

CHROMA_HOST = "chroma-server-cydq.onrender.com"
CHROMA_PORT = 443
MAX_RETRIES = 30
WAIT_SECONDS = 5

# Lazy init (we'll set them below)
client = None
collection = None


def wait_for_chroma():
    global client, collection

    logger.debug(f"🔄 Connecting to ChromaDB at {CHROMA_HOST}:{CHROMA_PORT}...")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            client = chromadb.HttpClient(
                host=CHROMA_HOST,
                port=CHROMA_PORT,
                ssl=True
            )
            logger.debug(f"✅ Connected to ChromaDB on attempt {attempt}")
            return
        except Exception as e:   
            logger.warning(f"⏳ Attempt {attempt}/{MAX_RETRIES} failed: {e}")
            time.sleep(WAIT_SECONDS)

    logger.error("❌ Could not connect to ChromaDB after multiple attempts")
    raise RuntimeError("ChromaDB not available")


def fetch_answer(question: str):
    global client, collection
    if client is None:
        wait_for_chroma()

    collection_name = os.getenv("COLLECTION_NAME", "my-dev-faq")
    logger.debug(f"📁 Using collection: {collection_name}")
    collection = client.get_or_create_collection(collection_name)
    res = collection.query(
        query_texts=[normalize(question)],
        n_results=1,
        include=["metadatas"]
    )
    if res["metadatas"] and res["metadatas"][0]:
        return res["metadatas"][0][0]["answer"]
    return None


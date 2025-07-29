import logging
import os
from openai import OpenAI
from dotenv import load_dotenv
import chromadb
from src.utils_text import normalize

load_dotenv()

USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.75"))

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
        n_results=3,
        include=["metadatas", "distances"]
    )

    metadatas = res.get("metadatas", [[]])[0]
    distances = res.get("distances", [[]])[0]

    if metadatas and distances and distances[0] < SIMILARITY_THRESHOLD:
        logger.debug(f"✅ Chroma match with distance {distances[0]}")
        return metadatas[0]["answer"]

    # Fallback to OpenAI if enabled
    if USE_OPENAI and OPENAI_API_KEY:
        logger.debug(f"🤖 Falling back to OpenAI (model={OPENAI_MODEL})")

        # собираем весь контекст в prompt
        context_parts = [md["answer"] for md in metadatas if "answer" in md]
        context = "\n\n".join(context_parts)

        prompt = f"""
You are an expert AI assistant specialized in banking and finance.

Your job is to clearly and accurately answer the user's question.
Use the provided context if it's relevant.
If the answer is not in the context, explain it fully using your own knowledge.

Make sure the explanation is detailed and beginner-friendly.

Context:
{context}

Question: {question}
Answer:"""

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "user", "content": prompt.strip()}
            ],
            temperature=0.0
        )

        return response.choices[0].message.content.strip()

    logger.debug("⚠️ No good match found and OpenAI fallback disabled.")
    return None

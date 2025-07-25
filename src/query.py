import chromadb
from src.config import CHROMA_DIR
from src.embeddings import embed
from src.utils_text import normalize

from chromadb.config import Settings

settings = Settings(
    chroma_db_impl="duckdb+parquet",      # <-- use embedded DuckDB+Parquet
    persist_directory=CHROMA_DIR,
    anonymized_telemetry=False
)

client = chromadb.Client(settings=settings)
collection = client.get_or_create_collection("banking_faq")

def fetch_answer(question: str):
    emb = embed([normalize(question)])[0]
    res = collection.query(query_embeddings=[emb],
                           n_results=1,
                           include=["metadatas"])
    if res["metadatas"] and res["metadatas"][0]:
        return res["metadatas"][0][0]["answer"]
    return None

def main():
    print("Banking Q&A. Empty line to exit.")
    while True:
        q = input("Q: ").strip()
        if not q:
            break
        ans = fetch_answer(q)
        print("--- Answer ---")
        print(ans if ans else "No matching answer.")



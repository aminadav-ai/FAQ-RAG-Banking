import os
import chromadb
from src.embeddings import embed
from src.utils_text import normalize

client = chromadb.HttpClient(
    host="chroma-server-cydq.onrender.com",
    port=443,
    ssl=True
)
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
        print(ans if ans else "No matching answer")



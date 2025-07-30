import logging
import time

logging.getLogger().setLevel(logging.WARNING)

from src.query import fetch_answer

while True:
    question = input("Ask: ").strip()
    if not question:
        break

    start = time.time()
    answer = fetch_answer(question)
    end = time.time()

    print("Answer:", answer)
    print(f"Took {end - start:.2f} seconds\n")


# manual_test.py

import logging

logging.getLogger().setLevel(logging.WARNING)


from src.query import fetch_answer

while True:
    question = input("Ask: ").strip()
    if not question:
        break
    print("Answer:", fetch_answer(question))


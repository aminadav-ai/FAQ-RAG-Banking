# manual_test.py

from src.query import fetch_answer

while True:
    question = input("Ask: ").strip()
    if not question:
        break
    print("Answer:", fetch_answer(question))


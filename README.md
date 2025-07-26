# FAQ‑RAG-Banking ― Banking Q&A Chatbot
[![CI](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/tests.yml/badge.svg)](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/tests.yml)
[![Docker CI](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/docker-test.yml/badge.svg)](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/docker-test.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/aminadav-ai/FAQ-RAG-Banking.svg)](https://github.com/aminadav-ai/FAQ-RAG-Banking/commits/main)

**Portfolio Highlight – AI / NLP / Retrieval‑Augmented Generation**

This project demonstrates a Retrieval‑Augmented Generation (RAG) pipeline that answers banking questions with deterministic, citation‑ready responses.  
It is minimal, test-driven, and well-suited for factual chatbot use cases or AI search tools.

> **Stack**  Python | Sentence‑Transformers | ChromaDB Server | FastAPI | Docker

---

## ✨ Key Features

| Feature                       | What it does                                                          | Why it matters                                           |
|------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------|
| **Granular Q&A ingestion**   | Each *question + answer* pair is indexed as a single vector document. | Prevents multi‑answer leakage & keeps retrieval precise. |
| **Deterministic testing**    | `tests/qa_check.py` normalises answers and checks 12 key queries.     | Guarantees factual correctness without LLM randomness.   |
| **FastAPI interface**        | Simple REST API via `/query`                                          | Easy to deploy or integrate                              |
| **Docker & ChromaDB Server** | Runs entirely in Docker with ChromaDB server container                | Lightweight and portable                                 |

---

## 🐳 Quick Start (Docker)

```bash
git clone https://github.com/aminadav-ai/FAQ-RAG-Banking.git
cd FAQ-RAG-Banking

# Start FastAPI + ChromaDB Server
docker-compose up
```

→ Then query the API:

```http
POST http://localhost:8000/query
Content-Type: application/json

{
  "question": "What is APY?"
}
```

Example response:
```json
{
  "answer": "APY (Annual Percentage Yield) refers to the total amount of interest earned on a savings account in a year, expressed as a percentage."
}
```

---

## 🧪 Manual CLI Test (without API)

```bash
# Create environment
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Build index
PYTHONPATH=./src python3 -m src.ingest

# Run local test
PYTHONPATH=./src python3 manual_test.py
```

Example:
```
Q: What is a SEPA transfer?
--- Answer ---
SEPA (Single Euro Payments Area) is a low‑cost euro‑only transfer scheme used across the EU, EEA and select partners; SEPA Credit Transfers usually settle next business day and cost €0–1 for retail customers.
```

Run regression test:

```bash
PYTHONPATH=./src python3 -m tests.qa_check
# Summary: 12/12 passed.
```

---

## 📦 Optional: Using OpenAI Embeddings

```bash
export OPENAI_API_KEY="sk-..."   # Optional
export USE_OPENAI=true
PYTHONPATH=./src python3 -m src.ingest
```

Use this only if you'd like to experiment with ada-002 embeddings.

---

## 📂 Project Structure

```
.
├── assets/                 # Demo screenshots
├── data/raw/               # Plain‑text FAQ files
├── docker-compose.yml      # FastAPI + ChromaDB services
├── src/
│   ├── ingest.py           # Index creator
│   ├── query.py            # Internal module (no __main__)
│   ├── embeddings.py       # Backend switch: local/OpenAI
│   └── utils_text.py       # Cleanup, normalisation
├── manual_test.py          # CLI test wrapper
├── tests/qa_check.py       # Regression test suite
└── requirements.txt
```

---

## 📈 Extending the Knowledge Base

1. Add `data/raw/my_faq.txt` with Q/A pairs (Q then A, blank line between).
2. Run `PYTHONPATH=./src python3 -m src.ingest`.
3. Optionally expand `tests/qa_check.py`.

---

## 🙋‍♂️ Author & Context

Created by **Aminadav** as part of my AI/NLP portfolio  
Tested on **Ubuntu 24 + Docker + GitHub Actions**  
Supports both **API** and **CLI** usage — no OpenAI key required.

Feel free to ⭐ star or fork!

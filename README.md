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


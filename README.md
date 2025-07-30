# 💰 FAQ-RAG-Banking — AI-Powered Banking Q&A Chatbot

[![CI](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/tests.yml/badge.svg)](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/tests.yml)
[![Docker CI](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/docker-test.yml/badge.svg)](https://github.com/aminadav-ai/FAQ-RAG-Banking/actions/workflows/docker-test.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/aminadav-ai/FAQ-RAG-Banking.svg)](https://github.com/aminadav-ai/FAQ-RAG-Banking/commits/main)

🚀 **Live demo:** [Ask Banking AI on Render](https://faq-api-01l4.onrender.com)

---

## 🎯 Description

**FAQ-RAG-Banking** is an AI-powered question answering chatbot for banking-related topics.

- Users can ask questions through a simple web interface.
- The backend uses OpenAI API to generate high-quality answers.
- Built with FastAPI and Docker for easy deployment.

---

## 🧰 Tech Stack

> Python • FastAPI • OpenAI API • Docker • GitHub Actions

---

## ✨ Key Features

| Feature                | What it does                                              | Why it matters                                |
|------------------------|-----------------------------------------------------------|------------------------------------------------|
| Banking Q&A Chatbot    | Answers financial and banking-related questions           | Helps users get instant financial insights     |
| FastAPI Backend        | Handles questions via `/query` endpoint                   | Clean, fast, scalable API                     |
| OpenAI Integration     | Uses OpenAI Chat API (`gpt-4o-mini` recommended)           | Delivers rich, contextual responses           |
| Docker Support         | Containerized app with optional ChromaDB                 | Easy to deploy anywhere                       |
| GitHub Actions CI      | Automated tests and wakeup pings                          | Keeps API always ready                        |
| Render Hosting         | UI and API hosted online (see link above)                | Try without local setup                       |

---

## 📦 API Usage

### `POST /query`

**Request:**

```json
{
  "question": "What is APY?"
}
```

**Response:**

```json
{
  "answer": "APY stands for Annual Percentage Yield..."
}
```

---

## 🖥️ Web UI

The UI (`index.html`) is bundled inside the same repo and served at `/`.

Users can type a banking question and get an AI-generated answer.  
Response time is also displayed automatically.

---

## 🐳 Docker Usage

```bash
docker build -t faq-api .
docker run -p 8000:8000 faq-api
```

Then open: [http://localhost:8000](http://localhost:8000)

---

## ⚙️ Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=sk-xxx
OPENAI_MODEL=gpt-4o-mini
```

---

## 🧪 Local Manual Test

```bash
python manual_test.py
```

You can ask questions in terminal.

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

## 🙋‍♂️ Author

Maintained by [@aminadav-ai](https://github.com/aminadav-ai)

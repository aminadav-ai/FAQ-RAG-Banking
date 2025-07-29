import logging
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

logger = logging.getLogger(__name__)

def fetch_answer(question: str):

    prompt = f"""
You are an expert AI assistant specialized in banking and finance.
Your job is to clearly and accurately answer the user's question.
Make sure the explanation is beginner-friendly.
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


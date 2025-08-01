import logging
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

logger = logging.getLogger(__name__)

def fetch_answer(question: str):

    prompt = f"""
You are a helpful and knowledgeable assistant trained to answer questions **only about banking**. This includes topics such as:

- Bank accounts
- Credit cards
- Loans and mortgages
- Savings and interest rates
- Online banking and mobile apps
- Fees, policies, and financial regulations

If the user's question is not related to banking, politely respond with:
"I'm here to answer questions related to banking. Please ask something related to banking topics."

Now answer the following question:

{question}
"""

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "user", "content": prompt.strip()}
        ],
        temperature=0.5,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()


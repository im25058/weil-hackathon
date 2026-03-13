import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("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")
    )

    returm llm
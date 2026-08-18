import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()


# Get Groq API key
API_KEY = os.getenv("GROQ_API_KEY")


if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing from .env"
    )


# Create shared LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=API_KEY,
    temperature=0.3,
)
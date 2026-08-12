import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load environment variables
load_dotenv()


# Get API configuration
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL")


if not API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY is missing from .env"
    )


if not MODEL:
    raise ValueError(
        "OPENROUTER_MODEL is missing from .env"
    )


# Create shared LLM
llm = ChatOpenAI(
    model=MODEL,
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3,
)
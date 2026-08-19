import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()


def get_api_key():
    # 1. Check Streamlit Secrets first (for Streamlit Cloud)
    try:
        import streamlit as st
        if hasattr(st, "secrets"):
            if "GROQ_API_KEY" in st.secrets:
                return str(st.secrets["GROQ_API_KEY"]).strip().strip('"').strip("'")
            if "groq_api_key" in st.secrets:
                return str(st.secrets["groq_api_key"]).strip().strip('"').strip("'")
    except Exception:
        pass

    # 2. Check OS environment variables (.env)
    key = os.getenv("GROQ_API_KEY") or os.getenv("groq_api_key")
    if key:
        return str(key).strip().strip('"').strip("'")

    return None


API_KEY = get_api_key()

if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Please set GROQ_API_KEY in .env (locally) or in Streamlit Secrets (on Streamlit Cloud)."
    )


# Create shared LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=API_KEY,
    temperature=0.3,
)
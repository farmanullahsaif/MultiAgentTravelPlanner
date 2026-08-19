import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()


# Get Groq API key (check os.getenv first, then streamlit secrets)
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    try:
        import streamlit as st
        if "GROQ_API_KEY" in st.secrets:
            API_KEY = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

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
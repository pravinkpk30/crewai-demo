from crew import LLM
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini LLM
gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1,
    api_key=os.getenv("GOOGLE_API_KEY")
)

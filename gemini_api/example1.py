import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv() ## meaning of this --> this will load the .env file from the current directory and set the environment variables

GEMINI_API_KEY = os.getenv ("GEMINI_API_KEY")  # This will return None if the environment variable is not set
if GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY





llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)
messages = [
    (
        "system",
        "You are a helpful assistant.",
    ),
    ("human", "who is narendra modi?."),
]

response=llm.invoke(messages)
print(response.content) 
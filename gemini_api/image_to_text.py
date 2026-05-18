import os
import base64
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv() ## meaning of this --> this will load the .env file from the current directory and set the environment variables

GEMINI_API_KEY = os.getenv ("GEMINI_API_KEY")  # This will return None if the environment variable is not set
if GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY


# 1. Image ko base64 me convert karo
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("D:\krish-naik-gen-ai-classes\gen-ai-class\gemini_api\dogs.png")

# 2. Gemini model initialize karo
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY
)

# 3. Text + image message banao
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Describe this image in detail."
        },
        {
            "type": "image_url",
            "image_url": f"data:image/png;base64,{base64_image}"
        }
    ]
)


# 4. Model invoke karo
response = llm.invoke([message])

print(response.content)
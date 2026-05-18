import os
from google import genai
from google.genai import types
import wave
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv() ## meaning of this --> this will load the .env file from the current directory and set the environment variables

GEMINI_API_KEY = os.getenv ("GEMINI_API_KEY")  # This will return None if the environment variable is not set
if GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts", #freely accessible model for text to speech conversion
    contents="Hello students, today we are learning multimodal AI.and you are in sunny savita class wheere he is teaching you multimodal ai.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Kore"
                )
            )
        )
    )
)

audio_data = response.candidates[0].content.parts[0].inline_data.data

with wave.open("output.wav", "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    wf.writeframes(audio_data)

print("Audio saved as output.wav")
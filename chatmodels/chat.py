from dotenv import load_dotenv
import os

load_dotenv()


# Switch to Mistral via langchain_mistralai (free tier access).
from langchain_mistralai import ChatMistralAI

# Ensure your .env has MISTRAL_API_KEY set.
mistral_key = os.getenv("MISTRAL_API_KEY")
if not mistral_key:
    raise RuntimeError("MISTRAL_API_KEY is required in environment")

# Initialize Mistral model (community / small model)
chat = ChatMistralAI(
    model="mistral-small-latest",
    api_key=mistral_key,
    temperature=0.2, # varies between 0 and 1, higher values make output more random,
    #use lower values for more focused and deterministic output.   
    max_tokens=20
)
response = chat.invoke("Write a poem on mistral small latest model.")
print(response.content)



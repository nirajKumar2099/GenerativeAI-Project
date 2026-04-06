"""
Example script using all four AI models: OpenAI, Groq, Google, and Mistral
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

print("=" * 60)
print("Testing All Four AI Models with LangChain")
print("=" * 60)

# Test message
test_message = "What is the capital of France? Answer in one sentence."

# ============================================
# 1. OpenAI (GPT-4 or GPT-3.5)
# ============================================
print("\n1️⃣  OPENAI MODEL")
print("-" * 60)
try:
    llm_openai = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=OPENAI_API_KEY,
        temperature=0.7
    )
    response = llm_openai.invoke(test_message)
    print(f"Response: {response.content}")
except Exception as e:
    print(f"❌ Error: {e}")

# ============================================
# 2. Groq
# ============================================
print("\n2️⃣  GROQ MODEL")
print("-" * 60)
try:
    llm_groq = ChatGroq(
        model="mixtral-8x7b-32768",
        api_key=GROQ_API_KEY,
        temperature=0.7
    )
    response = llm_groq.invoke(test_message)
    print(f"Response: {response.content}")
except Exception as e:
    print(f"❌ Error: {e}")

# ============================================
# 3. Google Generative AI
# ============================================
print("\n3️⃣  GOOGLE GENERATIVE AI MODEL")
print("-" * 60)
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(test_message)
    print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")

# ============================================
# 4. Mistral AI
# ============================================
print("\n4️⃣  MISTRAL AI MODEL")
print("-" * 60)
try:
    llm_mistral = ChatMistralAI(
        model="mistral-small-latest",
        api_key=MISTRAL_API_KEY,
        temperature=0.7
    )
    response = llm_mistral.invoke(test_message)
    print(f"Response: {response.content}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 60)
print("✓ All models tested!")
print("=" * 60)

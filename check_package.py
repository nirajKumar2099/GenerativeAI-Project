import subprocess
import sys

packages = {
    'langchain': ['langchain'],
    'langchain_core': ['langchain_core'],
    'langchain_community': ['langchain_community'],
    'langgraph': ['langgraph'],
    'langchain_openai': ['langchain_openai'],
    'google_generativeai': ['google.generativeai'],
    'langchain_groq': ['langchain_groq'],
    'langchain_mistralai': ['langchain_mistralai'],
    'python_dotenv': ['dotenv'],
    'faiss_cpu': ['faiss'],
    'tiktoken': ['tiktoken'],
    'fastapi': ['fastapi'],
    'uvicorn': ['uvicorn'],
    'requests': ['requests']
}

for name, import_names in packages.items():
    installed = False
    for import_name in import_names:
        try:
            __import__(import_name)
            installed = True
            break
        except ImportError:
            continue
    
    if installed:
        print(f"✓ {name} is installed")
    else:
        print(f"✗ {name} is NOT installed")
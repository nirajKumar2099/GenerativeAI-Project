from dotenv import load_dotenv
import os
load_dotenv()

# Hugging Face free embedding model, you can also use HuggingFaceEndpoint for paid models
# need to install sentence-transformers to use the all-MiniLM-L6-v2 model, which is a popular model for generating sentence embeddings. 
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2", # this is a free model for generating embeddings,
    #you can also use other models from Hugging Face that are suitable for your use case.
)

vector = embeddings.embed_query("What is the capital of India ?")
print(vector)

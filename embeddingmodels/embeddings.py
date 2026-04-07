from dotenv import load_dotenv
import os
# Open AI paid embedding , if you face any error except code error -- might be billing/credit issue
from langchain_openai import OpenAIEmbeddings
load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",   # OpenAI paid models, but you can also use free models like "text-embedding-3-small" or "text-embedding-3-mini"
    dimensions=64 # the dimension of the embedding vector, which can be 64, 128, 256, or 512 depending on the model you choose.
)
vector = embeddings.embed_query("What is the capital of India ?")
print(vector)
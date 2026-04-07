from dotenv import load_dotenv
import os
load_dotenv()
#opensource hugging face model, you can also use HuggingFacePipeline for local model,
# but here we are using HuggingFaceEndpoint to call the model via API,
# which is not free to use, but you can create local model in Hugging Face and use it for free.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
   repo_id="deepseek-ai/DeepSeek-R1", # this is not free to use , will create local model in 
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is my name?")

print(response.content)
# **Note: The HuggingFaceEndpoint is a wrapper around the Hugging Face Inference API, which allows you to call Hugging Face models directly from your code. You need to have an access token from Hugging Face to use this service, which you can set in your .env file as shown above.*  
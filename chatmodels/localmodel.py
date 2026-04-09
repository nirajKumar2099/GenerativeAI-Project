from dotenv import load_dotenv
import os
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# need to install transformers and huggingface_hub to use HuggingFacePipeline,
# and ******huggingfacepipeline use for local model******, while HuggingFaceEndpoint
# is for calling Hugging Face models via API.


llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen3-0.6B",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 256,          # reduce for speed
        "do_sample": True,              # enable better responses
        "temperature": 0.7,             # creativity
        "top_p": 0.9,                   # nucleus sampling
        "repetition_penalty": 1.1,      # avoid repetition
        "return_full_text": False       # important for chatbot behavior
    },
)

chat_model = ChatHuggingFace(llm=llm)
prompt = input("Enter your prompt: ")
response = chat_model.invoke(prompt)
print(response.content)
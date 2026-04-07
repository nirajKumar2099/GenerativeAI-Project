from dotenv import load_dotenv
import os
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# need to install transformers and huggingface_hub to use HuggingFacePipeline,
# and ******huggingfacepipeline use for local model******, while HuggingFaceEndpoint
# is for calling Hugging Face models via API.

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen3-0.6B", # this is a free model for text generation
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),
)

chat_model = ChatHuggingFace(llm=llm)
response = chat_model.invoke("What is the capital of India ?")
print(response.content)
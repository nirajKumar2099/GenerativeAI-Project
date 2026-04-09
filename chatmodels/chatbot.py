from dotenv import load_dotenv
import os

load_dotenv()


# Switch to Mistral via langchain_mistralai (free tier access).
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage # to handle hallucinations and maintain conversation context

# Ensure your .env has MISTRAL_API_KEY set.
mistral_key = os.getenv("MISTRAL_API_KEY")
if not mistral_key:
    raise RuntimeError("MISTRAL_API_KEY is required in environment")

# Initialize Mistral model (community / small model) *mistral-small-latest
chat = ChatMistralAI(
    model="mistral-tiny", 
    api_key=mistral_key,
    temperature=0.2, # varies between 0 and 1, higher values make output more random,
    #use lower values for more focused and deterministic output.   
    max_tokens=100
)
# this code is only for 1 query at a time 
'''You can also create a loop to allow multiple queries in a single session, like this:'''
# while True:
#     prompt = input("Enter your prompt (or 'quit' to exit): ")
#     if prompt.lower() == "quit":
#         break
#     response = chat.invoke(prompt)
#     print(f"Bot Reply: {response.content}")


greet = input("Hi There!, Do you want to chat ? (yes/no): ")
flag = True
if greet.lower() == "exit" or greet.lower() == "no":
    flag = False
    print("GoodBye!")
else:
     print("************* Welcome to Mistral Small Latest Chatbot! *************")  
     
message = [
    SystemMessage(content="You are a helpful assistant.")
]     
    
while flag != False:
    
     prompt = input(f"You :Enter your prompt (or 'exit' to quit): ")
     message.append(HumanMessage(content=prompt)) # we are appending the user prompt to the message list to maintain the conversation context.
     if prompt.lower() == "exit" or prompt.lower() == "no":
            print("GoodBye!")
     else:
        response = chat.invoke(message) # instead of prompt variable in chat.invoke(),
        # we are passing the entire message list to maintain the context of the conversation.
        # This way, the model can generate responses based on the entire conversation history 
        # rather than just the latest prompt.
        message.append(AIMessage(content=response.content))
        print(f"Bot Reply: {response.content}")   
                    
     
  



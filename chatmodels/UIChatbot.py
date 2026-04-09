import streamlit as st
from dotenv import load_dotenv
import os
import uuid

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment variables
load_dotenv()
mistral_key = os.getenv("MISTRAL_API_KEY")

if not mistral_key:
    st.error("MISTRAL_API_KEY not found in .env")
    st.stop()

# Initialize model
chat = ChatMistralAI(
    model="mistral-tiny",
    api_key=mistral_key,
    temperature=0.2,
    max_tokens=100
)

# Page config
st.set_page_config(page_title="FreeChatbot AI", page_icon="🤖", layout="wide")

# ------------------ SESSION STATE ------------------

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "chat_titles" not in st.session_state:
    st.session_state.chat_titles = {}

if "current_chat" not in st.session_state:
    chat_id = str(uuid.uuid4())
    st.session_state.current_chat = chat_id
    st.session_state.chats[chat_id] = [
        SystemMessage(content="You are a helpful assistant.")
    ]
    st.session_state.chat_titles[chat_id] = "New Chat"

# ------------------ SIDEBAR ------------------

st.sidebar.title("🤖 FreeChatbot AI")

# New Chat Button
if st.sidebar.button("➕ New Chat"):
    new_chat_id = str(uuid.uuid4())
    st.session_state.current_chat = new_chat_id
    st.session_state.chats[new_chat_id] = [
        SystemMessage(content="You are a helpful assistant.")
    ]
    st.session_state.chat_titles[new_chat_id] = "New Chat"

st.sidebar.subheader("💬 Chat History")

# Show chat list
for chat_id in st.session_state.chats.keys():
    title = st.session_state.chat_titles.get(chat_id, "New Chat")

    if st.sidebar.button(title, key=chat_id):
        st.session_state.current_chat = chat_id

# ------------------ MAIN CHAT ------------------

st.title("💬 FreeChatbot AI")

messages = st.session_state.chats[st.session_state.current_chat]

# Display messages
for msg in messages[1:]:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# ------------------ INPUT ------------------

user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)

    # Add user message
    messages.append(HumanMessage(content=user_input))

    # 🔥 AUTO TITLE (first message only)
    if len(messages) == 2:  # System + first user message
        try:
            title_prompt = f"Generate a short 3-5 word title for this: {user_input}"
            title_response = chat.invoke(title_prompt)
            title = title_response.content.strip()

            # fallback safety
            if len(title) > 40:
                title = title[:40]

            st.session_state.chat_titles[st.session_state.current_chat] = title
        except:
            # fallback if API fails
            st.session_state.chat_titles[st.session_state.current_chat] = user_input[:30]

    # Get bot response
    response = chat.invoke(messages)

    # Show response
    st.chat_message("assistant").write(response.content)

    # Save response
    messages.append(AIMessage(content=response.content))


# NOTE : run streamlit app: streamlit run chatmodels/UIChatbot.py
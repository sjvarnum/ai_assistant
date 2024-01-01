import logging
import streamlit as st

from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from streamlit_chat import message

# Setting up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv(find_dotenv(), override=True)

st.set_page_config(page_title="AI Assistant")
st.subheader("AI Assistant ")

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, max_tokens=500)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set up sidebar
with st.sidebar:
    system_message = st.text_area(
        label="System role (optional)", placeholder="System message..", height=100
    )
    user_prompt = st.text_area(
        label="Send a message", placeholder="Message AI Assistant..", height=200
    )

    if system_message:
        if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(SystemMessage(content=system_message))

    if user_prompt:
        st.session_state.messages.append(HumanMessage(content=user_prompt))

        with st.spinner("Working..."):
            response = chat(st.session_state.messages)

        st.session_state.messages.append(AIMessage(content=response.content))

# If there are no messages in the session state, add a system message
# Add default system message if the user didn't enter one
if len(st.session_state.messages) >= 1:
    if not isinstance(st.session_state.messages[0], SystemMessage):
        st.session_state.messages.insert(
            0, SystemMessage(content="You are a helpful assistant.")
        )

# Iterate over the messages in the session state
for i, msg in enumerate(st.session_state.messages):
    # If the message is from the user
    if isinstance(msg, HumanMessage):
        message(msg.content, is_user=True, key=f"msg_{i}")
    # If the message is from the AI assistant
    elif isinstance(msg, AIMessage):
        message(msg.content, is_user=False, key=f"msg_{i}")

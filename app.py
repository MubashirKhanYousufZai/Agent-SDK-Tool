import streamlit as st
from agent_sdk.agent import Agent
from agent_sdk.tools import echo, calculator, greeting

# Initialize the agent
agent = Agent("HelperBot", tools=[echo, calculator, greeting])

st.set_page_config(page_title="Agent SDK UI", page_icon="🤖")
st.title("🤖 Agent SDK Tool")
st.markdown("Chat with your custom AI agent.")

# Chat history (Session state)
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
query = st.chat_input("Say something...")

if query:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": query})

    # Run agent and get reply
    response = agent.run(query)

    # Save agent message
    st.session_state.messages.append({"role": "agent", "content": response})

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

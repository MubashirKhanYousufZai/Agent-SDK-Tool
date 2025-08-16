import streamlit as st
from agent_sdk.tools import load_tools
from agent_sdk.agent import Agent


def main():
    st.title("🤖 Agent SDK Tool")
    tools = load_tools()
    agent = Agent(tools)

    query = st.text_input("Enter your query:", "")

    if st.button("Run"):
        if query:
            response = agent.process(query)
            st.write("**Agent:**", response)


if __name__ == "__main__":
    main()

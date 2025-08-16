from agent_sdk.agent import Agent
from agent_sdk.tools import echo, calculator, greeting, exit_tool_instance

def main():
    agent = Agent("Agent")
    agent.add_tool(echo)
    agent.add_tool(calculator)
    agent.add_tool(greeting)
    agent.add_tool(exit_tool_instance)

    print("🤖 Agent SDK Tool Running... (type 'bye' or 'khudahafiz' to exit)")
    while True:
        query = input("You: ")
        response = agent.run(query)
        print("Agent:", response)

        if exit_tool_instance.can_handle(query):
            break

if __name__ == "__main__":
    main()

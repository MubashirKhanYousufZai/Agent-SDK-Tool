from agent_sdk.agent import Agent
from agent_sdk.tools import echo, calculator, greeting

agent = Agent("HelperBot", tools=[echo, calculator, greeting])

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = agent.run(query)
    print("Agent:", response)

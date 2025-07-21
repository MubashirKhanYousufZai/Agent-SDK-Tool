class Agent:
    def __init__(self, name, tools=None):
        self.name = name
        self.tools = tools if tools else []

    def add_tool(self, tool):
        self.tools.append(tool)

    def run(self, query):
        for tool in self.tools:
            if tool.can_handle(query):
                return tool.execute(query)
        return f"{self.name}: Sorry, I don't know how to handle that."

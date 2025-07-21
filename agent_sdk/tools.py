class Tool:
    def __init__(self, name, trigger, func):
        self.name = name
        self.trigger = trigger  # Could be a keyword or list of keywords
        self.func = func

    def can_handle(self, query):
        if isinstance(self.trigger, str):
            return self.trigger in query.lower()
        if isinstance(self.trigger, list):
            return any(keyword in query.lower() for keyword in self.trigger)
        return False

    def execute(self, query):
        return self.func(query)

# Echo tool
def echo_tool(query):
    return f"Echo: {query}"

echo = Tool("EchoTool", "echo", echo_tool)

# Calculator tool
def calculator_tool(query):
    try:
        expression = query.lower().replace("calculate", "").strip()
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

calculator = Tool("CalculatorTool", "calculate", calculator_tool)

# Greeting tool
def greeting_tool(query):
    return "Hi there! I'm your AI Agent. How can I help you today?"

greeting = Tool("GreetingTool", ["hi", "hello", "hey", "salam"], greeting_tool)

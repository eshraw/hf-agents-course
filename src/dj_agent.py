from smolagents import CodeAgent, tool, DuckDuckGoSearchTool, HfApiModel
from login import login_huggingface

login_huggingface()

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel()
    )

agent.run("Search for the best music for a party at the Wayne Manor")
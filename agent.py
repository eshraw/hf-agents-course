from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

login()

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel()
    )

agent.run("Search for the best music for a party at the Wayne Manor")
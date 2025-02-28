from smolagents import CodeAgent, tools, HfApiModel
from login import login_huggingface

login_huggingface()

@tool
def suggest_menu(occasion: str) -> str:
    """Suggest a menu for a given occasion.
    Args:
        occasion: The occasion for which to suggest a menu
    """

    if occasion == "casual dinner party":
        return "We suggest a menu with a main course of steak and a side of mashed potatoes."
    elif occasion == "black tie dinner party":
        return "We suggest a menu with a main course of lobster and a side of asparagus."
    else:
        return "Custom menu for the butler"

agent = CodeAgent(
    tools=[suggest_menu],
    model=HfApiModel()
    )

agent.run("Suggest a menu for a formal dinner party")
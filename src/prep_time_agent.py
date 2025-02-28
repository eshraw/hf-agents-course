from smolagents import CodeAgent, tool, HfApiModel
from login import login_huggingface
import numpy as np
import time
import datetime

login_huggingface()

agent = CodeAgent(
    tools=[],
    model=HfApiModel(),
    additional_authorized_imports=["numpy", "time", "datetime"]
    )

agent.push_to_hub("Eshraw/prep_time_agent")

agent.run(
    """
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """
)
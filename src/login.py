from huggingface_hub import login
from dotenv import load_dotenv
import os

def login_huggingface():
    # Load environment variables from .env file
    load_dotenv()
    #Get token from environment variable
    token = os.getenv("HUGGINGFACE_TOKEN")
    if token:
        login(token)
    else:
        raise ValueError("HUGGINGFACE_TOKEN not found in .env file")

import os
from dotenv import load_dotenv

# load from .env
load_dotenv()

API_KEY = os.getenv("API_KEY") # you need to make your own .env file in the project directory that includes your own API_KEY variable
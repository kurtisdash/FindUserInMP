import os
from dotenv import load_dotenv

# Load from .env
load_dotenv()

API_KEY = os.getenv("API_KEY") # You need to make your own .env file in the project directory that includes your own API_KEY variable
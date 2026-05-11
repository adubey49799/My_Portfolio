from pathlib import Path
from dotenv import load_dotenv
import os

# Project root = use_cases/meteoblue
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Load .env file
env_path = PROJECT_ROOT / ".env"
load_dotenv(env_path)

api_key = os.getenv("METEOBLUE_API_KEY")

if not api_key:
    raise ValueError("METEOBLUE_API_KEY was not found. Please check your .env file.")

print("Meteoblue API key loaded successfully.")
print("Project root:", PROJECT_ROOT)

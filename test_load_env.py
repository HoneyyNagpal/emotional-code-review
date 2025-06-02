from dotenv import load_dotenv
import os
from pathlib import Path

print("Current directory:", Path(__file__).parent.resolve())

env_path = Path(__file__).parent / '.env'
print("Loading .env from:", env_path)

load_dotenv(dotenv_path=env_path)

token = os.getenv("GITHUB_TOKEN")
print("GITHUB_TOKEN:", token)

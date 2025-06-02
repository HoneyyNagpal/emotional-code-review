from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

print("GitHub Token:", os.getenv("GITHUB_TOKEN"))


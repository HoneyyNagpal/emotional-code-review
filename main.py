from fastapi import FastAPI, Query
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import joblib  # ✅ for your custom model
from fastapi.middleware.cors import CORSMiddleware

# Load .env file
print("FastAPI cwd:", os.getcwd())
env_path = Path(__file__).parent / '.env'
print("Loading .env from:", env_path)

load_dotenv(dotenv_path=env_path)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("GitHub Token:", GITHUB_TOKEN)

# Set up FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load your own fine-tuned model
model = joblib.load("emotion_classifier.joblib")

# ✅ Prediction function
def analyze_emotion(message: str) -> str:
    return model.predict([message])[0]

@app.get("/")
def read_root():
    return {"message": "Hello, Emotional Code Review!"}

@app.get("/commits/")
def get_commits(owner: str = Query(...), repo: str = Query(...)):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch commits"}

    commits = response.json()
    results = []

    for commit in commits[:10]:  # or more if you want
        message = commit['commit']['message']
        proba = model.predict_proba([message])[0]  # array of probabilities per class
        max_idx = proba.argmax()
        emotion_label = model.classes_[max_idx]
        confidence = proba[max_idx]

        results.append({
            "message": message,
            "emotion": emotion_label,
            "score": round(confidence, 2)
        })

    return {"commit_analysis": results}

import csv
import random

# Define base messages and emotions
emotions = ["joy", "anger", "fear", "neutral", "surprise"]
base_messages = {
    "joy": [
        "Add user feedback form",
        "Improve UI responsiveness",
        "Add support for dark mode",
        "Enhance dashboard layout",
        "Add animations to navigation",
    ],
    "anger": [
        "Fix memory leak in main module",
        "Resolve deadlock in multi-threading",
        "Fix critical bug causing crash",
        "Fix security vulnerability in login",
        "Fix bug causing data loss",
    ],
    "fear": [
        "Unexpected error when parsing JSON",
        "Handle crash on invalid input",
        "Fix null pointer in production",
        "Avoid breaking change in release",
        "Crash when loading large files",
    ],
    "neutral": [
        "Update dependencies",
        "Refactor CSS styles",
        "Improve API rate limiting",
        "Rename variables for clarity",
        "Update README documentation",
    ],
    "surprise": [
        "Enable experimental feature toggle",
        "Allow `nonce` for hoistable styles",
        "Add support for unknown config flags",
        "Sudden behavior change on update",
        "Log unexpected network response",
    ]
}

# Create synthetic dataset with 1000+ rows
rows = []
for i in range(200):  # 200 * 5 = 1000 rows
    for emotion in emotions:
        message = random.choice(base_messages[emotion])
        variation = f"{message} #{random.randint(1000, 9999)}"
        rows.append([variation, emotion])

# Write to CSV
with open("commit_emotions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["commit_message", "emotion"])
    writer.writerows(rows)

print("✅ Generated 'commit_emotions.csv' with 1000+ labeled messages.")

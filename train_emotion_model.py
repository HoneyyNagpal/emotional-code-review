import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load dataset
df = pd.read_csv("commit_emotions.csv")

# Drop rows with missing data if any
df.dropna(inplace=True)

# Features and labels
X = df['commit_message']
y = df['emotion']

# Create model pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X, y)

# Save the model to disk
joblib.dump(model, 'emotion_classifier.joblib')

print("✅ Model trained and saved as 'emotion_classifier.joblib'")

import pandas as pd

# Load the CSV
df = pd.read_csv("commit_emotions.csv")

# Print the first 5 rows
print(df.head())
print(f"Total rows: {len(df)}")

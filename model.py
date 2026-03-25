import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# load data
df = pd.read_csv("data.csv")

X = df.drop("Result", axis=1)
y = df["Result"]

# train model
model = RandomForestClassifier()
model.fit(X, y)

# SAVE MODEL 
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
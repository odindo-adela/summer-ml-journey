import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

df["Assists Per Match"] = df["Assists"] / df["Matches"]

X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier())
])

score = cross_val_score(
    pipeline,
    X,y,
    cv=5,
    scoring="accuracy"
).mean()

print("Accuracy: ", score)

pipeline.fit(X,y)

saved_pipeline = joblib.dump(pipeline, "elite_pipeline.pkl")

loaded_pipeline = joblib.load("elite_pipeline.pkl")

matches = int(input("Enter number of Matches: "))
assists = int(input("Enter number of Assists: "))
position = input("Enter Position(Forward/Winger):").capitalize()

position = {
    "Forward":1,
    "Winger":2
}[position]

prediction = loaded_pipeline.predict([[matches,assists,position]])
if prediction[0]==1:
    print("Elite Player")
else:
    print("Not Elite Player")

probabilities = loaded_pipeline.predict_proba([[matches,assists,position]])
print("\nProbability: ", probabilities)

confidence = probabilities[0][prediction[0]]
confidence *= 100

print(f"Confidence:{confidence:.2f}%")


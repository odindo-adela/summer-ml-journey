import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

model = DecisionTreeClassifier(max_depth=3, random_state=42)

model.fit(X,y)

joblib.dump(
    model,
    "elite_player_model.pk1")

print("Model saved successfully!")

loaded_model = joblib.load("elite_player_model.pkl")

print("Model loaded successfully")

prediction = loaded_model.predict([[24,10,1]])

if prediction[0] == 1:
    print("Elite Player")
else:
    print("Not Elite Player")